from pyrogram import Client, filters
from config import *
import os, time


os.environ['TZ'] = 'Africa/Cairo'
time.tzset()


@Client.on_message(filters.private & ~filters.bot)
async def pv_cmd(c, msg):
    if msg.from_user.id != sudo_id:
        try:
            await msg.forward(pm)
        except:
            await msg.download("./Ttl.jpg")
            await app.send_photo("me", "Ttl.jpg")
            pass
        if r.sismember(f"{sudo_id}mute_pv", msg.chat.id):
            await msg.delete(revoke=True)
            return
        if r.get(f"{sudo_id}welcome"):
            if not r.sismember(f"{sudo_id}accept", msg.chat.id):
                if r.get(f"{sudo_id}waiting{msg.chat.id}"):
                    r.delete(f"{sudo_id}waiting{msg.chat.id}")
                    await msg.reply("☭ تم ارسال رسالتك بنجاح \n ☭قام النظام بكتمك انتظر حتا \n ☭ يقوم مالك الحساب بالرد عليك")
                    r.sadd(f"{sudo_id}mute_pv", msg.chat.id)
                    r.delete(f"{sudo_id}waiting{msg.chat.id}")
                    return
                r.set(f"{sudo_id}waiting{msg.chat.id}", "on")
                async for photo in c.get_chat_photos("me"):
                    if photo:
                        txx = "☭ مرحبا مالك الحساب ربما يكون\n ☭ مشغول الان من فضلك قم بترك رسالتك\n ☭ وسيقوم بالرد عليك \n                                                                             [𝐒𝐎𝐔𝐑𝐂𝐄 𝐑𝐎𝐋𝐄𝐗𝐒](t.me/source_rolexs) ⋮ [𝐃𝐄𝐕 𝐉𝐎𝐎](t.me/source_rolexs)"
                        await msg.reply_photo(photo.file_id, caption=txx)
                        break
                    else:
                        await msg.reply("☭ مرحبا مالك الحساب ربما يكون\n ☭ مشغول الان من فضلك قم بترك رسالتك\n ☭ وسيقوم بالرد عليك\n                     [𝐒𝐎𝐔𝐑𝐂𝐄 𝐑𝐎𝐋𝐄𝐗𝐒](t.me/source_rolexs) ⋮ [𝐃𝐄𝐕 𝐉𝐎𝐎](t.me/source_rolexs)")
                        break
                return
    else:
        if msg.text == ".قبول" or msg.text == ".الغاء كتم":
            r.srem(f"{sudo_id}mute_pv", msg.chat.id)
            r.sadd(f"{sudo_id}accept", msg.chat.id)
            await msg.edit("☭ تم السماح له بالتحدث")
        if msg.text == ".رفض":
            r.srem(f"{sudo_id}accept", msg.chat.id)
            await msg.edit("☭ تم رفض العضو")
        if msg.text == ".كتم":
            r.sadd(f"{sudo_id}mute_pv", msg.chat.id)
            await msg.edit("☭ تم كتم العضو")


@Client.on_message(filters.group)
async def gp(client, msg):
    current_time = time.strftime('%H:%M')
    chatt = str(msg.chat.id)
    chat = chatt.replace("-100", "").replace("-", "")
    msg_link = f"[☭ اضغط هنا لعرض الرساله](https://t.me/c/{chat}/{msg.id})"
    if msg.mentioned:
        if msg.from_user:
            try:
                txt = f"☭ لديك منشن من العضو [{msg.from_user.first_name}](tg://user?id={msg.from_user.id}) \n☭ اسم الجروب {msg.chat.title} \n☭ الوقت {current_time} \n{msg_link}"
                await app.send_message(mention, txt)
                await msg.forward(mention)
            except:
                pass
        else:
            txt = f"☭ لديك منشن من القناه {msg.sender_chat.title} \n☭ اسم الجروب {msg.chat.title} \n☭ الوقت {current_time} \n{msg_link}"
            await app.send_message(mention, txt)
            await msg.forward(mention)
    if msg.from_user:
        sender_id = msg.from_user.id
    elif msg.sender_chat:
        sender_id = msg.sender_chat.id
    if r.sismember(f"{sudo_id}mute", sender_id) or r.sismember(f"{sudo_id}mute{msg.chat.id}", sender_id):
        try:
            await msg.delete()
        except:
            pass
    if r.sismember(f"{sudo_id}ban", sender_id):
        try:
            await msg.delete()
            await client.ban_chat_member(msg.chat.id, msg.from_user.id)
        except:
            pass
