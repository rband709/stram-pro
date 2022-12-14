# (c) adarsh-goel 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

if MY_PASS:
            buttonz=ReplyKeyboardMarkup(
            [
                ["startโก๏ธ","help๐"]
                        
            ],
            resize_keyboard=True
        )
else:
            buttonz=ReplyKeyboardMarkup(
            [
                ["startโก๏ธ","help๐"]
                        
            ],
            resize_keyboard=True
        )

            
            
@StreamBot.on_message((filters.command("start") | filters.regex('startโก๏ธ')) & filters.private )
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**Nแดแดก Usแดส Jแดษชษดแดแด:** \n\n__Mส Nแดแดก Fสษชแดษดแด__ [{m.from_user.first_name}](tg://user?id={m.from_user.id}) __Sแดแดสแดแดแด Yแดแดส Bแดแด !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="__๐ข๐๐ก๐ก๐จ, ๐จ๐๐ค ๐๐ก๐ ๐๐ก๐ ๐๐๐๐๐๐ ๐๐ก๐๐ ๐ค๐ข๐๐๐ ๐๐. ๐แดษดแดแดแดแด แดสแด ๐แดแด แดสแดแดแดส__\n\n  **๐๐ ๐ฌ๐๐ก๐ก ๐๐๐ก๐ฅ ๐ฎ๐ค๐ช**",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://telegra.ph/file/68259e3c723b935e22e69.jpg",
                caption="<i>๐น๐พ๐ธ๐ฝ CHANNEL ๐๐พ ๐๐๐ด ๐ผ๐ด๐</i>",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jแดษชษด ษดแดแดก ๐", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="<i>๐ข๐ธ๐ถ๐ฎ๐ฝ๐ฑ๐ฒ๐ท๐ฐ ๐๐ฎ๐ท๐ฝ ๐๐ป๐ธ๐ท๐ฐ</i> <b> <a href='https://t.me/Hollywood_in_HindiHD'>CLICK HERE FOR SUPPORT </a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_photo(
        chat_id=m.chat.id,
        photo ="https://telegra.ph/file/19eeb26fa2ce58765917a.jpg",
        caption =f'Hi {m.from_user.mention(style="md")}!,\nI am Telegram File to Link Generator Bot with Channel support.\nSend me any file and get a direct download link and streamable link.!',
        reply_markup=buttonz)


@StreamBot.on_message((filters.command("help") | filters.regex('help๐')) & filters.private )
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**Nแดแดก Usแดส Jแดษชษดแดแด **\n\n__Mส Nแดแดก Fสษชแดษดแด__ [{message.from_user.first_name}](tg://user?id={message.from_user.id}) __Started Your Bot !!__"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="<i>Sแดสสส Sษชส, Yแดแด แดสแด Bแดษดษดแดแด FROM USING แดแด. Cแดษดแดแดแดแด แดสแด Dแดแด แดสแดแดแดส</i>",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://telegra.ph/file/19eeb26fa2ce58765917a.jpg",
                Caption="**๐น๐พ๐ธ๐ฝ ๐๐๐ฟ๐ฟ๐พ๐๐ ๐ถ๐๐พ๐๐ฟ ๐๐พ ๐๐๐ด แดสษชs Bแดแด!**\n\n__Dแดแด แดแด Oแด แดสสแดแดแด, Oษดสส Cสแดษดษดแดส Sแดสsแดสษชสแดสs แดแดษด แดsแด แดสแด Bแดแด!__",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("๐ค Jแดษชษด Uแดแดแดแดแดs Cสแดษดษดแดส", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="__Sแดแดแดแดสษชษดษข แดกแดษดแด Wสแดษดษข. Cแดษดแดแดแดแด แดแด__ [Support](https://t.me/Redxpromotionrobot).",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""<b> Send me any file or video i will give you streamable link and download link.</b>\n
<b> I also support Channels, add me to you Channel and send any media files and see miracleโจ also send /list to know all commands""",
        
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("๐โโ๏ธ Owner", url="https://t.me/AmanReDX")]
            ]
        )
    )
