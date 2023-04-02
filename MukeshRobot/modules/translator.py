from gpytranslate import SyncTranslator
from telegram import ParseMode, Update
from telegram.ext import CallbackContext

from MukeshRobot import dispatcher
from MukeshRobot.modules.disable import DisableAbleCommandHandler

trans = SyncTranslator()


def totranslate(update: Update, context: CallbackContext) -> None:
    message = update.effective_message
    reply_msg = message.reply_to_message
    if not reply_msg:
        message.reply_text(
            "ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇs ᴏʀ ᴡʀɪᴛᴇ ᴍᴇssᴀɢᴇs ғʀᴏᴍ ᴏᴛʜᴇʀ ʟᴀɴɢᴜᴀɢᴇs ​​ғᴏʀ ᴛʀᴀɴsʟᴀᴛɪɴɢ ɪɴᴛᴏ ᴛʜᴇ ɪɴᴛᴇɴᴅᴇᴅ ʟᴀɴɢᴜᴀɢᴇ\ɴ\ɴ"
            "ᴇxᴀᴍᴘʟᴇ: `/tr ᴇɴ-ʜɪ` ᴛᴏ ᴛʀᴀɴsʟᴀᴛᴇ ғʀᴏᴍ ᴇɴɢʟɪsʜ ᴛᴏ ʜɪɴᴅɪ\ɴ"
            "ᴏʀ ᴜsᴇ: `/tr en` ғᴏʀ ᴀᴜᴛᴏᴍᴀᴛɪᴄ ᴅᴇᴛᴇᴄᴛɪᴏɴ ᴀɴᴅ ᴛʀᴀɴsʟᴀᴛɪɴɢ ɪᴛ ɪɴᴛᴏ ᴇɴɢʟɪsʜ.\ɴ"
            "ᴄʟɪᴄᴋ ʜᴇʀᴇ ᴛᴏ sᴇᴇ [ʟɪsᴛ ᴏғ ᴀᴠᴀɪʟᴀʙʟᴇ ʟᴀɴɢᴜᴀɢᴇ ᴄᴏᴅᴇs](https://t.me/mukeshbotzone/16).",
            parse_mode="markdown",
            disable_web_page_preview=True,
        )
        return
    if reply_msg.caption:
        to_translate = reply_msg.caption
    elif reply_msg.text:
        to_translate = reply_msg.text
    try:
        args = message.text.split()[1].lower()
        if "//" in args:
            source = args.split("//")[0]
            dest = args.split("//")[1]
        else:
            source = trans.detect(to_translate)
            dest = args
    except IndexError:
        source = trans.detect(to_translate)
        dest = "en"
    translation = trans(to_translate, sourcelang=source, targetlang=dest)
    reply = (
        f"<b>ᴛʀᴀɴsʟᴀᴛᴇᴅ ғʀᴏᴍ {source} ᴛᴏ {dest}</b> :\n"
        f"<code>{translation.text}</code>"
    )

    message.reply_text(reply, parse_mode=ParseMode.HTML)


__help__ = """
 ❍ /tr  /tl (ʟᴀɴɢᴜᴀɢᴇ ᴄᴏᴅᴇ) ᴀs ʀᴇᴘʟʏ ᴛᴏ ᴀ ʟᴏɴɢ ᴍᴇssᴀɢᴇ
*ᴇxᴀᴍᴘʟᴇ:* 
 ❍ /tr en*:* ᴛʀᴀɴsʟᴀᴛᴇs sᴏᴍᴇᴛʜɪɴɢ ᴛᴏ ᴇɴɢʟɪsʜ
 ❍ /tr hi-en*:* ᴛʀᴀɴsʟᴀᴛᴇs ʜɪɴᴅɪ ᴛᴏ ᴇɴɢʟɪsʜ

*ʟᴀɴɢᴜᴀɢᴇ ᴄᴏᴅᴇs*
`af,am,ar,az,be,bg,bn,bs,ca,ceb,co,cs,cy,da,de,el,en,eo,es,
et,eu,fa,fi,fr,fy,ga,gd,gl,gu,ha,haw,hi,hmn,hr,ht,hu,hy,
id,ig,is,it,iw,ja,jw,ka,kk,km,kn,ko,ku,ky,la,lb,lo,lt,lv,mg,mi,mk,
ml,mn,mr,ms,mt,my,ne,nl,no,ny,pa,pl,ps,pt,ro,ru,sd,si,sk,sl,
sm,sn,so,sq,sr,st,su,sv,sw,ta,te,tg,th,tl,tr,uk,ur,uz,
vi,xh,yi,yo,zh,zh_CN,zh_TW,zu`

☆............𝙱𝚈 » [𝚅𝙸𝙿 𝙱𝙾𝚈](https://t.me/the_vip_boy)............☆
"""
__mod_name__ = "⚡Tʀᴀɴs⚡"

TRANSLATE_HANDLER = DisableAbleCommandHandler(["tr", "tl"], totranslate)

dispatcher.add_handler(TRANSLATE_HANDLER)

__command_list__ = ["tr", "tl"]
__handlers__ = [TRANSLATE_HANDLER]
