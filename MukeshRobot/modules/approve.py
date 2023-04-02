import html

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode, Update
from telegram.error import BadRequest
from telegram.ext import CallbackContext, CallbackQueryHandler, run_async
from telegram.utils.helpers import mention_html

import MukeshRobot.modules.sql.approve_sql as sql
from MukeshRobot import DRAGONS, dispatcher
from MukeshRobot.modules.disable import DisableAbleCommandHandler
from MukeshRobot.modules.helper_funcs.chat_status import user_admin
from MukeshRobot.modules.helper_funcs.extraction import extract_user
from MukeshRobot.modules.log_channel import loggable


@loggable
@user_admin
@run_async
def approve(update, context):
    message = update.effective_message
    chat_title = message.chat.title
    chat = update.effective_chat
    args = context.args
    user = update.effective_user
    user_id = extract_user(message, args)
    if not user_id:
        message.reply_text(
            "I don't know who you're talking about, you're going to need to specify a user!"
        )
        return ""
    try:
        member = chat.get_member(user_id)
    except BadRequest:
        return ""
    if member.status == "administrator" or member.status == "creator":
        message.reply_text(
            "User is already admin - locks, blocklists, and antiflood already don't apply to them."
        )
        return ""
    if sql.is_approved(message.chat_id, user_id):
        message.reply_text(
            f"[{member.user['first_name']}](tg://user?id={member.user['id']}) is already approved in {chat_title}",
            parse_mode=ParseMode.MARKDOWN,
        )
        return ""
    sql.approve(message.chat_id, user_id)
    message.reply_text(
        f"[{member.user['first_name']}](tg://user?id={member.user['id']}) has been approved in {chat_title}! They will now be ignored by automated admin actions like locks, blocklists, and antiflood.",
        parse_mode=ParseMode.MARKDOWN,
    )
    log_message = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#APPROVED\n"
        f"<b>Admin:</b> {mention_html(user.id, user.first_name)}\n"
        f"<b>User:</b> {mention_html(member.user.id, member.user.first_name)}"
    )

    return log_message


@loggable
@user_admin
@run_async
def disapprove(update, context):
    message = update.effective_message
    chat_title = message.chat.title
    chat = update.effective_chat
    args = context.args
    user = update.effective_user
    user_id = extract_user(message, args)
    if not user_id:
        message.reply_text(
            "I don't know who you're talking about, you're going to need to specify a user!"
        )
        return ""
    try:
        member = chat.get_member(user_id)
    except BadRequest:
        return ""
    if member.status == "administrator" or member.status == "creator":
        message.reply_text("This user is an admin, they can't be unapproved.")
        return ""
    if not sql.is_approved(message.chat_id, user_id):
        message.reply_text(f"{member.user['first_name']} isn't approved yet!")
        return ""
    sql.disapprove(message.chat_id, user_id)
    message.reply_text(
        f"{member.user['first_name']} is no longer approved in {chat_title}."
    )
    log_message = (
        f"<b>{html.escape(chat.title)}:</b>\n"
        f"#UNAPPROVED\n"
        f"<b>Admin:</b> {mention_html(user.id, user.first_name)}\n"
        f"<b>User:</b> {mention_html(member.user.id, member.user.first_name)}"
    )

    return log_message


@user_admin
@run_async
def approved(update, context):
    message = update.effective_message
    chat_title = message.chat.title
    chat = update.effective_chat
    msg = "The following users are approved.\n"
    approved_users = sql.list_approved(message.chat_id)
    for i in approved_users:
        member = chat.get_member(int(i.user_id))
        msg += f"- `{i.user_id}`: {member.user['first_name']}\n"
    if msg.endswith("approved.\n"):
        message.reply_text(f"No users are approved in {chat_title}.")
        return ""
    else:
        message.reply_text(msg, parse_mode=ParseMode.MARKDOWN)


@user_admin
@run_async
def approval(update, context):
    message = update.effective_message
    chat = update.effective_chat
    args = context.args
    user_id = extract_user(message, args)
    member = chat.get_member(int(user_id))
    if not user_id:
        message.reply_text(
            "I don't know who you're talking about, you're going to need to specify a user!"
        )
        return ""
    if sql.is_approved(message.chat_id, user_id):
        message.reply_text(
            f"{member.user['first_name']} is an approved user. Locks, antiflood, and blocklists won't apply to them."
        )
    else:
        message.reply_text(
            f"{member.user['first_name']} is not an approved user. They are affected by normal commands."
        )


@run_async
def unapproveall(update: Update, context: CallbackContext):
    chat = update.effective_chat
    user = update.effective_user
    member = chat.get_member(user.id)
    if member.status != "creator" and user.id not in DRAGONS:
        update.effective_message.reply_text(
            "Only the chat owner can unapprove all users at once."
        )
    else:
        buttons = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="📍Unapprove all users📍", callback_data="unapproveall_user"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="📍Cancel📍", callback_data="unapproveall_cancel"
                    )
                ],
            ]
        )
        update.effective_message.reply_text(
            f"Are you sure you would like to unapprove ALL users in {chat.title}? This action cannot be undone.",
            reply_markup=buttons,
            parse_mode=ParseMode.MARKDOWN,
        )


@run_async
def unapproveall_btn(update: Update, context: CallbackContext):
    query = update.callback_query
    chat = update.effective_chat
    message = update.effective_message
    member = chat.get_member(query.from_user.id)
    if query.data == "unapproveall_user":
        if member.status == "creator" or query.from_user.id in DRAGONS:
            approved_users = sql.list_approved(chat.id)
            users = [int(i.user_id) for i in approved_users]
            for user_id in users:
                sql.disapprove(chat.id, user_id)

        if member.status == "administrator":
            query.answer("Only owner of the chat can do this.📍")

        if member.status == "member":
            query.answer("You need to be admin to do this.📍")
    elif query.data == "unapproveall_cancel":
        if member.status == "creator" or query.from_user.id in DRAGONS:
            message.edit_text("Removing of all approved users has been cancelled.📍")
            return ""
        if member.status == "administrator":
            query.answer("Only owner of the chat can do this.📍")
        if member.status == "member":
            query.answer("You need to be admin to do this.📍")


__help__ = """
sᴏᴍᴇᴛɪᴍᴇs, ʏᴏᴜ ᴍɪɢʜᴛ ᴛʀᴜsᴛ ᴀ ᴜsᴇʀ ɴᴏᴛ ᴛᴏ sᴇɴᴅ ᴜɴᴡᴀɴᴛᴇᴅ ᴄᴏɴᴛᴇɴᴛ.
ᴍᴀʏʙᴇ ɴᴏᴛ ᴇɴᴏᴜɢʜ ᴛᴏ ᴍᴀᴋᴇ ᴛʜᴇᴍ ᴀᴅᴍɪɴ, ʙᴜᴛ ʏᴏᴜ ᴍɪɢʜᴛ ʙᴇ ᴏᴋ ᴡɪᴛʜ ʟᴏᴄᴋs, ʙʟᴀᴄᴋʟɪsᴛs, ᴀɴᴅ ᴀɴᴛɪғʟᴏᴏᴅ ɴᴏᴛ ᴀᴘᴘʟʏɪɴɢ ᴛᴏ ᴛʜᴇᴍ.

ᴛʜᴀᴛ's ᴡʜᴀᴛ ᴀᴘᴘʀᴏᴠᴀʟs ᴀʀᴇ ғᴏʀ - ᴀᴘᴘʀᴏᴠᴇ ᴏғ ᴛʀᴜsᴛᴡᴏʀᴛʜʏ ᴜsᴇʀs ᴛᴏ ᴀʟʟᴏᴡ ᴛʜᴇᴍ ᴛᴏ sᴇɴᴅ 

*ᴀᴅᴍɪɴ ᴄᴏᴍᴍᴀɴᴅs:*
❍ /approval*:* ᴄʜᴇᴄᴋ ᴀ ᴜsᴇʀ's ᴀᴘᴘʀᴏᴠᴀʟ sᴛᴀᴛᴜs ɪɴ ᴛʜɪs ᴄʜᴀᴛ.
❍ /approve *:* ᴀᴘᴘʀᴏᴠᴇ ᴏғ ᴀ ᴜsᴇʀ. ʟᴏᴄᴋs, ʙʟᴀᴄᴋʟɪsᴛs, ᴀɴᴅ ᴀɴᴛɪғʟᴏᴏᴅ ᴡᴏɴ'ᴛ ᴀᴘᴘʟʏ ᴛᴏ ᴛʜᴇᴍ ᴀɴʏᴍᴏʀᴇ.
❍ /unapprove *:* ᴜɴᴀᴘᴘʀᴏᴠᴇ ᴏғ ᴀ ᴜsᴇʀ. ᴛʜᴇʏ ᴡɪʟʟ ɴᴏᴡ ʙᴇ sᴜʙᴊᴇᴄᴛ ᴛᴏ ʟᴏᴄᴋs, ʙʟᴀᴄᴋʟɪsᴛs, ᴀɴᴅ ᴀɴᴛɪғʟᴏᴏᴅ ᴀɢᴀɪɴ.
❍ /approved *:* ʟɪsᴛ ᴀʟʟ ᴀᴘᴘʀᴏᴠᴇᴅ ᴜsᴇʀs.
❍ /unapproveall *:* ᴜɴᴀᴘᴘʀᴏᴠᴇ *ᴀʟʟ* ᴜsᴇʀs ɪɴ ᴀ ᴄʜᴀᴛ. ᴛʜɪs ᴄᴀɴɴᴏᴛ ʙᴇ ᴜɴᴅᴏɴᴇ.

☆............𝙱𝚈 » [𝚅𝙸𝙿 𝙱𝙾𝚈](https://t.me/the_vip_boy)............☆
"""

APPROVE = DisableAbleCommandHandler("approve", approve)
DISAPPROVE = DisableAbleCommandHandler("unapprove", disapprove)
APPROVED = DisableAbleCommandHandler("approved", approved)
APPROVAL = DisableAbleCommandHandler("approval", approval)
UNAPPROVEALL = DisableAbleCommandHandler("unapproveall", unapproveall)
UNAPPROVEALL_BTN = CallbackQueryHandler(unapproveall_btn, pattern=r"unapproveall_.*")

dispatcher.add_handler(APPROVE)
dispatcher.add_handler(DISAPPROVE)
dispatcher.add_handler(APPROVED)
dispatcher.add_handler(APPROVAL)
dispatcher.add_handler(UNAPPROVEALL)
dispatcher.add_handler(UNAPPROVEALL_BTN)

__mod_name__ = "♨️Aᴘᴘʀᴏᴠᴇ♨️"
__command_list__ = ["approve", "unapprove", "approved", "approval"]
__handlers__ = [APPROVE, DISAPPROVE, APPROVED, APPROVAL]
