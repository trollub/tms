from .. import loader, utils
import psutil
import platform
from datetime import datetime
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
from asyncio import sleep

start = datetime.now()
ph = ""


#by n3rz4
class InformationMod(loader.Module):
	strings = {
	"name": "n3rz4Mod",
	"loader": "<b>Downloading</b>"
	}

	async def client_ready(self, client, db):
		self.db = db
		self.client = client

	async def downloadcmd(self, message):
		reply = await message.get_reply_message()
		global ph
		await message.edit("<b><u>скачиваю...</u></b>")
		await sleep(5)
		if reply.photo:
			media = await reply.download_media('shab.jpg')
			ph = media
			await message.edit("<b>succesfully</b>")
		if reply.video:
			media = await reply.download_media('shab.mp4')
			ph = media
			await message.edit("<b>succesfully</b>")

	async def ninfocmd(self, message):
		args = utils.get_args_raw(message)
		st = platform.platform()
		memory_usage = psutil.virtual_memory()
		cpu = psutil.cpu_count()
		cpu_count = psutil.cpu_percent()
		time_now = datetime.now()
		python_version = platform.python_version()
		version = platform.version()
		timing = time_now - start
		time_string = str(timing)
		time_result = time_string.split(".")[0]
		chat_id = message.chat_id
		me = message.sender_id
		user = await self.client.get_entity(me)
		if chat_id:
			await self.client.send_file(message.peer_id, ph, caption=f"<b><emoji document_id=5776317089941819022>🔣</emoji><emoji document_id=5469764774147401992>😈</emoji><emoji document_id=5775980785412608123>🔣</emoji>-𝑯𝒊𝒌𝒌𝒂 𝑰𝒏𝒇𝒐-<emoji document_id=5776317089941819022>🔣</emoji><emoji document_id=5469764774147401992>😈</emoji><emoji document_id=5775980785412608123>🔣</emoji>\n\n<emoji document_id=5776317089941819022>🔣</emoji><emoji document_id=5379696449502060899>🔥</emoji><emoji document_id=5775980785412608123>🔣</emoji>-𝑨𝒅𝒎𝒊𝒏-<emoji document_id=5776317089941819022>🔣</emoji><emoji document_id=5379696449502060899>🔥</emoji><emoji document_id=5775980785412608123>🔣</emoji> - <a href='tg://user?id={me}'>{user.first_name}</a>\n\n<emoji document_id=5776317089941819022>🔣</emoji><emoji document_id=5379696449502060899>🔥</emoji><emoji document_id=5775980785412608123>🔣</emoji>-𝑼𝒑𝒕𝒊𝒎𝒆-<emoji document_id=5776317089941819022>🔣</emoji><emoji document_id=5379696449502060899>🔥</emoji><emoji document_id=5775980785412608123>🔣</emoji> - <code>{time_result}</code>\n<emoji document_id=5776317089941819022>🔣</emoji><emoji document_id=5379696449502060899>🔥</emoji><emoji document_id=5775980785412608123>🔣</emoji>-𝑹𝒂𝒎-<emoji document_id=5776317089941819022>🔣</emoji><emoji document_id=5379696449502060899>🔥</emoji><emoji document_id=5775980785412608123>🔣</emoji> - <code>{psutil.virtual_memory()[2]}%</code>\n\n - <code>{cpu}</code>\n<emoji document_id=5776317089941819022>🔣</emoji><emoji document_id=5379696449502060899>🔥</emoji><emoji document_id=5775980785412608123>🔣</emoji>-𝑪𝒑𝒖 𝑳𝒐𝒂𝒅-<emoji document_id=5776317089941819022>🔣</emoji><emoji document_id=5379696449502060899>🔥</emoji><emoji document_id=5775980785412608123>🔣</emoji> - <code>{cpu_count}%</code>\n\n<emoji document_id=5776317089941819022>🔣</emoji><emoji document_id=5379696449502060899>🔥</emoji><emoji document_id=5775980785412608123>🔣</emoji>-𝑷𝒚𝒕𝒉𝒐𝒏 𝑽𝒆𝒓𝒔𝒊𝒐𝒏-<emoji document_id=5776317089941819022>🔣</emoji><emoji document_id=5379696449502060899>🔥</emoji><emoji document_id=5775980785412608123>🔣</emoji> - <code>{python_version}</code>\n<emoji document_id=5776317089941819022>🔣</emoji><emoji document_id=5379696449502060899>🔥</emoji><emoji document_id=5775980785412608123>🔣</emoji>-𝑯𝒐𝒔𝒕 𝑽𝒆𝒓𝒔𝒊𝒐𝒏-<emoji document_id=5776317089941819022>🔣</emoji><emoji document_id=5379696449502060899>🔥</emoji><emoji document_id=5775980785412608123>🔣</emoji> - <code>{version}</code>\n\n<emoji document_id=5776317089941819022>🔣</emoji><emoji document_id=5379696449502060899>🔥</emoji><emoji document_id=5775980785412608123>🔣</emoji>-𝑷𝒍𝒂𝒕𝒇𝒐𝒓𝒎-<emoji document_id=5776317089941819022>🔣</emoji><emoji document_id=5379696449502060899>🔥</emoji><emoji document_id=5775980785412608123>🔣</emoji> - GoormIde</b>")