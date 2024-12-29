from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from RishuMusic import app
from config import BOT_USERNAME
from RishuMusic.utils.errors import capture_err
import httpx 
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_txt = """
**
┌┬─────────────────⦿
│├─────────────────╮
│├ ᴛɢ ɴᴀᴍᴇ - ʀɪsʜᴜ sᴀɴᴀᴛᴀɴɪ
│├ ʀᴇᴀʟ ɴᴀᴍᴇ - ʀɪsʜᴜ ʀᴀᴊᴘᴜᴛ
│├─────────────────╯
├┼─────────────────⦿
├┤~ @RishuNetwork
├┤~ @Ur_rishu_143
├┤~ @Vip_robotz
├┼─────────────────⦿
│├─────────────────╮
│├OWNER│ @Rishu1286
│├─────────────────╯
└┴─────────────────⦿
**
"""




@app.on_message(filters.command("owner"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("Ｒ I Տ ᕼ ᑌ ", url=f"https://t.me/Rishu1286")
        ],
        [
          InlineKeyboardButton("ＨＥＬＰ", url="https://t.me/rishu1286"),
          InlineKeyboardButton("ＲＥＰＯ", url="https://github.com/RishuBot/RishuManagement"),
          ],
               [
                InlineKeyboardButton(" ＮＥＴＷＯＲＫ", url=f"https://t.me/ur_rishu_143"),
],
[
InlineKeyboardButton("ＯＦＦＩＣＩＡＬ ＢＯＴ", url=f"https://t.me/vip_music_vc_bot"),

        ]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo="https://envs.sh/oKU.jpg",
        caption=start_txt,
        reply_markup=reply_markup
    )
