#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>👨‍💻 Developer : <a href='tg://Itz_Sung_Jin_Woo'>This Person</a>\n📑 Language : <a href='https://python.org/'>Python3</a>\n📚 Library : <a href='https://docs.pyrogram.org/'>Pyrogram asyncio {__version__}</a>\n🌐 Server : <a href='https://heroku.com/'>Heroku</a>\n📣 Channel : <a href='https://t.me/Anime_Worlds_In_Tamil'>Anime World in Tamil<a/>\n🤖 My Name : <a href='https://t.me/Shonobi_File_Bot'>File Sharing Bot</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🔒 Close", callback_data = "close")
                    ]
                ]
            )
        )
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
