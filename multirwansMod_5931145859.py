import random
from asyncio import sleep
from telethon import types

from .. import loader, utils


@loader.tds
class multirwansMod(loader.Module):
    strings = {
        "name": "RWANS MULTI",
        "pref": "<b>[RWANS MULTI]</b> ",
        "need_arg": "{}нужен аргумент",
        "status": "{}{}",
        "on": "{}запущен",
        "off": "{}выключен",
    }
    _db_name = "rwansmulti"

    async def client_ready(self, _, db):
        self.db = db

    @staticmethod
    def str2bool(v):
        return v.lower() in (
            "yes",
            "y",
            "ye",
            "yea",
            "true",
            "t",
            "1",
            "on",
            "enable",
            "start",
            "run",
            "go",
            "да",
        )

    async def rwanschatcmd(self, m: types.Message):
        "переключить режим"
        args = utils.get_args_raw(m)
        if not m.chat:
            return
        chat = m.chat.id
        if self.str2bool(args):
            chats: list = self.db.get(self._db_name, "chats", [])
            chats.append(chat)
            chats = list(set(chats))
            self.db.set(self._db_name, "chats", chats)
            return await utils.answer(
                m, self.strings("on").format(self.strings("pref"))
            )
        chats: list = self.db.get(self._db_name, "chats", [])
        try:
            chats.remove(chat)
        except:
            pass
        chats = list(set(chats))
        self.db.set(self._db_name, "chats", chats)
        return await utils.answer(m, self.strings("off").format(self.strings("pref")))



    async def rwansshcmd(self, m: types.Message):
        '''установка шапки'''
        args: str = utils.get_args_raw(m)
        self.db.set(self._db_name, "sh", str(args))
        return await utils.answer(
                m, self.strings("status").format(self.strings("pref"), args)
            )


    async def rwanszcmd(self, m: types.Message):
        "задержка секунды"
        args: str = utils.get_args_raw(m)
        if args.isdigit():
            self.db.set(self._db_name, "chance", int(args))
            return await utils.answer(
                m, self.strings("status").format(self.strings("pref"), args)
            )

        return await utils.answer(
            m, self.strings("need_arg").format(self.strings("pref"))
        )


    async def rwanstxtcmd(self, m: types.Message):
        "установка шаблона с форматом .txt"
        args: str = utils.get_args_raw(m)
        self.db.set(self._db_name, "text", str(args))
        return await utils.answer(
                m, self.strings("status").format(self.strings("pref"), args)
            )

    async def downloadcmd(self, message):
        """скачивание txt файла"""
        name = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        if reply:
            await message.edit('скачиваем...')
            if reply.text:
                text = reply.text
                fname = f'{name or message.id + reply.id}.txt'
                file = open(fname, 'w')
                file.write(text)
                file.close()
                await message.edit(
                    f'файл сохранён как: <code>{fname}</code>')
            else:
                ext = reply.file.ext
                fname = f'{name or message.id + reply.id}{ext}'
                await message.client.download_media(reply, fname)
                await message.edit(
                    f'этот файл сохранён как: <code>{fname}</code>')
        else:
            return await message.edit('Нет реплая.')


    async def watcher(self, m: types.Message):
        if not isinstance(m, types.Message):
            return
        if m.sender_id == (await m.client.get_me()).id or not m.chat:
            return
        if m.chat.id not in self.db.get(self._db_name, "chats", []):
            return
        ch = self.db.get(self._db_name, "chance", [])
        sh = self.db.get(self._db_name, 'sh', [])
        text = self.db.get(self._db_name, 'text', [])
        with open(f'{text}', 'r', encoding='utf-8') as f:
            a = f.read()
            b = a.split('\n')
            await sleep(ch)
            await m.reply(sh + random.choice(b))