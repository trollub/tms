from .. import loader, utils
import psutil
from datetime import datetime
from typing import List
from urllib.parse import quote
import requests
from telethon.tl.types import Message
from ..inline.types import InlineCall
from .. import loader, utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from contextlib import suppress
from datetime import datetime
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import Message, MessageMediaPhoto

ph = ""
start = datetime.now()

class PingMod(loader.Module):
	strings = {
	"name": "PingMod",
	"load": "<b>Downloading...</b>"
	}

	async def client_ready(self, client, db):
		self.db = db
		self.client = client

	async def pkcmd(self, message):
		reply = await message.get_reply_message()
		file = reply if reply and reply else False
		await message.edit("<b>Downloading...</b>")
		media = await reply.download_media('shab.jpg')
		global ph
		ph = media
		await message.edit("<b>file succesfully downloaded!</b>")


	async def pcmd(self, message):
		time_now = datetime.now()
		timing = time_now - start
		time_string = str(timing)
		time_result = time_string.split(".")[0]
		end = datetime.now()
		pins = (end-start).microseconds / 1200
		cpu = psutil.cpu_count()
		cpu_init = psutil.cpu_percent()
		memory = psutil.virtual_memory()
		chat_id = message.chat_id
		if chat_id:
			await self.client.send_file(message.peer_id, ph, caption=f'<b>Ping:<code>{pins}</code> ms\nUptime:<code>{time_result}</code>\nCpu Cores:<code>{cpu}</code>\nCpu Load:<code>{cpu_init}%</code>\nMemory Used:<code>{psutil.virtual_memory()[2]}%</code></b>')
					