import html
import os

import nekos
import requests
from PIL import Image
from telegram import Update
from telegram.error import BadRequest, RetryAfter, Unauthorized
from telegram.ext import CallbackContext, CommandHandler, run_async
from telegram.utils.helpers import mention_html

import MukeshRobot.modules.sql.nsfw_sql as sql
from MukeshRobot import dispatcher
from MukeshRobot.modules.helper_funcs.chat_status import user_admin
from MukeshRobot.modules.helper_funcs.filters import CustomFilters
from MukeshRobot.modules.log_channel import gloggable


@run_async
@user_admin
@gloggable
def add_nsfw(update: Update, context: CallbackContext):
    chat = update.effective_chat
    msg = update.effective_message
    user = update.effective_user
    is_nsfw = sql.is_nsfw(chat.id)
    if not is_nsfw:
        sql.set_nsfw(chat.id)
        msg.reply_text("ᴀᴄᴛɪᴠᴀᴛɪᴏɴ ɴsғᴡ ᴍᴏᴅᴇ!")
        message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"ᴀᴄᴛɪᴠᴀᴛᴇᴅ_ɴsғᴡ\n"
            f"<b>ᴀᴅᴍɪɴ:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        )
        return message
    else:
        msg.reply_text("ɴsғᴡ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ғᴏʀ ᴛʜɪs ᴄʜᴀᴛ")
        return ""


@run_async
@user_admin
@gloggable
def rem_nsfw(update: Update, context: CallbackContext):
    msg = update.effective_message
    chat = update.effective_chat
    user = update.effective_user
    is_nsfw = sql.is_nsfw(chat.id)
    if not is_nsfw:
        msg.reply_text("ɴsғᴡ ᴍᴏᴅᴇ ɪs ᴀʟʀᴇᴀᴅʏ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ")
        return ""
    else:
        sql.rem_nsfw(chat.id)
        msg.reply_text("ʀᴏʟʟᴇᴅ ʙᴀᴄᴋ ᴛᴏ ɴsғᴡ ᴍᴏᴅᴇ")
        message = (
            f"<b>{html.escape(chat.title)}:</b>\n"
            f"ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇᴅ_ɴsғᴡ\n"
            f"<b>Admin:</b> {mention_html(user.id, html.escape(user.first_name))}\n"
        )
        return message


def list_nsfw_chats(update: Update, context: CallbackContext):
    chats = sql.get_all_nsfw_chats()
    text = "<b>ɴsғᴡ ᴀᴄᴛɪᴠᴀᴛᴇᴅ ᴄʜᴀᴛs</b>\n"
    for chat in chats:
        try:
            x = context.bot.get_chat(int(*chat))
            name = x.title if x.title else x.first_name
            text += f"• <code>{name}</code>\n"
        except BadRequest:
            sql.rem_nsfw(*chat)
        except Unauthorized:
            sql.rem_nsfw(*chat)
        except RetryAfter as e:
            sleep(e.retry_after)
    update.effective_message.reply_text(text, parse_mode="HTML")


def neko(update, context):
    msg = update.effective_message
    target = "neko"
    msg.reply_photo(nekos.img(target))


def feet(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "feet"
    msg.reply_photo(nekos.img(target))


def yuri(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "yuri"
    msg.reply_photo(nekos.img(target))


def trap(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "trap"
    msg.reply_photo(nekos.img(target))


def futanari(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "futanari"
    msg.reply_photo(nekos.img(target))


def hololewd(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "hololewd"
    msg.reply_photo(nekos.img(target))


def lewdkemo(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "lewdkemo"
    msg.reply_photo(nekos.img(target))


def sologif(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "solog"
    msg.reply_video(nekos.img(target))


def feetgif(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "feetg"
    msg.reply_video(nekos.img(target))


def cumgif(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "cum"
    msg.reply_video(nekos.img(target))


def erokemo(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "erokemo"
    msg.reply_photo(nekos.img(target))


def lesbian(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "les"
    msg.reply_video(nekos.img(target))


def wallpaper(update, context):
    msg = update.effective_message
    target = "wallpaper"
    msg.reply_photo(nekos.img(target))


def lewdk(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "lewdk"
    msg.reply_photo(nekos.img(target))


def ngif(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "ngif"
    msg.reply_video(nekos.img(target))


def tickle(update, context):
    msg = update.effective_message
    target = "tickle"
    msg.reply_video(nekos.img(target))


def lewd(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "lewd"
    msg.reply_photo(nekos.img(target))


def feed(update, context):
    msg = update.effective_message
    target = "feed"
    msg.reply_video(nekos.img(target))


def eroyuri(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "eroyuri"
    msg.reply_photo(nekos.img(target))


def eron(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "eron"
    msg.reply_photo(nekos.img(target))


def cum(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "cum_jpg"
    msg.reply_photo(nekos.img(target))


def bjgif(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "bj"
    msg.reply_video(nekos.img(target))


def bj(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "blowjob"
    msg.reply_photo(nekos.img(target))


def nekonsfw(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "nsfw_neko_gif"
    msg.reply_video(nekos.img(target))


def solo(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "solo"
    msg.reply_photo(nekos.img(target))


def kemonomimi(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "kemonomimi"
    msg.reply_photo(nekos.img(target))


def avatarlewd(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "nsfw_avatar"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    msg.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")


def gasm(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "gasm"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    msg.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")


def poke(update, context):
    msg = update.effective_message
    target = "poke"
    msg.reply_video(nekos.img(target))


def anal(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "anal"
    msg.reply_video(nekos.img(target))


def hentai(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "hentai"
    msg.reply_photo(nekos.img(target))


def avatar(update, context):
    msg = update.effective_message
    target = "nsfw_avatar"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    msg.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")


def erofeet(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "erofeet"
    msg.reply_photo(nekos.img(target))


def holo(update, context):
    msg = update.effective_message
    target = "holo"
    msg.reply_photo(nekos.img(target))


def keta(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "keta"
    if not target:
        msg.reply_text("No URL was received from the API!")
        return
    msg.reply_photo(nekos.img(target))


def pussygif(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "pussy"
    msg.reply_video(nekos.img(target))


def tits(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "tits"
    msg.reply_photo(nekos.img(target))


def holoero(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "holoero"
    msg.reply_photo(nekos.img(target))


def pussy(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "pussy_jpg"
    msg.reply_photo(nekos.img(target))


def hentaigif(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "random_hentai_gif"
    msg.reply_video(nekos.img(target))


def classic(update, context):
    msg = update.effective_message
    target = "classic"
    msg.reply_video(nekos.img(target))


def kuni(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "kuni"
    msg.reply_video(nekos.img(target))


def waifu(update, context):
    msg = update.effective_message
    target = "waifu"
    with open("temp.png", "wb") as f:
        f.write(requests.get(nekos.img(target)).content)
    img = Image.open("temp.png")
    img.save("temp.webp", "webp")
    msg.reply_document(open("temp.webp", "rb"))
    os.remove("temp.webp")


def kiss(update, context):
    msg = update.effective_message
    target = "kiss"
    msg.reply_video(nekos.img(target))


def femdom(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "femdom"
    msg.reply_photo(nekos.img(target))


def hug(update, context):
    msg = update.effective_message
    target = "cuddle"
    msg.reply_video(nekos.img(target))


def erok(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "erok"
    msg.reply_photo(nekos.img(target))


def foxgirl(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "fox_girl"
    msg.reply_photo(nekos.img(target))


def titsgif(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "boobs"
    msg.reply_video(nekos.img(target))


def ero(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    target = "ero"
    msg.reply_photo(nekos.img(target))


def smug(update, context):
    msg = update.effective_message
    target = "smug"
    msg.reply_video(nekos.img(target))


def baka(update, context):
    msg = update.effective_message
    target = "baka"
    msg.reply_video(nekos.img(target))


def dva(update, context):
    chat_id = update.effective_chat.id
    if not update.effective_message.chat.type == "private":
        is_nsfw = sql.is_nsfw(chat_id)
        if not is_nsfw:
            return
    msg = update.effective_message
    nsfw = requests.get("https://api.computerfreaker.cf/v1/dva").json()
    url = nsfw.get("url")
    # do shit with url if you want to
    if not url:
        msg.reply_text("No URL was received from the API!")
        return
    msg.reply_photo(url)


ADD_NSFW_HANDLER = CommandHandler("addnsfw", add_nsfw)
REMOVE_NSFW_HANDLER = CommandHandler("rmnsfw", rem_nsfw)
LIST_NSFW_CHATS_HANDLER = CommandHandler(
    "nsfwchats", list_nsfw_chats, filters=CustomFilters.dev_filter
)
LEWDKEMO_HANDLER = CommandHandler("lewdkemo", lewdkemo)
NEKO_HANDLER = CommandHandler("neko", neko)
FEET_HANDLER = CommandHandler("feet", feet)
YURI_HANDLER = CommandHandler("yuri", yuri)
TRAP_HANDLER = CommandHandler("trap", trap)
FUTANARI_HANDLER = CommandHandler("futanari", futanari)
HOLOLEWD_HANDLER = CommandHandler("hololewd", hololewd)
SOLOGIF_HANDLER = CommandHandler("sologif", sologif)
CUMGIF_HANDLER = CommandHandler("cumgif", cumgif)
EROKEMO_HANDLER = CommandHandler("erokemo", erokemo)
LESBIAN_HANDLER = CommandHandler("lesbian", lesbian)
WALLPAPER_HANDLER = CommandHandler("wallpaper", wallpaper)
LEWDK_HANDLER = CommandHandler("lewdk", lewdk)
NGIF_HANDLER = CommandHandler("ngif", ngif)
TICKLE_HANDLER = CommandHandler("tickle", tickle)
LEWD_HANDLER = CommandHandler("lewd", lewd)
FEED_HANDLER = CommandHandler("feed", feed)
EROYURI_HANDLER = CommandHandler("eroyuri", eroyuri)
ERON_HANDLER = CommandHandler(
    "eron",
    eron,
)
CUM_HANDLER = CommandHandler("cum", cum)
BJGIF_HANDLER = CommandHandler("bjgif", bjgif)
BJ_HANDLER = CommandHandler("bj", bj)
NEKONSFW_HANDLER = CommandHandler("nekonsfw", nekonsfw)
SOLO_HANDLER = CommandHandler("solo", solo)
KEMONOMIMI_HANDLER = CommandHandler("kemonomimi", kemonomimi)
AVATARLEWD_HANDLER = CommandHandler("avatarlewd", avatarlewd)
GASM_HANDLER = CommandHandler("gasm", gasm)
POKE_HANDLER = CommandHandler("poke", poke)
ANAL_HANDLER = CommandHandler("anal", anal)
HENTAI_HANDLER = CommandHandler("hentai", hentai)
AVATAR_HANDLER = CommandHandler("avatar", avatar)
EROFEET_HANDLER = CommandHandler("erofeet", erofeet)
HOLO_HANDLER = CommandHandler("holo", holo)
TITS_HANDLER = CommandHandler("tits", tits)
PUSSYGIF_HANDLER = CommandHandler("pussygif", pussygif)
HOLOERO_HANDLER = CommandHandler("holoero", holoero)
PUSSY_HANDLER = CommandHandler("pussy", pussy)
HENTAIGIF_HANDLER = CommandHandler("hentaigif", hentaigif)
CLASSIC_HANDLER = CommandHandler("classic", classic)
KUNI_HANDLER = CommandHandler("kuni", kuni)
WAIFU_HANDLER = CommandHandler("waifu", waifu)
LEWD_HANDLER = CommandHandler("lewd", lewd)
KISS_HANDLER = CommandHandler("kiss", kiss)
FEMDOM_HANDLER = CommandHandler("femdom", femdom)
CUDDLE_HANDLER = CommandHandler("hug", hug)
EROK_HANDLER = CommandHandler("erok", erok)
FOXGIRL_HANDLER = CommandHandler("foxgirl", foxgirl)
TITSGIF_HANDLER = CommandHandler("titsgif", titsgif)
ERO_HANDLER = CommandHandler("ero", ero)
SMUG_HANDLER = CommandHandler("smug", smug)
BAKA_HANDLER = CommandHandler("baka", baka)
DVA_HANDLER = CommandHandler("dva", dva)


dispatcher.add_handler(ADD_NSFW_HANDLER)
dispatcher.add_handler(REMOVE_NSFW_HANDLER)
dispatcher.add_handler(LIST_NSFW_CHATS_HANDLER)
dispatcher.add_handler(LEWDKEMO_HANDLER)
dispatcher.add_handler(NEKO_HANDLER)
dispatcher.add_handler(FEET_HANDLER)
dispatcher.add_handler(YURI_HANDLER)
dispatcher.add_handler(TRAP_HANDLER)
dispatcher.add_handler(FUTANARI_HANDLER)
dispatcher.add_handler(HOLOLEWD_HANDLER)
dispatcher.add_handler(SOLOGIF_HANDLER)
dispatcher.add_handler(CUMGIF_HANDLER)
dispatcher.add_handler(EROKEMO_HANDLER)
dispatcher.add_handler(LESBIAN_HANDLER)
dispatcher.add_handler(WALLPAPER_HANDLER)
dispatcher.add_handler(LEWDK_HANDLER)
dispatcher.add_handler(NGIF_HANDLER)
dispatcher.add_handler(TICKLE_HANDLER)
dispatcher.add_handler(LEWD_HANDLER)
dispatcher.add_handler(FEED_HANDLER)
dispatcher.add_handler(EROYURI_HANDLER)
dispatcher.add_handler(ERON_HANDLER)
dispatcher.add_handler(CUM_HANDLER)
dispatcher.add_handler(BJGIF_HANDLER)
dispatcher.add_handler(BJ_HANDLER)
dispatcher.add_handler(NEKONSFW_HANDLER)
dispatcher.add_handler(SOLO_HANDLER)
dispatcher.add_handler(KEMONOMIMI_HANDLER)
dispatcher.add_handler(AVATARLEWD_HANDLER)
dispatcher.add_handler(GASM_HANDLER)
dispatcher.add_handler(POKE_HANDLER)
dispatcher.add_handler(ANAL_HANDLER)
dispatcher.add_handler(HENTAI_HANDLER)
dispatcher.add_handler(AVATAR_HANDLER)
dispatcher.add_handler(EROFEET_HANDLER)
dispatcher.add_handler(HOLO_HANDLER)
dispatcher.add_handler(TITS_HANDLER)
dispatcher.add_handler(PUSSYGIF_HANDLER)
dispatcher.add_handler(HOLOERO_HANDLER)
dispatcher.add_handler(PUSSY_HANDLER)
dispatcher.add_handler(HENTAIGIF_HANDLER)
dispatcher.add_handler(CLASSIC_HANDLER)
dispatcher.add_handler(KUNI_HANDLER)
dispatcher.add_handler(WAIFU_HANDLER)
dispatcher.add_handler(LEWD_HANDLER)
dispatcher.add_handler(KISS_HANDLER)
dispatcher.add_handler(FEMDOM_HANDLER)
dispatcher.add_handler(CUDDLE_HANDLER)
dispatcher.add_handler(EROK_HANDLER)
dispatcher.add_handler(FOXGIRL_HANDLER)
dispatcher.add_handler(TITSGIF_HANDLER)
dispatcher.add_handler(ERO_HANDLER)
dispatcher.add_handler(SMUG_HANDLER)
dispatcher.add_handler(BAKA_HANDLER)
dispatcher.add_handler(DVA_HANDLER)

__handlers__ = [
    ADD_NSFW_HANDLER,
    REMOVE_NSFW_HANDLER,
    LIST_NSFW_CHATS_HANDLER,
    NEKO_HANDLER,
    FEET_HANDLER,
    YURI_HANDLER,
    TRAP_HANDLER,
    FUTANARI_HANDLER,
    HOLOLEWD_HANDLER,
    SOLOGIF_HANDLER,
    CUMGIF_HANDLER,
    EROKEMO_HANDLER,
    LESBIAN_HANDLER,
    WALLPAPER_HANDLER,
    LEWDK_HANDLER,
    NGIF_HANDLER,
    TICKLE_HANDLER,
    LEWD_HANDLER,
    FEED_HANDLER,
    EROYURI_HANDLER,
    ERON_HANDLER,
    CUM_HANDLER,
    BJGIF_HANDLER,
    BJ_HANDLER,
    NEKONSFW_HANDLER,
    SOLO_HANDLER,
    KEMONOMIMI_HANDLER,
    AVATARLEWD_HANDLER,
    GASM_HANDLER,
    POKE_HANDLER,
    ANAL_HANDLER,
    HENTAI_HANDLER,
    AVATAR_HANDLER,
    EROFEET_HANDLER,
    HOLO_HANDLER,
    TITS_HANDLER,
    PUSSYGIF_HANDLER,
    HOLOERO_HANDLER,
    PUSSY_HANDLER,
    HENTAIGIF_HANDLER,
    CLASSIC_HANDLER,
    KUNI_HANDLER,
    WAIFU_HANDLER,
    LEWD_HANDLER,
    KISS_HANDLER,
    FEMDOM_HANDLER,
    LEWDKEMO_HANDLER,
    CUDDLE_HANDLER,
    EROK_HANDLER,
    FOXGIRL_HANDLER,
    TITSGIF_HANDLER,
    ERO_HANDLER,
    SMUG_HANDLER,
    BAKA_HANDLER,
    DVA_HANDLER,
]
__mod_name__ = "⚡ɴsғᴡ⚡"

__help__ = """
*ɴsғᴡ:*
❂ /addnsfw  : ᴇɴᴀʙʟᴇ ɴsғᴡ ᴍᴏᴅᴇ
❂ /rmnsfw  : ᴅɪsᴀʙʟᴇ ɴsғᴡ ᴍᴏᴅᴇ
 
*ᴀᴠᴀɪʟᴀʙʟᴇ ᴄᴏᴍᴍᴀɴᴅs:*  
❂ /neko : sᴇɴᴅs ʀᴀɴᴅᴏᴍ sғᴡ ɴᴇᴋᴏ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /feet : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴀɴɪᴍᴇ ғᴇᴇᴛ ɪᴍᴀɢᴇs.
❂ /yuri : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ʏᴜʀɪ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /trap : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴛʀᴀᴘ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /futanari : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ғᴜᴛᴀɴᴀʀɪ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /hololewd : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ʜᴏʟᴏ ʟᴇᴡᴅs.
❂ /lewdkemo : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴋᴇᴍᴏ ʟᴇᴡᴅs.
❂ /sologif : sᴇɴᴅs ʀᴀɴᴅᴏᴍ sᴏʟᴏ ɢɪғs.
❂ /cumgif : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴄᴜᴍ ɢɪғs.
❂ /erokemo : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴇʀᴏ-ᴋᴇᴍᴏ ɪᴍᴀɢᴇs.
❂ /lesbian : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ʟᴇs sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /lewdk : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴋɪᴛsᴜɴᴇ ʟᴇᴡᴅs.
❂ /ngif : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ɴᴇᴋᴏ ɢɪғs.
❂ /tickle : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴛɪᴄᴋʟᴇ ɢɪғs.
❂ /lewd : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ʟᴇᴡᴅs.
❂ /feed : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ғᴇᴇᴅɪɴɢ ɢɪғs.
❂ /eroyuri : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴇʀᴏ-ʏᴜʀɪ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /eron : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴇʀᴏ-ɴᴇᴋᴏ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /cum : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴄᴜᴍ ɪᴍᴀɢᴇs.
❂ /bjgif : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ʙʟᴏᴡ ᴊᴏʙ ɢɪғs.
❂ /bj : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ʙʟᴏᴡ ᴊᴏʙ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /nekonsfw : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ɴsғᴡ ɴᴇᴋᴏ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /solo : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ɴsғᴡ ɴᴇᴋᴏ ɢɪғs.
❂ /kemonomimi : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴋᴇᴍᴏɴᴏᴍɪᴍɪ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /avatarlewd : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴀᴠᴀᴛᴇʀ ʟᴇᴡᴅ sᴛɪᴄᴋᴇʀs.
❂ /gasm : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴏʀɢᴀsᴍ sᴛɪᴄᴋᴇʀs.
❂ /poke : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴘᴏᴋᴇ ɢɪғs.
❂ /anal : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴀɴᴀʟ ɢɪғs.
❂ /hentai : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ʜᴇɴᴛᴀɪ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /avatar : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴀᴠᴀᴛᴀʀ sᴛɪᴄᴋᴇʀs.
❂ /erofeet : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴇʀᴏ-ғᴇᴇᴛ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /holo : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ʜᴏʟᴏ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /tits : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴛɪᴛs sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /pussygif : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴘᴜssʏ ɢɪғs.
❂ /holoero : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴇʀᴏ-ʜᴏʟᴏ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /pussy : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴘᴜssʏ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /hentaigif : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ʜᴇɴᴛᴀɪ ɢɪғs.
❂ /classic : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴄʟᴀssɪᴄ ʜᴇɴᴛᴀɪ ɢɪғs.
❂ /kuni : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴘᴜssʏ ʟɪᴄᴋ ɢɪғs.
❂ /waifu : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴡᴀɪғᴜ sᴛɪᴄᴋᴇʀs.
❂ /kiss : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴋɪssɪɴɢ ɢɪғs.
❂ /femdom : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ғᴇᴍᴅᴏᴍ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /cuddle : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴄᴜᴅᴅʟᴇ ɢɪғs.
❂ /erok : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴇʀᴏ-ᴋɪᴛsᴜɴᴇ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /foxgirl : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ғᴏxɢɪʀʟ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /titsgif : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴛɪᴛs ɢɪғs.
❂ /ero : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴇʀᴏ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.
❂ /smug : sᴇɴᴅs ʀᴀɴᴅᴏᴍ sᴍᴜɢ ɢɪғs.
❂ /baka : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ʙᴀᴋᴀ sʜᴏᴜᴛ ɢɪғs.
❂ /dva : sᴇɴᴅs ʀᴀɴᴅᴏᴍ ᴅ.ᴠᴀ sᴏᴜʀᴄᴇ ɪᴍᴀɢᴇs.


☆............𝙱𝚈 » [𝚅𝙸𝙿 𝙱𝙾𝚈](https://t.me/the_vip_boy)............☆"""
