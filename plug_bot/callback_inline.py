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
• تفعيل ، تعطيل الترحيب 
• قبول ، رفض
• كتم ، الغاء كتم 
• سبام + الكلمه + الرقم (سبام رولكس 22)
• ايدي + ايدي بالرد"""
txx2 = """
• حظر ، الغاء حظر
• مسح المحظورين
• كتم ، الغاء كتم 
• مسح المكتومين
• ايدي + ايدي بالرد
• مسح رسايله (بالرد)
• تدمير (لتحظر جميع اعضاء المجموعه او القناه)
• مسح الروابط 
• مسح الصور 
• مسح + العدد
• اضف جهاتي
"""
txx3 = """
• غ + اسم الاغنيه
• ف + اسم الفيديو 
"""
txx4 = """
• اذاعه خاص (بالرد علي النص)
• اذاعه للمجموعات (بالرد علي النص)
• اذاعه للقنوات (بالرد علي النص)

• توجيه للخاص (بالرد علي الرساله)
• توجيه للمجموعات (بالرد علي الرساله)
• توجيه للقنوات (بالرد علي الرساله)
"""
txx5 = """
• زواج ، طلاق -- زوجاتي -- مسح زوجاتي
• رفع ، تنزيل خول -- الخولات -- مسح الخولات 
• رفع ، تنزيل بنتي -- بناتي -- مسح بناتي
• رفع ، تنزيل شاذ -- الشواذ -- مسح الشواذ
• رفع ، تنزيل عرص -- المعرصين -- مسح المعرصين
• رفع ، تنزيل كلب -- الكلاب -- مسح الكلاب
• رفع ، تنزيل متوحد -- المتوحدين -- مسح المتوحدين
• رفع ، تنزيل حمار -- الحمير -- مسح الحمير
• رفع ، تنزيل بقلبي -- القلوب -- مسح القلوب 
• رفع ، تنزيل ابني -- اولادي -- مسح اولادي
"""
txx6 = """
• تلجراف (بالرد علي صوره لرفعها علي تليجراف)
• وش يقول (بالرد علي صوت)
• تفعيل تعطيل الساعه 
• تغيير اسمي + الاسم (تغيير اسمي rolexs)
• سورس
"""
txx7 = """
• تهكير
• قتل
• قمور
• زعلت
• متت
• فليم
• رسم
• موسيقي
• مصه
• قطار
• فايروس
• مايكرو
• ولد
• افعي
• عبقري
• معاكسه
• قياس
• بشره
• شرطه
• مربع
• تحميل
"""
txx8 = """
• نسبة الانوثة
• نسبة الرجولة
• نسبة الغباء
"""
txx9 = """
• `.هنضحك`
• `.مينفعش`
• `.عاوزين نعملك بني ادم`
• `.ي حوستي السوده`
• `.هنضحك حاضر`
• `.انا تعبان ي حامد`
• `.نعم انها المخدرات`
• `.قول كلام غير ده`
• `.ءنا عملت ءيه`
• `.عيب يجدعان`
• `.هتتحرقو في نار جهنم`
• `.يالي هتتحرقو`
• `.احترمي نفسك يوليه`
"""
txx10 = """
• `.في رمضان`
• `.مش عارف اقوم`
• `.دمك خفيف اوي`
• `.لا تقتل المتعه ي مسلم`
• `.يختاااي`
• `.بيكدب`
• `.احنا جامدين اوي`
• `.اي الهبل دا`
• `.فاشل فاشل`
• `.اجمد كدا متعيطش`
• `.يا لاهوي`
• `.دا اي الهم دا`
• `.هعوره`
"""
txx11 = """
• `.تاخد نفس عميق`
• `.ربنا نصرني`
• `.لو معايا خنجرين`
• `.اماااال`
• `.خخ امال`
• `.اهلا بيكم`
• `.اخلاقك العاليه دي`
• `.علي مهلك`
• `.خبر اي ي مرا`
• `.انا بيه بن بيه`
• `.اتكلم بادب يولد`
• `.انا رمضان جانا يعم`
• `.انت مش مظبوط ياض`
• `.ي حلو ي جميل`
• `.خلصانه`
• `.انا في دوامه`
• `.مش اسمحلك`
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
@bot.on_callback_query(filters.regex("^help7$"))
async def help7(client, callback_query):
  await callback_query.edit_message_text(txx7,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help8$"))
async def help8(client, callback_query):
  await callback_query.edit_message_text(txx8,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help9$"))
async def help9(client, callback_query):
  await callback_query.edit_message_text(txx9,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help10$"))
async def help10(client, callback_query):
  await callback_query.edit_message_text(txx10,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help11$"))
async def help11(client, callback_query):
  await callback_query.edit_message_text(txx11,reply_markup=reply_markup)
@bot.on_callback_query(filters.regex("^help$"))
async def back(client, callback_query):
  await callback_query.edit_message_text("• اهلا بك في اوامر اليوزر البوت\n• ① اوامر الخاص\n• ② اوامر القنوات والمجموعات \n• ③ اوامر اليوتيوب \n• ④ اوامر الاذاعه\n• ⑤ اوامر التسليه \n• ⑥ اوامر اضافيه\n• ⑦ اوامر المرح\n• ⑧ اوامر النسب\n• ⑨ اوامر الميمز\n• ⓪① اوامر الميمز2\n• ①① اوامر الميمز3",reply_markup = InlineKeyboardMarkup(
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
             ))
