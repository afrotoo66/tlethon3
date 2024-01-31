from pyrogram import Client, filters,enums
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from config import *
import asyncio


@bot.on_inline_query(filters.regex("^الاوامر$") )
async def answer(client, inline_query):
    reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton("①",callback_data="help1"),
             InlineKeyboardButton("②",callback_data="help2"),
             ],
             [
             InlineKeyboardButton("③",callback_data="help3"),
             InlineKeyboardButton("④",callback_data="help4"),
             ],
             [
             InlineKeyboardButton("⑤",callback_data="help5"),
             InlineKeyboardButton("⑥",callback_data="help6"),
             ],
             [
             InlineKeyboardButton("「 𝗦𝗢𝗨𝗥𝗖𝗘 𝗦𝗣𝗜𝗗𝗘𝗥 」",url="https://t.me/EE_20"),
             ],
             [
             InlineKeyboardButton("「 𝗠𝗔𝗞𝗘𝗥 𝗦𝗣𝗜𝗗𝗘𝗥 」",url="https://t.me/TELE1SPIDER1bot"),
             ]]
             )
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="اوامر البوت",
                input_message_content=InputTextMessageContent(
                    "⎊ اهلا بك في اوامر تيلثون سبايدر\n① اوامر الخاص\n② اوامر القنوات والمجموعات \n③ اوامر اليوتيوب \n④ اوامر الاذاعه\n⑤ اوامر التسليه \n⑥ اوامر اضافيه"
                ),
                url="https://t.me/EE_20",
                description="SOURCE SPIDER",
                reply_markup=reply_markup
            ),
        ],
        cache_time=1
    )
