from mody import Mody
from pyrogram import Client,filters,enums
import redis
r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    charset="utf-8",
    decode_responses=True
)

sudo_id = 5904216848
bot_user = Mody.BOT_USER
via_user = Mody.VIA_USER
elhyba = bot_user
via = via_user
api_id = Mody.APP_ID
api_hash = Mody.API_HASH
session = Mody.SESSION
token = Mody.TG_BOT_TOKEN
sudo_command = [5904216848]
pm =  Mody.MENTION
mention = "5904216848"
plugins = dict(root="plugins")
app = Client(via,api_id , api_hash ,in_memory=True,session_string = session,plugins=plugins)
bot = Client(elhyba,api_id=api_id , api_hash=api_hash ,bot_token=token,plugins=dict(root="plug_bot"))
