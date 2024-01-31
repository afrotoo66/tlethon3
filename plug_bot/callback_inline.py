from pyrogram import Client, filters,enums
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from config import *
import asyncio
reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton("عوده",callback_data="help"),
             ]]
             )
txx1 = """
⎈━━━⊶𐂡•𝗦𝗣𝗜𝗗𝗘𝗥•𐂡⊷━━━⎈
⎊ تفعيل ، تعطيل الترحيب 
⎊ قبول ، رفض
⎊ كتم ، الغاء كتم 
⎊ سبام + الكلمه + الرقم (سبام اسامه 22)
⎊ ايدي + ايدي بالرد
 ⌯︙ @EE_20
"""
txx2 = """
⎈━━━⊶𐂡•𝗦𝗣𝗜𝗗𝗘𝗥•𐂡⊷━━━⎈
⎊ حظر ، الغاء حظر
⎊ مسح المحظورين
⎊ كتم ، الغاء كتم 
⎊ مسح المكتومين
⎊ ايدي + ايدي بالرد
⎊ مسح رسايله (بالرد)
⎊ تدمير (لتحظر كل اعضاء المجموعه او القناه)
⎊ مسح الروابط 
⎊ مسح الصور 
⎊ مسح + العدد
⎊ اضف جهاتي
 ⌯︙ @EE_20
"""
txx3 = """
⎈━━━⊶𐂡•𝗦𝗣𝗜𝗗𝗘𝗥•𐂡⊷━━━⎈
⎊ غ + اسم الاغنيه
⎊ ف + اسم الفيديو 
 ⌯︙ @EE_20
"""
txx4 = """
⎈━━━⊶𐂡•𝗦𝗣𝗜𝗗𝗘𝗥•𐂡⊷━━━⎈
⎊ اذاعه خاص (بالرد علي النص)
⎊ اذاعه للمجموعات (بالرد علي النص)
⎊ اذاعه للقنوات (بالرد علي النص)

⎊ توجيه للخاص (بالرد علي الرساله)
⎊ توجيه للمجموعات (بالرد علي الرساله)
⎊ توجيه للقنوات (بالرد علي الرساله)
 ⌯︙ @EE_20
"""
txx5 = """
⎈━━━⊶𐂡•𝗦𝗣𝗜𝗗𝗘𝗥•𐂡⊷━━━⎈
⎊ زواج ، طلاق -- زوجاتي -- مسح زوجاتي
⎊ رفع ، تنزيل خول -- الخولات -- مسح الخولات 
⎊ رفع ، تنزيل بنتي -- بناتي -- مسح بناتي
⎊ رفع ، تنزيل شاذ -- الشواذ -- مسح الشواذ
⎊ رفع ، تنزيل عرص -- المعرصين -- مسح المعرصين
⎊ رفع ، تنزيل كلب -- الكلاب -- مسح الكلاب
⎊ رفع ، تنزيل متوحد -- المتوحدين -- مسح المتوحدين
⎊ رفع ، تنزيل حمار -- الحمير -- مسح الحمير
⎊ رفع ، تنزيل بقلبي -- القلوب -- مسح القلوب 
⎊ رفع ، تنزيل ابني -- اولادي -- مسح اولادي
 ⌯︙ @EE_20
"""
txx6 = """
⎈━━━⊶𐂡•𝗦𝗣𝗜𝗗𝗘𝗥•𐂡⊷━━━⎈
⎊ تلجراف (بالرد علي صوره لرفعها علي تليجراف)
⎊ وش يقول (بالرد علي صوت)
⎊ تفعيل ، تعطيل الساعه 
⎊ تغيير اسمي + الاسم (تغيير اسمي OSAMA)
⎊ سورس
 ⌯︙ @EE_20
"""



@bot.on_callback_query(filters.regex("^help1$"))
async def help1(client, callback_query):
  await callback_query.edit_message_text(txx1,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help2$"))
async def help2(client, callback_query):
  await callback_query.edit_message_text(txx2,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help3$"))
async def help3(client, callback_query):
  await callback_query.edit_message_text(txx3,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help4$"))
async def help4(client, callback_query):
  await callback_query.edit_message_text(txx4,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help5$"))
async def help5(client, callback_query):
  await callback_query.edit_message_text(txx5,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help6$"))
async def help6(client, callback_query):
  await callback_query.edit_message_text(txx6,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help$"))
async def back(client, callback_query):
  await callback_query.edit_message_text("⎊ اهلا بك في اوامر تيلثون سبايدر\n① اوامر الخاص\n② اوامر القنوات والمجموعات \n③ اوامر اليوتيوب \n④ اوامر الاذاعه\n⑤ اوامر التسليه \n⑥ اوامر اضافيه",reply_markup = InlineKeyboardMarkup(
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
             ))
