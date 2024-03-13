from pyrogram import Client, filters,enums
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from config import *
import asyncio


@bot.on_inline_query(filters.regex("^اومري$") )
async def answer(client, inline_query):
    reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton("①",callback_data="help1"),
             InlineKeyboardButton("②",callback_data="help2"),
             InlineKeyboardButton("③",callback_data="help3"),
             InlineKeyboardButton("④",callback_data="help4"),
             ],
             [
             InlineKeyboardButton("⑤",callback_data="help5"),
             InlineKeyboardButton("⑥",callback_data="help6"),
             InlineKeyboardButton("⑦",callback_data="help7"),
             InlineKeyboardButton("⑧",callback_data="help8"),
             ],
             [
             InlineKeyboardButton("⑨",callback_data="help9"),
             InlineKeyboardButton("①⓪",callback_data="help10"),
             InlineKeyboardButton("①①",callback_data="help11"),
             ],
             [
             InlineKeyboardButton("𝙰𝙵𝚁𝙾𝚃𝙾𝙾",url="https://t.me/VVYVVJ"),
             ],
             [
             InlineKeyboardButton("ᯓ 𝚂𝙾𝚞𝚁𝙲𝙴 𝙰𝙵𝚁𝙾𝚃𝙾𝙾 ‌",url="https://t.me/UI_VM"),
             ]]
             )
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="اوامر البوت",
                input_message_content=InputTextMessageContent(
                    "• اهلا بك في اوامر اليوزر البوت\n• ① اوامر الخاص\n• ② اوامر القنوات والمجموعات \n• ③ اوامر اليوتيوب \n• ④ اوامر الاذاعه\n• ⑤ اوامر التسليه \n• ⑥ اوامر اضافيه\n• ⑦ اوامر المرح\n• ⑧ اوامر النسب\n• ⑨ اوامر الميمز\n• ⓪① اوامر الميمز2\n• ①① اوامر الميمز3"
                ),
                url="https://t.me/SOURCE_HORSE",
                description="ᯓ 𝚂𝙾𝚞𝚁𝙲𝙴 𝙰𝙵𝚁𝙾𝚃𝙾𝙾 ‌",
                reply_markup=reply_markup
            ),
        ],
        cache_time=1
    )
