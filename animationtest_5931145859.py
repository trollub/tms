import random
from asyncio import sleep
import os
from .. import loader, utils, version
from telethon.tl.functions.users import GetFullUserRequest
import time
import logging
import re
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
from ..inline.types import InlineCall
from telethon.tl.functions.account import UpdateProfileRequest
from telethon.tl.types import Message
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest, GetFullChatRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins, UserStatusOnline
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError)
from telethon.errors.rpcerrorlist import UsernameOccupiedError
from telethon.tl.functions.account import UpdateProfileRequest, UpdateUsernameRequest
from telethon.tl.functions.users import GetFullUserRequest
from datetime import datetime
from math import sqrt
import requests
import git
from .. import loader, utils
from random import choice
from asyncio import sleep
import datetime
import asyncio
from telethon import types
from telethon.tl.functions.channels import GetFullChannelRequest
from .. import loader, utils
from asyncio import sleep
from datetime import timedelta
from telethon import types
import datetime
import logging
import time
import random
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import Message
from datetime import datetime
from datetime import timedelta
from telethon import functions
from os import remove
from telethon.tl.functions.channels import LeaveChannelRequest, InviteToChannelRequest 
from telethon.errors import UserIdInvalidError, UserNotMutualContactError, UserPrivacyRestrictedError, BotGroupsBlockedError, ChannelPrivateError, YouBlockedUserError,  MessageTooLongError, \
                            UserBlockedError, ChatAdminRequiredError, UserKickedError, InputUserDeactivatedError, ChatWriteForbiddenError, UserAlreadyParticipantError
from telethon.tl.types import ChannelParticipantCreator, ChannelParticipantsAdmins, PeerChat, ChannelParticipantsBots
from telethon.tl.functions.messages import AddChatUserRequest
import io
import io
import logging
from io import BytesIO

import requests
from requests import post
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from telethon.tl.types import DocumentAttributeFilename

from .. import loader, utils
import string
from typing import List
from urllib.parse import quote
import requests
from telethon.tl.types import Message
from ..inline.types import InlineCall
from .. import loader, utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins, UserStatusOnline
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError)
from datetime import datetime
import random
from asyncio import sleep
import os
from .. import loader, utils
from telethon.tl.functions.users import GetFullUserRequest
import time 
from telethon.tl.types import Message
from telethon import types
from random import randint
from contextlib import suppress
from telethon.tl.types import Message, MessageMediaPhoto
from telethon import errors, functions
from telethon.errors import (
    BotGroupsBlockedError,
    ChannelPrivateError,
    ChatAdminRequiredError,
    ChatWriteForbiddenError,
    InputUserDeactivatedError,
    MessageTooLongError,
    UserAlreadyParticipantError,
    UserBlockedError,
    UserIdInvalidError,
    UserKickedError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
    YouBlockedUserError,
)
from telethon.tl.functions.channels import InviteToChannelRequest, LeaveChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest, GetCommonChatsRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import (
    ChannelParticipantCreator,
    ChannelParticipantsAdmins,
    ChannelParticipantsBots,
)
from .. import loader, utils

from asyncio import sleep

from datetime import timedelta

from telethon import types

import datetime

import logging

import time

import random

import io

from asyncio import sleep

from os import remove



from telethon import errors, functions

from telethon.errors import (

    BotGroupsBlockedError,

    ChannelPrivateError,

    ChatAdminRequiredError,

    ChatWriteForbiddenError,

    InputUserDeactivatedError,

    MessageTooLongError,

    UserAlreadyParticipantError,

    UserBlockedError,

    UserIdInvalidError,

    UserKickedError,

    UserNotMutualContactError,

    UserPrivacyRestrictedError,

    YouBlockedUserError,

)

from telethon.tl.functions.channels import InviteToChannelRequest, LeaveChannelRequest

from telethon.tl.functions.messages import AddChatUserRequest, GetCommonChatsRequest

from telethon.tl.functions.users import GetFullUserRequest

from telethon.tl.types import (

    ChannelParticipantCreator,

    ChannelParticipantsAdmins,

    ChannelParticipantsBots,

)

from telethon import types



from telethon.tl.types import Message

from datetime import datetime

from datetime import timedelta

from telethon import functions

from telethon.tl.functions.users import GetFullUserRequest

import datetime

from datetime import datetime

from datetime import timedelta



from telethon import functions

from telethon.tl.types import Message

import time

from random import randint

from contextlib import suppress

from telethon.tl.functions.users import GetFullUserRequest
import time 
from telethon.tl.types import Message
from telethon import types
from random import randint
from contextlib import suppress
from telethon.tl.types import Message, MessageMediaPhoto
from telethon import errors, functions
from telethon.errors import (
    BotGroupsBlockedError,
    ChannelPrivateError,
    ChatAdminRequiredError,
    ChatWriteForbiddenError,
    InputUserDeactivatedError,
    MessageTooLongError,
    UserAlreadyParticipantError,
    UserBlockedError,
    UserIdInvalidError,
    UserKickedError,
    UserNotMutualContactError,
    UserPrivacyRestrictedError,
    YouBlockedUserError,
)
from telethon.tl.functions.channels import InviteToChannelRequest, LeaveChannelRequest
from telethon.tl.functions.messages import AddChatUserRequest, GetCommonChatsRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import (
    ChannelParticipantCreator,
    ChannelParticipantsAdmins,
    ChannelParticipantsBots,
)
from telethon.tl.functions.channels import GetFullChannelRequest, GetParticipantsRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.types import MessageActionChannelMigrateFrom, ChannelParticipantsAdmins, UserStatusOnline
from telethon.errors import (ChannelInvalidError, ChannelPrivateError, ChannelPublicGroupNaError)
from datetime import datetime
from .. import loader, utils
from asyncio import sleep
from datetime import timedelta
from telethon import types
import datetime
import logging
import time
import random
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import Message
from datetime import datetime
from datetime import timedelta
from telethon import functions
from os import remove
from telethon.tl.functions.channels import LeaveChannelRequest, InviteToChannelRequest 
from telethon.errors import UserIdInvalidError, UserNotMutualContactError, UserPrivacyRestrictedError, BotGroupsBlockedError, ChannelPrivateError, YouBlockedUserError,  MessageTooLongError, \
                            UserBlockedError, ChatAdminRequiredError, UserKickedError, InputUserDeactivatedError, ChatWriteForbiddenError, UserAlreadyParticipantError
from telethon.tl.types import ChannelParticipantCreator, ChannelParticipantsAdmins, PeerChat, ChannelParticipantsBots
from telethon.tl.functions.messages import AddChatUserRequest
import io
import string
from typing import List
from urllib.parse import quote
import requests
from telethon.tl.types import Message
from ..inline.types import InlineCall
from .. import loader, utils
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

ph = ""
start = datetime.now()


@loader.tds
class animationtest(loader.Module):
    '''описание хелпера'''
    strings = {
    "name":  "<b>animation test</b>",
    "loading": "<b>animation test</b>",
    "not_chat": "<b>animation test</b>",
    }

    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    async def client_ready(self, client, db):
        self.client = client

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client

    async def client_ready(self, client, db):
        self.db = db
        self.client = client
        self.users = []

    async def client_ready(self, client, db):
        self.db = db
        self.client = client

    async def testanimcmd(self, message):
        """загрузка информации"""
        args = utils.get_args_raw(message)
        await message.edit(
            "ч")
        time.sleep(0.1)
        await message.edit(
            "че")
        time.sleep(0.1)
        await message.edit(
            "че б")
        time.sleep(0.1)
        await message.edit(
            "че бл")
        time.sleep(0.1)
        await message.edit(
            "че бля")
        time.sleep(0.1)
        await message.edit(
            "че бля п")
        time.sleep(0.1)
        await message.edit(
            "че бля пе")
        time.sleep(0.1)
        await message.edit(
            "че бля пед")
        time.sleep(0.1)
        await message.edit(
            "че бля педи")
        time.sleep(0.1)
        await message.edit(
            "че бля педик")
        time.sleep(0.1)
        await message.edit(
            "че бля педик в")
        time.sleep(0.1)
        await message.edit(
            "че бля педик ви")
        time.sleep(0.1)
        await message.edit(
            "че бля педик вид")
        time.sleep(0.1)
        await message.edit(
            "че бля педик виде")
        time.sleep(0.1)
        await message.edit(
            "че бля педик видеш")
        time.sleep(0.1)
        await message.edit(
            "че бля педик видешь?")
        time.sleep(0.1)
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()
        args = utils.get_args_raw(message)
        starter = datetime.now()
        end = datetime.now()
        pins = (end - start).microseconds / 1000
        timing = starter - start
        ping_string = str(pins)
        pingg = ping_string.split(".")
        ping = float(pingg[1])
        time_string = str(timing)
        time_result = time_string.split(".")[0]
        to_chat = None
        try:
            if args:
                to_chat = int(args) if args.isdigit() else args
            else:
                to_chat = message.chat_id
        except ValueError:
            to_chat = message.chat_id
        chat = await message.client.get_entity(to_chat)
        chat_id = message.chat_id
        chat = await message.client.get_entity(to_chat)
        user_info = (
                "TEST FOR RAGNAROK\n"
                f"ping: <code>{ping}</code>\n"
                f"time result: <code>{time_result}</code>\n"
                f"chat id: <code>{chat_id}</code>\n"
                f"name for chat: <code>{chat.title}</code>\n"
            )

        args = utils.get_args_raw(message)
        if not args:
            if chat_id:
                await self.client.send_file(message.peer_id, ph, caption=user_info)

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