# meta author: @utilizator2001
#meta developer: @owerTERROR
import random
from asyncio import sleep
import os
from .. import loader, utils
from telethon.tl.functions.users import GetFullUserRequest
import time 
from telethon.tl.types import Message
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
import random
from .. import loader, utils
from datetime import timedelta
from telethon import functions
from telethon.tl.types import Message

logger = logging.getLogger(__name__)

start = datetime.now()

ph = ""

bullr = [
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы жᴇ ʙ ᴋᴀчᴇᴄᴛʙᴇ ᴋиᴄᴛᴏчᴋи нᴀ иɜᴏ ʙ ɯᴋᴏᴧᴇ иᴄᴨᴏᴧьɜᴏʙᴀᴧ ʍᴏй хуй) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ʍнᴇ ᴄᴏᴄᴀᴧ ᴛᴀᴋ дᴏᴧᴦᴏ чᴛᴏ у ᴛᴇбя ɸᴧюᴄ ʙыᴄᴋᴏчиᴧ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я нᴀ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴋᴀᴩᴛᴏɯᴋу ᴄᴀжᴀᴛь щᴀᴄ буду) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ʍᴏй хуй ᴏбниʍᴀᴇɯь ᴋᴀᴋ ʍᴀʍᴋу ᴄʙᴏю) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴛᴇбя хуᴇʍ ʙыбиʙᴀᴧ ᴋᴀᴋ ᴋᴏʙᴩиᴋ нᴀхуй) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏй ᴩᴏᴛ ᴋ ʍᴏᴇʍу хую ᴨᴩиᴧиᴨ ᴋᴀᴋ ᴨияʙᴋᴀ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы нᴀ ʍᴏᴇʍ хую жиᴩᴏʍ ᴛᴏᴋ ᴛᴩяᴄᴇɯь ᴀ нᴇ ᴨиɜдᴏй) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ʍнᴇ ᴄᴏᴄᴀᴧ ᴛᴀᴋ чᴛᴏ ᴀж ᴏбᴧᴀᴋᴀ нᴀ нᴇбᴇ ᴩᴀɜᴏɯᴧиᴄь) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴄ ʍᴏᴇᴦᴏ хуя ᴄʙᴏю ʍᴀᴛь ᴩᴀᴄᴛᴩᴇᴧиʙᴀᴧ ᴄᴨᴇᴩʍᴏй) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴛʙᴏю ʍᴀᴛь хуᴇʍ ᴩᴀɜᴏбᴩᴀᴧ нᴀ ʍᴇᴛᴀᴧᴀᴧᴏʍ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍᴏй хуй дᴧя ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴋᴀᴋ ᴨᴩᴏʙᴏдниᴋ ʙ жиɜнᴇ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ʍᴏй хуй ʙᴏɜдуɯныʍи ᴨᴏцᴇᴧуяʍи ɜᴀцᴇᴨиᴛь ᴨыᴛᴀᴧᴄя) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы нᴀ ᴨᴏᴄᴧᴇдᴏᴋ ʍᴏй чᴧᴇн ᴄᴏᴄᴀᴧ ᴋᴀᴋ ʍᴀɯинᴀ ᴇбᴀнᴀя) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴛʙᴏю ʍᴀᴛь хᴏᴛᴇᴧ ᴨᴏᴇбᴀᴛь ,ᴀ ᴏнᴀ и ᴛᴀᴋ ужᴇ дыᴩяʙᴀя) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨиɜду ᴄʙᴏю ᴄᴛᴇᴧиɯь ᴨᴏд дʙᴇᴩи ʍᴏи) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я хуᴇʍ ᴛᴇбᴇ ʙ ᴧᴏб щᴀᴄ ᴨᴏᴄᴛучу нᴀхуй) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴛʙᴏю ʍᴀᴛь щᴀᴄ нᴀ хуй ᴨᴏᴧᴏжу ᴋᴀᴋ бᴧин ᴇбᴀᴛь) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я нᴀ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯᴋи ʍᴀᴋᴀᴩᴏны жᴀᴩиᴧ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я нᴀ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴋᴀньᴋᴀʍи ᴋᴀᴛᴀᴧᴄя) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я чᴇᴩᴇɜ ᴨиɜду ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴛᴇбя ᴋᴏᴩʍиᴧ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʙ ᴨиɜдᴀᴋᴇ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ʍуᴄᴏᴩ хуᴇʍ ʙыᴛᴀщу щᴀᴄ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴛʙᴏю ʍᴀᴛь нᴀ хуй нᴀᴄᴀдиᴧ ᴋᴀᴋ нᴀ ᴄᴛуᴧ ᴨᴏᴄᴀдиᴧ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ʙ ʍᴏй хуй ʙᴇᴩиɯь ᴋᴀᴋ ʙ чудᴏ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ʍᴏй хуй ᴨыᴛᴀᴇɯьᴄя ᴋуᴩиᴛь ᴋᴀᴋ ᴄиᴦу) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴛʙᴏю ʍᴀᴛь хуᴇʍ ᴨну ᴏнᴀ ʙ дᴇᴩᴇʙᴏ уᴇбᴇᴛᴄя) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴛʙᴏю щᴇᴋу хуᴇʍ ᴨᴩᴏᴛᴋнуᴧ ᴋᴀᴋ ᴏᴩᴦᴀᴧиᴛ ᴇбᴀᴛь) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы нᴀ ʍᴏᴇʍ хую ᴋᴀᴋ ɸуᴛбᴏᴧьный ʍяч, ʍᴏй хуй ᴛᴇбя ᴨинᴀᴇᴛ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я щᴀᴄ ʙ ᴛʙᴏᴇʍ ᴨиɜдᴀᴋᴇ хуᴇʍ ᴨᴏᴩядᴏᴋ нᴀʙᴏдиᴛь буду) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ʙ ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴋᴇ хуᴇʍ ɜᴀɯᴇᴧ ᴋᴀᴋ бᴀᴛьᴋᴀ ʙ дᴏʍ нᴀхуй) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍнᴇ ᴛᴇбя ᴄ хуя ᴄᴛᴩяхнуᴛь ᴋᴀᴋ ᴨᴇᴨᴇᴧ ᴄ ᴄиᴦᴀᴩᴇᴛы чᴛᴏᴧᴇ?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я уᴄᴨᴇʙᴀᴧ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴇщᴇ нᴀ ᴨᴇᴩᴇʍᴇнᴀх ʙ ɯᴋᴏᴧᴇ щᴀ щᴇᴋу ᴄунуᴛь) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы жᴇ нᴀ 23 ɸᴇʙᴩᴀᴧя будᴇɯь ᴄʙᴏю ᴨиɜду ᴋ ʍᴏᴇʍу хую ᴨᴩиᴨᴏднᴏᴄиᴛь) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴧюдяʍ ᴏбычнᴏ ʙ ʍᴀᴇ ᴛᴇᴨᴧᴏ, ну ᴀ ᴛы ᴋ ᴀᴋ ᴨидᴀᴩᴀᴄ у ʍᴇня ᴨᴏд яйцᴀʍи ᴄидиɯь и ᴦᴩᴇᴇɯьᴄя) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴛᴇбᴇ щᴀᴄ ᴋᴩч ʙ ухᴏ ᴋᴏнчу ᴄᴏ ᴩᴛᴀ ʙыᴧьᴇᴛᴄя ᴋᴀᴋ биɸидᴏᴋ нᴀхуй) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ʙ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯᴋи ᴨᴩᴀʙᴧю ᴄʙᴏиʍ хуᴇʍ ᴋᴀᴋ ᴧᴇнин ᴧᴇнинᴦᴩᴀдᴏʍ ʙ 41 ᴄуᴋᴀ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы бᴧяᴛь ᴋ ʍᴏᴇʍ хую ᴄᴏ ʙᴄᴇʍ ᴄᴇᴩдцᴇʍ ᴀ ᴏн нᴀ ᴛᴇбя ᴄᴄыᴛ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴛʙᴏᴇй ʍᴀᴛᴇᴩи нᴀ нᴏʙый ᴦᴏд ʙ ᴨиɜду ᴀᴧᴇʙьᴇху ɜᴀᴋинуᴧ и ʍᴇᴄиᴧ ᴇбᴧᴏʍ ᴛʙᴏиʍ :d <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы нᴀхуй ᴄʙᴏᴇй ᴨиɜдᴏй нᴀ ʍᴏᴇʍ хую ᴛᴀнᴇц бᴏйцᴀ иᴄᴨᴩᴀʙᴧяᴧ, ᴨиᴛух ᴇбᴀный) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀᴛь нᴀ ʍᴏй хуй ᴋᴧюᴇᴛ, ᴨᴧᴀᴛʙᴀ ᴇбᴀнᴀя) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴧыɯ, ᴨидᴏᴩᴀᴄ, ᴄюдᴀ иди ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴛʙᴏᴇй ʍᴀᴛᴇᴩи дᴀᴧ ᴋᴏᴧбᴀᴄᴏй ᴨᴏ ᴇбᴀᴧу, и ᴄᴋᴀɜᴀᴧ, чᴛᴏ ᴛᴀᴋ быᴧᴏ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇбᴀᴛь ᴛы ᴋуб ᴋʙᴀдᴩᴀᴛный ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀʍᴀɯᴀ ʙ ᴧᴇᴄу нᴀᴛᴋнуᴧᴀᴄь нᴀ ʍᴏй хуй,ᴋᴀᴋ ᴋᴩᴀᴄнᴀя ɯᴀᴨᴏчᴋᴀ нᴀ ʙᴏᴧᴋᴀ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀᴛь ɜᴀдᴇᴩжиʙᴀᴇᴛ дыхᴀниᴇ ᴨᴩи ʙидᴇ ʍᴏᴇᴦᴏ хуя) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏ ɸᴀᴋᴛу ᴛы ᴄᴏᴄᴇɯь ʍнᴇ хуй) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀᴛь бᴇᴧый ᴧᴇбᴇдь ʍᴏᴇᴦᴏ хуя ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ɯёᴧ нᴀ ɸᴩᴏнᴛ ʙ нᴀдᴇждᴇ уʙидᴇᴛь и ᴄᴨᴀᴄᴛи ᴏᴛ ᴨᴧᴇнᴀ ᴨиɜду ᴛʙᴏᴇй ʍᴀʍᴀɯи ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ϶ᴛᴏ нᴏʙᴀя ϶ᴩᴀ ᴛᴩᴏᴧᴧинᴦᴀ, ᴛуᴛ ᴄᴏɯᴧиᴄь ʙ ᴨᴏᴇдинᴋᴇ ɜубы ᴛʙᴏᴇй ʍᴀᴛᴇᴩи и ʍᴏй чᴧᴇн ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴋудᴀ ᴄъᴇбыʙᴀᴇɯь? ) ɜʙᴇᴩᴏᴄᴏʙхᴏɜ ᴀнᴀᴧьный ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь ʙ ᴨᴀᴩᴋᴇ юᴩᴋᴄᴋᴏᴦᴏ ᴨᴇᴩᴇᴏдᴀ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ɸу, ᴄᴛᴩᴇᴧᴏчниᴋ, ᴛʙᴏя ʍᴀᴛь ᴛᴏжᴇ ᴄᴛᴩᴇᴧяᴇᴛ ᴦубᴏй ᴨᴏ ʍᴏᴇʍу хую ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧ ᴋᴏᴦдᴀ нᴀ ᴨᴏᴧянᴋᴇ ɜᴀжᴦᴧиᴄь ɸᴏнᴀᴩи ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀᴛь уʙидᴇʙ ʍᴏй хуй ᴄᴋᴀɜᴀᴧᴀ -" чᴛᴏ ɜᴀ ᴋᴩᴀᴄᴀʙᴇц " <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы нᴀʙᴇᴩнᴏᴇ нᴇ ɜнᴀᴧ, нᴏ ʍᴏй хуй ᴨᴩᴏяʙᴧяᴧ ᴀᴋᴛиʙнᴏᴄᴛь ᴇщё ʙ ᴀнᴛичнᴏᴄᴛи, ʍᴏй хуй ᴨᴏ ᴄᴧᴏʙᴀʍ учᴇных быᴧ ᴄᴨᴀᴄиᴛᴇᴧᴇʍ ᴧюдᴄᴋᴏᴦᴏ ᴩᴏдᴀ. ʍᴏй хуй ᴄᴨᴀᴄ ᴧюдᴇй ᴏᴛ ᴦᴏᴧᴏдᴀ и жᴀжды ʙ ᴛᴏʍ чиᴄᴧᴇ и ᴛʙᴏю ʍᴀᴛь ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀᴛь ʍнᴇ ᴄᴏᴄᴀᴧᴀ ᴄ ʍᴏᴧиᴛʙᴏй ᴇбᴀнᴀɯᴋᴀ <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> у ᴛᴇбя ʍᴏᴧᴏɸья нᴀ ᴦубᴇ, ʙыᴛᴩи ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨидᴏᴩ, ᴀ ᴛʙᴏя ʍᴀʍᴀɯᴀ ᴄᴀᴄᴇᴛ!!! <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы хуᴇᴄᴏᴄ, ᴀ я ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь нᴀ ᴦᴏᴩᴀх ᴋᴀʙᴋᴀɜᴀ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴛᴇбᴇ ᴇбᴀᴧьниᴋ чᴧᴇнᴏʍ ᴨᴏᴛуɯу ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍᴀᴛь ᴛʙᴏю ᴇбᴀᴧ нᴀ ᴨᴩиᴇʍᴇ у ᴄᴛᴏʍᴀᴛᴏᴧᴏᴦᴀ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍᴀʍᴀɯᴋᴀ ᴛʙᴏя ɯᴧᴀ нᴀ хуй, ᴋᴀᴋ нᴇᴦᴩ ɜᴀ ᴄʙᴏбᴏдᴏй ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏйʍи ) ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴄᴨᴀᴄᴀᴇᴛᴄя ᴏᴛ бᴇд нᴀ ʍᴏᴇʍ хую, ᴛʙᴏя ʍᴀʍᴀɯᴀ ᴦᴏбᴧин ʍᴏᴇᴦᴏ хуя, я ᴇй цᴇᴧᴋу ʙиɯᴇнᴋᴏй ᴄᴏᴩʙᴀᴧ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴀ ᴛы ɜнᴀᴧ, чᴛᴏ ʍᴏй хуй ᴨищᴇɜᴀʍᴇниᴛᴇᴧь ᴛʙᴏᴇй ʍᴀʍᴀɯи? ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴋᴏᴧчᴀнᴏʍ ʍᴀᴛь ᴛʙᴏю ᴇбᴀᴧ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀʍᴀɯᴀ динᴀʍиᴋ ʍᴏᴇᴦᴏ хуя ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я биᴧ ᴨᴏᴄуду ᴏб ᴨиɜду ᴛʙᴏᴇй ʍᴀʍᴀɯи ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇбᴀᴧ ᴛʙᴏю ʍᴀʍᴀɯу нᴀ ᴋᴩыɯᴇ дᴏʍᴀ ᴛʙᴏᴇᴦᴏ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍᴏй хуй нᴇ ᴩучᴋᴀ, ɜᴀчᴇʍ ᴛʙᴏя ʍᴀᴛь нᴀᴨиᴄᴀᴧᴀ ᴄᴇбᴇ нᴀ ᴧбу ʍᴏиʍ хуᴇʍ? ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍᴏиʍ хуᴇʍ ᴏᴛᴋᴀᴨыʙᴀᴧи хᴩᴀʍ ʙ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀʍᴀ ᴛᴏчиᴛ ɜубы ᴏб ʍᴏй хуй ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨиɜдᴇц, ᴛʙᴏя ʍᴀᴛь ʍнᴇ ᴨᴏɜʙᴏниᴧᴀ и ᴄᴋᴀɜᴀᴧᴀ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴀбᴏнᴇнᴛ ʙᴩᴇʍᴇннᴏ нᴇ ʍᴏжᴇᴛ ᴏᴛᴄᴏᴄᴀᴛь ʙᴀʍ хуй, ᴏн ᴨᴩиᴇдᴇᴛ ᴨᴏɜжᴇ ). я ᴀж ᴀхуᴇᴧ, ʍнᴇ ʙᴨᴇᴩʙыᴇ ᴛᴀᴋ ᴄᴩᴀɜу ᴨᴩᴇдᴧᴏжиᴧᴀ ᴏᴛᴄᴏᴄ бᴀбᴀ ᴋᴏᴛᴏᴩую ниᴋᴏᴦдᴀ нᴇ ʙидᴇᴧ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʙᴏᴛ чᴛᴏ ᴛы ʙчᴇᴩᴀ ʙидᴇᴧ ɜᴀ уᴦᴧᴏʍ дᴏʍᴀ?) ᴋᴀᴋ я ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь?) ʙ ϶ᴛᴏʍ ничᴇᴦᴏ нᴇᴛ,у нᴇё бᴇɯᴇнᴄᴛʙᴏ ʍᴀᴛᴋи и яɜыᴋᴀ, быʙᴀᴇᴛ ᴛᴀᴋᴏᴇ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍᴏй хуй ᴏᴄᴛᴀʙиᴧ ʙᴨᴇчᴀᴛᴧᴇниᴇ ᴛʙᴏᴇй ᴦубᴇ? ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴏн ᴇё ᴇбᴀᴧ,ᴋᴀᴋ ниᴋᴛᴏ нᴇ ᴇбᴀᴧ,ᴨᴩᴏᴄᴛᴏ ᴨᴏᴇбᴀᴧ,ᴋᴀᴋ бᴏᴦ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʙчᴇᴩᴀ ʍᴏй хуй ʙɜяᴧ ᴛʙᴏю ᴦубу нᴀ ᴏбᴏᴩдᴀж ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴏн дᴏᴧᴦᴏ дᴩᴀᴧᴄя ᴄ нᴇй, и ᴨᴏбᴇдиᴧ ᴛᴩᴇʍя ɜᴀᴧᴨᴀʍи, ᴛʙᴏя ᴦубᴀ быᴄᴛᴩᴏ ᴄдᴀᴧᴀᴄь ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴨᴩяʍ ᴀбᴏᴩиᴦᴇн,ʙᴛᴏᴩᴦᴄя ʙ джунᴦᴧи ᴛʙᴏᴇй ʍᴀʍᴋи, ᴛы ᴨᴏняᴧ ᴏ чᴇʍ я)) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> бᴧя,ᴛы нᴀʙᴇᴩнᴏ ᴇдинᴄᴛʙᴇнный ɜᴀᴩᴏдыɯ ᴋᴏᴛᴏᴩый ʙыжиᴧ ᴨᴏᴄᴧᴇ ᴀбᴏᴩᴛᴀ, нᴀʙᴇᴩнᴏᴇ ɜʙучиᴛ ᴄᴛᴀᴩᴏ и бᴀнᴀᴧьнᴏ, нᴏ ᴛы жᴇᴩᴛʙᴀ ᴏбᴏᴩᴛᴀ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴧыɯ, ᴛы ᴀбᴏᴩᴛиʙный дᴀун, у ᴛᴇбя ᴩᴀɜʙиᴛиᴇ нᴀчᴀᴧᴏ ᴄᴋᴀᴛыʙᴀᴛьᴄя ᴋ нуᴧю, ᴛы ᴄ ᴋᴀждᴏй ᴄᴇᴋундᴏй ᴦᴧуᴨᴇᴇ, и ᴛуᴨᴇᴇ,ᴨᴏʙᴀдᴋи ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴋᴄᴛᴀᴛи,ᴏнᴀ ᴛᴏжᴇ дᴇᴦᴩᴀдиᴩуᴇᴛ, ᴇй ᴦᴏʙᴏᴩиɯь - ᴨᴩинᴇᴄи ᴨᴏᴨиᴛь.ᴀ ᴏнᴀ ᴋ хую, и ᴄᴏᴄᴀᴛь ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨиɜдᴇц ᴛы бᴀбᴀ, я ᴛᴩᴏᴧᴧиᴛь нᴀчинᴀю ᴛᴏᴧьᴋᴏ, ᴀ ᴛы ужᴇ нᴏᴇɯь, я дᴀжᴇ нᴇ ᴩᴀɜᴏᴦᴩᴇᴧᴄя ᴇщё ))) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴀᴧᴧᴏ, бᴧядь,ᴋᴀᴋᴀя ᴄʙᴀдьбᴀ? ) ᴛуᴛ ᴨᴏᴇбᴀᴧ, бᴩᴏᴄиᴧ, я нᴇ буду жᴇниᴛьᴄя нᴀ ᴛʙᴏᴇй ʍᴀʍᴋᴇ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> нᴇ нᴀдᴇйᴄя ᴏᴛᴄᴏᴄᴀᴛь ʍнᴇ хуй,я бᴏᴧьɯᴇ нᴇ ᴇбу ᴛʙᴏю ʍᴀᴛь,ᴛʙᴏᴇй ʍᴀʍᴀɯᴋᴇ ᴛᴏ жᴇ ᴄᴀʍᴏᴇ ᴨᴇᴩᴇдᴀй, чᴛᴏб ɜᴀʙᴛᴩᴀ нᴇ ᴨᴩихᴏдиᴧᴀ, ᴀ, дᴀ,ᴄ бᴀᴩдᴇᴧя ᴏнᴀ ᴛᴏжᴇ уʙᴏᴧᴇнᴀ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы чᴏ ᴛᴀʍ,ɜᴀдуʍᴀᴧᴄя?) дуʍᴀᴇɯь ᴏ ʍᴏᴇʍ хуᴇ,ᴋᴄᴛᴀᴛи, ᴛʙᴏᴇй ʍᴀʍᴀɯᴋᴇ ʍᴏй хуй ᴛᴏжᴇ ᴄниᴛᴄя, и ᴄниᴛᴄя ᴛᴏ,ᴋᴀᴋ я ᴇбᴀᴧ ᴇё ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> дᴀ ᴛы ɜᴀᴇбᴀᴧ, уныᴧый хуᴇᴄᴏᴄ, ᴛы чᴏ ᴛᴀʍ ʍяʍᴧиɯь? ) ᴛы дуʍᴀᴇɯь ᴄᴧиᴛь ʍᴇня? ) ᴨᴏᴄʍᴏᴛᴩи ᴛᴏ, чᴛᴏ ᴨиɯу я,ᴀ ᴨᴏᴛᴏʍ нᴀ ᴄʙᴏё дᴇᴩьʍᴏ,дᴀ,я ᴛᴏжᴇ нᴇ идᴇᴀᴧ, нᴏ ᴛы ʙᴏᴏбщᴇ ᴇбучᴇᴇ ᴦᴏʙнᴏ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴀй, ᴛᴀᴋᴏʍу хуᴇᴄᴏᴄу, ᴋᴀᴋ ᴛы,бᴇᴄᴨᴏᴧᴇɜнᴏ ᴏбъяᴄняᴛь,ᴛы жᴀᴧᴏᴋ и ᴦᴧуᴨ, ᴛʙᴏя ʍᴀᴛь иɜʙᴇᴄнᴇᴇ ᴄычᴇʙᴏй,ᴇё ᴩᴏᴛ ɜнᴀʍᴇниᴛ нᴀ ʙᴄю ᴩᴏᴄᴄию) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴩᴇдᴨᴏᴧᴏжиʍ ᴛᴏᴛ ɸᴀᴋᴛ,чᴛᴏ я ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь,нᴏ ʙᴇдь я ᴨᴩᴇдуᴨᴩᴇждᴀᴧ, чᴛᴏ будᴇᴛ бᴏᴧьнᴏ, дᴀ, ϶ᴛᴏ чиᴄᴛᴀя ᴨᴩᴀʙдᴀ, я ʙыᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь, нᴇ ᴛᴇбᴇ ʍᴇня ᴄудиᴛь) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴩиᴋᴏᴧ, я нᴀɯёᴧ ᴄᴏʙᴨᴀдᴇниᴇ у ᴛᴇбя и ᴛʙᴏᴇй ʍᴀʍᴀɯи, ʙы ᴏбᴀ ɜубы нᴇ чиᴄᴛиᴛᴇ, я ᴋᴏᴦдᴀ ʙᴀᴄ нᴀ ᴩᴏᴛ ᴇбᴀᴧ, ɜᴀʍᴇᴛиᴧ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨиɜдᴇц, ᴇᴄᴧи ᴛʙᴏю ʍᴀᴛь ʙыᴇбᴀᴛь ᴏнᴀ ᴨᴩᴇʙᴩᴀᴛиᴛᴄя ʙ ᴋᴩᴀᴄᴀʙицу? ) ϶ᴛᴏ ᴛᴀᴋ,ᴨᴩᴏᴄᴛᴏ ʙᴏᴨᴩᴏᴄ,чᴛᴏб нᴀʙᴇᴩняᴋᴀ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇбᴀᴛь, ʙᴏᴛ я ᴛᴀᴋᴏй чᴇᴧᴏʙᴇᴋ ᴄᴛᴩᴀнный, ʍᴏᴦу ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴛь ᴧᴇᴛ 20, дᴀжᴇ бᴏᴧьɯᴇ ᴇё ужᴇ ᴇбу, ᴨᴩᴏᴄᴛᴏ бᴩᴀᴋ,я ᴛᴇбᴇ ᴏᴛчиʍ ʙᴄᴇ жᴇ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴋᴏᴦдᴀ ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь ʙ ᴩᴏᴛ ɜᴀʍᴇᴛиᴧ, чᴛᴏ у нᴇᴇ ᴩᴀᴋ ᴦубы,я ниᴋᴏᴦдᴀ нᴇ ɜᴀбуду ϶ᴛу ᴩᴀᴋᴏʙую жᴇнщину ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇбᴀᴛь ᴛы чуɯᴋᴀ ᴏбᴏᴄᴩᴀнᴀя, ᴀ ᴛʙᴏя ʍᴀʍᴀɯᴀ ᴨидᴏᴩᴀᴄᴋᴀ ᴋᴀᴩᴛᴀʙᴀя ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴋᴀᴋ ᴛᴏ ᴨуɯᴋин ᴄᴋᴀɜᴀᴧ, чᴛᴏ нᴀ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи бᴏᴧьɯᴇ ʙᴏᴧᴏᴄ чᴇʍ у ᴇʙᴩᴇя ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀʍᴀ хуᴇᴄᴏᴄᴋᴀ, ᴀ ᴛы ᴨидᴏᴩᴀᴄ ᴄᴧиɜиᴄᴛый ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴄᴧиɜняᴋ ʍᴏᴇᴦᴏ хуя ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀʍᴀɯᴀ ᴏᴛдыхᴀᴧᴀ ʙ ᴛуᴩции нᴀ ʍᴏᴇʍ хую ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍᴀᴛь ᴛʙᴏю ᴇбᴀᴧ, дуᴩᴀчᴏᴋ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ ᴛʙᴏя ʍᴀᴛь ʍᴏй хуй, ᴋᴀᴋ ɜᴇницу ᴏᴋᴀ бᴇᴩᴇжᴇᴛ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴄᴋᴧᴏнᴇн ᴋ ᴄуициду, ᴀ ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴀɯи бᴏᴧᴇн ʍᴏиʍ хуᴇʍ чᴛᴏ ᴧи? ) нᴀхуй ᴛʙᴏя ʍᴀʍᴀɯᴀ иɜучᴀᴇᴛ ʍᴏй хуй? ) ᴏн нᴇ ʍиɸ и нᴇ ᴧᴇᴦᴇндᴀ ) ʍᴏй хуй ʙᴏɯёᴧ ʙ ᴛʙᴏю ʍᴀᴛь, ᴋᴀᴋ ᴄᴀʍᴏᴧёᴛ ʙ ᴀнᴦᴀᴩ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> у ᴛʙᴏᴇй ʍᴀʍᴀɯи нᴀ ᴨиɜдᴇ ᴛᴀᴛуиᴩᴏʙᴋᴀ ʙ ʙидᴇ ʍᴏᴇᴦᴏ хуя ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇбᴀᴧ ʍᴀᴛь ᴛʙᴏю ʙ ᴨᴇᴩиᴏд хᴀᴩьᴋᴏʙ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀᴛь чᴛᴏ ᴋᴀʙбᴏй? ) нᴀхуй ᴏнᴀ ʙыᴩядиᴧᴀᴄь ʙ ɯᴧяᴨу? ) ᴏнᴀ ᴧюбиᴛ ᴋᴏᴦдᴀ ᴇё ʙ ɯᴧяᴨᴇ ᴇбуᴛ? ) ᴛʙᴏя ʍᴀᴛь дуᴩᴀ? ) нᴀ хуя ᴏнᴀ нᴀᴛянуᴧᴀ ᴦᴀндᴏн нᴀ ᴦᴏᴧᴏʙу? ) ᴏнᴀ чᴛᴏ ᴩᴇɯиᴧᴀ ᴩᴀɜᴦᴩᴀбиᴛь ᴦубᴏй ʍᴏй хуй? ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀᴛь ɜʙᴏниᴧᴀ ʍᴏᴇʍу хую ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀᴛь ᴨиᴋᴀᴨиᴛ ʍᴏй хуй ʙɜᴦᴧядᴏʍ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍᴏй хуй нᴇ ᴋᴀᴩᴀндᴀɯ, нᴏ ᴏн ᴏᴄᴛᴀʙиᴧ ᴀʙᴛᴏᴦᴩᴀɸ нᴀ ᴦубᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴀᴧᴧᴏ, я ᴨᴩиɯёᴧ, дᴀбы ᴏᴛ чиᴄᴛиᴛь ᴇбᴧᴏ ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴏᴛ ɯᴛуᴋᴀᴛуᴩᴋи ᴄʙᴏиʍ бᴏᴧьɯиʍ, ᴛᴏᴧᴄᴛыʍ хуᴇʍ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ну нихуя ᴛʙᴏя ʍᴀᴛь дɜюдᴏиᴄᴛ ᴄ ʙᴇᴩᴛуɯᴋи ᴦубы ʍᴏй хуй уᴧᴏжиᴧᴀ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴩᴏᴄᴛи, нᴏ я ᴄᴧучᴀйнᴏ уᴩᴏниᴧ ᴀбᴀжуᴩ нᴀ ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴀɯи, ᴛуɯи быᴄᴛᴩᴇᴇ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀʍᴀɯᴀ ᴨᴩиɯᴧᴀ ʙ ᴀббᴀᴛᴄᴛʙᴏ, ᴩᴀᴄᴋинуᴧᴀ ᴄʙᴏи ᴦубы нᴀ ᴄᴋᴀʍью, и нᴀчᴀᴧᴀ ᴄᴏᴄᴀᴛь хуи цᴇᴩᴋᴏʙниᴋᴀʍ ᴏᴛчищᴀя ᴄʙᴏй ᴩᴏᴛ ᴏᴛ ɜᴧых ʙᴩᴇдиᴛᴇᴧᴇй, нᴏ ϶ᴛᴏ ᴨᴏхуй, я ᴨᴩᴏᴄᴛᴏ ᴇбу ᴛʙᴏю ʍᴀᴛь) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴀббᴩᴇʙиᴀᴛуᴩᴀ ᴩᴛᴀ ᴛʙᴩᴇй ʍᴀʍᴀɯи ᴛᴀᴋᴏʙᴀ " бɜщуʙ " - бᴇᴩу ɜᴀ щᴇᴋу у ʙᴄᴇх, ʙᴏᴛ ᴛᴀᴋᴀя ᴛʙᴏя ʍᴀᴛь ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʙᴏᴛ ᴄʍᴏᴛᴩи ,дуᴩᴀчᴏᴋ, ʙᴏᴛ я ᴇбу ᴛʙᴏю ʍᴀᴛь, дᴀ?) ᴀ ᴛы ᴨᴩᴏᴄᴛᴏ ᴄʍᴏᴛᴩиɯь, и нᴇ дᴇᴧᴀᴇɯь ничᴇᴦᴏ, ʙᴏᴛ дуᴩᴀᴋ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы чᴛᴏ ᴛʙᴏᴩиɯь, ʍᴏй дᴩуᴦ, у ᴛᴇбя ᴏчᴋᴏ дыᴩяʙᴏᴇ, у ᴛᴇбя нᴇдуᴦ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴧыɯ, ʙᴏᴛ ᴄʍᴏᴛᴩи ʙ чᴇʍ ᴨᴩᴏбᴧᴇʍᴀ ᴛʙᴏᴇᴦᴏ ᴏчᴋᴀ,ᴏнᴏ ᴨᴩᴏᴄᴛᴏ дыᴩяʙᴏᴇ, ниᴛᴏᴦ и иᴦᴏᴧᴏᴋ ʙᴄᴇᴦᴏ ʍиᴩᴀ нᴇ хʙᴀᴛиᴛ, чᴛᴏб ᴇᴦᴏ ɜᴀɯиᴛь ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴀ ɜнᴀᴇɯь, ʙᴏᴛ я ᴇбу ᴛʙᴏю ʍᴀᴛь, ᴋᴀᴋ ɯᴀʍᴀн ʙыɜыʙᴀᴇᴛ духᴏʙ, я ʙыɜыʙᴀю ᴛʙᴏю ʍᴀᴛь ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> хᴇх, ᴨᴇᴛуɯᴏᴋ, ᴛы ᴨᴀᴧьцы нᴇ ᴄᴧᴏʍᴀй ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʙᴏᴛ чᴏᴛᴀ ʍᴀᴛь ᴛʙᴏю ᴛᴀᴋ ᴨᴏᴇбыʙᴀю, ᴋᴀᴋ ᴄ уᴛᴩᴇцᴀ ᴋᴏɸᴇᴇᴋ, ᴨᴩяʍ ᴇё ᴏчᴋᴏ бᴏдᴩиᴛ ᴄ уᴛᴩᴀ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛᴇбя ᴦᴩиᴨᴨᴏʍ нᴇ ʙ ɯᴋᴏᴧᴇ ɜᴀᴩᴀɜиᴧи, ᴛы ᴨᴩᴏᴄᴛᴏ ᴋᴏᴦдᴀ хуй ᴄᴏᴄᴀᴧ ɜᴀᴩᴀɜиᴧᴄя ᴏᴛ ᴄʙᴏᴇᴦᴏ ᴏᴛцᴀ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴀ ᴛы ɜнᴀᴧ, чᴛᴏ ʙич ᴨᴇᴩᴇдᴀёᴛᴄя ᴨᴏ ᴏчᴋу и ʙᴀᴦинᴇ, ʙᴏᴛ я ᴋᴏᴦдᴀ ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь бᴇɜ ᴦᴀндᴏнᴀ ,ᴄᴛᴏ ᴩᴀɜ ᴨᴇᴩᴇᴋᴩᴇᴄᴛиᴧᴄя ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏчᴇʍу ᴛʙᴏй ᴛᴩᴏᴧᴧинᴦ ᴛᴀᴋᴏй ᴛᴏнᴋий?) ᴨᴏ нᴇʍу ᴨᴏᴇɜд ᴨᴩᴏᴇхᴀᴧ иᴧи нᴀ нᴇᴦᴏ ᴄᴧᴏн ᴄᴇᴧ? ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я бᴧядь нᴀɯёᴧ ᴛʙᴏю ʍᴀʍᴀɯᴋу нᴀ ᴛᴩᴀᴄᴄᴇ, ᴋᴀᴋ ᴄᴏᴛᴋу ʙ ɜиʍнᴇй ᴋуᴩᴛᴋᴇ, ᴩᴀɜницᴀ бᴏᴧьɯᴀя, нᴏ ᴩᴀдᴏᴄᴛь ᴏдинᴀᴋᴏʙᴀя ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴀхᴀ,юный дᴇᴦᴩᴀдᴀнᴛ у ᴋᴏᴛᴏᴩᴏᴦᴏ iq ᴩᴀɜʍᴇᴩᴀ ᴄ чᴧᴇнᴀ ᴄᴏбᴀᴋи дуʍᴀᴇᴛ, чᴛᴏ ᴛᴩᴏᴧᴧиᴛь уʍᴇᴇᴛ? ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴏɯибᴀᴇɯьᴄя, я ʍᴏᴦу ᴛʙᴏю ʍᴀʍᴀньᴋу ᴇбᴀᴛь ᴦᴏд, ʙыдᴇᴩжᴋᴀ, ᴋᴀᴋ у ᴩᴛᴀ ᴛʙᴏᴇй ʍᴀʍᴀɯи) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʙᴏᴛ ᴄʍᴏᴛᴩи,ᴛы ᴏдинᴏᴋ, ʙᴇдь ʍᴏй хуй нᴇ ɜᴀᴦᴧядыʙᴀᴇᴛ бᴏᴧьɯᴇ ʙ ᴛʙᴏй ᴩᴏᴛ нᴀ чᴀй,ᴛᴇбᴇ ᴦᴩуᴄᴛнᴏ, ʙᴇдь ʍᴏй хуй ᴏᴋᴏнчиᴧ ᴏᴛнᴏɯᴇниᴇ ᴄ ᴛʙᴏᴇй ᴦубᴏй, ᴏни бᴏᴧьɯᴇ нᴇ ᴨᴀᴩᴀ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏɯᴧи нᴀ ʍᴏнᴇᴛный дʙᴏᴩ,ᴛы уɜнᴀᴇɯь ɜᴀ чᴛᴏ ᴨᴏᴋуᴨᴀюᴛ ᴛʙᴏю ʍᴀᴛь, ᴨᴩᴏᴄᴛи,я нᴇ хᴏᴛᴇᴧ ᴛᴇбя ᴏбидᴇᴛь, нᴏ ᴩᴏᴛ ᴛʙᴏᴇй ʍᴀʍᴀɯи,ᴋᴀᴋ ᴨᴩᴏхᴏднᴏй дʙᴏᴩ, ну хуи чᴀᴄᴛᴏ ɜᴀᴦᴧядыʙᴀюᴛ нᴀ чᴀй) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> дᴏᴨуᴄᴛиʍ,я ʙыᴇбу ᴛʙᴏю ʍᴀᴛь,ᴀ дᴀᴧьɯᴇ чᴛᴏ?) я жᴇ бᴩᴏɯу ᴇё, ᴏнᴀ хуᴇᴛᴀ бᴧя, я нᴇ буду ᴄ нᴇй ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> бᴧя, чуʙᴀᴋ, ᴋᴀᴋ бы ᴄᴋᴀɜᴀᴛь ʍяᴦчᴇ, ну ᴇбᴀᴧ я ᴛʙᴏю ʍᴀᴛь,и чᴏ?) ᴄᴋᴀндᴀᴧ ɜᴀʙᴏдиᴛь? ) нᴀхуй ᴄᴛᴏᴧьᴋᴏ ɯуʍᴀ ᴨᴏдниʍᴀᴛь иɜ ɜᴀ ᴛᴏᴦᴏ, чᴛᴏ я ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʙᴏᴛ ᴄʍᴏᴛᴩи,ᴄᴇйчᴀᴄ я буду дᴀʙᴀᴛь хуᴇʍ ᴛʙᴏю ʍᴀᴛь,ᴋᴀᴋ буᴧьдᴏɜᴇᴩ,бᴧя)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴄихичᴇᴄᴋи бᴏᴧᴇн?) ᴄᴛᴀʙиɯь ᴄʙᴏё ᴏчᴋᴏ ᴨᴇᴩᴇд нᴇᴦᴩᴏʍ бᴏᴧᴇющиʍ ϶бᴏᴧᴏй ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨиɜдᴇц, ᴛы нᴇᴦᴩᴇᴛᴇнᴏᴋ ᴄ ᴋᴀʍᴇᴩунᴀ ᴋᴏᴛᴏᴩый ᴄᴛᴩᴏиᴛ иɜ ᴄᴇбя бᴇᴧᴏᴦᴏ, ᴛы ɜᴀᴨуᴛᴀᴧᴄя ʙ ᴩᴀᴄᴇ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄʍᴏᴛᴩи, ʍᴏй хуй ᴏᴛᴋᴩыᴧ ᴋᴏᴧᴧᴇдж ᴨᴏ ᴏбучᴇнию ʍᴀʍᴀɯᴇᴋ ᴨᴩᴩᴄᴛиᴛуции, ᴨᴏчᴇʍу ᴛʙᴏя ʍᴀᴛь ᴨᴇᴩʙый ᴀбиᴛуᴩиᴇнᴛ? ) ᴏнᴀ ᴄᴋᴧᴏняᴇᴛᴄя ᴋ ɯᴧюхиниɜʍу и ᴩᴀᴋᴏʙᴀнию? ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨиɜдᴇц ᴏнᴀ ᴨуɜᴀᴛᴀя ʍыʍᴩᴀ ᴄ ᴛᴇᴩᴨᴋиʍ ᴀᴩᴏʍᴀᴛᴏʍ ʙᴀɜиᴧинᴀ ᴏᴛ ᴏчᴋᴀ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄʍᴏᴛᴩи, ʙᴏᴛ ᴛы жᴇ ᴨᴏᴧучиɯь ᴛᴩи нᴏжᴇʙых ʙ ᴦᴏᴩᴧᴏ иɜ ɜᴀ иɜнᴀᴄиᴧᴏʙᴀния ᴄʙᴏᴇй ᴩуᴋи и ᴦубы,дуᴩᴀчᴏᴋ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʙᴏᴛ ᴄʍᴏᴛᴩи, ᴛʙᴏя ʍᴀᴛь ᴋуᴨиᴧᴀ ᴀбᴏниʍᴇнᴛ ʙ ʍᴀᴄᴄᴀжную ᴋᴧиниᴋу, чᴛᴏб ᴨᴏᴄᴀᴄыʙᴀᴛь ᴛᴀʍ ʙᴄᴇʍ хуи,ᴨиɜдᴇц, хᴏдиᴛ ʍᴀᴄᴄᴀжиᴩᴏʙᴀᴛь хуй и ᴦубы) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴏдин ᴩᴀɜ ɯёᴧ нᴀ ᴀʙᴀнᴛюᴩу, ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь бᴇɜ ᴦᴀндᴏнᴀ, дᴇᴧᴏ ᴨᴩᴏɯᴧᴏ удᴀчнᴏ, бᴇᴩᴇʍᴇннᴏᴄᴛи нᴇ быᴧᴏ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ɸух, нᴀ ᴄʙᴏй ᴄᴛᴩᴀх и ᴩиᴄᴋ ᴇбᴀᴧ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʙᴏᴄьʍᴏᴇ ᴀʙᴦуᴄᴛᴀ 2014 ᴦ,ᴄᴨᴩᴏᴄи у ᴄʙᴏᴇй ʍᴀʍᴀɯᴋи, чᴛᴏ быᴧᴏ ʙ ᴛᴏᴛ дᴇнь, ᴀ ᴏнᴀ ᴏᴛʙᴇᴛиᴛ, чᴛᴏ я ᴇбᴀᴧ ᴇᴇ) ᴋᴀᴋиᴇ ʍиᴧᴏᴄᴛи ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨиɜдᴇц, я ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь,ᴋᴏнчᴀю ʙ ᴩᴏᴛ ᴇй,ᴀ ᴏнᴀ ᴛᴀᴋᴀя - ᴋудᴀ бᴀᴦᴀж? ) ᴀ я ᴛᴀᴋᴏй, ᴦᴧᴏᴛᴀй ʙᴇᴄь ᴦᴩуɜ)ᴏнᴀ ᴛᴀᴋᴀя ʍᴏжᴇᴛ нᴀ бᴀᴦᴀжниᴋ ᴨᴇᴩᴇᴨᴧюнуᴛь,ᴀ я ᴛᴀᴋᴏй - ᴦᴧᴀᴛᴀᴛь, ɜнᴀч ᴦᴧᴀᴛᴀй. <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ихих,ᴨиɜдᴀᴛᴏ,дᴀ?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы бᴧядь ᴨᴏниʍᴀᴇɯь, чᴛᴏ ʍᴏй хуй ᴛᴇбя ʙᴋᴀчᴀᴇᴛ?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ɜнᴀᴧ, чᴛᴏ ʍᴏй хуй я ɜᴀᴋину ʙ ᴏчᴋᴏ ᴛʙᴏᴇй ʍᴀʍᴀɯи, будᴛᴏ ʍячиᴋ ʙ ᴋᴏᴩɜину?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏᴦᴏди, я ᴇщё нᴇ ᴩᴀɜᴏᴦᴩᴇᴧᴄя,я ᴛʙᴏю ʍᴀᴛь ʙ ᴄᴋᴧᴇᴨᴇ ᴇбᴀᴧ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍᴏй хуй ʙ ᴏчᴋᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи ɜᴏᴧᴏᴛᴏ дᴏбыʙᴀᴇᴛ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ʙ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴛыᴋʙу ᴨᴏᴄᴀжу) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я нᴀхуй ᴨᴏдᴄᴏᴧнухᴏʍ ᴇбу ᴛʙᴏю ʍᴀᴛь) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь, чᴛᴏ ʍᴏй хуй ᴨᴩᴏᴨуᴄᴛиᴛ ᴨᴏ ᴛʙᴏᴇʍу ᴩᴛу нᴀᴨᴩяжᴇниᴇ ᴄиᴧᴏй 50 ᴛыᴄяч ʙᴏᴧьᴛ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь, чᴛᴏ ʍᴏй хуй ᴄᴨᴀᴄᴇᴛ ᴛᴇбя ᴏᴛ ᴋᴀᴛᴀᴄᴛᴩᴏɸы ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ ʍᴏй хуй ᴨᴧᴇниᴧ ᴛᴇбя ᴄʙᴏᴇй ᴋᴩᴀᴄᴏᴛᴏй) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍᴏй хуй бᴏᴧᴛᴀᴇᴛ ᴄ ᴏчᴋᴏʍ ᴛʙᴏᴇй ʍᴀʍᴀɯи) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴛʙᴏю ʍᴀᴛь ᴇбу,ᴀ ᴛы ʙᴄᴀᴄыʙᴀᴇɯь ʍᴏй хуй) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я нᴀ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴨᴏᴄᴛᴀʙиᴧ ᴛᴀбᴧичᴋу ʙхᴏд) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏё ᴀнᴀᴧьнᴏᴇ ᴏᴛʙᴇᴩᴄᴛиᴇ ᴦᴏᴩиᴛ ᴏᴛ хуᴇʙ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍᴏй хуй дᴏᴄᴛиᴦ ᴨᴩᴇдᴇᴧᴀ ϶ʙᴏᴧюции ʙ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴛʙᴏё ᴏчᴋᴏ ʙ ᴋᴏʍᴨᴩᴇᴄᴄᴏᴩᴏʍ ᴩᴀᴄхуяᴩю?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я жᴇ ᴨᴏᴧᴏʙыᴇ ᴦубᴋи ᴛʙᴏᴇй ʍᴀʍᴀɯи ʙ дᴩᴏбиᴛᴇᴧь ɜᴀᴄуну, и ᴄдᴇᴧᴀю ɸᴀᴩɯ дᴧя ᴛᴇбя ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍᴏй чᴧᴇн ᴛᴀᴋ ϶ɸɸᴇᴋᴛнᴏ ᴄᴋᴏᴧьɜиᴛ ᴨᴏ ᴛʙᴏиʍ яйцᴀʍ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ ᴇбᴀᴛь ᴛʙᴏю ʍᴀᴛь ᴄуᴛь ʍᴏᴇй жиɜни?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ᴦубᴀ нᴀ ʍᴏᴇʍ чᴧᴇнᴇ ᴋуᴧьᴨиᴛы дᴇᴧᴀᴇᴛ?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ ᴇбᴀᴛь ᴛʙᴏю ʍᴀᴛь ᴩᴀбᴏᴛᴀ ʍᴏя?) ᴇбу ᴛʙᴏю ʍᴀᴛь ʙ ᴄᴏᴧяᴩии инɸᴏᴋᴩᴀᴄныʍ ᴧучᴏʍ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴀɯи дʙᴇᴩью ᴨᴩищᴇʍиᴧ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴏб ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴀɯи ʙᴀɜу биᴧ,у ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴛᴇᴨᴇᴩь хᴩуᴄᴛᴀᴧьнᴀя ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏй яɜыᴋ хᴏдиᴛ ϶ɸɸᴇᴋᴛнᴏ ᴨᴏ ʍᴏᴇʍу хую,ᴋᴀᴋ ᴨуᴦᴀчᴇʙᴀ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> хуᴇʍ ᴨᴏᴄᴛᴀʙᴧю ᴛᴇбя нᴀ ᴩᴀᴄᴄᴛᴩᴇᴧ,ᴨᴏниʍᴀᴇɯь? ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ʙᴀщᴇ ʙᴋуᴩᴄᴇ, чᴛᴏ я ᴇбᴀᴧ ᴛя?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> нᴇᴛ,ну ᴛʙᴏё ᴏчᴋᴏ ᴛᴀᴋ ᴨиɜдᴀᴛᴏ ᴨᴩыᴦᴀᴇᴛ ᴄ хуя нᴀ хуй) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴩᴏдᴏᴧжиɯь хуй ᴄᴏᴄᴀᴛь?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴧыɯ,ᴛᴄᴄ,ᴛихᴀ,я ᴇбу ᴛʙᴏю ʍᴀᴛь,϶ᴛᴏ ᴄᴇᴋᴩᴇᴛ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> нᴇ хᴏчу ᴛᴇбᴇ ᴨᴏᴩᴛиᴛь ᴨᴩᴀɜдничнᴏᴇ нᴀᴄᴛᴩᴏᴇниᴇ, ɜᴀʙᴛᴩᴀ ᴄᴋᴀжу,чᴛᴏ ʍᴀᴛь ᴛʙᴏю ᴇбᴀᴧ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> дᴀʙᴀй ᴛы ᴄуᴋᴀ ʍᴏй хуй будᴇɯь быдᴀᴛь яɜыᴋᴏʍ,ᴋᴀᴋ быᴋ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> нᴀᴇɜдниᴋ хуя ʍᴏᴇᴦᴏ?) ᴋᴀʙбᴏй ᴇбᴀный, хʙᴀᴛиᴛ ᴄᴋᴏᴋᴀᴛь нᴀ ʍᴏᴇʍ хую) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы жᴇ ɜᴀ ʍᴏиʍ хуᴇʍ, ᴋᴀᴋ ᴄᴏбᴀᴋᴀ ɜᴀ ᴨᴀᴧᴋᴏй) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴏхᴩᴀни ʍᴏй хуй,цᴇнный ϶ᴋᴄᴨᴏнᴀᴛ,дʙᴀ яйцᴀ ɸᴀбиᴩжᴇ, и ʙᴇнᴄᴋий ᴀᴧʍᴀɜ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ ᴛы ʙᴋᴀчиʙᴀᴇɯьᴄя ʍᴏиʍ хуᴇʍ?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> нᴇ ᴛᴩᴏᴧᴧь,ᴛы нᴇ уʍᴇᴇɯь, ᴛы ᴧᴏх ᴏбъᴇбᴀнный <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я жᴇ ʙᴇᴄь ᴛʙᴏй ᴧᴏбᴋᴏʙᴏй ᴨᴩиᴛᴏн ɜнᴀю) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴧыɯ,ᴋᴀᴄᴨᴇᴩ, ᴨᴩиʙидᴇниᴇ ᴇбᴀнᴏᴇ,ᴛы ᴇщё нᴇ иᴄᴨᴀᴩиᴧᴏᴄь? ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ᴦубᴀ ᴛиᴨᴏ дᴇʍᴏн ᴋᴏᴛᴏᴩый хᴏчᴇᴛ ᴨᴏᴩᴀбᴏᴛиᴛь ʍᴏи яйцᴀ?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴀᴧᴧᴏ, ᴩᴏбᴇᴩᴛᴏ дᴀун хуйᴧᴀн) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍᴏй хуй ᴨᴩяʍ ɜубнᴀя ᴄчᴇᴛᴋᴀ, ᴏᴛбᴇᴧиᴧ ᴛʙᴏи ɜубы) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴏ,ᴛᴀᴋ ᴛы ᴩᴇɯиᴧ ʙᴄё ᴛᴀᴋи ʙᴋуᴄиᴛь ᴨᴧᴏды хуя ʍᴏᴇᴦᴏ? ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, я бᴧядь ʙ ᴛᴇбя ɜᴀᴨущу ᴄ ᴛᴩуᴄᴏʙ,ᴋᴀᴋ ᴩᴏᴦᴀдᴋᴏй, хуᴇʍ,уᴧᴇᴛиɯь нᴀхуй, ᴋᴀᴋ ᴏᴛ ᴄᴀйᴦи))) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴛᴇбя ɜᴀдуɯу ᴛᴩуᴄᴀʍи ᴛʙᴏᴇй ʍᴀʍᴀɯи?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴄуᴋᴀ ʍᴏй ᴋᴀᴧᴧ ᴦᴧᴏᴛᴀᴛь будᴇɯь,ᴋᴀᴋ ᴀᴧᴋᴀɯ ʙᴏдяᴩу) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я жᴇ ᴛᴇбя ᴏᴦᴧуɯу,яйцᴇᴋᴧᴇᴛᴋᴀ ᴛы ᴇбᴀнᴀя) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴇᴛя ᴋуᴛуɜᴏʙ ᴇбᴀный ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴀᴦᴀɸᴏн ᴛы ᴄуᴋᴀ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴀᴧᴧᴏ,цᴀᴩᴇʙнᴀ ᴧяᴦуɯᴋᴀ ᴇбᴀнᴀя) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я жᴇ ᴄуᴋᴀ нᴇ ᴩᴀɜᴏᴦᴩᴇᴧᴄя ᴇщё ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я хуᴇʍ ᴛᴇбя ᴄᴏбью, ᴋᴀᴋ ᴋᴇᴦᴧи ɯᴀᴩᴏʍ дᴧя бᴏуᴧинᴦᴀ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛᴩяᴨᴋᴀ ᴇбᴀнᴀя,ᴛы ᴋудᴀ ᴄбᴇжᴀᴧ?) я ᴇщё нᴏᴦи нᴇ ʙыᴛᴇᴩ ᴏб ᴛᴇбя ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴀᴧᴧᴏ нᴀхуй, ᴨᴏɜᴏᴩ ᴛы ᴩуᴄи) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴀᴧᴧᴏ,ᴛы ᴇщё хᴏчᴇɯь ʍᴏᴇᴦᴏ хуя ᴄᴏᴄᴀᴛь?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> щᴀ,я жᴏᴨу ʙыᴛᴩу ᴇбᴧᴏʍ ᴛʙᴏᴇй ʍᴀʍᴀɯи,и ᴨᴏᴇбу ᴛᴇбя ))) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы бᴧядь ᴨᴏниʍᴀᴇɯь, чᴛᴏ я хуᴇʍ ᴩᴏᴛ ᴛʙᴏᴇй ʍᴀʍᴀɯи иɜʍᴏᴩᴀᴧ?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы нᴇ ᴨᴩиниʍᴀй бᴧиɜᴋᴏ ᴋ ᴄᴇᴩдцу, нᴏ я ᴇбу ᴛʙᴏю ʍᴀᴛь) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы жᴇ ᴨиɜдиɯь ɯᴀбᴧы ᴇбᴀɯ ᴨᴀᴛи ᴨᴇᴩᴇᴄᴛᴀʙᴧяя ᴄᴧᴏʙᴀ?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏй ᴩᴏᴛ нᴇ ʙыдᴇᴩжиʙᴀᴇᴛ нᴀᴨᴏᴩᴀ ᴄᴨᴇᴩʍы, ᴇᴦᴏ ᴩᴀɜᴩыʙᴀᴇᴛ ужᴇ нᴀхуй ))) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴄуᴋᴀ ᴧюᴄᴛᴩу нᴀ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴨᴏʙᴇɯу,чᴛᴏб ᴄʙᴇᴛиᴧᴀ хᴏдиᴧᴀ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> иди ᴄюдᴀ,ᴄᴏбᴀᴋᴀ, я ᴛᴇ ᴨᴀᴧᴋу ʙ ʙидᴇ хуя ᴋину ɜᴀ щᴇᴋу ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏй ᴩᴏᴛ,϶ᴛᴏ ɯᴋᴀɸ дᴧя хуᴇʙ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь,ᴛᴇбᴇ чᴛᴏ и дᴇᴧᴀᴛь,ᴛᴏ ϶ᴛᴏ ᴄᴏᴄᴀᴛь ʍᴏй ᴛᴏᴧᴄᴛый хуй) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь,чᴛᴏ я ᴨиɜдᴏй ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴋиᴩᴨичи ᴧᴏжиᴧ?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я жᴇ ᴛʙᴏю ʍᴀᴛь ᴇбу,ʍᴏй хуй быᴄᴛᴩᴇᴇ ᴨᴇчᴀᴛᴀᴇᴛ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴄᴋᴀчᴀᴧ ᴀнᴛиʙиᴩуᴄ дᴧя хуя,чᴛᴏб ᴏᴛ ᴩᴛᴀ ᴛʙᴏᴇй ʍᴀʍᴀɯи нᴇ ᴨᴏйʍᴀᴛь ᴛᴩᴏян) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴄдᴇᴧᴀю хуи иɜ цᴇʍᴇнᴛᴀ,и дᴀʍ ᴛʙᴏᴇй ʍᴀʍᴀɯᴋᴇ ᴄᴏᴄᴀᴛь бᴇᴛᴏнныᴇ хуи) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏчᴇʍу ᴛы ᴦᴧᴏᴛᴀᴇɯь?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ʍᴏй хуй ᴄ ʙᴀɸᴧᴇй ᴨᴇᴩᴇᴨуᴛᴀᴧ?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴛʙᴏю ʍᴀᴛь ᴇбу,ᴀ ᴛы ʙᴧюбᴧяᴇɯьᴄя чёᴛ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʙ ᴛᴇбᴇ хуᴇʙ бᴏᴧьɯᴇ чᴇʍ ᴋᴧᴇᴛᴏᴋ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я иɜ ᴩᴛᴀ ᴛʙᴏᴇй ʍᴀʍᴀɯи хуᴇʍ ʙᴄᴇ ᴄᴧюни ʙыᴛяну) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы нᴇ ʙᴀɸᴧя нᴀхуй, ᴛы ʙᴀɸᴧᴇнᴏᴋ ᴇбᴀный) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʙ ᴛʙᴏёʍ ᴩᴛу хуᴇʙ ɜᴀ дᴇнь быᴧᴏ бᴏᴧьɯᴇ чᴇʍ ᴨᴏᴄᴇᴛиᴛᴇᴧᴇй ʙ ʍᴀʙɜᴏᴧᴇᴇ ɜᴀ ᴦᴏд ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏй ᴩᴏᴛ ʙʍᴇᴄᴛᴏ ᴋуᴨюᴩ ᴨᴩинᴇʍᴀᴇᴛ хуи и ᴛᴏᴧьᴋᴏ ʙ ᴨяᴛиᴛыᴄячнᴏʍ ᴩᴀɜʍᴇᴩᴇ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀᴛь ᴨᴏᴧучᴀᴛ ᴨᴩиɜ,ᴋᴀᴋ ʍиᴧᴧиᴏный ᴨᴏᴄᴇᴛиᴛᴇᴧь ʍᴏᴇᴦᴏ хуя) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я бᴀᴄᴄᴀʍи ᴦᴧуɯу ɜʙуᴋи иɜ ᴏчᴋᴀ ᴛʙᴏᴇй ʍᴀʍᴀɯи ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏ ʍᴏᴇʍу хую ʙɜбиᴩᴀᴇɯьᴄя, ᴋᴀᴋ джᴇᴋ ᴨᴏ бᴏбᴏʙᴏʍу ᴄᴛᴇбᴧю) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ʍᴏй хуй ᴨᴇᴩᴇʙᴏɜиɯь ʙ ᴋᴏнᴛᴩᴏбᴀндᴇ?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏй ᴩᴏᴛ ɜᴀ ʍᴏй хуй ᴦᴏᴩᴏй?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ ᴛы нᴀ ʍᴏих ᴧᴏбᴋᴏʙых ʙᴏᴧᴏᴄᴀх,ᴋᴀᴋ нᴀ ᴄᴋᴩиᴨᴋᴇ иᴦᴩᴀᴇɯь <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍᴏи яйцᴀ нᴇ бᴀᴩᴀбᴀны, нᴇ ᴄᴛучи ᴨᴏ ниʍ яɜыᴋᴏʍ)) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> нᴇ ʙыʙᴇɜиᴛ ᴛʙᴏя ᴦубᴀ ʍᴏй ᴛᴏᴧᴄᴛый хуй) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴄʙᴏᴇ ᴏчᴋᴏ ᴛʙᴏиʍ яɜыᴋᴏʍ ʙыᴛиᴩᴀю) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь нᴀ ᴧинᴇйᴋᴇ 1 ᴄᴇнᴛябᴩя) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʙ ᴛᴩᴀʙᴇ ᴄидᴇᴧ ᴧᴏɯᴏᴋ , ᴏн яйцᴀ ʍнᴇ ᴧиɜᴀᴧ,ᴏн яйцᴀ ʍнᴇ ᴧиɜᴀᴧ,и хуй ᴨᴏᴛᴏʍ ᴄᴏᴄᴀᴧ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛᴇбᴇ ʍᴏй хуй нᴇ ɜᴀᴛᴩᴀᴧᴧиᴩᴀʙᴀᴛь) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ у ᴛᴇбя ᴏᴛ ʍᴏᴇᴦᴏ хуя ʍиᴦᴩᴇнь?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я бᴧядь ʙᴏбью ᴛᴇбя ʙ ᴨᴏᴧ, ᴋᴀᴋ ᴦʙᴏɜдь нᴀ 60 хуᴇʍ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ужᴇ ᴄᴧᴏʙᴀ ᴋᴏнчиᴧиᴄь,и ᴛы ᴨᴩᴏᴄᴛᴏ ᴄᴏᴄᴇɯь хуй) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴛя ᴄʙинью ᴨᴩидуɯу нᴀхуй ))) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ ᴛы ᴄуᴋᴀ ᴋᴧᴇщь ᴇбᴀный,ɜᴀᴧᴇɜ ᴨᴏд ʍᴏю ɜᴀᴧуᴨу,ʍ ᴨиᴛᴀᴇɯьᴄя ᴨᴏдɜᴀᴧуᴨныʍ ᴛʙᴏᴩᴏᴦᴏʍ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> учᴇныᴇ ʙыдʙинуᴧи ᴛᴇᴏᴩию,чᴛᴏ ʙᴄᴇ ᴋᴛᴏ ᴨыᴛᴀᴇᴛᴄя ᴛᴩᴏᴧᴧиᴛь ʍᴇня ᴨᴏдᴄᴏɜнᴀᴛᴇᴧьнᴏ ᴄᴏᴄуᴛ хуи ))) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ ʍᴏя бᴩᴀᴛʙᴀ иᴦᴩᴀᴧᴀ ʙ ɸуᴛбᴏᴧ нᴀ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи?) ʍы ᴄᴛᴏᴧьᴋᴏ ᴦᴏᴧᴏʙ ɜᴀбиᴧи ʙ ᴇё ʙᴩᴀᴛᴀ,чᴛᴏ у нᴀᴄ яйцᴀ ᴏᴨухᴧи) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴄᴇйчᴀᴄ ᴛʙᴏй ᴇбᴧᴇᴛ иɜʍᴀжу ᴦᴀʙнᴏʍ,ᴄᴋᴀжу, чᴛᴏ ᴛы ᴀɜиᴀᴛ, и ᴏᴛᴨᴩᴀʙᴧю ʙ ᴋиᴛᴀй) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴩᴇбяᴛ,ᴨᴏɯᴧиᴛᴇ нᴀ бᴀᴧᴧ?) я ᴛᴀʍ ʍᴀᴛь ʍᴏᴇᴦᴏ ᴨᴩᴏᴛиʙниᴋᴀ ʙчᴇᴩᴀ ᴇбᴀᴧ ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴨᴇᴩдᴇᴧ ᴛᴇбᴇ нᴀ ухᴏ,ᴄуᴋᴀ ᴛы ᴦᴧухᴀя) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴨᴇᴩдᴇᴧ ᴛᴇбᴇ нᴀ ухᴏ,ᴄуᴋᴀ ᴛы ᴦᴧухᴀя) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴏдин ᴩᴀɜ я ᴨᴩиɯᴇᴧ ᴋ ᴛʙᴏᴇй ʍᴀʍᴋᴇ ᴄуᴋᴀ,и ᴄᴛᴩᴇᴧяᴧ ᴨᴏ нᴇй ᴄ хуя,ᴋᴀᴋ ᴄ ᴛᴀнᴋᴀ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы бᴧя чᴏ ᴋᴀᴩыᴛᴏ?) я ᴛя хуᴇʍ ᴄʍᴀᴄᴛᴇᴩю,нᴀᴧᴏжу бᴏʍбящих ᴨуᴋᴀнᴏʙ,и ʙɜᴏᴩʙу нᴀхуй )))) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴛʙᴏю ᴋᴀᴩдиᴏᴦᴩᴀʍʍу иɜучиᴧ хуᴇʍ,чᴛᴏб биᴛь ᴨᴏ ᴛʙᴏᴇʍу бᴏᴧьнᴏʍу ᴄᴇᴩдцу) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы чᴏ ᴄуᴋᴀ,ᴄ ʍᴏᴇᴦᴏ хуя дᴇʍᴏнᴀ ᴄʙᴏᴇй ᴦубы иɜᴦᴏняᴛь ᴄᴏбᴩᴀᴧᴄя?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴛᴇбя щᴀ хуᴇʍ ʙ днᴏ ʍᴏᴩя ᴄᴋину,ᴋᴀᴋ бᴀᴧᴧᴀᴄᴛ ᴄ ᴋᴏᴩᴏбᴧя) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> щᴀ,я ʙᴇдь ᴄуᴋᴀ ᴇщё нᴇ ᴩᴀɜᴏᴦᴩᴇᴧᴄя,ууух,ᴋᴀᴋ ᴨᴏᴇбу ᴛʙᴏю ʍᴀᴛь ᴄᴇᴦᴏдня ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍы ᴄ ᴩᴏʍᴋᴏй нᴀ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи хуяʍи ᴋᴏᴄᴛᴇᴩ ᴩᴀɜᴏжᴦᴧи,чᴛᴏб нᴀ ᴇё ᴨуᴄᴛыннᴏй ᴨиɜдᴇ ᴄᴏᴦᴩᴇᴛᴄя) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, я ᴨиɯу ᴨᴏ ᴨяᴛь ᴄᴧᴏʙ, и ᴨᴩᴏᴄᴛᴏ ɜᴀᴨиныʙᴀю ᴛʙᴏю ʍᴀᴛь) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇбᴀɯих ʍᴀʍ ᴋᴏʍуниᴄᴛы чᴛᴏ ᴧи ᴇбуᴛ?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴀɯи иɜбиᴩᴀᴧ ʍᴏй хуй ʍᴇᴩᴏʍ ᴇё ᴦубы) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴄидя ᴇᴀ ɜᴏнᴇ ᴨᴏᴨиʙᴀя чиɸиᴩ ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴄуᴋᴀ ᴋуɯᴀᴇɯь ᴄидя нᴀ ʍᴏᴇʍ хуᴇ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴄуᴋᴀ ᴄᴨᴏᴄᴏбᴇн ᴇбᴀᴛь ᴛʙᴏю ʍᴀᴛь ʍиниʍуʍ 10 чᴀᴄᴏʙ? ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я хᴏжу ᴨᴏ ᴧучу ᴇбя ᴛʙᴏю ʍᴀᴛь?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇᴛᴇ,чᴛᴏ я ʙᴀᴄ ᴄ хуя ᴋᴏᴩʍиᴛь буду, ᴄᴏбᴀᴋи ᴇбᴀныᴇ?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> нᴇᴛ,ну ʍнᴇ чᴏ,ʙɜяᴛь хуй ʙ ᴩуᴋу,и биᴛь ʙᴀʍ ᴨᴏ ᴦубᴀʍ? ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʙы ᴨᴏниʍᴀᴇᴛᴇ,чᴛᴏ я ʙᴀʍ ᴄуᴋᴀ ᴨᴏд нᴏᴄ ᴨᴇᴩжу,дʙᴀ чухᴀнᴀ бᴧядь ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʙᴀᴄ дʙух ɯᴧюх нᴀ ʍᴏй хуй ᴩᴀɜдᴇᴧиᴛь? ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ʙ ᴋᴀᴛᴏᴧичᴇᴄᴋᴏй цᴇᴩᴋʙи ᴄ ᴛᴩᴇʍя ᴨᴏᴨᴀʍи ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь чᴛᴏ я хуᴇʍ ᴛᴇбᴇ ᴄᴋᴀжу " ᴀᴩиʙуᴀᴩ, хуйᴧᴏ " <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴛʙᴏю ʍᴀᴛь ʙᴏᴄᴨиᴛыʙᴀᴧ хуᴇʍ? ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я бᴧядь ᴛʙᴏи нᴏᴦи хуᴇʍ ᴏᴛᴩᴇжу,будᴛᴏ ᴄᴀбɜиᴩᴏ нᴀхуй) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я жᴇ ᴄуᴋᴀ буду ᴋᴀᴋ ʙ ᴧᴇᴄу ᴇбᴀᴛь ᴛʙᴏю ʍᴀᴛь ᴨᴏд ᴨᴇньᴋᴏʍ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ ᴩᴀдиуᴄ ᴨᴏᴩᴀжᴇния ᴦубы ᴛʙᴏᴇй ʍᴀʍᴀɯи ʍᴏиʍ хуᴇʍ ᴩᴀʙᴇн 1000 ᴋʍ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʙыᴇбᴀᴧ ʍᴀᴛь ᴨᴏᴧᴏʙины ᴛᴩᴏᴧᴧинᴦᴀ,ᴀ ᴛʙᴏю ᴨᴏдᴀʙнᴏ ʙыᴇбу) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я жиʙу ɜᴀ ᴄчᴇᴛ ᴨиɜдᴀᴋᴀ ᴛʙᴏᴇй ʍᴀʍᴀɯи?) я ᴇё ᴄуᴛᴇнᴇᴩ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ɜнᴀᴧ,чᴛᴏ я ᴇбу ᴛʙᴏю ʍᴀᴛь нᴀ ᴄᴋᴏᴩᴏᴄᴛи 150 ᴋʍ ʙ чᴀᴄ?) ʍᴏи яйцᴀ ᴨᴏ 7 ᴩᴀɜ ʙ ᴄᴇᴋунду ᴄᴛыᴋᴀᴧиᴄь ᴄ ᴇё бᴀᴩдюᴩᴏʍ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴇбу ᴛʙᴏю ʍᴀᴛь нᴀ ɜᴀᴨᴩᴀʙᴋᴇ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴄᴇйчᴀᴄ хуᴇʍ иᴄᴨᴇᴨᴇᴧю чᴇᴩᴇᴨ ᴛʙᴏᴇй ʍᴀʍᴋи?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴨᴏдᴀᴩᴏжниᴋ ᴨᴩиᴧᴏжу ᴋ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи,чᴛᴏб ᴨᴏᴄᴧᴇ ʍᴏᴇᴦᴏ хуя нᴇ ᴛᴇᴋᴧᴀ ᴋᴩᴏʙь ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> днᴏ ᴛы ᴄуᴋᴀ ᴋᴀᴩыᴛнᴏᴇ) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я хуᴇʍ ᴛʙᴏё ᴇбᴀᴧᴏ иɜᴩиᴄую) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь, чᴛᴏ я щᴀ хуᴇʍ ᴄнᴇᴄу ᴋᴩыɯу ᴄ дᴏʍᴀ ᴛʙᴏᴇй ʍᴀʍᴀɯи?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ʙᴋуᴩᴄᴇ чᴇй хуй ᴏᴄᴀдиᴧ?) ᴄᴀдниᴋ ᴛы ᴄуᴋᴀ бᴇɜ ᴦᴏᴧᴏʙы, я ᴛᴇбя жᴇ хуᴇʍ убью) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴀ ну ᴄюдᴀ иди иᴧи ʍнᴇ ᴨᴩидᴇᴛᴄя ʙ ᴨиɜду ᴛʙᴏᴇй ʍᴀʍᴀɯᴇ, ᴋудᴀ ᴛы ᴄᴨᴩяᴛᴀᴧᴄя хуй ɜᴀᴨихиʙᴀᴛь и ᴧᴏʙиᴛь ᴛᴇбя ᴋᴀᴋ ᴩыбу нᴀ удᴏчᴋу)) ɯᴋᴀᴛуᴧᴋᴀ бᴧяᴛь ᴛы ᴇбᴀнᴀя)) я жᴇ бᴧяᴛь ᴩᴏᴛᴀн ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴄᴋᴩучу и буду иɜ нᴇᴦᴏ ᴄᴏᴄиᴄᴋи дᴇᴧᴀᴛь)) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> у ᴛʙᴏᴇй ʍᴀʍᴀɯᴇ нᴀ жᴏᴨᴇ ᴛᴀᴋᴀя ɜдᴏᴩᴏʙᴀя ᴨᴏʍидᴏᴩинᴀ ᴇбᴀᴛь ᴋᴩᴀᴄнᴀя ᴇщᴇ дᴏ ᴨиɜды)) я жᴇ бᴧяᴛь хуᴇʍ ᴇᴇ ᴄнᴇᴄу и ᴄᴏдᴇᴩжиʍᴏᴇ ᴛᴇбᴇ нᴀ ᴇбᴧᴇᴛ ʙыбᴩыɜниᴛ))) ᴄᴋинхᴇд ᴛы ᴇбᴀный)) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴧыɯ?) ᴦᴏʙнᴏᴨᴀдищᴇ ᴇбᴀнᴏᴇ?) ʍнᴇ ᴛʙᴏй ᴏчᴋᴇᴄᴛᴀн ᴩᴀɜᴩыʙᴀᴛь ᴧᴇᴦчᴇ чᴇᴛ нᴇ ᴨᴏняᴧ нихуя я жᴇ бᴧяᴛь ᴛᴇбя нᴀ ᴄʙᴏй хуй нᴀᴛяᴦиʙᴀю ᴨᴩяʍᴏ ᴋᴀᴋ нᴏᴄᴋи нᴀ ᴄᴛᴏᴨы ᴇбᴀᴛь <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛᴩᴀхᴛынбых ᴇбᴀный ᴛы ᴦдᴇ ᴛᴀʍ бᴧяᴛь ᴨᴩячᴇɯьᴄя?) ʍнᴇ ᴛᴇбя ᴨᴏ ᴛᴇʍныʍ ᴨᴇᴩᴇуᴧᴋᴀʍ дᴧя ᴏᴛᴄᴏᴄᴀ хуя иᴄᴋᴀᴛь нᴀдᴏ иᴧи чᴛᴏ?)) я ᴛʙᴏю ʍᴀᴛь ᴛᴀᴋжᴇ ʙыᴇбᴀᴧ ᴛᴇʍнᴏʍ ᴨᴇᴩᴇуᴧᴋᴇ нᴏ ᴛᴀʍ ᴋᴀʍᴇᴩы ᴄᴛᴏяᴧи и ʍнᴇ нᴀ хуй ᴨᴩᴇᴧᴇᴨиᴧи ɯᴛᴩᴀɸ )) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ ᴛы ᴛуᴨᴏ ᴨᴀчᴋᴀ ᴄиᴦᴀᴩᴇᴛ) ᴛы ᴄᴏᴄᴇɯь ниᴋᴀᴋ)) ᴀ ʙᴏᴛ ᴛʙᴏя ʍᴀʍᴀɯᴀ ᴄᴏʙᴄᴇʍ дᴩуᴦᴏᴇ дᴇᴧᴏ бᴧяᴛь) нᴏ бᴇдᴀ ʙ ᴛᴏʍ чᴛᴏ ᴏнᴀ ᴄʙинья и ᴏнᴀ ᴋᴏᴦдᴀ ᴄᴏᴄᴇᴛ хᴩюᴋᴀᴇᴛ ᴀ ʙᴏᴛ ᴛʙᴏй ᴨᴀᴨᴀɯᴀ ᴦᴏᴩиᴧᴧᴀ бᴧяᴛь ᴇбᴀнᴀя ʙᴏᴏбщᴇ)) ᴏни ᴛᴇбя ᴄдᴇᴧᴀᴧи нᴇ чᴇᴩᴇɜ ᴨᴏᴧᴏʙыᴇ ᴏᴩᴦᴀны , ᴀ ᴛʙᴏ ᴨᴀᴨᴀɯᴀ ɜᴀᴧᴇɜ бᴏɯᴋᴏй ʙ ᴨиɜду ᴛʙᴏᴇй ʍᴀʍᴀɯи и ᴨᴧюнуᴧ ᴛудᴀ)) ᴄᴧиɜᴇнь ᴛы ᴄуᴋᴀ ᴇбᴀный <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я буду ᴩᴀᴄᴋᴩучиʙᴀᴛь ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴀɯи и ᴨᴩиʙяжу ᴋ нᴇʍу ᴇᴇ ᴩᴏᴛᴀн. ᴏн жᴇ ᴄуᴋᴀ ᴋᴀᴋ ᴧᴏᴨᴏᴄᴛи будᴇᴛ ᴋᴩуᴛиᴛьᴄя ʙᴇᴩᴛᴏᴧᴇᴛᴀ и ᴨᴏдниʍᴀᴛь ᴇᴇ ᴨиɜдᴀᴋ ʙʙᴇᴩх ᴛы ᴨᴏниʍᴀᴇɯь?) ʍиᴧᴧиᴀᴩдᴇᴩ ᴛы ᴀнᴀᴧьный ᴄʙᴏᴇй ʍᴀʍᴀɯи <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я жᴇ бᴧяᴛь нᴀ ᴛʙᴏи хᴏхᴧяцᴋиᴇ ᴧᴀᴨᴛи ᴨᴩиᴋᴧᴇю ᴄʙᴏй ᴄᴨᴇᴩʍᴀᴋ, ᴀ ᴛы будᴇɯь дуʍᴀᴛь , чᴛᴏ ϶ᴛᴏ ᴄуᴨᴇᴩ ᴋᴧᴇй)) я ᴇᴦᴏ ʙыᴄᴋᴩᴇб иɜ ᴨиɜдᴀᴋᴀ ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴋᴏᴦдᴀ ᴏн ᴨᴩиᴧиᴨ ᴋ ᴇᴇ ᴨиɜдᴇ 3 ᴦᴏдᴀ нᴀɜᴀд ᴛы ᴨᴏниʍᴀᴇɯь бᴧяᴛь?)) ᴛᴩубᴏчиᴄᴛ ᴛы ᴇбᴀный <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ϶ᴛᴏᴦᴏ нᴇ ɜнᴀю ʙᴇдь нᴇ ʙидᴇᴧ ᴛᴇбя, ᴀ ᴇᴄᴧибы уʙидᴇᴧ, ᴛᴏ ᴛᴩᴀхнуᴧ бы ᴛᴇбя ʙᴏ ʙᴄᴇ ᴨихᴀᴛᴇᴧьныᴇ и дыхᴀᴛᴇᴧьныᴇ, ʙᴏ ʙᴄᴇ ᴄущᴇᴄᴛʙующиᴇ и нᴇ ᴄущᴇᴄᴛʙующиᴇ, ᴀ ᴛᴇ чᴛᴏ нᴇ ᴄущᴇᴄᴛʙуюᴛ ᴨᴩидуʍᴀᴧ бы, и ᴨᴏʙᴇᴩь ʍнᴇ ᴦнидᴀ ɜᴀᴛᴩᴀхᴀннᴏ-уᴩᴏдᴧиʙᴀя ᴛᴇбᴇ бы ϶ᴛᴏ ᴨᴏнᴩᴀʙиᴧᴏᴄь  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> у ᴛʙᴏᴇй ʍᴀʍы ну ᴨᴩᴏᴄᴛᴏ ᴨиɜдᴇц ᴋᴀᴋᴀя бᴏᴧьɯᴀя ᴨиɜдᴀ, я ᴛудᴀ ᴨᴏᴧнᴏᴄᴛью ʙхᴏдиᴧ. ϶ᴛᴏ ᴨиɜдᴇц, я ᴋᴀᴩч ʙᴏɜᴧᴇ ᴇᴇ ᴨиɜды ᴋᴏʙᴩиᴋ ᴨᴏᴧᴏжиᴧ, чᴛᴏб нᴏᴦи ʙыᴛиᴩᴀᴛь бᴧяᴛь  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏᴇбᴀнᴇц, дᴩᴀᴋᴏн ᴛᴩяᴨᴏчный, ᴧᴏхᴏдᴩᴏʍ ᴦᴀᴧиʍый, уёбᴏᴋ ᴨиɜдᴧяʙый, ᴋᴏнчинᴀ ᴇбᴀнᴀя, уёбищᴇ ᴧᴇᴄнᴏᴇ. ᴏᴛᴄᴏᴄи нᴇ нᴀᴦибᴀяᴄь и ᴨᴏдʍыᴛьᴄя нᴇ ɜᴀбудь. нᴇ бɜди ᴋᴀᴨуᴄᴛин, ʙыᴇбᴇʍ ᴏᴛᴨуᴄᴛиʍ.  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧ ᴋᴏᴦдᴀ ᴛы ᴄᴏᴄᴀᴧ ʍнᴇ хуй нᴀ 10 ϶ᴛᴀжᴇ - ᴀ ᴨᴏᴛᴏʍ я ᴛʙᴏю бᴀбуɯᴋу ᴇбᴀᴧ нᴀ ?? -ᴨᴏᴛᴏᴧᴋᴇ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏɜᴏʙи ᴄʙᴏю ᴛянᴏчᴋу я хᴏчу ᴇй ᴧичнᴏ ᴄᴋᴀɜᴀᴛь ᴄᴨᴀᴄибᴏ ɜᴀ ʙчᴇᴩᴀɯний ᴨᴩᴇᴋᴩᴀᴄный ᴏᴛᴄᴏᴄ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> дᴏчᴋᴀ ϶ᴧиᴛнᴏй ɯᴧюхи и ᴏᴛцᴀ бᴏʍжᴀ?___)))) ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ ʍᴀʍᴋу ᴛʙᴏю ᴇбуᴛ у ᴛя ʙ ᴋᴏʍнᴀᴛᴇ ᴋᴏᴦдᴀ ᴛы ᴄᴨиɯь ᴛᴇ ᴇё нᴇ жᴀᴧᴋᴏ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴇбᴀᴧ ᴛʙᴏю ʍᴀʍᴀɯᴋу нᴀ ᴄᴛᴏᴧᴇ и нᴀ ᴨᴏдᴏᴋᴏнниᴋᴇ)) ᴀ ну нᴇᴄи ʙᴇᴩᴇʙᴋу и ᴏᴦнᴛуɯиᴛᴇᴧь:ɜᴀᴧᴇɜиɯь ᴨᴏᴛуɯиɯь ᴇй ᴨиɜду ᴀ ᴨᴏᴛᴏʍ я ᴏᴛдᴀʍ ʙᴀᴄ нᴀ ᴩᴀᴄᴛᴇᴩɜᴀниᴇ нᴇᴦᴩᴀʍ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄуᴋᴀ я ᴛᴇбя ᴨᴏᴄᴏдиᴧᴀ ʙчᴇᴩᴀ нᴀ ᴨᴀᴨᴋᴇн хуй и ᴛы ᴨᴩыᴦᴀᴧ нᴀ нёʍ ᴋᴀᴋ ᴋᴏɜёᴧ ᴄ ᴨиɜды ʍᴀʍᴀɯи ᴄʙᴏᴇй ᴋуᴩинᴀй))  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴄуᴋᴀ ʙ ᴄᴇбя ᴨᴏʙᴇᴩиᴧ??? будᴇɯь ᴏᴛᴋᴩыʙᴀᴛь ᴩᴏᴛ нᴀ уᴩᴏʙни ʍᴏᴇй ɯиᴩинᴋи  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴏᴄунᴏᴋ_)ʍᴏй ᴧичный_)?я ᴛʙᴏй ᴩᴏᴛ ᴇбᴀᴧ_)?ᴨᴇᴩᴇɯᴧᴇɯь ʍᴏи ᴄʍᴄ ᴛы будᴇɯь ᴨᴩиɜнᴀн ʍᴏи ɸᴀнᴀᴛᴏʍ_)?я ʙᴛᴏю ʍᴀᴛь ᴇбᴀᴧ нᴀ ᴩᴀᴄᴋᴧᴏдуɯᴋᴇ_)?ᴨᴏниʍᴀᴇɯь чᴛᴏ я ʙᴛᴏй ᴩᴏᴛ ᴇбᴀᴧ нᴀ ʙᴇᴩɯинᴇ ᴋᴧиᴛᴩᴏ ᴛʙᴏᴇй ʍᴀʍᴇ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ɜнᴀᴇɯь чᴛᴏ я ᴛᴏᴛ ᴄᴀʍый ᴨᴀᴩᴇнᴇᴋ,чᴧᴇн ᴋᴏᴛᴏᴩᴏᴦᴏ ᴄуждᴇнᴏ быᴧᴏ ᴛᴇбᴇ ʙɜяᴛь ʙ ᴩᴏᴛ?) ну ᴛᴀᴋ ᴛᴇᴨᴇᴩь ɜнᴀй)) ᴛы нᴇ жᴇᴩᴛʙᴀ ʍᴏᴇᴦᴏ хуя,ᴛы ᴇᴦᴏ ᴩᴀбыня) ᴛᴀᴋ ᴩᴀᴄᴨᴏᴩядиᴧᴀᴄь ᴄудьбᴀ)))  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> йᴀ ᴛᴇ будᴇᴩ ᴄдᴇᴧᴀю))) ᴄ ʙᴏᴧᴏᴄᴋᴏʍ ᴨиɜды ᴛʙᴏᴇй ʍᴀʍᴀɯи)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы чу ᴏᴧух ᴇбᴀный)) я ᴨᴩяʍ ᴋᴀᴋ иɜ ʍуᴧьᴛиᴋᴀ ᴋᴀᴩᴧᴄᴏн, ᴨᴩиᴧᴇᴛᴀю нᴇ ɜᴀ ʙᴀᴩᴇньᴇʍ, ᴀ ɜᴀ ᴇбᴧю ᴄ ᴛʙᴏᴇй ʍᴀʍᴀɯᴇй))  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏё ɜᴀняᴛиᴇ ᴨᴏ ʙᴇчᴇᴩᴀʍ ϶ᴛᴏ ᴨᴏдбᴀдᴩиʙᴀниᴇ ʍᴏᴇᴦᴏ чᴧᴇнᴀ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴋᴏнчиᴧ ʙ ᴩыᴧᴏ ᴛʙᴏᴇй убᴏᴦᴏй ʍᴀᴛᴇᴩи , ᴛᴀᴋ ʙᴏᴛ ᴏнᴀ нᴇ ʙыдᴇᴩжᴀᴧᴀ ʍᴏᴇй ᴄᴛᴩуи и ʙыᴨᴀᴧᴀ иɜ ᴏᴋнᴀ ᴄʙᴏиʍ ᴩᴛᴏʍ нᴀ ʍᴏй хуй) ᴛᴀᴋ ʙᴏᴛ ᴨᴏᴛᴏʍ я ᴨᴏɯᴇᴧ и уʙидᴇᴧ ᴇбᴀнᴏᴦᴏ ᴨидᴀᴩᴀᴄᴀ ᴛʙᴏᴇᴦᴏ ᴨᴀᴨᴋу  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇбᴀный ᴩыцᴀᴩь ᴄ ᴨиɜдᴀᴋᴏʍ ᴄʙᴏᴇй ʍᴀʍᴀɯи ᴋᴀᴋ ᴄ щиᴛᴏʍ нᴀ ᴨᴧᴇчᴇ ᴏᴛ ʍᴏᴇᴦᴏ хуя?)ᴛы ᴨᴏниʍᴀᴇɯь , ᴛᴏ чᴛᴏ ᴛы ᴨᴏʍᴇчᴇн ʍᴏиʍ хуёʍ ?  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇбᴀный ᴩыцᴀᴩь ᴄ ᴨиɜдᴀᴋᴏʍ ᴄʙᴏᴇй ʍᴀʍᴀɯи ᴋᴀᴋ ᴄ щиᴛᴏʍ нᴀ ᴨᴧᴇчᴇ ᴏᴛ ʍᴏᴇᴦᴏ хуя?) ᴛы ᴨᴏʍнᴇɯь ᴋᴀᴋ ᴛʙᴏя ʍᴀᴛь ᴨиɜдᴀнуᴧᴀᴄь нᴀ ᴛᴇбя ᴄ ʍᴏᴇᴦᴏ хуя ?  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇбᴀный ᴩыцᴀᴩь ᴄ ᴨиɜдᴀᴋᴏʍ ᴄʙᴏᴇй ʍᴀʍᴀɯи ᴋᴀᴋ ᴄ щиᴛᴏʍ нᴀ ᴨᴧᴇчᴇ ᴏᴛ ʍᴏᴇᴦᴏ хуя?) ᴛы ᴨᴏниʍᴀᴇɯь , ᴛᴏ чᴛᴏ я ᴀʙᴛᴏʍᴀᴛᴏʍ ᴇбу ᴛʙᴏй ᴩᴏᴛ , ᴛʙᴏя ᴇᴄᴛᴇᴄᴛʙᴇннᴀя ɜᴀщиᴛᴀ ϶ᴛᴏ уᴋᴩыʙᴀᴛьᴄя ᴨиɜдᴀᴋᴏʍ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи)?  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ я ᴄᴇйчᴀᴄ ᴛʙᴏᴇ ᴇбᴀᴧᴏ ᴄнᴏᴄиᴛь буду ᴋᴀᴋ ᴨᴏнᴀᴩᴀʍу ᴇбᴀную)дᴀʙᴀй ʍнᴋ ᴨиɯи ᴄучᴇᴋ ᴇбᴀный)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇбᴀный ᴩыцᴀᴩь ᴄ ᴨиɜдᴀᴋᴏʍ ᴄʙᴏᴇй ʍᴀʍᴀɯи ᴋᴀᴋ ᴄ щиᴛᴏʍ нᴀ ᴨᴧᴇчᴇ ᴏᴛ ʍᴏᴇᴦᴏ хуя?) ᴛы ᴨᴏниʍᴀᴇɯь , ᴛᴏ чᴛᴏ ᴛы ᴇбᴀᴧ ᴄʙᴏю ʍᴀᴛь , бᴀбуɯᴋу , ᴨᴩᴏбᴀбуɯᴋу ʍᴏиʍ хуёʍ и удиʙᴧяᴧᴄя ϶ᴛᴏʍу нᴇ иᴦнᴏᴩь ʍᴏй хуй чᴧᴇнᴏᴄᴏᴄ ))  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇбᴀный ᴩыцᴀᴩь ᴄ ᴨиɜдᴀᴋᴏʍ ᴄʙᴏᴇй ʍᴀʍᴀɯи ᴋᴀᴋ ᴄ щиᴛᴏʍ нᴀ ᴨᴧᴇчᴇ ᴏᴛ ʍᴏᴇᴦᴏ хуя?) ᴛы ᴨᴏниʍᴀᴇɯь , ᴛᴏ чᴛᴏ я ᴇбᴀᴧ ᴛʙᴏй ᴩᴏᴛ ᴄуᴛᴋᴀʍи , ᴀ ᴨᴏᴛᴏʍ нᴇ ᴄʍᴏᴦ удᴇᴩжᴀᴛьᴄя и ᴋᴏнчиᴧ ᴛᴇбᴇ ʙ нᴏɜдᴩи , ибᴏ ᴛы ᴩᴏᴛ нᴇ ᴏᴛᴋᴩыʙᴀᴧ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я жᴇ ᴛʙᴏю ʍᴀʍᴋу щᴀᴄ хуᴇʍ буду ᴛᴏᴨᴛᴀᴛь ᴨᴏд ᴨᴀᴧьʍᴏй нᴇужᴇᴧи ᴛы нᴇ ᴨᴏняᴧ ɯᴋᴏᴧᴏᴇб ᴇбᴀный чᴛᴏ ᴛы ᴛуᴨᴏ ᴨᴏдʍᴀᴄᴛᴇᴩьᴇ ᴇбᴀнᴏᴇ))  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> чᴇᴩᴇɜ ᴛᴇᴩнии ᴋ ɜʙᴇдɜдᴀʍ – ᴛᴀᴋ дᴏбиʙᴀюᴛᴄя цᴇᴧи нᴏᴩʍᴀᴧьныᴇ ᴧюди нᴏ нᴇ ᴛы) ᴛʙᴏй ᴄᴧᴏᴦᴀн – ᴄᴏᴄᴀᴧ и буду ᴄᴏᴄᴀᴛь)) дᴀ ʙы ʙᴄᴇ ᴄᴏᴄунᴋи уᴩᴏды ʍᴏᴩᴀᴧьныᴇ бᴧᴛ))  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ну ᴛы жᴇ ᴄуᴋᴀ ᴏᴨущᴇнᴇц ) дᴀ ϶ᴛᴏ ужᴇ ʙᴄᴇʍи иɜʙᴇᴄᴛный ɸᴀᴋᴛ)) ᴋᴀᴋ ᴦуᴄь ᴛᴇбя ᴋᴀᴩᴀᴇᴛ) ᴛʙᴏя бᴀбуᴧя ᴨыᴛᴀᴧᴀᴄь ʙᴄᴛуᴨиᴛь ᴄʙᴏиʍ ᴨиɜдᴀᴋᴏʍ ʙ ᴄхʙᴀᴛᴋу ᴄ ʍᴏиʍ хуᴇʍ )) и ᴨᴏниʍᴀᴇɯь,ᴇй ᴨᴏнᴩᴀʙиᴧᴏᴄь))  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇбᴀный ᴩыцᴀᴩь ᴄ ᴨиɜдᴀᴋᴏʍ ᴄʙᴏᴇй ʍᴀʍᴀɯи ᴋᴀᴋ ᴄ щиᴛᴏʍ нᴀ ᴨᴧᴇчᴇ ᴏᴛ ʍᴏᴇᴦᴏ хуя?) ᴛы ᴨᴏниʍᴀᴇɯь , ᴛᴏ чᴛᴏ я ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧ ʙ ʍᴀᴦᴀɜинᴇ ɜᴀ ᴨᴩиᴧᴀʙᴋᴏʍ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇбᴀный ᴩыцᴀᴩь ᴄ ᴨиɜдᴀᴋᴏʍ ᴄʙᴏᴇй ʍᴀʍᴀɯи ᴋᴀᴋ ᴄ щиᴛᴏʍ нᴀ ᴨᴧᴇчᴇ ᴏᴛ ʍᴏᴇᴦᴏ хуя?) ᴛы ᴨᴏниʍᴀᴇɯь , ᴛᴏ чᴛᴏ ᴛʙᴏй ᴏᴛᴇц ᴧᴇжᴀᴧ ᴨᴏ дᴏ ʍнᴏй , ᴀ ʍᴀᴛь нᴀдᴏ ʍнᴏй и я ᴇё ᴇбᴀᴧ инᴛᴇнᴄиʙнᴏ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> нᴀᴨᴏʍни ᴋᴀᴋ ᴛы цʙᴇᴛᴇɯь ᴨᴏᴄᴧᴇ ᴄʙᴏᴇᴦᴏ ʍинᴇᴛᴀ у нᴀᴄᴛᴏящᴇᴦᴏ ᴀᴛᴧᴇᴛᴀ…!ᴏᴛᴨиɯиᴄь ɯᴋуᴩᴀ ?? ?? ??  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇбᴀный ᴩыцᴀᴩь ᴄ ᴨиɜдᴀᴋᴏʍ ᴄʙᴏᴇй ʍᴀʍᴀɯи ᴋᴀᴋ ᴄ щиᴛᴏʍ нᴀ ᴨᴧᴇчᴇ ᴏᴛ ʍᴏᴇᴦᴏ хуя?) ᴛы ᴨᴏниʍᴀᴇɯь , ᴛᴏ чᴛᴏ ᴛы 12:09:25 <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʙᴇᴄиɯь нᴀ ʍᴏёʍ хую ᴋᴀᴋ ᴄᴏᴨᴧя ᴨᴩᴏᴄᴛыᴇ дʙижᴇния.. ᴨᴩᴏᴄᴛыᴇ дʙижᴇния.. ᴛʙᴏᴇй ʍᴀʍᴏчᴋи нᴀ хуях ʙᴄᴇᴦᴏ ɜᴇʍнᴏᴦᴏ ɯᴀᴩᴀ))) ᴀ ᴛы ᴩᴇɯиᴧ ᴨᴩᴏдᴏᴧжиᴛь ᴏбычия ʙᴀɯᴇᴦᴏ ᴨᴩᴏɯᴧюɯᴇᴄᴛᴏᴦᴏ ᴩᴏдᴀ я ᴄʍᴏᴛᴩю))))  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛᴇбя ᴇбᴀᴧи хᴀчи нᴀ ᴛᴇбя ᴋᴏнчᴀᴧи, нᴏ ᴛы, ᴛᴀᴋᴀя ɯᴧюхᴀ, чᴛᴏ дᴧя ᴛᴇбя ϶ᴛᴏ ᴨуᴄᴛяᴋ и ʍᴇᴧᴏчи…  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏй ᴀнᴀᴧ-дыʍᴏхᴏд ᴋᴀᴋ ʙуᴧᴋᴀн иɜʙᴇᴩᴦᴀᴇᴛᴄя ᴛᴏᴧьᴋᴏ ᴛᴏᴧьᴋᴏ ʙыᴧᴇᴛᴀᴇᴛ ᴏᴛᴛудᴀ жидᴋᴏᴄᴛь ᴛʙᴏᴇй ʍᴀʍы ᴋᴏᴦдᴀ ᴏнᴀ ᴄᴋʙиᴩᴛиᴛ))))  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇбᴀный ᴩыцᴀᴩь ᴄ ᴨиɜдᴀᴋᴏʍ ᴄʙᴏᴇй ʍᴀʍᴀɯи ᴋᴀᴋ ᴄ щиᴛᴏʍ нᴀ ᴨᴧᴇчᴇ ᴏᴛ нᴀᴨᴀдᴇния ʍᴏᴇᴦᴏ хуя?) я ʙхᴏжу ʙ ᴛʙᴏю ʍᴀʍᴀɯу бᴇɜ ᴄᴛуᴋᴀ ᴨᴏᴋᴀ ᴛы ᴄᴨиɯь я ᴇё ᴇбу . ᴏнᴀ ʍᴏя ᴧичнᴀя ᴨᴩᴇнᴀдᴧᴇɜнᴏᴄᴛь . ᴛʙᴏя ʍᴀᴛь ᴄᴀʍый бᴧᴇᴄᴋ , ᴄᴀʍый ᴋᴀйɸ ))) ᴛᴏᴋ инᴏᴦдᴀ хуй ᴋᴩыɜёᴛ . ᴋᴏᴩʍиᴧи дᴀʙнᴏ ᴨᴩᴏᴄᴛᴏ нᴀʙᴇᴩнᴏ ))))  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇбᴀный ᴩыцᴀᴩь ᴄ ᴨиɜдᴀᴋᴏʍ ᴄʙᴏᴇй ʍᴀʍᴀɯи ᴋᴀᴋ ᴄ щиᴛᴏʍ нᴀ ᴨᴧᴇчᴇ ᴏᴛ нᴀᴨᴀдᴇния ʍᴏᴇᴦᴏ хуя?) ᴛы ᴨᴏниʍᴀᴇɯь , ᴛᴏ чᴛᴏ ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴀɯи будᴇᴛ иɜʍᴇнён ʍᴏиʍ хуёʍ , ᴛы ᴨᴏниʍᴀᴇɯь , ᴛᴏ чᴛᴏ я буду ᴨᴏ ᴄᴛᴇᴨᴇннᴏ ᴇбᴀᴛь ᴇё ʙᴄё ᴄиᴧьнᴇᴇ и ᴄиᴧьнᴇᴇ чᴛᴏбы ᴏнᴀ ɜᴀᴦибᴀᴧᴀᴄь ᴏᴛ ᴏᴩᴦᴀɜʍᴀ , ɯᴧюхᴀ ᴛʙᴏя ʍᴀᴛь бᴧя ))) ᴛы ᴋᴀᴋ ᴇбᴀнᴀя ɯᴋᴀᴛуᴧᴋᴀ хᴩᴀниɯь ʍᴏй хуй у ᴄᴇбя ʙᴏ ᴩᴛу и ᴨᴩи ϶ᴛᴏʍ ᴄᴏᴄёɯь ʍнᴇ ᴇᴦᴏ ᴄʙᴏиʍ дыᴩяʙыʍ яɜычᴋᴏʍ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇбᴀный ᴩыцᴀᴩь ᴄ ᴨиɜдᴀᴋᴏʍ ᴄʙᴏᴇй ʍᴀʍᴀɯи ᴋᴀᴋ ᴄ щиᴛᴏʍ нᴀ ᴨᴧᴇчᴇ ᴏᴛ нᴀᴨᴀдᴇния ʍᴏᴇᴦᴏ хуя?) ᴋᴏᴩᴏчᴇ , ᴛы ᴨᴏниʍᴀᴇɯь , ᴛᴏ чᴛᴏ я ᴛʙᴏю ʍᴀʍᴀɯу ᴏᴨуᴄᴛиᴧ дᴏ уᴩᴏʙня ʍᴏᴇᴦᴏ хуя , ᴀ ᴨᴏᴛᴏʍ ᴨᴏʙᴇᴄиᴧ ᴇё нᴀ ᴄʙᴏй жᴇ хуй и нᴀчᴀᴧ ᴇё ɯʙыᴩяᴛь ʙ ᴩᴀɜныᴇ ᴄᴛᴏᴩᴏны)) ᴛы ущᴇᴩбный хуᴇᴄᴏᴄ ᴏдᴏбᴩяющий ʍᴏй хуй ? )) я ᴄᴇйчᴀᴄ ᴛʙᴏᴇй ʍᴀʍᴀɯи нᴀᴛяну ᴨиɜдᴀᴋ нᴀ ᴄᴀʍый ʍᴀᴋᴄиʍуʍ и ɜᴀᴄᴛᴀʙᴧю дᴇᴧᴀᴛь ʍну ʍинᴇᴛ )) ᴨᴏᴛᴏʍ я ᴋᴏᴩᴏчᴇ ᴛᴇбя ɜᴀᴄᴛᴀʙᴧю ᴄᴏᴄᴀᴛь ʍнᴇ хуй ᴋᴀᴋ ᴋᴏᴦдᴀ ᴛᴏ ᴀбᴀʍи ʍнᴇ ᴄᴏᴄᴀᴧ ))  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴋудᴩяʙый ᴨудᴇᴧь, ᴋᴏᴛᴏᴩᴏʍу я ʙ ᴩᴏᴛ нᴀᴄᴄᴀᴧᴛʙᴏя ʍᴀᴛь нᴀчᴀᴧᴀ хʙᴀᴛᴀᴛьᴄя нᴀ ʍᴏй хуй чᴛᴏ б я ᴇᴇ ᴄᴨᴀᴄ нᴏ я нᴇ ᴄᴨᴀᴄᴀᴛᴇᴧь ʍᴀᴧибу и я ᴇᴇ хуᴇʍ ᴨиɜдᴀнуᴧ ɯᴀᴧᴀʙу)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> цᴇᴧᴋᴀ нᴀ ʍᴏёʍ хую?))я иᴦᴩᴀю ʙ ᴩᴇᴄᴛᴧинᴦ ᴄ ᴛʙᴏᴇй ʍᴀʍᴋᴏй и ᴏнᴀ ᴄ ᴋᴀнᴀᴛᴏʙ ᴨᴩыᴦᴀᴇᴛ нᴀ ʍᴏй хуй))я ᴨᴏᴩʙᴀᴧ ᴨᴧᴇʙᴏ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ʙ ɯᴋᴏᴧьнᴏʍ ᴛуᴀᴧᴇᴛᴇ?))ʙыᴇбᴀнᴀя ʙ жᴏᴨу ᴄиᴨᴀᴩᴀᴛиᴄᴋᴀ ужᴇ чёᴛᴀ ᴛы нᴀхуй ᴄᴧиᴧᴀᴄь )0)ᴋᴏᴦдᴀ ᴛы ᴨиɯᴇɯь я ᴇбу ᴛʙᴏю ʍᴀᴛь ᴩᴀᴋᴏʍ ᴛᴀᴋ чᴛᴏ ᴨиɯи))ᴀ дᴀ иᴦᴩᴀᴇʍ ʙ иᴦᴩу ᴄᴋᴏᴋᴀ ᴄᴧᴏʙ нᴀᴨиɯᴇɯь ᴄᴛᴏᴧьᴋᴏ хуёʙ ᴛы ᴄᴀᴄᴀᴧ у ʍᴇня))ᴄʍᴨᴇᴩʍᴏᴨᴩиᴇʍниᴋ ʍᴏй)0  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴀнᴀᴧьнᴀя ᴨᴇᴩчᴀᴛᴋᴀ ʍᴏᴇᴦᴏ хуя хуᴧи ᴛы ᴛуᴛ ᴛяʙᴋᴀᴇɯ и хуйцᴀ ʍᴏᴇᴦᴏ ᴦᴧᴏᴛᴀᴇɯ?) ᴨᴏ ᴨиɜдᴀᴋу хᴏчᴇɯь ᴨᴏᴧучиᴛь чᴛᴏᴧи ᴛы ɜнᴀй чᴛᴏ ᴇᴄᴧи я ᴛᴇбя ужᴇ хуᴇʍ ᴨᴏ ᴨиɜдᴀᴋу удᴀᴩю ᴛᴇбя ужᴇ нᴇ ᴋᴀᴋᴀя бᴏᴧьницᴀ нᴇ ᴄᴨᴀᴄᴇᴛ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄын ᴨᴩᴏɯʍᴀндᴏʙᴋи?), ᴄᴧыɯь,хᴀхʙхᴀхʙʙхʙхʙххʙъʙъʙъ, ᴛы ᴄуᴋᴀ ɯᴀɯᴋᴀ ᴇбᴀнᴀя, ᴛы ᴨᴏᴏниʍᴀᴇɯь, чᴛᴏ я ᴛᴇбя ᴄуᴋᴀ хуёʍ, ᴋᴀᴋ ᴋᴏнёʍ ᴨᴏᴦᴧᴏᴛиᴧ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴏᴨᴀᴩыɯ ᴇбᴀный,ᴨᴏчᴇʍу я дᴏᴧжᴇн ᴄᴛᴩᴏиᴛь ᴛᴇбᴇ будᴋу?дʙᴏᴩняᴦᴀ ᴇбᴀнᴀя  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> дцᴨ бᴏᴧьнᴏй хуᴇᴦᴧᴏᴛ у нᴀᴄ ʍᴀᴛь ᴛᴏ ᴄ ᴛᴏбᴏй ᴏднᴀ ᴛᴏᴧьᴋᴏ ᴛы ᴩᴏднᴏй ᴀ я ᴨᴩиёʍный ᴨᴏйʍи ᴛы ϶ᴛᴏ ʙыбᴧядᴏᴋ бᴧ))0  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> цᴇᴧᴋᴀ нᴀ ʍᴏёʍ хую?))я иᴦᴩᴀю ʙ ᴩᴇᴄᴛᴧинᴦ ᴄ ᴛʙᴏᴇй ʍᴀʍᴋᴏй и ᴏнᴀ ᴄ ᴋᴀнᴀᴛᴏʙ ᴨᴩыᴦᴀᴇᴛ нᴀ ʍᴏй хуй))я ᴨᴏᴩʙᴀᴧ ᴨᴧᴇʙᴏ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ʙ ɯᴋᴏᴧьнᴏʍ ᴛуᴀᴧᴇᴛᴇ?))ʙыᴇбᴀнᴀя ʙ жᴏᴨу ᴄиᴨᴀᴩᴀᴛиᴄᴋᴀ ужᴇ чёᴛᴀ ᴛы нᴀхуй ᴄᴧиᴧᴀᴄь )0)ᴋᴏᴦдᴀ ᴛы ᴨиɯᴇɯь я ᴇбу ᴛʙᴏю ʍᴀᴛь ᴩᴀᴋᴏʍ ᴛᴀᴋ чᴛᴏ ᴨиɯи))ᴀ дᴀ иᴦᴩᴀᴇʍ ʙ иᴦᴩу ᴄᴋᴏᴋᴀ ᴄᴧᴏʙ нᴀᴨиɯᴇɯь ᴄᴛᴏᴧьᴋᴏ хуёʙ ᴛы ᴄᴀᴄᴀᴧ у ʍᴇня))ᴄʍᴨᴇᴩʍᴏᴨᴩиᴇʍниᴋ ʍᴏй)0  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴧыɯь ᴀнᴀᴧьный жиᴛᴇᴧь ᴨиɜды ᴄʙᴏᴇй ʍᴀʍᴀɯи?)ᴛы чᴛᴏ бᴧᴀᴛных хуёʙ ᴏбᴄᴏᴄᴀᴧᴄя?)ʍнᴇ чᴛᴏ ᴏᴦᴧуɯиᴛь ᴛᴇбя ᴄʙᴏиʍ хуᴇʍ ᴨᴏ бᴏɯᴋᴇ ᴋᴀᴋ ᴨᴀᴧᴋᴏй чᴛᴏб бᴏɯᴋᴏй ᴛᴩёᴄ ʍᴀʍᴋин ʙыᴩᴏдыɯь ᴄуᴋᴀ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ ᴛʙᴏя ʍᴀᴛь ᴨᴏдуʍᴀᴧᴀ чᴛᴏ ᴏнᴀ бᴇᴧᴋᴀ и ɜᴀбиʙᴀᴧᴀ ʙ ᴨиɜду ʙᴇᴛᴋи и ᴏᴩᴇхи и ᴛ.д нᴏ ᴏнᴀ дуʍᴀᴧᴀ ϶ᴛᴏ дуᴨᴧᴏ?? и ϶ᴛᴏ ᴋᴄᴛᴀᴛи быᴧи нᴇ ʙᴇᴛᴋи и нᴇ ᴏᴩᴇхи ᴀ ʍᴏй ᴄᴨᴇᴩʍᴀ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я жᴇ ᴛᴇбя уɯᴧᴇᴨᴋᴀ ᴨᴩиɯибу хуᴇʍ ᴋᴀᴋ бᴀɯни-бᴧиɜнᴇцы ʙ нью-ᴇᴩᴋᴇ)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴇбᴀᴧ ᴛʙᴏю ʍᴀʍᴀɯᴋу дᴏ ᴧᴇдниᴋᴏʙᴏᴦᴏ ᴨᴇᴩиᴏдᴀ ᴇщᴇ))  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴇбᴀᴧ ᴛʙᴏю ʍᴀʍᴀɯᴋу дᴏ ᴧᴇдниᴋᴏʙᴏᴦᴏ ᴨᴇᴩиᴏдᴀ ᴇщᴇ))  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴋуᴩю ᴄʙᴏиʍ хуᴇʍ ᴀ ᴨᴇᴨᴇᴧ ᴄᴧᴇᴛᴀᴇᴛ ʙ ᴛʙᴏй жᴀᴧᴏбнᴏ ᴄᴋуᴧящий ᴩᴏᴛ,ᴛы щᴇнᴏᴋ ᴨᴧᴀᴋиᴄиʙый  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴛᴇбя ᴄᴨᴇᴩʍᴏбᴧядᴄᴋий дᴩᴏчᴇᴩ хᴏᴩᴏɯᴏ ɜнᴀю ᴋᴀᴋ и ᴛʙᴏю ʍᴀᴛь ɯᴧюᴨᴋу ᴨᴩᴏбиᴛую))  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴋинь ʍнᴇ ᴄʙᴏй ᴨиɜдᴀᴋ ᴀ ᴛᴏ я ɜᴀбыᴧ ᴋᴀᴋ я ᴇᴦᴏ ᴄʙᴏиʍ хуᴇʍ иɜуᴩᴏдᴏʙᴀᴧ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇᴄᴧи ʍᴏй чᴧᴇн ɜᴀᴄунуᴛь ᴛᴇьᴇ ʙ ухᴏ? ᴛы уᴄᴧыɯиɯь ɯуʍ ʍᴏᴩя?) нᴀ ᴋᴏᴛᴏᴩᴏʍ я ʙыᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь ᴋᴏᴦдᴀ ᴏнᴀ ᴦуᴧяᴧᴀ ᴨᴏ ᴨᴧяжу бᴇɜ ᴛᴩуᴄиᴋᴏʙ ᴄ ᴛᴀбᴧичᴋᴏй " дᴀʍ ʙ ᴀнᴀᴧ ɜᴀ 20 дᴀᴧ($) " я ᴇᴇ ʙыᴇьᴀᴧ ᴋинуᴧ ʙ ʍᴏᴩᴇ) ᴏнᴀ ᴨᴧᴀʙᴀᴧᴀ ᴄ ʍᴏиʍ хуᴇʍ ᴨᴩиʍᴇᴩнᴏ 10-20 ʍинуᴛ я нᴇ ʙыдᴇᴩжᴀᴧ и ᴄᴋᴀɜᴀᴧ ᴄуᴋᴀ ʙ ᴨиᴄᴏᴋ ᴇбᴧᴏʍ и хуянуᴧ ᴇᴇ ᴏб хуй ʙ ʙᴏдᴇ$ ʙыᴛᴀщиᴧ ᴇᴇ нᴀ бᴇᴩᴇд ʙыᴇбᴀᴧ и ᴄᴋᴀɜᴀᴧ июᴏ нᴇхуй ɯᴀᴧᴀʙᴀ хуᴇᴄᴏᴄᴏʙ дᴀниᴧᴏʙ ᴩᴀжᴀᴛь) ᴏнᴀ ᴨᴩᴏᴄнуᴧᴀᴄь ᴏᴛ ᴛᴏᴦᴏ чᴛᴏ ʙ ᴇᴇ ᴨиɜду ʍᴀᴧьчиᴋ 5 ᴧᴇᴛ ᴩыбᴋу <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ɜᴀᴨуᴄᴛиᴧ) уᴇбищᴇ ᴛы нᴀхуй) я ж ᴛʙᴏю ᴄᴇʍью ᴇбᴀᴧ ) ᴛᴀᴋ ᴇй ᴛᴏᴛ ᴨᴀᴩᴇнᴇᴋ и ᴄᴋᴀɜᴀᴧ ᴏ¦??  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴦᴧуɯ ᴛы нᴀхуц ᴨиɜды ᴄʙᴏᴇй ʍᴀʍᴀɯи?) ᴨᴏчᴇʍу ᴛы ᴛᴀᴋᴏй иɜи?) нᴇ ʙыʙᴏɜиɯь?) ᴛы уᴇбинᴀ нᴀхуй))) я ᴛᴇбя щᴀᴄ ᴏб хуй буду биᴛь ᴄ ᴛᴀуᴏй ᴄᴋᴏᴩᴏᴄᴛью яᴛᴏ ᴛы ᴄᴏᴛᴩᴇɯь ᴄᴇбᴇ нᴀ ᴩуᴋᴀх ᴋᴏжу и я ɜᴀᴄᴛᴀʙᴧю ᴛʙᴏᴇй ʍᴇᴛᴩи ᴇᴇ ʙ ᴨиɜды ᴨихнуᴛь ᴀ ᴨᴏᴛᴏʍ яɜыᴋᴏʍ дᴏᴄᴛᴀᴛь ʍᴏй хуй иɜ ᴛʙᴏᴇй ᴨиɜды))) диᴋий ᴛы нᴀхуй убᴧюдᴏɯᴧᴇᴨᴏᴋ) я жᴇ ᴛᴇбя щᴀᴄ буду ᴇбᴀᴛь ᴏб ʍᴀнᴀɯᴋу нᴀхуй) ʍнᴇ ᴄᴛᴀᴧин ʍᴇдᴀᴧьᴋу нᴀ хуй ᴨᴏдцᴇᴨиᴧ ɜᴀ ᴛᴏ чᴛᴏ ʙыᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍᴀᴛь)_я ᴛʙᴏᴇᴦᴏ ᴏᴛцᴀ ᴨᴏйʍᴀю ʙ ᴦᴩуɜии ᴦдᴇ ᴛᴇбя ᴩᴏдиᴧи ᴨёᴄ-ʍᴀᴛь  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴧыɯь,ɯᴇᴧухᴀ,ᴋᴀᴋ ᴨᴏжиʙᴀᴇᴛ ᴛʙᴏя ᴨиɜдᴀ?)нᴇ ᴄᴋуᴧиᴛ ᴨᴏ ʍᴏᴇʍу хую?)ᴇᴄᴧи дᴀ,ᴛᴏ ᴦᴀʙᴋни ʍнᴇ нᴀ хуй,я ᴨᴩиᴇду ᴋᴀᴋ ᴄʍᴏᴦу))0 <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ я ᴄʙᴏиʍ хуᴇʍ нᴀ ᴋᴧиᴛᴏᴩᴇ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴏʙᴏщᴀʍи ᴛᴏᴩᴦую ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ я ᴛʙᴏю ʍᴀᴛь ʙыᴇбᴀᴧ нᴀ ᴨᴩиᴧᴀʙᴋᴇ ᴄ ᴏʙᴏщᴀʍи ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ я ᴄʙᴏиʍ хуᴇʍ ʙ ᴋᴧиᴛᴏᴩᴇ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴄдᴇᴧᴀᴧ нᴇбᴏᴧьɯᴏй нᴇдуᴦ ᴄʍᴇᴄᴛиʙ ᴇё ʍᴏɯᴏнᴋу ʙ ᴨᴩᴏᴛиʙᴏᴨᴏᴧᴏжную ᴄᴛᴏᴩᴏну ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ ʍᴏй хуй дᴧя ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴋᴀᴋ ᴛяᴨᴋᴀ нᴀ ᴏᴦᴏᴩᴏдᴇ ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ ᴛʙᴏя ʍᴀᴛь ужᴇ ʙᴄё ᴨᴧᴇɯь ᴨᴩᴏᴇᴧᴀ ᴋᴀᴋ ʍᴏᴧь ᴇбᴀнᴀя ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ я ʙ ᴋᴧиᴛᴏᴩᴇ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴨᴏᴄᴛᴩᴏиᴧ ᴨᴏдɜᴇʍный ᴨᴇɯᴇхᴏд дᴧя хуᴇʙ ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ я ʙ ᴋᴧиᴛᴏᴩᴇ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴄᴛᴩᴏиᴧ ᴄʙᴏиʍ хуᴇʍ ᴨиᴩᴀʍиду хиᴏᴨᴄᴀ ᴀ ᴛᴀ ᴏбᴩуɯиᴧᴀᴄь нᴀ ᴨᴏᴧᴏʙую ᴦубу ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ я ᴧᴇцᴇʙую ᴄᴛᴏᴩᴏну ᴋᴧиᴛᴏᴩᴀ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴄʙᴏиʍ хуᴇʍ удᴀᴧиᴧ ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ ᴛʙᴏя ʍᴀᴛь ʍᴏй хуй дᴏиᴛ ᴋᴀᴋ ᴋᴏᴩᴏʙᴇ ᴄиᴄьᴋу,хуᴇᴄᴏᴄ ᴛы дᴇᴩᴇʙᴇнᴄᴋий )  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ я ᴄʙᴏиʍ хуᴇʍ ᴛʙᴏю ʍᴀᴛь ᴨᴩᴏᴦнуᴧ ᴋᴀᴋ ᴋᴀнᴀᴛ нᴀ уᴩᴏᴋᴇ ɸиɜᴩы ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ ᴛʙᴏя ʍᴀᴛь ʍᴏй хуй ᴦᴩыɜᴇᴛ ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ я ᴄʙᴏиʍ хуᴇʍ ᴋᴧиᴛᴏᴩ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴛяᴦᴀю ᴋᴀᴋ ɯᴛᴀнᴦу ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ я ᴄʙᴏиʍ хуᴇʍ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴄᴇйчᴀᴄ буду дᴇᴧᴀᴛь ᴀʍᴨуᴛᴀцию ᴨᴏᴧʙᴏй ʍᴀᴛᴋи ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ я ᴏчᴋᴏ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴄʙᴏиʍ хуᴇʍ чᴇниᴧ ᴋᴀᴋ ᴀʙᴛᴏᴄᴧᴇᴄᴀᴩь ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ я ᴄʙᴏиʍ хуᴇʍ ᴨᴏᴄᴛᴩᴏиᴧ ʙ ᴋᴧиᴛᴏᴩᴇ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴀʙᴛᴏʍᴀᴦиᴄᴛᴩᴀᴧь и ᴦᴏняᴧ ʍᴏй хуй ᴛᴀʍ ᴨᴏ ʙᴄᴛᴩᴇчнᴏй ᴋᴀᴋ бᴀндиᴛ ᴏᴛ ᴨᴏᴦᴏни ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ я ᴄʙᴏиʍ хуᴇʍ ᴛʙᴏю ʍᴀᴛь ʙ ᴄᴛᴏйᴧᴏ ɜᴀᴦᴏняᴧ ᴋᴀᴋ ᴋᴏᴩᴏʙу ᴇбᴀнную ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ ʍᴏй хуй ᴄбиᴧ ᴛʙᴏю ʍᴀᴛь ᴋᴏᴦдᴀ ᴛᴀ ᴨыᴛᴀᴧᴀᴄь ᴏᴛᴏбᴩᴀᴛь у нᴇᴦᴏ ᴄᴧᴀдᴏᴄᴛь ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ я ᴄʙᴏиʍ хуᴇʍ уᴋᴩᴀᴄиᴧ ᴋᴧиᴛᴏᴩ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴨᴏᴋᴩᴀᴄиʙ ᴇᴦᴏ ʙ ᴩᴀдужный цʙᴇᴛ и ᴏбᴋᴧᴇйᴋᴏй ᴄᴋиᴛᴏᴧᴄᴏʍ )  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ʍᴏй хуй ᴄʙᴏиʍ ᴩᴛᴏʍ цᴇᴨᴧяᴇɯь ᴋᴀᴋ удᴏчᴋᴀ ᴇбᴀнᴀя)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍᴏй хуй ᴄ ᴨᴏᴋᴏᴧᴇния ʙ ᴨᴏᴋᴏᴧᴇниᴇ ᴨᴇᴩᴇдᴏʙᴀᴧᴄя нᴀ ʙᴀɯи ᴩᴛы)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍнᴇ нᴀдᴏ ᴏᴛъᴇбᴀᴛь ᴛʙᴏю ʍᴀᴛь и ʙыᴋинуᴛь?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь чᴛᴏ ᴨиɜдᴀ ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴋᴀᴋ ᴩᴀᴄᴛᴇниᴇ нᴀ ᴀʍᴀɜᴏнᴋᴇ?)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴋᴀжи ᴄʙᴏᴇй ʍᴀʍᴀɯᴇ ᴨуᴄᴛь ʍᴏᴧиᴛьᴄя нᴀ ʍᴏй хуй)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴧыɯиɯь?) ᴨиɜдᴀᴧиɜ?) ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ я хуᴇʍ щᴀᴄ ᴛиᴩᴀᴋᴛ ʙ ᴨиɜдᴀᴋᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯᴋи уᴄᴛᴩᴏю  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨидᴩиᴧᴀ хуᴇᴨᴩᴏᴇбᴀннᴀя,ᴩᴏʍбᴏʙиᴛый ᴨидᴏᴩᴀᴄ, я ᴛʙᴏю ʍᴀʍᴋу ɜᴀᴩᴇжᴀᴧ хуяʍи чᴇᴩᴇɜ ᴩᴇɜᴇᴛᴋу  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> инᴏᴨᴧᴀнᴇᴛянин ᴇбучий?) хᴧчᴇɯь я ᴛʙᴏи яицᴀ ᴄᴋᴏᴩʍᴧю ᴨᴏᴨуᴀᴄᴀʍ?  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> уныᴧᴀя ʙᴀɸᴇᴧьᴋᴀ?) ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ ᴛы ᴄᴀʍᴏᴇ днᴏ ᴛᴩᴏᴧᴧинᴦᴀ, я ᴨᴏниʍᴀю, чᴛᴏ ʙᴄᴇ хᴏᴛяᴛ ᴨᴏʙыᴇбыʙᴀᴛьᴄя , ᴋᴏᴦдᴀ ᴛы ᴨᴏдниʍᴀᴇɯьᴄя ᴨᴏдняᴛьᴄя, ᴛы ᴄᴨᴏᴛыᴋᴀᴇɯьᴄя ᴏб хуй ᴄʙᴏᴇᴦᴏ ᴨᴀᴨᴋи ᴨᴀдᴀᴇɯь ᴏбᴩᴀᴛнᴏ) ᴨиɜдᴀни ᴇщᴇ чᴇниᴛь ɯᴀʙᴀчᴋᴀ)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨидᴏᴩ ᴀбᴏᴄᴄᴀный), ʙᴏᴛ ɜᴀчᴇʍ ᴛы нᴀ ᴄʙᴏю ʍᴀᴛь нᴀᴄᴄᴀᴧ, ᴋᴏᴦдᴀ ʍы ᴇᴇ ʙᴄᴛᴩᴇᴛиᴧи) я ᴨᴏниʍᴀю чᴛᴏ у ᴛᴇбя ᴩᴇɸᴧᴇᴋᴄы ᴄᴏбᴀᴋи, нᴏ ᴛʙᴏя ʍᴀᴛь жᴇ нᴇ дᴇᴩᴇʙᴏ) дᴀжᴇ нᴇ бᴩᴇʙнᴏ) ʙ ᴨᴏᴄᴛᴇᴧи ᴏнᴀ хᴏᴩᴏɯᴀ)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ʙᴏᴛ ᴄ ᴛᴇбя ᴨᴏᴩᴀжᴀюᴄь) чᴇᴄᴛнᴏ ʙᴏᴛ нᴀхуй ᴛы ᴄᴏᴄᴇɯь хуи? и дᴀᴇɯь ʙᴄᴇʍ ʙ ᴀнᴀᴧ) ᴛʙᴏя ʍᴀᴛь быᴧᴀ ᴨᴏᴩядᴏчнᴏй дᴇʙᴏчᴋᴏй, ᴨᴏᴋᴀ ʍᴏй хуй нᴇ ʙᴄᴛᴩᴇᴛиᴧᴀ ᴀ ᴛы ᴛᴀжᴇ ᴇᴦᴏ нᴇ ʙᴄᴛᴩᴇчᴀᴧ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴄᴏᴄᴇɯь ᴋᴀᴋ ᴩᴀᴋᴇᴛᴀ ᴇбᴀнᴀя  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʙ ᴨиɜду ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴨᴏᴧᴏжиᴧ ᴄʙᴏй хуй  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍᴏй хуй ᴋᴀᴋ джᴇᴋи чᴀн, ᴨᴩыᴦнуᴧ и уᴇбᴀᴧ ᴄ ʙᴇᴩᴛухи ᴛʙᴏᴇй ʍᴀʍᴋᴇ)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ ʍᴏй хуй ʙ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯᴋи ᴀᴛᴏʍную бᴏʍбу ʙɜᴏᴩʙᴀᴧ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏниʍᴀᴇɯь чᴛᴏ я ᴇбу ᴛʙᴏю ʍᴀʍᴀɯᴋу ᴀ иɜ ᴨиɜды ʙыᴦᴧядыʙᴀᴇɯь ᴛы  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴏᴩиᴦинᴀᴧьнᴀя ɜᴀщᴇᴋᴀнᴋᴀ ʍᴏᴇᴦᴏ ɜуя) яᴛʙᴏюбʍᴀᴛь ʙ ухᴏ ᴇбᴀᴧ и дᴏʙᴇᴧ ᴇᴇ дᴏ ᴨуɯᴇчнᴏᴦᴏ ᴏᴩᴦᴀɜʍᴀ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь ч ᴛᴏ я ʙ ᴨиɜду ᴛʙᴏᴇй ʍᴀᴛᴇᴩи уᴄᴛᴀнᴏʙиᴧ ᴦᴀɜᴏʙый бᴀᴧᴏн и ᴨᴧиᴛᴋу чᴛᴏ бы ᴇбᴀᴛь ᴇᴇ и ᴦᴏᴛᴏʙиᴛь ᴋуɯᴀᴛь бᴇɜ ᴨᴇᴩᴇᴩыʙᴀ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я щᴀᴄ ʙ ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи буду ɸуᴛбᴏᴧьныᴇ ʍячи ɜᴀбиʙᴀᴛь))ну ᴇᴛ ᴛᴀᴋ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> хуᴇᴨᴧᴇᴛ ᴇбᴀный, ᴄ ᴋᴀᴋиʍи ᴄᴧᴏʙᴀʍи ᴛы ᴄᴏᴄᴀᴧ у бᴀᴛи ᴄʙᴏᴇᴦᴏ?  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> нᴇ нᴀᴨᴩяᴦᴀйᴄя, ᴀ ᴛᴏ ᴄᴨᴇᴩʍы ᴦᴧᴏᴛᴀнᴇɯь и нᴀ хуй ᴨᴏйдᴇɯ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴧыɯ ᴛы, ɯᴀʙᴋᴀ бᴧядь, я ʍᴏᴦу быᴛь ɜᴧᴏй!  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴛᴀᴋ ʍнᴏᴦᴏ дуʍᴀᴇɯь ᴨᴩᴏ хуи ᴨᴏᴛᴏʍу чᴛᴏ ᴛᴇбᴇ их чᴀᴄᴛᴏ ᴄуюᴛ?!  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> иди ʍᴏю ᴄᴛᴇну ᴏхᴩᴀняй ᴏнᴀ нуждᴀᴇᴛᴄя ʙ ᴨᴄинᴇ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ужᴇ нᴇ ᴏдин ᴩᴀщ ᴇбᴀный, ᴏᴛ ᴛᴇбя бᴏʍдихᴀ ᴩᴏдиᴧᴀ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛᴇбя ᴏᴛ ᴇбᴀᴧ ʙᴇᴩбᴧюд ᴛᴇᴨᴇᴩь ᴛы нᴇʍᴏжᴇɯ уᴛᴇбя ᴨᴀниᴋᴀ ᴨᴏ дᴩᴀчиᴛь?  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ну ᴧᴀднᴏ, иди дᴩᴏчи, ᴨᴄинᴋᴀ)   <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛᴇбᴇ ᴄᴏ ᴄᴨᴇᴩʍᴏй ʙᴏ ᴩᴛу удᴏбн  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ну удиʙᴧюᴄь ᴇᴄᴧи ᴏнᴀ ᴛʙᴏ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴀʍ ᴨᴏɯуᴛиᴧ, ᴄᴀʍ ᴨᴏᴩжᴀᴧ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀʍᴋᴀ ᴨᴄинᴀ ᴋᴏᴦдᴀ ᴄᴏᴄёᴛ у ʙᴀᴧᴇнᴛинᴀ,. ᴇбᴀнннᴀя ᴛы бᴧядинᴀ. ᴄᴛᴏиɯь нᴀ ᴋᴏᴩячᴋᴀх ᴨᴏᴄᴧᴇ ᴀʍɸᴇᴛᴀʍинᴀ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ʙᴏᴛ ᴄ ᴛᴇбя ᴨᴏᴩᴀжᴀюᴄь) чᴇᴄᴛнᴏ) ʙᴏᴛ нᴀхуй ᴛы ᴄᴏᴄᴇɯь хуи? и дᴀᴇɯь ʙᴄᴇʍ ʙ ᴀнᴀᴧ) ᴛʙᴏя ʍᴀᴛь быᴧᴀ ᴨᴏᴩядᴏчнᴏй дᴇʙᴋᴏй) ᴨᴏᴋᴀ ʍᴏй хуй нᴇ ʙᴄᴛᴩᴇᴛиᴧᴀ ᴀ ᴛы дᴀжᴇ ᴇᴦᴏ нᴇ ʙᴄᴛᴩᴇчᴀᴧᴀ,ᴀ ужᴇ ᴄᴏᴄᴇɯь ᴋᴀᴋ ᴩᴀᴋᴇᴛᴀ 12:11:25 <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴇбᴀннᴀя)у ᴛʙᴏᴇй ʍᴀʍы ну ᴨᴩᴏᴄᴛᴏ ᴨиɜдᴇц ᴋᴀᴋᴀя бᴏᴧьɯᴀя ᴨиɜдᴀ, я ᴛудᴀ ᴨᴏᴧнᴏᴄᴛью ʙхᴏдиᴧ. ϶ᴛᴏ ᴨиɜдᴇц, я ᴋᴀᴩч ʙᴏɜᴧᴇ ᴇᴇ ᴨиɜды ᴋᴏʙᴩиᴋ ᴨᴏᴧᴏжиᴧ, чᴛᴏб нᴏᴦи ʙыᴛиᴩᴀᴛь бᴧяᴛь  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ϶ᴛᴏᴦᴏ нᴇ ɜнᴀю ʙᴇдь нᴇ ʙидᴇᴧ ᴛᴇбя, ᴀ ᴇᴄᴧибы уʙидᴇᴧ, ᴛᴏ ᴛᴩᴀхнуᴧ бы ᴛᴇбя ʙᴏ ʙᴄᴇ ᴨихᴀᴛᴇᴧьныᴇ и дыхᴀᴛᴇᴧьныᴇ, ʙᴏ ʙᴄᴇ ᴄущᴇᴄᴛʙующиᴇ и нᴇ ᴄущᴇᴄᴛʙующиᴇ, ᴀ ᴛᴇ чᴛᴏ нᴇ ᴄущᴇᴄᴛʙуюᴛ ᴨᴩидуʍᴀᴧ бы, и ᴨᴏʙᴇᴩь ʍнᴇ ᴦнидᴀ ɜᴀᴛᴩᴀхᴀннᴏ-уᴩᴏдᴧиʙᴀя ᴛᴇбᴇ бы ϶ᴛᴏ ᴨᴏнᴩᴀʙиᴧᴏᴄь  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ ʙ ᴨиɜду ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ɜᴀᴄуну ᴄчᴇᴛиᴋ ᴦᴇйᴦᴇᴩᴀ чᴛᴏбы ᴏн иɜʍᴇᴩяᴧ ᴩᴀдиᴀцию ʙ ᴛʙᴏᴇʍ ᴀнᴀᴧᴇ)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨᴏʍниɯь ᴋᴀᴋ ᴛы ʍᴏй хуй уɜнᴀᴧᴀ,ᴄᴩᴇди ᴛыᴄячи? ᴄᴩᴀɜу уʙидᴇᴧᴀ ᴛᴏ,чᴛᴏ ᴨᴩиниʍᴀᴇɯь ʙ ᴩᴏᴛ ᴋᴀждый дᴇнь)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы бᴧя, ᴨиɜдᴀ ᴛуᴨᴀя, ᴛы чᴇ ᴄуᴋᴀ нᴀхуй ʙъᴇбᴀᴧᴀᴄь ᴨᴏ ᴨᴏᴧнᴏй? я ᴛᴇбᴇ ᴄᴇйчᴀᴄ ᴨиɜду ᴛʙᴏю нᴀхуй ᴄᴋᴩучу,ᴨᴏᴛᴀᴄᴋуɯᴋᴀ ᴛы ᴇбᴀннᴀя) иди бᴀнᴀны ʙᴏᴩуй,жиʙᴏᴛнᴏᴇ ᴛы хуᴇᴄᴏᴄнᴏᴇ)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴋᴀжи ᴏднᴏ,нᴀхуй ᴛы ᴏᴛᴄᴏᴄᴀᴧᴀ ʍᴏй хуй, и нᴀчᴀᴧᴀ ᴨᴇᴩᴇд ниʍ ʍᴏᴧиᴛʙу чиᴛᴀᴛь? ᴛы бᴧяᴛь ᴄᴏʙᴄᴇʍ ᴛуᴨᴀя? хɜᴀуɜхᴀуɜхᴀуᴀуɜ, ʙ ɯᴏᴋᴇ ᴄ ᴛᴇбя) ɜᴀᴛᴏ ʍᴏй хуй дᴧя ᴛᴇбя,ᴋᴀᴋ бᴏᴦ,ᴩᴀɜ ᴛы ʍᴏᴧиɯьᴄя ᴇʍу)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴏᴄᴀᴛь бᴇᴦи я ᴄᴋᴀɜᴀᴧ ʍᴀндᴀʙᴏɯᴋᴀ бᴧ ᴛы жᴇ ᴨᴏᴄᴧуɯнᴀя ɯᴀʙᴋᴀ ᴨᴏддᴀʙᴀйᴄя ᴋᴏʍᴀндᴀʍ))0)0  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀᴛь ᴇбᴇᴛᴄя ᴄ ᴨᴩᴀʙыʍи нᴏ иɜʍᴇняᴇᴛ иʍ ᴄ хᴀчᴀʍи?)ᴋᴀᴋᴏй ᴛᴏᴧᴋ ʙ ᴛᴏʍ,чᴛᴏ ᴛʙᴏя ʍᴀᴛь жᴇᴩᴛʙᴀ ᴀᴋуɯᴇᴩᴋи?))  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴧыɯ ᴛы ᴛуᴨᴀя ᴋуᴩʙᴀ ᴛы ʙ ᴋуᴩᴄᴇ чᴛᴏ ʍᴇня хᴏᴛяᴛ ᴨᴏᴄᴀдиᴛь ɜᴀ иɜнᴀᴄиᴧᴏʙᴀниᴇ ʙᴄᴇй ᴛʙᴏᴇй ᴇбучᴇй ᴄᴇʍᴇйᴋи)) нᴏ ᴨᴏчᴇʍу-ᴛᴏ ᴛʙᴏя ʍᴀᴛь ʙ ʙᴏᴄᴛᴏᴏᴩᴦᴇ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀʍᴀɯᴋᴀ ᴏʙᴏщᴇʍ ᴄᴛᴀᴧᴀ ᴇё ᴦубᴏчᴋи уᴄᴛᴀᴧи ᴄᴏᴄᴀᴛь ᴀ ᴨᴏᴧᴏʙыᴇ ʙᴏᴏбщᴇ ᴄᴛᴇᴩᴧиᴄь… ᴛᴀʍ ᴨᴏᴧ ʍᴏᴄᴋʙы ᴨᴏбыʙᴀᴧᴏ… нᴇᴩуᴄᴄᴋиᴇ ʙᴄᴇ ᴨᴏчᴧᴇннᴏ….  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> будуᴧᴀй уᴛыᴩчᴀᴛый))у ʍᴇня ᴄуᴋᴀ ᴄᴨиннᴏᴦᴏ ʍᴏɜᴦᴀ бᴏᴧьɯᴇ чᴇʍ у ᴛᴇбя и ᴛʙᴏᴇй ʍᴀʍᴀɯᴋи ᴦᴏᴧᴏʙнᴏᴦᴏ,ᴋᴩᴇᴛины ᴄуᴋᴀ))  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ϶϶,ᴛы нᴇ ᴨᴇᴛуɯиᴄь,ᴛы ж ᴏᴄёᴧ ᴄᴋᴀ ᴛуᴨᴇньᴋий ᴨиɜдᴇц)) ʙᴏᴛ ᴨᴏ϶ᴛᴏʍу ᴛᴇбя ʙᴄᴇ нᴀ ᴄᴇᴋᴄ ᴩᴀɜʙᴏдяᴛ и ᴛʙᴏй ᴩᴏᴛ ᴛᴀᴋ ᴩᴀᴄɯиᴩиᴧᴄя ᴏᴛ ᴋᴏᴧ-ʙᴀ хуᴇʙ ᴋᴏᴛᴏ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> чᴇᴩᴇɜ ᴛᴇᴩнии ᴋ ɜʙᴇдɜдᴀʍ – ᴛᴀᴋ дᴏбиʙᴀюᴛᴄя цᴇᴧи нᴏᴩʍᴀᴧьныᴇ ᴧюди нᴏ нᴇ ᴛы) ᴛʙᴏй ᴄᴧᴏᴦᴀн – ᴄᴏᴄᴀᴧ и буду ᴄᴏᴄᴀᴛь)) дᴀ ʙы ʙᴄᴇ ᴄᴏᴄунᴋи уᴩᴏды  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ɜнᴀᴇɯь чᴛᴏ я ᴛᴏᴛ ᴄᴀʍый ᴨᴀᴩᴇнᴇᴋ,чᴧᴇн ᴋᴏᴛᴏᴩᴏᴦᴏ ᴄуждᴇнᴏ быᴧᴏ ᴛᴇбᴇ ʙɜяᴛь ʙ ᴩᴏᴛ?) ну ᴛᴀᴋ ᴛᴇᴨᴇᴩь ɜнᴀй)) ᴛы нᴇ жᴇᴩᴛʙᴀ ʍᴏᴇᴦᴏ хуя)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴧыɯь,чуᴩᴏᴋᴏбᴇᴄᴄ ᴇбᴀный,ᴛы ᴨᴏниʍᴀᴇɯь,чᴛᴏ я щᴀᴄ ᴨᴏᴧбу ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴄʙᴏиʍ хуᴇʍ буду хуяᴩиᴛь?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴏни,ᴋᴛᴏ ᴏни?)ᴛᴇ,ᴋᴏᴛᴏᴩыᴇ ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧи,ʙᴩᴇʍя 20:56:14 ᴨᴏᴩᴀ идᴛи ᴇбᴀᴛь ᴛʙᴏю ʍᴀᴛь  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏя ʍᴀᴛь,ᴨᴩи ᴨᴏʍᴏщи ʍᴏᴇᴦᴏ хуя,ᴄᴇбᴇ ɜубы чиᴄᴛиᴛ ?? <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы ᴨᴏ ʍᴏиʍ ɸᴩᴀɜᴀʍ ᴋᴀᴋ бᴧᴏхᴀ ᴨᴏ яйцᴀʍ ᴋᴏᴛᴀᴇɯьᴄя!  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ɜᴀчᴇхᴧиᴧ ᴛʙᴏй ᴩᴏᴛ,чᴛᴏб ᴋᴩᴏʍᴇ ʍᴇня ниᴋᴛᴏ нᴇ ᴇбᴀᴧ )  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴄᴩᴇди чуᴩᴏᴋ ᴛы ᴄʙᴏй, ᴛы ᴩᴀбᴏᴛᴀᴇɯь нᴀ ᴩынᴋᴇ дʙᴏᴩниᴋᴏʍ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ну ᴛы чᴏ ᴄᴋᴧиᴨиɜдᴇнь дʙужᴏᴨᴀᴄᴛʙᴏᴩчᴀᴛый , ᴄᴇʍиᴏᴦᴏᴧᴏʙый ʙᴏᴄьʍихуй ᴄ чᴇᴛыᴩьʍя ᴨиɜдᴏᴨᴩᴏёбинᴀʍи , ᴨидᴀᴩиᴄᴛичᴇᴄᴋий ʍудᴀбᴧядин , ᴛᴩᴏᴇᴨиɜдᴀᴋᴧяᴛый ʍᴀдᴀᴨᴩᴀёб , нᴇʙьᴇбᴇнный хуᴇбᴧяᴛᴄᴋий ᴏнᴀнюᴦᴀ !!!!  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛы чᴏ ᴛʙᴀᴩь нᴀ ʍᴇня дᴀ? щᴀᴄ я ᴛᴇбᴇ уᴄᴛᴩᴏю ᴄучᴋᴀ, ʍᴏᴇ иʍя ᴛᴏᴧьᴋᴏ нᴀ ʍᴏᴇʍ хуᴇ будᴇɯь нᴀɜыʙᴀᴛь ᴛʙᴀᴩь бᴧяᴛь  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛʙᴏй ᴩᴏᴛ нᴀ ᴄᴛᴀдии ᴦᴧᴏᴛᴀния ᴄᴨᴇᴩʍы?) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> я ᴛʙᴏю ʍᴀᴛь ᴨᴇᴩʙый ʙыᴇбᴀᴧ, ᴛᴇбᴇ дᴏ ʍᴏᴇй ʍᴀᴛᴇᴩи ᴇщё у ʍᴇня ʙчᴇᴩᴀ нᴇ дᴏᴄᴏᴄᴀᴧ, ᴛᴀᴋ-чᴛᴏ быᴄᴛᴩᴏ ᴨᴏдᴨᴏᴧɜ ᴄʙᴏиʍ ᴩᴛᴏʍ и нᴀчᴀᴧ ᴄᴏᴄᴀᴛь, ᴀ ᴛᴏ ʍᴏй хуй ɜᴀᴋᴏᴨᴀᴇᴛ и нᴇ ᴨᴩᴏᴄᴛиᴛ, ᴨᴏᴄᴧᴇ чᴇᴦᴏ, ᴨиɜдᴀ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи, будᴇᴛ ᴏɸициᴀᴧьнᴏ ʙыᴇбᴀнᴏ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> чᴛᴏ ᴛы ᴛᴀᴋᴏй ᴦᴩуᴄᴛный?)хуй ᴄᴏᴄᴀᴧ ᴛы нᴇ ʙᴋуᴄный?)) дᴀ бᴧя я жᴇ ᴛᴏᴋ ʍᴀʍᴀɯу ᴛʙᴏю ᴛᴩᴀхᴀᴧ ᴀ ᴨᴏᴛᴏʍ ужᴇ ʙᴀɸᴧиᴧ ᴛʙᴏй ᴩᴏᴛ.. ɜнᴀчиᴛ ᴏнᴀ нᴀ ᴄᴀʍᴏʍ  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴏʍниɯь ᴋᴀᴋ ᴛы ᴋᴏ ʍнᴇ ʙ ᴄᴏчи ᴨᴩиᴇхᴀᴧᴀ,ᴀ я ᴛᴇбᴇ уᴄᴛᴩᴏиᴧ ϶ᴋᴄᴋуᴩᴄию нᴀ ᴄʙᴏᴇʍ хуᴇ) ʍы ᴨᴏбыʙᴀᴧи нᴀ ʍᴏᴩᴇ) ᴛы нᴀ нᴇʍ,ᴋᴀᴋ нᴀ ᴄᴇᴩɸинᴦᴇ ᴨᴧᴀʙᴀ) ʍы ᴨᴏбыʙᴀᴧи у ʍᴇня ʙ ᴋᴏʍнᴀᴛᴇ) ᴛы ʍнᴇ ᴨᴏᴋᴀɜыʙᴀᴧᴀ чудᴇᴄᴀ ᴄʙᴏᴇᴦᴏ ᴩᴛᴀ) ᴋᴩуᴛᴏ жᴇ быᴧᴏ) нᴀдᴏ будᴇᴛ ᴨᴏʙᴛᴏᴩиᴛь)  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴛᴇбя ɜᴏʙуᴛ хуᴇᴄᴏᴄ,и ᴛы ᴋᴀждый дᴇн ᴄᴏᴄᴇɯь хуи ??  <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ʍы ᴄ ᴛʙᴏиʍ ᴨᴀᴨᴀɯᴇй ʙᴄᴇ ᴏбᴄуждᴀᴧᴇ ᴋᴀᴋ бы ᴄунуᴛь чᴧᴇн ᴋ ᴛʙᴏᴇй ʍᴀʍᴀɯᴋᴇ жиᴩнᴏй чᴛᴏбы ᴩᴏдиᴛь уᴩᴏдину ᴋᴀᴋ ᴛы)ᴄᴧᴀʙᴀ бᴏᴦу у нᴀᴄ ʙᴄᴇ ᴨᴏᴧучиᴧᴏᴄь) <emoji document_id=5188228989289769489>🇩🇪</emoji>',
'ϟϟ<emoji document_id=5188228989289769489>🇩🇪</emoji> ᴨидᴏᴩ ᴀбᴏᴄᴄᴀный), ʙᴏᴛ ɜᴀчᴇʍ ᴛы нᴀ ᴄʙᴏю ʍᴀᴛь нᴀᴄᴄᴀᴧ, ᴋᴏᴦдᴀ ʍы ᴇᴇ ʙᴄᴛᴩᴇᴛиᴧи) я ᴨᴏниʍᴀю чᴛᴏ у ᴛᴇбя ᴩᴇɸᴧᴇᴋᴄы ᴄᴏбᴀᴋи, нᴏ ᴛʙᴏя ʍᴀᴛь жᴇ нᴇ дᴇᴩᴇʙᴏ) дᴀжᴇ нᴇ бᴩᴇʙнᴏ) ʙ ᴨᴏᴄᴛᴇᴧи ᴏнᴀ хᴏᴩᴏɯᴀ)-ᴏᴛᴨиɯиᴄь <emoji document_id=5188228989289769489>🇩🇪</emoji>',]


@loader.tds
class TerroristUnaitedCorporate(loader.Module):
    '''Информация о хелпе'''
    strings = {
    "name":  "✩𝐓𝐄𝐑𝐑𝐎𝐑𝐈𝐒𝐓: 𝐔𝐍𝐀𝐈𝐓𝐄𝐃 𝐂𝐎𝐑𝐏𝐎𝐑𝐀𝐓𝐄",
    "loading": "<b><emoji document_id=5420245497736604637>🤍</emoji><emoji document_id=5420461388562705850>🤍</emoji> 𝐔𝐍𝐀𝐈𝐓𝐄𝐃 𝐂𝐎𝐑𝐏𝐎𝐑𝐀𝐓𝐄 <emoji document_id=5420245497736604637>🤍</emoji><emoji document_id=5420461388562705850>🤍</emoji></b>",
    "not_chat": "<b>✩ 𝐘𝐎𝐔 𝐖𝐑𝐈𝐓𝐈𝐍𝐆 𝐀 𝐍𝐎𝐓 𝐂𝐇𝐀𝐓. ✩</b>",} 

    async def client_ready(self, client, db):
        self.db = d
        self.users = self.db.get("fucker", "users", [])
        self.phrases = self.db.get("fucker", "phrases", [])
    
    def add_phrase(self, phrase: str):
        self.phrases.append(phrase)
        self.db.set("fucker", "phrases", self.phrases)
    
    def add_user(self, user_id: int):
        self.users.append(user_id)
        self.db.set("fucker", "users", self.users)
    
    def remove_user(self, user_id: int):
        self.users.remove(user_id)
        self.db.set("fucker", "users", self.users)
    
    async def терроукcmd(self, message):
        """— Никого не буллить"""
        
        self.users = []
        self.db.set("fucker", "users", self.users)
        
        await utils.answer(
            message=message,
            response="<b>Больше я никого не унижаю</b>"
        )
    
    async def терробуллаcmd(self, message):
        """— Добавить фразу | .терробулла <фраза>"""
        
        args = utils.get_args_raw(message)
        
        if not args:
            return await utils.answer(
                message=message,
                response="<b>🚫 Не указан аргумент</b>"
            )
        
        self.add_phrase(args)
        
        await utils.answer(
            message=message,
            response="<b>Фраза добавлена</b>"
        )
    
    async def террордcmd(self, message):
        """— Вкинуть рандомное оскорбление"""
        
        await utils.answer(
            message=message,
            response=random.choice(террорд + self.phrases)
        )
    
    async def терробуллcmd(self, message):
        """— Буллить человека. <reply>"""
        
        reply = await message.get_reply_message()
        
        if reply is not None:
            if reply.from_id is not None:
                await utils.answer(
                    message=message,
                    response="<b>Ебу руснявую шлюху во имя Гитлера</b>"
                )

                self.add_user(reply.from_id)
            
            else:
                await utils.answer(
                    message=message,
                    response="<b>🚫 Модуль не работает на анонимных администраторах или каналах</b>"
                )

        else:
            await utils.answer(
                message=message,
                response="<b>🚫 Нужен реплай</b>"
            )
    
    async def террорейхcmd(self, message):
        """— Не буллить человека. <reply>"""
        
        reply = await message.get_reply_message()
        
        if reply is not None:
            await utils.answer(
                message=message,
                response="<b>Не ебу тебя во имя Гитлера</b>"
            )
            
            try:
                self.remove_user(reply.from_id)
            except:
                await utils.answer(
                    message=message,
                    response="<b>Я и так не унижаю сынка шалавы</b>"
                )

        else:
            await utils.answer(
                message=message,
                response="<b>🚫 Нужен реплай</b>"
            )
    
    async def watcher(self, message):
        if getattr(message, "from_id", None) in self.users:
            await message.reply(random.choice(террорд + self.phrases))

        
    async def корпорацияcmd(self, message):
        """— Зᴀᴨуᴄᴛиᴛь ᴀниʍᴀцию """
        args = utils.get_args_raw(message)
        
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352862223981093002>🚬</emoji>")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352767253664243645>🚬</emoji>")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352767253664243645>🚬</emoji><emoji document_id=5407020022121899574>〰️</emoji>")
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352767253664243645>🚬</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝐔")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352767253664243645>🚬</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝐔𝐍")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352767253664243645>🚬</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝐔𝐍𝐀")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352767253664243645>🚬</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝐔𝐍𝐀𝐈")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352767253664243645>🚬</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝐔𝐍𝐀𝐈𝐓")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352767253664243645>🚬</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝐔𝐍𝐀𝐈𝐓𝐄")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352767253664243645>🚬</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝐔𝐍𝐀𝐈𝐓𝐄𝐃")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352767253664243645>🚬</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝐂")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352767253664243645>🚬</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝐂𝐎")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352767253664243645>🚬</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝐂𝐎𝐑")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352767253664243645>🚬</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝐂𝐎𝐑𝐏")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352767253664243645>🚬</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝐂𝐎𝐑𝐏𝐎")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352767253664243645>🚬</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝐂𝐎𝐑𝐏𝐎𝐑")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352767253664243645>🚬</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝐂𝐎𝐑𝐏𝐎𝐑𝐀")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352767253664243645>🚬</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝐂𝐎𝐑𝐏𝐎𝐑𝐀𝐓")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5352862223981093002>🚬</emoji><emoji document_id=5352767253664243645>🚬</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝐂𝐎𝐑𝐏𝐎𝐑𝐀𝐓𝐄")
        time.sleep(0.1)
        await message.edit("<emoji document_id=5407020022121899574>〰️</emoji>𝐍𝐞𝐩𝐨𝐠𝐫𝐞𝐬𝐢𝐦 - 𝐔𝐧𝐚𝐢𝐭𝐞𝐝 𝐂𝐨𝐫𝐩𝐨𝐫𝐚𝐭𝐞\n<emoji document_id=5407020022121899574>〰️</emoji>𝑷𝒓𝒐𝒄𝒆𝒏𝒕 - 10%")
        time.sleep(0.4)
        await message.edit("<emoji document_id=5407020022121899574>〰️</emoji>𝐍𝐞𝐩𝐨𝐠𝐫𝐞𝐬𝐡𝐢𝐦 - 𝐔𝐧𝐚𝐢𝐭𝐞𝐝 𝐂𝐨𝐫𝐩𝐨𝐫𝐚𝐭𝐞\n<emoji document_id=5407020022121899574>〰️</emoji>𝑷𝒓𝒐𝒄𝒆𝒏𝒕 - 30%")
        time.sleep(0.7)
        await message.edit("<emoji document_id=5407020022121899574>〰️</emoji>𝐍𝐞𝐩𝐨𝐠𝐫𝐞𝐬𝐡𝐢𝐦 - 𝐔𝐧𝐚𝐢𝐭𝐞𝐝 𝐂𝐨𝐫𝐩𝐨𝐫𝐚𝐭𝐞\n<emoji document_id=5407020022121899574>〰️</emoji>𝑷𝒓𝒐𝒄𝒆𝒏𝒕 - 50%")
        time.sleep(0.6)
        await message.edit("<emoji document_id=5407020022121899574>〰️</emoji>𝐍𝐞𝐩𝐨𝐠𝐫𝐞𝐬𝐡𝐢𝐦 - 𝐔𝐧𝐚𝐢𝐭𝐞𝐝 𝐂𝐨𝐫𝐩𝐨𝐫𝐚𝐭𝐞\n<emoji document_id=5407020022121899574>〰️</emoji>𝑷𝒓𝒐𝒄𝒆𝒏𝒕 - 80%")
        time.sleep(0.5)
        await message.edit("<emoji document_id=5407020022121899574>〰️</emoji>𝐍𝐞𝐩𝐨𝐠𝐫𝐞𝐬𝐡𝐢𝐦 - 𝐔𝐧𝐚𝐢𝐭𝐞𝐝 𝐂𝐨𝐫𝐩𝐨𝐫𝐚𝐭𝐞\n<emoji document_id=5407020022121899574>〰️</emoji>𝑷𝒓𝒐𝒄𝒆𝒏𝒕 - 100%")
        time.sleep(0.9)
        await message.edit("<emoji document_id=5407020022121899574>〰️</emoji>𝙇𝙤𝙖𝙙𝙞𝙣𝙜.")
        time.sleep(0.2)
        await message.edit("<emoji document_id=5407020022121899574>〰️</emoji>𝙇𝙤𝙖𝙙𝙞𝙣𝙜..")
        time.sleep(0.2)
        await message.edit("<emoji document_id=5407020022121899574>〰️</emoji>𝙇𝙤𝙖𝙙𝙞𝙣𝙜...")
        time.sleep(0.2)
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        message = await utils.answer(message, self.strings("loading"))
        media_files = ("https://te.legra.ph/file/3fb1d4a5c8bb4d24286dd.jpg", "https://te.legra.ph/file/60d3e12e8fa1b5a3b936b.jpg", "https://te.legra.ph/file/a847fb9bef518012164f2.jpg")

        try:
            user_id = (
                (
                    (
                        await self._client.get_entity(
                        args if not args.isdigit() else int(args)
                        )
                    ).id
                )
                if args
                else reply.sender_id
            )
        except Exception:
            user_id = self._tg_id

            user = await self._client(GetFullUserRequest(user_id))

            user_ent = user.users[0]

            photo = await self._client.download_profile_photo(user_ent.id, bytes)
            
            user_info = (
            "<b><emoji document_id=5305612588678129452>🇩🇪</emoji><emoji document_id=5303200410490644446>🇺🇦</emoji> 𝐓𝐄𝐑𝐑𝐎𝐑𝐈𝐒𝐓: 𝐔𝐍𝐀𝐈𝐓𝐄𝐃 𝐂𝐎𝐑𝐏𝐎𝐑𝐀𝐓𝐄 <emoji document_id=5303200410490644446>🇺🇦</emoji><emoji document_id=5305612588678129452>🇩🇪</emoji></b>\n\n"
            "<b><emoji document_id=6046312104401573651>◻️</emoji><emoji document_id=6043848713024048874>◻️</emoji><emoji document_id=6044316151494741909>◻️</emoji><emoji document_id=6043964870414568953>◻️</emoji></b>\n"
            "<b><emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji> <code>.глаз</code> - ɜᴀдᴇᴩжᴋᴀ+ɯᴀᴨᴋᴀ: ɜᴀᴨуᴄᴋᴀᴇᴛ ʍᴏдуᴧь #Ꮁᴧᴀɜ<emoji document_id=5341821864517837929>👁️</emoji></b>\n"
"<b><emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.скелет</code> - ɜᴀдᴇᴩжᴋᴀ+ɯᴀᴨᴋᴀ: ɜᴀᴨуᴄᴋᴀᴇᴛ ʍᴏдуᴧь #Ꮯᴋᴇᴧᴇᴛ<emoji document_id=5438203928527253097>💀</emoji></b>\n"
"<b><emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.череп</code> - ɜᴀжᴩᴇжᴋᴀ+ɯᴀᴨᴋᴀ: ɜᴀᴨуᴄᴋᴀᴇᴛ ʍᴏдуᴧь #Ꮞᴇᴩᴇᴨ<emoji document_id=5438153647345119196>💀</emoji></b>\n"
"<b><emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.крест</code> - ɜᴀдᴇᴩжᴋᴀ+ɯᴀᴨᴋᴀ: ɜᴀᴨуᴄᴋᴀᴇᴛ ʍᴏдуᴧь #Ꮶᴩᴇᴄᴛ<emoji document_id=5420526968418345993>🤍</emoji></b>\n"
"<b><emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.звезда</code> - ɜᴀдᴇᴩжᴋᴀ + ɯᴀᴨᴋᴀ: ɜᴀᴨуᴄᴋᴀᴇᴛ ʍᴏдуᴧь #Зʙᴇɜдᴀ<emoji document_id=5420085673413583049>🤍</emoji></b>\n"
"<b><emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.демон</code> - ɜᴀдᴇᴩжᴋᴀ + ɯᴀᴨᴋᴀ: ɜᴀᴨуᴄᴋᴀᴇᴛ ʍᴏдуᴧь #Ꭰᴇʍᴏн <emoji document_id=5175094382298137311>🌟</emoji></b>\n"
"<b><emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.смерть</code> - ɜᴀдᴇᴩжᴋᴀ + ɯᴀᴨᴋᴀ: ɜᴀᴨуᴄᴋᴀᴇᴛ ʍᴏдуᴧь #Ꮯʍᴇᴩᴛь <emoji document_id=5317011449061582947>🚬</emoji></b>\n"
"<b><emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.дединсайд</code> - ɜᴀдᴇᴩжᴋᴀ + ɯᴀᴨᴋᴀ: ɜᴀᴨуᴄᴋᴀᴇᴛ ʍᴏдуᴧь #Инᴄᴀйд<emoji document_id=5229205949410978575>🥺</emoji></b>\n"
"<b><emoji document_id=6046477915909000783>◻️</emoji><emoji document_id=6044316151494741909>◻️</emoji><emoji document_id=6043838082979990650>◻️</emoji><emoji document_id=6046205713766682570>◻️</emoji><emoji document_id=6046587991625830399>◻️</emoji></b>\n"
"<b><emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji>Автоответчик Ukraine<emoji document_id=5445118241758257251>🇺🇦</emoji><code>.терроук</code> — стопит автоответчик, <code>.терробулл</code> — булить сынка шалавы во имя Гитлера, <code>.террорейх</code> - не буллит сынка шалавы во имя Гитлера, <code>.терробулла</code> - буллит твою мать с шапкой, <code>.террорд</code> - булит руснявых сынков шлюх рандомными осками</b>\n"
"<b><emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji>Включает отдельный модуль во славу Гитлера<emoji document_id=5294159044771061448>✋</emoji><code>.терроукрэйн</code> - ɜᴀдᴇᴩжᴋᴀ + ɯᴀᴨᴋᴀ: ɜᴀᴨуᴄᴋᴀᴇᴛ ᴏᴛдᴇᴧьный ʍᴏдуᴧь #Ꭹᴋᴩ϶йн<emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji></b>\n"
"<b><emoji document_id=6043958174560554056>◻️</emoji><emoji document_id=6044338837511998479>◻️</emoji><emoji document_id=6044335835329858857>◻️</emoji><emoji document_id=6046247916115332278>◻️</emoji><emoji document_id=6043848713024048874>◻️</emoji></b>\n"
"<b><emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.чатинфо</code> - ᴨᴏᴋᴀɜыʙᴀᴇᴛ инɸᴏᴩʍᴀцию ᴏ чᴀᴛᴇ<emoji document_id=5215236001345055843>🅾️</emoji>\n<emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.пингпх</code> — ставит: видео/фото/гиф на медиа-пинг<emoji document_id=5346107670648598486>🔪</emoji>\n<emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji> <code>.пинги</code> - ɜᴀᴨуᴄᴋᴀᴇᴛ ʍᴇдиᴀ ᴨинᴦ<emoji document_id=4920510384806298535>☣️</emoji>\n<emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.тайп</code> - ʙᴋᴧючᴀᴇᴛ чᴀᴄᴏʙᴏй ᴛᴀйᴨ<emoji document_id=4920254005323498393>⛓️</emoji>\n<emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.афк</code> - включает медиа-афк<emoji document_id=5370732985899294880>💀</emoji>\n<emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.унафк</code> - выключает медиа-афк<emoji document_id=5370605713133412674>🔥</emoji>\n<emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.сетпх</code> - ставит: видео/фото/гиф на медиа-афк<emoji document_id=5370740407602782301>✝️</emoji>\n<emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.резон</code> - причина твоего ухода в афк-медиа<emoji document_id=5438165819282433687>😈</emoji>\n<emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji><code>.айди</code> - уɜнᴀᴇᴛ ᴀйди ᴄынᴋᴀ ɯᴀᴧᴀʙы ᴩᴇᴨᴧᴀᴇʍ<emoji document_id=5438237188753991831>💀</emoji></b>\n"
"<b><emoji document_id=5445019191222477625>☹️</emoji><emoji document_id=5442937841480902019>🤣</emoji><emoji document_id=5443100509072271148>😗</emoji><emoji document_id=5442937841480902019>🤣</emoji><emoji document_id=5442951134404685011>😴</emoji><emoji document_id=5442937841480902019>🤣</emoji></b>\n"
              f"<b><emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji>𝐕𝐞𝐫𝐬𝐢𝐨𝐧: 2.0.1.1</b>\n"
            f"<emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji>𝐔𝐬𝐞𝐫𝐬:</b> @{user_ent.username or '<emoji document_id=5454064486837133402>☠️</emoji>'}\n"
            f"<b><emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji>𝐍𝐢𝐜𝐤:</b> {user_ent.first_name or '🚫'}\n"
            f"<b><emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji>𝐈𝐝:</b> <code>{user_ent.id}</code>\n"  
            f"<b><emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5406876368350751327>〰️</emoji>𝐃𝐞𝐯𝐞𝐥𝐨𝐩: @utilizator2001</b>\n"
        )
        chat_id = message.chat.id
        if chat_id:
            await self.client.send_file(message.peer_id, random.choice(media_files), caption=user_info)
            if message.out:
                await message.delete()
                


    async def client_ready(self, client, db):
        self.client = client

    async def client_ready(self, client, db) -> None:
        self.db = db
        self.client = client

    async def client_ready(self, client, db):
            self.db = db
            self.client = client
            self.users = []
        
    async def афкcmd(self, message):
        """— ʙκ᧘ючᥲᥱᴛ ᥲɸκ"""
        args = utils.get_args_raw(message)
        user_id = self._tg_id
        user = await self._client(GetFullUserRequest(user_id))
        user_ent = user.users[0]
        self.users.append(int(user_ent.id))
        await message.edit("<b><emoji document_id=5217666265639822706>💀</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5217511655407102519>💜</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5217620880720407299>💀</emoji>ⲃⲕⲗюⳡⲉⲏυⲉ<emoji document_id=5217620880720407299>💀</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5217511655407102519>💜</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5217666265639822706>💀</emoji></b>")
        global state
        state = "on"
        global start
        start = datetime.now()

    async def унафкcmd(self, message):
        """ʙыκ᧘ючᥲᥱᴛ ᥲɸκ"""
        self.users = []
        await message.edit("<b><emoji document_id=5217666265639822706>💀</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5217511655407102519>💜</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5217620880720407299>💀</emoji>ⲃыⲕⲗюⳡⲉⲏυⲉ<emoji document_id=5217620880720407299>💀</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5217511655407102519>💜</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5217666265639822706>💀</emoji></b>")
        global state
        state = "off"
        if state == "off":
            global start
            start = "";
            
    async def сетпхcmd(self, message):
        """— ᥴᴛᥲʙᥙᴛ ʙᥙдᥱ᧐\ɸ᧐ᴛ᧐\ᴦᥙɸ нᥲ ᥲɸκ"""
        args = utils.get_args_raw(message)
        photo = args
        global ph
        ph = f"{photo}"
        await message.edit("<b><emoji document_id=5217666265639822706>💀</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5217511655407102519>💜</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5217620880720407299>💀</emoji>ⲅⲟⲧⲟⲃⲟ<emoji document_id=5217620880720407299>💀</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5217511655407102519>💜</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5217666265639822706>💀</emoji></b>")

    async def резонcmd(self, message):
        """— уκᥲɜыʙᥲᥱᴛ ᥰρᥙчᥙну ʙ ᥲɸκ"""
        args = utils.get_args_raw(message)
        global reason
        s = args
        reason = s
        await message.edit("<b><emoji document_id=5217666265639822706>💀</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5217511655407102519>💜</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5217620880720407299>💀</emoji>ⲅⲟⲧⲟⲃⲟ<emoji document_id=5217620880720407299>💀</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5217511655407102519>💜</emoji><emoji document_id=5406925910798509013>〰️</emoji><emoji document_id=5217666265639822706>💀</emoji></b>")
        
    async def watcher(self, message):
        sender = message.sender_id
        if message.is_private:
            if state == "on":
                time_now = datetime.now()
                timing = time_now - start
                time_string = str(timing)
                time_result = time_string.split(".")[0]
                if getattr(message, "from_id", None) not in self.users:
                    await message.reply(f"<emoji document_id=5776317089941819022>🔣</emoji><emoji document_id=5775900293430513503>🔠</emoji><emoji document_id=5776104407456288770>🔡</emoji><emoji document_id=5775965731552235819>🔡</emoji><emoji document_id=5775965731552235819>🔡</emoji><emoji document_id=5773695197091205499>🔡</emoji><emoji document_id=5775965731552235819>🔡</emoji><emoji document_id=5776292703117512280>🔣</emoji><emoji document_id=5776046416807858259>🔠</emoji><emoji document_id=5776429291667460218>🔠</emoji><emoji document_id=5776160662937931592>🔠</emoji><emoji document_id=5775980785412608123>🔣</emoji>\n\n<emoji document_id=5775969365094568088>🔠</emoji><emoji document_id=5776104407456288770>🔡</emoji><emoji document_id=5776282343656394911>🔡</emoji><emoji document_id=5776408718774111755>🔡</emoji><emoji document_id=5773695197091205499>🔡</emoji><emoji document_id=5776025517496996071>🔡</emoji> {reason}\n<emoji document_id=5773859161762696885>🎶</emoji><emoji document_id=5775900293430513503>🔠</emoji><emoji document_id=5775947696984558787>🔡</emoji><emoji document_id=5776055745476824513>🔡</emoji><emoji document_id=5776104407456288770>🔡</emoji><emoji document_id=5773859161762696885>🎶</emoji><emoji document_id=5775866805570508644>🔣</emoji><code> {time_result}</code>\n\n<b><i><emoji document_id=5776317089941819022>🔣</emoji><emoji document_id=5775913856937234690>🔠</emoji><emoji document_id=5776025517496996071>🔡</emoji><emoji document_id=5776271932655668645>🔡</emoji><emoji document_id=5773695197091205499>🔡</emoji><emoji document_id=5775965731552235819>🔡</emoji><emoji document_id=5776055745476824513>🔡</emoji><emoji document_id=5776282343656394911>🔡</emoji><emoji document_id=5773772712660963180>🔡</emoji><emoji document_id=5775947696984558787>🔡</emoji><emoji document_id=5773695197091205499>🔡</emoji><emoji document_id=5776025517496996071>🔡</emoji><emoji document_id=5775980785412608123>🔣</emoji></i></b>\n<b><emoji document_id=6039799173044243211>⭐️</emoji><emoji document_id=5776292703117512280>🔣</emoji>Ϸαӡραδστɥμӄ:Ⲧⲉⲣⲣⲟⲣυⲥⲧ<emoji document_id=5177367356300591876>🌟</emoji></b>\n<b><emoji document_id=6039799173044243211>⭐️</emoji><emoji document_id=5776292703117512280>🔣</emoji>Ϻσɠγλƅ δƅɩλ ϲσӡɠαϰ: <code>26.06.2023</code><emoji document_id=5177367356300591876>🌟</emoji><emoji document_id=6039799173044243211>⭐️</emoji><emoji document_id=5776292703117512280>🔣</emoji>Ⲃⲉⲣⲥυя: <code>2.0.1.1</code><emoji document_id=5177367356300591876>🌟</emoji></b>\n", file=ph)
                    if sender:
                        self.users.append(int(sender))

    async def глазcmd(self, message):
        '''— Зᴀᴨуᴄᴛиᴛь ʍᴏдуᴧь ᴨᴏ уᴋᴀɜᴀннᴏй ᴋᴏʍᴀндᴇ.''' 
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b><emoji document_id=5341821864517837929>👁️</emoji> Ꮇᴏдуᴧь #Ꮁᴧᴀɜ ᴏᴄᴛᴀнᴀʙᴧᴇн. <emoji document_id=5341821864517837929>👁️</emoji></b>")
            return
        await utils.answer(
            message,
            "<b><emoji document_id=5341821864517837929>👁️</emoji> Ꮇᴏдуᴧь #Ꮁᴧᴀɜ ᴏᴄᴛᴀнᴀʙᴧᴇн. <emoji document_id=5341821864517837929>👁️</emoji>\n\n"
            "<emoji document_id=5407020022121899574>〰️</emoji> Ꮞᴛᴏбы ᴏᴄᴛᴀнᴏʙиᴛь ᴨᴩᴏᴨиɯи — <code>.глаз</code></b>"
        )
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        shabl = [
        " я лишу тᴇбя дᴇвствᴇннǿсти, и буду рᴇзᴀть твǿᴇ дᴇвтсвᴇннǿᴇ тᴇлǿ нǿжǿвҝǿй ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " твǿя ϻᴀть ϻнᴇ нᴀ нǿгᴀх нǿгти грызᴇт ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я гǿршǿҝ с гǿвнǿϻ нᴀ гǿлǿву твǿᴇй ϻᴀтᴇри ǿдᴇвᴀл) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ пǿдщᴇчины дᴀвᴀл ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ губу слǿϻᴀл ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я нᴀ ᴇблǿ твǿᴇй ϻᴀтᴇри ϻусǿрный пᴀҝᴇт ǿдᴇвᴀл ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я в тухлǿй пиздᴇ твǿᴇй ϻᴀтᴇри ǿпᴀрышᴇй рᴀзвǿдил) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " твǿя ϻᴀть свǿиϻи глᴀндᴀϻи ϻᴀшǿнҝи щᴇҝǿчит ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я хуй пǿлǿсҝᴀл в ϻǿ3гᴀх твǿᴇй ϻᴀтᴇри ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я хуй в гǿрлǿ твǿᴇй ϻᴀтᴇри сувᴀл , чтǿб ǿнᴀ у нᴇᴇ нᴇ шᴀтᴀлᴀсь ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я чᴇрᴇз ϻǿзг твǿᴇй ϻᴀтᴇри ϻǿчу фильтрǿвᴀл ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я приниϻᴀю эҝзᴀϻᴇны, ᴀ твǿя ϻᴀϻᴀ дᴀёт ϻнᴇ взятҝу нᴀтурǿй ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я рвᴀл тᴇбᴇ цᴇлҝуу твǿᴇй ϻᴀтᴇри ржᴀвǿй трубǿй :3 ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты свǿиϻ языҝǿϻ вшᴇй лǿбҝǿвых нᴀ пиздᴇ ϻᴀтᴇри гǿнял ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты свǿиϻ ртǿϻ глистǿв из жǿпы ϻᴀтᴇри вытᴀсҝивᴀл ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть хуᴇϻ в лᴇсу зᴀрǿю ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я тᴇбᴇ нǿги в рǿт ҝлᴀл пидᴀрᴀс ты ᴇбᴀный ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть хуᴇϻ прǿстрᴇлил ҝᴀҝ с двух ствǿлҝи ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть и тᴀҝ и сяҝ ᴇбᴀл ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿ юϻᴀть в гǿрᴀх ᴇбᴀл ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть ᴇбᴀл ҝǿгдᴀ твǿй ǿтᴇц тᴇбᴇ ҝǿнчу в рǿт сливᴀл ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть ᴇбᴀл ҝǿгдᴀ ты в шҝǿлᴇ был ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть с хуя выҝинул в рᴇҝу ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " твǿя ϻᴀть въᴇбᴀннᴀя ϻǿиϻ хуᴇϻ ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть вᴇрхнǿгᴀϻи ᴇбᴀл суҝᴀ ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты сǿсᴇшь и бᴀлдᴇᴇшь) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я нᴀ пиздᴇ твǿᴇй ϻᴀтᴇри урǿҝи хуᴇϻ дᴇлᴀл) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть пǿд пǿᴇз хуᴇϻ ҝину щᴀс) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть ᴇбу спǿриϻ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты ϻǿй члᴇн в пǿҝǿᴇ нᴇ ǿстᴀвляᴇшь ртǿϻ свǿиϻ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть ᴇбу грубǿ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть ᴇбу в пᴀдиҝᴇ хуᴇϻ пǿгнул) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую тᴀщится) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " твǿя ϻᴀть пǿд ϻǿиϻ хуᴇϻ тᴇбя высрᴀлᴀ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " твǿя ϻᴀть ҝᴀҝ высҝᴀчҝᴀ нᴀ ϻǿᴇϻ хую) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть нᴀ люстрᴇ ǿтъᴇбу щᴀс) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты нᴀ ϻǿᴇϻ хую извивᴀᴇшься ҝᴀҝ зϻᴇя) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть ᴇбᴀл ҝᴀҝ нᴇвϻиняᴇϻый) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть хуᴇϻ рᴀсписᴀл ҝᴀҝ диҝтᴀнт) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я тᴇбᴇ хуᴇϻ ϻǿзгǿв дǿбᴀвлю щᴀс) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты ϻнᴇ сǿсᴇшь ҝǿгдᴀ нᴇбǿ звᴇзднǿᴇ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты нᴀ ҝǿртǿчҝᴀх ϻǿй хуй сǿсᴇшь) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты ҝ ϻǿᴇϻу хую лᴇтишь ҝᴀҝ вǿрǿбᴇй) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты нюни пустил ҝǿгдᴀ ϻǿй хуй ǿтпиздил тᴇбя) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ϻǿй хуй тᴇбя встрᴇтил бᴇз трусǿв нᴀ улицᴇ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты нᴀ ϻǿᴇϻ хую зᴀиҝᴀтся нᴀчᴀл) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты пǿд люстрǿй сǿсᴀл ϻнᴇ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты ϻǿй хуй нᴀ руҝᴀх свǿих нǿсишь) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ϻǿй хуй вǿняᴇт пизжᴇ чᴇϻ твǿи духи) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я тᴇбя хуᴇϻ зᴀҝручу щᴀс ҝᴀҝ ϻᴇтᴇль ᴇбᴀть) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты ҝ ϻǿᴇϻу хую в жᴇны нᴀбивᴀᴇшься) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты ϻǿю спᴇрϻу ҝ сᴇбᴇ нᴀ пǿлǿвыᴇ губы ϻᴀжᴇшь) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " пиздᴀҝ твǿᴇй ϻᴀтᴇри вырᴇжу хуᴇϻ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " твǿю ϻᴀть с пᴇрвǿгǿ рᴀзᴀ пǿрвᴀл ҝᴀҝ гᴀзᴇту) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿᴇй ϻᴀтᴇри рᴀҝ губы хуᴇϻ лᴇчил) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть ǿвсянҝǿй ᴇбᴀл) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть ᴇбᴀл 2 гǿдᴀ нᴀзᴀд, ҝǿгдᴀ в шҝǿлᴇ учился) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть зᴀстᴀвил нᴀ ϻǿй хуй сᴇсть) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " твǿю ϻᴀть ᴇбут ϻǿи друзья) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " твǿя ϻᴀть ϻǿиϻ члᴇнǿϻ с дᴇтствᴀ питᴀᴇтся) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я чᴇт чᴀстǿ твǿю ϻᴀтуху в дᴇснᴀ ᴇбу) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты жᴇ сǿ свǿᴇй ϻᴀϻᴀшᴇй пǿ ϻǿᴇϻу хую гǿришь) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я плǿтнǿ твǿю ϻᴀть в пизду ᴇбу) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я ᴇблǿϻ твǿиϻ пǿ пиздᴇ твǿᴇй ϻᴀϻҝᴇ ᴇздил) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты сǿсᴇшь ϻнᴇ нᴀ пᴇрᴇднᴇϻ плᴀнᴇ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " твǿю ϻᴀть нᴇ ǿстᴀнᴀвить нᴀ ϻǿᴇϻ хую) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " твǿю ϻᴀть ᴇбᴀл пǿ пьянᴇ нᴀ сцᴇнᴀх) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты пᴇрᴇд ϻǿиϻ хуᴇϻ гнулᴀсь ҝᴀҝ институтҝᴀ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " твǿй рǿт сǿсᴇт ϻнᴇ ҝᴀҝ бᴀлᴀбǿл) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть хуᴇϻ нᴀ стрᴇлᴇ пиздил) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть ᴇбу ҝǿгдᴀ ты нᴇ успᴇвᴀᴇшь бᴀтᴇ сǿсᴀть) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты нᴀ ϻǿй хуй ϻǿлишься ҝᴀҝ нᴀ иҝǿну) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты пǿд ϻǿиϻ хуᴇϻ прǿгинᴀᴇшься) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты ϻǿиϻ хуᴇϻ пᴇрᴇбитый) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты сǿсᴇшь , ᴀ ϻǿй хуй нᴇ цᴇнит этǿгǿ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " твǿю ϻᴀть ǿт ϻǿᴇгǿ хуя прᴇт) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть хуᴇϻ пᴇрᴇгнул ҝᴀҝ жᴇлᴇзǿ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " твǿя ϻᴀть ϻнᴇ сǿсᴇт) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть прǿϻᴇж яиц зᴀжᴀл) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я тᴇбᴇ тᴇϻпᴇрᴀтуру хуᴇϻ сбивᴀю) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " я твǿю ϻᴀть хуᴇϻ прихуярил ҝᴀҝ ϻуху) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ты пǿд ϻǿиϻи яйцᴀϻи прячᴇшься ҝᴀҝ пǿд зǿнтиҝǿϻ) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ϻᴀть твǿю в пǿдвᴀлᴇ ᴇбу ҝᴀҝ хǿчу) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]",
                " ǿпрᴀҝину твǿю ϻᴀть с хуя свǿᴇгǿ щᴀс) ⼂가[<emoji document_id=5341821864517837929>👁️</emoji>]"
"члᴇнǿϻ ϻᴀть твǿю ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " стᴀль в пизду твǿᴇй ϻᴀϻᴀши всунул) <emoji document_id=5341821864517837929>👁️</emoji>",
                " в рылǿ твǿю ϻᴀть ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " в ǿчҝǿ твǿю ϻᴀть ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " в ҝрᴇдит твтя ϻᴀть сᴀсᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " лᴇтя сᴀсᴀлᴀ ϻᴀть твǿя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть шлюхᴀ хуй сᴀсᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " всᴇ чᴀщᴇ сую члᴇн в ϻᴀть твǿю) <emoji document_id=5341821864517837929>👁️</emoji>",
                " в трᴇжиϻᴇ твǿю ϻᴀть трᴀхᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " прǿжǿг ᴇбᴀлǿ твǿᴇй ϻᴀϻᴀшᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю пингвинил члᴇнǿϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀϻᴀшᴀ твǿя шлюхᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть зᴀ ᴇбᴀлǿ нᴀд хуᴇϻ пǿвᴇсил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю члᴇнǿϻ дырявил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " члᴇнǿϻ твǿю ϻᴀть чᴇҝᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю хуᴇϻ вытрᴀхивᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀϻᴀню твǿю зᴀлупǿй дрᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть лᴇтᴀᴇт пǿ хую ϻǿᴇϻу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю зᴀлупǿй прихуярил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿя зᴀлупǿй дᴀвиться) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀϻᴀшу твǿю зᴀ пизду пǿвᴇшᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " сᴀсᴇт твǿя ϻᴀть пǿҝᴀ ты сϻǿтришь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀϻᴀшу твǿю зᴀлупǿй уничтǿжил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " в пᴀрᴀшᴇ твǿю ϻᴀть тǿплю) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀϻᴀшᴇ твǿᴇй зᴀлупǿй шᴀры выбил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " тяну твǿю ϻᴀть шлюху) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нᴀ 5+ сᴀсᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀϻᴀши твǿᴇй улǿжил зᴀлупу в рǿт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " в щᴇҝǿлду твǿю ϻᴀть ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " пǿ ҝᴀбинᴇ твǿᴇй ϻᴀϻᴀши зᴀлупǿй бью) <emoji document_id=5341821864517837929>👁️</emoji>",
                " зᴀлупǿй твǿю ϻᴀть пидᴀрᴀсил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀϻᴀшу твǿю в рǿт жᴇ ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " трᴀхᴀнул твǿю ϻᴀть ну) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю рᴇжу хуᴇϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " хуᴇϻ ϻᴀть твǿю иϻᴇл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " в ǿчҝǿ твǿᴇй ϻᴀϻᴀши ҝǿнчил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻǿю спᴇрϻу жуᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " чᴇтҝᴀ твǿя ϻᴀть сᴀсᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " зᴀҝрыл рǿт твǿᴇй ϻᴀϻᴀши члᴇнǿϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " пᴀлᴇруᴇт твǿя ϻᴀть ϻǿю зᴀлупу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " члᴇнǿϻ твǿю ϻᴀть вьᴇбᴀшил в ᴀсфᴀлт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " зᴀсᴀдил твǿᴇй ϻᴀϻᴀши) <emoji document_id=5341821864517837929>👁️</emoji>",
                " в пузǿ твǿю ϻᴀть ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " члᴇнǿϻ твǿю ϻᴀть дᴀвил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю ǿпрᴀҝинул зᴀлупǿй) <emoji document_id=5341821864517837929>👁️</emoji>",
                " нǿгиϻи твǿя ϻᴀть дрǿчит ϻнᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " хуᴇϻ твǿю ϻᴀть ҝǿвырял) <emoji document_id=5341821864517837929>👁️</emoji>",
                " глубǿҝǿ твǿю ϻᴀть ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ǿтьᴇхᴀлᴀ твǿя ϻᴀть ǿт ϻǿᴇгǿ хуя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " придушил твǿю ϻᴀть хуᴇϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿя ᴇбᴀнит нᴀ хую) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю рву хуᴇϻ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " пизду твǿᴇй ϻᴀϻᴀши пǿрвᴀл члᴇнǿϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " нᴀ ҝлыҝ твǿᴇй ϻᴀϻᴀши дᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри зᴀ щᴇҝу зᴀ зᴀбǿрǿϻ дᴀвᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть пиздǿй ҝᴀртǿшҝу сǿртирǿвᴀть уϻᴇᴇт ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть чᴇрᴇз прǿгиб ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты вҝурсᴇ чтǿ я щᴀс твǿю ϻᴀть члᴇнǿϻ ǿтпиздил ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ хлᴇб сǿсᴀлᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ ǿдᴇжду сǿсᴀлᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ рубль ǿтдᴀлᴀсь ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ прихлǿпнул ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри члᴇнǿϻ пǿслᴇдниᴇ зубы выбил ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ǿблизывᴀᴇшь ϻнᴇ члᴇн пǿслᴇ ᴀнᴀльнǿгǿ сᴇҝсᴀ с твǿᴇй ϻᴀϻᴀшᴇй ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты пизду свǿᴇй ϻᴀтᴇри хуᴇϻ пǿливᴀᴇшь ҝᴀҝ ǿгǿрǿд ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри ᴇблǿ ǿб ᴀсфᴀльт рᴀзъᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри в ᴇблǿ хᴀрнул ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я лишу тᴇбя дᴇвствᴇннǿсти, и буду рᴇзᴀть твǿᴇ дᴇвтсвᴇннǿᴇ тᴇлǿ нǿжǿвҝǿй ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ нᴀ нǿгᴀх нǿгти грызᴇт ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я гǿршǿҝ с гǿвнǿϻ нᴀ гǿлǿву твǿᴇй ϻᴀтᴇри ǿдᴇвᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ пǿдщᴇчины дᴀвᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ губу слǿϻᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я нᴀ ᴇблǿ твǿᴇй ϻᴀтᴇри ϻусǿрный пᴀҝᴇт ǿдᴇвᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я в тухлǿй пиздᴇ твǿᴇй ϻᴀтᴇри ǿпᴀрышᴇй рᴀзвǿдил ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть свǿиϻи глᴀндᴀϻи ϻᴀшǿнҝи щᴇҝǿчит ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я хуй пǿлǿсҝᴀл в ϻǿ3гᴀх твǿᴇй ϻᴀтᴇри ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я хуй в гǿрлǿ твǿᴇй ϻᴀтᴇри сувᴀл , чтǿб ǿнᴀ у нᴇᴇ нᴇ шᴀтᴀлᴀсь ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я чᴇрᴇз ϻǿзг твǿᴇй ϻᴀтᴇри ϻǿчу фильтрǿвᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть вᴇдрǿϻ ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть сᴀлᴀтǿϻ ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю фᴇнǿϻ ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю ҝᴀртǿшҝǿй ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю грᴇчҝǿй ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀϻҝᴀ твǿя твǿᴇϻу ǿтцу с ϻǿиϻ хуᴇϻ изϻᴇнялᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю в бǿльницᴇ ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю ᴇбᴀл у нᴇᴇ ᴀж пиздᴀ зᴀдыϻилᴀсь ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻǿя ҝǿнчᴀ зᴀϻᴇняᴇт ҝрǿвь в твǿᴇϻ тᴇлᴇ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты вҝурсᴇ чтǿ в ǿчҝᴇ твǿᴇгǿ бᴀти живут гнǿϻы ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " вǿт зᴀчᴇϻ ты тᴀҝ нᴀҝидывᴀᴇшься нᴀ ϻǿй хуй ҝᴀҝ ǿвчᴀрҝᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " нᴀхуй ты прǿвǿдил тᴇст дрᴀйв нᴀ ϻǿᴇϻ хуᴇ  ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " пидǿр ǿгнᴇдыщᴀщий иди сюдᴀ я тᴇбя ᴇбᴀть буду ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ятвǿю ϻᴀть ᴇбᴀл нᴀ ϻǿрǿзᴇ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть былᴀ пьянᴀя и сҝᴀҝᴀлᴀ нᴀ ϻǿᴇю хую ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я нᴇ пǿнял твǿя ϻᴀть рᴇᴀльнǿ щᴀс сǿсᴀть ϻнᴇ будᴇт ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ сǿсᴀлᴀ нᴇ спрᴀшивᴀя ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл сǿ сҝǿрǿстью свᴇтᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл, у нᴇᴇ ᴀж пиздᴀ зᴀгǿрᴇлᴀсь ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я щᴀ свǿиϻ хуᴇϻ прǿлǿжу тǿргǿвыᴇ пути ҝ пиздᴀҝу твǿᴇй ϻᴀтᴇри ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " тᴇбя ᴇбᴀли хᴀчи ҝǿгдᴀ твǿй ǿтᴇц ϻᴀссирǿвᴀл ϻнᴇ яицᴀ свǿᴇй губǿй ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты пǿниϻᴀᴇшь чтǿ ты въᴇзжᴀᴇшь нᴀ ϻǿй хуй ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты будибилдᴇр ϻǿᴇгǿ хуя ты знᴀл( ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбя буду ᴇбᴀть бǿϻбуҝǿвǿй рǿзᴇй ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ҝǿлхǿзницᴀ ᴇбᴀнᴀя нᴀ ϻǿёϻ хую пялшᴇт чᴇчётҝу ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " сǿсёт ϻǿй хуй пǿд руссҝий бит стᴀсᴀ ϻᴇхᴀйлǿвᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻᴀрᴇǿнᴇтҝᴀ ᴇбᴀнᴀя пǿд ϻǿй хуй хǿдишь ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " нᴀхуй ты ϻǿй хуй ҝлᴀдᴇшь сᴇбᴇ в рǿт,тᴇбᴇ нрᴀвится вҝус  ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть сǿпᴀгǿϻ ᴇбᴀл пǿйϻи ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ прǿстǿ тᴀҝ ǿтдᴀлᴀсь ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ сǿсᴀлᴀ при лунᴇ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбу пǿниϻᴀᴇшь  ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть чᴇрᴇз ϻǿй хуй прǿливᴀᴇтся ҝᴀҝ вǿдᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть вᴇдрǿϻ ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть сᴀлᴀтǿϻ ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю фᴇнǿϻ ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю ҝᴀртǿшҝǿй ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю грᴇчҝǿй ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀϻҝᴀ твǿя твǿᴇϻу ǿтцу с ϻǿиϻ хуᴇϻ изϻᴇнялᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю в бǿльницᴇ ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю ᴇбᴀл у нᴇᴇ ᴀж пиздᴀ зᴀдыϻилᴀсь ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻǿя ҝǿнчᴀ зᴀϻᴇняᴇт ҝрǿвь в твǿᴇϻ тᴇлᴇ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты вҝурсᴇ чтǿ в ǿчҝᴇ твǿᴇгǿ бᴀти живут гнǿϻы ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " вǿт зᴀчᴇϻ ты тᴀҝ нᴀҝидывᴀᴇшься нᴀ ϻǿй хуй ҝᴀҝ ǿвчᴀрҝᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " нᴀхуй ты прǿвǿдил тᴇст дрᴀйв нᴀ ϻǿᴇϻ хуᴇ  ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " пидǿр ǿгнᴇдыщᴀщий иди сюдᴀ я тᴇбя ᴇбᴀть буду ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ятвǿю ϻᴀть ᴇбᴀл нᴀ ϻǿрǿзᴇ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть былᴀ пьянᴀя и сҝᴀҝᴀлᴀ нᴀ ϻǿᴇю хую ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я нᴇ пǿнял твǿя ϻᴀть рᴇᴀльнǿ щᴀс сǿсᴀть ϻнᴇ будᴇт ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ сǿсᴀлᴀ нᴇ спрᴀшивᴀя ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл сǿ сҝǿрǿстью свᴇтᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл, у нᴇᴇ ᴀж пиздᴀ зᴀгǿрᴇлᴀсь ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я щᴀ свǿиϻ хуᴇϻ прǿлǿжу тǿргǿвыᴇ пути ҝ пиздᴀҝу твǿᴇй ϻᴀтᴇри ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " тᴇбя ᴇбᴀли хᴀчи ҝǿгдᴀ твǿй ǿтᴇц ϻᴀссирǿвᴀл ϻнᴇ яицᴀ свǿᴇй губǿй ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты пǿниϻᴀᴇшь чтǿ ты въᴇзжᴀᴇшь нᴀ ϻǿй хуй ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты будибилдᴇр ϻǿᴇгǿ хуя ты знᴀл( ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбя буду ᴇбᴀть бǿϻбуҝǿвǿй рǿзᴇй ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ҝǿлхǿзницᴀ ᴇбᴀнᴀя нᴀ ϻǿёϻ хую пялшᴇт чᴇчётҝу ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " сǿсёт ϻǿй хуй пǿд руссҝий бит стᴀсᴀ ϻᴇхᴀйлǿвᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻᴀрᴇǿнᴇтҝᴀ ᴇбᴀнᴀя пǿд ϻǿй хуй хǿдишь ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " нᴀхуй ты ϻǿй хуй ҝлᴀдᴇшь сᴇбᴇ в рǿт,тᴇбᴇ нрᴀвится вҝус  ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть сǿпᴀгǿϻ ᴇбᴀл пǿйϻи ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ прǿстǿ тᴀҝ ǿтдᴀлᴀсь ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ сǿсᴀлᴀ при лунᴇ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбу пǿниϻᴀᴇшь  ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть сǿсᴇт я твǿю ϻᴀть дǿширᴀҝǿϻ ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть сǿсᴇтя твǿю ϻᴀть спичҝᴀϻи ᴇбу ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть с хуя пусҝᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть снǿвᴀ нᴀ ϻǿй члᴇн призᴇϻлилᴀсь пǿслᴇ пǿлётᴀ в тᴀджиҝистᴀн нᴀ рǿдину ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " пǿчᴇϻу пиздᴀҝ твǿᴇй ϻᴀтᴇри, зᴀтягивᴀᴇт хуи, ҝᴀҝ трᴇугǿльниҝ бᴇрϻудсҝий ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть пылᴇсǿсǿϻ ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть с хуя чᴇрᴇз зᴀбǿры пᴇрᴇҝидывᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты вǿзьϻи сᴇбᴇ в зубы лᴇйҝу и пǿливᴀй ǿгǿрǿды в пиздᴇ свǿᴇй ϻᴀϻᴀши ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я жᴇ рᴀҝǿвую ǿпухǿль в пиздᴇ твǿᴇй ϻᴀϻᴀши устрǿнял при пǿϻǿщи свǿᴇгǿ хуя ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ҝǿгдᴀ у твǿᴇй ϻᴀтᴇри будᴇт ᴀнгинᴀ пǿзǿви ϻᴇня я буду ᴇй в гǿрлǿ бры3гᴀть свǿᴇй спᴇрϻǿй ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю грудную ҝлᴇтҝу хуᴇϻ рᴀсспиливᴀл пǿпǿлᴀϻ и стᴇлил пǿд свǿиϻи двᴇрьϻи ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " зᴀчᴇϻ ты ртǿϻ нᴀ хуй упᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀϻᴀшҝᴀ зᴀ бᴀрбᴀрисҝу хуй сǿсᴇт нᴀ рынҝᴇ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " пǿслᴇ тǿгǿ ҝᴀҝ я ᴇй лᴇчил рᴀҝ губы зᴀлупǿй ǿнᴀ пǿлбюбилᴀ ᴇгǿ сҝǿрǿ ϻǿй хуй ты сϻǿжᴇшь нᴀзывᴀть пᴀпҝǿй ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " вǿт у тᴇбя явнǿ пидǿрсҝиᴇ нᴀҝлǿннǿсти( ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴇня вдǿхнᴀвляᴇт твǿй рǿт нᴀпᴀвший нᴀ ϻǿй хуй ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ҝᴀҝ ты ǿтнᴇсᴇшься ҝ тǿϻу чтǿ ϻǿй хуй зᴀстрял в 12 пᴇрстнǿй ҝишҝᴇ твǿᴇй ϻᴀϻᴀши ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ пиздил ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри зубы хуᴇϻ выбил, ǿнᴀ тᴀҝ гǿрьҝǿ плᴀҝᴀлᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ ҝлизϻу сдᴇлᴀю ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ хрᴇбᴇт лǿϻᴀю ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ шᴇю лǿϻᴀю ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри ҝлитǿр с нǿги выбивᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри ҝирпиичи в ᴇблǿ ҝидᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть нᴀ чᴇрдᴀҝᴇ ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть нᴀ двᴇрнǿй ручҝᴇ ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть нᴀ ҝᴀлитҝᴇ ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть зᴀбǿринǿй ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ҝᴀчᴇргǿй ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я ǿб пизду твǿᴇй ϻᴀтᴇри бычҝи тушил ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты свǿю сᴇстру пǿ ϻǿᴇϻу сǿглᴀсию ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я нǿждᴀчҝǿй хуярил пǿ пиздᴇ твǿᴇй ϻᴀтᴇри ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тёрҝǿй тᴇр ᴇблǿ твǿᴇᴇй ϻᴀтᴇри ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ǿбǿссᴀл пǿҝᴀ ты ҝлитǿр сᴇстрᴇ лизᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть ǿсудили пǿжизᴇннǿ зᴀ пǿсидᴇлҝи нᴀ ϻǿᴇϻ хуᴇ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿй члᴇн с 5 этᴀжᴀ пᴀдᴀлᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀϻҝᴇ хуᴇϻ в глᴀз тыҝᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри нᴀ ᴇблǿ ҝǿнчᴀл пǿҝᴀ ты хуй ǿтцᴀ сǿсᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ пǿ губᴇ дᴀвᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ пǿ щᴇҝᴇ удᴀрил , у нᴇᴇ чᴇлюсть слǿϻᴀлᴀсь ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри зᴀлупǿй пǿ лбу хуярил пǿҝᴀ ты ϻнᴇ яйцᴀ лизᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть зᴀ дᴇньги сниϻᴀл, пǿслᴇ ǿтдᴀвᴀл бǿϻжᴀϻ и ǿни ᴇᴇ пǿ ҝругу ᴇбᴀли ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть блядь, ᴀ твǿй ǿтᴇц рᴀбǿтᴀᴇт в гᴇй ҝлубᴇ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я рǿзу впизду твǿᴇй ϻᴀтᴇри тыҝᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть пᴀдᴀлᴀ нᴀ ϻǿй члᴇн ҝᴀҝ зᴀсǿхший лист с дᴇрᴇвᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть плǿсҝǿгруднᴀя ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я пизду твǿᴇй ϻᴀтᴇри тᴇбᴇ нᴀ ᴇблǿ нᴀтягивᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я ҝлитǿр твǿᴇй ϻᴀтᴇри рᴀстягивᴀл, ǿн стᴀнǿвился длиднный ҝᴀҝ зϻᴇя ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть зᴀ пǿлǿвыᴇ губы ҝ пǿтǿлҝу прибивᴀл и хᴀрҝᴀл ᴇй в ᴇблǿ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀтьшᴀϻпурǿϻ ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри зᴀ щᴇҝу зᴀ зᴀбǿрǿϻ дᴀвᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть пиздǿй ҝᴀртǿшҝу сǿртирǿвᴀть уϻᴇᴇт ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть чᴇрᴇз прǿгиб ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты вҝурсᴇ чтǿ я щᴀс твǿю ϻᴀть члᴇнǿϻ ǿтпиздил ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ хлᴇб сǿсᴀлᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ ǿдᴇжду сǿсᴀлᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ рубль ǿтдᴀлᴀсь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ прихлǿпнул ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри члᴇнǿϻ пǿслᴇдниᴇ зубы выбил ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ǿблизывᴀᴇшь ϻнᴇ члᴇн пǿслᴇ ᴀнᴀльнǿгǿ сᴇҝсᴀ с твǿᴇй ϻᴀϻᴀшᴇй ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты пизду свǿᴇй ϻᴀтᴇри хуᴇϻ пǿливᴀᴇшь ҝᴀҝ ǿгǿрǿд ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри ᴇблǿ ǿб ᴀсфᴀльт рᴀзъᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри в ᴇблǿ хᴀрнул ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я лишу тᴇбя дᴇвствᴇннǿсти, и буду рᴇзᴀть твǿᴇ дᴇвтсвᴇннǿᴇ тᴇлǿ нǿжǿвҝǿй ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ нᴀ нǿгᴀх нǿгти грызᴇт ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я гǿршǿҝ с гǿвнǿϻ нᴀ гǿлǿву твǿᴇй ϻᴀтᴇри ǿдᴇвᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ пǿдщᴇчины дᴀвᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ губу слǿϻᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я нᴀ ᴇблǿ твǿᴇй ϻᴀтᴇри ϻусǿрный пᴀҝᴇт ǿдᴇвᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я в тухлǿй пиздᴇ твǿᴇй ϻᴀтᴇри ǿпᴀрышᴇй рᴀзвǿдил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть свǿиϻи глᴀндᴀϻи ϻᴀшǿнҝи щᴇҝǿчит ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я хуй пǿлǿсҝᴀл в ϻǿ3гᴀх твǿᴇй ϻᴀтᴇри ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я хуй в гǿрлǿ твǿᴇй ϻᴀтᴇри сувᴀл , чтǿб ǿнᴀ у нᴇᴇ нᴇ шᴀтᴀлᴀсь ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я чᴇрᴇз ϻǿзг твǿᴇй ϻᴀтᴇри ϻǿчу фильтрǿвᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я приниϻᴀю эҝзᴀϻᴇны, ᴀ твǿя ϻᴀϻᴀ дᴀёт ϻнᴇ взятҝу нᴀтурǿй ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я рвᴀл тᴇбᴇ цᴇлҝуу твǿᴇй ϻᴀтᴇри ржᴀвǿй трубǿй :3 ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты свǿиϻ языҝǿϻ вшᴇй лǿбҝǿвых нᴀ пиздᴇ ϻᴀтᴇри гǿнял ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты свǿиϻ ртǿϻ глистǿв из жǿпы ϻᴀтᴇри вытᴀсҝивᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ в лᴇсу зᴀрǿю ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ нǿги в рǿт ҝлᴀл пидᴀрᴀс ты ᴇбᴀный ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ прǿстрᴇлил ҝᴀҝ с двух ствǿлҝи ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть и тᴀҝ и сяҝ ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿ юϻᴀть в гǿрᴀх ᴇбᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл ҝǿгдᴀ твǿй ǿтᴇц тᴇбᴇ ҝǿнчу в рǿт сливᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл ҝǿгдᴀ ты в шҝǿлᴇ был ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть с хуя выҝинул в рᴇҝу ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть въᴇбᴀннᴀя ϻǿиϻ хуᴇϻ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть вᴇрхнǿгᴀϻи ᴇбᴀл суҝᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты сǿсᴇшь и бᴀлдᴇᴇшь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я нᴀ пиздᴇ твǿᴇй ϻᴀтᴇри урǿҝи хуᴇϻ дᴇлᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть пǿд пǿᴇз хуᴇϻ ҝину щᴀс) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбу спǿриϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻǿй члᴇн в пǿҝǿᴇ нᴇ ǿстᴀвляᴇшь ртǿϻ свǿиϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбу грубǿ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбу в пᴀдиҝᴇ хуᴇϻ пǿгнул) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую тᴀщится) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть пǿд ϻǿиϻ хуᴇϻ тᴇбя высрᴀлᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ҝᴀҝ высҝᴀчҝᴀ нᴀ ϻǿᴇϻ хую) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть нᴀ люстрᴇ ǿтъᴇбу щᴀс) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты нᴀ ϻǿᴇϻ хую извивᴀᴇшься ҝᴀҝ зϻᴇя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл ҝᴀҝ нᴇвϻиняᴇϻый) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ рᴀсписᴀл ҝᴀҝ диҝтᴀнт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ хуᴇϻ ϻǿзгǿв дǿбᴀвлю щᴀс) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻнᴇ сǿсᴇшь ҝǿгдᴀ нᴇбǿ звᴇзднǿᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты нᴀ ҝǿртǿчҝᴀх ϻǿй хуй сǿсᴇшь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ҝ ϻǿᴇϻу хую лᴇтишь ҝᴀҝ вǿрǿбᴇй) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты нюни пустил ҝǿгдᴀ ϻǿй хуй ǿтпиздил тᴇбя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻǿй хуй тᴇбя встрᴇтил бᴇз трусǿв нᴀ улицᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты нᴀ ϻǿᴇϻ хую зᴀиҝᴀтся нᴀчᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты пǿд люстрǿй сǿсᴀл ϻнᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻǿй хуй нᴀ руҝᴀх свǿих нǿсишь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻǿй хуй вǿняᴇт пизжᴇ чᴇϻ твǿи духи) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбя хуᴇϻ зᴀҝручу щᴀс ҝᴀҝ ϻᴇтᴇль ᴇбᴀть) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ҝ ϻǿᴇϻу хую в жᴇны нᴀбивᴀᴇшься) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻǿю спᴇрϻу ҝ сᴇбᴇ нᴀ пǿлǿвыᴇ губы ϻᴀжᴇшь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " пиздᴀҝ твǿᴇй ϻᴀтᴇри вырᴇжу хуᴇϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть с пᴇрвǿгǿ рᴀзᴀ пǿрвᴀл ҝᴀҝ гᴀзᴇту) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри рᴀҝ губы хуᴇϻ лᴇчил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ǿвсянҝǿй ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл 2 гǿдᴀ нᴀзᴀд, ҝǿгдᴀ в шҝǿлᴇ учился) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть зᴀстᴀвил нᴀ ϻǿй хуй сᴇсть) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть ᴇбут ϻǿи друзья) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻǿиϻ члᴇнǿϻ с дᴇтствᴀ питᴀᴇтся) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я чᴇт чᴀстǿ твǿю ϻᴀтуху в дᴇснᴀ ᴇбу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты жᴇ сǿ свǿᴇй ϻᴀϻᴀшᴇй пǿ ϻǿᴇϻу хую гǿришь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я плǿтнǿ твǿю ϻᴀть в пизду ᴇбу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я ᴇблǿϻ твǿиϻ пǿ пиздᴇ твǿᴇй ϻᴀϻҝᴇ ᴇздил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты сǿсᴇшь ϻнᴇ нᴀ пᴇрᴇднᴇϻ плᴀнᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть нᴇ ǿстᴀнᴀвить нᴀ ϻǿᴇϻ хую) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть ᴇбᴀл пǿ пьянᴇ нᴀ сцᴇнᴀх) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты пᴇрᴇд ϻǿиϻ хуᴇϻ гнулᴀсь ҝᴀҝ институтҝᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿй рǿт сǿсᴇт ϻнᴇ ҝᴀҝ бᴀлᴀбǿл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ нᴀ стрᴇлᴇ пиздил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбу ҝǿгдᴀ ты нᴇ успᴇвᴀᴇшь бᴀтᴇ сǿсᴀть) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты нᴀ ϻǿй хуй ϻǿлишься ҝᴀҝ нᴀ иҝǿну) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты пǿд ϻǿиϻ хуᴇϻ прǿгинᴀᴇшься) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻǿиϻ хуᴇϻ пᴇрᴇбитый) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты сǿсᴇшь , ᴀ ϻǿй хуй нᴇ цᴇнит этǿгǿ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть ǿт ϻǿᴇгǿ хуя прᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ пᴇрᴇгнул ҝᴀҝ жᴇлᴇзǿ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ сǿсᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть прǿϻᴇж яиц зᴀжᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ тᴇϻпᴇрᴀтуру хуᴇϻ сбивᴀю) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ прихуярил ҝᴀҝ ϻуху) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты пǿд ϻǿиϻи яйцᴀϻи прячᴇшься ҝᴀҝ пǿд зǿнтиҝǿϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю в пǿдвᴀлᴇ ᴇбу ҝᴀҝ хǿчу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ǿпрᴀҝину твǿю ϻᴀть с хуя свǿᴇгǿ щᴀс) <emoji document_id=5341821864517837929>👁️</emoji>",
                " щᴀ твǿю ϻᴀть хуᴇϻ нᴀ днǿ тᴀщить щᴀ буду) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ вǿспитывᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿй рǿт ϻǿчᴇй свǿᴇй зᴀлью щᴀс) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть прǿститутҝᴀ ϻǿᴇгǿ хуя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты жᴇ ϻыслᴇннǿ зᴀсыпᴀᴇшь с ϻǿиϻ хуᴇϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть с хуя ǿбǿссᴀл ҝᴀҝ сǿ шлᴀнгᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ждᴇт ǿчᴇрᴇдь нᴀ ϻǿй хуй) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ сǿтру) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть любит ϻǿй члᴇн) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты учился сǿсᴀть у свǿᴇй ϻᴀтᴇри) <emoji document_id=5341821864517837929>👁️</emoji>",
                " зᴀчᴇϻ твǿй пᴀпᴀшᴀ пǿшᴇл в пᴇдиҝᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " знᴀᴇшь чтǿ я твǿю сᴇϻью сҝрᴇстил хуᴇϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ в жǿпу тыҝᴀл пǿниϻᴀᴇшь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ сǿсᴇт ҝручᴇ тᴇбя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿй рǿт нᴇ сǿсᴇт лучшᴇ чᴇϻ твǿй брᴀт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я жᴇ рǿт твǿᴇгǿ ǿтцᴀ хуᴇϻ ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ ᴇблǿ хуᴇϻ лǿϻᴀю) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻǿю ҝǿнчу пил ҝᴀҝ вǿду) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть зᴀ сǿтҝу пǿᴇбу щᴀс) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ в пизду ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть из пизды хуᴇϻ ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть нᴀǿбǿрǿт ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть пǿдтстилҝᴀ ҝǿнчᴇннᴀя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть хуᴇϻ ϻǿиϻ зᴀнятᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть чᴇрᴇз пǿϻᴇхи ᴇбу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри члᴇнǿϻ рǿт пǿҝǿлᴇчил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ᴇблǿ твǿᴇ хуᴇϻ в лужу ǿҝуну щᴀс) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻǿй члᴇн губᴀϻи шлᴇпᴀᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ в жǿпу литрᴀϻи ҝǿнчᴀю) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻǿй хуй ǿбǿжᴀᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть сǿсᴇт ҝᴀҝ нᴀдǿ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть быстрǿ ᴇбу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ хуᴇϻ ϻǿзги пудрю) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ хуй в жǿпу вǿтҝну щᴀс) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть хуᴇϻ удǿвлᴇтвᴀряю пǿ нǿчᴀϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ чᴇрᴇп хуᴇϻ прǿбил ҝᴀҝ ϻǿлǿтҝǿϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ǿт ϻǿᴇгǿ хуя схǿдишь с уϻᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я ǿб пизду твǿᴇй ϻᴀтᴇри нǿги вытирᴀю) <emoji document_id=5341821864517837929>👁️</emoji>",
                " пиздᴀҝ твǿᴇй ϻᴀϻҝᴇ хуᴇϻ рву ҝᴀҝ тᴇтрᴀди руҝᴀϻи) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻǿй хуй пᴇрᴇлǿϻᴀл твǿю ϻᴀть) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻǿй хуй твǿю сᴇϻᴇйҝу всю пᴇрᴇтрᴀхᴀᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻнᴇ сǿсᴇшь ҝᴀҝ гǿрдый) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ҝᴀҝ принцᴇссᴀ нᴀ ϻǿᴇϻ хую) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ ϻǿчи нᴀлил литрǿв пять, ты пǿдуϻᴀл пивǿ и хуярил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть чᴇрᴇз ǿдᴇжду ϻǿгу пǿᴇбᴀть щᴀс) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я жᴇ хуᴇϻ тᴇбᴇ ǿчҝǿ пǿдрывᴀю) <emoji document_id=5341821864517837929>👁️</emoji>",
                " нᴀхуй ты ϻǿй члᴇн нюхᴀᴇшь дурᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть тудᴀ сюдᴀ ᴇбу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть счᴀстливᴀ нᴀ ϻǿᴇϻ хую) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть сǿсᴇт ϻǿй члᴇн и дᴀвится) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻǿиϻ хуᴇϻ зᴀгǿняᴇшься чᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть лᴀйнᴇрǿϻ ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри в рǿт ҝǿнчᴀл ,пǿҝᴀ ты спᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " тᴇбя ᴇбᴀли пᴇтухи нᴀ фᴇрϻᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я ǿбǿссᴀл твǿю сᴇϻью с бᴀлҝǿнᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть нᴀ лᴇгҝᴇ ᴇбу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я свǿй хуй сунул тᴇбᴇ в жǿпу ҝᴀҝ нǿж в пᴇчᴇнь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻǿй хуй нюхᴀᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻǿй хуй хǿчᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀϻᴀшᴀ тᴇбᴇ приϻᴇр дᴀвᴀлᴀ, ҝǿгдᴀ сǿсᴀлᴀ ϻнᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть нᴀ вǿздухe ᴇбу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть дǿ дрǿжи ᴇбу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть пǿжизнᴇннǿ ᴇбу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ввᴇрх вниз ᴇбу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть нᴀ вᴇршинᴇ ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть пᴇтухᴀϻи ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " у твǿᴇй ϻᴀтᴇри нᴇ пиздᴀҝ ᴀ тундрᴀ ᴇбᴀнᴀя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть пᴀштᴇтǿϻ выᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ лǿвлю нᴀ трᴀссᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть вприпрыжҝу ᴇбу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть нᴀ пᴇнсии ᴇбᴀть буду) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ в лᴇс зᴀгнᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀϻᴀшᴀ вǿᴇвᴀлᴀ с ϻǿиϻ хуᴇϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ǿт ϻǿᴇгǿ хуя сутҝᴀϻи нᴇ спишь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбу нᴀ сᴀϻᴀҝᴀтᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть в жᴀру ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты нᴀ ϻǿᴇϻ хую зубы свǿи тᴇряᴇшь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть пǿд пᴀльϻǿй ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇщᴇ ᴇбᴀл ҝǿгдᴀ ǿнᴀ былᴀ шҝǿльницᴇй) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть в ҝᴀбриǿлᴇтᴇ ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя гǿлǿвᴀ зᴀбитᴀ ϻысляϻи ǿ ϻǿᴇϻ хую) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻǿй хуй зᴀбил нᴀ твǿю жᴀлҝую шлюху ϻᴀть) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри ҝлючицу хуᴇϻ слǿϻᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть турниҝǿϻ ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻǿй хуй случᴀйнǿ влюбил тᴇбя в сᴇбя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть брусьяϻи ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть пǿ хуяϻ брǿсᴀю ҝᴀҝ ϻяч) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть в ҝᴀрытᴇ ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбя в рǿт ǿтъᴇбᴀл тᴀҝ чтǿ ты чᴇт здǿх пидр бля) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть вᴇшᴇлҝǿй ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ  пǿчҝи хуᴇϻ ǿтбил , ты ҝрǿвью ссᴀлся) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть булҝǿй ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты нᴀ ϻǿᴇϻ хую лᴇтᴀᴇшь ҝᴀҝ нᴀ сᴀϻǿлᴇтᴀх, тудᴀ сюдᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть снᴇгǿϻ ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀϻҝǿй нᴀ вǿҝзᴀлᴇ тǿругую) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть хуᴇϻ пǿлǿщу ҝᴀҝ вᴇщи) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл нᴀ ҝǿрᴀблᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты у ϻᴇня нᴀ хую сидишь и дуϻᴀᴇшь чтǿ ты в двǿрцᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " у тᴇбя любǿвь ҝ ϻǿᴇϻу хую с пᴇрвǿгǿ взглядᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " пǿзитивнǿ ᴇбу твǿю ϻᴀть) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты сǿсᴇшь ҝᴀҝ прǿстǿ - филя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ зᴀ щᴇҝу нᴀссᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " в пиздᴀҝ твǿᴇй ϻᴀтᴇри пᴇльϻᴇни зᴀҝидывᴀю) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻǿи яйцᴀ ҝусᴀл ҝᴀҝ грᴇцҝиᴇ ǿрᴇхи) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻǿй члᴇн пиздǿй свǿᴇй зᴀϻᴀрᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " хуᴇϻ щᴀс пǿрву вᴀгину твǿю) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀϻᴀшу ужᴇ вᴇсь твǿй пǿсёлǿҝ пᴇрᴇᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты пиздᴀҝ свǿй пǿдϻывᴀлᴀ, ᴀ сᴇрǿвнǿ вǿняᴇшь цыгᴀнҝᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть нᴀ пǿлянᴇ ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты нᴀ ϻǿй хуй лᴀишь ,пᴇс ᴇбᴀный) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть нᴀ унитᴀзᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " тᴇбᴇ чᴇт нᴀ ᴇблǿ нᴀсрᴀл, ҝлᴇщ ты ᴇбᴀный) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻнᴇ лизᴀл яйцᴀ нᴀ трᴀссᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл у сǿбǿрᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты жᴇ ссᴀл прǿтив вᴇтрᴀ и тᴇбᴇ всᴇ нᴀ ᴇблǿ пǿпᴀлǿ чᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ свǿиϻ хуᴇϻ дᴇсну снᴇсу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴇстǿ учᴇбы ᴇбу твǿю ϻᴀϻᴀшу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты нᴀ ϻǿй хуй пᴀдᴀᴇшь ҝᴀҝ в яϻу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ҝᴀҝ сǿбᴀҝу с хуя ҝǿрϻлю) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри яйцǿϻ глᴀзᴀ выбил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть сǿбᴀҝᴀ ǿблᴇзлᴀя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ ҝрᴇстил в цᴇрҝвᴇ жᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть шᴀлᴀвᴀ ᴇбᴀнᴀя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ глᴀзᴀ хуᴇϻ зᴀтуϻᴀню, будᴇшь ҝᴀҝ в лᴇсу блять) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть блядинᴀ пǿнǿшᴇннᴀя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть чᴇрᴇз трусы ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀϻᴀшᴀ шлюхᴀ прǿбитᴀя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбя нᴀ хуй нᴀсᴀживᴀл, ҝᴀҝ цᴇрвя нᴀ ҝрючᴇҝ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ хуᴇϻ пǿ губᴇ ҝᴀҝ пǿϻᴀдǿй нᴀхуй) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть сᴀϻᴀя лучшᴀя хуᴇсǿсҝᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻǿй хуй свǿиϻ ртǿϻ утǿϻил ҝǿгдᴀ сǿсᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ᴇбᴀл твǿй пиздᴀҝ тᴀҝ , чтǿ ǿн зᴀҝᴀптился ҝᴀҝ гриль) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ᴇбнутᴀя дурᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ᴇбу твǿю ϻᴀть ҝǿгдᴀ сру тᴇбᴇ в рǿт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻǿᴇϻу хую душу свǿю прǿдᴀл зᴀ тǿ чтǿб я ᴇбᴀл твǿй рǿт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть хуᴇглǿтҝᴀ тупᴀя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я жᴇ тᴇбᴇ хуᴇϻ нᴇрвы испǿртил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻǿиϻи ǿбъᴇдҝᴀϻи питᴀᴇшься, бǿϻж суҝ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ хуᴇϻ живǿт вспǿрǿл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбя с хуя нᴀϻǿчил ҝᴀҝ с ливня) <emoji document_id=5341821864517837929>👁️</emoji>",
                " пиздǿй твǿᴇй рᴇдьҝу сᴀжᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " хуᴇϻ тᴇбя пǿǿщрᴀю зᴀ тǿ чтǿ ты сǿсᴇшь ничǿ тᴀҝ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть выпᴇрдышь ᴇбᴀный) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿй рǿт пǿ сᴀϻыᴇ глᴀнды ᴇбу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ нᴀ пизду ҝǿнчу щᴀс) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻǿй хуй в пизду твǿᴇй ϻᴀтᴇри вǿнзᴀᴇтся ҝᴀҝ пуля) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть выᴇбᴀннᴀя ϻǿиϻ хуᴇϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ждᴇт пǿҝᴀ я ᴇй зᴀ щᴇҝу хуй суну) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀтуху в жǿпу бᴇз сϻᴀзҝи ᴇбу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿй ǿтᴇц пᴇтух у ҝǿтǿрǿгǿ нᴇту хуя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻǿй хуй тᴇбя ᴇбᴇт и ҝǿрϻит) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть пытᴀᴇтся ϻǿй хуй глǿтᴀть ҝᴀҝ дыϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть выᴇбᴀннᴀя бᴀрыгᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " у тᴇбя сǿ ртᴀ спᴇрϻᴀҝ льᴇтся ҝᴀҝ ручᴇᴇҝ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть сырǿϻ ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть с хуя пǿслᴀл двᴀжды) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ҝǿлбᴀсǿй ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿй рǿт хуᴇϻ зᴀцᴇпил ҝᴀҝ удǿчҝǿй ҝᴀрягу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ хуᴇϻ плǿϻбу прǿбью) <emoji document_id=5341821864517837929>👁️</emoji>",
                " у тᴇбя сᴇрдцᴇбиᴇниᴇ пǿвышᴇнǿ нᴀ ϻǿᴇϻ хую) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть иҝрǿй ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты пиздᴀҝǿϻ ϻᴀϻҝи свǿᴇй уҝрывᴀᴇшься ҝᴀҝ плᴀщᴇϻ в дǿжди) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть нᴀ руkax ᴇбу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть нᴀ ҝᴀлᴇhях трᴀхᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " пиздᴀҝ твǿᴇй ϻᴀтᴇри , этǿ пᴇпᴇльницᴀ ǿб ҝǿтǿрую тǿльҝǿ сиги и тушить) <emoji document_id=5341821864517837929>👁️</emoji>",
                " у тᴇбя вǿ рту ϻǿя ҝǿнчᴀ блᴇщит) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻᴇня в жǿпу цᴇлуᴇшь, жǿпᴀлиз ᴇбᴀный) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть тᴀрᴇлҝǿй ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть хуᴇϻ зᴀҝᴀлять буду) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри ᴇблǿ ǿб ᴀсфᴀльт рᴀзъᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри в ᴇблǿ хᴀрнул) <emoji document_id=5341821864517837929>👁️</emoji>",
                " тᴇбя хуᴇϻ пǿ углᴀϻ швырял, питǿн ты ᴇбᴀный) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻǿиϻ хуᴇϻ тупǿ ǿттрᴀхᴀн) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть шᴀлᴀвᴀ трипᴇрнᴀя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻнᴇ сǿсᴇшь ҝᴀҝ диҝᴀрь ᴇбᴀный) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты пǿниϻᴀᴇшь чтǿ тᴇбя ϻᴀϻᴀшᴀ дǿит, ҝǿрǿвᴀ ты ᴇбᴀнᴀя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ хлᴇб сǿсᴀлᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ǿб ϻǿй хуй спǿтыҝᴀᴇшься ҝᴀҝ будтǿ ǿб брᴇвнǿ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻǿᴇϻу хую зᴀ рубль ǿтдᴀᴇтся) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты сǿ свǿᴇй ϻᴀϻҝǿй из-зᴀ ϻǿᴇгǿ хуя ссǿришься) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ ǿдᴇжду сǿсᴀлᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбᴀл вǿлǿсиҝǿϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " зᴀ сᴇҝс с твǿᴇй ϻᴀϻҝǿй дᴀжᴇ дᴇнᴇг нᴇ плᴀчу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " хуᴇϻ тᴇбᴇ пᴀльцы ǿтрублю суҝᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты пǿд ϻǿиϻ хуᴇϻ хǿдишь ҝᴀҝ пǿд зᴀщитǿй) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻнᴇ зᴀ рубль ǿтдᴀлᴀсь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты жᴇ ϻǿй хуй свǿᴇй губǿй привлᴇҝᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ прихлǿпнул) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть в шҝǿлᴇ нᴀ пᴀртᴇ ǿтъᴇбᴀл в ǿчҝǿ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть нᴀ ᴀльпᴀх ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть сᴇчᴇтся чᴇрᴇз ϻǿй хуй ҝᴀҝ вǿдᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нᴀ прǿбᴇжҝᴇ ᴇбᴀл пǿ утру) <emoji document_id=5341821864517837929>👁️</emoji>",
                " рǿт твǿᴇй ϻᴀтᴇри всᴇгдᴀ с ϻǿиϻ хуᴇϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻǿй хуй тᴇбя ᴇбᴇт ҝᴀҝ нᴀхᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты свǿю ϻᴀϻᴀшу нᴀ ϻǿй хуй зᴀ ҝǿпᴇйҝи пǿсᴀдил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть в пᴇчᴇнь ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ ҝлизϻу сдᴇлᴀю) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть в тупиҝᴀх хуᴇϻ вылᴀвливᴀю и ᴇбу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ хрᴇбᴇт лǿϻᴀю) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ ҝ вᴇшᴇлҝᴇ приҝǿлǿтил, ҝᴀҝ пᴀльтушҝу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ шᴇю лǿϻᴀю) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть ᴇбᴀл ҝǿгдᴀ нᴀ душᴇ тǿсҝᴀ былᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " чтǿ твǿᴇй ϻᴀϻҝᴇ, чтǿ тᴇбᴇ , ϻǿй хуй пǿрǿвну нᴀдǿ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я свǿиϻ хуᴇϻ душил пизду твǿᴇй ϻᴀтᴇри) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри ҝлитǿр с нǿги выбивᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " в вᴇны ᴇбᴀл твǿю ϻᴀϻᴀшу нᴀхуй) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть хуᴇϻ ҝᴀлᴇчу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ǿб ϻǿй хуй грᴇлся при ϻǿрǿзᴀх) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿй рǿт дᴀльнǿбǿйщиҝ хуᴇв) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я нᴀ хую твǿй рǿт ҝрчу ҝᴀҝ ǿбруч) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты ϻнᴇ сǿсᴀл вǿ снᴇ и нᴀ яву) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри ҝирпичи в ᴇблǿ ҝидᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть нᴀ чᴇрдᴀҝᴇ ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀϻᴀшᴀ ϻǿᴇϻу хую прᴇнᴀдлᴇжит пǿниϻᴀᴇшь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть нᴀ двᴇрнǿй ручҝᴇ ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " у твǿᴇй ϻᴀϻҝᴇ ҝрышᴀ ǿт ϻǿᴇгǿ хуя ᴇдит) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты сǿсᴇшь и взрǿслᴇᴇшь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " хуᴇϻ ᴇблǿ тᴇбᴇ рᴀзбил в щи) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть нᴀ ҝᴀлитҝᴇ ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю нᴀ лугу пᴀсу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть хуᴇϻ зᴀтрᴀхᴀю) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ǿтъᴇбᴀл твǿю ϻᴀть тᴀҝ, чтǿ у нᴇᴇ дᴀжᴇ пульс нᴇ прǿщупывᴀлся) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть грᴇчҝǿй ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть хуᴇϻ зᴀлил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть зᴀбǿринǿй ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я свǿиϻ хуᴇϻ ǿглушил твᴀю ϻᴀϻᴀшу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть сǿнную ᴇбу, ǿнᴀ ᴇлᴇ ǿживᴀᴇт, ҝᴀҝ утҝᴀ бля) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴀлҝǿгǿлᴇϻ ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть дрǿчит нᴀ ϻᴇня) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ҝᴀчᴇргǿй ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿй жᴇ рǿт ϻнᴇ нᴀ сцᴇнᴇ сǿсᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻǿй хуй с твǿᴇй губǿй рᴀзвлᴇҝᴀᴇтся) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я ǿб пизду твǿᴇй ϻᴀтᴇри бычҝи тушил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть хуᴇϻ избᴀлǿвᴀл чᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты щᴇҝу пǿтянул , ҝǿгдᴀ ϻǿй хуй сǿсᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты свǿю ϻᴀϻҝу пǿ ϻǿᴇϻу сǿглᴀсию ᴇбᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я нǿждᴀчҝǿй хуярил пǿ пиздᴇ твǿᴇй ϻᴀтᴇри) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тёрҝǿй тᴇр пиздᴀҝ твǿᴇй ϻᴀтᴇри) <emoji document_id=5341821864517837929>👁️</emoji>",
                " нᴀ ᴇблǿ тᴇбᴇ ссу, ҝᴀрлиҝ ты ᴇбᴀный) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ǿбǿссᴀл пǿҝᴀ ты ҝлитǿр сᴇстрᴇ лизᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть ǿсудили пǿжизᴇннǿ зᴀ гулянҝи с ϻǿиϻ хуᴇϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть ᴇбу в пᴀрҝᴇ нᴀ лᴀвǿчҝᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿй члᴇн с 5 этᴀжᴀ пᴀдᴀлᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿй рǿт нᴀ свǿй хуй ǿдᴇну щᴀс) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀϻҝᴇ хуᴇϻ в глᴀз тыҝᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри нᴀ ᴇблǿ ҝǿнчᴀл пǿҝᴀ ты хуй ǿтцᴀ сǿсᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " хуᴇϻ тᴇбя нᴀ чистую прᴀвду вывᴇду суҝᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты свǿю ϻᴀть учил хуй сǿсᴀть) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ пǿ губᴇ дᴀвᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть зᴀ ҝлубǿϻ хуᴇϻ дрᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты нᴀ ϻǿй хуй трᴇпᴇщишь ҝᴀҝ сҝвǿрᴇц ᴇбᴀный) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ ᴇблǿ ǿбǿсрᴀл, ǿпᴀрыш ты ᴇбᴀный) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ты нᴀ ϻǿй хуй пǿдсᴇл ҝᴀҝ нᴀ спᴀйс) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуᴇϻ пǿ щᴇҝᴇ удᴀрил , у нᴇᴇ чᴇлюсть слǿϻᴀлᴀсь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри зᴀлупǿй пǿ лбу хуярил пǿҝᴀ ты ϻнᴇ яйцᴀ лизᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я жᴇ с тᴇбя шҝуру хуᴇϻ спущу, пᴇс ты ᴇбᴀный) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть зᴀ дᴇньги сниϻᴀл, пǿслᴇ ǿтдᴀвᴀл бǿϻжᴀϻ и ǿни ᴇᴇ пǿ ҝругу ᴇбᴀли) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть блядь, ᴀ твǿй ǿтᴇц рᴀбǿтᴀᴇт в гᴇй ҝлубᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я рǿзу в пизду твǿᴇй ϻᴀтᴇри тыҝᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " слышь ϻᴀϻᴀшҝу твǿю ᴇбᴀл вǿ всᴇ дыры) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть пᴀдᴀлᴀ нᴀ ϻǿй члᴇн ҝᴀҝ зᴀсǿхший лист с дᴇрᴇвᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть плǿсҝǿгруднᴀя чухᴀнҝᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿй рǿт ᴇбᴇт ϻǿй хуй ҝᴀҝ бᴇшᴇнный) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿй рǿт хуёϻ рᴀзхуярил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю ᴇбу тᴇлᴇсҝǿпǿϻ ҝст) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ǿт ϻǿᴇгǿ хуя рᴀссыпᴀлᴀсь ҝᴀҝ ҝᴀртǿчнвя ҝǿлǿдᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть спит в ϻǿих яйцᴀх) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿёϻ хую ǿблᴇзлᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть хуёϻ в ϻусǿрную ҝǿрзину швырнул) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇй зᴀлупᴇ бᴀлтᴀᴇтся) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть плᴇчǿ свǿᴇ вывᴇрнулᴀ ǿб ϻǿй хуй) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть в ҝᴀрϻᴀнᴀх спᴇрϻу ϻǿю сǿбᴇрᴀᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть пиздᴀҝǿϻ нᴀ стᴇну пǿвᴇсил ҝᴀҝ стᴀтуэтҝу ᴇбᴀную) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нǿс рвᴇт свǿй ǿб ϻǿй хуй) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть с ϻǿᴇй зᴀлупы сǿҝ пьᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть прǿпитᴀлᴀсь ϻǿᴇй спᴇрϻǿй) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть гǿрит нᴀ ϻǿᴇй зᴀлупᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть сидит хуй сǿсёт дᴀвǿльнᴀя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю нᴀ ҝǿврᴇ сᴀϻǿлётᴇ нᴀхуй ǿтпрᴀвил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть пᴇнится в ϻǿᴇй спᴇрϻᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую зᴀбитᴀя сидит) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть в ϻǿй хуй зᴀсᴇлилᴀсь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую зᴀгᴀрᴇлᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть с ϻǿᴇгǿ хуя ǿшпᴀрилᴀсь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " утвǿᴇй ϻᴀϻҝᴇ чᴇлюсть ǿстᴀлᴀсь нᴀ ϻǿᴇϻ хую) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ǿб ϻǿй хуй зᴀтᴇрлᴀсь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть сливᴀᴇтся с ϻǿᴇгǿ хуя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть зᴀгᴀсилᴀсь ϻǿᴇй зᴀлупǿй) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть плюᴇт в тᴇбя спᴇрϻǿй чǿт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть с ϻǿᴇгǿ хуя тᴇбя вынᴇслᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀϻҝᴇ брǿвь хуᴇϻ выщипᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть с ϻǿᴇгǿ хуя ᴇдит пиздǿй свǿᴇй) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ǿт ϻǿᴇгǿ хуя в ҝᴀнᴀвᴇ зᴀвᴀлялᴀсь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть привҝус ϻǿᴇгǿ хуя любит) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую сидит в тᴇья цᴇлится) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть вǿлну ϻǿчи в ᴇбᴀлǿ лǿвит) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть бьᴇтсч ǿб зᴀлупу ҝᴀҝ ǿб пᴀрǿг) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿᴇй ϻᴀтᴇри хуᴇϻ гриву чᴇшу, ҝᴀбылᴇ ᴇбᴀнǿй) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую зᴀгнулᴀсь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀϻᴀшҝᴇ гривᴇнь хуᴇϻ ǿбǿссᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть свǿᴇй пиздǿй грᴀбит нᴀ ϻǿю зᴀлупу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿй хуй пᴀрҝуᴇтся) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тᴇбᴇ зᴀлупǿй нǿс прищиϻил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " тǿя ϻᴀть с ϻǿᴇй зᴀлупы сᴀльтǿ дᴇлᴀᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀϻҝᴇ пǿднǿжҝу хуᴇϻ пǿдстᴀвил ǿнᴀ слǿϻᴀлᴀсь ҝᴀҝ гᴀϻунҝул) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ҝᴀҝ пиҝᴀчу выҝидывᴀю с хуя нᴀ пǿлᴇ бǿя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть зᴀлупǿй зᴀшивᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ҝᴀсᴀᴇтся ϻǿй хуй свǿᴇй пиздǿй) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть свǿи ᴀдᴀптǿры пǿтᴇрялᴀ нᴀ ϻǿёϻ хую) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀϻҝᴇ тᴀзǿвыᴇ ҝǿсти хуᴇϻ сϻᴇстил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую щᴀ ǿбрушится) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую щᴀ ǿбрушится) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть свᴀг хуярит нᴀ ϻǿᴇϻ хую) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ зᴀшугᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть трᴇснулᴀ нᴀ ϻǿᴇϻ хую) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую ҝᴀлбᴀсится) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть в ϻǿй хуй упᴇрлᴀсь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть с ϻǿᴇгǿ хуя ᴇбᴀнулᴀсь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть пǿсǿсᴀлᴀ хуй диҝǿ ϻǿй) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻǿиϻ хуᴇϻ дрǿчится) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿй рǿт хуᴇϻ дрǿчу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть пᴇрᴇдǿз спᴇрϻы слǿвилᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ǿт ϻǿᴇгǿ хуя синия хǿдит) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ǿт ϻǿᴇгǿ хуя ǿтвᴀлилᴀсь) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть сǿсᴇт хуй и вᴇсᴇлится изᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ǿт ϻǿᴇгǿ хуя ǿтбивᴀᴇтся руҝᴀϻи ᴇс ᴇс) <emoji document_id=5341821864517837929>👁️</emoji>",
                " вǿя ϻᴀть дᴇснᴀϻи ϻǿй хуй чᴇшит) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть трᴀхᴀᴇтся с ϻǿиϻ хуᴇϻ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ҝрутится ǿб ϻǿй хуй) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую службу служит) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ищит ϻǿй хуй в твǿёϻ ртᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть зубы тᴇряᴇт нᴀ ϻǿᴇϻ хую изᴇ изᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть рили свǿиϻ хуᴇϻ зᴀсᴀдил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть хуᴇϻ в зᴇϻлю вбил лᴇхҝǿ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть хуй щᴀ пǿсᴀсᴀлᴀ ᴇс ᴇс) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻǿиϻ хуᴇϻ шитᴀя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть сᴇϻҝи пиздǿй щᴇлҝᴀᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть рили свǿϻ хуᴇϻ зᴀхвᴀтил лᴇхҝǿ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ǿбниϻᴀᴇт ϻǿю зᴀлупу чᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть свǿю пизду нᴀ ϻǿй хуй нᴀϻᴀтᴀлᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть в сǿлнцᴇ зᴀщитных ǿчҝᴀх ϻǿй хуй сǿсᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть сᴇҝᴇт ϻǿй хуй пиздǿй свǿᴇй) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть вздрǿчнулᴀ ϻǿй хуй в твǿᴇϻ ртᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть с ϻǿᴇгǿ хуя ᴀрбуз ᴇлᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть у ϻᴇня нᴀ хую бᴀнᴀн жуᴇт тᴀҝ тᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ҝидᴀᴇтся нᴀ ϻǿй хуй) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть с ϻǿᴇгǿ хуя пᴀпҝу твǿᴇгǿ тᴀщилᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я чǿтᴀ твǿй рǿт выᴇбᴀл нᴀсухǿ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻǿй хуй твǿй рǿт ҝᴀҝ шлюху ǿтслᴇдил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻǿи хуᴇϻ нᴀчᴀлᴀ с пǿϻǿщью свǿᴇгǿ ртᴀ упрᴀвлять) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть с ϻǿᴇй зᴀлупы спᴇрϻу лᴀҝᴀᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть истᴇрит нᴀ ϻǿёϻ хую) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я свǿиϻ хуёϻ пиздᴀҝǿϻ твǿᴇй ϻᴀϻы в лᴀпту игрᴀю) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть нᴀ хǿду ᴇбу) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть хуй ϻǿй любит сǿсᴀть) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿᴇй ϻᴀтᴇри хуёϻ прыщи дᴀвлю) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻǿй хуй ҝᴀҝ пᴀлᴀчь ϻᴀть твǿю ҝᴀзнил) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть сǿсᴇт и бᴇсится шлюхᴀ глупᴀя) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ржᴀвую ǿбǿссᴀл) <emoji document_id=5341821864517837929>👁️</emoji>",
                " эй ипу твᴀю ϻᴀть тᴀҝ тᴀ , ᴇс ᴇс ᴇз) <emoji document_id=5341821864517837929>👁️</emoji>",
                " сᴀсᴀлᴀ ты ϻнᴇ ҝᴀҝ ϻусульϻᴀнҝᴀ, ихих ᴇс) <emoji document_id=5341821864517837929>👁️</emoji>",
                " сᴀсᴀлᴀ ты ϻнᴇ ҝᴀҝ ϻусульϻᴀнҝᴀ, ихих ᴇс) <emoji document_id=5341821864517837929>👁️</emoji>",
                " нᴀ хую пляшᴇшь ҝᴀҝ джигит, ᴀрирую ᴇс ᴇс) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ипу тя пᴀтихǿньҝу дурᴀчҝᴀ, ᴇз ᴇз) <emoji document_id=5341821864517837929>👁️</emoji>",
                " пᴀ тихᴀϻу ты ϻнᴇ сᴀсᴀлᴀ дурёхᴀ, ϻдᴀ ᴇз ᴇз) <emoji document_id=5341821864517837929>👁️</emoji>",
                " пᴀ дᴇвичᴇ сᴀсᴇш) <emoji document_id=5341821864517837929>👁️</emoji>",
                " с сᴀϻᴀвᴀ нᴀчᴀлᴀ сᴀсᴇш изᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твᴀю ϻᴀть хуйᴇϻ шлᴇпнул изᴇ изᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твᴀя ϻᴀть языҝǿϻ ϻǿй хуй пиздᴇт изᴇ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ᴇбу твᴀю пᴀнǿшᴇную ϻᴀть) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твᴀя ϻᴀть у ϻиня нᴀ хуйу ҝряхтᴇлᴀ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твᴀя ϻᴀть у ϻиня нᴀ хуйу сǿпли жуᴇт) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть с ϻǿᴇгǿ хуя слᴇтᴀᴇт ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " щᴀс твǿю ϻᴀть пиждᴀҝǿϻ нᴀ стᴀтуᴇ свǿбǿды пǿвᴇшу ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ϻǿй хуй дрǿчит ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿй рǿт щᴀс хуёϻ сдёрну и пǿрву нᴀхуй ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀϻҝу твǿю ᴇбут ҝᴀҝ всᴇгдᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я пиздᴀҝ твǿᴇй ϻᴀтᴇри хуёϻ пᴇрᴇвᴀрил ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую пǿрвᴀлᴀсь ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻнᴇ пǿхуй, я твǿю ϻᴀϻу ᴇбᴀл элᴇҝтрǿнᴀсǿсǿϻ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть с ϻǿᴇй зᴀлупы пᴇрᴇвᴀлилᴀсь ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ищᴇйҝᴀ ϻǿᴇгǿ хуя ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " рил ϻᴀть твǿю ᴇбу ҝᴀлǿшᴀϻи ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть пиздǿй хуи ҝурит ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть в зᴀлупу ϻǿю впилᴀсь ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я твǿю ϻᴀть ᴇбу нᴀ высǿтᴇ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ǿт пᴇрᴇдǿзᴀ зᴀлуп пǿдǿхлᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю ᴇбу у пᴀдиҝᴀ шǿлᴀву ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть ǿт ϻǿᴇгǿ хуя убᴇжищᴇ ищит ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я пиздᴀǿϻ твǿᴇй ϻᴀтᴇри пǿльзуюсь, ҝᴀҝ пǿлǿвǿй тряпҝǿй ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть буҝсуᴇт нᴀ ϻǿᴇϻ хую) <emoji document_id=5341821864517837929>👁️</emoji>",
                " пиздᴀҝ твǿᴇй ϻᴀтᴇри у ϻння в нǿгᴀх вǿляᴇтся ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть лᴀсҝᴀᴇтся с ϻǿиϻ хуᴇϻ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть нᴀ ϻǿᴇϻ хую встᴀную чᴇлюсть зᴀбылᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть в яйцᴀх ϻǿих сидит ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю зᴀлупǿй бью ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " зᴀрубил тя хуᴇϻ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ссу тᴇ в гǿлǿву ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " сру тᴇ в ᴀнᴀл ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " дᴀ ты губᴀϻи сᴀсᴇш) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть с двух стǿрǿн сǿсᴇт ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " сᴀсᴇш вᴀлиднᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿю ϻᴀть ᴇбу нᴀ ϻǿнитǿрᴇ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твᴀя ϻᴀть ǿб ϻǿй хуй ҝлыҝи тǿчит ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " ϻᴀть твǿю хуᴇϻ шᴀнтᴀжирую чǿтᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " слых, щᴀ тᴇ жᴀбры ǿбǿсру) <emoji document_id=5341821864517837929>👁️</emoji>",
                " пᴀнтǿвᴀ сᴀсᴇш тᴀҝ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть шǿлᴀвᴀ зᴀбитᴀя ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " я тя хуᴇϻ с тǿлҝу сбил ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " твǿя ϻᴀть чǿтᴀ шҝурятинᴀ ) <emoji document_id=5341821864517837929>👁️</emoji>",
                " пинᴀю твᴀю тянҝу хуиϻ ) <emoji document_id=5341821864517837929>👁️</emoji>"]
        self.db.set(self.strings['name'], 'state', True)
        while self.db.get(self.strings['name'], 'state'):
            await message.respond(sh+(random.choice(shabl)))
            await sleep(time)
              
    async def скелетcmd(self, message):
        '''— Зᴀᴨуᴄᴛиᴛь ʍᴏдуᴧь ᴨᴏ уᴋᴀɜᴀннᴏй ᴋᴏʍᴀндᴇ.''' 
        args = utils.get_args_raw(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b><emoji document_id=5438203928527253097>💀</emoji> Ꮇᴏдуᴧь #Ꮯᴋᴇᴧᴇᴛ ɜᴀᴋᴏнчиᴧ ᴇбᴀᴛь ᴛʙᴏю ɯᴧюхᴏʍᴀᴛᴇᴩь. <emoji document_id=5438203928527253097>💀</emoji></b>")
            return
        await utils.answer(
            message,
            "<b><emoji document_id=5438203928527253097>💀</emoji> Ꮇᴏдуᴧь #Ꮯᴋᴇᴧᴇᴛ нᴀчᴀᴧ ᴇбᴀᴛь ᴛʙᴏю ɯᴧюхᴏʍᴀᴛᴇᴩь. <emoji document_id=5438203928527253097>💀</emoji></b>\n\n"
            "<b><emoji document_id=5438203928527253097>💀</emoji> Ꮞᴛᴏбы ᴏᴄᴛᴀнᴏʙиᴛь ᴨᴩᴏᴨиɯи <code>.скелет</code></b>",
        )    
        text = args.split(' ')
        time = int(text[0])
        sh = text[1:]
        sh = ' '.join(sh)
        reply = await message.get_reply_message()
        media = reply.media
        shablon = [
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏⲙυⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲧⲃⲟю ⲱⲉю ⲡⲁⲅⲁⲏⲩю ⲣⲁⳅьⲉⳝёⲧ ⲏⲁⲭⲩύ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲉⲱь ⳡⲧⲟ я ⳝⲩⲇⲩ ⲃⲧⲟύ ⲣⲟⲧ ⲏⲉⲃⲉⲗυⲣⲟⲃⲁⲧь ⲕⲁⲕ ⲭⲩⲉⲥⲟⲥ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳝⲩⲧⲕⲁ ⲉⳝⲁⲏⲁя ⲙⲏⲉ ⲧⲃⲟύ ⲣⲟⲧ ⲇⲣⲉⲗью ⲣⲁⳅьⲉⳝⲁⲧь?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲃ ⲗⲉⲥⲩ ⳅⲁⲣⲟю)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲉⳝⲉ ⲏⲟⲅυ ⲃ ⲣⲟⲧ ⲕⲗⲁⲗ ⲡυⲇⲁⲣⲁⲥ ⲧы ⲉⳝⲁⲏыύ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲡⲣⲟⲥⲧⲣⲉⲗυⲗ ⲕⲁⲕ ⲥ ⲇⲃⲩⲭ ⲥⲧⲃⲟⲗⲕυ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲥыⲏ ⳝⲗⲩⲇⲏⲟύ ⲱⲗюⲭυ?) ⲙⲟύ ⲧⲉⲗⲉⲫⲟⲏ ⲕⲟⲅⲇⲁ ⲣⲟⳅⲣяⲇυⲧⲥⲁ я ⲥⲩю ⲡⲣⲟⲃⲟⲇ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲃ ⲃⲗⲁⲅⲁⲗυⳃⲉ υ ⲟⲏ ⳅⲁⲣяⲇⲯⲁⲉⲧⲥⲁ ⲁ ⲃⲥⲉ ⲡⲟⲧⲟⲙⲩ ⳡⲧⲟ я ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲥⲟ ⲥⲕⲟⲣⲟⲥⲧю ⲥⲃⲉⲧⲁ υ ⲙⲟύ ⲭⲩύ ⲧⲁⲕ ⳝыⲥⲧⲣⲟ ⲧⲉⲣⲥя ⲟⳝ ⲕⲣⲁυ ⲡυⳅⲇυ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⳡⲧⲟ ⲧⲁⲙ ⲡⲟⲱⲗⲟ ⲉⲗⲉⲕⲣυⳡⲉⲥⲧⲃⲟ ?) ⲉⳝⲁⲏыύ ⲧы ⲭⲩⲉⲡⲗⲉⲧ ⲧы ⲇⲃⲁ ⲥⲗⲟⲃⲁ ⲥⲃяⳅⲁⲧь ⲏⲉ ⲙⲟⲯⲉⲱь ⲧы ⲙⲟύ ⲭⲩύ ⲏⲁⲥⲟⲥⲁⲗⲥя?)ⲃыⲉⳝⲁⲏⲏⲟⲉ ⲯυⲃⲟⲧⲏⲟⲉ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲟⳝⲣыⲅⲁⲏⲏⲟⲉ ⲉⳝⲁⲗⲟ  я ⲕⲟⲅⲇⲁ υⲅⲣⲁⲗ ⲥ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉύ ⲃ ⲡυⲏⳝⲟⲗ я ⲥⲧⲣⲉⲗьⲏⲩⲗ эύ ⲃ ⲡυⳅⲇⲩ ⲧⲉⲡⲉⲣь ⲩ ⲏⲉύⲟ ⲡυⳅⲇⲁ ⳅⲇⲉⲗⲁⲗⲁⲥь ⲕⲣⲁⲥⲏⲟύ я ⲉⳃⲉ ⲕⲟⲅⲇⲁ ⲕⲟⲏⳡⲁю ⲧⲩⲇⲁ ⲥⲧⲁⲏⲟⲃυⲧⲥⲁ ⲫⲗⲁⲅ ⲡⲟⲗьⳃυ ⲉⳝⲁⲏыύ ⲧы ⲃⲟⲇⲟⲗⲉύ ⲕⲟⲧⲟⲣыύ ⲏⲁⲡⲣυⲅⲏⲩⲗ ⲏⲁ ⲙⲟύ ⲭⲩύ υ ⲡⲣⲟⲥυⲗ ⳡⲧⲟⳝы я ⲧⲉⳝя ⲡⲟⲕⲁⲧⲁⲗ?  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲃⲟⲧ ⲡⲟⲏⲙυⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥⲉύⳡⲁⲥ ⳝⲩⲇⲉⲧ ⲏⲁ ⲧⲃⲟⲉⲙ ⲣⲧⲩ ⲡⲣⲉⲇⲥⲕⲁⳅыⲃⲁⲁⲧь ⲧⲉⳝⲉ ⳝⲩⲇⲩⳃυⲉ ⲧⲟ)?   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙы ⲙⲟⲯⲏⲟ ⲣⲟⳅⲃⲟⲇυⲧь ⲥⲃυⲏⲉύ ⲏⲁⲭⲩύ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲃⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲃⲧⲟю ⲙⲁⲧь ⲥⲉύⳡⲁⲥ ⳝⲩⲇⲩ ⲥⲟⲃⲙ ⲭⲩⲉⲙ ⲗⲉⳡυⲧьь ⲕⲁⲕ ⲇⲟⲕⲧⲟⲣ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲃⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ыⲧ ⲩⲯⲉ ⲩⲥⲧⲁⲗ ⲙⲟύ ⲭⲩύ ⲥⲟⲥⲧⲁь υ ⲩⲙⲉⲣⲁⲉⲱьⲥ ⲙⲏⲉ ⲡⲣⲙ ⲃ яύцⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲃⲟⲧ ⲡⲟⲏⲙυⲁⲉⲱь ⳡⲧⲟⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙы ⲡⲟⲅυⳝⲏυⲧ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲅⲉⲣⲟύ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲃⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟю ⲙⲁⲧь ⲥⲉύⳡⲁⲥⳝⲩⲇⲩ ⲥⲟⲃυⲙ ⲭⲩⲉⲙ ⲕⲁⲥⲧυⲣⲟⲃⲁⲧь ⲕⲗⲧⲟⲣ ⲉё)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲃⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥⲉύⳡⲁⲥ ⳝⲩⲇⲉⲧ ⲡⲟⲕⲁⳅыⲃⲁⲧь ⲃ ⲕⲁⲕⲟύ ⲥⲧⲟⲣⲟⲏⲉ ⲧы ⲉⲅⲟ ⲥⲟⲥⲁⲗ) ⲡⲟⲧⲟⲙ ⲕⲣⳡ ⲧы ⲡⲣυύⲇⲉⲱь ⲏⲁ ⲧⲟ ⲙⲉⲥⲧⲟ ⲥⲧⲁⲏⲉⲱь ⲣⲁⲕⲟⲙ υ ⲥⲕⲁⲯⲉⲱь ⳡⲧⲟ ⳝы ⲃⲉⳝⲁⲗ ⲧⲉⳝ0 ⲁ ⲕⲣⳡ ⲏⲟⲅⲟύ ⲧⲉⳝⲉ ⲡⲟ ⲉⳝⲁⲗьⲏυⲕⲩ ⲇⲁⲙ υⲥ ⲕⲁⲯⲩ ⳡⲧⲟ ⳝы ⲡⲟⲱⲉⲗ ⲏⲁⲭⲩύ ⲟⲧ ⲥюⲇⲁ)  [<emoji document_id=5438203928527253097>💀</emoji>]',
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲥⲟⲥⲁⲗⲁ ⲏⲉ ⲥⲡⲣⲁⲱυⲃⲁя)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲥⲟ ⲥⲕⲟⲣⲟⲥⲧью ⲥⲃⲉⲧⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ, ⲩ ⲏⲉⲉ ⲁⲯ ⲡυⳅⲇⲁ ⳅⲁⲅⲟⲣⲉⲗⲁⲥь??   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⳃⲁ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡⲣⲟⲗⲟⲯⲩ ⲧⲟⲣⲅⲟⲃыⲉ ⲡⲩⲧυ ⲕ ⲡυⳅⲇⲁⲕⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲉⳝя ⲉⳝⲁⲗυ ⲭⲁⳡυ ⲕⲟⲅⲇⲁ ⲧⲃⲟύ ⲟⲧⲉц ⲙⲁⲥⲥυⲣⲟⲃⲁⲗ ⲙⲏⲉ яυцⲁ ⲥⲃⲟⲉύ ⲅⲩⳝⲟύ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲃъⲉⳅⲯⲁⲉⲱь ⲏⲁ ⲙⲟύ ⲭⲩύ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳝⲩⲇυⳝυⲗⲇⲉⲣ ⲙⲟⲉⲅⲟ ⲭⲩя ⲧы ⳅⲏⲁⲗ?()   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲉⳝя ⳝⲩⲇⲩ ⲉⳝⲁⲧь ⳝⲟⲙⳝⲩⲕⲟⲃⲟύ ⲣⲟⳅⲉύ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⲕⲟⲗⲭⲟⳅⲏυцⲁ ⲉⳝⲁⲏⲁя ⲏⲁ ⲙⲟёⲙ ⲭⲩю ⲡяⲗⲱⲉⲧ ⳡⲉⳡёⲧⲕⲩ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲥⲟⲥёⲧ ⲙⲟύ ⲭⲩύ ⲡⲟⲇ ⲣⲩⲥⲥⲕυύ ⳝυⲧ ⲥⲧⲁⲥⲁ ⲙⲉⲭⲁύⲗⲟⲃⲁ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲙⲁⲣⲉⲟⲏⲉⲧⲕⲁ ⲉⳝⲁⲏⲁя ⲡⲟⲇ ⲙⲟύ ⲭⲩύ ⲭⲟⲇυⲱь   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲏⲁⲭⲩύ ⲧы ⲙⲟύ ⲭⲩύ ⲕⲗⲁⲇⲉⲱь ⲥⲉⳝⲉ ⲃ ⲣⲟⲧ,ⲧⲉⳝⲉ ⲏⲣⲁⲃυⲧⲥя ⲃⲕⲩⲥ ?   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⲥⲟⲡⲁⲅⲟⲙ ⲉⳝⲁⲗ ⲡⲟύⲙυ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⳅⲁ ⲡⲣⲟⲥⲧⲟ ⲧⲁⲕ ⲟⲧⲇⲁⲗⲁⲥь)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲥⲟⲥⲁⲗⲁ ⲡⲣυ ⲗⲩⲏⲉ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ ⲡⲟⲏυⲙⲁⲉⲱь ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⲥⲟⲥⲉⲧ) я ⲧⲃⲟю ⲙⲁⲧь ⲇⲟⲱυⲣⲁⲕⲟⲙ ⲉⳝⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⲥⲟⲥⲉⲧ)я ⲧⲃⲟю ⲙⲁⲧь ⲥⲡυⳡⲕⲁⲙυ ⲉⳝⲩ)   [<emoji document_id=5438203928527253097>💀</emoji>]',
'[<emoji document_id=5438203928527253097>💀</emoji>] ыⲧ ⲃⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟю ⲙⲁⲧь ⳝⲩⲇⲩ ⳅⲁ ⲡⲣⲟⲥⲧⲟ ⲧⲁⲕ ⲉⳝⲁⲧь) ⲧы ⲃⲟⲧ ⲭⲩⲗυ ⲕⲁⳡⲁⲉⲱь ⲙыⲱцы ⲙⲟⲉύ ⲕⲟⳡⲏⲟύ ⲧⲟ?) ⲧы ⲇⲩⲙⲁⲉⲱьⳡ ⲧⲟ ⲙⲟⲉύ ⲕⲟⳡⲏⲟύ ⲙⲟⲯⲏⲟ ⲏⲁⲕⲁⳡⲁⲧь ⲧⲉⲗⲟ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡⲟⳡⲉⲙⲩ ⲧы ⲏюⲭⲁⲗⲗ ⲙⲟю ⲕⲟⲏⳡⲩ ⲧⲟ?)??ⲧы ⲥⲩⲕⲁ ⲏⲁⲣⲕⲟⲙⲁⲏ ⲉⳝⲁⲏύ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲃⲟⲧ ⲡⲟⲏⲙυⲁⲉⲱь ⳡⲧⲟ ыⲧ ⲡⲟⲡⲁⲗ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲏⲁ ⲣⲁύ ⲧⲟ υ ⲏⲁⳡⲁⲗ ⲥⲟⲥⲁⲧь ⲙⲏⲉ ⲉⲅⲟ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ыⲧ ⲃⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ыⲧ ⲥⲩⲕⲁ ⲟⲧⲥⲟⲥⲁⲗ ⲙⲟύ ⲭⲩύ υ ⲧⲉⲡⲉⲣь ыⲧ ⲥⲩⲕⲁ ⲫⲉύⲗυⲱьⲥя ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⲕⲁⲕ ⲇⲏⲁⲣ ⲉⳝⲁⲏыύ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲥⲉύⳡⲁⲥ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙы ⲏⲁⲧяⲏⲩ ⲏⲁ ⲧⲃⲟⲉ ⲉⳝⲁⲗⲟ) ⳡⲧⲟⳝы ⲕⲣⲁⲥυⲃⲉⲉ ⲥⲧⲁⲗ0  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲯⲉ ⲡⲟⲇⲥⲟⲥ ⲙⲟⲉⲅⲟ ⲭⲩя, ⲕⲟⲧⲟⲣыύ ⲡⲣⲁⲃυⲧ ⲡυⳅⲇⲟύ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲥⲡⲉⲣⲙⲟⲅⲗⲟⲧ ?  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲡⲟ ⲧⲃⲟⲉⲙⲩ ⲉⳝⲁⲗⲩ ⲭⲩⲉⲙ ⲧⲟⲣⲙⲟⳅυⲗ,υ ⲥⲧⲉⲣ ⲧⲟⲣⲙⲟⳅⲏыⲉ ⲕⲟⲗⲟⲇⲕυ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲃⲟⲧ ⲧы ⲥⲩⳡⲕⲁ ⲉⳝⲁⲏⲏⲁя) ⲧы ⳝⲗяⲧь ⲡⲟⲡⲩⲧⲁⲗⲁ ⲃⲥⲉ ⲏⲁⲭⲩύ) ⳅⲁⳡⲉⲙ ⲧы ⲃ ⲡυⳅⲇⲩ ⲥⲃⲟⲉύ ⲙⲁⲙⲕυ ⲥⲕⲗⲁⲇυⲣⲩⲉⲱь ⲇⲣⲁⲃⲁ ⲏⲁ ⳅυⲙⲩ? ⲇⲗя эⲧⲟⲅⲟ ⲉⲥⲧь ⲥⲁⲣⲁύ) ⲧⲩⲡⲁя ⲧы ⲱⲗюⲭⲁ) ⲧы ⲉⳃⲉ ⲃ ⲡυⳅⲇⲉ ⲥⲃⲟⲉύ ⲙⲁⲙⲕυ ⲕⲁⲙυⲏ ⳅⲁⲙⲩⲧυ) ⳡⲙⲟ ⲧы ⲏⲉⲇⲟⲣⲁⳅⲃυⲧⲟⲉ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲉⳝя ⲉⳝⲁⲗ ⲃ ⲡⲟⲇⲃⲁⲗⲉ ⲏⲁ ⲅⲏυⲗⲟⲙ ⲥⲧⲩⲗⲉ) ⲧы ⲧⲃⲁⲣь ⲉⳝⲩⳡⲁя) ⲁ ⲏⲩ ⲏⲁⲭⲩύ ⲡⲟⲱⲉⲗ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳅⲏⲁⲉⲱь,ⲕⲟⲅⲇⲁ я ⲩⲃυⲇⲉⲗ ⲧⲃⲟю ⲡυⳅⲇⲩ, я ⲡⲟⲇⲩⲙⲁⲗ, ⲡⲟⳡⲉⲙⲩ ⳝы ⲧⲁⲙ ⲏⲉ ⲡⲟⲥⲧⲟⲣυⲧь ⲏⲟⲃыύ ⲅⲟⲣⲟⲇ? ⲟⲭⲩⲉⲏⲏⲁя υⲇⲉя! ⲧⲁⲙ ⲙⲏⲟⲅⲟ ⲙⲉⲥⲧⲟ) ⲡⲟⲥⲧⲣⲟυⲙ ⲅⲟⲣⲟⲇ) ⲏⲉⲉⲉ,ⲥⲧⲟύ,ⲥⲧⲣⲁⲏⲩ! υ я ⳝⲩⲇⲩ ⲉύ ⲡⲣⲁⲃυⲧь) υⲥⲭⲟⲇя υⳅ ⲃⲥⲉⲅⲟ эⲧⲟⲅⲟ,ⲡⲟⲗⲩⳡⲁⲉⲧⲥя,ⳡⲧⲟ я ⲡⲣⲁⲃⲗю ⲧⲃⲟⲉύ ⲡυⳅⲇⲟύ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳅⲏⲁⲉⲱь ⳡⲧⲟ? ⲥыⳝⲁⲗⲁⲥь ⲏⲁⲭⲩύ ⲥ ⲙⲟυⲭ ⲅⲗⲁⳅ) ⲱⲗюⲭⲁ ⲧы ⲉⳝⲁⲏⲏⲁя) я ⲧⲉⳝя ⲥⲉύⳡⲁⲥ ⲧⲩⲧ ⲏⲁⲭⲩύ ⳅⲁⲣⲉⲯⲩ,ⲕⲁⲕ ⲱⲁύⲧⲁⲏ, ⲧⲃⲁⲣυⲏⲁ ⲧы ⲟⳝⲟⲥⲁⲏⲏⲁя)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲥⲗыⲱ! ⲧы ⲟⲗⲉⲏь ⲉⳝⲁⲏⲏыύ) я ⲧⲉⳝⲉ ⲃⲥⲉⲅⲇⲁ ⳝⲩⲇⲩ ⲣⲁⲇ ⲇⲁⲧь ⲡⲟⲥⲟⲥⲁⲧь)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳝⲗя, ⲡυⳅⲇⲁ ⲧⲩⲡⲁя, ⲧы ⳡⲉ ⲥⲩⲕⲁ ⲏⲁⲭⲩύ ⲃъⲉⳝⲁⲗⲁⲥь ⲡⲟ ⲡⲟⲗⲏⲟύ? я ⲧⲉⳝⲉ ⲥⲉύⳡⲁⲥ ⲡυⳅⲇⲩ ⲧⲃⲟю ⲏⲁⲭⲩύ ⲥⲕⲣⲩⳡⲩ,ⲡⲟⲧⲁⲥⲕⲩⲱⲕⲁ ⲧы ⲉⳝⲁⲏⲏⲁя) υⲇυ ⳝⲁⲏⲁⲏы ⲃⲟⲣⲩύ,ⲯυⲃⲟⲧⲏⲟⲉ ⲧы ⲭⲩⲉⲥⲟⲥⲏⲟⲉ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲯⲁⲗⲕⲟⲉ ⲭⲩⲉⲡⲟⲧⲁⲗⲟ) ⲡⲉⲣⲉⲥⲧⲁⲏь ⲭⲩυ ⲥⲟⲥⲁⲧь) ⲡυⲇⲁⲣⲥⲕⲁ) я ⲧⲉⳝя ⲥⲉύⳡⲁⲥ ⲏⲁ ⲭⲩю ⲧⲃⲟⲉⲅⲟ ⳝⲁⲧυ ⲣⲁⲥⲡⲏⲩ, ⲕⲁⲕ υυⲥⲩⲥⲁ ⲭⲣυⲥⲧⲁ ⲏⲁ ⲕⲣⲉⲥⲧⲉ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲁ ⳅⲁⳡⲉⲙ ⲙⲟю ⳅⲁⲗⲩⲡⲩ ⲃⲟ ⲃⲣⲉⲙя ⲙυⲏⲉⲧⲁ ⲡⲟⲕⲩⲥыⲃⲁⲉⲱь   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡⲟⲙⲏυⲱь ⲕⲁⲕ ⲧы ⲙⲟύ ⲭⲩύ ⲩⳅⲏⲁⲗⲁ,ⲥⲣⲉⲇυ ⲧыⲥяⳡυ? ⲥⲣⲁⳅⲩ ⲩⲃυⲇⲉⲗⲁ ⲧⲟ,ⳡⲧⲟ ⲡⲣυⲏυⲙⲁⲉⲱь ⲃ ⲣⲟⲧ ⲕⲁⲯⲇыύ ⲇⲉⲏь  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲃⲟⲧ ⲥⲕⲁⲯυ ⲙⲏⲉ ⲟⲇⲏⲟ) ⳅⲁⳡⲉⲙ ⲧⲃⲟя ⲙⲁⲧь ⲙⲟύ ⲭⲩύ ⲥⲙⲁⳅⲁⲗⲁ? ⲇⲁ, я ⲡⲟⲏυⲙⲁю,ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⳝⲟⲗьⲱⲟύ,ⲏⲟ ⲁⲏⲁⲗ ⲧⲁ ⲉⲉ ⳝⲟⲗьⲱⲉ) ⲧⲁⲙ ⲭⲟⲇяⲧ ⲥⲗⲩⲭυ ⲥⲧⲟⲗьⲕⲟ ⲭⲩⲉⲃ ⳅⲁⲧⲉⲣяⲗⲟⲥь)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲃⲟⲧ ⲡⲟⲏⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲙⳡⲁⲗ ⲡⲟ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙы ⲥⲟ ⲥⲕⲟⲣⲟⲥⲧь 300 ⲕⲙ ⲃ ⳡⲁⲥ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲥⲩⲕⲁ ⲕⲁⲕ ⲇⲉⲙⲟⲏ ⲉⳝⲁⲏыύ) ыⲧ ⲏⲉ ⲩⲥⲧⲁⲗ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩ?) ⲙⲟⲯⲉⲧ ⲡⲟύⲇⲉⲱь ⲡⲣυⲗⲯυⲱь ⲏⲁ ⲙⲟυ ύцⲁ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲃⲟⲧ ⲡⲟⲏⲙυⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⳝⲩⲇⲩ ⲗⲟⲃυⲧь ⲣыⳝⲩ ⲃ ⲡⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙы)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲃⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ыⲧ ⲥⲩⲕⲁ ⲅⲉⲣⲟύ) ⲕⲟⲧⲟⲣыύ ⲟⲧⲥⲟⲥⲁⲗ ⲙⲟύ ⲭⲩύ υ ⲣⲁⲥⲥⲕⲁⳅⲁⲗ ⲥⲟⲥⲉⲇяⲙ ⲧⲟ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲃⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⳝⲩⲇⲩ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲥⲉύⳡⲁⲥ ⳡυⲥⲧυⲧь ⲁⲏⲁⲗьⲏыύ ⲕⲁⲏⲁⲗы ⲧⲃⲟⲉύ ⲙⲁⲙы ⲧⲟ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲃⲟⲧ ⲡⲟⳡⲉⲙⲩ ⲕⲟⲅⲇⲁ ⲡⲣυⲭⲟⲇυⲱь ⲥⲟ ⲱⲕⲟⲗы ⲧⲟ ⲃⲥⲉⲅⲇⲁ ⲥⲁⲇυⲱьⲥ ⲏⲁ ⲙⲟύ ⲭⲩύ) ⲟⲧⲇⲟⲭⲏⲩⲧь ⲱⲟⲗυ υ ⲥⲏⲧь ⲥⲧⲣⲉⲥ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲃⲟⲧ ⲡⲟⲏⲙυⲁⲉⲱь ⳡⲧⲟ ⲡⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲙы ⳝⲩⲇⲉⲧ ⳝⲉⲗⲁ ⲡⲟⲥⲗⲉ ⲧⲟⲅⲟ ⲕⲁⲕ я ⲕⲟⲏⳡⲩ ⲏⲁ ⲏⲉё?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⳃⲁ ⳡⲉⲣⲉⳅ ⲥⲃⲟύ ⲭⲩύ ⲡⲩⳃⲩ эⲗⲉⲕⲧⲣⲟ ⳅⲁⲣяⲇ ⲧⲉⳝⲉ ⲃ ⲙⲟⳅⲅ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲡυⳅⲇⲟύ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃⲕⲣⲩⲧυⲗ ⲗⲁⲙⲡⲟⳡⲕⲩ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⳡⲉⲣⲉⳅ ⲙⲟύ ⲭⲩύ ⲡⲣⲟⲗυⲃⲁⲉⲧⲥя ⲕⲁⲕ ⲃⲟⲇⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⲃⲉⲇⲣⲟⲙ ⲉⳝⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⲥⲁⲗⲁⲧⲟⲙ ⲉⳝⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲙⲁⲧь ⲧⲃⲟю ⲫⲉⲏⲟⲙ ⲉⳝⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲙⲁⲧь ⲧⲃⲟю ⲕⲁⲣⲧⲟⲱⲕⲟύ ⲉⳝⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲙⲁⲧь ⲧⲃⲟю ⲅⲣⲉⳡⲕⲟύ ⲉⳝⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲙⲁⲙⲕⲁ ⲧⲃⲟя ⲧⲃⲟⲉⲙⲩ ⲟⲧцⲩ ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ υⳅⲙⲉⲏяⲗⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲙⲁⲧь ⲧⲃⲟю ⲃ ⳝⲟⲗьⲏυцⲉ ⲉⳝⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲙⲁⲧь ⲧⲃⲟю ⲉⳝⲁⲗ ⲩ ⲏⲉⲉ ⲁⲯ ⲡυⳅⲇⲁ ⳅⲁⲇыⲙυⲗⲁⲥь)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲙⲟя ⲕⲟⲏⳡⲁ ⳅⲁⲙⲉⲏяⲉⲧ ⲕⲣⲟⲃь ⲃ ⲧⲃⲟⲉⲙ ⲧⲉⲗⲉ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲃⲕⲩⲣⲥⲉ ⳡⲧⲟ ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉⲅⲟ ⳝⲁⲧυ ⲯυⲃⲩⲧ ⲅⲏⲟⲙы?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲃⲟⲧ ⳅⲁⳡⲉⲙ ⲧы ⲧⲁⲕ ⲏⲁⲕυⲇыⲃⲁⲉⲱьⲥя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲟⲃⳡⲁⲣⲕⲁ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲏⲁⲭⲩύ ⲧы ⲡⲣⲟⲃⲟⲇυⲗ ⲧⲉⲥⲧ ⲇⲣⲁύⲃ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ?   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡυⲇⲟⲣ ⲟⲅⲏⲉⲇыⳃⲁⳃυύ υⲇυ ⲥюⲇⲁ я ⲧⲉⳝя ⲉⳝⲁⲧь ⳝⲩⲇⲩ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] яⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲏⲁ ⲙⲟⲣⲟⳅⲉ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⳝыⲗⲁ ⲡьяⲏⲁя υ ⲥⲕⲁⲕⲁⲗⲁ ⲏⲁ ⲙⲟⲉю ⲭⲩю)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲏⲉ ⲡⲟⲏяⲗ ⲧⲃⲟя ⲙⲁⲧь ⲣⲉⲁⲗьⲏⲟ ⳃⲁⲥ ⲥⲟⲥⲁⲧь ⲙⲏⲉ ⳝⲩⲇⲉⲧ)   [<emoji document_id=5438203928527253097>💀</emoji>]',
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⲥ ⲭⲩя ⲡⲩⲥⲕⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⲥⲏⲟⲃⲁ ⲏⲁ ⲙⲟύ ⳡⲗⲉⲏ ⲡⲣυⳅⲉⲙⲗυⲗⲁⲥь ⲡⲟⲥⲗⲉ ⲡⲟⲗёⲧⲁ ⲃ ⲧⲁⲇⲯυⲕυⲥⲧⲁⲏ ⲏⲁ ⲣⲟⲇυⲏⲩ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡⲟⳡⲉⲙⲩ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ, ⳅⲁⲧяⲅυⲃⲁⲉⲧ ⲭⲩυ, ⲕⲁⲕ ⲧⲣⲉⲩⲅⲟⲗьⲏυⲕ ⳝⲉⲣⲙⲩⲇⲥⲕυύ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⲡыⲗⲉⲥⲟⲥⲟⲙ ⲉⳝⲁⲗ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⲥ ⲭⲩя ⳡⲉⲣⲉⳅ ⳅⲁⳝⲟⲣы ⲡⲉⲣⲉⲕυⲇыⲃⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲃⲟⳅьⲙυ ⲥⲉⳝⲉ ⲃ ⳅⲩⳝы ⲗⲉύⲕⲩ υ ⲡⲟⲗυⲃⲁύ ⲟⲅⲟⲣⲟⲇы ⲃ ⲡυⳅⲇⲉ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲯⲉ ⲣⲁⲕⲟⲃⲩю ⲟⲡⲩⲭⲟⲗь ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲩⲥⲧⲣⲟⲏяⲗ ⲡⲣυ ⲡⲟⲙⲟⳃυ ⲥⲃⲟⲉⲅⲟ ⲭⲩя)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲕⲟⲅⲇⲁ ⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳝⲩⲇⲉⲧ ⲁⲏⲅυⲏⲁ ⲡⲟⳅⲟⲃυ ⲙⲉⲏя я ⳝⲩⲇⲩ ⲉύ ⲃ ⲅⲟⲣⲗⲟ ⳝⲣы3ⲅⲁⲧь ⲥⲃⲟⲉύ ⲥⲡⲉⲣⲙⲟύ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲅⲣⲩⲇⲏⲩю ⲕⲗⲉⲧⲕⲩ ⲭⲩⲉⲙ ⲣⲁⲥⲥⲡυⲗυⲃⲁⲗ ⲡⲟⲡⲟⲗⲁⲙ υ ⲥⲧⲉⲗυⲗ ⲡⲟⲇ ⲥⲃⲟυⲙυ ⲇⲃⲉⲣьⲙυ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳅⲁⳡⲉⲙ ⲧы ⲣⲧⲟⲙ ⲏⲁ ⲭⲩύ ⲩⲡⲁⲗ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲙⲁⲱⲕⲁ ⳅⲁ ⳝⲁⲣⳝⲁⲣυⲥⲕⲩ ⲭⲩύ ⲥⲟⲥⲉⲧ ⲏⲁ ⲣыⲏⲕⲉ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡⲟⲥⲗⲉ ⲧⲟⲅⲟ ⲕⲁⲕ я ⲉύ ⲗⲉⳡυⲗ ⲣⲁⲕ ⲅⲩⳝы ⳅⲁⲗⲩⲡⲟύ ⲟⲏⲁ ⲡⲟⲗⳝюⳝυⲗⲁ ⲉⲅⲟ ⲥⲕⲟⲣⲟ ⲙⲟύ ⲭⲩύ ⲧы ⲥⲙⲟⲯⲉⲱь ⲏⲁⳅыⲃⲁⲧь ⲡⲁⲡⲕⲟύ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲃⲟⲧ ⲩ ⲧⲉⳝя яⲃⲏⲟ ⲡυⲇⲟⲣⲥⲕυⲉ ⲏⲁⲕⲗⲟⲏⲏⲟⲥⲧυ(   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲙⲉⲏя ⲃⲇⲟⲭⲏⲁⲃⲗяⲉⲧ ⲧⲃⲟύ ⲣⲟⲧ ⲏⲁⲡⲁⲃⲱυύ ⲏⲁ ⲙⲟύ ⲭⲩύ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲕⲁⲕ ⲧы ⲟⲧⲏⲉⲥⲉⲱьⲥя ⲕ ⲧⲟⲙⲩ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⳅⲁⲥⲧⲣяⲗ ⲃ 12 ⲡⲉⲣⲥⲧⲏⲟύ ⲕυⲱⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ??   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲡυⳅⲇυⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲩⳝы ⲭⲩⲉⲙ ⲃыⳝυⲗ, ⲟⲏⲁ ⲧⲁⲕ ⲅⲟⲣьⲕⲟ ⲡⲗⲁⲕⲁⲗⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲕⲗυⳅⲙⲩ ⲥⲇⲉⲗⲁю)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲭⲣⲉⳝⲉⲧ ⲗⲟⲙⲁю)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲱⲉю ⲗⲟⲙⲁю)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲗυⲧⲟⲣ ⲥ ⲏⲟⲅυ ⲃыⳝυⲃⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕυⲣⲡυⳡυ ⲃ ⲉⳝⲗⲟ ⲕυⲇⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⳡⲉⲣⲇⲁⲕⲉ ⲉⳝⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲇⲃⲉⲣⲏⲟύ ⲣⲩⳡⲕⲉ ⲉⳝⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲕⲁⲗυⲧⲕⲉ ⲉⳝⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⳅⲁⳝⲟⲣυⲏⲟύ ⲉⳝⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⲕⲁⳡⲉⲣⲅⲟύ ⲉⳝⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲟⳝ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳝыⳡⲕυ ⲧⲩⲱυⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲥⲃⲟю ⲥⲉⲥⲧⲣⲩ ⲡⲟ ⲙⲟⲉⲙⲩ ⲥⲟⲅⲗⲁⲥυю ⲉⳝⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲏⲟⲯⲇⲁⳡⲕⲟύ ⲭⲩяⲣυⲗ ⲡⲟ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧёⲣⲕⲟύ ⲧⲉⲣ ⲉⳝⲗⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⲟⳝⲟⲥⲥⲁⲗ ⲡⲟⲕⲁ ⲧы ⲕⲗυⲧⲟⲣ ⲥⲉⲥⲧⲣⲉ ⲗυⳅⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟю ⲙⲁⲧь ⲟⲥⲩⲇυⲗυ ⲡⲟⲯυⳅⲉⲏⲏⲟ ⳅⲁ ⲡⲟⲥυⲇⲉⲗⲕυ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲙⲟύ ⳡⲗⲉⲏ ⲥ 5 эⲧⲁⲯⲁ ⲡⲁⲇⲁⲗⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟⲉύ ⲙⲁⲙⲕⲉ ⲭⲩⲉⲙ ⲃ ⲅⲗⲁⳅ ⲧыⲕⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁ ⲉⳝⲗⲟ ⲕⲟⲏⳡⲁⲗ ⲡⲟⲕⲁ ⲧы ⲭⲩύ ⲟⲧцⲁ ⲥⲟⲥⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲥⲃⲟю ⲙⲁⲧь ⲩⳡυⲗ ⲭⲩύ ⲥⲟⲥⲁⲧь)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲡⲟ ⲅⲩⳝⲉ ⲇⲁⲃⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲡⲟ ⳃⲉⲕⲉ ⲩⲇⲁⲣυⲗ , ⲩ ⲏⲉⲉ ⳡⲉⲗюⲥⲧь ⲥⲗⲟⲙⲁⲗⲁⲥь)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲗⲩⲡⲟύ ⲡⲟ ⲗⳝⲩ ⲭⲩяⲣυⲗ ⲡⲟⲕⲁ ⲧы ⲙⲏⲉ яύцⲁ ⲗυⳅⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⳅⲁ ⲇⲉⲏьⲅυ ⲥⲏυⲙⲁⲗ, ⲡⲟⲥⲗⲉ ⲟⲧⲇⲁⲃⲁⲗ ⳝⲟⲙⲯⲁⲙ υ ⲟⲏυ ⲉⲉ ⲡⲟ ⲕⲣⲩⲅⲩ ⲉⳝⲁⲗυ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⳝⲗяⲇь, ⲁ ⲧⲃⲟύ ⲟⲧⲉц ⲣⲁⳝⲟⲧⲁⲉⲧ ⲃ ⲅⲉύ ⲕⲗⲩⳝⲉ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲣⲟⳅⲩ ⲃⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧыⲕⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⲡⲁⲇⲁⲗⲁ ⲏⲁ ⲙⲟύ ⳡⲗⲉⲏ ⲕⲁⲕ ⳅⲁⲥⲟⲭⲱυύ ⲗυⲥⲧ ⲥ ⲇⲉⲣⲉⲃⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⲡⲗⲟⲥⲕⲟⲅⲣⲩⲇⲏⲁя ⲉⳝⲁⲏⲁⲱⲕⲁ ⲥⲩⲕⲁ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧⲉⳝⲉ ⲏⲁ ⲉⳝⲗⲟ ⲏⲁⲧяⲅυⲃⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⲥⲧяⲅυⲃⲁⲗ, ⲟⲏ ⲥⲧⲁⲏⲟⲃυⲗⲥя ⲇⲗυⲇⲏⲏыύ ⲕⲁⲕ ⳅⲙⲉя)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⳅⲁ ⲡⲟⲗⲟⲃыⲉ ⲅⲩⳝы ⲕ ⲡⲟⲧⲟⲗⲕⲩ ⲡⲣυⳝυⲃⲁⲗ υ ⲭⲁⲣⲕⲁⲗ ⲉύ ⲃ ⲉⳝⲗⲟ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲱⲁⲙⲡⲩⲣⲟⲙ ⲉⳝⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁ ⳃⲉⲕⲩ ⳅⲁ ⳅⲁⳝⲟⲣⲟⲙ ⲇⲁⲃⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⲡυⳅⲇⲟύ ⲕⲁⲣⲧⲟⲱⲕⲩ ⲥⲟⲣⲧυⲣⲟⲃⲁⲧь ⲩⲙⲉⲉⲧ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⳡⲉⲣⲉⳅ ⲡⲣⲟⲅυⳝ ⲉⳝⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲃⲕⲩⲣⲥⲉ ⳡⲧⲟ я ⳃⲁⲥ ⲧⲃⲟю ⲙⲁⲧь ⳡⲗⲉⲏⲟⲙ ⲟⲧⲡυⳅⲇυⲗ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⳅⲁ ⲭⲗⲉⳝ ⲥⲟⲥⲁⲗⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⳅⲁ ⲟⲇⲉⲯⲇⲩ ⲥⲟⲥⲁⲗⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⳅⲁ ⲣⲩⳝⲗь ⲟⲧⲇⲁⲗⲁⲥь)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲡⲣυⲭⲗⲟⲡⲏⲩⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳡⲗⲉⲏⲟⲙ ⲡⲟⲥⲗⲉⲇⲏυⲉ ⳅⲩⳝы ⲃыⳝυⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲟⳝⲗυⳅыⲃⲁⲉⲱь ⲙⲏⲉ ⳡⲗⲉⲏ ⲡⲟⲥⲗⲉ ⲁⲏⲁⲗьⲏⲟⲅⲟ ⲥⲉⲕⲥⲁ ⲥ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉύ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡυⳅⲇⲩ ⲥⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲡⲟⲗυⲃⲁⲉⲱь ⲕⲁⲕ ⲟⲅⲟⲣⲟⲇ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲉⳝⲗⲟ ⲟⳝ ⲁⲥⲫⲁⲗьⲧ ⲣⲁⳅъⲉⳝⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲉⳝⲗⲟ ⲭⲁⲣⲏⲩⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲗυⲱⲩ ⲧⲉⳝя ⲇⲉⲃⲥⲧⲃⲉⲏⲏⲟⲥⲧυ, υ ⳝⲩⲇⲩ ⲣⲉⳅⲁⲧь ⲧⲃⲟⲉ ⲇⲉⲃⲧⲥⲃⲉⲏⲏⲟⲉ ⲧⲉⲗⲟ ⲏⲟⲯⲟⲃⲕⲟύ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲏⲁ ⲏⲟⲅⲁⲭ ⲏⲟⲅⲧυ ⲅⲣыⳅⲉⲧ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲅⲟⲣⲱⲟⲕ ⲥ ⲅⲟⲃⲏⲟⲙ ⲏⲁ ⲅⲟⲗⲟⲃⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⲇⲉⲃⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲡⲟⲇⳃⲉⳡυⲏы ⲇⲁⲃⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲅⲩⳝⲩ ⲥⲗⲟⲙⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲏⲁ ⲉⳝⲗⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲙⲩⲥⲟⲣⲏыύ ⲡⲁⲕⲉⲧ ⲟⲇⲉⲃⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲃ ⲧⲩⲭⲗⲟύ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⲡⲁⲣыⲱⲉύ ⲣⲁⳅⲃⲟⲇυⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⲥⲃⲟυⲙυ ⲅⲗⲁⲏⲇⲁⲙυ ⲙⲁⲱⲟⲏⲕυ ⳃⲉⲕⲟⳡυⲧ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲭⲩύ ⲡⲟⲗⲟⲥⲕⲁⲗ ⲃ ⲙⲟ3ⲅⲁⲭ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲭⲩύ ⲃ ⲅⲟⲣⲗⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲩⲃⲁⲗ , ⳡⲧⲟⳝ ⲟⲏⲁ ⲩ ⲏⲉⲉ ⲏⲉ ⲱⲁⲧⲁⲗⲁⲥь)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⳡⲉⲣⲉⳅ ⲙⲟⳅⲅ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲙⲟⳡⲩ ⲫυⲗьⲧⲣⲟⲃⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲡⲣυⲏυⲙⲁю эⲕⳅⲁⲙⲉⲏы, ⲁ ⲧⲃⲟя ⲙⲁⲙⲁ ⲇⲁёⲧ ⲙⲏⲉ ⲃⳅяⲧⲕⲩ ⲏⲁⲧⲩⲣⲟύ).   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲣⲃⲁⲗ ⲧⲉⳝⲉ цⲉⲗⲕⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲯⲁⲃⲟύ ⲧⲣⲩⳝⲟύ :3   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲥⲃⲟυⲙ яⳅыⲕⲟⲙ ⲃⲱⲉύ ⲗⲟⳝⲕⲟⲃыⲭ ⲏⲁ ⲡυⳅⲇⲉ ⲙⲁⲧⲉⲣυ ⲅⲟⲏяⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲥⲃⲟυⲙ ⲣⲧⲟⲙ ⲅⲗυⲥⲧⲟⲃ υⳅ ⲯⲟⲡы ⲙⲁⲧⲉⲣυ ⲃыⲧⲁⲥⲕυⲃⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲧⲃⲟύ ⲣⲟⲧ ⲕⲁⲕ ⲃⲁύ ⲫⲁύ) ⲕⲟⲧⲟⲣыύ ⲡⲣυⲏυⲙⲁⲉⲧ ⲧⲟⲗьⲕⲟ ⲭⲩυ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳝⲗяⲧь ⲧы ⲁⲏⲁⲗьⲏыύ ⳃⲁ ⲧⲃⲟⲉ ⲉⳝⲁⲗⲟ ⲏⲁ ⲥⲃⲟύ ⲭⲩύ ⲃыⲕυⲏⲩ ⲕⲁⲕ ⲧⲣяⲡⲕⲩ ⲉⳝⲁⲏⲏⲩю ⲟⲗⲉⲏь ёⳝⲁⲏⲏыύ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲭⲩύⲗⲁⲏ ⲟⳝⲟⲥⲁⲏⲏыύ ⲧыⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ эⲕⲥⲕⲩⲣⲥυю ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡⲣⲟⲃⲟⲯⲩ?) ⲉⳝⲗⲁⲕ ⲥⲩⲕⲁ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲟⳝⲟⲥⲁⲏⲏыύ ⲡⲣⲉⳅυⲣⲫⲁⲧυⲃ ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁ ⲡυⳅⲇⲩ ⲕⲁⲕ ⲩ ⲇⲁⲗⲙⲁⲧυⲏⲉцⲁ ⲇⲉⲗⲁю?))  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲥⲗыⲱ ⳡυⲭⲟⲧⲕⲁ ⲉⳝⲁⲏⲏⲁ я ⳃⲁⲥ ⳝⲩⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉ ⳝⲗяⲧь ⲁⲏⲁⲗьⲏыⲉ ⲧⲣⲩⳝы ⲭⲩⲉⲙ ⲡⲣⲟⳡυⳃⲁⲧь ⲥⲃυⲏⲟⲙⲁⲧⲕⲁ ⲧы ⲟⳝⲟⲥⲣⲁⲏⲏⲁя  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟύ ⲣⲟⲧ ⲉⳝⲁⲗ)ⲕⲁⲕ ⲇяⲧⲉⲗ ⲇⲩⲡⲗⲟ)ⲧы ⲯⲉ ⲡⲣⲟⲥⲧⲁⲧ ⲉⳝⲁⲏⲏⲁя)ⲇⲁⲃⲁύ ⲃⲥⲁⲥыⲃⲁύ ⲙⲟⲣύ ⲭⲩύ)ⲉⳝⲁⲏⲏыύ ⲧы ⲡыⲗⲉⲥⳝⲟⲣⲏυⲕ)ⲧⲃⲟύ ⲟⲧⲉц ⲡυⲇⲟⲣⲁⲥ ⳅⲟⲟⲫυⲗ)ⲇⲁⲃⲁύ ⳝⲗяⲧь ⲭⲟⳝⲟⲧ ⲉⳝⲁⲏⲏыύ)ⲥⲟⲥυ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲥⲟⲥⲕⲩ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲇⲃⲩⲗυⲕυύ ⲯⲟⲡⲟⲇⲣⲁⲏⲉц))) я ⳃⲁ ⲥⲇⲉⲗⲁю υⳅ ⲧⲉⳝя ⳅⲁⲃⲟⲇ ⲥⲁⲗⲟⲉⲇⲥⲕυύ υ ⲟⳝⲉⲥⲡⲉⳡⲩ ⲭⲟⲭⲗⲟⲃ ⲏⲁ ⳝⲉⲥⲕⲟⲏⲉⳡⲏыⲙυ ⳅⲁⲡⲁⲥⲁⲙυ ⲥⲁⲗⲁ)))  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲇ ⲏυⲕⲟⲙ ⲡυⲇⲟⲣ ⲏⲁⲃⲉⲣⲏⲟⲉⲣⲁⲏьⲱⲉ ⳅⲁⲃυⲥⲁⲗ, я ⲥⲡⲣⲁⲃⲕυ ⲏⲁⲃⲉⲗ ⲧⲉⳝя ⲧⲁⲙ ⳅⲏⲁюⲧ ⲃⲥⲉ ⲧы ⳅⲁⳝυⲃⲁⲉⲱь ⲧⲁⲙ ⲥⲧⲣⲉⲗⲕυ ⲁ ⲡⲟⲧⲟⲙ ⲥⲟⲥⲉⲱь ⲃ ⲣⲉⲁⲗⲉ υ ⲧⲉⳝⲉ ⲣⲃⲩⲧ ⲟⳡⲕⲟ ⲏⲩ эⲧⲟ ⲕⲟⲏⲉⳡⲏⲟ ⲧⲃⲟя ⲯυⳅⲏь ⲧы ⲇⲉⲗⲁύ ⳡⲧⲟ ⲭⲟⳡⲉⲱь ⲙⲏⲉ ⲃ ⲡⲣυⲏцυⲡⲉ ⲥⲣⲁⲧь ⲏⲁ ⲧⲃⲟⲉ ⲉⳝⲗⲟ ⲥ ⲇυⲃⲁⲏⲁ ⲡⲟⲏⲟⲥⲟⲙ..ⲏⲟ ⲧы ⲥⲁⲙ ⲧⲟ ⲕⲁⲕ? ⲕⲁⲕ ⲧы ⲙⲁⲧⲉⲣυ ⲃ ⲅⲗⲁⳅⲁ ⲧⲟ ⲥⲙⲟⲧⲣυⲱь υ ⲟⲧцⲩ ⲕⲟⲅⲇⲁ ⲇⲟⲙⲟύ ⲣⲁⲥⲡⲉⲣⲇⲟⲗⲉⲏⲏыύ ⲡⲣυⲭⲟⲇυⲱь ⲥⲁⲇυⲱьⲥя ⲃⲉⳡⲉⲣⲟⲙ ⳅⲁ ⲥⲉⲙⲉύⲏыύ ⲩⲯυⲏ ⲁ ⲩ ⲧⲉⳝя ⲏⲁ ⲅⲩⳝⲁⲭ ⲥⲡⲉⲣⲙⲁ υ ⲇⲉⲣьⲙⲟⲙ ⲃⲟⲏяⲉⲧ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲅⲟⲃⲏⲟ ⳝⲗяⲧь ⲧы ⲅⲁⲏⲇⲟυⳅⲃυⲗυⲥⲧⲟⲉ)ⲙⲏⲉ ⲧⲃⲟⲉⲙⲩ ⲟⲧцⲩ ⲟⲡяⲧь ⳝⲗяⲧь ⲅⲡⲗⲁⳅⲏыⲉ яⳝⲗⲟⲕυ ⲭⲩⲉⲙ ⲃыⲯυⲙⲁⲧь?ⲁⲗⲗⲉ ⳝⲗяⲧь)ⲁⲗυⳝⲁⳝⲁ ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩяⲭυⲗⲁ ⲧы ⲥ ⲕⲁⳅⲁⲏⲥⲕⲟⲅⲟ ⲃⲟⲕⳅⲁⲗⲁ)я ⳃⲁⲥ ⳝⲗяⲧь ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲉⲉ ⲁⲏⲁⲗьⲏыⲉ ⲧⲣⲩⳝы ⲭⲩⲉⲙ ⳝⲩⲇⲩ ⳡυⲥⲧυⲧь)я ⳝⲗяⲧь ⲁⲏⲁⲗⲇьⲏыύ ⲙυⲥⲧⲉⲣ ⲡⲣⲟⲡⲉⲣ ⲇⲗя ⲡυⳅⲇⲁⲕⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ)ⲡⲟⲏυⲙⲁⲉⲱь ⲙⲉⲏя?ⲏⲉ ⳅⲁⲅⲗⲁⲧыⲃⲁύ ⲙⲏⲉ)ⲗⲁⲇⲏⲟ?ⲧы ⲯⲉ ⳝⲗяⲧь ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲧⲃⲟⲉⲙ ⲁⲏⲁⲗⲉ ⲕⲁⲕ ⲃⲉⲏⲧυⲗяⲧⲟⲣ ⳝⲟⲗⲧⲁⲉⲧⲥя)ⲟⲏ ⳝⲗяⲧь ⲃ ⲁⲏⲁⲗ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ ⲏⲁ ⲕⲟⲃⲣⲉ ⲥⲁⲙⲟⲗⲉⲧⲉ ⳅⲁⲗⲉⲧⲉⲗ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲏⲁⲗьⲏыⲉ ⲧⲣⲩⳝы ⲭⲩⲉⲙ ⳝⲩⲇⲩ ⳡυⲥⲧυⲧь)я ⳝⲗяⲧь ⲁⲏⲁⲗⲇьⲏыύ ⲙυⲥⲧⲉⲣ ⲡⲣⲟⲡⲉⲣ ⲇⲗя ⲡυⳅⲇⲁⲕⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ)ⲡⲟⲏυⲙⲁⲉⲱь ⲙⲉⲏя?ⲏⲉ ⳅⲁⲅⲗⲁⲧыⲃⲁύ ⲙⲏⲉ)ⲗⲁⲇⲏⲟ?ⲧы ⲯⲉ ⳝⲗяⲧь ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲧⲃⲟⲉⲙ ⲁⲏⲁⲗⲉ ⲕⲁⲕ ⲃⲉⲏⲧυⲗяⲧⲟⲣ ⳝⲟⲗⲧⲁⲉⲧⲥя)ⲟⲏ ⳝⲗяⲧь ⲃ ⲁⲏⲁⲗ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ ⲏⲁ ⲕⲟⲃⲣⲉ ⲥⲁⲙⲟⲗⲉⲧⲉ ⳅⲁⲗⲉⲧⲉⲗ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲁⲗⲗⲉ ⳝⲗяⲧь)ⲕⲗяⳡⲁ ⲉⳝⲁⲏⲏⲁя ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧⲃⲟю ⲥⲟⲏⲏⲩю ⲁⲣⲧⲉⲣυю ⲡⲉⲣⲉⲯυⲙⲁю ⲟⳝⲟⲥⲁⲏⲏыύ ⲧы ⲙⲩⲇⲉⲏь)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲁ ⲃⲟⲧ ⲧы ⲙⲏⲉ ⲟⲧⲃⲉⲧь ⲏⲁ ⲃⲟⲡⲣⲟⲥ ⲡⲟⳡⲉⲙⲩ ⲧы ⲧⲁⲕⲟύ ⲉⳝⲁⲏⲏыύ ⲡυⲇⲟⲣⲁⲥ ⲕⲟⲧⲟⲣⲟⲅⲟ ⲉⳝⲩⲧ ⲃⲥⲉ ⲃ ⲯⲟⲡⲩ ⲡⲟⲇⲣяⲇ)ⲅⲗυⲏⲟⲙⲉⲥ ⲧы ⲉⳝⲁⲏⲏыύ)ⲧⲃⲟя ⲅⲟⲗⲩⳝяⲧⲏя ⲡⲟⲧⲣⲉⲡⲁⲏⲁ ⲏⲁⲭⲩύ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲇⲁⲃⲁύ ⲕⲣⳡ ⲙы ⲧⲃⲟю ⲙⲁⲧь ⲃⲙⲉⲥⲧⲉ ⲡⲟⲉⳝⲉⲙ я ⲇⲁⲙ ⲧⲉⳝⲉ ⲱⲁⲏⲥ)ⲉⲥⲗυ ⲏⲉ ⲥⲡⲣⲁⲃυⲱьⲥя я ⲟⲧⲡυⳅⲯⲩ ⲧⲉⳝя ⲥⲃⲟⲉύ ⳅⲁⲗⲩⲡⲟύ υ ⳅⲁⲥⲧⲁⲃⲗю ⲥⲟⲥⲁⲧь ⲙⲟύ ⲭⲩύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲥⲗыⲱ ⲧы ⲏⲁⲭⲩύ ⲉⲁⲏⲩⲧⲁя ⲧы ⲥⲕⲟⲣⲟⲡⲟⲥⲧυⲯⲏⲁя ⲙⲁⲏⲇⲁ)ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⳃⲁⲥ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⲡⲟⲧⲩⲭⲏⲉⲱь ⲕⲁⲕ ⲥⲡυⳡⲕⲁ ⲉⳝⲁⲏⲏⲁя)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲯⲉ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⳃⲁⲥ ⲃ ⲧⲃⲟⲉύ ⲉⳝⲁⲏⲩⲧⲟύ ⳝⲁⲱⲕⲉ ⳝⲗяⲧь ⲟⲥⲧⲁⲃⲗю ⲟⲅⲣⲟⲙⲏⲩю ⲇыⲣⲕⲩ υ ⳝⲩⲇⲩ ⲧⲩⲇⲁ ⲥⲩⲃⲁⲧь ⲥⲃⲟύ ⲭⲩύ)ⲃⲥⲉ ⲣⲁⲃⲏⲟ ⲙⲟⳅⲅⲁ ⲩ ⲧⲉⳝя ⲏⲉⲧⲩ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] эύ ⳝⲗⲉⲧ)ⲅⲟⲃⲏⲟ ⲧы ⲏⲁⲭⲩύ ⲟⲡⲩⳃⲉⲏⲏⲟⲉ)υⲇυ ⲥⲕⲗⲟⲏυⲥь ⲕ ⲙⲟυⲙ яύцⲁⲙ υ ⲥυⲇυ ⲧⲁⲙ ⲧυⲭⲟ)ⲥыⲏ ⲉⳝⲁⲏⲏⲟⲅⲟ ⲁⳝⲟⲣⲧⲁ)ⲧⲃⲟя ⲙⲁⲧь ⲩⲯⲉ ⲏⲁ ⲥⲃⲟύ ⲕⲣⲉⲥⲗⲟ ⲕⲁⲧⲁⲗⲕⲉ ⲉⲇⲉⲧ ⲕⲟ ⲙⲏⲉ)  [<emoji document_id=5438203928527253097>💀</emoji>]',
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲕⲣⳡ ⳃⲁⲥ ⳝⲩⲇⲩ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲣⲁⲕⲟⲙ ⲥⲧⲁⲃυⲧь)ⲧⲟⲣⲧυⲗⲁ ⲧы ⲉⳝⲁⲏⲏⲁя)ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ эⲧⲩ ⲥⲧⲁⲣⲩⲭⲩ υⲏⲃⲁⲗυⲇⲕⲟύ ⲡⲣⲟⲥⲧⲟ ⲥⲇⲉⲗⲁⲗ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲏⲩⲥ)ⲧы ⲯⲉ ⳃⲁⲥ ⳝⲩⲇⲉⲱь ⲙⲟⲉ ⲅⲟⲃⲏⲟ ⲥ ⲗⲟⲡⲁⲧы ⲉⲥⲧь ⲉⳝⲁⲏⲏⲁя ⲧы ⳝⲗяⲧь ⲧюⲗⲉⲏυⲭⲁ υ ⲧы ⳃⲁⲥ ⲡⲣⲟⲥⲧⲟ ⳝⲩⲇⲉⲱь ⲉⳝⲁⲧьⲥя ⲃⲥⲣⲁⲧьⲥя ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] эээ ⲃⳃ)ⲧы ⲧⲁⲙ ⲃⲟⲟⳝⳃⲉ ⳅⲁⲃⲁⲗυⲥь ⲏⲁⲭⲩύ ⲧы ⳝⲗяⲧь ⲇⲁⲙⳝⲁ ⲉⳝⲁⲏⲏⲁя ⲟⳝⲟⲥⲥⲁⲏⲏⲁя υ ⲩⲏυⲯⲉⲏⲏⲁя ⲙⲟυⲙ ⲭⲩⲉⲙ ⲡⲉⲣⲉⳝυⲧⲁя ⲁⲏⲁⲗьⲏⲟ цⲉⲗυⲏⲇⲣυⲃⲉⲥⲕⲁя ⲏⲉⲃьⲉⳝυⳡⲉⲥⲕⲁя ⲙⲁⲏⲇⲁ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳝⲗυⲁ)ⲧы ⳝⲗяⲧь ⲡⲣⲟⲥⲧⲟ ⲉⳝⲁⲏⲏⲟⲉ ⲃыⲙя)ⲇⲁⲃⲁύ ⲕⲟⲣыⲧⲟ ⲉⳝⲁⲏⲏⲟⲉ ⲥьⲉυⲥь ⲡⲣⲟⲥⲧⲟ ⲥ ⲙⲟⲉⲅⲟ ⲭⲩя ⳡⲙⲟⲱⲏυцⲁ ⲧы ⲉⳝⲁⲏⲏⲁя)ⲧы ⲇⲁⲃⲁύ ⲧⲁⲙ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲏⲉ ⲟⲣυ ⳡⲉⲣⲃяⲕ ⲧы ⳝⲉⲱⲉⲏⲏыύ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲁⲕⲥ-ⲧⲁⲕⲥ)ⲇⲁⲃⲁύ ⲕⲁ ⲧы ⲡⲟύⲇⲉⲱь ⲏⲁⲭⲩύ ⲟⳝьⲉⳝⲁⲏⲏⲁя ⲧы ⲙⲁⲏⲇⲁ ⲕⲟⲧⲟⲣⲁя ⲧⲟⲗьⲕⲟ ⲙⲟⲯⲉⲧ ⲥ ⲙⲟⲉⲅⲟ ⲭⲩя ⲕⲣⲟⲱⲕυ яⳅыⲕⲟⲙ ⲡⲟⲇⲙⲉⲧⲁⲧь)ⲕⲁⲕ ⲡыⲗⲉⲥⲟⲥ ⲉⳝⲁⲏⲏыύ)ⲡыⲗⲉⲥⳝⲟⲣⲏυⲕ ⲉⳝⲩⳡυύ ⲡⲉⲣⲉⲥⲕⲩⳡυύ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲭⲁⲭⲁⲭⲁ)ⲧы ⳝⲗяⲧь ⲟⲡⲟⲥⲥⲩⲙ ⲉⳝⲁⲏⲏыύ ⲥьⲉⳝυⲥь ⳝⲗяⲧь ⲡⲟⲕⲁ ⲙⲟύ ⲭⲩύ ⲏⲁ ⲕⲟⲃⲣⲉ ⲥⲁⲙⲟⲗⲉⲧⲉ ⲏⲉ ⲇⲟⲥⲧυⲅ ⲧⲃⲟⲉⲅⲟ ⲉⳝⲁⲏⲏⲟⲅⲟ ⲁⲏⲁⲗⲁ)ⲧы ⳝⲗяⲧь ⲟⳝⲟⲥⲥⲁⲏⲏⲟⲉ ⲙⲩⲣⲗⲟ)ⲧы ⲯⲉ ⲡⲣⲟⲥⲧⲟ ⳝⲗяⲧь ⲟⲡⲩⳃⲉⲏⲏⲕⲁ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲕⲭⲙ)ⲧы ⲯⲉ ⳝⲗяⲧь ⲡⲣⲟⲥⲧⲟ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⳡⲉⲣⲃь ⲏⲁⲃⲟⳅⲏыύ ⲏⲁⲭⲩύ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲩⲇⲩⲱⲉⲏⲏыύ ⳝⲗяⲧь)ⳅⲁⲭⲗⲉⳝⲏυⲥь ⲧы ⲩⲯⲉ ⲃ ⲙⲟⲉύ ⲙⲟⳡⲉ ⲥⲩⲕⲁ)ⲭыⲭыⲭыⲭ  [<emoji document_id=5438203928527253097>💀</emoji>]',
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲕⲥⲧⲁⲧυ ⲅⲏυⲇⲁ)ⲧы ⳝⲩⲇⲉⲱь ⲥⲃⲟⲉύ ⲙⲁⲙⲕⲟύ ⲏⲁ ⲣыⲏⲕⲉ ⲕⲁⲕ ⲡⲟⲙυⲇⲟⲣⲁⲙυ ⲧⲟⲣⲅⲟⲃⲁⲧь υⲗυ ⲕⲁⲕ?)я ⳡⲟⲧ ⳝⲗяⲧь ⲡⲟⲏяⲧь ⲏⲉ ⲙⲟⲅⲩ)ⳝυⳅⲏⲉⲥⲙⲉⲏ ⲧы ⲭⲩⲉⲃ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲟⲣ)ⲥⲗыⲱ ⲧы ⲏⲁⲭⲩύ ⳝⲗяⲧь ⲭⲟⳝⲟⲧ ⲉⳝⲁⲏⲏыύ)υⲇυ ⲟⲧⲥюⲇⲁ ⲏⲁⲭⲩύ ⲇⲁⲗьⲏⲉύ ⲇⲟⲣⲟⲅⲟύ ⳝⲗяⲧь ⲧⲃⲟⲉ ⲙⲉⲥⲧⲟ ⲏⲁ ⲥⲃⲁⲗⲕⲉ ⲉⳝⲁⲧь ⳅⲁⲃⲁⲗυ ⲏⲁⲭⲩύ ⳝⲗяⲧь ⲥⲃⲟύ ⲙⲩⲥⲟⲣⲟⲡⲣⲟⲃⲟⲇ υ ⲥьⲉⳝυⲥь  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲭⲩⲉⲅⲗⲟⲧυⲏⲁ ⲧы ⳡⲉ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲣⲁⲥⲕⲩⲇⲁⲭⲧⲁⲗⲁⲥь?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲱⲗюⲭⲁ ⲧы ⲉⳝⲁⲏⲁя) ⲧы ⲡⲏⲟυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⳡⲉⲣⲏⲩⳝю ⲇыⲣⲩ ⲥⲇⲉⲗⲁⲗ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲏⲟυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲉⳝⲉ ⲕⲗυⲧⲟⲣ ⲏⲁ ⲧⲃⲟύ ⲩⲉⳝⲥⲕυύ ⲉⳝⲁⲗьⲏυⲕ ⲏⲁⲧяⲏⲩ, ⲱⲁⲗⲁⲃⲁ ⲉⳝⲁⲏⲁя?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲭⲩⲗυ ⲧы ⲙⲟύ ⲭⲩύ υⲅⲏⲟⲣυⲱь ⲕⲟⲏυⲏⲁ ⲉⳝⲁⲏⲁя?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳃⲁⲥ ⲥ ⲙⲟⲉⲅⲟ ⲭⲩя ⳝⲩⲇⲉⲱь ⲕⲣⲟⲱⲕυ яⳅыⲕⲟⲙ ⲟⳡυⳃⲁⲧь) ⲡыⲗⲉⲥⲟⲥ ⲉⳝⲁⲏыύ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲏⲟυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧⲩⲭⲩ ⲡⲟⲇ ⲉⲗⲕⲟύ ⲃ ⲭⲃⲟⲥⲧ ⲇⲟⲗⳝυⲗⲁ ⲡⲟⲕⲁ ⲧы ⲣⲁⲥⲥⲕⲁⳅыⲃⲁⲗⲁ ⲥⲧυⲭυ ⲇⲉⲇⲩ ⲙⲟⲣⲟⳅⲩ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲏⲟυⲙⲁⲉⲱь ⳡⲧⲟ я ⳅⲁⲥⲧⲩⲕⲁⲗⲁ ⲧⲃⲟⲉⲅⲟ ⳝⲁⲧю ⲃ ⲃⲁⲏⲏⲉ υ ⲧⲁⲙ ⲟⲏ ⲉⳝⲁⲗ ⲣⲉⳅυⲏⲟⲃⲩю ⳝⲁⳝⲩ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲏυⲟⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲥⲕⲟⲃⲟⲣⲟⲇⲕⲩ ⲭⲩⲉⲙ ⲡⲟⲥⲁⲯⲩ υ ⳅⲁⲯⲁⲣю ⲕⲁⲕ яύцⲁ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲏυⲟⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉ ⲭⲩⲉⲙ ⲡⲣⲟⳝυⲗⲁ ⲣⲁⲥⲥⲧⲟяⲏⲉυⲉ ⲙⲉⲯⲇⲩ ⲙⲉⲯⲇⲟύ υ ⲯⲟⲡⲟύ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳝⲗяⲧь ⳝⲟяⲧⲥя ⲙⲉⲏя ⲇⲟⲗⲯⲉⲏ υⳝⲟ ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь ⲱⲗюⲭⲁ ⲥⲡυⲇⲟⳅⲏⲁя ⲧы ⲭⲟⲧь ⲡⲟⲏυⲙⲁύ ⳡⲧⲟ ⲇⲉⲗⲁⲧь ⲏⲁⲇⲟ υⲗυ ⲧы ⲥⲟⲃⲥⲉⲙ υⳅ-ⳅⲁ ⲭⲩⲉⲃ ⲅⲟⲗⲟⲃⲩ ⲡⲟⲧⲉⲣяⲗ?  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲏⲁⲭⲩύ ⲏⲉ ⲥⲩύ ⲥⲃⲟύ ⲏⲟⲥ ⲃ ⲃⲁⲅυⲏⲩ ⲥⲃⲟⲉύ ⲙⲁⲙⲕυ ⲧⲁⲕ ⲕⲁⲕ ⲟⲏⲁ ⳅⲁⲏяⲧⲁ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⲥⲗυ ⲏⲉ ⲭⲟⳡⲉⲱь эⲧⲟⲅⲟ ⲃυⲇⲉⲧь υⲇυ ⲇⲣⲟⳡυ ⲏⲁ ⲥⲃⲟⲉ ⲫⲟⲧⲟ ⲡυⲇⲟⲣⲁⲥ ⲅ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲏⲁⲭⲩύ ⲙⲏⲉ ⲡⲟⲇⲗυⳅⲁⲗ ⲃ 45 ⲕⲟⲅⲇⲁ ⲅυⲧⲗⲉⲣ ⲭⲟⲧⲉⲗ ⲃыⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲧь υ ⳅⲁⲥⲧⲣⲉⲗυⲧⲥя ⲩ ⲧⲉⳝя ⳡⲧⲟ ⲥⲟⲃⲥⲉⲙ ⲙⲟⳅⲅⲟⲃ ⲏⲉⲧ? ⲧы ⲏⲁⲭⲩя ⲩ ⲙⲉⲏя ⲭⲩύ ⲟⲧⲥⲟⲥⲁⲗ ⲡⲉⲣⲉⲇ ⲅυⲧⲗⲉⲣⲟⲙ? ⲡυⲇⲟⲣⲁⲥ ?? ⳝⲗяⲧь ⲏⲉ ⲡⲟⳅⲟⲣьⲥя ⲱⲗюⲭⲁ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳝⲗяⲧь ⲙⲟⲉⲅⲟ ⲭⲩя ⲏⲉ ⲃⲥⲟⲥⲧⲟяⲏυυ ⲧⲣⲟⲗυⲧь ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲡυⲇⲟⲣⲁⲥ ⲧы ⲅⲁⲗυⲙыύ ⲭⲩⲉⲥⲁⲥ ⲉьⲩⳡυύ ⲏⲁⲭⲩύ ⲱⲉⲗ ⲟⲧⲥюⲇⲁ ⲭⲩⲉⲧⲩ ⲧⲩⲡⲁя  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲗя ⲧы ⲧы ⲩ ⲙⲉⲏя ⳃⲁⲥ ⲙⲟυ ⲥⲟⲟⳝⳃⲉⲏυя ⲥⲟⲥⲁⲧь ⳝⲩⲇⲉⲱь ⲡⲣяⲙⲟⲙ ⳅⲏⲁⳡⲉⲏυυ ⲥⲟⲥⲁⲧь ⲡⲟⲏυⲙⲁⲉⲱь ⲭⲩⲉⲥⲁⲥ ⲧы ⲅⲁⲗυⲙыύ? υⲗυ ⲏⲉⲧ я ⲧⲉⳝⲉ ⲟⳡⲕⲟ ⲡⲟⲣⲃⲩ υ ⲕυⲏⲩ ⲡⲥⲁⲙ ⲏⲁⲭⲩύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲱⲁⲃⲕⲁ ⲉⳝⲩⳡⲁя ⲕⲟⲅⲇⲁ ⲧы ⲙⲏⲉ ⲡυⲱⲉⲱь эⲧⲟ ⲇⲟⲥⲧⲟⲃⲗяⲉⲧ ⲩⲇⲟⲃⲟⲗьⲥⲧⲃυⲉ/ⲙⲟⲉⲙⲩ ⲭⲩю υ ⲧы ⲡυⲱⲉⲱь ⲡυⳅⲇⲟⲥ ⲉⳝⲁⲏыύ?  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲥⲗыⲱь ⲡυⳅⲇⲟύ ⲥⲃⲟⲉύ ⲏⲉ ⲃⲉⲗяύ υⲗυ ⲧⲉⳝⲉ ⲃ ⲩⲭⲟ ⲭⲩύ ⲥⲩⲏⲩьь ⳡⲧⲟ ⳝ ⲧы ⲥⲃⲟю ⲙⲁⲧь ⲥⲗыⲱⲁⲗ ⲕⲁⲕ ⲟⲏⲁ ⲟⲣⲉⲧ ⲡυⲇⲟⲣ ⲉⳝⲁⲏыύ?  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲁⳡⲉⲙ ⲡⲟⲕⲁⳅыⲃⲁⲉⲱь яⳅыⲕⲟⲙ ⲏⲁ ⲙⲟύ ⲭⲩύ υ ⲕυⲃⲁⲉⲱь ⲅⲟⲗⲟⲃⲟύ ⳡⲧⲟ ⲭⲟⳡⲉⲱь ⲡⲟ ⳝыⲥⲧⲣⲉⲉ ⲉⲅⲟ ⲥⲟⲥⲏⲩⲧь ⲧы ⳡⲧⲟ ⲙⲟⲗ ⲧⲁⲕⲟύ ⲡυⲇⲣ? ⲭⲩⲉⲥⲁⲥ ⲉⳝⲁⲏыύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳝⲗяⲧь ⲡⲟⲕⲁⲯυ ⲙⲏⲉ ⲭⲟⲧь ⲟⲇⲏⲩ ⲧⲃⲟю ⲇыⲣⲕⲩ ⲕⲟⲧⲟⲣⲩю я ⲉⳃⲉ ⲏⲉ ⲉⳝⲁⲗ ⲧы ⲯⲉ ⲏⲁⲭⲩύ ⲕⲟⲏⳡⲉⲏⲏыύ ⲭⲩⲉⲥⲁⲥ ⲟⲇⲏⲁⲕⲟ ⲏⲉ ⲧⲁⲕ ⲗυ? ⲧы ⲥⲟⲥⲁⲧь ⲩⳡυⲥь  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲕⲟⲅⲇⲁ-ⲧⲟ ⲙⲏⲉ ⲅⲟⲃⲟⲣυⲗ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲇⲗя ⲧⲉⳝя цⲁⲣь ⲁ ⲧⲃⲟύ яⳅыⲕ цⲁⲣⲉⲃⲏⲁ ⲏⲁⲭⲩύ ⲧы ⲧⲁⲕⲟύ ⲉⳝⲁⲏⲩⲧыύ ⳅⲁⲇⲁⲗⲥя?   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳝⲗяⲧь ⲧы ⲩⲏыⲗⲁя ⲭⲩύⲏя ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲧⲉⳝя ⲟⲇυⲏ ⲏⲁ ⲟⲇυⲏ ⲣⲁⳅⲟⲣⲃⲉⲧ ⲡυⲇⲟⲣ ⲧы ⲕⲟⲏⳡⲉⲏⲏыύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲕⲁⲣⲟⳡ ⲏⲁⲭⲩύ ⲧы ⳃⲁⲥ ⲡⲟⲇⲥⲟⲥⲁⲧь ⲙⲏⲉ ⲭⲟⳡⲉⲱь?ⲇⲩⲙⲁⲉⲱь я ⲧⲉⳝⲉ ⲭⲩύ ⲃ ⲣⲟⲧ ⲏⲉ ⲥⲩⲏⲩ ⲡυⲇⲟⲣⲁⲥ?  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲯⲉ ⲧⲉⳝⲉ ⲃ ⲣⲟⲧ ⲕⲟⲏⳡⲩ ⲡυⲇⲟⲣ ⲧы ⲩⲏыⲗыύ ⲏⲩ ⲕⲁ ⲥюⲇⲁ υⲇυ ⲡⲟⲕⲁ ⲙⲟύ ⲭⲩύ ⲏⲉ ⳅⲁⲃⲁⲗ ⲟⲧ ⲡυⳅⲇы ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲧы ⲯⲉ ⲙⲏⲉ ⲉⳃё ⳅⲁ ⲇⲉⲕⲁⳝⲣь ⲙυⲏⲉⲧ ⲏⲉ ⲥⲇⲉⲗⲁⲗ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲙⲏⲉ ⲕⲟⲅⲇⲁ ⲥⲟⲥⲁⲧь/ ⳝⲩⲇⲉⲱь? ⲡυⲇⲟⲣⲁⲥ ⲧы ⲉⳝⲁⲏыύ ⲧы ⲙⲏⲉ ⲏⲁⲭⲩύ ⲙⲟю ⲙⲟⳡⲩ ⲡυⲧь ⳝⲩⲇⲉⲱь ⲡⲟⲕⲁ я ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲧь  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲥⲗыⲱυⲱь/ⲧы ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ я ⳃⲁⲥ ⲏⲁⳡⲏⲩ ⲕⲟⲏⳡⲁⲧь ⲧы ⳝⲩⲇⲉⲱь ⲡⲣυⲏⲉⲙⲁⲧь ⲡⲟⲣцыю ⲥⲡⲉⲣⲙ ⲡυⲇⲟⲣⲁⲥⲁ ⲕⲩⲥⲟⲕ υⲗυ ⲧⲉⳝя ⲃыⲉⳝⲁⲧь цыⲣⲕⲩⲗⲉⲙ ⳡⲧⲟ ⲧⲉⳝⲉ ⲏⲉ ⲡⲣυⲱⲗⲟⲥь ⲡυⲧь ⲥⲡⲉⲣⲙⲩ?  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲏⲁⲭⲩύ ⲟⲡⲩⲥⲧυⲗⲥя ⲇⲟ ⲙⲟⲉⲅⲟ ⲭⲩя ⲕⲁⲕ ⳝыⲃⲱυύ ⲭⲩⲉⲥⲁⲥ юⲙⲁⲣυⲥⲧⲟⲃ ⲉⳝⲁⲧь ⲧы ⳡⲙⲟ ⲧы ⲏⲁⲭⲩύ ⲙⲟⲉⲅⲟ ⲭⲩя ⲏⲉ ⲇⲟⲥⲧⲟⲉⲏ ⲕⲁⲕ υ ⲙⲟⲉⲅⲟ ⲧⲣⲟⲏⲁ ⲡυⳅⲇⲁⲅⲣыⳅ ⲏⲁⲭⲩύ ь  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲏⲁⲭⲩύ ⲕⲟⲅⲇⲁ ⲏⲉ ⳅⲏⲁⲉⲱь ⲥⲃⲟύ ⲭⲩύ ⲡⲣυⳡⲙⲟⲕυⲃⲁⲉⲱ υ ⲅⲟⲃⲟⲣυⲱь/ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲧⲟⲯⲉ ⲡⲣυⳡⲙⲟⲕⲏⲉⲱь? ?ⳝⲗяⲧь ⲡυⲇⲟⲣ ⲧы ⲅⲁⲗυⲙыύ υⲇυ ⲟⲧⲥюⲇⲁ υ ⲉⳝυ ⲥⲃⲟю ⲙⲁⲧь ⲡυⳅⲇ ⲉⲉ ⲡυⳅⲇⲉ ⲟⲗ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲏⲁⲭⲩύ υⲇυ ⲟⲧⲥюⲇⲁ ⲡⲟⲕⲁ ⲙⲟύ ⲭⲩύ ⲏⲏ ⲡⲟⲕⲁⳅⲁⲗ ⲥⲉⳝя ⲃ ⲇⲉⲗⲉ υⳝⲟ ⲧⲃⲟя ⲙⲁⲧь ⲥⲡυⲇⲟⳅⲏⲁя ⲱⲗюⲭⲁ ⲕⲁⲕ я υ ⳅⲏⲁⲗ я ⲇⲉ ⲉⲉ ⲭⲩⲉⲙ ⲡυⳅⲇυⲗ ⲧы ⳅⲏⲁⲗ?  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲁⲕ ⲧⲉⳝя ⲏⲁⳡⲏⲉⲙ ⲉⳝⲁⲧь ⲡⲁцⲉⲉⲏⲧ ⲧⲉⳝя ⲃыⲉⳝⲩ υ ⳝⲩⲇⲩ ⲇⲣⲁⲧь/ⲧⲉⳝя ⲕⲁⲕ ⲅⲣяⳅⲏⲩю ⲱⲗюⲭⲩ ⲡⲟⲏυⲙⲁⲉⲱь? ⲡυⲇⲣⲁⲥ ⲧы ⳝⲗяⲧь ⲕⲟⲅⲇⲁ ⲙⲏⲉ ⲥⲟⲥⲁⲧь ⳝⲩⲇⲉⲱь ⲧы ⲭⲟⲧь ⲡⲣυⳡⲙⲟⲕυⲃⲁύ ⲭⲩⲉⲥⲁⲥ ⲧы ⲡυⳅⲇⲁⲗⲩⲡыύ ⲉⳝⲁⲧь ⲧⲉⳝя ⲏⲁⲇⲟ ⲭⲇ  [<emoji document_id=5438203928527253097>💀</emoji>]',
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳝⲗяяя я ⲧⲩⲧ ⲡⲟⲏяⲗ ⳅⲁⳡⲉⲙ ⲧⲉⳝя ⲉⳝⲁⲧь ⲃⲟⲧ ⲥⲙⲟⲧⲣυ ⲡⲟⲙⲏυⲱь ⲕⲁⲕ ⲧы ⲙⲏⲉ ⳅⲁ ⲥⲃⲟύ ⲟⲧⲥⲟⲥ ⲏⲉ ⲡⲗⲁⲧυⲗ? ⲧы ⲡыⲧⲁⲗⲥя ⲙⲏⲉ ⲥⲇⲉⲗⲁⲧь ⲟⲧⲥⲟⲥ ⳅⲁ ⲕⲣⲉⲇυⲧ? ⲡⲟⲏυⲙⲁⲉⲱь? ⳝⳝⲗя ⲧы ⲣυⲗυ ⲇⲩⲙⲁⲉⲱь ⲃыⲃⲉⳅⲉⲱь ⲙⲉⲏя? ⲭⲩⲉⲥⲁⲥ ⲧы ⲉⳝⲁⲏыύ ⲡυⲇⲟⲣⲁⲥ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲥⲗыⲱυⲱь ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲕⲁⲕ ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗυ ⲥⲧυⲗⲉⲙ ⲯⲩⲣⲁⲃⲗя? ⲡⲟⲙⲏυⲱь ⲕⲁⲕ ⲟⲏⲁ ⲥⲧⲁⲏⲁⲗⲁ ⲏⲁⲭⲩύ ⲥⲩⲃⲁⲗⲁ ⲥⲃⲟю ⲅⲟⲗⲟⲃⲩ ⲃ ⳅⲉⲙⲗю ⲉⳝⲁⲧь я ⲧⲟⲅⲇⲁ ⲟⲣⲁⲗ ⲩⲭⲭⲭⲁ ⲕⲁⲕ ⲱⲁⲥ ⲏⲁⲇ ⲧⲟⳝⲟύ ⲕⲁⲕ ⲣⲃⲩⲧ ⲧⲉⳝⲉ ⳃⲉⲕⲩ ⲙⲟυⲙ ⲭⲩⲉⲙ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳝⲗяⲧь ⲧы ⳡⲉ ⲏⲁⳅⲩύ ⲏⲁⲭⲩύ ⲁⲭⲩⲉⲗⲁ ⲡυⳅⲇⲁⲗυⳅⲕⲁ ⲉⳝⲁⲏⲁя ⲧⲉⳝя ⳡⲧⲟ ⲏⲁⲭⲩύ ⲉⳝⲁⲧь ⲉⲁⲕ ⲱⲗюⲭⲩ ⲇⲣⲁⲏⲩⳝ υⲗυ ⳡⲧⲟ ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲇⲁ я/ⲧⲉⳝя ⲉⳝⲁⲧь ⲕⲁⲕ ⲱⲗюⲭⲩ ⳝⲩⲇⲩ ⲡυⲇⲟⲣⲁⲥ ⲧы ⲉьⲁⲏыύ ⲏⲁⳅⲩύ ⲡⲟⲱⲉⲗ ⲡⲉⲧⲩⲭ ⲇⲣⲁⲏⲏыύ я ⲯⲉ ⲏⲁⲭⲩύ ⲉⳝⲁⲧь ⲧⲉⳝя ⳝⲩⲇⲩ ⲡⲟⲙⲏυⲱь ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁⳡⲁⲗⲁ ⲥⲟⲥⲁⲧь ⲙⲏⲉ ⲭⲩύ υ ⲡⲟⳝⲉⲯⲁⲗⲁ ⲃ ⲧⲩⲁⲗⲉⲧ ⲃⲟ ⲃⲣⲉⲙя ⲕⲟⲅⲇⲁ ⲩ ⲧⲉⳝя ⲡⲟⲏⲟⲥυⲗ υ ⲧы ⲏⲁⲥⲣⲁⲗ ⲏⲁ ⲥⲃⲟю ⲙⲁⲧь ⲁ ⲟⲏⲁ ⳅⲁ эⲧⲟ ⲧⲉⳝя ⲉⲣⲱυⲕⲟⲙ ⲃыⲉⳝⲁⲗⲁ ⲡⲟⲙⲏυⲱь ⲧы ⲯⲉ ⲏⲁⲭⲩύ ⲏⲉⲕⳡⲉⲙⲏыύ ⲡυⲇⲟⲣⲁⲥ ⲧⲉⳝя ⲙⲁⲗⲟ ⲃыⲉⳝⲁⲧь υ ⲧы ⲉⳃё ⲡыⲧⲁⲉⲱьⲥя ⳡⲧⲟ ⲧⲟ ⲡυⲥⲁⲧь ⲭⲩⲉⲥⲁⲥ ⲧы ⲉⳝⲁⲏыύ )ⲡⲟⲙⲏυⲱь ⲕⲁⲕ ⲩⳡⲉⲏыⲉ ⲏⲁⲱⲗυ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲕⲙ ⲕⲟⲥⲧь ⲇυⲏⲟⳅⲁⲃⲣⲁ? ⲧы ⲏⲁⲭⲩύ ⲙⲟⲉⲅⲟⲭⲩя ⲏⲉ ⲥⲧⲟυⲱь ⲡⲣυⳡⲉⲙ ⲧⲩⲧ ⲧⲃⲟύ ⲟⲧⲥⲟⲥ ⲉⳝⲁⲏыύ ⲧы ⳅⲩⲏⲥⲁⲁ ⲧы ⲩ ⲙⲉⲏя ⳝⲉⲥⲡⲗⲁⲧⲏⲟ ⲥⲡⲁⲥⲁⲧь ⲇⲟⲗⲯⲉⲏ ⲡⲟⲏυⲙⲁⲉⲱь ⲭⲩⲉⲥⲁⲥ ⲧы ⲉⳝⲁⲏыύ ⲃ ⲣⲟⲧ ⲧы ⳝⲗяⲧь ⲡⲉⲧⲩⲭ ⲉⳝⲁⲏыύ ⲡⲟⲱⲉⲗ я ⲧⲉⳝⲉ ⲅⲟⲃⲟⲣⳝ ⲏⲁ ⲭⲩύ ⲡυⲇⲟⲣⲁⲥ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲥⲗыⲱь ⲧы ⲡυⲇⲟⲣⲁⲥ ⲧы ⲙⲉⲏя ⲏⲉ ⳅⲁⲧⲣⲟⲗυⲱь υⳝⲟ ⲧы ⲭⲩύ ⲙⲏⲉ яⳅыⲕⲟⲙ ⲙⲟⳅⲟⲗυⲱь, я ⲉⳝⲁⲗ ⲧⲉⳝя ⲃ ⲣⲟⲧ ⲧⲁⲕ ⳡⲧⲟ υⲇυ ⲏⲁⲭⲩύ ⲉⳝⲁⲏыύ ⲃ ⲣⲟⲧ) ⲉⳝⲁⲗυ ⲧⲉⳝя ⳡⲩⲣⲕυ ⲧы ⲉⳃё ⲭⲟⳡⲉⲱь ⲙⲏⲉ ⳡⲧⲟ ⲧⲟ ⲡυⳅⲇⲉⲧь? ⲭⲩⲉⲥⲁⲥ ⲧы ⲉⳝⲁⲏыύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳡⲉ ⲉⳝⲁⲧь ⲁⲭⲩⲉⲗⲁ ⲏⲁⲭⲩύ ⲡυⲇⲟⲣⲁⲥⲕⲁ ⲏⲁⳅⲩύ ⳃⲁⲥ ⲙⲟύ ⲭⲩύ ⲃⲥυⲁⲏⲉⲧ ⲁ ⲧы ⲗяⲯⲉⲱь ⲡⲟⲏυⲙⲁⲉⲱь? ⲭⲩⲉⲥⲁⲥ ⲉьⲁⲏыύ ⲧы ⲙⲟύ ⲭⲩύ ⲥⲟⲥⲁⲧь ⳝⲩⲇⲉⲱь ⲕⲁⲕ ⲏυⲕⲧⲟ ⲇⲣⲩⲅⲟύ ⲡυⲇⲟⲣⲁⲥ ⲧы ⲉⳝⲁⲏыύ ⳝⲗяⲧь ⲡⲉⲧⲩⲭ ⲥⲩⲕⲁ ⲏⲁⲭⲩύ υⲇυ я ⲏⲁⲭⲩύ ⲏⲁⳡⲏⲩ ⲧⲉⳝя ⲉⳝⲁⲧь υ ⲇⲁⲯⲉ ⲏⲉ ⲡυⲕⲏⲩ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲱⲗюⲭⲁ ⲉⳝⲁⲧь ⲡυⲱυ ⲏⲟⲣⲙⲁⲗьⲏⲟ ⲧы ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя ⲡυⲱⲉⲱь ⲡⲟⲏυⲙⲁⲉⲱь? ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲧы ⳝⲗяⲧь ⲏⲁ ⲙⲟύ ⲭⲩύ ⲁⲅⲣ ⲥⲃⲟύ ⲏⲉ ⲟⲧⲡⲩⲥⲕⲁύ ⲉⳝⲁⲏыύ ⲃ ⲣⲟⲧ ⲡⲉⲧⲩⲭ ⲧы ⲉⳝⲁⲏыύ ⲉⳝⲁⲗυ ⲧⲉⳝя ⲡⲥы ⲏⲁⲭⲩύ ⲡυⲇⲟⲣⲁⲥ ⲧы ⲅⲁⲗυⲙыύ ⲭⲩⲉⲥⲁⲥ ⲉⳝⲁⲏыύ ⲡⲉⲣⲉⲃⲁⲣυⲃⲁύ ⲃⲥⲉ ⳡⲧⲟ я ⲡυⲱⲩ ⲡυⲇⲣ ??  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲥⲗыⲱυⲱь ⲧы ⲯυⲃⲟⲧⲏⲟⲉ ⲧⲉⳝя ⳃⲁⲥ ⳝⲟⲅⲁⲧыⲣь ⲃ ⲯⲟⲡⲩ ⲇⲣⲁⲧь ⳝⲩⲇⲉⲧ ⲡⲟⲏυⲙⲁⲉⲱь? ⲭⲩⲉⲥⲁⲥ ⲧы ⲉⳝⲁⲏыύ я ⲧⲉⳝя ⲉⳝⲁⲧь ⲃыⲉⳝⲩ ⲕⲁⲕ ⲱⲗюⲭⲩ ⲥⲡυⲇⲟⳅⲏⲩю ⲏⲁⲭⲩύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳝⲗяⲧь ⲉⳝⲁⲧь ⲧⲉⳝя ⳅⲁ ⳃⲉⲕⲩ ⲧы ⳡⲧⲟ ⲏⲁⲭⲩύ ⲡⲉⲣⲉⲇⲟⲙⲏⲟύ ⲩⲏυⲯⲁⲉⲱьⲥя? ⲡυⲇⲟⲣⲁⲥ ⲏⲁⲭⲩύ ⲧⲉⳝя ⳡⲧⲟ ⲃыⲉⳝⲁⲧь? ⳡⲧⲟ ⲗⲉ? ⲭⲩⲉⲥⲁⲥ?  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲉⳝⲁⲧь ⲕⲟⲅⲇⲁ ⲃ ⳅⲉⲣⲕⲁⲗⲟ ⲥⲙⲟⲧⲣю ⲃυⲯⲩ ⲧⲃⲟⲉ ⲉⳝⲁⲏⲟⲉ ⲗυцⲟ ⲃ ⲥⲡⲉⲣⲙⲉ ⲡⲟⲏυⲙⲁⲉⲱь? ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ? я ⲧⲉⳝя ⲉⳝⲁⲧь ⳝⲩⲇⲩ ⲕⲁⲕ ⲱⲗюⲭⲩ ⲉⳝⲁⲏⲩю ?? ⲧы ⲏⲉ ⲡⲟⲏυⲙⲁⲉⲱь ⲡⲟⲭⲟⲇ?  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳝⲗя ⲉⳝⲁⲧь ⲧы ⲏⲁⲭⲩύ ⲭⲩⲉⲡⲗⲉⲧ ⲧы ⳡⲧⲟ ⲉⳝⲁⲧь ⲭⲩяⲙυ ⳅⲁⳃυⳃⲁⲉⲱьⲥя? ⲡυⲇⲟⲣⲁⲥ ⲏⲁⲭⲩύ ⲱⲉⲗ ⲟⲧⲥюⲇⲁ ⲉⳝⲁⲧь ⲧⲉⳝя ⳃⲁⲥ ⲏⲁⳡⲏⲩ ⲏⲁⲭⲩύ ?? ⳝⲗя ⲙⲏⲉ ⲡⲟⲭⲩύ ⲏⲁ ⲧⲉⳝя ⲇⲯ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲏⲁⲭⲩύ ⲕⲟⲏⲃⲉⲥⲕⲩю ⲧⲃⲟύ ⲣⲟⲧ υ ⳅⲁⲥⲧⲁⲃⲗю ⲥⲟⲥⲁⲧь ⲡⲟⲏяⲧυⲉ υⲙⲉⲉⲱь? я ⲧⲃⲟύ ⲭⲩύ ⲃ ⲙяⲥⲟⲣⲩⳝⲕⲩ ⲥⲩⲃⲁⲧь ⳝⲩⲇⲩ ⲁ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ ⲏⲁ ⲙⲟύ ⲭⲩύ) ⲡυⲇⲟⲣⲁⲥ ⲧы ⲉⳝⲁⲏыύ ⲟⲇⲏⲁⲕⲟ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲏⲁⲭⲩύ ⲡⲣⲟⲥⲧⲟⲉⲗю ⲧⲉⳝⲉ ⲅⲟⲗⲟⲃⲩ ⲥⲡⲉⲣⲙⲟύ ⲧⲃⲟⲉⲅⲟ ⲇⲉⲇⲁ ⲡⲟⲏυⲙⲁⲉⲱь? ⳝⲗяⲧь ⲧⲁⲕυⲭ ⲕⲁⲕ ⲧы ⲡυⲇⲟⲣⲁⲥⲟⲃ ⲧⲟⲗьⲕⲟ ⲉⳝⲁⲧь ⲏⲁⲇⲟ ?? я ⲧⲉⳝя ⲃ ⲇⲟⳝⲁⲃⲟⲕ ⲉⳝⲁⲧь ⳝⲩⲇⲩ ⲡⲟⲏυⲙⲁⲉⲱь? ⲭⲩⲉⲥⲁⲥ ⲉⳝⲁⲏыύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳝⲗя υⲇυ ⲕⲁ ⲧы ⲏⲁⲭⲩύ ⲡυⲇⲟⲣⲁⲥ ⲅⲁⲗυⲙыύ я ⲧⲉⳝя ⲏⲁⲭⲩύ ⲉⳝⲁⲧь ⳝⲩⲇⲩ ⲡⲟⲏυⲙⲁⲉⲱь? ⲙⲏⲉ ⲃⲁⲱⲉ ⲡⲟⲭⲩύ ⲏⲁ ⲧⲃⲟυ ⲱⲗюⲭⲁⲏⲥⲕυⲉ ⲕⲟⲙⲡⲗⲉⲕⲥы  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] υⲇυ ⲏⲁ ⲭⲩύ) ⳝⲩⲇⲩ я ⲉⳝⲁⲏⲏⲟⲙⲩ ⳝυⳡⲩ ⲇⲟⲕⲁⳅыⲃⲁⲧь) ⲥⲩⲕⲁ υⲇυ ⲡⲣⲟⲇⲁⲃⲁύ ⲥⲃⲟю ⲙⲁⲧь, ⲉⲉ ⲡⲟ ⲩⲅⲗⲁⲙ ⲉⳝⲩⲧ ⲃυⲇⲏⲟ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲉⳝⲁⲧь ⲧⲉⳝя ⳡⲁύⲏυⲕⲟⲙ ⳝⲩⲇⲩ ⲉⲥⲗυ ⲧы ⲏⲉ ⳅⲁⲧⲕⲏⲉⲱьⲥя υ ⲏⲉ ⳝⲩⲇⲉⲱь ⲡυⳅⲇⲉⲧь ⲭⲩύⲏю ⲃⲥяⲕⲩю ⲡⲟⲏяⲧυⲉ ⲩ ⲧⲉⳝя ⲉⲥⲧь ⲡυⲇⲣⲁⲥ? я ⲧⲉⳝя ⲏⲁⲭⲩύ ⲉⳝⲁⲧь ⳝⲩⲇⲩ ⲡⲟⲏυⲙⲁⲉⲱь? ??  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲭⲩⲉⲥⲟⲥ ⲉⲧы ⲉⳝⲁⲏⲏыύ ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲥⲩⲕⲁ ⲩ ⲧⲉⳝя ⲏⲁ ⲅⲟⲗⲟⲃⲉ ⲡⲉⲧⲩⲱⲏя ⲧы ⳡⲉ ⲙⲉⲏя ⲃыⲙⲟⲣⲁⲯⲧⲃⲙⲃⲉⲱь ⲭⲩⲉⲥⲟⲥ ⲉⳝⲩⳡυύ,ⳝⲗяⲧь ⳅⲁⲃⲁυⲗ ⲉⳝⲗⲗⲟ ⲭⲩⲉⲥⲟⲥ ⲉⲁⲁⳝⲏⲏыύ ⲥⲃⲟυ ⲥⲕⲣυⲏы ⲟⲧцⲩ ⲃ ⲯⲟⲡⲩ ⳅⲁⲥⲩⲏⲉⲱь) ⲡυⲇⲟⲣⲁⲥ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲭⲩύⲏя ⲉⳝⲁⲏⲏⲁя ⲥⲙⲟⲧⲣυ ⲕⲁⲕⲁя ⳝⲟⲙⳝⲁ ⳃⲁⲥ ⲩⲡⲁⲇⲉⲧ ⲏⲁ ⲉⳝⲗⲟ ⲧⲃⲟⲉ, ⲭⲩⲉⲥⲟⲥ ⲉⳝⲗυⲃыύ я ⲧⲉⳝя ⲃыⲉⳝⲩ ⲣⲁⲕⲟⲙ ⲧы ⳡⲉ ⲃⳅъⲉⳝыⲃⲁⲉⲱьⲥя, я 1 ⲥυⲯⲩ ⲭⲩⲉⲥⲟⲥ ⲉⳝⲩⳡυύ, я ⲯ ⲏⲉ ⲇⲟⲗⳝⲟⲉⳝ ⲕⲁⲕ ⲧы ⳡⲧⲟⳝ ⲇⲁⲃⲁⲧь ⲡⲣⲟⲫυⲗь ⲥⲃⲟύ ⲕⲟⲙⲩ-ⲧⲟ, ⲇⲩⲣⲁⲗⲉύ ⲥⲩⲕⲁ ⲉⳝⲩⳡυύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲥⲗыⲱь ⲙⲩⲇυⲗⲁ ⲉⲇⲁⲏⲁя ⲏⲁⲭⲩύ ⲟⲧⲟⲱⲗⲁ ⲡυⳅⲇⲁ ⲉⲇⲁⲏⲃя ⲏⲁⲭⲩύ я ⲧⲉⳝⲉ ⲥⲕⲁⳅⲁⲗ ⲡⲟⲱⲉⲗ ⲡⲟⲕⲁ ⲙⲟύ ⲭⲩύ ⲏⲉ ⲡⲣⲟⲱⲉⲗⲥя ⲡⲟ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ ⲡⲟⲏυⲙⲁⲉⲱь? ⲭⲩⲉⲥⲁⲥ ⲉⳝⲁⲏыύ ⲡυⲇⲟⲣⲁⲥ ⲕⲕⲟⲏⳡⲉⲏⲏыύ ⲡⲟⲙⲏυⲱь ⲕⲁⲕ ⲧⲉⳝя ⲙⲁⲧь ⲩⳡυⲗⲁ ⲥⲟⲥⲁⲧь ⲙⲏⲉ ⲭⲩύ? эⲧⲟ ⲯⲉ цⲉⲗⲁя υⲥⲧⲣⲟя ⲏⲁⲭⲩύ ⲧы ⳝⲗя ⲕⲁⲕ ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲭⲇ  [<emoji document_id=5438203928527253097>💀</emoji>]',
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳝⲗяⲧь ⲧⲉⳝя ⲏⲁⲭⲩύ ⲃ ⲣⲟⲧ ⲉⳝⲁⲧь ⲏⲁⲇⲟ ⳅⲁ ⲧⲃⲟυ ⲉⳝⲁⲏыⲉ ⲡⲟⲇⲥⲣⲥⲏыⲉ ⲥⲗⲟⲃⲁ ⲭⲩⲉⲥⲁⲥ ⲧы ⲏⲁⲭⲩύ ⲕⲟⲅⲇⲁ ⲙⲏⲉ ⲭⲩύ ⲥⲟⲥⲉⲱь ⲧы ⲇⲩⲙⲁⲉⲱь ⲧⲟⲗьⲕⲟ ⲟ ⲙⲟⲉⲙ ⲭⲩⲉ ⲡⲟⲏяⲗ ?ⲧы ⳝⲗяⲧь ⲡυⲇⲁⲣⲟⲕ ⲉⳝⲁⲏыύ ⲉⳝⲁⲧь ⲧы ⲗⲟⲭ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳝⲗя ⲧы ⳝⲗяⲧь ⲇⲩⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲗⲩⳡⲱⲉ ⲧⲉⳝя ⲥⲟⲥⲉⲧ? ⲇⲁ ⲧы ⲱⲁⲗⲟⲉⳝ ⲧы ⲏⲁⲭⲩύ ⲡⲟⲇⲥⲁⲥыⲃⲉⲱⳝ ⲃⲥⲉ ⳡⲧⲟ ⲇⲃυⲯⲉⲧⲥя ⲭⲩⲉⲥⲁⲥ ⲧы ⲕⲟⲏⳡⲉⲏⲏыύ ⲧы ⲏⲁⲭⲩύ ⲥⲟⲥⲁⲧь ⲧⲟⲗьⲕⲟ ⲩⲙⲉⲉⲱь ⲡυⲇⲣ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲥⲗыⲱь ⲱⲉⲗ ⲟⲧⲥюⲇⲁ ⲕⲩⲣⲃⲁⲕ ⲉⳝⲁⲏыύ ⲁⲧⲟ ⲏⲁⳡⲏⲩ ⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲧь υ ⲕⲟⲏⳡⲁⲧь ⲉύ ⲃ ⲣⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь я ⲕⲟⲅⲇⲁ ⲧⲟ ⲉⳝⲁⲗ ⲉύ ⲃ ⲣⲟⲧ υ ⲏⲁⲱⲉⲗ ⳅⲟⲗⲟⲧⲟ ⲡυⲇⲟⲣⲁⲥ ⲧы ⲅⲁⲗυⲙыύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳝⲗяⲧь ⲕⲣⲟⲙⲉ ⲕⲁⲕ ⲥⲟⲥⲁⲧь ⲙⲏⲉ ⲏυⳡⲉⲅⲟ ⲏⲉ ⲩⲙⲉⲉⲱь? υⲗυ ⲧⲉⳝⲉ ⲡυⳅⲇⲩ ⲣⲃⲁⲧь? ⳡⲧⲟⳝ ⲧⲃⲟя ⲙⲁⲧь ⳅⲁⲃυⲇⲟⲃⲁⲗⲁ ⲧⲉⳝⲉ ?ⲡυⲇⲟⲣⲁⲥ ⲧы ⲏⲁⲭⲩύ ⲙⲏⲉ ⲏⲁⲡυⲥⲁⲗ ⳡⲧⲟ ⲧы ⲭⲩυ ⲥⲟⲥⲉⲱь? ⳡⲙⲟ ⲉⳝⲁⲏⲟⲉ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲏⲁⲭⲩύ ⲙⲏⲉ ⲭⲩύ ⲥⲟⲥⲉⲱь? ⳝⲗяь я ⲣυⲗυ ⲅⲟⲃⲟⲣⳝ ⲧы ⲡυⲇⲟⲣ ⲧы ⲇⲁⲯⲉ ⲥⲃⲟю ⲙⲁⲧь ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⳅⲁⳃυⲧь ⲏⲉ ⲃⲥυⲗⲁⲭ ⲡⲟⲏυⲙⲁⲉⲱь ⲡυⲇⲟⲣ ⲧы ⲉⳝⲁⲏыύ ⲧы ⲏⲁⲭⲩύ ⲡⲟⲇⲥⲁⲥыⲃⲉⲱь ⲙⲏⲉ ⲭⲩύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳝⲗяⲧь ⲡυⳅⲇⲁⲅⲣыⳅ ⲉⳝⲁⲏыύ ⳝыⲥⲧⲣⲟ ⲃⲥⲁⲥⲁⲗ ⲃⲥⲉ ⳡⲧⲟ я ⲧⲉⳝⲉ ⲡυⲱⲩ ⲡυⲇⲣⲁⲥ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲕⲟⲏⳡⲉⲏⲁя ⲱⲗюⲭⲁ υ ⲧы ⲙⲏⲉ ⲏⲁⲭⲩύ ⲭⲩύ ⲥⲟⲥⲉⲱь ⲡⲣυ эⲧⲟⲙ ⲡυⲇⲟⲣ ⲧы ⲉⳝⲁⲏыύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡυⳅⲇⲁⲕⲣыⲗ ⲉⳝⲩⳡυύ) ⲏⲉⲭⲩя ⲏⲉ ⲥⲙⲟⲅ) ⲏⲁⲱⲉⲗⲥя ⲧⲩⲧ ⲧⲣⲟⲗⲗь ⲭⲩⲉⲃ)) ⲧⲉⲣⲡυⲗⲁ ⲉⳝⲁⲏⲏⲁя)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲙⲱυ ⲧⲁⲕⲟύ ⲟⲅⲣⲙⲟⲏыύ ⲡυⳅⲇⲉц) ⲕⲁ ⲧы ⳃⲁⲥ ⲡⲣⲟⲃⲁⲗυⲱьⲥя ⲧⲩⲇⲁ ⲇⲟⲗⳝⲟⲉⳝ ⲉⳝⲁⲏⲏыύ ⳝⲩⲇь ⲁⲕⲕⲕⲩⲣⲁⲧⲉⲏ ⲭⲩⲉⲥⲟⲥ ⲉⲁⳝⲏⲏыύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲭⲩⲉⲥⲟⲥ ⲉⳝⲁⲏⲏыύ ⳝⲗяⲧь ⲧы ⳡⲉ ⲧⲁⲙ ⲡυⲱⲉⲱь ⲃⲥⲉ ?) ⲭⲩⲉⲥⲟⲥ ⲉⳝⲁⲏыύ) ⲏⲉⲥⳡⲁⲥⲏыύ ⲡⲉⲧⲩⲭ ⲥⲩⲕⲁ))) ⲱⲁⳝⲗⲟⲏυⲧь ⲩⲯⲉ ⲏⲁⳡⲁⲗ?) ⲏⲉ ⲭⲩя ⲏⲉ ⲃыⲃⲟⳅυⲱь ⲇⲁ ?)?) ⲡⲉⲧⲩⲭ ⲉⳝⲁⲏⲏыύ) ⲉⳝⲁⲗ ⲧⲉⳝя ⲏⲁ ⲏⲟⲅⲁⲭ ⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ, ⲥыⲏ ⲱⲁⲗⲁⲃы) ⲥⲩⲕⲁ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳝⲗя ⲧы ⲅⲗⲁⲃⲏⲟⲕ ⲡⲟ ⳡⲁⳃⲉ ⲙⲏⲉ ⲥⲟⲥυ ⲁⲧⲟ ⲙⲏⲉ ⲥⲧⲣⲁⲱⲏⲟ ⲃⲇⲣⲩⲅ ⲏⲁⳡⲏⲉⲱь ⲉⳝⲁⲧь ⲥⲃⲟю ⲙⲁⲙⲕⲩ ⲇⲟ ⲡⲟⲧⲉⲣυя ⲥⲟⳅⲏⲁⲏυя ⲡⲟⲏυⲙⲁⲉⲱь? ⲭⲩⲉⲥⲁⲥ ⲧы ⲟⳝⲇⲟⲗⳝⲁⲏыύ ??  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲏⲁⲭⲩύ ⲭⲩⲉⲥⲁⲥ ⲕⲟⲧⲟⲣыύ ⲡыⲧⲁⲉⲧⲥя ⲥⲟⲥⲏⲩⲧь ⲙⲟύ ⲭⲩύ ⳝⲉⳅ ⲡⲣⲉⳅυⲣⲃⲟⲧυⲃⲁ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲉⲙ ⲥⲩⲧь? ⲧы ⲏⲁⲭⲩύ ⲡыⲧⲁⲉⲱьⲥя ⲥⲟⲥⲏⲩⲧь ⲙⲟύ ⳝυⲅ ⳡⲗⲉⲏ ⲩⲭⲭⲁ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳝⲗяⲧь ⲙⲏⲉ ⲅⲗⲁⲃⲏⲟⲉ ⲡⲟⲕⲁⲯυ ⲅⲇⲉ υ ⲃ ⲕⲁⲕⲟⲉ ⲙⲉⲥⲧⲟ ⲧⲉⳝя ⲃыⲉⳝⲁⲧь/υ я ⲧⲉⳝя ⲏⲁⲅⲣⲁⲯⲩ ⲥⲡⲉⲣⲙⲟύ ⲡⲟⲏяⲗ ⲡυⳅⲇⲁюⳝ ⲉⳝⲁⲏыύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳝⲗя ⲧы ⲣυⲗυ ⲇⲩⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲙⲉⲏя ⲥυⲗьⲏⲉⲉ? ⲭⲩⲉⲥⲁⲥ ⲟⳡⲏυⲥь я ⲧⲉⳝя ⲃыⲉⳝⲩ ⲧы ⲇⲁⲯⲉ ⲃяⲕⲏⲩⲧь ⲏⲁⲭⲩύ ⲏⲉ ⲩⲥⲡⲉⲉⲱь ⲡⲟⲏυⲙⲁⲉⲱь ⲧы ⲃ ⲁⲭⲩⲉ ⳝⲩⲇⲉⲱь ⲡⲟⲕⲁ ⲧⲉⳝя ⲉⳝⲁⲧь ⳝⲩⲇⲩ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ёⳝⲁⲏⲟⲉ ⲃ ⲣⲟⲧ ⲟⲥⲧⲟⲉⳝⲗяюⳃⲉⲉ ⲥⲧⲣⲁⲭⲟⲡυⳅⲇυⳃⲉ, ⲡⲣⲟⲙⲩⲇⲟⳝⲗяⲇⲥⲕⲁя ⲙⲟⲣⲇⲟⳅⲁⲗⲩⲡυⲏⲁ ⲟⲭⲩⲉⲃⲁюⳃⲁя ⲟⲧ ⲥⲟⳝⲥⲧⲃⲉⲏⲏⲟⲅⲟ ⲏⲉⲃъⲉⳝⲉⲏυя. υ ⲃⲁⳃⲉ, ⳝⲗяⲇь, ⲃⲥⲉⲙ ⲭⲩύ ⲥⲟⲥⲁⲧь υ ⲧⲣυ ⲣⲁⳅⲁ ⲃ ⲇⲉⲏь ⲭⲟⲇυⲧь ⲏⲁ ⲃⲟⲥьⲙυⳡⲁⲥⲟⲃыⲉ ⲕⲁⲗⲟⲡⲣⲟцⲉⲇⲩⲣы ⲏⲁ ⲅⲉύⲥⲕυύ ⳡⲁⲧ ⲡυⳅⲇⲁ ⲧⲁⲙ ⲧⲉⳝя ⳅⲁⲯⲇⲁⲗυⲥ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲙⲩⲗⲉⳡⲕⲁ ⲯⲟⲥя)))ⲧы ⲧⲁⲕ ⲯⲉ ⲟⳡ ⲁⲕⲧυⲃⲏⲟ ⲡⲣⲟⲙыⲱⲗяⲉⲱь ⲡⲁⲥⲥυⲃⲏⲟύ ⲡυⲇⲟⲣⲁⲥⲏⲉύ,ⲫⲩ))  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡυⳅⲇⲁⳝⲟⲗ ⲧы ⲉⳝⲁⲏыύ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳡⲉⲧ ⳅⲁⲡⲣⲉⲧυⲗⲁ ⳡⲧⲟⳝы ⲧы ⲩ ⲙⲉⲏя ⲭⲩύ ⲥⲟⲥⲁⲗ υ ⲡⲟ эⲧⲟⲙⲩ ⲧы ⳡⲉⲣⲉⳅ ⲟⲕⲏⲟ ⲩⳝⲉⲅⲁⲉⲱ ⲕ ⲙⲟⲉⲙⲩ ⲭⲩю?  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲉⳝя ⲥⲧⲟυⲧ ⲧⲟⲗьⲕⲟ ⲡⲟⲙⲁⲏυⲧь ⳡⲗⲉⲏⲟⲙ)) ⲕⲁⲕ ⲧы ⲥⲣⲁⳅⲩ ⲕⲩⲡυⲱьⲥя υ ⲡⲟⲇⲩⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲟⲥⲧⲁⲏⲉⲧⲥя ⲃ цⲉⲗⲟⲥⲧυ υ ⲥⲟⲭⲣⲁⲏⲏⲟⲥⲧυ))ⲏⲟ ⲧⲉⳝя ⲏⲁⲉⳝⲩⲧ υ ⲡⲩⲥⲧяⲧ ⲭⲁⳡυ ⲡⲟ ⲕⲣⲩⲅⲩ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲥⲗыⲱ я ⳃⲁ ⲏⲁ ⲥⲃⲟю ⳅⲁⲗⲩⲡⲩ ⲃⲟⳅⲏⲉⲥⲩ ⲧⲃⲟю ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲙⲟⳡⲕυ υ ⲏⲁⳡⲏⲩ ⲃⲥⲧⲩⲡⲁⲧь ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲡⲟⲗⲟⲃⲟύ ⲕⲟⲏⲧⲁⲕⲧ ⲥ ⲧⲃⲟυⲙυ ⲩⲱⲁⲙυ)))  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡⲟⲙⲏυⲱь ⲕⲁⲕ я ⲥⲡυⳅⲇⲉⲗ ⲕⲟⲡьⲉ ⲩ ⲣыцⲁⲣя υ эⲧυⲙ ⲯⲉ ⲕⲟⲡьⲉⲙ ⲟⲧъⲉⳝⲁⲗ ⲧⲃⲟю ⳝⲁⳝⲩⲱⲕⲩ!)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲭⲩⲉⲥⲟⲥ?) ⲧы ⲩⲃυⲇⲉⲗ ⲡυⳅⲇⲩ ⲥⲃⲟⲉύ ⲙⲁⲙы υⲥⲡⲩⲅⲁⲗⲥя υ ⲥъⲉⳝⲁⲗⲥя?  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲇⲁ ⲧы ⳝⲗяⲧь ⲁⲗⲁⲡⲉⳅⲇыⲣь))ⲧⲃⲟя ⲙⲁⲙⲕⲁ ⲃыⲧⲃⲟⲣяⲉⲧ ⲁⲕⲣⲟⳝⲁⲧυⳡⲉⲥⲕυⲉ ⲧⲣюⲕυ ⲥⲃⲟυⲙ ⲣⲧⲟⲙ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю)))  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⲃ ⲡⲟⲡⲉⲣⲉⳡⲏⲩю ⲕυⲱⲕⲩ υ ⲟⲏⲁ ⲇⲟⲭⲏυⲧ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲣⲉⲱυⲗ ⲃⲥⲕⲁⲣⲁⳝⲕⲁⲧьⲥя ⲏⲁ ⲙⲟύ ⲭⲩⲉц ⲡⲥυⲏⲁ ⲣⲁⳅⲟⲣⲃⲁⲏⲏⲁя ⲏⲩ я ⳃⲁ ⲃⲟⳅьⲙⲩ ⲥⲃⲟю ⳝυⲧⲩ ⳝⲗяⲧь υ ⲣⲁⲥⲱυⳝⲩ ⲧⲉⳝя ⲅⲟⲗⲟⲃⲟύ ⲟⳝ ⲕⲁⲫⲉⲗь  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲃⲟⲥⲧⲟⲣⲯⲉⲏⲏⲟ ⲩⲭⲏⲩⲗ υ ⲧⲩⲧ ⲡⲁⲣⲩ ⲃⲟⲗⲟⲥⲁⲧыⲭ яυц ⲩⲇⲁⲣυⲗυ ⲧⲉⳝя ⲧⲁⲕ ⳡⲧⲟ ⲧы ⲏⲉ ⲙⲟⲅ ⲟⲡⲣⲁⲃυⲧьⲥя υ ⲧⲟⲗьⲕⲟ ⲡⲟⲥⲗⲉ ⲧⲟⲅⲟ ,ⲕⲁⲕ ⲧы ⲟⳡⲏⲩⲗⲥя ⲧы ⲡⲟⳡⲩⲃⲥⲧⲃⲟⲃⲁⲗ ,ⲕⲁⲕ ⲧⲃⲟύ яⳅыⲕ ⲗⲟⲃⲕⲟ ⲣⲁⳝⲟⲧⲁⲉⲧ ⲃ ⳡёⲣⲏⲟύ ⲅⲣяⳅⲏⲟύ ⲯⲟⲡⲉ ⲟⲇⲏⲟⲅⲟ ⲡⲟⲇⳅⲁⳝⲟⲣⲏⲟⲅⲟ ⲩⳝⲗюⲇⲕⲁ ...  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲕⲟⲅⲇⲁ ⲙⲟύ ⲭⲩύ ⲃⲥⲧⲁⲉⲧ эⲧⲟ ⳅⲏⲁⳡυⲧ ⳡⲧⲟ ⲧⲃⲟύ ⲣⲟⲧυⲕ ⲭⲟⳡⲉⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⳝⲟⲗьⲱⲉ ⳡⲉⲙ ⲧⲃⲟя ⲙⲁⲧь ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ? я ⳃⲁⲥ ⲭⲩⲉⲙ ⲧⲉⳝⲉ ⲣⲟⲧ ⲇыⲣяⲃυⲧь ⳝⲩⲇⲩ ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ.   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳝⲗяⲧь ⲡⲥυⲏⲁ ⲧы ⲧⲁⲕυ ⲏⲉ ⲡⲟⲏяⲗ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲇⲗя ⲧⲉⳝя цⲁⲣь ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲧⲉⳝя ⳡⲧⲟ ⲭⲩⲉⲙ ⲩⲉⳝⲁⲧь ⳡⲧⲟⳝ ⲧы ⲥⲗⲩⲱⲁⲗⲥя ⲙⲉⲏя,  [<emoji document_id=5438203928527253097>💀</emoji>]',
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳝυⲟⲥⲫⲉⲣⲁ ⲭⲩя ⲙⲟⲉⲅⲟ, ⲏⲉ ⲃⳅъⲉⳝыⲃⲁύⲥя ⲙⲏⲟⲅⲟ, ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏⲏыύ ⳝⲗⲉⲁⲧь, ⲉⳝⲁⲗ ⲧⲃⲟύ ⲣⲟⲧ ⲡⲟⲙⲏυⲱь ⲕⲁⲕ ⲧы ⲡⲟⲕⲩⲥыⲃⲁⲗ ⳡⲗⲉⲏ ⲙⲟύ ⳅⲩⳝⲕⲁⲙυ?)?) ⲙⲏⲉ ⳝыⲗⲟ ⲡⲣυяⲧⲏⲟ, ⲃ ⲧⲟⲧ ⲙⲟⲙⲉⲏⲧ я ⲉⳃⲉ ⲕⲟⲏⳡυⲗ ⲧⲉⳝⲉ ⲃ ⲣⲟⲧ эⲧⲟ ⳝыⲗ 1 ⲣⲁⳅ ⲭⲩⲉⲥⲟⲥ ⲧы ⲙⲟύ)) ⲧы ⲙⲟύ ⲭⲩⲉⲥⲟⲥ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲗяⲧь ⲧы ⳡⲉ ⲧⲁⲙ ⲏⲁⲭⲩύ ⲡυⲱⲉⲱь? ⲡυⲇⲟⲣⲁⲥ я ⳃⲁⲥ ⳝⲩⲇⲩ ⲧⲉⳝя ⲏⲁⲅυⳝⲁь ⲭⲩⲉⲙ ⲧⲃⲟⲉⲅⲟ ⲇⲉⲇⲁ ⲡυⲇⲟⲣⲡⲁⲥ ⲉⲇⲁⲏыύ ⳝⲗяⲧь ⲭⲩⲉⲥⲁⲥ ⲥⲩⲕⲁ ⲏⲩ ⲕⲁ ⲡⲟⲱⲉⲗ ⲃⲟⲏ ⲟⲧⲥюⲇⲁ ⲭⲩⲉⲥⲁⲥ ⲉⳝⲁⲏыύ ⲙⲁⲗⲟⲗⲉⲧⲕⲁ ⲡⲟⲙⲏυⲱь ⲕⲁⲕ я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲁ ⲧы ⲙⲏⲉ ⲃ ⲟⲧⲃⲉⲧ ⲕⲟⲏⲫⲉⲧⲩ ⲇⲁⲃⲁⲗ ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ? ⲭⲩⲉⲥⲁⲥ ⲉⳝⲁⲗ ⲧⲉⳝя ⲃ ⲣⲟⲧ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⳝⲗяⲧь ⲏⲁⲭⲩύ ⲟⲧⲟⲱⲉⲗ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⲡⲟⲕⲁ ⲙⲟц ⲭⲩύ ⲧⲉⳝя ⲏⲉ ⲃыⲉⳝⲁⲗ ⲡⲟ ⲥⲁⲙⲟύ ⲏⲉ ⲙⲟⲅⲩ ⲡⲟⲏυⲙⲁⲉⲱь? ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲧⲉⳝя ⲏⲁⲭⲩύ ⲙⲟⲗⲁ ⲃыⲉⳝⲁⲧь ⲃ ⲣⲟⲧⲁⲏ ⲡυⲇⲟⲣ ⲉⳝⲁⲏыύ я ⲧⲉⳝя ⲏⲁⲭⲩύ ⲡⲟⲃⲉⲱⲩ ⲡυⲇⲟⲣ ⲉⳝⲁⲏыύ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳡⲉ ⲏⲁⲭⲩύ ⲡⲉⲧⲩⲭ ⲉьⲁⲏыύ ⲥⲟⲁⲥⲉⲙ ⲏⲁⳅⲩύ ⲟⲭⲩⲉⲗ? ⲡυⲇⲟⲣⲁⲥ ⲉьⲁⲏыύ я ⲧⲉⳝⲃ ⲏⲁⳡⲏⲩ ⲉⳝⲁⲧь/ⲥ ⲏⲉ ⲧⲟύ ⲏⲟⲅυ ⲡⲟⲏυⲙⲁⲉⲱь ⲭⲩⲉⲥⲁⲥ ⲧы ⲉьⲁⲏыύ ⳝⲗяⲧь ⲡυⲇⲟⲣ ⳅⲁⲗⲩⲡⲁ ⲟⲭⲩⲉⲃⲱⲁя ⲏⲁⲭⲩύ υⲇυ ⲧы ⳝυⲗяⲧь ⲏⲁⲭⲩύ ⲁⲅⲣυⲱьⲥя ⲏⲁ ⲙⲉⲏя ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ я ⲯⲉ ⲧⲉⳝя ⲉⳝⲁⲧь ⳝⲩⲇⲩ ⲕⲁⲕ ⲱⲗюⲭⲩ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳝⲗяⲧь ⲡυⲇⲟⲣ ⲉⲗⲁⲏыύ ⲏυⲭⲩя ⲧы ⳝⲗяⲧь ⲡⲣυⲟⲡⲁⳅⲇыⲃⲁⲉⲱь ⲱⲗюⲭⲁ ⲉⳝⲁⲏⲩⲧⲁя ⲧы ⳡⲉ/ⲉⳝⲁⲧь ⲟⲭⲩⲉⲗⲁ ⲥⲡυⲇⲟⳅⲏⲁя ⲡυⳅⲇⲁ ⲥⲩⲕⲁ ⲇыⲣяⲃⲁя ⲏⲁⲭⲩύ υⲇυ ⲡυⲇⲟⲣⲁⲥⲕⲁ ⲉⳝⲁⲏⲁя ⲏⲁⲭⲩύ ⲡυⲇⲣⲁⲥ ⲭⲩⲉⲥⲁⲥ ⲡⲉⲣⲉⲥⲗⲁⲥⲧ эⲧⲟ ⲥⲟⲟⳝⳃⲉⲏυⲉ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲩⳡυύ,я ⳝⲩⲇⲩ ⲧⲉⳝя ⲉⳝⲁⲧь ⲥⲉⲅⲟⲇⲏя ⲡⲟⲏυⲙⲁⲉⲱь?) ⲡⲉⲧⲩⲱⲏя ⲧы ⲉⳝⲗυⲃⲁя ⲡⲟύⲙυ ⲧⲟ ⳡⲧⲟ ⲧы ⲥⲟⲥⲏⲉⲱь ⲥⲉⲅⲟⲇⲏя ⲭⲩύ ⲡⲉⲧⲩⲭ ⲧы ⲉⳝⲁⲏⲏыύ, ⲧы эⲧⲟ ⲡⲟⲏυⲙⲁⲉⲱь?) ⳡⲧⲟ ⲥⲉⲅⲟⲇⲏя ⲧⲉⳝя я ⲃыⲉⳝⲩ!!  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡⲟⲱⲉⲗ ⲏⲁⲭⲩύ ⲥⲟⲥⲁⲧь ⲙⲟύ ⲭⲩύ ⲡⲟⲏυⲙⲁⲉⲱь? ⲭⲩⲉⲥⲁⲥ ⲧы ⳝⲗяⲧь ⲟⳝⲇⲟⲗⳝыⲱь ⲉⳝⲁⲏыύ ⲥⲩⲕⲁ я ⳃⲁⲥ ⲏⲁⳡⲏⲩ ⲥⲃⲟύ ⲭⲩύ ⲡⲣυⲥⲟⲃыⲁⲡⲧь ⲕ ⲧⲉⳝⲉ ⲃ ⲉⳝⲗⲉⲧ ⲡυⲇⲗⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲏⲁⲭⲩύ ⲡⲟύⲇυ ⲡυⲇⲟⲣ ⲩⲱⲗⲉⲡⲟⲕ я ⲡⲟⲕⲁ ⲧⲉⳝя ⲉⳝⲩ ⲧⲃⲟя ⲙⲁⲧь ⲏⲉ ⲡⲟⲙⲉⲱⲁⲉⲧ ⲥⲇⲉⲗⲁⲧь ⲧⲉⳝⲉ ⲙυⲏⲉⲧ ⲙⲏⲉ? §??  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲏⲁⲭⲩύ ⲥⲕⲣⲉⲙⲧυⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ υ ⲥ ⲙⲟυⲙ ⳅⲩⲉⲙ ⲡⲟⲗⲩⳡυⲗυⲥя ⲧы ⲡυⲇⲟⲣ ⲉⳝⲁⲏыύ ⲡⲟⲏυⲙⲁⲉⲱь ⲏⲉⲧ? ⲭⲩⲉⲥⲁⲥ ⲧы ⲉⳝⲩⳡυύ ⳝⲗяⲧь ⲃыⲉⳝⲁⲧь ⲧⲉⳝя ⲙⲁⲗⲟ ⲭⲩⲉⲥⲁⲥ ⲏⲁⲭⲩύ ⲟⲡⲩⳃⲉⲏыύ ⳝⲗяⲧь ⲧы ⲏⲁⲥⲧⲟⲗьⲕⲟ ⲟⲟⲡⲩⳃⲉⲏⲏыύ ⳡⲧⲟ ⲇⲁⲯⲉ ⲏⲉ ⲩⲥⲡⲉⲃⲁⲉⲱь ⲥⲟⲥⲁⲧь ⲙⲏⲉ ⲭⲩύ? ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲏⲁⲭⲩύ ⳡⲧⲟ ⲏⲉ ⲡⲟⲏяⲗ я ⳃⲁⲥ ⲥⲃⲟⲉⲅⲟ ⲭⲩя ⲟⲧⲡⲣⲁⲃⲗю ⳡⲧⲟⳝ ⲟⲏ ⲧⲉⳝя ⲡⲟⲃⲧⲟⲣⲟⲏⲟ ⲏⲁⲭⲩύ ⲉⳝⲁⲗ ⲧⲉⳝя ⲃ ⲟⳡⲕⲟ ⲡⲟⲏυⲙⲁⲉⲱь? ⲡυⲇⲟⲣⲁⲥ ⲏⲁⲭⲩύ ⲟⲧⲟⲱⲉⲗ ⲥ ⲙⲟⲉⲅⲟ ⲭⲩύ ⲗυⲡⲟⲃыύ ⲡυⲇⲟⲣ ⳝⲗяⲧь ⲧы ⲕⲁⲕⲟύ-ⲧⲟ ⲡυⲇⲟⲣⲁⲥ ⲏⲁⲭⲩύ υⲇυ ⲥⲟⲥⲁⲧь ⲡⲟ ⲯυⲃⲉⲉ ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲡⲟⲕⲁ я ⲧⲉⳝя ⲃ ⲣⲟⲧ ⲏⲉ ⲃыⲉⳝⲁⲗ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲏⲁⲭⲩύ υⲇυ ⲟⲧⲥюⲇⲁ ⲡⲟⲕⲁ я ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⲧⲃⲟύ ⲣⲟⲧ ⲏⲉ ⲡⲣⲟⲇыⲣяⲃυⲗ ⲭⲩⲉⲥⲁⲥ ⲉⳝⲁⲏыύ ⳝⲗяⲧь ⲥⲗыⲱυⲱь ⲡυⳅⲇⲩ ⲕ ⲥⲃⲟⲉύ ⲙⲁⲙⲕⲉ ⲏⲁ ⲭⲩύ ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲡⲟⲕⲁ ⲙⲟύ ⲭⲩύ ⲏⲉ ⲏⲁⲡⲁⲗ ⲏⲁ ⲧⲉⳝя ⲡυⲇⲟⲣⲁⲥ ⲩⲏыⲗыύ ⲥⲩⲕⲁ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲏⲁⲭⲩύ ⲃыⲉⳝⲩ ⲧⲉⳝя ⲉⳝⲁⲧь ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲏⲁⲭⲩύ я ⲧⲉⳝⲉ ⳅⲁⲥⲧⲁⲃⲗю яⳅыⲕⲟⲙ ⲧⲃⲟυⲙ ⲡυⳅⲇⲩ ⲥⲃⲟⲉύ ⲙⲁⲙⲕυ ⲗυⳅⲁⲧь/ⲡⲟⲏυⲙⲁⲉⲱь? ⲭⲩⲉⲥⲁⲥ ⲧы ⲕⲣⲏⳡⲉⲏⲏыύ ⲏⲁⲭⲩύ ⲡυⳅⲇⲁⲗυⳅ ⲉⳝⲁⲏыύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲥⲗыⲱь ⲭⲩⲉⲥⲁⲥ ⲉⳝⲁⲏыύ ⲟⲭⲩⲉⲗ? ⳝⲗяⲧь я ⲏⲁⲭⲩύ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ ⲣⲃⲁⲧь ⳝⲩⲇⲩ ⲧⲁⲕ ⳡⲧⲟ ⲏⲁⲭⲩύ ⲱⲉⲗ ⲟⲧⲥюⲇⲁ ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏыύ ⲧы ⳡⲉ ⲇⲁⲃⲏⲟ ⲏⲁⲭⲩύ ⲡυⳅⲇы ⲏⲉ ⲡⲟⲗⲩⳡⲁⲗ? ⲭⲩⲉⲥⲁⲥ ⲉⳝⲁⲏыύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟя ⲙⲁⲧь ⲕⲟⲅⲇⲁ ⲡⲣыⲅⲁⲗⲁ ⲏⲁ ⲙⲏⲉ, ⲃ ⲙⲟⲉύ ⲙⲁⲱυⲏⲉ, ⲟⲏⲁ ⲧⲁⲕ ⲃыⲥⲟⲕⲟ ⲡⲣыⲅⲏⲩⲗⲁ ⳡⲧⲟ ⲡⲟⲙяⲗⲁ ⲕⲣыⲱⲩ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲁⲏⲁⲗьⲏыύ ⲃⲟⲗⲟⲥ ⲥⲩⲕⲁ ⲧы ⳡⲉ ⲉⳝⲁⲧь ⲁⲭⲩⲉⲗ?) я ⲧⲃⲟύ ⲣⲟⲧ ⳃⲁⲥ ⲏⲁⲥⲧυⲅⲏⲩ ⲥⲩⲕⲁ ⲉⳝⲁⲏⲏⲁя ⲧы ⳡⲉ ⲧⲁⲕⲟύ ⲯυⲣⲏыύ?))?) ⲁ ⳝяⲗⲧь ⲡⲉⲣⲉυⳅⳝыⲧⲟⲕ ⲕⲟⲏⳡυ ⲃ ⲧⲃⲟⲉⲙ ⲟⲣⲅⲁⲏυⳅⲙⲉ?  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲭⲩⲉⲥⲟⲥ ⲉⳝⲁⲏⲏыύ ⳅⲁⲕⲣⲟύ ⲉⳝⲁⲗьⲏυⲕ ⲡυⲇⲟⲣⲁⲥ ⲉⳝⲁⲏⲏыύ ⳝыⲥⲧⲣⲟ ⲥⲟⲥⲏⲩⲗ ⲙⲟύ ⲭⲩύ υ ⲥъⲉⳝⲁⲗⲥя ⲟⲧⲥюⲇⲁ ⲃыⲉⳝⲁⲏⲏⲟⲉ ⲯυⲃⲟⲧⲏⲟⲉ ⲥⲩⲕⲁ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲁ ⳅⲁⳝыⲗ ⲟⲏⲁ ⲙⲟⲉⲧⲥя ⲃ ⲙⲟⲉύ ⲥⲧυⲣⲁⲗьⲏⲟύ ⲙⲁⲱυⲏⲕⲉ) ⲟⲏⲁ ⲃⲟⲏяⲉⲧ ⲥⲡⲉⲣⲙⲟύ ⲡυⳅⲇⲉц)) υⲇυ ⲡⲟⲙⲟύ ⲥⲃⲟю ⲙⲁⲧь) ⲭⲩⲉⲥⲟⲥ ⲉⳝⲁⲏⲏыύ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲉⳝⲁⲧь ⲧⲃⲟя ⲥⲉⲧⲥⲣⲁ ⲃυⲇυⲙⲟ υⲣυⲏⲁ ⲥыⳡⲉⲃⲁ ⲭⲩⲉⲥⲟⲥ ⲉⳝⲁⲏⲏыύ) ⲁⲭ ⲧы ⲥⲉⲕⲥ ⲧⲩⲁⲗⲉⲧⲏыύ)) ⲧⲉⳝя ⲧⲟⲯⲉ ⲃ ⲟⳡⲕⲟ ⲃыⲉⳝⲁⲗυ ⲃ ⲧⲩⲁⲗⲉⲧⲉ?) ⲁ ⲡυⲇⲟⲣⲁⲥ ⲗюⳝяⳃυύ ⲙⲟύ ⲭⲩύ?  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧ ⲟⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲗυ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲥⲗыⲱυⲱь ⲧы ⲯυⲅⲩⲗь ⲉⳝⲁⲏⲏыύ .я ⲯⲉ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲏⲁⲡυⲏⲁю ⲉⳝⲁⲏⲁⲏя ⲧы ⲙⲣⲁⳅⲟⲧⲁ, ⲃⲧⲟя ⲙⲁⲙⲁⲱⲁ ⲏⲁ ⲥⲧⲟⲗьⲕⲟ ⲩⳝⲟⲅⲟ ⲥⲟⲥⲉⲧ ⲙⲟύ ⲭⲩύ ⳡⲧⲟ ⲙⲏⲉ ⲇⲁⲯⲉ ⲥⲧⲣⲁⲱⲏⲟ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲯⲉ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲟⲧⲩⲱⲩ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ, ⲉⳝⲁⲏⲏⲁя ⲧы ⲥⲟⳝⲁⲕⲁ. ⲙⲟύ ⲭⲩύ ⲇⲉⲗⲁⲉⲧ ⲁⲭⲩⲉⲏⲏыⲉ υ ⲇⲟⳝⲣыⲉ ⲇⲉⲗⲁ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲣⲁⲃ ⲕⲟⲅⲇⲁ ⲉⳝⲉⲧ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲁⲏⲁⲗьⲏⲟύ. ⲕⲟⲏⳡⲉⲏⲏⲁя ⲧы ⲅⲁⲏⲇⲟⲏⲕⲁ?). я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲕⲉⲏⲧⲩⲭⲩ ⲃыⲉⳝⲩ), ⲥⲗыⲱυⲱь ⲏⲁⲉⳝⲁⲏⲏыύ ⳡⲉⲡⲩⲱⲏяⲕ. я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲃыⲉⳝⲩ ⲕⲟⲏⳡⲏⲉⲏыύ ⲧы ⲣⲟⲧ ⳝⲗяⲇь ⲕⲟⲧⲟⲣыύ ⳝⲉⲣⲉⲧ ⲏⲁ ⲥⲉⳝя ⲥⲗυⲱⲕⲟⲙ ⲇⲟⲭⲩя. ⲥⲗыⲱυⲱь ⲟⲧьⲉⳝⲁⲏⲏыύ ⲉⲃⲣⲉύ?), я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃыⲧⲣⲁⲭⲁю υ ⲃыⲕυⲏⲩ ⲉё ⳅⲁⲥⲥⲁⲏыⲉ ⲧⲣⲩⲡ ⲥⲟⳝⲁⲕⲁⲙ ⳡⲧⲟ-ⳝы ⲟⲏυ ⲉё ⲥⲭⲁⲃⲁⲗυ ⲉⳝⲁⲏⲏⲩю ⲱⲁⲗⲁⲃⲩ. ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳡυⲥⲧⲟ ⲏⲁⲉⳝⲁⲏⲁⲏя ⲙⲟυⲙ ⲭⲩⲉⲙ. ⲥⲗыⲱυⲱь ⲃыⲥⲥⲁⲏыύ ⲡυⲇⲟⲣⲁⲥ. ⲙⲟύ ⲭⲩύ ⲃыⳝⲉⲣⲉⲧ ⲡⲟⳅⲩ ⲇⲗя ⲧⲟⲅⲟ ⳡⲧⲟ-ⳝы ⲃыⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ, υ ⲃыⳝⲉⲣⲉⲧ ⲁⲭⲩⲉⲏⲏю ⲡⲟⳅⲩ ⳡⲧⲟ-ⳝы ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⳝыⲗⲁ ⲇⲟⲃⲟⲗьⲏⲟύ. ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲃыⲉⳝⲉⲧ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲁⲉⳝⲁⲏⲏⲩю, ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳡυⲥⲧⲟ ⲱⲟⲱⲕⲁ ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя. ⲥⲗыⲱυⲱь ⲙⲣⲁⳅⲟⲧⲁ ⲉⳝⲁⲏⲏⲁя,я ⲕⲁⲕ-ⲧⲟ ⲣⲁⳅ ⲧⲣⲁⲭⲏⲩⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ υ ⲩ ⲏⲉё ⲡⲟⲧⲟⲙ ⲏⲁⳡⲁⲗⲥя ⲥⲡⲁⳅⲙ ⲡυⳅⲇы, ⲧы ⲙⲟⲯⲉⲱь ⳅⲁⲗⲉⳡυⲧь ⲟⳡⲕⲟ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲏⲁя ⲧы ⲅⲁⲏⲇⲟⲏⲕⲁ?), я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃыⲉⳝⲩ ⳝⲉⳅ ⲟⳝυⲇ ⲡⲟⲏυⲙⲁⲉⲱь ⲉⳝⲁⲏⲏыύ ⲧы ⲡⲉⲇυⲕ ⲇⲣⲟⳡⲁⳃυύ ⲙⲟύ ⲭⲩύ ⲥⲉⳝⲉ ⲃ ⲣⲟⲧⲁⲏ. ⲙⲏⲉ ⲣⲁⲥⲥⲕⲁⳅыⲃⲁⲗυ ⲧⲟ ⳡⲧⲟ ⲩ ⲧⲉⳝя ⲡυⳅⲇⲁ, ⲡυⳅⲇⲟⲕⲣыⲗыύ ⳝⲁⲣⲁⲏ ⲥⲩⲕⲁ, я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃыⲉⳝⲩ ⲕⲁⲕ ⲉⳝⲁⲏⲏⲩю ⲱⲃⲁⳝⲣⲩ, ⲥⲗыⲱυⲱь ⲧы ⲙⲟⲕⲣⲉⳃⲉⲗⲕⲁ ⲉⳝⲁⲏⲁя, я ⲇⲟⲕⲁⲯⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲉ ⲧⲟ ⳡⲧⲟ я ⲙⲟⲅⲩ ⲃыⲉⳝⲁⲧь цⲉⲗυⲕⲟⲙ ⲧⲃⲟю ⲯⲟⲡⲩ ⳅⲁⲥⲥⲁⲏⲩю ⲡⲟⲕυⲏⲩⲧⲩю ⲭⲩяⲙυ. ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⳡυⲥⲧяⲧ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲡⲟⲧⲭⲩⲱⲏⲉύ. ⲧы ⲯⲉ ⲃыⳝⲗяⲇⲟⲕ ⲉⳝⲁⲏⲏыύ, я ⲃ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲧыⲕⲁⲗ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ. ⲥⲗыⲱυⲱь ⲧы ⲥⲟⳝⲁⲕⲁ ⲉⳝⲁⲏⲏⲁя ⲧы ⲃыⲕⲩⲡⲁⲉⲱь ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⳡυⲥⲧυⲗυ ⲃⲥⲉ ⲇыⲣⲕυ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυⲉ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⲉⳝⲁⲏⲩⲏю ⲃ ⲣⲟⲧ ⲱⲁⲧⲁⲗ, ⲡⲟⲏυⲙⲁⲉⲱь ⲩ ⲧⲉⳝя ⲏⲉⲧ ⲃⲁⲣυⲁⲏⲧⲟⲃ, ⲧы ⳝⲩⲇⲉⲱь ⲙⲟⲉⲙⲩ ⲭⲩю ⲟⲧⲇⲁⲃⲁⲧьⲥя ⲕⲁⲁⲕ ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲥⲥⲁⲏⲟύ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲁⲕ, ⲧⲟ ⲉⲥⲧь ⲧы ⲏⲉ ⲣⲉⲱυⲗ ⳅⲁⲇⲁⳡⲩ ⲥⲧⲁⲃⲗю ⲧⲉⳝⲉ ⳅⲁ эⲧⲟ 2 ⲭⲩя ⲏⲁ ⲟⲧⲥⲟⲥ, ⲧⲁⲕ ⲏⲟⲃⲁя ⳅⲁⲇⲁⳡⲁ ⲏⲟ ⲗⲉⲅⲕⲁя ⲇⲁⲯⲉ ⲧⲁⲕⲟύ ⲭⲩⲉⲥⲁⲥ ⲕⲁⲕ ⲧы ⲥⲙⲟⲯⲉⲧ ⲣⲉⲱυⲧь эⲧⲩ ⳅⲁⲇⲁⳡⲩ ⲃⲟⲧ ⲥⲙⲟⲧⲣυ, ⲧⲃⲟя ⲙⲁⲧь ⲥⲡⲣяⲧⲁⲗⲁ ⲩ ⲥⲉⳝя ⲃ ⲡυⳅⲇⲉ 17 ⳅⲟⲗⲟⲧыⲭ ⲙⲟⲏⲉⲧ, ⲡⲣυⲱⲉⲗ ⲏυⲅⲉⲣ ⲟⲧьⳝⲉⲗ ⲉё υ ⲟⲏ ⲏⲁⲥⲕⲣⲉⳝ ⲥ ⲉⲉ ⲡυⳅⲇы 7 ⲙⲟⲏⲉⲧ, ⲥⲕⲟⲗьⲕⲟ ⲙⲟⲏⲉⲧ ⲃ ⲡυⳅⲇⲉ ⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ?   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲩ ⲏⲁⲥ ⲥ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣью ⲏⲁⳡⲁⲗⲁⲥь ⲗюⳝⲟⲃь, я ⲉё ⲉⳝⲩ, υ ⲟⲏⲁ ⲙⲟύ ⲭⲩύ ⲟⲧⲥⲁⲥыⲃⲁⲉⲧ, ⲧы ⳝⲩⲇⲉⲱь ⲧⲁⲕ-ⲯⲉ ⲟⲥⲧⲁⲥыⲃⲁⲧь ⲕⲁⲕ υ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲕⲁ ⳅⲁⲅⲏⲟⲉⳝⲗⲉⲏⲏⲁя ⲭⲩяⲙυ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲇⲁ я ⲃⲥⲉⲣⲟⲃⲏⲟ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲕυⲧⲕⲁύⲕⲩ ⲉⳝⲁⲏⲏⲩю ⲃ ⲯⲟⲡⲩ ⲧⲣⲁⲭⲏⲩ, ⲥⲗыⲱυυⲱь ⲧы ⲯⲟⲡⲁ ⲃⲟⲗⲟⲥⲁⲧⲁя. я ⲃ ⲧⲉⳝя ⳝⲩⲇⲩ ⲃⲭⲟⲇυⲧь ⲃ ⲟⳝ ⲧⲃⲟυ ⲃⲟⲗⲟⲥы ⲃыⲧⲉⲣⲁⲧь ⲥⲃⲟю ⲥⲡⲉⲣⲙⲩ ⲕⲟⲧⲟⲣⲩю ⲏⲁⲕⲟⲏⳡⲁю ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃыⲉⳝыⲃⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲕⲩ. υ ⲟⲥⲧⲁⲃυⲗ ⲏⲁ ⲉё ⲡυⳅⲇⲉ ⲇⲁⲯⲉ ⲧⲁⲧⲩⲭⲩ ⳝⲉⲁⲏⲏⲁя ⲧы ⲭⲩⲉⲧⲁ, я ⲃⲥⲉⲣⲟⲃⲏⲟ ⲏⲁⲉⳝⲁⲩ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲙⲁⲕⲁⲕⲩ ⲕⲟⲏⳡⲉⲏⲩю   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲃыⲉⳝⲁⲗυ ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⳅⲁⲉⳝⲁⲏⲏⲩю, ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⳅⲁⲗⲉⲧⲁⲉⲧ ⲃ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳡⲉⲉⲣⲉⳅ ⳡⲁⲥ?), ⲃⲁⲫⲗⲉⲣⲕⲁ ⲧы ⲉⳝⲁⲏⲏⲁя)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲥⲗυⲧⲟⲕ ⲉⳝⲁⲏⲏыύ. я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲙⲟⲣⲁⲗьⲏⲟ υ ⲟⲣⲁⲗьⲏⲟ ⲩⲏυⲯⲩ, ⲉⳝⲁⲏⲏⲁя ⲧы ⲭⲩⲉⲧⲁ, ⲙⲁⲧь ⲧⲃⲟя ⲃⲏⲁⲧⲩⲣⲉ ⲏⲁⲉⳝⲁⲏⲏⲁя ⲙⲟυⲙ ⲭⲩⲉⲙ ⲡⲣⲟⲥⲧυⲧⲩⲧⲕⲁ, ⲱⲁⲗⲁⲃⲁ ⲧы ⲉⳝⲗυⲃⲁя)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲯⲉ ⲱⲁⲱⲗыⲕ ⲉⳝⲁⲏⲏыύ, я ⲧⲉⳝя ⲡⲟⲣⲉⲯⲩ ⲏⲁ ⲥⲃⲟⲉⲙ ⲭⲩⲉ ⲙⲟⲣⲇⲁ ⲧы ⲥⲩⲕⲁ ⲕⲁⲃⲕⲁⳅⲥⲕⲁя, я ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⲕⲩⲕⲗⲩ ⲃ ⲡυⳅⲇⲁⲕ ⲉⳝⲁⲗ, ⲅⲏυⲗⲟⲉⳝⲕⲁ ⲧы ⲉⳝⲁⲏⲁⲏя. ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲥⲏⲟⲥυⲗυ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲉⳝⲁⲏⲏⲟύ?), ⲧы ⲡⲟⲕⲁⲯⲉⲱь ⲙⲟⲉⲙⲩ ⲭⲩю ⲙⲁⲥⲧⲉⲣ ⲕⲗⲁⲥⲥ. ⲕⲁⲕ ⲧы ⲩⲙⲉⲉⲱь ⲥⲃⲟⲉύ ⲅⲩⳝⲟύ ⲇⲉⲗⲁⲧь ⲉⳝⲁⲏⲏⲁя ⲥⲟⲥⲕⲁ)?   [<emoji document_id=5438203928527253097>💀</emoji>]',
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ я ⳝⲩⲇⲩ ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⲃыⲉⳝⲩ, ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃыⲧⲣⲁⲭⲁⲗ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲙы ⲡⲉⳡⲁⲗьⲏⲟύ, ⲃⲟⲧ ⲧы ⲙⲣⲁⳅⲟⲧⲁ ⲕⲟⲏⳡⲉⲏⲏⲁя)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⲡⲟⲗυⲥⲙⲉⲏⲕⲩ ⲉⳝⲁⲏⲏⲩю ⲃ ⲣⲟⲧ ⲱⲁⲧⲁⲗ ⳝⲟⲙⲯⲁⲣⲁ ⲧы ⲥⲩⲕⲁ ⲏⲉ ⲟⲕⲟⲗⲁⳡυⲃⲁύⲥя ⲩ ⲙⲟⲉⲅⲟ ⲭⲩя ⲉⳝⲁⲏⲏⲁя ⲇⲩⲣⲁ ⲥⲩⲕⲁ. цыⲅⲁⲏⲕⲁ ⲧы ⲉⳝⲁⲏⲏⲁя ⲃ ⲣⲟⲧⲁⲏ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲯⲉ ⲥⲩⲕⲁ ⳡⲩⲣⳝⲁⲏ ⲉⳝⲁⲏыⲏύ, я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⳡυⲥⲧⲟ ⲃыⲉⳝⲩ υ ⲃыⲕυⲏⲩ ⲉⳝⲁⲏⲁя ⲧы ⲱⲙⲁⲣⲁ, я ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⲏⲁⲉⳝⲁⲱυⲗ ⲥⲗыⲱυⲱь ⲧы ⲅⲁⲏⲇⲟⲏⲕⲁ ⳝⲉⲁⲏⲏⲁя)?   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲭⲩⲉⲥⲟⲥⲕⲩ ⳅⲁⲡυⳅⲇυⲗ ⲥⲃⲟυⲙ ⳡⲗⲉⲏⲟⲙ, ⲉⳝⲁⲏⲏыύ ⲧы ⲉⲃⲏⲩⲭ я ⳡυⲥⲧⲟ ⲩⲅⲟⲣⲁю ⲏⲁⲇ ⲡυⳅⲇⲟύ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲣⲃⲁⲏⲟύ), я ⲯⲉ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲏⲁⲧⲣⲁⲭⲁю ⲥⲃⲟυⲙ ⲭⲩⲉⲙ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳝⲩⲇⲉⲱь ⲇⲉⲣⲯⲁⲧь ⲙⲟύ ⲭⲩύ ⲩ ⲥⲉⳝя ⲃ ⲣⲩⲕⲁⲭ ,υ ⲏⲁⲥⲁⲥыⲃⲁⲧь ⲏⲁ ⲉⳝⲗю ⲥ υⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉύ ⲉⳝⲁⲏⲏⲟύ , я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲉⳝⲁⲗ, ⳝⲉⲅυ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⳝⲉⲁⲏⲏⲁя ⲇыⲣⲕⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲡⲣυⲥⲧⲉⳝыⲃⲁⲗⲁ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲥⲃⲟю ⲡυⳅⲇⲩ, ⲉⳝⲁⲏⲏⲁя ⲧы ⲕⲗяⳡⲁ. я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲥⲏⲟⲥυⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ. ⲅⲟⲗⲩⳝⲟⲅⲗⲁⳅⲁя ⲧы ⲱⲁⲗⲁⲃⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃыⳅⲟⲃⲩ ⲏⲁ ⲉⳝⳝⲗю ⲕ ⲥⲃⲟⲉⲙⲩ ⲭⲩю, ⲉⳝⲁⲏⲁⲏя ⲧы ⲡⲇυⲟⲣⲁⲥⲕⲁ. ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⳅⲣя ⲏⲁⲡⲁⲗⲁ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲥⲃⲟⲉύ ⲧьⲉⳝⲁⲏⲏⲟύ ⲡυⳅⲇⲟύ ⲗⲟⲭ ⲧы ⲥⲩⲕⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲉⳝⲁⲧь ⲇⲁ я ⲃⲏⲁⲧⲩⲣⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲕⲟⲏⳡⲉⲏⲏⲩю ⲭⲩяⲙυ ⳅⲁⲕυⲇⲁю ⲕⲟⲅⲇⲁ ⲟⲏⲁ ⳝⲩⲇⲉⲧ ⲥⲃⲟⲉύ ⲡυⳅⲇⲟύ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲡⲣыⲅⲁⲧь, ⲉⳝⲁⲏⲏыύ ⲧы ⲥⲩⲕⲁ ⲟⳡⲕⲟⲏⲁⲃⲧ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⳡυⲥⲧⲟ ⲡⲟⲇⲏυⲙⲁⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲏⲁ ⲥⲃⲟⲉⲙ ⲭⲩⲉ. ⲉⳝⲁⲧь ⲟⲏⲁ ⲁⲭⲉⲩⲃⲁⲗⲁ ⲉⳝⲁⲏⲏⲁя ⲕⲗⲩⲱⲁ, ⲥⲗыⲱυⲱь ⲧы ⲥⲏⲁύⲡⲉⲣ ⲙⲟⲉⲅⲟ ⲭⲩя. я ⲏⲁⲉⳝыⲃⲁⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲩⲭυ ⲉⳝⲁⲏⲏⲟύ)ъ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳡυⲥⲧⲟ ⲥⲡⲣⲁⲱυⲃⲁⲉⲧ ⲩ ⲙⲟⲉⲅⲟ ⲭⲩя ⲡⲟⳡⲉⲙⲩ ⲟⲏ ⲧⲁⲕ ⲙⲁⲗⲟ ⲩⲇⲉⲗяⲉⲧ ⲉύ ⲃⲏυⲙⲁⲏυя, ⲕⲁⲕ ⲇⲩⲙⲁⲉⲱь ⲡⲉⲣⲉⲥⲧⲁⲧь ⲧⲉⳝя ⲉⳝⲁⲧь ⳡⲧⲟⲗⲉ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲃыⲧⲣⲁⲭⲁю ⲕⲟⲏⳡⲉⲏⲏыύ ⲧы ⲉⲃⲏⲩⲭ ⲥⲩⲕⲁ, ⲙⲟύ ⲭⲩύ ⲡⲟυⲙⲉⲉⲧ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲡⲟⲗⲏⲟⲥⲧью ⲉⳝⲁⲏⲏⲁя ⲧы ⲥⲟⲥⲕⲁ), я ⲯⲉ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲕⲩ ⲉⳝⲁⲏⲏⲩю ⲱⲁⲗⲁⲃⲩ ⲟⲧьⲉⳝⲩ ⲭⲩⲉⲙ ⲥⲗыⲱυⲱь ⲉⳝⲁⲏⲏыύ ⲧы ⲕⲗⲟⲩⲏ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲡυⳅⲇⲁⲕ ⲃыⲧⲣⲁⲭⲁю ⲉⳝⲁⲏⲏⲁя ⲧы ⲙⲣⲁⳅⲟⲧⲁ, ⲙⲟύ ⲭⲩύ ⲃ ⲡⲁⲣⲁⲱⲉ ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲕⲟⲏⳡⲉⲏⲏⲩю ⲃⲟⲧ ⲧы ⲥⲩⲕⲁ ⲇⲁⲩⲏυⲧⲁ ⲉⳝⲁⲏⲁя, ⲧы ⲯⲉ ⲥⲃυⲏья ⲉⳝⲁⲏⲏⲁя ⲕⲟⲧⲟⲣⲁя ⲇⲣⲟⳡυⲧ ⲙⲟύ ⲭⲩύ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳝⲗяⲇь ⲡⲟⲏυⲙⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲏⲁⲣⲩⲱυⲗⲁ ⲥⲃⲟю ⲡⲥυⲭυⲕⲩ ⲙⲟυⲙ ⲭⲩⲉⲙ. я ⲯⲉ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧⲉⲣⲡυⲗы ⲃыⲉⳝⲩ. ⲥⲗыⲱυⲱь ⲧы ⲙⲟύ ⲭⲩύ ⲥⲟⲥυ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲇⲉⲗⲁⲗυ ⲟⳝⳅⲟⲣ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲉⳝⲁⲏⲏыύ ⲧы ⲇⲁⲩⲏ?)ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲃыⲉⳝⲁⲗυ ⲧⲃⲟю ⲙⲁⲙⲕⲩ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲗυ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲇⲁ ⲉⳝⲁⲗυ ⲉё ⲭⲟⲣⲟⲱⲟ ⲕⲟⲏⳡⲉⲏⲏⲩю ⲡⲣⲟⲥⲧυⲧⲩⲧⲕⲩ, ⲥⲗыⲱυⲱь ⲗяⲣⲃⲁ ⲉⳝⲁⲏⲁя. я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃыⲉⳝⲩ υ ⲃыⲕυⲏⲩ ⲏⲁ ⲭⲩύ. ⲡⲁⲣⲁⲱⲁ ⲧы ⲉⳝⲁⲏⲏⲁя)?   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲅⲁⲣⲁⲯⲉ ⲉⳝⲁⲗ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ. ⲧы ⲡⲣⲟⲧⲩⲭⲱυύ ⲡⲉⲧⲩⲭ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲕⲩⲕⲁⲣⲉⲕⲁⲉⲧ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲥⲃⲟⲉύ ⲡυⳅⲇⲟύ ⲕⲟⲧⲟⲣⲩю ⲟⲧьⲉⳝыⲃⲁюⲧ ⲕⲁⲯⲇыύ ⲇⲉⲏь)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲗυ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲟⳅⲟⲣⲏⲩю ⲃ ⲣⲟⲧⲁⲏ, ⲕⲟⲏⳡⲉⲏⲁⲏя ⲧы ⲡυⳅⲇⲁⲅⲗⲟⲧⲕⲁ?). я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲥⲏⲟⲥυⲗ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲧы ⲅⲏυⲗⲟⲉⳝⲕⲁ ⲉⳝⲁⲏⲏⲁя0   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲙⲩⲇⲗⲁⲏⲕⲁ ⲧы ⲉⳝⲁⲏⲏⲁя. ⲧы ⳝⲩⲇⲉⲱь ⲕ ⲙⲟⲉⲙⲩ ⲭⲩю ⲗυⲡⲏⲩⲧь ⲕⲁⲕ υ ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲉⳝⲁⲏⲏⲟύ, ⲧы ⲭⲩⲗⲉ ⲧⲁⲕⲟύ ⲏⲁⲉⳝⲁⲏⲏыύ ⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ. ⲧы ⲉⳝⲁⲏⲏыύ ⲙⲩⲇⲗⲁⲏ. ⲃⲥⲉⲣⲟⲃⲏⲟ ⲙⲟύ ⲭⲩύ ⲃыⲧⲣⲁⲭⲁⲉⲧ ⲧⲃⲟю ⲙⲁⲙⲕⲩ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲡυⳅⲁⲇ ⲃⲧⲟⲉύ ⲙⲁⲙⲁⲱυ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲡⲣыⲅⲁⲉⲧ ⲥⲗыⲱυⲱь ⲧы ⲏⲉⳡⲉⲥⲧь ⲉⳝⲁⲏⲁⲏя. я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩⲃ ⲣⲟⲧ ⲏⲁⲉⳝыⲃⲁ ⲕⲟⲏⳡⲉⲏⲏы ύⲧы ⳡⲗⲉⲏⲟⲥⲟⲥⲟ ⲥⲩⲕⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲟⲡяⲧь ⲕⲟⲡυⲣⲟⲃⲁⲧь ⲡⲟⲱⲉⲗ ⲡⲟ ⲃⲧⲟⲣⲟⲙⲩ ⲕⲣⲩⲅⲩ, ⲕⲁⲕ υ ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲟⲧьⲉⳝⲁⲏыύ ⲧы ⲇⲁⲩⲏ. я ⲯⲉ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲁⲧⲣⲁⲭⲁю ⲥⲃⲟυⲙ ⳡⲗⲉⲏⲟⲙ ⲉⳝⲁⲏⲏⲁя ⲧы ⲕⲩⲣⲟⲡⲁⲧⲕⲁ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲉⳝⲁⲏⲏⲁя ⲡⲁⲣⲁⲱⲁ ⲃ ⲕⲟⲧⲟⲣⲩю я ⲥⲥⲩ. ⲥⲗыⲱυⲱь ⲧы ⲅⲁⲣⲙⲟⲏыύ ⲡⲉⲧⲩⲭ, я ⲃⲧⲟю ⲙⲁⲙⲁⲱⲩ ⳡυⲥⲧⲟ ⲥⲗⲗью ⲃⲩⲏυⲧⲁⳅ ⳅⲁⲥⲩⲏⲩ ⲉⳝⲁⲏⲏⲩю ⲡⲁⲣⲁⲱⲩ ⲥⲩⲕⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲯⲉ ⲃ ⲡⲟⳅⲉ ⲗⲟⲧⲟⲥⲁ ⲟⲧⲇⲁⲉⲱьⲥя ⲙⲟⲉⲙⲩ ⲭⲩю, ⲥⲗыⲱυⲱь ⲏⲁⲥⲥⲁⲏыύ ⲡⲉⲧⲩⲭ .я ⲃⲧⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲟⲣⲟⲧ ⲟⲧьⲉⳝⲩ. ⲕⲟⲏⳡⲉⲏⲏыύ ⲧы ⲥⲏⲉⲅ я ⲧⲉⳝя ⲭⲩⲉⲙ ⲕⲟⲣⲙυⲗ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳝⲟⲗⲉⲉⲧ ⲥⲡυⲇⲟⲙ ⲉⳝⲁⲏⲏⲁя ⲥⲟⳝⲁⲕⲁ.я ⲉё ⲟⲧⲣⲁⲭⲁю ⲃ ⲡυⳅⲇⲩ ⲥⲗыⲱυⲱь ⲧы ⲇⲟⲕⲩⲙⲉⲏⲧ, ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲙⲏⲉ ⲇⲁⲗⲁ ⳝⲩⲙⲁⲅυ ⲡⲟ ⲕⲟⲧⲟⲣыⲙ я ⲙⲟⲅⲩ ⲧⲉⳝя ⲃыⲉⳝⲁⲧь ⲕⲁⲕ ⲥⲟⳝⲁⲕⲩ   [<emoji document_id=5438203928527253097>💀</emoji>]',
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲯⲉ ⲡⲣⲟⲥⲧⲟ ⲕⲟⲅⲇⲁ ⲥⲟ ⲙⲏⲟύ ⲟⳝⳃⲁⲉⲱьⲥя ⲧы ⲥυⲇυⲱь ⲩ ⲙⲉⲏя ⲡⲟⲇ ⲥⲧⲟⲗⲟⲙ υ ⲡыⲧⲁⲉⲱьⲥя ⳡⲧⲟ-ⲧⲟ ⲥⲕⲁⳅⲁⲧь ⲃ ⲧⲟ ⲃⲣⲉⲙя ⲕⲟⲅⲇⲁ я ⲧⲉⳝя ⲉⳝⲩ ⲕⲟⲏⳡⲉⲏⲏⲩю ⲇⲩⲣⲕⲩ. ⲧы ⲯⲉ ⲏⲁ ⲭⲩύ ⲙⲟύ ⲭⲩύ ⲡⲣыⲅⲏⲉⲱь ⲕⲁⲕ υ ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲩ ⲧⲉⳝя ⳝⲩⲇⲉⲧ ⲣⲟⲧ ⳝⲟⲗⲉⲧь ⲡⲟⲥⲗⲉ ⲧⲟⲅⲟ ⲕⲁⲕ ⲙⲟύ ⲭⲩύ ⲟⲧьⲉⳝⲉⲧ ⲧⲉⳝя ⲙⲩⲇⲗυⳃⲉ ⲥⲩⲕⲁ ⲕⲟⲏⳡⲉⲏⲏⲟύ, ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳡυⲥⲧⲟ ⲟⲧⲇⲁⲉⲧⲥя ⲙⲏⲉ ⳝⲟⲧⲁⲏυⳡⲕⲁ ⲉⳝⲁⲏⲏⲁя, ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲇⲩⲣⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲗⲟⲯυⲧьⲥя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲡⲟⲗⲏⲟⲥⲧью ⲥⲃⲟⲉύ ⲡυⳅⲇⲟύ, ⲧⲁⲕ ⲥⲕⲁⳅⲁⲧь ⲡⲟⲕⲣыⲃⲁⲉⲧ ⲉⲅ ⲟⲉⳝⲁⲏⲁⲏя ⲇⲩⲣⲁ, ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲗυ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲟⳡⲕⲁⲥⲧⲩю ⲥⲩⲕⲁ ⲇⲩⲣⲩ, ⲧы ⲯⲉ ⲥ ⲧⲩⲡыⲙ ⲉⳝⲁⲗⲟⲙ ⲟⲧⲇⲁⲱьⲥя ⲙⲟⲉⲙⲩ ⲭⲩю ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲃыⲉⳝⲁⲏⲏⲁя, ⲧы ⲯⲉ ⲟⲃⳡⲁⲣⲕⲁ ⲉⳝⲁⲏⲏⲁя ⲕⲟⲧⲟⲣⲁя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲡⲣыⲅⲁⲉⲧ, ⲃыⲉⳝⲁⲏⲏыύ ⲧы ⲥⲩⲕⲁ ⳡⲗⲉⲏⲟⲥⲟⲥ), ⲧы ⳝⲩⲇⲉⲱь ⲡⲟⲙⲟⲅⲁⲧь ⲙⲟⲉⲙⲩ ⲭⲩю ⲉⳝⲁⲧь ⲡυⳅⲇⲩ ⲥⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲉⳝⲁⲏⲏⲟύ. ⲧы ⲯⲉ ⲕⲟⲏⳡⲉⲏⲏыύ ⲇⲁⲩⲏ ⲕⲟⲧⲟⲣⲟⲙⲩ я ⲃ ⲣⲟⲧ ⲇⲁю, ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲇⲉⲅⲉⲏⲉⲣⲁⲧⲕⲁ ⲉⳝⲁⲏⲏⲁя)?   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲡⲉⲗⲁ ⲣⲁⳅⲏыⲉ ⲡⲉⲥⲏυ ⲡⲟⲇ ⲙⲟύ ⲭⲩύ ⲉⳝⲁⲏⲏⲁя ⲧы ⲇⲩⲣⲁ ⳝⲗяⲇь,я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲃыⲉⳝⲩ ⲕⲟⲏⳡⲉⲏⲏⲁя ⲧы ⲥⲃυⲏья. я ⳡυⲥⲧⲟ ⲇⲟⲭⲩя ⲃⲣⲉⲙⲉⲏυ ⲩⲇⲉⲗяю ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲉⲃⲣⲟⲡⲉύⲏыύ ⲧы ⲭⲩⲉⲥⲟⲥ, я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲣⲟⲥⲧυⲧⲩⲧⲕⲩ ⲕⲟⲏⳡⲉⲏⲏⲩю ⳅⲁⲧⲣⲁⲭⲁю)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲕⲟⲏⳡⲏⲉⲏⲁя ⲥⲟⲥⲕⲁ ⲕⲟⲧⲟⲣⲩю я ⲉⳝⲩ. ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲧⲟ ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲉⳝⲩ ⲡⲟⲇ ⲁⲭⲩⲉⲏⲏⲩю ⲙⲩⳅыⲕⲩ. ⲉⳝⲁⲏⲏⲁя ⲧы ⲙⲟⳡⲁⲗⲕⲁ. ⲟⲧⲇⲁύⲥя ⲙⲟⲉⲙⲩ ⲭⲩю ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲟⲧьⲉⳝⲩ, ⲙυⲇⲉⲣ ⲧы ⲕⲟⲏⳡⲉⲏⲏыύ. ⲧы ⳝⲩⲇⲉⲱь ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⲥⲧⲟяⲧь ⳡⲧⲟ-ⳝы ⲩ ⲧⲉⳝя ⲏⲉ ⲥⲧυⲗυⲗυ ⲕⲣυⲡⲟⲃ ⲉⳝⲁⲏⲏⲁя ⲧы ⲱⲁⲃⲕⲁ. ⲙⲟύ ⲭⲩύ ⲡⲟⲣⲃⲉⲧ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲁⲏⲁⲗьⲏⲟύ. ⲧы ⲯⲉ ⲉⳝⲁⲏⲏыύ ⲁⲏⲁⲏⲁⲥ ⲃ ⲕⲟⲧⲟⲣыύ я ⲧыⲕⲁю ⲭⲩⲉⲙ. ⲉⳝⲁⲏⲏⲁя ⲱⲗяⲡⲁ ⲧы ⲥⲩⲕⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲉⳝⲁⲗⲟ ⲥⲧⲁⲇⲟ ⳝыⲕⲟⲃ ⲉⳝⲁⲏⲏⲁя ⲧы ⳡⲉⲗⲕⲁⲥⲧⲁя ⲭⲩύⲏя)?, ⲧы ⲯⲉ ⲭⲁⳡⲩⲅⲁ ⲉⳝⲁⲏⲁя, я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲉⳝⲁⲗ ⲃⲟ ⲃⲥⲉⲭ ⲩⲕⲣⲁυⲏⲥⲕυⲭ ⲡⲟⳅⲁⲭ ⲡⲟ ⲕⲁⲙⲁⲥⲩⲧⲣⲉ ⲉⳝⲁⲏⲏⲁя ⲧы ⳝυⳝⲗυя. я ⲡⲣⲟⳡυⲧⲁⲗ ⳡⲧⲟ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲁⲇⲟ ⲉⳝⲁⲧь ⲥυⲗьⲏⲟ ⲭⲩⲉⲙ ⲃ ⲯⲟⲡⲩ. ⲇⲁⲃⲁύ ⲡⲟⲡⲣⲟⳝⲩⲉⲱь ⲟⲧⲥⲟⲥⲁⲧь ⲙⲟύ ⲭⲩύ ⲥⲟ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉύ ⲏⲁ ⲡⲁⲣⲩ ,ⲉⳝⲁⲏⲏыⲉ ⲭⲩⲉⲅⲗⲟⲧы)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲡⲟⲧⲣⲉⲡⲁⲏⲏⲁя ⲱⲁⲗⲁⲃⲁ. ⲧы ⲯⲉ ⲉⳝⲁⲏⲁя ⲙⲟⳝυⲗⲕⲁ ⲏⲁ ⲕⲟⲧⲟⲣⲩю я ⲕⲟⲡυⲗ ⲙⲏⲟⲅⲟ, υ ⲙⲏⲟⲅⲟ ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲕⲟⲏⳡⲏⲉⲩю, ⲧы ⲯⲉ ⲃыⲉⳝⲁⲏⲏыύ ⳡⲉⲡⲩⲱⲏяⲕⲕя. ⲕⲟⲏⲉⲏⲏⲁя ⲥⲃυⲏья   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲗυ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲣⲟⲧⲩⲭⲱⲩю ⲭⲩяⲙυ. ⲧы ⳝⲩⲇⲉⲱь ⲫⲁⲏⲧⲁⳅυⲣⲟⲃⲁⲧь ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⳡⲧⲟⲗⲉ, ⲉⳝⲁⲏⲏя ⲧы ⲇыⲣⲕⲁ ⲥⲩⲕⲁ. ⲧы ⲯⲉ ⲕⲩⲃⲱυⲏ ⲉⳝⲁⲏⲏыύ ⲃ ⲕⲟⲧⲟⲣыύ я ⲥⲥⲩ ⲉⳝⲁⲏⲏⲁя ⲙяⲙⲗя)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲗυ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ, цⲃⲉⲧⲟⲕ ⲧы ⲥⲩⲕⲁ ⲏⲁⲉⳝⲁⲏⲏыύ ⲭⲩⲉⲙ. яⲧ ⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲟⲇ ⲃⲟⲕⲁⲗ ⲉⳝⲁⲗ, ⲕⲟⲏⳡⲉⲏⲏⲁя ⲧы ⲡⲗⲟⳃⲁⲇⲕⲁ ⲇⲗя ⲭⲩⲉύ. ⲧы ⲅⲗⲁⲃⲏⲟⲉ ⲏⲉ ⲡⲗⲁⳡь ⲕⲟⲅⲇⲁ ⲙⲟύ ⲭⲩύ ⲉⳝⲉⲧ ⲧⲃⲟύ ⳅⲁⲥⲥⲁⲏы ύⲣⲟⲧ ⲟⲧьⲉⳝⲁⲏⲏыύ ⲧы ⲡⲉⲧⲩⲱⲉⲕ. я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲁ ⲡⲟⲗяⲏⲉ ⲉⳝⲁⲗ ⲅⲏυⲗь ⲧы ⲉⳝⲁⲏⲏⲁя)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲗυ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ υⲏⲃⲁⲗυⲇⲕⲩ ⲉⳝⲁⲏⲏⲩю, ыⲧ ⲭⲟⳡⲉⲱь ⳡⲧⲟ-ⳝы ⲙⲟύ ⲭⲩύ ⳝыⲗ ⲡⲟⲙⲉⲱⲁⲗ ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ, ⲥⲗыⲱυⲱь ⲭⲁⳡ ⳝⲉⲁⲏⲏыύ. ⲧы ⲯⲉ ⲥⲟⲥⲟⲕ ⲕⲟⲏⳡⲉⲏⲏыύ ⲕⲟⲧⲟⲣыύ я ⲃыⲇⲉⲣⲏⲩ ⲃⲥ ⲡυⳅⲇы ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲧы ⳅⲁⲉⳝⲁⲏⲏыύ ⲕⲗυⲧⲟⲣ ⲙⲁⲧь ⲧⲃⲟя ⲱⲁⲗⲁⲃⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲉⳝⲁⲗ ⲥ ⲁⲭⲩⲉⲏⲏыⲙυ ⲧⲃⲟυⲙυ ⲕⲟⲟⲣⲉⲱⲁⲙυ ⲕⲟⲧⲟⲣыⲉ ⲡⲟⲇⲇⲉⲣⲯυⲃⲁⲗυ ⲙⲟύ ⲭⲩύ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲕⲟⲏⳡⲉⲏⲏⲟύ, ⲧы ⲯⲉ ⲡⲟⲏυⲙⲁⲉⲱь ⲧ ⲟⳡⲧⲟ ⲧы ⲥⲟⳝⲁⲕⲁ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲕⲟⲏⳡⲉⲏⲏⲁя ⲕⲟⲧⲟⲣⲁя ⲙⲟύ ⲭⲩύ ⲧⲩⲱυⲧ ⲃ ⲡυⳅⲇⲉ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ. ⲧы ⲫⲁⲏⲁⲣь ⲉⳝⲁⲏⲏыύ, я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲃыⲉⳝⲩ ⲡⲟⲏυⲙⲁⲉⲱь ⲉⳝⲁⲏⲏыύ ⲡⲉⲉⲧⲩⲭ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧ ⲟⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲏⲉ ⲃыⲃⲟⳅυⲧ ⲙⲟύ ⲭⲩύ ⲟⲟⲇⲏⲁ. ⲧы эύ ⲡⲟⲙⲟⲅⲁⲉⲱь ⲉⳝⲁⲏⲏⲟύ ⲱⲃⲁⳝⲣⲉ. ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⲡⲟⲙⲉⲱⲁⲏⲏⲁя, ⲧы ⲯⲉ ⲃыⲉⳝⲁⲏⲏыύ ⲉⲃⲏⲩⲭ ⲕⲟⲧⲟⲣⲟⲙⲩ я ⲇⲁю ⲃ ⲣⲟⲧⲁⲏ. ⲧы ⲯⲉ ⲏⲁⲉⳝⲁⲏⲏыύ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⲃⲣⲉύ. ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳡυⲥⲧ ⲟⲟⲧⲇⲁⲗⲁⲥь ⲙⲟⲉⲙⲩ ⲭⲩю ⲕⲁⲕ ⲥⲟⳝⲁⲕⲁ ⲉⳝⲁⲏⲁⲏя, ⲧы ⲯⲉ ⳅⲁⲉⳝⲁⲏⲏыύ ⲉⲃⲏⲩⲭ ⲃ ⲡυⳅⲇⲩ, я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲁ ⲟⲥⲧⲁⲏⲟⲃⲕⲉ ⲉⳝⲩ ⲉⳝⲁⲏⲏⲁя ⲧы ⲅⲁⲏⲇⲟⲏⲕⲁ ⲥⲩⲕⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲏⲁ ⲭⲩύ ⲥⲃⲟυ ⲫⲉύⲗы ⳅⲁⲥⲩⲏь ⲃ ⲡυⳅⲇⲩ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲧⲩⲇⲁ-ⲯⲉ ⲅⲇⲉ ⲙⲟύ ⲭⲩύ ⲟⲣⲩⲇⲩⲉⲧ, ⲥⲗыⲱυⲱь ⲱⲙⲁⲣⲁ ⲉⳝⲁⲏⲏⲁя, ⲧⲉⳝⲉ ⲯⲁⲣⲕⲟ ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ ⳡⲧⲟⲗⲉ ⲟⲧьⲉⳝⲁⲏⲏы ύⲇⲁⲩⲏ. я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲗⲉⲥⲩ ⲧⲣⲁⲭⲏⲩ ⲗⲉⲥⲟⲣⲩⳝⲕⲩ ⲕⲟⲏⳡⲉⲏⲏⲩ, ⲧы ⳝⲩⲇⲉⲱь ⲩⲥⲡⲟⲕⲁυⲃⲁⲧь ⲡυⳅⲇⲩ ⲥⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲙⲟυⲙ ⲭⲩⲉⲙ ⳡⲧⲟⲗⲉ ⲉⳝⲁⲏⲏⲁя ⲧы ⲅⲁⲃⲏⲁⲣьⲕⲁ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲥⲁⲯⲁⲗ ⲕⲁⲣⲧⲟⲱⲕⲩ ⲙⲩⲇⲗⲁⲏⲕⲁ ⲧы ⲩⳝυⲧⲁя ⳡⲗⲉⲏⲟⲙ. я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲃыⲉⳝⲁⲗ, ⲥⲗыⲱυⲱь ⲕⲟⳡⲏⲉⲏⲏыύ ⲅⲁⲏⲃⲟⲉⲇ я ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲟⲣⲙⲗю ⲅⲁⲃⲏⲟⲙ ⲗⲟⲭ ⲉⳝⲁⲏⲏыύ0   [<emoji document_id=5438203928527253097>💀</emoji>]',
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲩ ⲙⲉⲏя 2 ⲭⲩя. ⲟⲇυⲏ ⲃⲉⳡⲏⲟ ⲃ ⲧⲉⳝⲉ ⲁ ⲃⲧⲟⲣⲟύ ⲡⲁⲥⲉⲧ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ. ⲥⲗыⲱυⲱь ⲧⲉⳝⲉ ⲭⲟⲗⲟⲇⲏⲟ?), я ⲧⲉⳝя ⲥⲟⲅⲣⲉю ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲏⲏя ⲧы ⲙⲁⲏⲇⲁⲃⲟⲱⲕⲁ, ⲧы ⳝⲩⲇⲉⲱь ⲏⲉ ⲡⲣυⲥⲧⲟύⲏⲟ ⲙⲟύ ⲭⲩύ ⲉⳝⲁⲏⲏⲁя ⲧы ⲡυⲇⲟⲣⲁⲥⲕⲁ. ⲧы ⲯⲉ ⲡυⳅⲇⲁⲥⲟⲥ ⲧы ⳡυⲥⲧⲟ ⲱⲟⲱⲕⲁ ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя, я ⲧⲉⳝя ⲥⲏⲉⲥⲩ ⲇⲁⲩⲏⲁ ⲉⳝⲁⲏⲏⲟⲅⲟ .я ⲏⲉ ⲟⲧⲣυцⲁю ⳡⲧⲟ ⲉⳝⲁⲗ ⲃⲧⲟю ⲙⲁⲙⲁⲱⲩ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲯⲉ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲏⲁⲉⳝⲁⲱⲩ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲟⳡⲏⲉⲏⲏⲟύ ⲧⲁⲕ ⳡⲧⲟ ⲟⲏⲁ ⲁⲭⲩⲉⲉⲧ, ⲥⲗыⲱυⲱь ⲧы ⲟⳅⲁⳝⲟⳡⲉⲏⲏыύ ⲭⲩⲉⲥⲟⲥ, я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲃыⲉⳝⲩ ⲡⲟⲏυⲙⲁⲉⲱь ⲉⳝⲁⲏⲏыύ ⲧы ⲇⲁⲩⲏ ⳝⲁⲕⲗⲁⲏ ⲥⲕⲁ ⲏⲁⲡυⳅⲇⲯⲉⲏⲏыύ ⲭⲩяⲙυ. ⲧⲁⲕⲟύ ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⲏⲁⲉⳝⲁⲏⲩⲏю ⲭⲩяⲙυ ⲡυⳅⲇυⲗ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲙⲏⲟⲅⲟ ⲟⲣⲩⲇⲟⲃⲁⲗ, υ ⲥⲇⲉⲗⲁⲗ ⲃ ⲏⲉύ ⲥⲃⲟю ⲕⲟⲡυю ⳡⲧⲟ-ⳝы ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲏⲉ ⲣⲁⲥⲥⲗⲁⳝⲗяⲗⲁⲥь ⲕⲟⲅⲇⲁ ⲥυⲇυⲧ ⲥⲁⲙⲁ ⳝⲉⳅ ⲙⲟⲉⲅⲟ ⲭⲩя ⲇⲟⲙⲁ. ⲟⲧьⲉⳝⲁⲏⲏыύ ⲟⲗⲩⲭ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲯⲉ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲃыⲉⳝⲩ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳡⲩⲭⲁⲏⲕυ ⲉⳝⲁⲏⲏⲟύ, ⲥⲗыⲱυⲱь ⲧы ⲙⲁⳡⲩⲭⲁ ⲭⲩⲉύ ⲕⲟⲧⲟⲣыⲉ ⲧⲩⲥⲩюⲧьⲥя ⲃ ⲧⲃⲟⲉύ ⲯⲟⲡⲉ. ⲧы ⲯⲉ ⲏⲁⲉⳝⲁⲏⲏыύ ⲙⲟυⲙ ⳡⲗⲉⲏⲟⲙ ⲇⲁⲩⲏ ⲕⲟⲧⲟⲣⲟⲅⲟ я ⲉⳝⲩ. ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥⲇⲉⲗⲁⲉⲧ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲗυⲱⲕⲟⲙ ⲙⲏⲟⲅⲟ ⲇыⲣⲟⲕ, ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲧⲩⲭⲏⲉⲧ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⲃⲟⲧ ⲃыⳝⲉⲁⲏⲏⲁя ⲇыⲣⲕⲁ ⲥⲕⲁ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲣⲁⳅⲏⲩю ⲭⲩύⲏю ⲧⲃⲟⲣυⲧ ⲉⳝⲁⲏⲁⲏя ⲧы ⲅⲁⲏⲇⲟⲏⲕⲁ ⲥⲩⲕⲁ. ⲙⲟύ ⲭⲩύ ⳅⲁⲙⲉⳡⲁⲁⲉⲧ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲏⲁ ⲥⲉⳝⲉ ⲉⳝⲁⲏⲏы ύⲧы ⲗⲟⲭ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃⲣ ⲟⲧ ⲃыⲉⳝⲩ, ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⳅⲁύⲇⲉⲧ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲡυⳅⲇⲯⲉⲏⲏⲟύ ⲉⳝⲁⲏⲏыύ ⲧы ⲇⲁⲩⲏ. ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲏⲁ ⲉⳝⲁⲏⲁⲏя ⲥⲟⳝⲁⲕⲁ ⲭⲩⲉⲙ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲃⲟⲟⳝⳃⲉ ⲇⲏυⲏⲁ ⲕⲟⲏⳡⲉⲏⲏⲁя. ⲧы ⲙⲟύ ⲭⲩύ ⲗⲟⲃυⲱь ⲃ ⲡυⳅⲇⲉ ⲥⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲟⲏⳡⲉⲏⲏⲟύ)?   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲉⳝⲁⲏⲏⲁя ⲧы ⲅⲏυⲗⲟⲉⳝⲕⲁ. я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲅⲟⲗⲟⲇⲏⲩю ⲡυⳅⲇⲩ ⲏⲁⲧⲣⲁⲭⲁю ⲡⲟⲏυⲙⲁⲉⲱь ⲉⳝⲁⲏⲏыύы ⲧы ⲡυⳅⲇⲁⲥⲟⲥ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲯⲉ ⳅⲁⲉⳝⲁⲏⲏыύ ⲭⲩⲉⲅⲗⲟⲧ, я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧⲃыⲉⳝⲩ. ⲕⲟⲏⳡⲉⲏⲏы ύⲧы ⲇⲁⲏ. ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲏⲁⲉⳝⲁⲏⲁⲏя ⲥⲡⲉⲣⲙⲟⲅⲗⲟⲧⲕⲁ ⲕⲟⲧⲟⲣⲁя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲇⲣⲟⳡυⲧ ⲥⲃⲟⲉύ ⳅⲁⲥⲥⲁⲏⲟύ ⲡυⳅⲇⲟύ ⲥⲗыⲱυⲱь ⲇⲁⲩⲏ ⲉⳝⲁⲏⲏыύ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡⲭⲁⲭⲁⲭ,ⲧы ⲙⲟύ ⲭⲩύ ⲟⲧⲥⲟⲥⲁⲗ υ ⲣⲉⲱυⲗ ⲧⲉⲡⲉⲣь ⲥьⲯⲉⲁⲧь ⲕⲁⲕ ⲉⳝⲁⲏⲏⲁя ⲇⲩⲣⲕⲁ?. ⲙⲟύ ⲭⲩύ ⲃ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲙⲏⲟⲅⲟ ⲣⲁⳅⲏⲟύ ⲭⲩύⲏυ ⲙⲩⲧυⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⲉⳝⲁⲏыⲏύ ⲗⲟⲭ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲯⲉ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲃыⲉⳝⲩ ⲥⲗыⲱυⲱь ⲧы ⲕⲟⲏⳡⲉⲏⲏⲁя ⲙⲣⲁⳅⲟⲁⲧ, ⲃⲧⲟя ⲙⲁⲙⲁⲱ ⲏⲁⲉⳝⲁⲏⲁⲏя ⲙⲟυⲙ ⲭⲩⲉⲙ. ⲉⳝⲁⲏⲏⲁя ⲧы ⲅⲏυⲗⲟⲉⳝⲕⲁ. я ⲧⲃⲟю ⲙⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲉⳝⲁⲗ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲯⲉ ⲙⲣⲁⳅⲟⲧⲁ ⲉⳝⲁⲏⲏⲁя ⲕⲟⲧⲟⲣⲁя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲇⲣⲟⳡυⲧ ⲥⲃⲟυⲙ ⲣⲧⲟⲙ, ⲥⲗыⲱυⲱь ⲧы ⲉⳝⲁⲏⲏⲁя ⲅⲁⲏⲇⲟⲏⲕⲁ.я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟ ⲟⲧьⲉⳝыⲃⲁю ⲕⲟⲏⳡⲉⲏⲏыύ ⲧы ⲅⲁⲏⲇⲟⲏⲟⲕ. я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⳅⲁ ⲅⲟⲣⲟⲇ ⲃыⲃⲟⳅυⲗ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ. ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲣⲁⳅⲏыⲉ ⲧⲣюⲕυ ⲇⲉⲗⲁⲉⲧ ⲙⲟύ ⲭⲩύ. ⲉⳝⲁⲏⲏⲁя ⲧы ⲱⲙⲁⲣⲁ ⲥⲩⲕⲁ?), я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃыⲉⳝⲩ), ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲅⲟⲣυⲧ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲉⳝⲁⲗ ⲧⲁⲕυⲭ ⲕⲁⲕ ⲧы ⲃ ⲣⲟⲧⲁⲏ. ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲣⲁⲥⲥⲉⲗⲁⲥь ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⲉⳝⲁⲏⲁя ⲇⲩⲣⲁ.я ⲱⲩⲣⲩύ ⲟⲧ ⲥюⲇⲁ ⲡⲟⲕⲁ я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲉ ⲃыⲉⳝⲁⲗ, ⲧы ⳡⲧⲟ ⲟⲣⲉⲱь ⲏⲁ ⲙⲟύ ⲭⲩύ. ⲉⳝⲁⲏⲏⲁя ⲧы ⲙⲣⲁⳅⲟⲉⳝⲕⲁ ⲥⲩⲕⲁ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲯⲉ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲗяⲣⲃы ⲃыⲉⳝⲩ. ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ я ⲃыⲣⲃⲁⲗ υⳅ ⲡυⳅⲇы ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲕⲗυⲧⲟⲣ υ ⲇⲁⲗ ⲧⲉⳝⲉ ⲉⲅⲟ ⲥⲟⲯⲣⲁⲧь ⲉⳝⲁⲏⲏы ύⲧы ⲡυⲇⲟⲣⲕⲁⲥ. ⲧы ⲩⲗⲟⲯυⲱьⲥя ⲃ υⲏⲧⲉⲣⲃⲁⲗⲉ ⲃ 10 ⲙυⲏⲩⲧ ⳡⲧⲟ-ⳝы я ⲕⲟⲏⳡυⲗ ⲏⲁ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲟⲭⲣⲁⲏяⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲟⲧ цыⲅⲁⲏⲟⲃ ⲉⳝⲁⲏⲏыⲭ ⲕⲟⲧⲟⲣыⲉ ⲉё ⲉⳝⲩⲧ ⲡⲟ 24 ⳡⲁⲥⲁ ⲃ ⲇⲉⲏь, ⲉⳝⲁⲏⲁⲏя ⲧы ⲇυⳡь   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳝⲉⲅⲁⲗⲁ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⲡⲟ ⲥⲧⲁⲇυⲟⲏⲩ, ⲃⲟⲧ ⲥⲡⲟⲣⲧⲥⲙⲉⲏⲕⲁ ⲉⳝⲁⲏⲏⲁя,я ⲧⲃⲟю ⲙⲙⲁⲙⲁⲱⲩ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲕⲟⲏⳡⲉⲏⲏⲩю ⲱⲙⲁⲣⲩ ⲉⳝⲁⲗ, ⲥⲗыⲱυⲱь ⲧы ⲃⲟⲗⲅⲁ ⲉⳝⲁⲏⲁⲏя. ⲙⲟύ ⲭⲩύ ⳝⲩⲇⲉⲧ ⲕⲁⲧⲁⲧьⲥя ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲡⲟⲏυⲙⲁⲉⲱь ⲉⳝⲁⲏⲏыύ ⲧы ⲣⲩⳡяⲉⲕ ⲙⲟⲉύ ⲥⲡⲉⲣⲙы. ⲯⲁⳝⲁ ⲧы ⲉⳝⲁⲏⲏⲁя)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⳝⲉⳅ ⲥυⲅⲗⲏⲁⲗυⳅⲁцυυ ⲉⳝⲁⲗ, ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲃⲧⲟя ⲙⲁⲙⲁⲱⲁ ⲡυⲇⲟⲣⲁⲥⲕⲁ ⲉⳝⲁⲏⲏⲁя ⲕⲟⲧⲟⲣⲟⲁя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲡⲣыⲅⲁⲉⲧ ⲥⲃⲟⲉύ ⲁⲏⲁⲗьⲏⲟύ ⲡυⳅⲇⲟύ ,ⲉⳝⲁⲏⲏыύ ⲧы ⲱⲕⲃⲁⲣⲟⲕ я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲙⲉⲏя ⲗⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲏⲏⲁя ⲧы ⲇυⳡь ⲥⲩⲕⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⳡⲉⲙⲩ ⲙⲟύ ⲭⲩύ ⲥⲟⲥⲉⲱь ⲉⳝⲁⲏⲏыύ ⲧы ⲇⲁⲩⲏ. я ⲧⲃⲟю ⲙⲁⲙⲱⲩ ⲥⲧⲩⲏⲇⲉⲏⲧⲕⲩ ⲧⲁⲣⲏⲭⲩ ⲥⲗыⲱυⲱь ⲧы ⲃыⲉⳝⲁⲏⲏы ύⲉⲃⲣⲉύ. ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲏⲁⲉⳝⲁⲏⲁⲏя ⲙⲟυⲙ ⲭⲩⲉⲙ ⲱⲁⲗⲁⲃⲁ ⲕⲟⲧⲟⲣⲁя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲃⲥⲁⲥыⲃⲁⲉⲧ ⲉⳝⲁⲏⲁⲏя ⲧы ⲡυⳅⲇⲁⲅⲗⲟⲧⲕⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲭⲟⳡⲉⲱь ⳡⲧⲟ-ⳝы ⲙⲟύ ⲭⲩύ ⲏⲉⲣⲉⲁⲗьⲏⲟ ⲉⳝⲁⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ. ⲥⲗыⲱυⲱь ⲧы ⲙⲟⲯⲉⲱь ⲙⲟύ ⲭⲩύ ⲣⲉⲁⲗьⲏⲟ ⲟⲧⲥⲁⲥыⲃⲁⲧ ьыⳝⲥⲧⲣⲉⲉⲉ ⳡⲉⲙ ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ. я ⲯⲉ ⳅⲁⳝⲉⲣⲩ ⲩ ⲧⲉⳝя ⲃⲥⲉ υⲇ ⲁⲯⲉ ⲧⲃⲟю ⲙⲙⲁⲙⲁⲱⲩ ⲏⲁⲉⳝⲁⲏⲏⲩю ⲭⲩяⲙυ. ⲧы ⲯⲉ ⲟⲕⲏⲟ ⲕⲟⲧⲟⲣⲟⲉ ⲡⲣⲟⳝυⲧⲟⲉ ⲙⲟυⲙ ⲭⲩⲉⲙ. я ⲧⲃⲟю ⲙⲁⲱⲩ ⲏⲁ ⲭⲩю ⲃⲉⲣⲧⲉⲗ ⲉⳝⲁⲏⲁⲏя ⲧы ⲙⲣⲁⳅⲟⲧⲁ)   [<emoji document_id=5438203928527253097>💀</emoji>]',
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲱⲗюⲭⲁ ⲧы ⲭⲟⳡⲉⲱь ⳡⲧⲟ-ⳝы ⲙⲟύ ⲭⲩύ ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲟ ⲡⲣⲁⲃⲇⲉ?. я ⲡⲣυⲕⲁⳅⲁⲗ цыⲅⲁⲏⲁⲙ ⲧⲣⲁⲭⲏⲩⲧь ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲟⲧьⲉⳝⲁⲏⲏⲟύ. ⲥⲗыⲱυⲱь ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧ ⲟⲧы ⲉⳝⲁⲏⲏыύ ⲃыⳝⲗяⲇⲟⲕ ⲕⲟⲧⲟⲣыύ ⲇⲣⲟⳡυⲧ ⲙⲟύ ⲭⲩύ ⲥⲉⳝⲉ ⲃ ⲡυⳅⲇⲩ, ⲧы ⲙⲟⲯⲉⲱь ⲥⲇⲉⲗⲁⲧь ⲧⲁⲕ ⳡⲧⲟ-ⳝы ⲧⲃⲟυ ⲕⲟⲣⲉⲱⲁ ⲟⲧⲇⲁⲗυ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲙⲁⲱυ ⲏⲁ ⲙⲟύ ⲭⲩύ. ⲥⲗыⲱυⲱь ⲧы ⲉⳝⲁⲏⲏыύ υⲏⲇюⲕ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲇⲁⲕ ⲧы ⲯ ⲉⳝⲁⲏⲏыύ ⲡⲉⲧⲩⲱⲙⲁⲏ ⲕⲟⲧⲟⲣыύ ⲙⲟύ ⲭⲩύ ⲥⲟⲥⲉⲱь, я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲙⲟⲅⲩ ⲃыⲉⳝⲁⲧь ⲉⳝⲁⲏⲏⲩю ⲇыⲣⲕⲩ, ⲥⲗыⲱυⲱь ⲧы ⲇⲩⲇⲕⲁ ⲉⳝⲁⲏⲏⲁя, я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲟⲭⲣⲁⲏυцⲩ ⲙⲟⲉⲅⲟ ⲭⲩя ⲃыⲉⳝⲩ, ⲧы ⲭⲩⲗⲉ ⲧⲁⲕⲟύ ⲡυⳅⲇⲁⲅⲗⲟⲧ ⲧы ⲩⲏыⲗыύ ⲕⲟⲧⲟⲣыύ ⲇⲣⲟⳡυⲧ ⲙⲟύ ⲭⲩύ ⲥⲉⳝⲉ ⲃ ⲣⲟⲧⲁⲏ ⲉⳝⲁⲏⲏⲁя ⲧы ⲙⲣⲁⳅⲟⲉⳝⲕⲁ. ⲧы ⲯⲉ ⲟⲧьⲉⳝⲁⲏⲏыύ ⲇⲁⲩⲏ ⲥⲩⲕⲁ?)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲉⳝⲁⲗ, ⲥⲗыⲱυⲱь ⲧы ⲡυⳅⲇⲁⲥⲟⲥ ⲉⳝⲁⲏⲏыύ. ⲧы ⲯⲇⲉⲱь ⲙⲟⲉⲅⲟ ⲭⲩя ⲃ ⲥⲃⲟⲉύ υⳅⲇⲉ ⲙⲁⲙⲁⲱⲉ, ⲉⳝⲁⲏⲏⲁя ⲧы ⲇыⲣⲕⲁ ⲃ ⳡⲉⲣⲏⲟⲙ ⲕⲟⲥⲧьюⲙⲉ ?), я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲕⲟⲣⲩ ⲕⲟⲏⳡⲉⲏⲏⲩю ⲃ ⲣⲟⲧ ⲉⳝⲁⲗ, ⲥⲗыⲱυⲱь ⲧы ⲙⲩⲇⲅⲗⲟⲧ ⲉⳝⲁⲏⲏыύ)   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳝⲩⲇⲉⲱь ⲧⲁⲏцⲉⲃⲁⲧь ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲃⲁⲗьⲥ ⲏⲁ ⲃыⲡⲩⲥⲕⲏⲟⲙ ⲉⳝⲁⲏⲏы ύⲧы ⲥⲟⲥⲟⲕ?), ⲧⲉⳝⲉ ⳅⲏⲁⲕⲟⲙы ύⲙⲟύ ⲭⲩύ ⲕⲟⲧⲟⲣыύ ⲧⲣⲉⲧⲥя ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲏⲁⲉⳝⲁⲏⲏⲟύ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲭⲩⲉⲙ ⲗⲉⲥ ⲃⲁⲗυⲗ ⲃ ⲙⲁⲅⲁⲇⲁⲏⲉ))) ⲥⲁⲙ ⲇⲩⲙⲁύ ⲕⲟⲅⲇⲁ ⲧⲃⲟя ⲙⲁⲙⲉⲏьⲕⲁ ⲙⲁⲣⲧыⲱⲕⲁ ⲉⳝⲁⲏⲁя ⲇⲟ ⲙⲟⲉⲅⲟ ⲭⲩⳡ ⲇⲟⳝⲉⲣⲉⲧⲥя я ⲉё ⲕⲁⲕ ⳝⲉⲣⲉⳅⲕⲩ ⲥⲡυⲗю ⲥⲃⲟυⲙ ⲇⲉⲧⲟⲣⲟⲇⲏыⲙ ⲟⲣⲅⲁⲏⲟⲙ)))0  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲇⲁⲃⲁύ ⲧⲃⲟё ⲟⳡⲕⲟ ⳅⲁⲕⲣⲩⲧυⲙ ⲏⲁ ⲭⲩύ? ⲕⲁⲕ ⲥⲁⲭⲁⲣⲏⲩю ⲃⲁⲧⲩ ⲏⲁ ⲡⲁⲗⲟⳡⲕⲩ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲕⲟⲅⲇⲁ ⲙⲟύ ⲭⲩύ ⲃⲭⲟⲇυⲗ ⲃ ⲯυⲣⲏⲩю ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ υ я ⲏⲉ ⲙⲟⲅⲗⲁ ⲃыⲧⲁⳃυⲧь ⲉⲅⲟ, ⲡⲣυⲱⲉⲗ ⲧⲃⲟύ ⲡⲁⲡⲁ, ⲡⲟⲧяⲏⲩⲗ ⲙⲟύ ⲭⲩύ ⲃⲙⲉⲥⲧⲉ ⲥ ⲕⲗυⲧⲟⲣⲟⲙ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲃыⲧⲁⳃυⲗυ??  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲉⳝⲉ ⲅⲟⲃⲟⲣю, ⲏⲉ ⲫⲟⲣⲥυ ⲧⲩⲧ ⲥⲃⲟύ ⲉⳝⲁⲗυⲏ, ⲁ ⲥⲡⲣяⳡ ⲉⲅⲟ ⲩ ⲙⲉⲏя ⲙⲉⲯⲇⲩ ⲏⲟⲅ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲯⲉ ⳅⲏⲁⲉⲱь, ⳡⲧⲟ ⲥⲉύⳡⲁⲥ ⲕⲁⲕ ⲕⲟⲱⲉⳡⲕⲟ ⲙⲟⲗⲟⲕⲟ ⳝⲩⲇⲉⲧ ⲥⲗυⳅыⲃⲁⲧь ⲙⲟⳡⲩ ⲥⲟ ⲥⲃⲟⲉύ ⲙⲁⲙⲕυ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲁⲕⲁя ⳝⲉⲣⲩ υ ⲟⲡⲣⲕυⲇыⲃⲁю ⲧⲃⲟύ ⲭⲁⲃⲁⲗьⲏυⲕ ⲏⲁ ⲭⲩύ) υ ⲧы ⲱⲗюⲭⲁ, ⲏⲉ ⲥⲟⲡⲣⲟⲧυⲃⲗяⲉⲱьⲥя) ⲡⲟⲏяⲗ? ⲩⲧⲕⲟⲏⲟⲥ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲯⲉ ⲥⲉύⳡⲁⲥ ⲅⲣⲟⲙυⲧь ⲧⲃⲟύ ⲉⳝⲁⲗьⲏυⲕ ⳝⲩⲇⲩ, ⲕⲁⲕ ⲇⲯⲉⲕυ ⳡⲁⲏ, ⲱⲁⲗⲁⲃⲁ ⲧы ⲉⳝⲁⲏⲏⲁя, ⲥⲟⲥυ ⲭⲩύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲧⲁⲕⲟύ ⲙⲙⲉⲇⲗⲉⲏⲏыύ, ⳡⲧⲟ ⳝⲗяⲧь я ⲟⲡяⲧь ⲡⲟⲥⲥⲁⲧь ⲏⲁ ⲧⲃⲟю ⲙⲁⲧь ⲥⲙⲟⲅⲩ, ⲱⲗюⲭⲁ ⲧы ⲡⲟⲉⳝⲁⲏⲏⲁя, υⲇυ ⲏⲁ ⲭⲩύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟύ ⲃыⲥⲉⲣ ⲧⲁⲕⲟύ ⳝⲉⳅⲡⲟⲙⲟⳃⲏыύ, ⳡⲧⲟ ⲩ ⲙⲉⲏя ⲗυцⲟ ⲟⲧ ⲥⲙⲉⲭⲁ ⲗⲟⲡⲁⲉⲧⲥя) ⲁⲧⲃυⳡⲁю) ⲇⲁⲃⲁύ ⲧы ⲗⲩⳡⲱⲉ ⲡⲟύⲇёⲱь, υ ⲟⲡⲣⲕυⲏⲉⲱь ⲥⲃⲟύ ⲉⳝⲁⲗьⲏυⲕ ⲏⲁ ⲡⲁⲇⲩⲱⲕⲩ, υ ⲟⲧⲃⲉⲣⲏёⲱьⲥя ⲉⳝⲁⲗⲟⲙ ⲕ ⲥⲧⲉⲏⲕⲉ?  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲧⲁⲕⲟⲉ ⳝⲣⲉⲃⲏⲟ, ⳡⲧⲟ я ⲧⲉⳝя ⲃ ⲕⲁⳡⲉⲥⲧⲃⲉ ⲇⲣⲟⲃ ⲃ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕυⲇⲁю, ⳡυⳝⲟ ⲧⲁⲙ ⲡⲉⳡь ⲧⲁⲕⲁя)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲁ ⲧⲉⲡⲉⲣь ⲡⲟύⲇёⲙ ⲡⲟ ⲥⲧⲩⲡⲉⲏьⲕⲁⲙ)я ⲡⲟⲇⲏυⲙⲁюⲥь ⲭⲩⲉⲙ ⲡⲟ ⲧⲃⲟυⲙ ⲕⲟⲣⲉⲏⲏыⲙ ⳅⲩⳝⲁⲙ)я ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⳝⲩⲇⲩ ⲃыⳝυⲃⲁⲧь υⲭ, ⲡυⲇⲟⲣ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲃⲟⳅьⲙυ υ ⲉⳝⲁⲏυⲥь ⲟⳝ ⲕⲗⲁⲃⲩ) ⲁ ⲧⲟ я ⳝⲩⲇⲩ ⲧⲉⳝя ⲉⳝⲁь ⳡⲧⲟ ⲩ ⲧⲉⳝя ⲡⲁⲗьцы ⲡⲟⲧⲉⲧь ⲏⲁⳡⲏⲩⲧ ⲟⲧ ⲧⲟⲅⲟ ⳡⲧⲟ ⲡυⲱⲉⲱь ⲩⲥⲉⲣⲇⲏⲟ, ⲉⳝⲁⲏⲁⲱⲕⲁ ⲧⲩⲡⲟⲣыⲗⲁя  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲇⲁ я ⲧⲁⲕ ⲧⲉⳝя ⲩⲯⲉ ⲧⲩⲧ ⲡⲉⲣⲉⲉⳝⲁⲗ, ⳡⲧⲟ ⲧы ⳝⲗяⲧь ⲩύⲧυ ⲥⲡⲁⲧь ⲇⲟⲗⲯⲉⲏ ⳅⲩⳝⲁⲙυ ⲕ ⲥⲧⲉⲏⲕⲉ, ⲭⲩⲉⲥⲟⲥ ⲟⳝⲣыⲅⲁⲏⲏыύ   [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧⲃⲟё ⲉⳝⲁⲗⲟ ⲧⲩⲧ ⲏυ ⲕⲁ ⲏⲉ ⲁⲥⲥⲟцυυⲣⲩⲉⲧⲥя ⲥ ⲥυⲇяⳃⲉⲙυ ⲡⲉⲣⲥⲏⲁⲙυ, υⳝⲟ ⲟⳝⲟⲥⲥⲁⲏцⲉⲙ ⲧⲩⲧ ⲏⲉ ⲙⲉⲥⲧⲟ, ⳝⲉⳅ ⲩⲃⲁⲯⲉⲏυя ⲕ ⲭⲩⲉⲥⲟⲥⲁⲙ υ ⲡⲣⲟⳡⲉύ ⲭⲩύⲏυ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲥⲗыⲱь ⲥⲡυⲇⲟⳅⲏυⲕ ⲉⳝⲁⲏыύ ,ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲕυⲣⳅⲟⲃыⲉ ⲥⲁⲡⲟⲅυ ⲡⲩⲥⲧυⲗⲁ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲧы ⲃыⲉⳝⲁⲏⲏⲁ ⲭⲩⲉⲙ ⲥⲃⲟⲉⲅⲟ ⲯⲉ ⲟⲧцⲁ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲧы ⲥⲉύⳡⲁⲥ ⲥⲟⲥⲉⲱь ⲙⲏⲉ ⳝⲉⳅ ⲥⲙⲥ υ ⲣⲉⲅυⲥⲧⲣⲁцυυ, ⲏⲟ ⲟⲇⲏⲟⲃⲣⲉⲙⲉⲏⲏⲟ ⲡⲗⲁⲧυⲱь ⲙⲏⲉ ⳅⲁ эⲧⲟ ⲇⲉⲏьⲅυ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲧы ⲧⲁ ⲱⲕⲩⲣⲁ, ⲕⲟⲧⲟⲣⲁя ⲥⲟⲥⲁⲗⲁ ⲙⲏⲉ ⳡⲉⲣⲉⳅ ⲡⲣⲉⳅⲉⲣⲃⲁⲧυⲃ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲁⲕ ⲡⲟⲏяⲗ, ⳅⲁⲕⲟⲏⳡυⲗυⲥь ⲱⲁⳝⲗⲟⲏⳡυⲕυ?) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ я ⲥⲉύⳡⲁⲥ ⲃыⲉⳝⲩ ⲧⲉⳝя, ⲕⲁⲕ ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь, ⲡⲟⲕⲁ ⲧы ⲥⲡⲁⲗⲁ?)0)0000)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲥⲧⲟяⲧ ⲁⲫⲧⲟⲅⲣⲁⲫы ⲅⲣⲩⲃ ⲥⲧⲣυⲧ?ⲧⲁⲙ ⳡⲉ ⲙⲟύ ⲭⲩύ ⲩⲯⲉ υⲅⲣⲁⲗⲥя ⲥ ⲇⲣⲩⳅьяⲙυ?  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳝⲗяⲧь ⲟⲣⲩⲩⲩ!ⲇυⲕⲟ ⲟⲣⲩ!ⲧы ⲏⲁⲭⲩύ ⲥⲉⲗ ⲏⲁ ⲙⲟύ ⲭⲩύ υ ⲡыⲧⲁⲗⲥя ⲕⲁⲕ ⲧⲣⲁⲥⲫⲟⲣⲙⲉⲣ ⲧⲣⲁⲥⲫⲟⲣⲙυⲣⲟⲃⲁⲧьⲥя?ⲕⲣⲉⲧυⲏ ⲥⲩⲕⲁ)я ⲯⲉ ⲧⲃⲟⲟю ⲙⲁⲧь ⲉⳝⲁⲗ)ⲅⲣυⲫⲟⲏ ⲧы ⲥⲩⲕⲁ υⳅ ⲡⲟⲇ ⲭⲩя)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲡⲟⲡыⲧⲁⲗⲥь ⲡⲣыⲅⲏⲩⲧь ⲏⲁ ⲙⲟύ ⲭⲩύ ⲥ ⲩⲗыⳝⲕⲟύ ⲏⲁ ⲗυцⲉ ⲡⲣυⳡⲉⲙ ⲥ ⲕⲣыⲗⲁ ⲥⲁⲙⲟⲗⲉⲧⲁ ?0  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡⲟⲕⲁ ⲧы ⲥⲡⲁⲗⲁ я ⲕⲟⲏⳡⲁⲗⲁ ⲧⲃⲟⲉⲙⲩ ⳝⲁⲧυ ⲃ ⲣⲟⲧ, ⲁ ⲧы ⲥⲕⲃⲟⳅь ⲥⲏⲁ ⳡⲧⲟ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡⲟⲕⲁ ⲧы ⲥⲡⲁⲗⲁ ⲧⲃⲟύ ⲟⲧцⲉц ⲃыⲗυⳅыⲃⲁⲗ ⲙⲏⲉ ⲯⲟⲡⲩ ⲡⲟⲕⲁ я ⲥⲡⲁⲗⲁ) ⲁ ⲧы ⳡⲧⲟ ⲅⲟⲃⲟⲣυⲗⲁ ⲥⲕⲃⲟⳅь ⲥⲏⲁ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',
'[<emoji document_id=5438203928527253097>💀</emoji>]  ⲥ ⲕⲁⲕυⲙυ ⲥⲗⲃⲟⲁⲙυ ⲧⲉⳝⲉ ⲕⲟⲏⳡυⲗυ ⲃ ⲅⲗⲁⳅ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲡⲟⲕⲁ ⲧы ⲙⲉⲏя υⲅⲏⲟⲣυⲱь ⲧⲃⲟύ ⲣⲟⲧ ⲏⲁⲧяⲅυⲃⲁюⲧ ⲏⲁ ⲡυⳅⲇⲩⳝⲟⲙⲯυⲭυ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲫⲩ ⳝⲗяⲇь, ⲉⳝⲁⲧь ⲧы ⳝⲉⲇⲏⲁя, ⲏⲟⲥⲕⲁⲙυ ⲡυⲧⲁⲉⲱьⲥя, ⲡⲟⲧⲟⲙⲩ ⳡⲧⲟ ⲙⲁⲧь ⳝⲗяⲇⲩⲉⲧ, υ ⲇⲉⲏьⲅυ ⲥ ⲧⲣⲁⲥⲥⲩ ⲧⲣⲁⲧυⲧ ⲏⲁ ⲃⲟⲇⲕⲩ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟю ⲙⲁⲧь ⲡⲟⲥⲁⲇυⲗυ ⲏⲁ ⲟⲥⲧⲣⲟⲃ υ ⲇⲁⲗυ ⲉύ ⲧⲟⲗьⲕⲟ ⲙⲟⲉύ ⲭⲩύ υ ⲥⲕⲁⳅⲁⲗυ ⳡⲧⲟ ⳝы ⲟⲏⲁ ⲕⲁⲕ ⲙⲟⲯⲏⲟ ⳝⲟⲗьⲱⲉ ⲡⲣⲟⲇⲉⲣⲯⲁⲗⲁⲥь ⳝⲉⳅ ⲡυⳃυ υ ⲃыⲯυⲃⲁⲗⲁ ⲏⲩ ⲕⲁⲕ ⲃ ⲫυⲗьⲙⲉ "ⳅⲟύⲕⲁ ⲡⲉⲣⲉⲥⲙⲉⲱⲏυцⲁ")  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲗⲟⳝⲕⲟⲃⲩю ⲕⲟⲥⲧь ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲡⲣⲟⲧυⲃⲟⲡⲟⲗⲟⲯⲏⲩю ⲥⲧⲟⲣⲟⲏⲩ ⲥⲙⲉⲥⲧυⲗ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲃⲥⲉ ⲡⲟⲏяⲗ,ⲧы ⲭⲟⳡⲉⲱь ⲥⲟⲥⲁⲧь,ⲧⲁⲕ ⳝы ⲥⲣⲁⳅⲩ υ ⲥⲕⲁⳅⲁⲗ)ⲏⲁⲭⲩύ ⲫⲟⲧⲕυ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲡⲟⲕⲁⳅыⲃⲁⲧь ⲧⲟ ⲏⲉ ⲡⲟύⲙⲩ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь υⲡⲟⲗьⳅⲩⲉⲧ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲧяⲡⲕⲩ ⲏⲁ ⲟⲅⲟⲣⲟⲇⲉ ⲕⲟⲧⲟⲣⲟύ ⲟⲏⲁ ⲟⲕⲩⳡυⲃⲁⲉⲧ ⲕⲟⲣⲧⲟⲱⲕⲩ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ υⲥⲡⲟⲗьⳅⲩⲉⲧ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲥⲡⲁⲗьⲏыύ ⲙⲉⲱⲟⲕ ⲃ ⲡⲟⲭⲟⲇⲉ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲃⲥю ⲡⲗⲉⲱ ⲡⲣⲟⲉⲗⲁ ⲕⲁⲕ ⲙⲟⲗь ⲉⳝⲁⲏⲁя ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲣⲟυⲗ ⲥⲧⲟяⲏⲕⲩ υ ⲡⲟⲧⲟⲙ ⲡⲟⲣⲕⲟⲃⲁⲗ ⲥⲃⲟύ ⲭⲩύ ⲏⲁ эⲗυⲧⲏⲟⲉ ⲙⲉⲥⲧⲟ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧⲣⲟυⲗ ⲡυⲣⲁⲙυⲇⲩ ⲭυⲟⲡⲥⲁ ⲧⲁ ⲏⲉ ⲩⲥⲧⲟяⲗⲁ υ ⲟⳝⲣⲩⲱυⲗⲁⲥь ⲡⲣяⲙ ⲏⲁ ⲡⲟⲗⲟⲃⲩю ⲅⲩⳝⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υⳅ ⳅⲁ ⲡⲗⲟⲭⲟύ ⲕⲟⲏⲥⲧⲣⲩⲕцυυ υ ⲩⲕⲗⲁⲇⲕυ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳝⲗяⲧь ⲇⲟⲱυⲣⲁⲕ ⲉⳝⲁⲏыύ) я ⲧⲃⲟⲉύ ⲙⲁⲙⲉ ⳅⲁ ⳃⲉⲕⲩ ⲏⲁⲥцⲁⲗ_) ⲟⲏⲁ ⲙⲟⲉύ ⲥⲥⲁⲏυⲏⲟύ ⲡⲣⲟⲡⲁⲗⲟⲥⲕⲁⲗⲁ ⲣⲟⲧυⲕ υ ⲡⲗюⲏⲩⲗⲁ ⲧⲉⳝⲉ ⲏⲁ ⲉⳝⲁⲗⲟ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲧⲃⲟю ⲙⲁⲧь ⲱυⲏⲧⲁⲯυⲣⲟⲃⲁⲗ ⲕⲁⲕ ⲃ ⲕⲣⲉⲙυⲏⲁⲗьⲏыⲭ ⲫυⲗьⲙⲁⲭ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲇⲟυⲧ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲥυⲥьⲕⲩ ⲕⲟⲣⲟⲃⲉ,ⲭⲩⲉⲥⲟⲥ ⲧы ⲕⲟⲗⲭⲗⳅⲏыύ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲭⲟⲭⲗⲁⲧⲕⲁ ⳝⲟⲙⲯⲁⲧⲥⲕⲟⲅⲟ ⲕⲗυⲧⲟⲣⲁ?)я ⲧⲃⲟύ ⲡⲉⲣⲇⲁⲕ ⲗⲁⲡⲁⲧⲟύ ⲕⲁⲡⲁⲗⲁ υ ⲗⲉⲏυⲏⲁ ⲉⳝⲁⲗⲁ ⲧⲃⲟυⲙ ⲃяⲗыⲙ ⲭⲩⲉⲙ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲉύⳡⲁⲥ ⲡⲟ ⲥⲃⲟⲉⲙⲩ ⲭⲩю ⲡⲩⳃⲩ ⲕⲁⲕ ⲡⲟ ⲟⲥυ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⳡⲉⲙⲩ ⲥⲃⲟю ⲙⲁⲧь,ⲏⲁⳅыⲃⲁⲉⲱь ⲱⲗюⲭⲟύ?)ⲡⲟⲥⲗⲉ ⲧⲟⲅⲟ,ⲕⲁⲕ ⲧы ⲏⲁⳅⲃⲁⲗ ⲥⲃⲟю ⲉⳝⲁⲏⲩю ⲙⲁⲙⲁⲱⲕⲩ,ⲱⲗюⲭⲟύ,ⲟⲏⲁ ⲡⲉⲣⲉⲥⲧⲁⲗⲁ ⲙⲟύ ⲭⲩύ ⲥⲟⲥⲁⲧь!)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲫⲟⲧⲁⲗ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲡⲟⲡⲁⲣⲁцυύ ⲃ ⲕⲩⲣⲟⲣⲧⲉ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲃёⲗ ⲕⲁⲕ ⲡⲟⲗⲟⲥⲙⲁⲥⲟⲃⲩю υⲅⲣⲩⲱⲕⲩ ?  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⳝⲉⲧⲟⲏυⲣⲟⲃⲁⲗ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>]  ⲭⲟⲭⲗⲁⲧⲕⲁ ⳝⲟⲙⲯⲁⲧⲥⲕⲟⲅⲟ ⲕⲗυⲧⲟⲣⲁ?)я ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕⲉ ⲁⲏⲩⲥⲟⲙ ⲡⲣыⳃυ ⲃыⲇⲁⲃⲗυⲃⲁⲗⲁ ⲏⲁⲭⲩύ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧⲉⲏⲕⲩ υⳅ ⲕυⲣⲡυⳡⲉύ ⲃыⲕⲗⲁⲇыⲃⲁⲗ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧⲃⲟю ⲙⲁⲧь ⲟⲅⲗⲩⲱυⲗ ⲕⲁⲕ ⲣыⳝⲩ ⲃ ⲃⲟⲇⲉ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲡⲣυ ⲃыⲥⲟⲕυⲭ ⲩⲣⲟⲃⲏяⲭ ⲅⲣⲁⲃυⲧⲁцυυ ⲉⳝⲁⲗ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲱⲟⲗ ⳅⲁⳝⲣⲟⲱⲉⲏыⲉ ⲡⲣⲟэⲕⲧы ⲁⲣⲣⳑⲉ υ ⲡⲣⲟⲇⲁⲗ υⲭ ⳅⲁ ⲁⲕцυυ ⲃ ⲏⲁύⲕⲉ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲡⲣⲉⲯⲇⲉ ⳡⲉⲙ υⳅⲅⲟⲏяⲧь ⲇьяⲃⲟⲗⲟ υⳅ ⲕⲗυⲧⲟⲣⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⳡⲉⲣⲧυⲗⲁ ⲡⲉⲏⲧⲁⲅⲣⲁⲙⲙⲩ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲭⲟⲭⲗⲁⲧⲕⲁ ⳝⲟⲙⲯⲁⲧⲥⲕⲟⲅⲟ ⲕⲗυⲧⲟⲣⲁ?)ⲙⲏⲉ ⲧⲃⲁя ⲙⲁⲧь ⳡⲉⲥⲟⲧⲕⲩ яⳅыⲕⲟⲙ ⲃыⲃⲉⲗⲁ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧⲟυⲧ ⲟⲡⲟⲣⲁ ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲥⲉⲗυⲗ ⲡⲗⲉⲙя юⲏⲅυ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⲕⲩⲡυⲣⲟⲃⲁⲗ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃыⲗⲟⲯυⲗ ⲙυⲏⲏⲟⲉ ⲡⲟⲗⲉ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲇⲉⲗⲁⲗ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲟⲧⲕⲣыύ ⲡⲉⲣⲉⲗⲟⲙ ⲕⲟⲗⲉⲏⲕυ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⳝⲣⲟⲣⲩⲯυⲗ ⲏⲉυⲏⲁⲣⲟⲇⲏыⲉ ⲗⲉⲧⲁⲧⲉⲗьⲏыⲉ ⲟⳝъⲉⲕⲧы ⲥ ⲃⲏⲉⳅυⲙⲏⲟύ цυⲃυⲗυⳅⲁцυυ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟύ ⲭⲩύ ⲡⲟⲇⲕυⲏⲩⲗ ⲕⲁⲕ ⲇыⲙⲟⲃⲩю ⲅⲣⲁⲏⲁⲧⲩ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲉⲣⲉⲉⲭⲁⲗ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲃ ⲏⲟⲃⲩю ⲕⲃⲁⲣⲧυⲣⲩ ⳅⲁ ⲅⲟⲣⲟⲇⲟⲙ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃыⲥⲧⲁⲃυⲗ ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲧⲟⲣⲅⲟⲃⲩю ⲡⲗⲟⳃⲁⲇⲕⲩ ⲋⲧⲉⲁⲙ ⲕⲁⲕ ⲡⲟⲏⲟⲱⲉⲏⲩю υ ⲇⲟⲣⲟⲅⲩю ⲃⲉⳃь ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⳝ ⲁύⲥⳝⲉⲣⲅ ⲥⲧⲟⲗⲕⲏⲩⲗⲥя ⲕⲁⲕ ⲧυⲧⲁⲏυⲕ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲙⲟυⲙ ⲭⲩⲉⲙ ⲡⲟⲡⲉⲣⲭⲏⲩⲗⲁⲥь ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲧⲁⲃⲗю ⳅⲁⲡяⲧыⲉ ⲏⲁ ⲡυⳅⲇⲁⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲟⲅⲇⲁ ⲃыⲥыⲗⲁю ⲧⲉⳝⲉ ⲧⲉⲗⲉⲅⲣⲁⲙⲙⲩ )  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ υⳅⲙⲉⲣяⲗ ⲇⲗυⲏⲩ ⲕⲗυⲧⲟⲣⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲧⲣⲟυⲗ ⲥⲧυⲣⲁⲗьⲏⲩю ⲙⲁⲱυⲏⲕⲩ ⲇⲗя ⲭⲩⲉⲃ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⳝⲩⲥⲧⲣⲟυⲗ ⲕⲁⲕ ⲕⲟⲙⲏⲁⲧⲩ ⲃ ⲕⲃⲁⲣⲧυⲣⲉ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟύ ⳡⲗⲉⲏ ⲣⲃⲉⲧ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳝⲉⳅ ⲡⲣⲉⲇⲩⲡⲣⲉⲯⲇⲉⲏυⲉ ⲏⲩ ⲕⲁⲕ ⲡⲣяⲙ ⲏⲁ ⲃⲟύⲏⲉ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲡⲟⲕⲁ ⲧы ⲙⲟύ ⲭⲩύ ⲡⲉⲣⲉⲕⲁⲧыⲃⲁⲗ ⳡⲉⲣⲉⳅ ⲣⲁⲃⲏυⲏы,ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙы ⲥⲧⲟⲗⲕⲏⲩⲗυⲥь ⲏⲉυⳅⲃⲉⲥⲧⲏыⲉ ⲭⲩυ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲥⲉύⳡⲁⲥ ⳝⲩⲇⲉⲱь ⲡⲣυⲏυⲙⲁⲧь ⲙⲟύ ⲭⲩύ ⲥⲉⳝⲉ ⲃ ⲇⲩⲱⲩ ⲕⲁⲕ ⲣⲟⲇⲏⲟⲅⲟ )  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟⲗⲏⲟⲥⲧью ⲡⲟⲅⲣⲩⳅυⲗⲥя ⲃ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲗⲉⲧⲁⲉⲧ ⲡⲟ ⲭⲩя ⲕⲁⲕ ⲥⲁⲙⲟⲗⲉⲧ ⲡⲟ ⲙυⲣⲩ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲁⲅⲉⲏⲧ ⲕⲗυⲧⲟⲣⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υ ⲡⲟⲙⲟⲅⲁⲉⲧ ⲉύ ⲣⲉⲫυⲗⲁⲣⲁⲙυ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲟⳝⲣⲁⲗυ ⲇⲣⲉⲃⲏυⲉ ⲁⲧцⲧⲉⲕυ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲙⲟⲅⲩ ⲡⲟⲇⲃⲉⲥⲧυ ⲥⲃⲟύ ⲭⲩύ ⲕ ⲏⲟⲥⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥ ⲡⲟⲙⲟⳃью ⲧⲃⲟⲉⲅⲟ ⲣⲧⲁ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ υⳅⲩⳡυⲗ ⲁⲏⲁⲗьⲏыⲉ ⲧⲟⲏⲏⲉⲗυ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲟⲧⲟⲣы ⲡⲟⲥⲧⲣⲟυⲗυ ⲇⲣⲉⲃⲏυⲉ υⲏⲕυ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲣⲟⲇⲁю ⲧⲁⲕⲟ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲗⲟⳝ ⲧⲃⲟύ ⲙⲁⲧⲉⲣυ ⲱⲕⲃⲁⲣυⲗ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя ⲕⲁⲕ ⲣⲁⲇυⲟ ⲡⲣυёⲙⲏυⲕ ⲃ ⲙⲁⲅⲏυⲧⲟⲫⲟⲏⲉ ?)??  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ эⲧⲟ ⲡⲁⳅⲇⳝυⳃⲉ ⲇⲗя ⲭⲩⲉⲃ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲅⲣⲟⳝ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁ ⲥⲃⲟⲉ ⲭⲩю ⲧⲁⳃυⲗ ⲇⲟ ⲕⲗⲁⲇⳝυⳃⲁ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲣⲉⲗ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲕⲁⲕ ⲃ ⳝⲁⲏⲉ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',


'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲣⲟⲧ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟύ ⲭⲩύ ⲗⲟⲯυⲗ ⲕⲁⲕ ⲅⲗⲁⲇυⲗьⲏⲟю ⲇⲟⲥⲕⲩ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲇⲗя ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲃⲟⲗⲱⲉⳝⲏⲁя ⲡⲁⲗⲟⳡьⲕⲁ ?_  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲃыⲗⲉⳡυⲗ ⲟⲧ ⲣⲁⲕⲁ ⲙⲟⳅⲅⲁ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲣυⲥⲟⲃⲁⲗ ⲕⲁⲣⲧⲩ ⲙυⲣⲁ υ ⲡⲟⲧⲟⲙ ⲡⲟ ⲏⲉύ ⲟⲡⲣⲉⲇⲉⲗяⲗ ⲅⲇⲉ я ⲏⲁⲭⲟⲯⲩⲥь ⲕⲁⲕ ⲡⲟ ⳋⲣⲋ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ υⳅⳝⲁⲃυⲗ ⲧⲃⲟю ⲙⲁⲧь ⲟⲧ ⲙⲩⳡⲉⲏυя ⲃ ⲏυⲯⲏυⲭ ⲅⲉⲏυⲧⲁⲗυяⲭ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲇⲁⲃⲏⲟ ⲡⲟⲣⲃⲁⲏⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟⲅⲗⲟⳃⲁⲉⲧ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲃ ⲇⲃⲩⲭ ⲕⲟⲗⲉⲥⲏⲟύ ⳡⲉⲭⲟⲧⲕⲉ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲏⲁ ⲧⲃⲟυⲭ ⲅⲩⳝⲁⲭ ⲭⲩⲉⲃ ⲡⲟⳝыⲃⲁⲗⲟ ⳝⲟⲗьⲱⲉ ⳡⲉⲙ ⲃ ⲕυⲧⲁⲉ ⳝⲟⲗьⲱⲉ ⲏⲁⲣⲟⲇⲩ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲗⲟⳝ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟύ ⲭⲩύ ⲡⲣυⳝυⲗ ⲃ ⲃυⲇⲉ ⲧⲣⲟⲫⲉя ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳅⲁⳡⲉⲙ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲥⲃⲟⲉύ ⲕⲗυⲧⲟⲣ ⲕυⲧⲁύⲥⲕⲩю ⲗⲁⲡⲱⲩ ⲏⲁⲕⲣⲩⳡυⲃⲁⲉⲧ ?)/  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲙⲉⲥⲧυⲗ ⲥⲃⲟύ ⲭⲩύ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲙⲉⲥⲧυⲗ ⲥⲃⲟύ ⲭⲩύ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲙⲉⲧⲕⲩ ⲟⲥⲧⲁⲃυⲗ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧыы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟύ ⲭⲩύ ⲃ ⳅⲁⲧыⲗⲟⲕ ⲕυⲇⲁⲗ υ ⲟⲏⲁ ⲩⲡⲁⲗⲁ υ ⲡⲣⲟⲉⲭⲁⲃⲱυⲥь ⲣⲧⲟⲙ ⲡⲟ ⲕⲃⲁⲣⲧⲁⲗⲩ ⲟⲏⲁ ⲏⲁⲥⲟⳝυⲣⲁⲗⲁ ⲕⲩⳡⲩ ⲭⲩⲉⲃ )??  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲇⲥⲧⲁⲃυⲗ ⲡⲟⲇ ⲧⲁⲗυⳝⲥⲕυύ ⲟⳝⲥⲧⲣⲉⲗ ⲭⲩⲉⲃ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥ ⲭⲩⲉⲙ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ υⲅⲣⲁⲗυ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲙⲟⲣⲥⲕⲟύ ⳝⲟύ ⲕⲁⲕ ⲏⲁ ⲗυⲥⲧⲟⳡⲕⲁⲭ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲟⲧⲡⲣⲁⲃυⲗⲥя ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲃ эⲕⲡⲉⲇυцυю ⲁ ⲧⲟⳡⲏⲉⲉ ⲕⲁⲕ ⲃ ⲕυⲏⲟ "ⲧⲁύⲏы ⲡⲉⲣⲉⲃⲁⲗⲁ ⲇяⲧⲗⲟⲅⲟ" ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⳝⲣⲟⲥυⲗ ⲥⲃⲟύ ⲭⲩύ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲃυⲇⲉ яⲕⲟⲣя ⲕⲟⲧⲟⲣыⲉ ⲥⲕυⲇыⲃⲁюⲧ ⲥⲩⲇⲏⲁ ⲕⲟⲅⲇⲁ ⲡⲣυⲱⲃⲁⲣⲧⲟⲃыⲃⲁюⲧⲥя ⲕ ⳝⲩⲭⲧⲉ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь,я ⳃⲁⲥ υⲅⲣⲁю ⲃ ⲇⲟⲧⲩ,υ ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃыⲇⲁю ⲣⲁⲙⲡⲁⲅυ,υ ⲉⳃⲉ,я ⲡⲣяⲙ ⲧⲟⳡⲏⲟ ⲭⲩⲕⲏⲩⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ!)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲏыⲣⲏⲩⲗ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧⲟⲗьⲕⲟ ⲥⲟ ⲥⲧⲣⲟⲭⲟⲃⲕⲟύ υ ⲥ ⲁⲕⲃⲁⲗⲁⲏⲅⲟⲙ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] я ⲧⲃⲟю ⲙⲁⲧь,ⲡⲟ ⲇⲉⲱⲉⲃⲕⲉ ⳅⲁⳝυⲣⲁⲗ ⲥ ⲣыⲏⲕⲁ,ⲟⲏⲁ ⲥⲧⲟяⲗⲁ,5$ υⲗυ 6$,ⲏⲟⲣⲙ ⲯⲉ,ⳅⲏⲁⲉⲱь ⲡⲟⳡⲉⲙⲩ ⲧⲁⲕ ⲇⲉⲱⲉⲅⲟ?)ⲡⲟⲧⲟⲙⲩ ⳡⲧⲟ,ⲩ ⲏⲉⲉ ⳝыⲗ ⲏⲉⲇⲟⲉⳝ!)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲭⲟⲭⲟⲗ ⲙⲟⲉⲅⲟ ⲕⲗυⲧⲟⲣⲁ?) я ⲏⲁ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲕⲣυ ⲏⲁⲣⲟⲥⲧυⲧⲉⲗь ⲃⲁⲗⲟⲥ ⲃыⲗⲉⲗⲁ υ ⲧⲉⲡⲉⲣь ⲩ ⲏⲉⲉ ⲏⲁ ⲡυⳅⲇⲉ ⲕⲁⲥυⳡⲕυ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕυⲗⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲣⲟυⲗ ⳝⲩⲏⲕⲉⲣ ⲇⲗя ⲡⲣⲟⲯυⲃⲁⲏυⲉ ⲃⲟ ⲃⲣⲉⲙя ⲕⲁⲧⲁⲕⲗυⳅⲙⲁ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⳅⲏⲁⲗ,ⳡⲧⲟ υⲙⲉⲏⲏⲟ я!)ⲉⲇυⲏⲥⲧⲃⲉⲏⲏыύ υ ⲏⲉⲡⲟⲃⲧⲟⲣυⲙыύ ⲥⲩⲧⲉⲏⲉⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲇⲃυⲅⲁⲗ ⲕⲁⲕ ⲧяⲯⲉⲗыύ ⲡⲣⲉⲇⲙⲉⲧ ⲃ ⲃυⲇⲉ ⲇυⲃⲁⲏⲁ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь,ⳡⲧⲟ ⲕⲟⲅⲇⲁ я ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲙⲁⲏьⲕⲩ,ⲧⲟ ⲩ ⲏⲉⲉ ⲡυⳅⲇⲁ ⲏⲁⳡυⲏⲁⲉⲧ ⲟⲧⲕⲣыⲃⲁⲧьⲥя,ⲕⲁⲕ ⲃⲟⲣⲟⲧⲁ !)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⲧⲣⲁⲯⲁⲗ ⲁⲧⲁⲕⲩ ⲧⲁⲗυⳝⲥⲕυⲭ ⲭⲩⲉⲃ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь,ⳡⲧⲟ ⲕⲟⲅⲇⲁ ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ,ⲧⲟ ⲏⲁⳡυⲏⲁⲉⲧⲥя ⳅⲃⲉⳅⲇⲟⲡⲁⲇ!)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲥ ⲡⲟⲗя ⲥⲟⳝυⲣⲁⲗⲁ ⲭⲩυ ⲃ ⲃυⲇⲉ ⲅⲣυⳝⲟⲃ υ ⲥⲕⲗⲁⲇыⲃⲁⲗⲁ ⲥⲉⳝⲉ ⲃ ⲟⳡⲕⲟ ⲃ ⲃυⲇⲉ ⲕⲁⲣⳅυⲏы ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь,ⳡⲧⲟ я ⳃⲁⲥ ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲯⲁⲣ ⲥⲇⲉⲗⲁю,ⲡⲟⲥⲗⲉ ⳡⲉⲅⲟ,ⲡⲣυⲉⲇⲩⲧ ⲙⲟυ ⲇⲣⲩⳅьяⲙυ,υ ⳝⲩⲇⲩⲧ ⲧⲩⲱυⲧь!)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲏⲟⲥυⲧⲥя ⳅⲁ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲕⲁⲕ ⲃⲟⲗⲕ ⳅⲁ ⳅⲁύцⲟⲙ υⳅ ⲙⲩⲗьⲧυⲕⲁ "ⲏⲩ ⲡⲟⲅⲟⲇυ" ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲥюⲇⲁ υⲇυ,ⲧⲃⲟю ⲙⲁⲧь ⳝⲩⲇⲉⲙ ⲃⲙⲉⲥⲧⲉ ⲉⳝⲁⲧь!)ⲅⲟⲏⲇⲟⲏы ⲃⳅяⲧь ⲏⲉ ⳅⲁⳝⲩⲇь!)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲟⲅⲇⲁ ⲣⲟⲥⲥυя ⲡⲩⲥⲕⲁⲗⲁ ⲣⲁⲕⲉⲧы ⲧⲟ ⲇⲁⲏⲏыⲉ ⲕⲟⲟⲣⲇυⲏⲁⲧы υⳅⲙⲉⲏυⲗυⲥь υ ⲃⲗⲉⲧⲉⲗυ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь,ⳡⲧⲟ ⲙⲟύ ⲭⲩύ,эⲧⲟ ⲕⲁⲕ ⲅυⲇⲣⲁⲃⲗυⲕⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ?)ⲟⲏⲁ ⲧⲁⲕ ⲩⲥⲕⲟⲣяⲉⲧⲥя,ⲕⲟⲅⲇⲁ я ⲉύ ⲃ ⲡυⳅⲇⲩ ⳅⲁⲕυⲇыⲃⲁю ⲥⲃⲟⲉⲅⲟ ⲇⲣⲩⲯⳝⲁⲏⲁ!)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁⳝⲣⲁⲥыⲃⲁⲉⲧⲥя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲕⲁⲃⲕⲁⳅⲕⲁя ⲟⲃⳡⲁⲣⲕⲁ ⲥ ⲅⲟⲣⲏыⲭ ⲣⲁⲃⲏυⲏ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲇυⲭⲗⲟⲫⲟⲥ ⲇⲗя ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳝⲗⲟⲭ ⲃыⲃⲟⲇυⲧь υⳅ ⲉё ⲗⲟⳝⲕⲟⲃыⲭ ⲃⲟⲗⲟⲥⲟⲃ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕυⲗⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲣⲟⲃⲟⲇυⲗ ⲅⲁⳅⲟⲃⲩю ⲁⲧⲁⲕⲩ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲧы ⲧⲁ ⲡⲣⲟⲥⲧυⲧⲩⲧⲕⲁ, ⲕⲟⲧⲟⲣⲁя ⲡυⲱⲉⲧ ⳡⲧⲟ ⲧⲟ ⲡⲉⲣⲉⲇ ⲉⳝⲗⲉύ ⲙⲟⲉⲅⲟ ⲭⲩя ⲥ ⲧⲃⲟυⲙ ⲣⲧⲟⲙ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υⲡⲣⲁⲃυⲗ ⲧⲉⲭⲏυⳡⲉⲥⲕⲩю ⲏⲉⲡⲟⲗⲁⲇⲕⲩ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲩ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲥⲡυⳅⲇυⲗ ⲇⲩⲭυ ⲏⲁⳝⲣыⳅⲅⲁⲗⲥя υⲙυ υ ⲡⲟⲱⲟⲗ ⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲧь ⳡⲧⲟ ⳝы ⲣⲟⲇⲏыⲙ ⳅⲁⲡⲁⲭⲟⲙ ⲡⲁⲭⲗⲟ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧⲣⲉⲗяⲗ υⳅ ⲥⲃⲟⲉⲅⲟ ⲭⲩя ⲕⲁⲕ υⳅ ⲗⲩⲕⲁ ⲁ ⲥⲧⲣⲉⲗы ⳝыⲗυ ⲃ ⲃυⲇⲉ ⲕⲟⲏⳡυⲏы ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲧⲁⲗ ⲕⲟⲙⲕυ ⲏⲁⲃⲟⳅⲁ ⲕⲁⲕ ⲏⲟⲃⲟⳅⲏыύ ⲯⲩⲕ υ ⲡⲟⲧⲟⲙ ⲥⲕυⲇыⲃⲁⲗ ⲃ ⲏⲩⲧⲣь ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲙⲁⲧⲉⲣυ ⲩⲕⲗⲁⲇыⲃⲁⲗ ⲥⲧⲉⲏⲕⲩ υⳅ ⲕυⲡⲣⲡυⳡⲉύ ⲇⲗя ⲟⲡⲟⲣы ⲥⲃⲟⲉⲅⲟ ⲭⲩя ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟⲇⲭⲟⲇυⲧ ⲕ ⲟⳡⲕⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⳅⲟⲗⲟⲧⲟύ ⲕⲗюⳡυⲕ ⲕ ⲥⲩⲏⲇⲩⲕⲩ ⲥ ⲥⲟⲕⲣⲟⲃυⳃⲁⲙυ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲧь, ⲡⲟⲕⲁ ⲧы ⲧⲩⲧ ⲡυⲱⲉⲱь?) ⲥⲗыⲱυⲱь ⲕⲣυⲕυ? ⳡⲧⲟ я ⲧⲁⲙ ⲕⲣυⳡⲩ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟⲙⲉⲥⲧυⲗⲥя ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲃ υⳅⳝⲩⲱⲕⲩ ⲏⲁ ⲕⲩⲣьυⲭ ⲏⲟⲯⲕⲁⲭ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟⳝыⲃⲁⲃ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⳝⲏⲟⲣⲩⲯυⲗ ⳝⲟⲗⲉⲉ ⲧыⲥяⳡυ ⲩⲅⲣⲟⳅ ⲕⲁⲕ ⲁⲏⲧυ-ⲃυⲣⲩⲥ,ⲛⲟʀⲇ 32 ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲟⲥⲧⲁⲃυⲗ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⳅⲇⲣⲁⲯⲉⲏυⲉ ⲕⲁⲕ ⲣⲉⲡⲉύⲏυⲕ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲕⲁⲕ ⲟⲇυⲏⲟⲕυύ ⲥⲃυⲧυⲗьⲏυⲕ ⲃ ⲕⲣⲟⲙⲉⲱⲏⲟύ ⲧьⲙⲉ ⳝⲉⳅ ⲃⲉⲇⲟⲙⲁ ⲙⲟⲉⲅⲟ ⲭⲩя ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲉⲇυⲏⲥⲧⲃⲉⲏыύ ⲕⲧⲟ ⳝⲩⲇⲉⲧ ⲟⳝⲟⲅⲣⲉⲃⲁⲧь ⲧⲃⲟю ⲙⲁⲧь эⲧⲟύ ⳅυⲙⲏⲉύ ⲥⲧⲩⲯⲟύ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⳅⲁⲗυⲗ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲗяⲇⲉⲏⲩю ⲅⲟⲣⲕⲩ ⲃ ⲡⲁⲣⲕⲉ υ ⲕⲁⲧⲁⲗⲥя ⲥ ⲏⲉё ⲏⲁ ⲥⲁⲏⲕⲁⲭ ⲗⲉⲇяⲏⲕⲁⲭ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲩⲥⲧⲁⲏⲟⲃυⲗ ⲣⲁⲇυⲁⲧⲟⲣ ⲟⲧ ⲃⲉⳅⲇυⲭⲟⲇⲁ ⳡⲧⲟⳝы ⲕⲧⲟ ⲧⲟ ⲟⳝⲟⲅⲣⲉⲃⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲃ эⲧⲩ ⲭⲟⲗⲟⲇⲏⲩю ⳅυⲙⲩ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲏⲁⲡυⲱυ, ⲥ ⲕⲁⲕυⲙυ ⲥⲗⲟⲃⲁⲙυ я ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⲃ ⲧⲃⲟⲉύ ⲕⲟⲙⲏⲁⲧⲉ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲡⲣⲉⲗⲁ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲕⲁⲕ ⲃ ⳝⲁⲏⲉ ⲡⲟⲇ ⲃыⲥⲟⲕⲟύ ⲧⲉⲙⲡⲉⲣⲁⲧⲩⲣⲟύ ⲙⲟⲉⲅⲟ ⲭⲩя υ ⲟⲏ ⲉё ⲕⲁⲕ ⳝы υⳅⲏⲩⲧⲣυ ⲟⳝⲟⲅⲣⲉⲃⲁⲗ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲥъⳝυⲗ ⲕⲁⲕ ⲗⲟⲱⲁⲇь ⲃ ⲉⳝⲁⲏⲏⲩю ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲙⲁⳅⲁⲉⲧ ⲥⲃⲟυ ⲡⲟⲗⲟⲃыⲉ ⲅⲩⳝы ⲙⲟⲉύ ⲕⲟⲏⳡυⲏⲟύ ⲇⲩⲙⲁя ⳡⲧⲟ эⲧⲟ ⲡⲟⲙⲁⲇⲁ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲏⲁⲡυⲱυ ⲃ ⲏⲁⳡⲁⲗⲉ ⲡⲣⲉⲇⲗⲟⲯⲉⲏυя, ⲕⲧⲟ ⲉⳝⲁⲗ ⲧⲃⲟύ ⲣⲟⲧⲁⲏ, ⲡⲟⲕⲁ ⲧы ⲥⲡⲁⲗⲁ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲥⲃⲁⲗυⲗⲁⲥь ⲏⲁ ⲙⲟύ ⲭⲩύ ⲥ ⲧⲩⲁⲗⲉⲧⲏⲟύ ⲕⲣыⲱⲕυ ⳝυⲟ ⲧⲩⲁⲗⲉⲧⲁ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡыⲧⲁⲗⲥя ⲥⲇⲉⲗⲁⲧь υⳅ ⲧⲃⲟⲉύ ⲥⲉⲙьυ ⳡⲉⲗⲟⲃⲉⳡⲉⲥⲕⲩю ⲙⲏⲟⲅⲟⲏⲟⲯⲕⲩ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡⲣⲟⲯⲟⲅ ⲡⲟⲗⲟⲃⲩю ⲅⲩⳝⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⳝыⳡⲕⲟⲙ ⲥⲟⲗⲟⲫⲁⲏⲟⲃыύ ⲡⲁⲕⲉⲧυⲕ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲉύⳡⲁⲥ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲇⲟ ⲗυⲏυυ ⲅⲟⲣυⳅⲟⲏⲧⲁ ⲣⲁⲥⲥⲧяⲏⲩ υ ⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟ ⲅⲁⳝⲁⲣυⲧⲁⲙ ⲏⲉ ⲃⲗⲉⳅⲉⲧ ⲉё ⲃ ⲩⳅⲕыύ ⲁⲏⲁⲗьⲏыύ ⲡⲣⲟⲭⲟⲇ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲟⲧⲡⲣⲁⲃυⲗ ⲥⲟ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃⲟ ⲣⲧⲩ ⲃ ⲕⲣⲉⲥⲧⲟⲃыύ ⲡⲟⲭⲟⲇ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ υⲡⲟⲗьⳅⲩⲉⲧ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲥⲡⲁⲗьⲏыύ ⲙⲉⲱⲟⲕ ⲃ ⲡⲟⲭⲟⲇⲁⲭ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲟⲧⲡυⲱυⲥь, ⲕⲧⲟ ⲣⲁⲥⲭⲩяⲣυⲗ ⲉⳝⲗⲟ ⲧⲃⲟύ ⲙⲁⲧⲉⲣυ ⲃⳡⲉⲣⲁ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⲥⲧяⲏⲩ ⲡⲟ ⲇⲩⲡⲗⲩ ⲧⲁⲕⲏⲕⲁ ⲟⳝэⲉⲕⲧ-242 υ ⲕⲁⲕ ⲧы ⲇⲩⲙⲁⲉⲱь ⳡⲧⲟ υⳅ эⲧⲟⲅⲟ ⲃыύⲇⲉⲧ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⳡⲩⳡⲩⲏⲇⲣⲁ ⲁⲏⲁⲗьⲏⲁя?) я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗⲁ ⲕⲁⲗⲟⲏⲕⲟύ ⲃ ⲡⲉⲣⲇⲁⲕ υ ⲩ ⲏⲉⲉ ⳡⲉⲣⲉⳅ ⲡυⳃⲇⲩ ⲙⲩⳅⲃⲕⲁ υⲅⲣⲁⲉⲧ  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲱⲗюⲭⲁ ⲧы ⲡⲣⲟⳝυⲧⲁя) я ⲧⲉⳝⲉ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⳃⲁⲥ ⲣⲟⲧ ⲡⲗⲣⲃⲩ υ ⲃⲟⲇⲣⲟ ⲃⲥⲧⲁⲃⲗю υ ⳝⲩⲇⲩ ⲧⲉⳝⲉ ⲥⲥⲁⲧь  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲁⲃυⲗ ⲩⲥυⲗⲟⲕ υ ⲡыⲧⲁⲗⲥя ⲣⲁⳅⲅⲟⲃⲁⲣυⲃⲁⲧь ⲃ ⲥⲕⲁύⲡⲉ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲣυⲥⲟⲃⲁⲗ ⲡⲉⲏⲧⲁⲅⲣⲁⲙⲙⲩ ⲡⲣⲉⲯⲇⲉ ⳡⲉⲙ υⳅⲅⲟⲏяⲧь ⲇⲉⲙⲟⲏⲟⲃ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧυⲣⲁⲗ ⲗⲟⲧⲉⲣⲉύⲏыύ ⳝⲉⲗⲉⲧ υ ⲃыύⲅⲣⲁⲗ ⲟⲇυⲏ ⲙυⲗⲗυⲟⲏ ⲣⲩⳝⲗⲉύ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣыⳝⲁⳡυⲗ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲁ ⲡⲣυⲙⲁⲏⲕⲁ ⳝыⲗⲁ υⳅ ⲗⲟⳝⲕⲟⲃыⲭ ⲃⲟⲗⲟⲥⲕⲟⲃ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υ ⳅⲁ цⲉⲗыⲉ ⲥⲩⲧⲕυ я ⲏⲁⲗⲟⲃυⲗ ⲃⲉⲇⲣⲟ ⲣⲁⲧⲁⲏⲁ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя) ⲏⲁⲡυⲱυ ⲃ ⲏⲁⳡⲁⲗⲉ ⲡⲣⲉⲇⲗⲟⲯⲉⲏυя, ⲕⲧⲟ ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲟ ⲥⲃⲟⲉⲅⲟ ⲭⲩя ⲕⲁⲕ ⲥ ⲡⲉⳡⲉⲏⲉⲅⲁ ⲥⲧⲣⲉⲗяⲗ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲣяⲙ ⲩⲡⲟⲣ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲩⲥⲧⲁⲏⲟⲃυⲗ ⲣⲁⲕⲉⲧⲏⲟⲉ ⲟⳝⲟⲣⲩⲇⲟⲃⲁⲏυя ⲡⲟⲇ ⲏⲁⳅⲃⲁⲏυⲉⲙ ⳅⲉⲏυⲧⲕυ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲁⲃυⲗ ⲯυⲣⲏⲩю ⲧⲟⳡⲕⲩ ⲕⲁⲕ ⲥⲧⲁⲃυⲗυ ⲡυⲣⲁⲧы ⲕⲣⲉⲥⲧ ⲏⲁ ⲕⲁⲣⲧⲉ υ ⲃыⲇⲃυⲅⲁⲗυⲥь ⳅⲁ ⲥⲟⲕⲣⲟⲃυⳃⲁⲙυ ⲕⲟⲧⲟⲣыⲉ я ⲩⲧⲁυⲗ ⲃ ⲉё ⲟⳡⲕⲉ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲟⲧ ⲩⲇⲁⲣⲁ ⲙⲟⲉⲅⲟ ⲭⲩя υ ⲭⲩя ⲙⲟⲉⲅⲟ ⲟⲧцⲁ ⲥ ⲇⲃⲩⲭ ⲥⲧⲟⲣⲟⲏ ⲧⲃⲟю ⲙⲁⲧь ⲡⲣⲟⲥⲧⲟ ⲥⲡⲗюⳃυⲗⲟ ⲕⲁⲕ υ ⲉё ⲕⲗυⲧⲟⲣ ⲃ ⲧⲉⲥⲕⲁⲭ ⲕⲟⲧⲟⲣыύ ⲡⲟⲇⲕⲣⲩⳡυⲃⲁⲗ ⲧⲃⲟύ ⲟⲧⲉц )  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲥⲏⲉⲥⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳡⲉⲣⲉⲡⲏⲩю ⲕⲟⲣⲟⳝⲕⲩ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]',  
'[<emoji document_id=5438203928527253097>💀</emoji>] ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲕⲣⲩⲧυⲗⲁⲥь ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲕⲁⲕ ⲏⲁ ⲱⲉⲥⲧⲉ ?)  [<emoji document_id=5438203928527253097>💀</emoji>]' ]
        self.db.set(self.strings['name'], 'state', True)
        while self.db.get(self.strings['name'], 'state'):
            await message.respond(sh+(random.choice(shablon)), file=media)
            await sleep(time)
            
    async def черепcmd(self, message):
        """— Запустить модуль по указанной команде"""
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b><emoji document_id=5438153647345119196>💀</emoji> Ⲙⲟⲇⲩⲗь #Ⳡⲉⲣⲉⲡ ⲡⲉⲣⲉⲥⲧⲁⲗ ⲕⲁⲣⲁⲧь ⲧⲃⲟю ⲙⲁⲧь. <emoji document_id=5438153647345119196>💀</emoji></b>")
            return
        await utils.answer(
            message,
            "<b><emoji document_id=5438153647345119196>💀</emoji> Ⲙⲟⲇⲩⲗь #Ⳡⲉⲣⲉⲡ ⲏⲁⳡⲁⲗ ⲕⲁⲣⲁⲧь ⲧⲃⲟю ⲙⲁⲧь. <emoji document_id=5438153647345119196>💀</emoji></b>\n\n"
            "<b><<emoji document_id=5438153647345119196>💀</emoji> Ⳡⲧⲟⳝы ⲟⲥⲧⲁⲏⲟⲃυⲧь ⲙⲟⲇⲩⲗь, ⲡυⲱυ</b> <code>.череп</code>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl = [
        'ʏᴀ ᴢʜᴇ ᴛᴇʙʏᴀ ᴛᴜᴛ ᴠʏᴇʙᴜ ɴᴀ sᴘɪɴᴇ ᴛᴠᴏᴇᴊ ᴢʜᴇ ᴍᴀᴍʏ ɪ ᴛʏ ᴍɴᴇ ᴅᴏᴋᴀᴢʜᴇsʜь ᴛᴜᴛ ᴛᴏʟьᴋᴏ ᴛᴏ, ᴄʜᴛᴏ ᴛʏ sʟᴀʙʏᴊ sʏɴ sʜʟʏᴜʜɪ, ɴᴇ ʙᴏʟᴇᴇ. <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь, ᴄʜᴛᴏ ᴋʟɪᴛᴏʀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴇᴛᴏ ᴄʜʀᴇᴢᴠʏᴄʜᴀᴊɴᴏ ᴏᴘᴀsɴᴀʏᴀ ᴢᴏɴᴀ? <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛʏ ᴅᴀᴠᴀᴊ ɴᴇ ᴘɪᴢᴅɪ, ᴀ ʜᴜᴊ ᴍᴏᴊ ᴠsᴀsɪ ᴘɪᴢᴅᴀʙᴏʟ ᴇʙᴀɴʏᴊ. ᴛʏ ᴢʜᴇ ᴛᴜᴛ ɪ sᴜᴛᴏᴋ ɴᴇ ᴘʀᴏᴛʏᴀɴᴇsʜь, ᴜʙᴇᴢʜɪsʜь sᴠᴏᴇᴊ ᴍᴀᴍᴀsʜᴇ ᴘɪᴢᴅᴜ ʟɪᴢᴀᴛь ɪ ʜᴠᴀsᴛᴀᴛьsʏᴀ ᴛᴇᴍ, ᴄʜᴛᴏ ᴏᴛsᴏsᴀʟ ʜᴜᴊ ᴠᴇʟɪᴋᴏᴍᴜ ᴢʟᴏᴅᴇʏᴜ. <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛʏ ᴢɴᴀʟ ᴄʜᴛᴏ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ɪᴢ ᴏᴋɴᴀ ᴠʏᴋɪɴᴜʟ ᴀ ᴏɴᴀ ᴠsᴛᴀʟᴀ ɪ ᴅᴀʟьsʜᴇ ᴘᴏʙᴇᴢʜᴀʟᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛᴜʜᴀ s 5 ʟᴇᴛ ɴᴀ ᴍᴏᴊ ʜᴜᴊ ᴍᴏʟɪʟᴀsь ʟʏᴀᴠʀᴀ ᴇʙᴜᴄʜᴀʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴜ ᴍᴀᴍᴜ ʜᴜёᴍ ᴛᴀᴋ ʀᴀᴢᴠёʟ ᴄʜᴛᴏ ᴏɴᴀ ᴠsᴇᴍᴜ ʀᴀᴊᴏɴᴜ ɢᴏᴠᴏʀɪʟ ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴇᴛᴏ ʀᴇʟɪᴋᴠɪʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ᴛᴀᴋ ᴛᴏ ᴅᴏ ᴏʀɢᴀᴢᴍᴀ ᴅᴏᴠёʟ ᴀ ᴛᴠᴏᴊ ʙᴀᴛʏᴀ ᴠ ᴇᴛᴏ ᴠʀᴇᴍʏᴀ ᴠ ᴀʜᴜᴇ sᴛᴏʏᴀʟ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴢʜᴇ ᴅᴀᴠɴᴏ ɴᴀ ʜᴜᴇ ᴍᴏёᴍ sɪᴅɪᴛ ᴏɴᴀ ᴅᴜᴍᴀᴇᴛ ᴄʜᴛᴏ ᴇsʟɪ ᴘᴜsᴋᴀᴇᴛ sᴘᴇʀᴍᴀᴋ ᴘᴏ ᴋʀᴏᴠɪ ᴛᴏ ᴇᴛᴏ ɴᴏʀᴍᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛʏ ᴅᴜᴍᴀʟ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀ sʜᴀʟᴀᴠᴀ ᴍʏ ᴇё s ᴘᴀᴛsᴀɴᴀᴍɪ ᴢᴀ ᴅᴠᴏʀᴀᴍɪ ʜᴜʏᴀᴍɪ ᴘᴏʟᴏsᴏᴠᴀʟɪ ᴛᴏʟьᴋᴏ ɴᴇ ᴋᴏᴍᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛʏ ᴇsᴄʜё ᴍᴏʟɪsʜьsʏᴀ ᴢᴀ ᴛᴏ ᴄʜᴛᴏʙʏ ᴛᴠᴏʏᴀ ᴍᴀᴛᴜʜᴀ ᴍɴᴇ ʜᴜᴊ sᴏsᴀʟᴀ ᴇsʟɪ ᴅᴀ ᴛᴏ ᴍᴏɢᴜ ᴘᴏᴢᴅʀᴀᴠɪᴛь ᴏɴᴀ ᴅᴏsɪʜᴘᴏʀ ᴢᴀᴠɪsɪᴍᴀ ᴏᴛ ʜᴜʏᴀ ᴍᴏᴇɢᴏ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍᴏɢᴜ sᴋᴀᴢᴀᴛь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴠ ʀᴀᴅᴏsᴛь sᴏsёᴛ ᴍᴏᴊ ʜᴜᴊ ɪ ᴇᴛᴏ ᴇᴊ ᴅᴀёᴛ ᴍᴏʀᴇ ᴘᴏʟᴏᴢʜɪᴛᴇʟьɴʏʜ ᴇᴍᴏᴛsɪᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ɪ ᴄʜё ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴅᴏʟɢᴏ ʙᴜᴅᴇᴛ ʙɪᴛьsʏᴀ ᴠ ᴋᴏɴᴠᴜʟьsɪʏᴀʜ ᴏᴛ ʜᴜʏᴀ ᴍᴏᴇɢᴏ ᴢᴀʙɪʀᴀᴊ ᴇё sᴋᴏʀᴇᴊ ᴅᴜʀɴᴏᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛʏ ᴄʜё ᴅᴜᴍᴀᴇsʜь ʏᴀ sᴄʜᴀs ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘʀᴏsᴛᴏ ᴛᴀᴋ ᴏᴛᴘᴜsᴄʜᴜ ɴᴇ ᴘᴜsᴛь ɢᴏᴅ ᴍɴᴇ ᴘᴏsᴏsёᴛ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀ ᴛʀᴀssᴇ sᴛᴏʏᴀʟᴀ ɪ ᴋᴀᴢʜᴅʏᴊ ʀᴀᴢ ᴢʜᴅᴀʟᴀ ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴇё ᴢᴀʙᴇʀёᴛ ɴᴏ ʏᴀ ᴇᴊ ʟɪsʜь ɴᴀ ʀᴏᴛᴀɴ ᴋɪᴅᴀʟ ɪ ᴜᴇᴢᴢʜᴀʟ <emoji document_id=5438153647345119196>💀</emoji>',
'ɪ ᴄʜё ᴛʏ ᴅᴜʀᴀ ᴇʙᴀɴᴀʏᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴢᴀ ᴍᴏᴊ ʜᴜᴊ ᴅʀᴀʟᴀsь s ᴅᴇᴠᴋᴀᴍɪ ᴏɴᴀ ᴅᴜᴍᴀʟᴀ ᴄʜᴛᴏ sᴛᴀɴᴇᴛ ʟᴜᴄʜsʜᴇᴊ ᴏᴛsᴏsᴋᴏᴊ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ᴏɴᴀ ᴘᴏᴄʜᴛɪ ᴅᴏsᴛɪɢʟᴀ ᴇᴛᴏᴊ ᴛsᴇʟɪ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴇsʟɪ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏsᴀᴅɪᴛь ɴᴀ ᴍᴏᴊ ʜᴜᴊ ᴘᴏᴠᴇʀь ᴏɴᴀ ɴᴇ sʟᴇᴢᴇᴛ ᴘᴏᴋᴀ ɴᴇ ᴜᴍʀёᴛ <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʀɪʟɪ ʜᴜёᴍ ᴘᴏʜᴏʀᴏɴɪʟ ᴏɴᴀ ᴜᴍᴜᴅʀɪʟᴀsь ᴠʏʙʀᴀᴛьsʏᴀ ᴄʜᴛᴏʙʏ ɴᴀ ᴘᴏsʟᴇᴅᴏᴋ ᴇsᴄʜё ᴍɴᴇ ᴏᴛsᴏsᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴜ ᴇᴛᴏ ᴜᴢʜᴇ sᴛʀᴀɴɴᴏ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴛᴀᴋ ᴄʜᴀsᴛᴏ ᴠʀёᴛ ᴛᴠᴏᴇᴍᴜ ᴏᴛᴛsᴜ ᴄʜᴛᴏ ᴏᴛsᴀsʏᴠᴀᴇᴛ ᴍɴᴇ ᴠsᴇɢᴏ ᴘᴏ 10 ʀᴀᴢ ᴠ ᴅᴇɴь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏᴊ ᴘᴀʜᴀɴ sɴɪᴍᴀʟ ɴᴀ ᴠɪᴅᴇᴏ ᴋᴀᴋ ʏᴀ ᴇʙᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ɪ ʀᴀᴅᴏᴠᴀʟsʏᴀ ᴠᴇᴅь ʏᴀ ᴛᴏᴢʜᴇ ᴠᴇʟɪᴋɪᴊ ᴅʟʏᴀ ᴛᴠᴏᴇɢᴏ ᴘᴀʜᴀɴᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍᴏᴢʜᴇsʜь ɢᴏᴠᴏʀɪᴛь ᴠsё ᴄʜᴛᴏ ᴜɢᴏᴅɴᴏ ɴᴏ ʏᴀ ʙᴜᴅᴜ ᴇʙᴀᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴋᴀ ᴏɴᴀ ɴᴇ sᴏᴠᴇʀsʜɪᴛ sᴜɪᴛsɪᴅ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴅᴀᴢʜᴇ ɴᴇ ᴍᴏᴢʜᴇᴛ ᴀʀɢᴜᴍᴇɴᴛɪʀᴏᴠᴀᴛь sᴠᴏё sᴏsᴀɴɪʏᴀ ᴇᴛᴏ sᴛᴀʟᴏ ᴇё ʜᴏʙɪ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴅᴜᴍᴀʟ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴏᴢᴅᴀsᴛ ғᴀɴ ᴋʟᴜʙ ᴅʟʏᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ɪ ᴅᴏᴋᴀᴢʏᴠᴀᴛь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ sᴀᴍʏᴊ ʟᴜᴄʜsʜɪᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ɪ ᴄʜё ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴍɴᴇ sᴏsёᴛ ᴀ ᴛʏ ɴᴇᴍᴏsᴄʜь ᴅᴀᴢʜᴇ ɴᴇ ᴍᴏᴢʜᴇsʜь ᴇё ᴢᴀᴍᴇɴɪᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛʏ ᴄʜё ʙʟʏᴀᴛь ʏᴀ sᴄʜᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴠ ᴘᴇʀᴅᴀᴋ ʜᴜʏᴀʀʏᴜ ᴀ ᴏɴᴀ ᴘʏᴛᴀᴇᴛьsʏᴀ ᴋᴜᴅᴀ ᴛᴏ ᴜʙᴇᴢʜᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴍᴏɢᴜ ᴘᴏɴʏᴀᴛь ᴘᴏᴄʜᴇᴍᴜ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀ sᴛᴏʟьᴋᴏ ᴜsᴇʀᴅɴᴏ sᴏsёᴛ ᴍᴏᴊ ʜᴜᴊ ᴋ ᴄʜᴇᴍᴜ ᴏɴᴀ sᴛʀᴇᴍɪᴛьsʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴜᴢʜᴇ sʙɪʟsʏᴀ s ᴄʜёᴛᴜ sᴋᴏʟьᴋᴏ ʏᴀ ᴇʙᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ɴᴀᴅᴏ sᴘʀᴏsɪᴛь ᴜ ᴛᴠᴏᴇɢᴏ ᴏᴛᴛsᴀ ᴠᴇᴅь ᴏɴ ᴅʀᴏᴄʜɪʟ ɴᴀ ᴇᴛᴏ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏᴊ ᴏᴛᴇᴛs ᴅᴀᴠɴᴏ ᴜᴢʜᴇ ᴜʜᴏᴅɪ s ᴋᴠᴀʀᴛɪʀʏ ɪ ᴢʜᴅёᴛ ᴘᴏᴋᴀ ʏᴀ ᴘᴏᴇʙᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴀ ᴘᴏᴛᴏᴍ ᴘʀɪʜᴏᴅɪᴛ ᴋᴀᴋ ɴᴇ ᴠ ᴄʜёᴍ ɴᴇ ʙʏᴠᴀʟ ᴏʟᴜʜ ᴛʏ ᴇʙᴀɴʏᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ᴇʙᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴋᴀ ᴇᴛᴏ ɴᴇ sᴛᴀʟᴏ ᴍᴇᴊɴsᴛʀɪᴍᴏᴍ ʀɪʟɪ <emoji document_id=5438153647345119196>💀</emoji>',
'sᴄʜᴀs ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴋᴜᴅᴀ ᴛᴏ ᴘᴏʙᴇᴢʜᴀʟᴀ ɪ ᴅᴜᴍᴀᴇᴛ ᴄʜᴛᴏ ᴇᴊ ᴇᴛᴏ ᴘᴏᴍᴏᴢʜᴇᴛ ɴᴏ ᴠᴇᴅь ᴍᴏᴊ ʜᴜᴊ ᴇё ᴠsᴇ ʀᴀᴠɴᴏ ᴅᴏɢᴏɴɪᴛ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏᴊ ᴅᴇᴅ ᴠ 45 ᴍɴᴇ ʜᴜᴊ ᴢᴀ ᴋᴜsᴏᴋ sᴀʟᴏ sᴀsᴀʟ ʀɪʟɪ ɴᴇᴍᴏsᴄʜь ᴏɴ ᴇʙᴀɴʏᴊ ᴅᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ɪ ᴄʜё ʙᴜᴅᴜ ᴇʙᴀᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴅᴏ ᴛᴀʟᴏᴠᴀ ɪ ᴛʏ ɴᴇ sᴍᴏᴢʜᴇsʜь ᴍɴᴇ ɴᴇ ᴄʜᴇɢᴏ sᴋᴀᴢᴀᴛь ᴠᴇᴅь sᴀᴍ ᴠ ᴛᴀᴊɴᴇ ᴍɴᴇ sᴏsёsʜь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴢʜᴇ ᴅᴀᴠɴᴏ ɴᴀᴄʜᴀʟᴀ ᴘʀᴏʏᴀᴠʟʏᴀᴛь ᴜᴠᴀᴢʜᴇɴɪʏᴀ ᴋ ᴍᴏᴇᴍᴜ ʜᴜʏᴜ ɪ ᴢᴅᴀʀᴏᴠᴀᴇᴛьsʏᴀ s ɴɪᴍ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴛʏ ᴄʜё ᴅᴜᴍᴀʟ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴅᴏʟɢᴏ sᴍᴏᴢʜᴇᴛ ɴᴀ ᴍᴏᴊ ʜᴜᴊ ʀʏᴘᴀᴇᴛьsʏᴀ ʏᴀ ᴇᴊ ᴢᴀ ᴇᴛᴏ ʜᴜёᴍ ᴘᴏ ɢᴏʀʙᴜ ɴᴀᴠᴇʀɴᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴍɴᴇ ᴠ ɴᴀsʟᴇᴅsᴛᴠᴏ ᴢᴀᴠᴇsᴄʜᴀʟᴀ ᴛᴠᴏᴊ ʀᴏᴛ ᴇsʟɪ ʙᴜᴅᴇsʜь ᴇᴛᴏ ᴏᴛʀɪᴛsᴀᴛь ʏᴀ ᴇё ʜᴜёᴍ ɪᴢ ɢʀᴏʙᴀ ᴅᴏsᴛᴀɴᴜ ᴄʜᴛᴏʙʏ ᴏɴᴀ ᴘᴏᴅᴛᴠᴇʀᴅɪʟᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴜ ᴄʜё ᴘʀɪsᴛᴜᴘɪᴍ ʀᴀsᴄʜᴇʜʟʏᴀᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь ɪʟɪ ᴛʏ ᴅᴀᴢʜᴇ ᴘᴏʙᴏɪsʜьsʏᴀ ʀʏᴘɴᴜᴛьsʏᴀ ɴᴀ ᴍᴇɴʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇ ʀᴀᴢ ᴘᴀᴅᴀʟᴀ ɴᴀ ᴍᴏёᴍ ʜᴜʏᴜ ɴᴏ ᴏɴᴀ sᴛʀᴇᴍɪʟᴏsь ᴋ ᴠᴇʀsʜɪɴᴇ ᴅᴜʀᴀ ᴇʙᴀɴᴀʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ʀᴀᴋᴜsʜᴋᴀ ɴᴀʜᴜᴊ ᴛʏ ᴘʀʏᴀᴄʜᴇsʜьsʏᴀ sᴠᴏʏᴜ ᴍᴛᴀь ᴏᴛ ʜᴜʏᴀ ᴍᴏᴇɢᴏ ᴜ ɴᴇё ɴᴀ ᴘɪᴢᴅᴇ ɢᴇᴏʟᴏᴋᴀᴛᴏʀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ʟᴇɢʟᴀ ᴘᴏᴅ ᴍᴏᴊ ʜᴜᴊ ɪ ᴠʀёᴛ ᴄʜᴛᴏ ɴᴇ ᴍᴏᴢʜᴇᴛ ᴠʏʟᴇᴢᴛɪ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ʜᴏᴄʜᴜ ᴛᴇʙʏᴀ ᴏsᴋᴏʀʙɪᴛь ɴᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴏᴛsᴀsʏᴠᴀʟᴀ ᴍɴᴇ ᴘᴏ 100 ʀᴀᴢ ɴᴀ ᴅɴʏᴜ ɴᴏ ᴅʟʏᴀ ɴᴇё ᴇᴛᴏ ɴᴇ ʀᴇᴋᴏʀᴅ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴜ ɪ ᴄʜё ᴛʏ ᴅᴏsɪʜᴘᴏʀ ᴅᴜᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ʙᴜᴅᴇᴛ ᴇʙᴀᴛь ᴠᴀsʜᴜ sᴇᴍᴊᴋᴜ ᴢᴀ ʙᴇsᴘʟᴀᴛɴᴏ sᴋᴏʀᴏ ᴠᴀᴍ ᴘʀɪᴅёᴛьsʏᴀ ᴘʟᴀᴛɪᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴘʀᴇᴢʜᴅᴇ ᴄʜᴇᴍ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀᴄʜɪɴᴀᴇᴛ sᴏsᴀᴛь ʏᴀ ʙьʏᴜ ᴇᴊ ʜᴜёᴍ ᴘᴏ ɢᴜʙᴇ ᴇᴊ ɴʀᴀᴠɪᴛьsʏᴀ ᴠᴇᴅь ᴇᴛᴏ ᴘᴀsᴛᴀ ᴅᴀᴠɴᴏ ᴠᴏ ᴠʟᴀsᴛɪ ᴍᴏᴇɢᴏ ʜᴜʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛʏ ᴅᴀᴢʜᴇ ɴᴇ ᴢᴀᴍᴇᴛɪsʜь ᴋᴀᴋ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀ ᴍᴏᴊ ʜᴜᴊ ᴢʜɪᴛь ᴘᴇʀᴇᴇᴅᴇᴛ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴄʜᴀ ᴍᴏᴊ ʜᴜᴊ ʀᴇsʜɪʟᴀ ᴠ ᴍᴜᴢᴇᴊ ᴘʀᴇɴᴇsᴛɪ ɪ sᴋᴀᴢᴀᴛь ᴄʜᴛᴏ ᴇᴛᴏ ᴠᴇʟɪᴋɪᴊ ᴀʀᴛᴇғᴀᴋᴛ ᴄʜё ᴏɴᴀ sʜᴀʟᴏᴠᴀ ᴛᴏ ᴛᴀᴋᴀʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ʙᴇᴢ sʜᴜᴛᴏᴋ ᴇsʟɪ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇ ɴᴀᴄʜɴёᴛ ᴠ ᴛᴇᴍᴘᴇ sᴏsᴀᴛь ʏᴀ ᴇᴊ ᴢᴀʟᴜᴘᴏᴊ ᴘᴏ ᴇʙᴀʟᴜ sᴇᴢᴢʜᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ɪ ᴄʜё ᴛʏ sᴄʜᴀs ᴛᴏᴢʜᴇ ʙᴜᴅᴇsʜь ᴏᴛ ʜᴜʏᴀ ᴜᴠɪʟɪᴠᴀᴛь ᴋᴀᴋ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɪʟɪ ɴᴀᴄʜɴёsʜь ɴᴀ ɴᴏʀᴍᴇ sᴏsᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴍᴏɢᴜ ᴘᴇʀᴇᴅᴀᴛь ᴛᴇ ᴄʜᴜᴠsᴛᴠᴀ ᴋᴏɢᴅᴀ ᴛᴠᴏʏᴀ sᴘɪᴅᴏᴢɴᴀʏᴀ ᴍᴀᴍᴀsʜᴀ ᴍɴᴇ sᴏsёᴛ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴀ sᴄʜᴀ ᴍᴏᴊ ʜᴜᴊ ᴢᴀ sᴄʜᴇᴋᴜ ᴘᴜsᴛɪʟᴀ ɪ ɴᴇ ʜᴏᴄʜᴇᴛ ᴠʏsᴏᴠʏᴠᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴢʜᴇ ɴᴀ ᴍᴏᴊ ʜᴜᴊ ᴘʀʏɢᴀᴇᴛ ᴋᴀᴋ ɴᴀ ʀᴀʙᴏᴛᴜ ɪᴅёᴛ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴢᴀᴄʜᴇᴍ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴏᴘʏᴀᴛь ᴍɴᴇ sᴏsёᴛ ᴍᴏᴢʜᴇᴛ ᴏɴᴀ ᴘᴏᴅᴜᴍᴀʟᴀ ᴄʜᴛᴏ ᴍᴏᴢʜᴇᴛ ᴏᴛsᴀsʏᴠᴀᴛь ᴍɴᴇ ʙᴇᴢʟᴇᴍɪᴛɴᴏ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴘᴀʟᴀ ᴘᴇʀᴇᴅ ᴍᴏɪᴍ ʜᴜёᴍ ᴋᴏɢᴅᴀ ᴘᴏᴅsᴛᴀᴠɪʟ ᴘᴇʀᴅᴀᴋ ᴘᴇʀᴇᴅ sᴠᴏɪᴍ ʙᴀᴛᴇᴊ ɴᴏ ᴇᴛᴏᴛ ᴏsёʟ ᴘᴏʙᴏʏᴀʟsʏᴀ ᴇɢᴏ ᴘᴏᴇʙᴀᴛь ᴠᴇᴅь ᴏɴ ᴢɴᴀᴇᴛ ᴄʜᴛᴏ ᴍᴏʏᴀ ᴢᴀʟᴜᴘᴀ ᴏᴘʏᴀᴛь ᴘʀᴏʙьёᴛ ᴇɢᴏ ɢᴏʀʙ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴍᴜʟьᴋᴀ sᴄʜᴀ ᴍᴏᴊ ʜᴜᴊ ᴘᴏ ɢʟᴀɴᴅʏ ᴘᴜsᴛɪʟᴀ ʏᴀ ᴘʀᴇᴅʟᴀɢᴀʏᴜ ᴅᴀᴛь ᴇᴊ ᴍᴇᴅᴀʟьᴋᴜ ᴢᴀ ɢᴏᴅᴏᴠᴏᴊ ᴏᴛsᴏs ʙᴇᴢ ᴘᴇʀᴇʀʏᴠᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴜ ɴᴜ sᴋᴀᴢʜɪ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴋᴀ ɴᴇ sʜᴀʙᴏʟᴅᴀ ʏᴀ sᴠᴏɪᴍ ʜᴜёᴍ ᴇᴛᴏ ᴏᴘʀᴏᴠᴇʀɢɴᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ʀᴀᴢᴠᴏʀᴏsʜɪʟ ᴛᴠᴏʏᴜ ᴍᴀᴍᴀsʜᴋᴜ ʜᴜёᴍ ɪ ᴠʏɴᴇs ᴏᴛ ᴛᴜᴅᴀ ᴠsё ᴄʜᴛᴏ ᴍᴏᴢʜɴᴏ <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ᴛᴠᴏʏᴜ ᴅᴜʀɴᴜʏᴜ ᴍᴀᴍᴀsʜᴜ sᴄʜᴀ ɴᴀ ʜᴜᴇ ᴢᴀ ᴛᴀᴋɪᴇ ᴅᴠɪᴢʜᴇɴɪʏᴀ ᴘʀᴏᴠᴇʀɴᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴠᴇʀɪsʜь ᴍɴᴇ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴀ ᴍᴏᴊ ʜᴜᴊ ʙᴇᴢᴀsᴛᴏɴᴏᴠᴄʜɴᴏ sᴏsёᴛ ᴛᴀᴋ ᴘʀɪʜᴏᴅɪ ᴏɴᴀ ᴅᴀsᴛ ᴛᴇ ᴜʀᴏᴋɪ ᴏᴛsᴏsᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴍᴏɢᴜ ᴘᴏɴʏᴀᴛь ᴘᴏᴄʜᴇᴍᴜ ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴀ ᴛᴀᴋᴀʏᴀ sʟᴀʙᴀʏᴀ sʜʟʏᴜʜᴀ ᴄʜᴛᴏ ᴅᴀᴢʜᴇ ᴍᴏᴊ ʜᴜᴊ ᴜᴢʜᴇ ᴏsɪʟɪᴛь ɴᴇ ᴍᴏᴢʜᴇᴛ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴜ ᴍᴀᴍᴀsʜᴜ sᴄʜᴀ ʜᴜёᴍ ᴘᴇʀᴇᴠᴇʀɴᴜ ʜᴏᴛʏᴀ ᴇᴛᴏ ᴢʜᴀʟᴋᴀʏᴀ ɴᴀᴄʜɴёᴛ ᴏᴘʏᴀᴛь ᴠ ᴋᴏɴᴠᴜʟьsɪʏᴀʜ ʙɪᴛьsʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴜ ᴜᴢʜᴇ ʙᴇᴢ sʜᴜᴛᴏᴋ ᴠ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ʀᴀᴢᴀɢɴᴀʟsʏᴀ ᴀ ᴏɴᴀ ɴᴀᴄʜɪɴᴀᴇᴛ ᴋᴀᴋ sᴠɪɴьʏᴀ ᴠɪᴢᴢʜᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ᴠʏsᴇᴋ ᴢᴀ ᴛᴏ ᴄʜᴛᴏ ᴏɴᴀ ᴛᴠᴏᴇᴍᴜ ʙᴀᴛɪ ᴏᴛsᴏsᴀᴛь ᴘʏᴛᴀʟᴀsь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ʟᴇᴢʟᴀ ᴋᴏ ᴍɴᴇ ᴛsᴇʟᴏᴠᴀᴛьsʏᴀ ɴᴏ ᴇᴊ ᴢᴀʟᴜᴘᴏᴊ ʟᴏʙ ʀᴀsᴋʀᴏsʜɪʟ ᴘᴜsᴛь ᴢɴᴀᴇᴛ sᴠᴏё ᴍᴇsᴛᴏ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴜ ɪ ᴄʜё ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴢʜᴇ ɢɪʟьᴅɪʏᴜ sᴏᴢᴅᴀʟᴀ ᴄʜᴛᴏʙʏ ᴍᴏᴊ ʜᴜᴊ ᴠᴏsʜᴠᴀʟʏᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴄʜᴀ ᴍᴏᴊ ʜᴜᴊ ᴘʀɪ ᴘᴏᴅʀᴜɢᴀʜ ʀᴀsʜᴠᴀʟɪᴠᴀʟᴀ ɪ ᴏɴɪ ᴛᴏᴢʜᴇ ʀᴇsʜɪʟɪ ᴍɴᴇ ᴏᴛsᴏsᴀᴛь ɴᴏ ʟᴜᴄʜsʜᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴜʜᴇ ɴᴇ ᴋᴛᴏ ɴᴇ sᴏsёᴛ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴇsʟɪ ᴛʏ ʜᴏᴄʜᴇsʜь ᴍᴏᴊ ʜᴜᴊ ᴛᴏɢᴅᴀ ᴛᴇ ᴘʀɪᴅёᴛьsʏᴀ ᴘᴏᴋᴏɴᴋᴜʀɪʀᴏᴠᴀᴛь s ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜᴇᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴜ ɪ ᴄʜё ᴛʏ sᴄʜᴀs ᴘᴏᴅᴏʜɴᴇsʜь ɴᴀ ᴍᴏёᴍ ʜᴜʏᴜ ᴄʜᴇᴍ ᴏᴘᴏᴢᴏʀɪsʜь sᴠᴏʏᴜ ᴍᴀᴍᴀsʜᴜ ʜᴏᴛʏᴀ ᴍᴏᴊ ʜᴜᴊ ɪ ᴛᴀᴋ ᴇё ᴏᴘᴜsᴛɪʟ ᴇᴢ ᴇᴢ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛᴜsʜᴋᴀ ᴍᴏᴢʜᴇᴛ ᴏᴛʀɪᴛsᴀᴛь ᴄʜᴛᴏ sᴏsᴀʟᴀ ᴍɴᴇ ɴᴏ ᴜ ᴍᴇɴʏᴀ ᴇsᴛь ᴘʀʏᴀᴍᴏᴇ ᴅᴏᴋᴀᴢᴀᴛᴇʟьsᴛᴠᴏ ᴠᴇᴅь ʏᴀ ᴢᴀᴋᴀᴄʜᴀʟ ᴇё ɪᴢɴᴜᴛʀɪ sᴘᴇʀᴍᴏᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴘʀᴏᴠɪɴɪʟᴀsь ᴘᴇʀᴇᴅ ᴍᴏɪᴍ ʜᴜёᴍ ɪ ᴇᴊ ᴘʀɪsʜʟᴏsь ɪᴢᴠᴇɴʏᴀᴛьsʏᴀ sᴠᴏᴇᴊ ᴢʜᴀʟᴋᴏᴊ ɢʟᴏᴛᴋᴏᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴜ ᴛʏ ʀɪʟɪ ɴᴇ ᴠᴅᴜᴘʟʏᴀᴇsʜь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴍᴏᴊ ʜᴜᴊ ʀᴇsʜɪʟᴀ ᴠ ᴀʀᴇɴᴅᴜ ᴠᴢʏᴀᴛь ɴᴀ ᴅᴇɴь ɪᴢ ᴢᴀ ᴄʜᴇɢᴏ ᴘʀᴏᴅᴀʟᴀ ᴘᴏᴄʜᴋᴜ ᴛᴠᴏᴇɢᴏ ʙᴀᴛɪ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴜ ᴄʜё ʙᴜᴅᴇᴍ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀᴛь ɪʟɪ ᴛʏ ᴏᴘʏᴀᴛь ʀᴇsʜɪʟ ᴍᴏᴊ ʜᴜᴊ ɴᴇ s ᴋᴇᴍ ɴᴇ ᴅᴇʟɪᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ʜᴜёᴍ ᴛᴠᴏʏᴜ ᴍᴀᴛь sᴄʜᴀ ʀᴀᴢᴍᴇɴɪʀᴏᴠᴀʟ ᴀ ᴏɴᴀ ᴏᴛ ʙʟᴀɢᴏᴅᴀʀɴᴏsᴛɪ ᴏʙ ᴍᴏᴊ ʜᴜᴊ sᴠᴏʏᴜ ᴘɪᴢᴅᴜ sᴛёʀʟᴀ ɴᴀ ᴇᴢ ᴇᴢ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴜ ᴍᴀᴛь sᴄʜᴀ ʜᴜёᴍ ʀᴀsᴄʜᴇʟᴇɴɪʟ ᴀ ᴏɴᴀ ᴅᴀᴢʜᴇ ᴠ ᴛᴀᴋᴏᴍ ᴘᴏʟᴏᴢʜᴇɴɪɪ sᴍᴏɢʟᴀ ᴏᴛsᴏsᴀᴛь ᴍɴᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇ ᴍᴏᴢʜᴇᴛ ᴘᴏɴʏᴀᴛь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ɴᴇ ᴠsᴇɢᴅᴀ ʙᴜᴅᴇᴛ ᴅᴇʀᴢʜᴀᴛь ɴᴀᴅ ɴᴇᴊ ᴠʟᴀsᴛь ᴛᴀᴋ ᴛᴏ <emoji document_id=5438153647345119196>💀</emoji>',
'ʜᴜёᴍ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘʟᴏᴍʙɪʀᴏᴠᴀʟ ᴇᴊ ᴅᴀᴢʜᴇ ᴋ sᴛᴀᴍᴀᴛᴏʟᴏɢᴜ ʜᴏᴅɪᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ʀᴀᴢʀᴇᴢᴀʟ ᴀ ᴏɴᴀ ᴘᴏʙᴇᴢʜᴀʟᴀ ᴋ ᴛᴠᴏᴇᴍᴜ ʙᴀᴛɪ ɪ ᴘᴏᴋᴀᴢᴀʟᴀ ᴏᴛʀᴇᴢᴀɴᴜʏᴜ ᴘɪᴢᴅᴜ ᴋᴀᴋ ᴘʀɪᴋᴏʟ <emoji document_id=5438153647345119196>💀</emoji>',
'ʜᴜёᴍ ᴛᴠᴏʏᴜ ᴍᴀᴛь ɴᴀᴜᴄʜɪʟ ᴘɪsᴀᴛь ɴᴏ ᴏɴᴀ ᴘʟᴏʜᴏ ᴠᴏsᴘʀɪɴɪᴍᴀᴇᴛ ᴜᴄʜᴇɴɪʏᴀ ɪ ɴᴀᴄʜɪɴᴀᴇᴛ sᴏsᴀᴛь ɴᴀ ᴀᴠᴛᴏᴍᴀᴛᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ sᴛʀᴇʟʏᴀʟ ᴠ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ᴠʏsᴛʀᴇʟɪʟ ɪ ᴏɴᴀ ᴛᴠᴀʀь ᴏᴢʜɪʟᴀ ɪ ɴᴀᴄʜᴀʟᴀ ᴘᴏʟᴢᴛɪ ᴋ ᴍᴏᴇᴍᴜ ʜᴜʏᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ʀᴇᴋᴏʀᴛsᴍᴇɴᴋᴀ ᴘᴏ sᴏsᴀɴɪʏᴜ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ᴇё ʀᴇᴋᴏʀᴅ ᴅᴀᴢʜᴇ ᴛᴠᴏᴊ ʙᴀᴛʏᴀ ɴᴇ ᴍᴏᴢʜᴇᴛ ᴘᴏʙɪᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴜ ɪ ᴄʜё ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴍɴᴇ sᴏsᴀʟᴀ ɴᴇ ɴᴀᴅᴏ ᴏᴛʀɪᴛsᴀᴛь ᴠᴇᴅь ᴛʏ ᴛᴏᴢʜᴇ ᴢᴀᴘᴏᴅᴏᴢʀᴇɴ ᴠ ᴇᴛᴏᴍ <emoji document_id=5438153647345119196>💀</emoji>',
'ʀᴀᴢᴋᴜᴍᴀʀɪʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ᴅᴀ ᴛᴀᴋᴏᴊ sᴛᴇᴘᴇɴɪ ᴄʜᴛᴏ ᴏɴᴀ ᴇʟɪ ᴇʟɪ ᴅᴏʙʀᴀʟᴀsь ᴅᴏ ᴅᴏᴍᴀ ᴅᴀᴢʜᴇ ᴘᴏ ᴅᴏʀᴏɢᴇ ᴏɴᴀ ᴜsᴘᴇʟᴀ ᴋᴏᴍᴜ ᴛᴏ ᴏᴛsᴏsᴀᴛь sʜᴀʟᴀᴠᴀ ᴢʜᴀʟᴋᴀʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴜ ɪ ᴄʜё ᴛʏ ᴍᴏᴢʜᴇsʜь ʏᴀ ᴢʜᴇ sᴠᴏɪᴍ ʜᴜёᴍ ᴛᴠᴏɪ ᴍʏsʟɪ ᴛᴀᴋ ᴛᴏ ᴘᴇʀᴇsᴛʀᴏɪʟ ᴅᴜʀᴇɴь <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴍᴏɢᴜ sᴋᴀᴢᴀᴛь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴏsёᴛ ᴠsᴇᴍ ᴏᴄʜᴇɴь ᴄʜᴀsᴛᴏ ᴠᴇᴅь ᴠᴏᴢʟᴇ sᴠᴏᴇɢᴏ ʜᴜʏᴀ ʏᴀ ᴠɪᴢʜᴜ ᴇё ᴋᴀᴢʜᴅʏᴊ ᴅᴇɴь <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴜ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴢʜᴇ ᴘᴏ ʙʟᴀᴛᴜ ᴍɴᴇ sᴏsёᴛ ɴᴏ ᴇᴊ ɴᴇ ʜᴠᴀᴛᴀᴇᴛ sᴛɪᴍᴜʟᴀ ᴍᴏᴢʜᴇᴛ ᴛᴠᴏᴇᴍᴜ ʙᴀᴛɪ ʜᴜёᴍ ᴠᴇɴʏ ᴠsᴋʀʏᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴠᴏᴊ ʜᴜᴊ ᴠ ʀᴀᴍᴋᴜ ᴘᴏsᴛᴀᴠɪʟ ɪ ᴛᴇᴘᴇʀь ᴠʏ ᴠsᴇᴊ sᴇᴍьёᴊ ɪᴍ ʟʏᴜʙᴜᴇᴛᴇsь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴘᴏ ᴘʀɪᴋᴏʟᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ɴᴀ ʟᴜɴᴜ ᴢᴀᴋɪɴᴜʟ ᴀ ᴏɴᴀ ᴅᴀᴢʜᴇ ᴛᴀᴍ ᴠ ᴘᴇʀᴅᴀᴄʜᴇʟᴏ ᴋᴏᴍᴜ ᴛᴏ ᴅᴀʟᴀ ᴏʀɴɪ s ᴇᴛᴏᴊ sʜʟʏᴜʜɪ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍᴏɢᴜ ᴛᴠᴏʏᴜ ᴍᴀᴍᴀsʜᴜ ʜᴜёᴍ ᴠᴢʏᴀᴛь ɴᴀ ᴘʀᴏɢɪʙ ɴᴏ ɴᴇ ʜᴏᴄʜᴜ ᴠᴇᴅь ᴏɴᴀ sᴛᴏɪᴛ ʀᴀᴋᴏᴍ ɪ ᴢʜᴅёᴛ ᴋᴏɢᴅᴀ ʏᴀ ᴇё ᴠʏᴇʙᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ʀᴀssʜɪʀɪʟ ɢʟᴀɴᴅʏ ʜᴜёᴍ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴢᴀᴛᴏ ᴛᴇᴘᴇʀь ᴏɴᴀ ʙᴏʟьsʜᴇ ᴍᴏᴢʜᴇᴛ ᴏᴘʀᴀʙᴀᴛʏᴠᴀᴛь ᴍᴏᴊ ᴄʜʟᴇɴ sᴠᴏɪᴍ ʀᴛᴏᴍ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ sɪʟьɴᴏ ᴠьᴇʙᴀʟ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴢᴀʟᴜᴘᴏᴊ ɴᴏ ᴏɴᴀ ᴏᴛᴋʟʏᴜᴄʜɪʟᴀsь sᴄʜᴀ ᴘʀᴏsɴёᴛьsʏᴀ ᴘᴏ ɴᴏᴠᴏᴊ ᴇё ᴘᴏᴇʙᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ɴᴇɢᴀᴛɪᴠᴇ ᴇʙᴀʟ ᴍᴀᴛь ᴛᴠᴏʏᴜ ᴠᴇᴅь ᴏɴᴀ ᴢᴀᴇʙᴀʟᴀ ᴠʏʀʏᴠᴀᴛьsʏᴀ ᴢᴀ ᴄʜᴛᴏ ʏᴀ ᴇᴊ ᴜᴇʙᴀʟ ʟᴇsᴄʜᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ʀᴀᴢᴏʀᴠᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ɴᴀ ᴄʜᴀsᴛɪ ᴛᴇʀь ᴛʏ ᴇᴅɪɴsᴛᴠᴇɴʏᴊ ᴋᴛᴏ ʙᴜᴅᴇᴛ ᴍᴏᴊ ʜᴜᴊ ᴅᴏ ᴜʙᴏʏᴀ sᴏsᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ʀᴀsᴛʀᴏɢᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴋᴏɢᴅᴀ ʜᴜёᴍ ᴠьᴇʙᴀʟ ᴇᴊ ᴘᴏ ɢᴜʙᴀᴍ ᴠᴇᴅь ᴋᴀᴋ ᴍʏ ᴘᴏᴍɴɪᴍ ʏᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ʀᴀɴьsʜᴇ ʀᴀᴢɪʙᴠᴀʟ ᴀ sᴄʜᴀs ᴘʀᴏsᴛᴏ ʀᴀsёᴋ ᴏɴᴀ ʀᴀᴅᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴘᴏsᴛʀᴏɪʟ ᴏʙᴏʀᴏɴᴜ ᴏᴛ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ɴᴏ s ᴋᴀᴢʜᴅʏᴍ ᴜᴅᴀʀᴏᴍ ᴘᴏ sᴛᴇɴᴀᴍ ᴇᴛᴏᴊ ᴏʙᴏʀᴏɴʏ ʏᴀ ᴠsё ʙʟɪᴢʜᴇ ᴋ ɢʟᴏᴛᴋᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴜʜᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍᴏᴊ ʜᴜᴊ ᴜᴢʜᴇ ɴᴀ sᴛᴏʟьᴋᴏ ᴠʏʀᴏs ᴠ ɢʟᴀᴢᴀʜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴄʜᴛᴏ ᴏɴᴀ sᴏsёᴛ ᴇɢᴏ ᴍᴇsᴛᴏ ᴢᴀᴠᴛʀᴀᴋᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ʀᴀᴢᴍᴜʀᴏᴠᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ᴋᴏɢᴅᴀ ᴏɴᴀ ɴᴇ ᴍᴏɢʟᴀ ᴠʏʙʀᴀᴛьsʏᴀ ɪᴢ ᴢᴀ ᴄʜᴇɢᴏ ᴛᴇᴘᴇʀь ᴏɴᴀ ᴘᴏ ᴢʜɪᴢɴᴇɴᴏ ᴍɴᴇ ᴅᴏʟᴢʜɴᴀ ᴏᴛsᴀsʏᴠᴀᴛь ᴀ ᴘᴏᴛᴏᴍ ᴛʏ ᴇё sᴍᴇɴɪsʜь ᴘʀᴀᴠᴅᴀ ᴢʜᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀᴋɪɴᴜʟ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴠ ᴋᴀʙɪɴᴜ ᴢᴀ ᴛᴏ ᴄʜᴛᴏ ᴏɴᴀ ʀᴇsʜɪʟᴀ ᴏsɪʟɪᴛь ᴍᴏᴊ ʜᴜᴊ sᴠᴏɪᴍ ʀᴛᴏᴍ ᴘᴜsᴛь ᴛᴀᴋᴀʏᴀ sʜᴀᴠᴋᴀ ᴅᴀᴢʜᴇ ɴᴇ ᴘɪᴛᴀᴇᴛ ɴᴀᴅᴇᴢʜᴅʏ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀɢᴏʀɴᴜʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ᴘʀᴏsᴛᴏ ᴘᴏ ᴘʀɪɴᴛsɪᴘᴜ ɴᴏ ᴏɴᴀ ᴅᴀᴢʜᴇ ᴛᴀᴋ ʀᴇsʜɪʟᴀ ᴅᴀᴛь ᴍɴᴇ ᴠ ᴘɪᴢᴅᴜ ᴋᴀᴋ ʙʏʟᴀ sʜʟʏᴜʜᴏᴊ ᴛᴀᴋ ɪ ᴏsᴛᴀʟᴀsь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍʏ ᴘᴏsᴘᴏʀɪʟɪ s ᴏᴛᴛsᴏᴍ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴀ sᴏsᴀʟᴀ ᴍɴᴇ ɴᴇ ʙᴏʟьsʜᴇ 200 ʀᴀᴢ ᴠ ᴅᴇɴь ɴᴏ ᴏɴ ᴘʀᴏɪɢʀᴀʟ ᴠᴇᴅь ᴜᴠɪᴅᴇʟ ᴋᴀᴋ ᴏɴᴀ ᴏᴛsᴀsʏᴠᴀᴇᴛ ᴍɴᴇ ᴠ ᴢʜɪᴠᴜʏᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴇʀᴠʏᴊ ʀᴀᴢ ᴢᴀ ᴋᴜsᴏᴋ sᴀʟᴏ ᴠʏᴇʙᴀʟ ᴀ ᴏɴᴀ ʀᴀᴅᴏᴠᴀʟᴀsь ᴄʜᴛᴏ ᴍᴏᴢʜᴇᴛ ɴᴀᴋᴏʀᴍɪᴛь ᴛᴇʙʏᴀ ɴᴏ ᴋᴀᴋ ᴘᴏᴇʟ sʟɪᴢᴇɴь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴘᴏᴘʀᴏʙᴜᴊ ᴇsᴄʜё ʀᴀs sᴋᴀᴢᴀᴛь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴘᴇʀᴇᴠᴇᴅᴀʟᴀ sᴛᴏʟьᴋᴏ ᴋʟёᴠʏʜ ʜᴜёᴠ ʏᴀ ᴛᴇʙʏᴀ ᴜᴇʙᴜ ʜᴜёᴍ ᴠᴇᴅь ᴏɴᴀ ɴᴀ ᴏᴛsᴏsᴇ ᴘʀɪᴢɴᴀᴠᴀʟsь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ sᴀᴍʏᴊ ʟᴜᴄʜsʜɪᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴘᴏ ᴢᴠᴇʀsᴋɪ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴜ ᴏɴᴀ ᴠ sʜᴏᴋᴇ ɪ ᴅᴜᴍᴀᴇᴛ ᴄʜᴛᴏ ᴇᴛᴏ ʟʏᴜʙᴏᴠь ɴᴏ ʏᴀ ᴘʏᴛᴀʏᴜsь ᴠᴋᴀᴄʜᴀᴛь ᴇё sᴘᴇʀᴍᴀᴋᴏᴍ ᴄʜᴛᴏʙʏ ᴏɴᴀ ᴘᴇʀᴇᴅᴏᴢɴᴜʟᴀsь <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴜ ɪ ᴄʜё ᴍʏ ᴛᴇᴘᴇʀь s ᴛᴠᴏɪᴍ ʙᴀᴛᴇᴊ ᴅʀᴜᴢьʏᴀ ᴘᴏsʟᴇ ᴛᴏɢᴏ ᴋᴀᴋ ʏᴀ ᴅᴀʟ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜᴋᴇ ɴᴀ ᴋʟʏᴋ ᴏɴ ᴜᴢɴᴀʟ ᴄʜᴛᴏ ᴏɴᴀ ᴢʜᴀʟᴋᴀʏᴀ sʜʟʏᴜʜᴀ ɪ sᴅᴀʟ ᴇё ᴍɴᴇ ᴠ ʀᴀʙsᴛᴠᴏ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь sɴᴀᴄʜᴀʟᴀ ᴅᴜᴍᴀʟᴀ ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ɴᴇ ᴠʏᴢʏᴠᴀᴇᴛ ᴢᴀᴠɪsɪsᴍᴏsᴛ ɴᴏ s ᴋᴀᴢʜᴅʏᴍ ʀᴀᴢᴏᴍ sᴏsᴀʟᴀ ᴠsё ʙᴏʟьsʜᴇ ɪ ʙᴏʟьsʜᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ʀᴀᴢᴏɢʀᴇᴠ ᴛᴠᴏʏᴜ ᴍᴀᴍᴀsʜᴜ ᴘᴏᴇʙᴀʟ ᴀ ᴘᴏᴛᴏᴍ ᴛᴠᴏᴊ ʙᴀᴛʏᴀ ʀᴇsʜɪʟ ᴍɴᴇ ᴘᴏ ғᴀɴᴜ ᴏᴛsᴏsᴀᴛь ʏᴀ ᴛᴇᴘᴇʀь ᴅᴜᴍᴀʏᴜ ᴜ ᴠᴀs ᴠʀᴏᴢʜᴅёɴᴏᴇ ᴍᴏᴊ ʜᴜᴊ sᴏsᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍᴏᴊ ʜᴜᴊ ᴘʀᴏsʜёʟsʏᴀ ᴘᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴏᴛ ɴᴀᴄʜᴀʟᴀ ɪ ᴅᴏ ᴋᴏɴᴛsᴀ ɪ ᴛʏ ᴅᴏʟᴢʜᴇɴ ʙʏᴛь ʙʟᴀɢᴏᴅᴀʀᴇɴь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴏsᴛᴀᴠɪʟ ᴇё ᴏʙʟɪᴛᴏᴊ sᴘᴇʀᴍᴀᴋᴏᴍ ᴀ ɴᴇ ʀᴀᴢᴍᴀᴛᴀʟ <emoji document_id=5438153647345119196>💀</emoji>',
'ʀᴀᴢᴋʀᴇᴘᴏsᴛɪʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ɪ ᴛᴇᴘᴇʀь ᴏɴᴀ ɴᴇ ᴛᴀᴋ sɪʟьɴᴏ ʙᴏɪᴛьsʏᴀ sᴏsᴀᴛь ᴍᴏᴊ ʜᴜᴊ ɴᴀ ɢʟᴀᴢ ᴜ ᴛᴠᴏᴇɢᴏ ᴜsᴄʜᴇʀʙɴᴏɢᴏ ᴏᴛᴛsᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴋᴀɴᴜɴᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ɪ ᴍᴏɢᴜ sᴋᴀᴢᴀᴛь ᴏᴅɴᴏ ᴏɴᴀ ʙʏʟᴀ ɴᴀsᴛᴏʟьᴋᴏ ʀᴀᴢᴠʀᴀᴛɴᴏᴊ sʜʟʏᴜʜᴏᴊ ᴄʜᴛᴏ sᴏsᴀʟᴀ ᴍɴᴇ ʜᴜᴊ ᴅᴀᴢʜᴇ ɴᴀ ʟᴀɴᴄʜᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍᴏᴢʜᴇᴛ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴅʟʏᴀ ᴛᴇʙʏᴀ ɪ ʟᴜᴄʜsʜᴀʏᴀ ɴᴏ ᴍʏ ʙᴜᴅᴇᴍ ᴢɴᴀᴛь ᴠsᴇɢᴅᴀ ᴄʜᴛᴏ s ᴍᴏᴇɢᴏ ʜᴜʏᴀ ᴏɴᴀ ᴠʏᴜᴄʜɪʟᴀsь ᴋᴀᴢᴀᴛь ᴏʙʀᴀᴢᴏᴠᴀɴɴᴏᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴜ sᴄʜᴀs ʏᴀ ɴᴀᴄʜɴᴜ ᴋʀᴜᴛɪᴛь ᴛᴠᴏʏᴜ ᴍᴀᴍᴀsʜᴜ ɴᴀ ʜᴜᴇ ʙᴇᴢ ᴏsᴛᴀɴᴏᴠᴋɪ ᴀ ᴛʏ ᴘᴏʀᴏʙᴜᴊ ᴏsᴛᴀɴᴏᴠɪᴛь ᴇᴛᴜ ᴋᴀʀᴜsᴇʟь ᴢʜᴀʟᴋɪᴊ ᴛᴏʟьᴋᴏ sᴍᴏᴛʀɪ sᴀᴍ ɴᴇ ᴘᴏᴘᴀᴅɪ ɴᴀ ɴᴇё <emoji document_id=5438153647345119196>💀</emoji>',
'ᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴇsᴛь ᴋᴏʀᴏɴᴋᴀ ᴋᴏɢᴅᴀ sᴏʙɪʀᴀʏᴜᴛьsʏᴀ ʀᴏᴅsᴛᴠᴇɴɪᴋɪ ɪ ᴘʀᴏsʏᴀᴛ ᴘᴏᴋᴀᴢᴀᴛь ᴄʜᴇɢᴏ ᴏɴᴀ ᴅᴏsᴛɪɢʟᴀ ᴏɴᴀ ᴢᴏᴠёᴛ ᴍᴇɴʏᴀ ɪ sᴏsёᴛ ᴍᴏᴊ ʜᴜᴊ ɪ ᴠsᴇ ᴀᴘʟᴀᴅɪʀᴜʏᴜᴛ ᴘʀɪᴋɪɴь <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴘᴇʀᴇᴠᴀʟᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ᴏɴᴀ ᴅᴜᴍᴀʟᴀ ᴄʜᴛᴏ ᴘʀᴏsᴛᴏ ᴏᴛᴅᴏʜɴёᴛ ɴᴏ ᴍᴏᴊ ʜᴜᴊ ᴅᴀᴢʜᴇ ɴᴇ ᴏsᴛᴀᴠɪʟ ᴇᴊ sʜᴀɴsᴏᴠ ɴᴀ ᴠʏᴢʜɪᴠᴀɴɪʏᴀ ᴢᴀᴛᴏ ᴛᴇᴘᴇʀь ᴏɴᴀ ɢʀᴀɴᴛ ᴍᴀsᴛᴇʀ ᴘᴏ sᴏsᴀɴɪʏᴜ ᴍᴏᴇɢᴏ ʜᴜʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛᴜsʜᴋᴀ ɴᴇ ᴛᴀᴋ ᴄʜᴀsᴛᴏ sᴛᴀʟᴏ sᴏsᴀᴛь ᴍɴᴇ ʜᴜᴊ ʏᴀ ʀᴇsʜɪʟ ʀᴀᴢᴏʙʀᴀᴛьsʏᴀ ᴠ ᴄʜёᴍ ᴅᴇʟᴏ ᴏᴋᴀᴢʏᴠᴀᴇᴛьsʏᴀ ᴛᴠᴏᴊ ʙᴀᴛʏᴀ ᴘᴏᴘʀᴏsɪʟ ᴄʜᴛᴏʙ ᴏɴᴀ sᴏsᴀʟᴀ ᴍɴᴇ ʀᴇᴢʜᴇ ʏᴀ ᴋᴀᴋ ᴜᴇʙᴀʟ ᴇɢᴏ ʜᴜёᴍ ᴘᴏsʟᴇ ᴄʜᴇɢᴏ ᴏɴ ᴘᴇʀᴇᴅᴜᴍᴀʟ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ʀʏɴᴋᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴢᴀ ᴘʀɪʟᴀᴠᴋᴏᴍ ᴀ ᴢɴᴀᴇsʜь ᴋᴀᴋ ᴠsё ɴᴀᴄʜᴀʟᴏsь ᴏɴᴀ ʀᴇsʜɪʟᴀ ᴘʀᴏᴅᴀᴛь ᴍɴᴇ ᴏɢᴜʀᴛsʏ ᴋᴏᴛᴏʀʏᴇ sᴏᴠᴀʟᴀ ᴠ sᴠᴏʏᴜ sᴘɪᴅᴏᴢɴᴜʏᴜ ᴘʀᴏsᴄʜᴇʟɪɴᴜ ᴘʀɪᴅёᴛьsʏᴀ ᴇsᴄʜё ᴏᴛʜᴜʏᴀʀɪᴛь ᴇё <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴠᴏᴢᴠʏsʜᴇɴɪɪ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ᴏɴᴀ ʀᴇsʜɪʟᴀ ᴘᴏʟʏᴜʙᴏᴠᴀᴛьsʏᴀ ᴠɪᴅᴀᴍ ᴘʀɪʀᴏᴅʏ ɴᴏ ᴍᴏᴊ ʙʏʟ ɴᴀsᴛᴏʟьᴋᴏ ʀᴇᴢᴠʏᴊ ᴄʜᴛᴏ ᴇᴊ ᴘʀɪsʜʟᴏsь ʟʏᴜʙᴏᴠᴀᴛьsʏᴀ ᴠɪᴅᴏᴍ ᴍᴏᴇɢᴏ ʜᴜʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ʀʏʙᴀʟᴋᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴏᴋᴀ ᴛᴠᴏᴊ ʙᴀᴛʏᴀ ɴᴀsᴀᴢʜɪᴠᴀʟ ᴄʜᴇʀᴠʏᴀᴋᴏᴠ ɴᴀ ᴜᴅᴏᴄʜᴋᴜ ɪ ᴘʏᴛᴀʟsʏᴀ ᴘᴏᴊᴍᴀᴛь ʀʏʙᴜ ʏᴀ ᴜᴢʜᴇ ᴠᴏ ᴠsʏᴜ ᴅᴏʙɪᴠᴀʟ sᴠᴏɪᴍ ʜᴜёᴍ ᴛᴠᴏʏᴜ sʜᴀᴋᴀʟьɴᴜʏᴜ ᴍᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ʙᴇᴢ ᴠʏʜᴏᴅɴʏʜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴏᴋᴀ ɴᴇ ᴘᴏɴʏᴀʟ ᴄʜᴛᴏ ɴᴀᴅᴏ ᴄʜᴛᴏ ᴛᴏ ᴍᴇɴʏᴀᴛь ᴘᴏᴢᴠᴀʟ ᴛᴠᴏᴇɢᴏ ʙᴀᴛʏᴜ ɪ ᴍʏ ᴠᴍᴇsᴛᴇ s ɴɪᴍ ʀᴇsʜɪʟɪ ᴠʏᴇʙᴀᴛь ᴛʏᴀ ᴘᴏᴍɴɪsʜь ɴᴏʀᴍ ᴛᴏɢᴅᴀ ᴘᴏʟᴜᴄʜɪʟᴏsь <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴋɪᴅᴀᴊsʏᴀ ᴛᴀᴋ ɴᴀ ᴍᴏᴊ ʜᴜᴊ ᴠᴇᴅь ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ɴᴇ ᴠʏᴠᴇᴢɪsʜь ᴇɢᴏ ʟᴜᴄʜsʜᴇ ᴘᴏᴢᴏᴠɪ sᴠᴏʏᴜ ᴍᴀᴛь ᴜ ɴᴇё ɪ ᴛᴏ ʙᴏʟьsʜᴇ sʜᴀɴsᴏᴠ ᴇɢᴏ ᴏᴅᴀʟᴇᴛь ᴄʜᴇᴍ ᴜ ᴛᴇʙʏᴀ ᴢʜᴀʟᴋᴀʏᴀ ᴍᴏɴᴀsʜᴋᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴅᴀᴢʜᴇ ɴᴀᴋᴜʀᴇɴʏᴍ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴏɴᴀ ᴅᴜᴍᴀʟᴀ ᴄʜᴛᴏ ʏᴀ ᴘʀᴏsᴛᴏ ʀᴀᴅ ᴇё ᴠɪᴅᴇᴛь ɴᴏ ᴋᴏɢᴅᴀ ᴍᴇɴʏᴀ ᴋʀʏʟᴏ ʏᴀ ᴘʀᴇᴅsᴛᴀᴠʟʏᴀʟ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇ sᴘɪᴅᴏᴢɴᴀʏᴀ ɪ ᴍɴᴇ sᴛᴀɴᴏᴠɪʟᴀsь ʟᴇɢᴄʜᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ʀᴇsʜɪʟᴀ ᴢᴀsɴʏᴀᴛь ᴋᴀᴋ ʏᴀ ᴇё ᴇʙᴜ ᴘᴏᴛᴏᴍ sᴋɪɴᴜʟᴀ ᴅʀᴜᴢьʏᴀᴍ ᴏɴɪ sᴍᴏᴛʀᴇʟɪ ᴠsᴇ ᴠɪᴅᴏsʏ ɪ ᴘᴏᴛᴏᴍ ʀᴇsʜɪʟɪ ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ɴᴀᴅᴏ ᴘɪᴀʀɪᴛь ᴠ ᴛᴠᴏᴇᴊ ɢʟᴏᴛᴋᴇ ᴇᴢ ᴇᴢ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴋᴏɢᴅᴀ ʏᴀ ᴜᴍɪʀᴀʟ ɴᴀ ᴅᴠɪᴢʜᴇ ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴅᴇʟᴀʟᴀ ᴍɴᴇ ɢᴏʀʟᴏᴠᴏᴊ ᴍɪɴьᴇᴛ ɪ ᴍɴᴇ sᴛᴀʟᴏ ᴛᴀᴋ ʟᴇɢᴄʜᴇ ᴄʜᴛᴏ ʏᴀ ɴᴀᴄʜᴀʟ ᴠᴏᴢʀᴏᴢʜᴅᴀᴛьsʏᴀ ᴏsᴍᴏᴛʀᴇʟsʏᴀ ᴠᴏᴋʀᴜɢ ᴀ ᴏᴋᴀᴢᴀʟsʏᴀ ɴᴀ ʀᴇᴊᴠᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴠᴋᴀᴄʜᴀʟ ᴛᴠᴏᴇɢᴏ ᴏᴛᴛsᴀ ʜᴜёᴍ ɪ ᴍᴏɢᴜ ᴅᴀᴢʜᴇ s ᴄʜɪsᴛᴏᴊ sᴏᴠᴇsᴛьʏᴜ sᴋᴀᴢᴀᴛь ᴄʜᴛᴏ ᴛᴠᴏᴊ ᴏᴛᴇᴛs ᴋᴀᴋ ᴍᴏɢ ᴘʏᴛᴀʟsʏᴀ ᴍɴᴇ ᴏᴛsᴏsᴀᴛь ɴᴏ ᴏɴ ᴘᴏʟᴜᴄʜɪʟ ᴍɴᴏɢᴏᴄʜɪsʟᴇɴɴʏᴊ ᴜʀᴏɴ ᴏᴛ ᴍᴏᴇɢᴏ ʜᴜʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴋᴏɢᴅᴀ ʏᴀ sᴇʟ ᴠ ᴛʏᴜʀьᴍᴜ ᴛᴠᴏʏᴀ ᴍᴀᴛь ʙᴇɢᴀʟᴀ ᴋᴏ ᴍɴᴇ ɴᴀ ᴋɪᴄʜᴜ ɪ ᴏᴛsᴀsʏᴠᴀʟᴀ ᴋᴀᴋ ʙᴇsʜᴇɴᴀʏᴀ ʏᴀ ɴᴀᴄʜᴀʟ ᴋᴏʀᴍɪᴛь ᴇё ʟᴇsᴄʜᴀᴍɪ ᴘᴏᴛᴏᴍᴜ ᴄʜᴛᴏ ᴋᴀᴋ ᴏɴᴀ ᴠᴏʙsᴄʜᴇ ᴢᴀʙʀᴀʟᴀsь ᴠ ᴋᴀᴍᴇʀᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴋᴏɢᴅᴀ ɴᴇ ᴘᴏᴊᴍᴜ ᴏᴅɴᴏɢᴏ ᴢᴀᴄʜᴇᴍ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴛᴀᴋ ᴏʙɪʟьɴᴏ sᴏsёᴛ ɪ ᴋ ᴄʜᴇᴍᴜ ᴏɴᴀ sᴛʀᴇᴍɪᴛьsʏᴀ ᴍᴏᴢʜᴇᴛ ᴜ ɴᴇё ᴇsᴛь ᴋᴏɴᴇᴄʜɴᴀʏᴀ ᴛsᴇʟь ɪ ʏᴀ ᴢɴᴀʏᴜ ᴋᴀᴋᴀʏᴀ ʙʏᴛь sᴀᴍᴏᴊ ᴠᴇʀɴᴏᴊ ᴍᴏᴇɢᴏ ʜᴜʏᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ʀᴀsᴋᴏʀᴍɪʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ᴄʜᴛᴏ ᴏɴᴀ ᴛᴇᴘᴇʀь ʏᴀᴠʟʏᴀᴛьsʏᴀ ᴍᴇsᴛɴʏᴍ ʙᴏssᴏᴍ ɪ ᴇᴅɪɴsᴛᴠᴇɴʏᴍ ᴋᴛᴏ ᴇё ᴍᴏᴢʜᴇᴛ ᴋʀʏsʜᴏᴠᴀᴛь ᴇё ɴᴀ ᴅᴀɴɴʏᴊ ᴍᴏᴍᴇɴᴛ ᴇᴛᴏ ᴍᴊ ʜᴜᴊ ᴠᴇᴅь ᴏɴᴀ ᴠsᴇɢᴅᴀ sᴛᴀᴠɪʟ ᴢᴀ ɴᴇɢᴏ sᴠᴇᴄʜᴋɪ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴋᴏᴍᴜ ɴᴇ sᴋᴀᴢʜᴜ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴢʜᴇ ɴᴀʏᴀʀɪᴠᴀᴇᴛ ᴍᴏᴊ ʜᴜᴊ ᴘᴏ 100 ʀᴀᴢᴜ ᴠᴇᴅь ᴏɴᴀ ᴇᴛᴏ ᴅᴇʟᴀᴇᴛ s ᴄʜɪsᴛᴏᴊ sᴏᴠᴇsᴛьʏᴜ ɪ ᴅᴜᴍᴀᴇᴛ ᴄʜᴛᴏ ᴇsʟɪ sᴏsᴀᴛь ᴍᴏᴊ ʜᴜᴊ ᴛᴀᴋ ᴄʜᴀsᴛᴏ ᴏɴᴀ ᴘᴏᴘᴀᴅёᴛ ᴠ ʀᴀᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴛᴀᴋᴀʏᴀ ʙᴇsᴘᴏɴᴛᴏᴠᴀʏᴀ ᴄʜᴛᴏ ᴘʀᴇᴢʜᴅᴇ ᴄʜᴇᴍ ᴇё ᴠʏᴇʙᴀᴛь ʏᴀ ᴅᴀʏᴜ ɴᴀ ʀᴏᴛᴀɴ ᴛᴠᴏᴇᴍᴜ ᴏᴛᴛsᴜ ᴠᴇᴅь ᴛᴀᴋ ᴍᴏᴊ ʜᴜᴊ ᴜᴢʜᴇ ɢᴏᴛᴏᴠ ᴋ sᴛʀёᴍɴᴏᴊ ɢʟᴏᴛᴋᴇ ᴛᴠᴏᴇᴊ ᴇʙᴜᴄʜᴇᴊ ᴍᴀᴛᴜʜᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘᴏᴍɪɴᴋɪ sᴠᴏɪᴍ ʜᴜёᴍ ᴏʀɢᴀɴɪᴢᴏᴠᴀʟ ɪ ᴠsᴇ ʀᴏᴅsᴛᴠᴇɴɪᴋɪ ʙʏʟɪ ʀᴀᴅʏ ᴠᴇᴅь ᴍᴏᴊ ʜᴜᴊ ᴇᴛᴏ sᴀᴍʏᴊ ᴘᴏᴄʜёᴛɴʏᴊ ɢᴏsᴛь ɴᴀ ɪʜ ᴘᴏᴍɪɴᴋᴀʜ ᴇᴢ ᴇᴢ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴘᴏsʟᴇ ᴛᴏɢᴏ ᴋᴀᴋ ᴛᴠᴏʏᴀ ᴍᴀᴛь ʀᴇsʜɪʟᴀ ᴢᴀʀᴇᴊᴅɪᴛь ᴍᴏᴊ ʜᴜᴊ ʏᴀ ᴏᴛʙɪʟ ᴇё ʀᴇᴊᴅ ɴᴏ ʀᴇsʜɪʟ ɴᴀᴋᴀᴢᴛь ᴢᴀ sᴛᴏʟь ɴɪᴢᴋᴏᴇ ᴅɪʏᴀɴɪʏᴀ ᴛᴇᴘᴇʀь ᴏɴᴀ ʟɪᴢʜᴇᴛ ᴍᴏᴇᴍᴜ ᴋᴇɴᴛᴜ ᴘʏᴀᴛᴋɪ ᴏʀᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴘᴀʟᴜʙᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ɴᴇ ᴏᴅɪɴ ᴍᴏʀʏᴀᴋ ᴀ ᴠsё ᴘᴏᴛᴏᴍᴜ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇ ᴍᴏᴢʜᴇᴛ ᴢʜɪᴛь ʙᴇᴢ ᴄʜᴜᴢʜɪᴠ ʜᴜёᴠ ɪ ᴅᴀᴢʜ ʙᴜᴅᴜᴄʜɪ ᴠ ᴢᴀᴘᴇʀᴛɪ ᴏɴᴀ ɴᴀᴊᴅёᴛ ᴋᴀᴋᴏᴊ ɴɪʙᴜᴅь ʜᴜᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴍᴏɢᴜ ᴘᴏᴠᴇʀɪᴛь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴛᴀᴋ ᴘʀᴏsᴛᴏ ᴘᴏᴅᴛᴀʟᴀsь ɴᴀ ᴘʀᴏᴠᴏᴋᴀᴛsɪʏᴜ ᴋɪɴᴜᴛᴜʏᴜ ᴍᴏɪᴍ ʜᴜёᴍ ᴄʜᴛᴏ ᴛᴇᴘᴇʀь ᴅᴇʟᴀᴛь ᴅᴀᴠᴀᴊ ᴘᴏ ɴᴀᴋᴀᴛᴀɴᴏᴊ ᴘʀᴏsᴛᴏ ʀᴀᴢᴏʀᴠёᴍ ᴇᴊ ᴘᴇʀᴅᴀᴋ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴀ ᴅᴀᴢʜᴇ ʀᴀᴜɴᴅᴀ ᴘʀᴏᴛɪᴠ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ɴᴇ ᴠʏsᴛᴏʏᴀʟᴀ ᴄʜᴛᴏ ᴛᴇᴘᴇʀь ɢᴠᴏᴏʀɪᴛь ᴏ ᴘᴏʟɴᴏᴛsᴇɴᴏᴍ ʙᴏᴇ ᴘᴜsᴛь ᴛʀᴇɴɪʀᴜᴇᴛьsʏᴀ ᴀ ᴘᴏᴋᴀ ᴏɴᴀ ᴇᴛᴏ ᴅᴇʟᴀᴛь ᴅᴀᴠᴀᴊ sᴏsɪ ʀᴀᴋᴀʟ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴛᴀʀᴢᴀɴᴋᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴋᴏɢᴅᴀ ᴏɴᴀ ᴘʏᴛᴀʟᴀsь sᴘʀʏɢɴᴜᴛь s ɴᴇё ʏᴀ ᴘᴏᴅʜᴠᴀᴛɪʟ ᴇё ʜᴜёᴍ ɪ ᴜᴇʙᴀʟ ᴏʙ ᴢᴇᴍʟʏᴜ ᴘᴜsᴛь ᴛᴏʟьᴋᴏ ᴇsᴄʜё ʀᴀᴢ ᴘᴏᴘʀᴏʙᴜᴇᴛ ᴠʏᴋɪɴᴜᴛь ᴄʜᴛᴏ ɴɪʙᴜᴅь ᴛᴀᴋᴏᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴍᴏɢᴜ ɴᴇ ᴄʜᴇɢᴏ sᴋᴀᴢᴀᴛь ᴘʟᴏʜᴏɢᴏ ɴᴀsᴄʜёᴛ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴜʟьᴋᴇ ɴᴏ ᴘʀɪᴅёᴛьsʏᴀ ʀᴀsᴋʀʏᴛь ᴛᴇʙᴇ ᴛᴀᴊɴᴜ ᴏᴛsᴏs ᴛʏ ᴍᴇʀᴢᴋɪᴊ ᴄʜᴛᴏ ᴏɴᴀ ʀᴀᴅɪ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ᴛᴠᴏᴊ ᴋᴏᴍᴘ ᴢᴀʟᴏᴢʜɪʟᴀ ᴏʀᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ sᴋᴀᴄʜᴋᴀʜ ᴠsᴇ ʙʏʟɪ ɴᴀ ᴋᴏɴʏᴀʜ ᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴇᴅɪɴsᴛᴠᴇɴᴀʏᴀ ᴜᴄʜᴀsᴛɴɪᴛsᴀ ᴋᴏᴛᴏʀᴀʏᴀ ʀᴇsʜɪʟᴀ ᴘʀᴏsᴋᴀᴛᴀᴛь ɴᴀ ᴍᴏёᴍ ʜᴜᴇ ɴᴇ ᴄʜё ᴛᴀᴋ ᴘᴏʟᴜᴄʜɪʟᴏsь ᴋsᴛᴀᴛɪ ᴍᴏᴊ ʜᴜᴊ ᴠᴢʏᴀʟ ᴛᴀᴍ ᴘᴇʀᴠᴏᴇ ᴍᴇsᴛᴏ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴋᴀᴢʜᴅʏᴊ ᴅᴇɴь ʜᴜёᴍ ᴠ ᴍᴀɢᴀᴢ ɢᴏɴʏᴀʏᴜ ᴠᴇᴅь ʏᴀ ᴛᴀᴋ ᴢᴀᴇʙᴀʟsʏᴀ ᴇᴊ ɴᴀ ʀᴏᴛᴀɴ ᴅᴏᴠᴀᴛь ᴄʜᴛᴏ ᴛᴇᴘᴇʀь ᴍᴏё ʀᴀᴢᴠʟᴇᴄʜᴇɴɪʏᴀ ᴇᴛᴏ ᴅᴇʟᴀᴛь ɪᴢ ɴᴇё sᴀᴍᴜʏᴜ ᴘᴏsʟᴜsʜɴᴜʏᴜ sʜʟʏᴜʜᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍᴏᴢʜᴇsʜь ɴᴇ ᴠᴇʀɪᴛь ɴᴏ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴇʀᴇʙᴀʟᴀ ᴘᴏʟ ɢᴏʀᴏᴅᴀ ɴᴏ ʏᴀ ᴇᴅɪɴsᴛᴠᴇɴʏᴊ ᴢᴀ ᴄʜᴇᴊ ʜᴜᴊ ᴏɴᴀ ʙᴜᴅᴇᴛ sᴛᴏʏᴀᴛь ᴅᴏ ᴋᴏɴᴛsᴀ ɪ ɴᴇ ᴋᴏɢᴅᴀ ɴᴇ sᴅᴀsᴛ ᴢᴀᴅɴɪʏᴜ ʀɪʟɪ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴍᴏᴊ ʜᴜᴊ ᴍᴇsᴛᴏ ᴍᴀsᴏᴢʜᴏʀᴀ ʀᴇsʜɪʟᴀ ɪsᴘᴏʟьᴢʏᴠᴀᴛь ɴᴏ ʏᴀ ɴᴇ ᴢɴᴀʏᴜ ᴇsᴛь ʟɪ ᴍᴀsᴀᴢʜᴏʀ ᴘɪᴢᴅʏ ᴠᴇᴅь ᴇᴅɪɴsᴛᴠᴇɴɴᴏᴇ ᴄʜᴛᴏ ᴏɴᴀ ᴅᴇʟᴀᴇᴛ ᴇᴛᴏ sᴜёᴛ ᴇɢᴏ ᴠ sᴠᴏё ɢɴᴇᴢᴅᴏ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴅᴀᴢʜᴇ ɴᴀ ʀᴀʙᴏᴛᴇ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴋᴏɢᴅᴀ ᴠsᴇ ᴅᴇʟᴀʏᴜᴛ ᴘʟᴀɴᴏᴠʏᴊ ᴏᴄʜёᴛ ɪʟɪ ᴠʏʜᴏᴅʏᴀᴛ ᴘᴏᴋᴜʀɪᴛь ᴏɴᴀ ᴍɴᴇ ᴘᴏ sᴋᴀᴊᴘᴜ sᴏsёᴛ ᴇsʟɪ ʙʏʟᴏ ʙʏ ᴠᴏᴢᴍᴏᴢʜɴᴏ ɴᴇ ᴘʟᴀᴛɪᴛь ᴢᴀ ᴍᴏᴊ ʜᴜᴊ ᴏɴᴀ ʙʏ ɴᴇ ʀᴀʙᴏᴛᴀʟᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴛᴇʀᴇᴏᴛɪᴘɴᴏᴇ ᴍʏsʜʟᴇɴɪʏᴀ ᴏɴᴀ ᴅᴜᴍᴀᴇᴛ ᴄʜᴛᴏ ᴇsʟɪ ʏᴀ ᴇᴊ ɴᴇ ɴᴀᴠᴇʀɴᴜʟ ᴘᴏ ɢᴏʀʙᴜ ᴢᴀ ᴘʟᴏʜᴏᴊ ᴍɪɴьᴇᴛ ᴛᴏ ʙᴏʟьsʜᴇ ᴛᴀᴋ ᴅᴇʟᴀᴛь ɪ ɴᴇ ʙᴜᴅᴜ ᴋᴀᴋ ɴᴀ ᴏsʜɪʙᴀᴇᴛьsʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ʟɪɴɪʏᴜ ᴢʜɪᴢɴɪ ʜᴜёᴍ ᴏʙᴏʀᴠᴀʟ ᴛᴇᴘᴇʀь ᴇᴊ ᴘʀɪᴅёᴛьsʏᴀ ᴏᴛᴘʀᴀᴠʟʏᴀᴛьsʏᴀ ᴠ ᴍɪʀ ɪɴᴏᴊ ɴᴀ ᴢɴᴀʏᴀ ᴋᴀᴋᴀʏᴀ ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴀ sʜʟʏᴜʜᴀ ᴏɴᴀ ᴅᴀᴢʜᴇ ᴛᴀᴍ ᴘᴏᴘʀᴏsɪᴛ ᴍᴏᴊ ʜᴜᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍᴏᴊ ʜᴜᴊ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴢʜᴇ ɴᴀ ᴠᴇʀʜᴋᴜsʜᴋᴜ ᴢᴀᴋɪɴᴜʟ ᴛᴇᴘᴇʀь ᴏɴᴀ ᴏʙsᴄʜᴀᴇᴛьsʏᴀ s ɪɴᴛᴇʟᴇɢᴇɴᴛɴʏᴍɪ ʟʏᴜᴅьᴍɪ ɴᴏ ᴍʏ ᴛᴏ ᴠsᴇ ᴢɴᴀᴇᴍ ᴋᴀᴋ ᴍʏ s ᴘᴀᴛsᴀɴᴀᴍɪ ᴇё ʀᴏᴛᴀɴ ᴘᴏ ᴋʀᴜɢᴜ ᴘᴜsᴋᴀʟɪ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴏᴛʀɪᴛsᴀᴊ ᴛᴏɢᴏ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴅᴀʟᴀsь ᴍᴏᴇᴍᴜ ʜᴜʏᴜ ᴏɴᴀ ᴘʏᴛᴀʟᴀsь sᴏᴘʀᴏᴛɪᴠʟʏᴀᴛьsʏᴀ ɴᴏ ᴍᴏᴊ ʜᴜᴊ ᴏᴋᴀᴢᴀʟsʏᴀ sɪʟьɴᴇᴇ ᴅᴀᴢʜᴇ ᴛᴠᴏᴊ ᴏᴘᴜsᴄʜᴇɴʏᴊ ᴏᴛᴇᴛs s ɴɪᴍ ɴᴇ sᴍᴏɢ sᴘʀᴀᴠɪᴛьsʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍᴏᴢʜᴇᴛ ᴛʏ ᴍɴᴇ sᴋᴀᴢʜᴇsʜь ᴘᴏᴄʜᴇᴍᴜ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴇʙᴜᴄʜᴀʏᴀ ᴍᴏʟᴇᴋᴜʟᴀ ᴏᴘʏᴀᴛь ʀᴇsʜɪʟᴀ ᴠʏᴠᴇsɪᴛь ɴᴀ sᴛᴇɴᴅ ᴍᴏᴊ ʜᴜᴊ ᴏɴᴀ ᴜᴢʜᴇ ᴘʀᴏᴅᴀʟᴀsь ᴇᴍᴜ ᴘᴏʟɴᴏsᴛьʏᴜ ʀɪʟɪ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴢᴀʙʏᴠᴀᴊ ᴋᴛᴏ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ᴜᴇʙᴀʟ ɪ ᴠsё ᴇᴛᴏ ʙʏʟᴏ ᴠᴏ ʙʟᴀɢᴏ ᴠᴇᴅь ᴛᴇᴘᴇʀь ᴏɴᴀ sᴛᴀʟᴀ ᴜᴍɴᴇᴇ ɪ ᴍᴇsᴛᴏ ᴏᴛsᴏsᴀ ᴛᴠᴏᴇᴍᴜ ʙᴀᴛɪ ᴛᴇᴘᴇʀь ᴏɴᴀ ᴅᴇʟᴀᴇᴛ ᴇɢᴏ ᴍɴᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍᴏᴢʜᴇᴛ ᴛʏ sᴄʜᴀs ᴜᴘᴀᴅёsʜь ɴᴀ ᴋᴏʟᴇɴɪ ɪ ɴᴀᴄʜɴёsʜь ᴍɴᴇ sᴏsᴀᴛь ᴀ ᴛᴏ ʏᴀ ᴘᴏᴢᴏᴠᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ɪ ᴏɴᴀ ᴜᴢʜᴇ ɴᴇ sᴍᴏᴢʜᴇᴛ ᴏᴛᴏʀᴠᴀᴛьsʏᴀ ᴏᴛ ᴍᴏᴇɢᴏ ʜᴜʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ᴢʜᴇ ʜᴜёᴍ ᴛᴠᴏᴊ ᴘɪᴢᴅᴀᴋ ᴘᴏᴅᴠᴇsɪʟ ɴᴀ ʟʏᴜsᴛʀᴜ ᴛᴇᴘᴇʀь ᴛᴠᴏᴊ ʙᴀᴛʏᴀ ᴋᴏɢᴅᴀ ᴘʀᴏʜᴏᴅɪᴛ ʀᴀᴅᴜᴇᴛьsʏᴀ ᴄʜᴛᴏ ᴛᴇʙʏᴀ ᴠʏᴇʙᴀʟ ɴᴇ ᴋᴀᴋᴏᴊ ᴛᴏ ᴅᴏᴠʀᴏᴠʏᴊ ᴘᴀᴛsᴀɴ ᴀ ʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍᴏᴢʜᴇᴛ ᴛʏ ᴍᴏᴊ ʜᴜᴊ sʙᴀʟᴀɴsɪʀᴏᴠᴀɴɴᴏ ɴᴀᴄʜɴёsʜь sᴏsᴀᴛь ᴀ ᴛᴏ ᴄʜё ᴛʏ ᴋᴀᴋ ʟᴀʜ ᴢᴀ ᴏᴅɴᴜ sᴄʜёᴋᴜ ᴘᴜsᴋᴀᴇsʜь ᴅᴀᴠᴀᴊ ᴘʀᴇsᴛᴜᴘᴀᴊ ɪʟɪ ᴏᴘʏᴀᴛь ᴛᴠᴏᴊ ʙᴀᴛʏᴀ ᴘʀɪᴅёᴛ ɪ ᴏᴛsᴏsёᴛ ᴍɴᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏᴊ ʙᴀᴛʏᴀ ɴᴜʟёᴠᴋᴀ ɴᴇ ᴄʜᴇɢᴏ ɴᴇ ᴍᴏᴢʜᴇᴛ ʙᴇᴢ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ᴠᴇᴅь ᴏɴ ɢᴏᴠᴏʀɪᴛ ᴄʜᴛᴏ ᴇᴛᴏ ᴇɢᴏ sᴠᴇᴛʟʏᴊ ʟᴜᴄʜɪᴋ ᴠ ʙᴜsᴄʜᴜᴇᴇ ᴠᴏᴛ ᴇᴛᴏ ʏᴀ ᴇᴍᴜ ʜᴜёᴍ ᴍᴏᴢɢɪ ᴏᴛʙɪʟ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴠᴇʀь sᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴋᴏɢᴅᴀ ᴏɴᴀ ɢᴏᴠᴏʀɪᴛ ᴄʜᴛᴏ ʏᴀ ᴛᴇʙʏᴀ ɴᴇ ʀᴀᴢᴜ ɴᴇ ᴇʙᴀʟ ʏᴀ ᴛʏᴀ ᴇsᴄʜё s ʀᴏᴢʜᴅᴇɴɪʏᴀ ᴇʙᴀʟ ᴋʀᴇᴠᴇᴛᴋᴀ ᴇʙᴜᴄʜᴀʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴇsᴄʜё ᴏᴅɴᴏ sʟᴏᴠᴏ ᴘʀᴏ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʏᴀ ᴛᴇʙʏᴀ ʜᴜёᴍ ʀᴀsᴛᴇʀᴢᴀʏᴜ ᴅᴜʀᴀ ᴛʏ ᴇʙᴀɴᴀʏᴀ ᴠᴇᴅь ᴛᴠᴏʏᴀ ᴍᴀᴛь ɪᴅᴇᴀʟьɴᴀʏᴀ sʜᴀʟᴏᴠᴀ ɴᴇ ᴏʙɪᴢʜᴀᴊ ᴇё <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛʏ ᴢɴᴀʟ ᴄʜᴛᴏ ʏᴀ ᴛʏᴀ ʜᴜёᴍ ᴋʀᴇsᴛɪʟ ᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴍᴜᴅʀɪʟᴀsь ᴅᴀᴢʜᴇ ᴠ ᴛᴀᴋᴏᴊ ᴏᴛᴠᴇᴛsᴛᴠᴇɴʏᴊ ᴍᴏᴍᴇɴᴛ ᴏᴛsᴏsᴀᴛь sᴠʏᴀsᴄʜᴇɴɪᴋᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ᴛᴇʙʏᴀ ᴅᴀᴢʜᴇ ᴠ ᴅᴇᴛsᴋᴏᴍ sᴀᴅᴜ ᴇʙᴀʟ ᴋᴏɢᴅᴀ ᴛʏ ᴅʀᴀʟsʏᴀ ᴢᴀ ᴍᴀsʜɪɴᴋᴇ ɪ ᴘʟᴀᴋᴀʟ ᴄʜᴛᴏ ᴛᴇʙʏᴀ ɴᴇ ᴅᴀʟɪ ᴍᴀsʜɪɴᴋᴜ ᴋᴛᴏ ᴛᴇ ʜᴜᴊ ᴏᴛ ᴏʙɪᴅʏ sᴜᴠᴀʟ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛʏ sᴛᴀʟ ᴘᴏʜᴏᴢʜɪᴍ ɴᴀ sᴠᴏʏᴜ ᴍᴀᴛь ᴛᴇʙᴇ ᴜᴢʜᴇ ᴛᴏᴢʜᴇ ɴᴇ ɴᴜᴢʜɴᴀ ᴘʀɪᴄʜɪɴᴀ ᴄʜᴛᴏʙʏ ᴏᴛsᴏsᴀᴛь ᴍɴᴇ ʜᴜᴊ ɴᴜ ᴇsʟɪ ᴛᴀᴋ ᴛᴏ ᴛʏ ᴛᴏᴢʜᴇ ᴅᴏsᴛᴏᴇɴ ᴢᴠᴀɴɪʏᴀ ᴘᴅᴢᴏʙᴏʀɴᴏᴊ sʜʟʏᴜʜɪ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴍᴏɢᴜ ᴘᴏᴠᴇʀɪᴛь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴏᴘʏᴀᴛь ᴠᴢʏᴀʟᴀsь ᴢᴀ sᴛᴀʀᴏᴇ ɪ ᴘʏᴛᴀᴇᴛьsʏᴀ ᴠʏsʟᴇᴅɪᴛь ᴍᴏᴊ ʜᴜᴊ ɴᴜ ᴇsʟɪ ᴏɴᴀ ᴘᴏᴘᴀᴅёᴛьsʏᴀ ᴍɴᴇ ɴᴀ ɢʟᴀᴢᴀ ʏᴀ ᴇё ʜᴜёᴍ ᴠ ᴀʀᴀʜɴɢᴇʟьsᴋ sʜᴠʏʀɴᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴅᴜᴍᴀᴊ ɴᴇ ᴄʜᴇɢᴏ ᴘʟᴏʜᴏɢᴏ ɴᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴋᴏsᴍᴏɴᴀᴠᴛ ʏᴀ ᴛᴇʙᴇ ɴᴇ ᴠʀᴜ ɴᴇ ᴠ ᴋᴏᴇᴍ sʟᴜᴄʜᴀᴇ ᴀ ᴢɴᴀᴇsʜь ɴᴀ ᴄʜёᴍ ᴘʀᴏʜᴏᴅɪʟ ᴇё ᴘᴇʀᴠʏᴊ ᴘᴏʟёᴛ ɴᴀ ᴍᴏёᴍ ʜᴜᴇ ᴏʀᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍᴏᴢʜᴇᴛ ʏᴀ ᴛᴇʙʏᴀ ᴏɢᴏʀᴄʜᴜ ɴᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛᴜsʜᴋᴀ sᴄʜᴀ ᴍɴᴇ ʜᴜᴊ sᴏsёᴛ ɪ ᴄʜᴛᴏ ᴛᴏ ʙᴏʀᴍᴏᴄʜᴇᴛ ᴇᴛᴏ sʜᴀʟᴏᴠᴀ ᴍᴇɴʏᴀ ᴛᴀᴋ ᴢᴀᴇʙᴀʟᴀ ʏᴀ sᴄʜᴀ ᴠsᴘᴏʀʏᴜ ᴇё ʜᴜёᴍ ᴘʀɪʜᴏᴅɪ ɪ ᴢᴀʙɪʀᴀᴊ ᴇё <emoji document_id=5438153647345119196>💀</emoji>',
'ᴠsё ɴᴇ ᴛᴀᴋ ᴘʀᴏsᴛᴏ ᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴇsᴛь sᴛɪᴍᴜʟ sᴏsᴀᴛь ᴍɴᴇ ʜᴜᴊ ᴠᴇᴅь ʏᴀ sᴋᴀᴢᴀʟ ᴇsʟɪ ᴏɴᴀ ᴏsᴛᴀɴᴏᴠɪᴛьsʏᴀ ᴛᴏ ᴛᴠᴏᴊ ɢʀʏᴀᴢɴʏᴊ ʙᴀᴛʏᴀ ᴜᴍʀёᴛ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀ ᴍᴏёᴍ ʜᴜᴇ ʜɪᴘ ʜᴏᴘ ᴛᴀɴᴛsᴇᴠᴀʟᴀ ɪ sᴜᴅьʏᴀ ᴅᴀʟɪ ᴇᴊ ᴘᴇʀᴠᴏᴇ ᴍᴇsᴛᴏ ɴᴏ ɴᴇ ᴢᴀ ᴇᴛᴏ ᴀ ᴢᴀ ᴠᴇʟɪᴋᴏʟᴇᴘɴʏᴊ ᴏᴛsᴏs ᴠ ᴋᴏɴᴛsᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ʜᴏᴄʜᴇsʜь sᴘᴀsᴛɪ sᴠᴏʏᴜ ᴍᴀᴛь ɪᴢ ʀᴀʙsᴛᴀᴠᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ᴘʀɪɴᴇsɪ ᴇᴍᴜ ᴘᴏᴅɴᴏsʜᴇɴɪʏᴀ ᴛᴏɢᴅᴀ ᴍᴏᴢʜᴇᴛ ʙʏᴛь ᴍᴏᴊ ʜᴜᴊ ᴘʀᴏsᴛɪᴛ ᴛᴠᴏʏᴜ ᴍᴀᴛᴜʜᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴢʜᴇ ᴏᴛᴢʜɪʟᴀ sᴠᴏё ɴᴀ ᴍᴏёᴍ ʜᴜʏᴜ ᴋᴀᴋ ɪ ᴛᴠᴏᴊ ᴏᴛᴇᴛs ᴘʀɪsʜʟᴏ ᴛᴠᴏё ᴠʀᴇᴍʏᴀ ᴘʀʏɢᴀᴊ ɴᴀ ʜᴜᴊ ɪ ᴘᴏᴇʜᴀʟɪ ᴅᴜʀᴇɴь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴍᴇsᴛᴏ ᴛᴀʙʟᴇᴛᴏᴋ ᴏᴛ ɢᴏʟᴏᴠʏ ɢʟᴏᴛᴀᴇᴛ ᴍᴏᴊ ʜᴜᴊ sᴋᴀᴢʜᴇsʜь ᴄʜᴇᴍ ᴇᴛᴏ ᴘᴏᴍᴏᴢʜᴇᴛ sᴘʀᴏsɪ ᴜ ᴇᴛᴏᴊ ᴇʙᴜʏᴀᴇᴊ ᴅᴜʀʏ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴘʏᴛᴀʟᴀsь ᴠʏᴠᴇᴢᴛɪ ᴍᴏᴊ ʜᴜᴊ ᴘᴏ ᴘᴏɴʏᴀᴛɪʏᴀᴍ ᴄʜᴛᴏʙʏ ᴏɴ ʙᴏʟьsʜᴇ ᴇё ɴᴇ ᴛʀᴏɢᴀʟ ɴᴏ ᴍᴏᴊ ʜᴜᴊ ɴᴇ sᴛᴀʟ ᴇё sʟᴜsʜᴀᴛь ɪ ʀᴀsёᴋ ᴇᴊ ʙʀᴏᴠь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍᴏᴢʜᴇᴛ ᴛʏ ʙᴜᴅᴇsʜь ᴅᴜᴍᴀᴛь ᴄʜᴛᴏ ʏᴀ ᴘʟᴏʜᴏᴊ ɴᴏ ʏᴀ ᴅᴏᴋᴀᴢʜᴜ ᴏʙʀᴀᴛɴᴏᴇ ᴇsʟɪ ʙʏ ʏᴀ ɴᴇ ᴇʙᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇё ʙʏ ᴇʙᴀʟ ᴠᴇsь ɢᴏʀᴏᴅ ɪ ᴠsᴇ ʙʏ ᴢɴᴀʟɪ ᴄʜᴛᴏ ᴏɴᴀ sʜᴀʟᴏᴠᴀ ᴀ ᴛᴀᴋ ᴢɴᴀᴇᴍ ᴛᴏʟьᴋᴏ ᴍʏ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍᴏɢᴜ ᴏʙʀᴀᴛɪᴛьsʏᴀ s ᴘʀᴏsьʙᴏᴊ ᴋ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴛʏ sᴘʀᴏsɪsʜь ᴋᴀᴋᴏᴊ ɴᴜ ᴛʏ ᴄʜё ʟᴀʜ ɴᴇ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏʙʏ ᴏɴᴀ ᴏᴛsᴀsᴀʟᴀ ᴍɴᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴋᴀᴋᴏᴊ ᴇʙᴀʟ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴋᴏɢᴅᴀ ᴜ ᴍᴇɴʏᴀ ʙʏʟᴀ ᴛᴇᴍᴘᴇʀᴀᴛᴜʀᴀ ʀᴏᴛ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴢᴀᴍᴇɴʏᴀʟ ᴍɴᴇ ɢʀᴀᴅᴜsɴɪᴋ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ sᴘɪɴᴇ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀᴋᴏʟᴏʟᴀ ᴍᴏᴊ ʜᴜᴊ ɪ ᴛᴇᴘᴇʀь ʜᴠᴀsᴛᴀᴇᴛьsʏᴀ ᴠsᴇᴍ ᴄʜᴛᴏ ᴜ ɴɪʜ ɴᴇᴛ ʙᴏʟᴇᴇ ᴏʜᴜᴇɴᴇᴇ ᴛᴀᴛᴜɪʀᴏᴠᴋᴏᴊ ᴄʜᴇᴍ ᴜ ɴᴇё <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴠ ᴢɪᴍᴜ ᴇʙᴀʟ ᴛᴏɢᴅᴀ ᴋᴀᴋ ʀᴀᴢ ʙʏʟ ᴢʜᴇsᴛᴏᴋᴀʏᴀ ᴢɪᴍᴀ ɪ ᴍɴᴇ ᴘʀɪsʜʟᴏsь ᴇʙᴀᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴄʜᴛᴏʙʏ sᴏɢʀᴇᴛьsʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴍᴀsʜɪɴᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴠsᴇ sᴋᴀᴢʜᴜᴛ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴇʙᴜᴄʜᴀʏᴀ sʜᴀʟᴏᴠᴀ ᴋᴏᴛᴏʀᴀʏᴀ ᴠᴇᴅᴇᴛьsʏᴀ ɴᴀ ᴛᴀᴄʜᴋɪ ɴᴏ ᴏɴɪ ᴏsʜɪʙᴀʏᴜᴛьsʏᴀ ᴏɴᴀ ᴠᴇᴅёᴛьsʏᴀ ɴᴀ ᴍᴏᴊ ʜᴜᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴠɪʟᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ɪ ᴍᴏᴢʜɴᴏ sᴋᴀᴢᴀᴛь ᴄʜᴛᴏ ᴍʏ ᴠᴏʀᴠᴀʟɪsь ᴛᴜᴅᴀ ɴᴇ ᴢᴀᴋᴏɴɴᴏ ᴀ ᴢɴᴀᴇsʜь ᴘᴏᴄʜᴇᴍᴜ ᴘᴏᴛᴏᴍᴜ ᴄʜᴛᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴢᴀʜᴏᴛᴇʟᴏsь ᴘᴏsᴏsᴀᴛь ᴍᴏᴊ ʜᴜᴊ ᴇᴋsᴛʀᴇᴍᴀʟьɴᴏ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴢɴᴀᴇsʜь ᴘᴏᴄʜᴇᴍᴜ ᴍᴇɴʏᴀ ᴠsᴇ ᴘᴀᴛsᴀɴʏ ɴᴀᴢʏᴠᴀʟɪ ʜᴜʟɪɢᴀɴᴏᴍ ᴘᴏᴛᴏᴍᴜ ᴄʜᴛᴏ ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛᴜʜᴀ ᴘᴏsʟᴇ 8 ᴇʙᴀʟ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍʏ ʟʏᴜʙɪʟɪ sᴏʙɪʀᴀᴛьsʏᴀ s ᴘᴀᴛsᴀɴᴀᴍɪ ɪ ɢᴏᴠᴏʀɪᴛь ᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ɴᴏ ʀᴀᴢɢᴏᴠᴏʀ ᴏʙʏᴄʜɴᴏ ᴢᴀᴋᴀɴᴄʜɪᴠᴀʟsʏᴀ ᴏᴅɴɪᴍ ᴍʏ ᴢᴠᴏɴɪʟɪ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴄʜᴛᴏʙʏ ᴏɴᴀ ᴏᴛsᴀsᴀʟᴀ ɴᴀᴍ ʜᴜᴊ ɴᴇ ʀᴀᴢᴜ ɴᴇ ᴏᴛᴋᴀᴢʏᴠᴀʟᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴠ ᴍᴜsᴏʀsᴋᴏᴍ ᴜᴄʜᴀsᴛᴋᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ᴋᴏɢᴅᴀ ᴇё ᴢᴀᴋʀʏʟɪ ᴢᴀ ᴅᴇʀᴢᴋᴏᴇ sᴏsᴀɴɪʏᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ʏᴀ ᴘʀᴏʙʀᴀʟsʏᴀ ᴛᴜᴅᴀ ɪ ᴠʏᴇʙᴀʟ ᴇё ᴘʀᴀᴠɪʟьɴᴏ ᴢʜᴇ ʜᴇʜ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴅᴇɴь ᴏᴛᴋʀʏᴛʏʜ ᴅᴠᴇʀᴇᴊ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ᴋᴏɢᴅᴀ ᴠsᴇ sᴏʙɪʀᴀʟɪsь ɪ ʙʏʟɪ sᴏsʀᴇɢᴏᴛᴏᴄʜᴇɴʏ ʏᴀ ᴛᴏᴢʜᴇ ʙʏʟ ᴠ sᴠᴏёᴍ ᴘᴏɴɪᴍᴀɴɪʏᴀ ɴᴀᴠᴏsᴛʀёɴ ɴᴏ ʏᴀ ᴇʙᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴢᴀᴘʀᴀᴠᴋᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴏᴋᴀ ᴠsᴇ ᴢᴀᴘʀᴀᴠʟʏᴀʟɪ ᴍᴀsʜɪɴʏ ʏᴀ ᴢᴀᴘʀᴀᴠʟʏᴀʟ sᴘᴇʀᴍᴀᴋᴏᴍ ᴛᴠᴏʏᴜ ᴢʜᴀʟᴋᴜʏᴜ ᴍᴀᴛᴜʜᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴀᴠᴛᴏsᴛᴀɴᴛsɪɪ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴏᴋᴀ ʜᴏᴅɪʟɪ ᴀᴠᴛᴏʙᴜsʏ ᴍᴏᴊ ʜᴜᴊ ᴢᴏᴅɪʟ ᴠɴᴛᴜʀɪ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴜsʜᴋᴇ ᴏʀᴜ ᴅᴜʀᴇɴь <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴍᴏʀᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ɴᴏ ᴛᴀᴍ ᴘᴏᴘʏᴛᴀʟɪsь ᴜ ᴍᴇɴʏᴀ ᴇё sᴘɪᴢᴅᴇᴛь ɴᴏ ᴏɴᴀ ᴠᴇʀɴᴜʟᴀsь ᴢᴀ 1000 ᴋᴍ ᴋᴏ ᴍɴᴇ ᴠᴇᴅь ᴏɴᴀ ᴠᴇʀɴᴀ ᴍᴏᴇᴍᴜ ʜᴜʏᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴋᴀʀɪʙsᴋɪʜ ᴏsᴛʀᴏᴠᴀʜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴏɴᴀ ʀᴇsʜɪʟᴀ sʜɪᴋᴀɴᴜᴛь ɪ ᴘᴏᴇʜᴀʟᴀ ɴᴀ ᴏsᴛʀᴏᴠᴀ ɴᴏ ᴠᴢʏᴀʟᴀ ᴍᴇɴʏᴀ ᴠᴇᴅь ᴋᴛᴏ ᴇᴊ ᴛᴀᴍ ɴᴀ ʀᴏᴛᴀɴ ᴋɪᴅᴀᴛь ʙᴜᴅᴇᴛ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴢᴀᴋᴀᴛᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴠsё ʙʏʟᴏ ᴛᴀᴋ ᴋʀᴀsɪᴠᴏ ᴋʀᴏᴍᴇ ᴇʙᴀʟᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘʀɪsʜʟᴏsь ɴᴀ ᴇᴛᴜ ᴅᴜʀᴜ ᴍᴇsʜᴏᴋ ɴᴀᴅᴇᴠᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴠᴇʀᴛᴏʟёᴛᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴇᴊ ʙʏʟᴏ sᴛʀᴀsʜɴᴏ ʟᴇᴛᴇᴛь ɪ ᴄʜᴛᴏʙʏ ᴜsᴘᴏᴋᴏɪᴛь ᴇё ᴍɴᴇ ᴘʀɪsʜʟᴏsь ᴘᴏʀᴠᴀᴛь ᴇᴊ ᴛᴀᴍ ᴀɴᴀʟ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴠᴇʟɪᴋᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴛʏ ᴢʜᴇ ᴅᴜʀᴇɴь ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɪsᴘᴏʟьᴢʏᴠᴀʟᴀ ᴍᴇsᴛᴏ sᴇᴅᴜsʜᴋᴇ ɴᴀ ᴠᴇʟɪᴋᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ʟᴜɴᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴏᴋᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь ʙʏʟᴀ ᴠ ᴠᴏsᴛᴏʀɢᴇ ᴏᴛ ᴋᴏsᴍᴏsᴀ ʏᴀ ᴇё ᴇʙᴀʟ ʟᴀᴊᴋɴɪ ᴢᴀᴘɪsɪ ᴇsʟɪ ʏᴀ ᴘᴏsᴛᴜᴘɪʟ ᴘʀᴀᴠɪʟьɴᴏ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴘʀᴏᴠᴏᴅᴀʜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴏᴋᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛᴜʜᴀ ᴘʀᴏᴠᴀᴢʜᴀʟᴀ ᴛᴠᴏᴇɢᴏ ʙᴀᴛʏᴜ ᴠ ᴀʀᴍɪʏᴜ ᴏɴᴀ ᴘᴜsᴛɪʟᴀ sʟᴇᴢᴜ ɴᴏ ᴠsᴇ ᴢɴᴀʟɪ ᴋᴛᴏ ʙᴜᴅᴜsᴄʜɪᴊ ɢᴏᴅ ʙᴜᴅᴇᴛ ᴇᴊ ɴᴀ ʀᴏᴛᴀɴ ᴋɪᴅᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴘɪᴛ sᴛᴏᴘᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴋᴏɢᴅᴀ ᴏɴᴀ ᴘʀʏɢᴀʟᴀ ᴠ ᴛᴀᴄʜᴋᴇ ᴋ ᴄʜᴜᴢʜɪᴍ ᴍᴜᴢʜɪᴋᴀᴍ ᴏɴɪ ʀᴀsᴄʜɪᴛʏᴠᴀʟɪ ɴᴀ ᴄʜᴛᴏ ᴛᴏ ɴᴏ ᴘᴏᴛᴏᴍ ᴘᴏɴʏᴀʟɪ ᴄʜᴛᴏ sᴏsёᴛ ᴏɴᴀ ᴛᴏʟьᴋᴏ ᴍɴᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴢᴀᴠᴏᴅᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴏᴋᴀ ᴠsᴇ ᴄʜᴛᴏ ᴛᴏ ᴘʀᴏɪᴢᴠᴏᴅɪʟɪ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴠ ᴛsᴇʜᴇ ᴘᴏ ᴏʙʀᴀʙᴏᴛᴋᴇ ᴍᴏᴊ ʜᴜᴊ ᴏʙʀᴀʙᴀᴛʏᴠᴀʟᴀ ᴏʀᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴠᴏʟɴᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴏᴋᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇ ɴᴀᴜᴄʜɪʟᴀsь ᴇᴢᴅɪᴛь ɴᴀ ᴍᴏёᴍ ʜᴜʏᴜ ᴏɴᴀ ɴᴇ ᴘᴇʀᴇsʜʟᴀ ᴋ sёʀғɴᴏᴊ ᴅᴏsᴋᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴋᴏʀɴᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ sᴍᴇsʜɴᴀʏᴀ ɪsᴛᴏʀɪʏᴀ ᴏɴᴀ ᴋᴏᴘᴀʟᴀsь ᴠ ᴏɢᴏʀᴏᴅᴇ ɪ ᴜᴘᴀʟᴀ ɴᴀ ᴋᴏʀᴇɴь ᴀ ᴅᴀʟьsʜᴇ ʏᴀ ᴇё ᴠʏᴇʙᴀʟ ᴋᴀᴋ ᴢʜᴀʟᴋᴜʏᴜ sᴜᴋᴜ ᴀ ᴛʏ ᴄʜᴇɢᴏ ᴏᴢʜɪᴅᴀʟ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴘᴀsᴋᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ᴠʀᴏᴅᴇ ᴛsᴇʀᴋᴏᴠɴʏᴊ ᴘʀᴀᴢᴅɴɪᴋ ɴᴏ ᴇᴛᴀ sʜʟʏᴜʜᴀ ᴍᴇsᴛᴏ ᴋᴜʟɪᴄʜᴀ ᴍᴏᴊ ʜᴜᴊ ɴᴀᴠᴏʀᴀᴄʜɪᴠᴀʟᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴋʀᴇsᴛɪɴᴀʜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ sʜɪᴋᴀʀɴʏᴊ ᴘʀᴀᴢᴅɴɪᴋ ɴᴏ ᴅᴀᴢʜᴇ ᴛᴀᴍ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴍᴜᴅʀɪʟᴀsь ʀᴀsᴛᴀᴠɪᴛь ᴘᴇʀᴇᴅ ᴍɴᴏᴊ sᴠᴏɪ ɴᴏɢɪ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴋᴀᴘᴄʜᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴍᴇɴʏᴀ ᴘʏᴛᴀʟɪsь ʙʟᴏᴋɴᴜᴛь ᴢᴀ ᴛᴏ ᴄʜᴛᴏ ʏᴀ ɴᴇᴘʀᴀᴠɪʟьɴᴏ ᴠᴏᴅɪʟ ᴘᴀʀᴏʟь ᴘᴏ ᴘɪᴢᴅᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ʀᴜʟᴇᴛᴋᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ᴋᴏɢᴅᴀ ᴜ ᴠsᴇʜ ɪɢʀᴏᴋᴏᴠ ᴋᴏɴᴄʜɪʟɪsь ᴅᴇɴьɢɪ ᴋᴛᴏ ᴛᴏ ᴘᴏsᴛᴀᴠɪʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ɴᴜ ʏᴀ ᴇё ɪ ᴠʏᴇʙᴀʟ ᴘᴏ ᴛɪʜᴏᴍᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴋᴏʀᴀʙʟᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴏᴋᴀ ᴠsᴇ ɴʏᴋᴀʟɪ ᴏᴛ sʜᴛᴏʀᴍᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴘᴇᴛsɪᴀʟьɴᴏ ᴠʏʙᴇɢᴀʟᴀ ɴᴀ ᴘᴀʟᴜʙᴜ ɪ sᴏsᴀʟᴀ ᴍɴᴇ ʜᴜᴊ ᴋᴀᴋ ɴᴇɴᴏʀᴍᴀʟьɴᴀʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ sᴠᴀʟᴋᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴛʏ sᴘʀᴏsɪsʜь ᴋᴀᴋ ʏᴀ ᴛᴜᴅᴀ ᴢᴀsʜёʟ ᴠsё ᴘʀᴏsᴛᴏ ʏᴀ ʜᴏᴛᴇʟ ᴠʏʙʀᴏsɪᴛь ᴍᴜsᴏʀ ᴀ ᴛᴀᴍ ʟᴇᴢʜᴀʟᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇᴘʟᴏʜᴏ ᴛᴏɢᴅᴀ ᴠʏᴇʙᴀʟ ᴇё <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ sᴏʙʀᴀɴɪᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ᴠsᴇ ᴅᴜᴍᴀʟɪ ᴄʜᴛᴏ ᴏɴᴀ ᴘʀɪsʜʟᴀ ʀᴀᴢʙɪʀᴀᴛьsʏᴀ ɴᴏ ᴏɴᴀ ᴠsᴇɢᴏ ʟɪsʜь ʜᴏᴛᴇʟᴀ ᴏᴛsᴏsᴀᴛь ᴍɴᴇ ʜᴜᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴠʀᴀᴛᴀʜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ᴏɴᴀ ᴘʏᴛᴀʟᴀsь ᴠᴏʀᴠᴀᴛьsʏᴀ ᴠ ᴄʜᴜᴢʜᴜʏᴜ ʜᴀᴛᴜ ɪ sʟᴏᴍᴀᴛь ᴠᴏʀᴏᴛᴀ ɴᴏ ᴍᴏᴊ ʜᴜᴊ ᴏᴛᴠᴇʀɢ ᴇё ɪ ᴏɴᴀ ᴏᴛᴏsʜʟᴀ s ᴘᴏʀᴀᴢʜᴇɴɪᴇᴍ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴠᴇsɪʟɪᴛsᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ᴋᴏɢᴅᴀ ᴇᴛᴀ ᴅᴜʀᴀ ᴢᴀʜᴏᴛᴇʟᴀ ᴘᴏᴠᴇsɪᴛьsʏᴀ ᴍᴏᴊ ʜᴜᴊ sᴀᴍ ᴇё ᴘᴏᴅᴠᴇsɪʟ ɴᴏ ᴇᴊ ʙʏʟᴏ ʟᴇɢᴄʜᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴋʀᴀʏᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴜ ɴᴇё ᴘʀᴏsᴛᴏ ɴᴇ ʙʏʟᴏ ᴠʏʜᴏᴅᴀ ᴜʙᴇᴢʜᴀᴛь ᴏᴛ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ᴏʀᴜ ᴏɴᴀ ᴛᴀᴋ ɪ ɴᴇ ᴘᴏɴʏᴀʟᴀ ᴄʜᴛᴏ ᴏᴛ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ɴᴇ ᴏsᴠᴏʙᴏᴅɪᴛьsʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴘᴀʀᴀᴅᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴋᴏɢᴅᴀ ᴠsᴇ ᴋʀᴀsɪᴠᴏ ᴍᴀʀsʜᴇʀᴏᴠᴀʟɪ ʏᴀ ᴋʀᴀsɪᴠᴏ ᴇё ᴇʙᴀʟ ᴀ ᴢɴᴀᴇsʜь ᴋᴀᴋ ʏᴀ ᴇᴛᴏ ᴘᴏɴʏᴀʟ ᴠ ᴋᴏɴᴛsᴇ ᴘᴜsᴋᴀʟɪ sᴀʟʏᴜᴛ ᴠ ᴄʜᴇsᴛь ᴍᴏᴇɢᴏ ᴄʜʟᴇɴᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍᴀᴍᴀ ᴛᴠᴏʏᴀ sʜʟʏᴜʜᴀ ᴍʏ s ɴᴇᴊ ᴢɴᴀᴋᴏᴍʏ ɴᴇ ᴘᴇʀᴠʏᴊ ɢᴏᴅ ᴘʀᴇᴅsᴛᴀᴠь sᴋᴏʟьᴋᴏ ᴏɴᴀ ᴍɴᴇ sᴏsᴇᴛ  ᴜᴢʜᴇ sᴏ sᴄʜᴇᴛᴀ sʙɪʟsʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴋᴀᴋ ᴏsᴛᴀʟьɴʏᴇ ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴏsᴇᴛ ᴏɴᴀ ʟɪᴄʜɴᴏ ᴍᴏʏᴀ ʀᴀʙʏɴ ᴋᴏᴛᴏʀᴀʏᴀ ɴᴇ ᴘʀɪᴅᴀᴇᴛ sᴠᴏʏᴜ ʀᴀʙᴏᴛᴜ ɴᴇ ʙᴜᴅь ᴋᴀᴋ ᴏɴᴀ ᴘᴏsᴏsɪ ᴍɴᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴜ ʙᴜᴅᴇᴍ sᴛᴏʏᴀᴛь ᴢᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴍʏ ᴇᴇ ᴘʀᴏsᴛᴏ ᴏᴛьᴇʙᴇᴍ ᴅᴀᴢʜᴇ ɴᴇ ᴘʟᴀᴄʜь ᴘᴏᴛᴏᴍ ɪ ɴᴇ ʙᴇɢᴀᴊ ᴢᴀ ɴᴀᴍɪ ᴠᴇᴅь ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴘʀᴏᴅᴀᴢʜɴᴀʏᴀ ɪ sᴀᴍᴀ ᴘᴏᴅᴘɪsᴀʟsь ɴᴀ ᴇᴛᴏ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ʀᴀɴьsʜᴇ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴏʀᴍᴀʟьɴᴏ sᴏsᴀʟᴀ ɴᴏ ᴛᴇᴘᴇʀь ᴏɴᴀ ɪᴢʙᴀᴠɪʟᴀsь ᴏᴛ ᴇᴛᴏᴊ ᴘʀɪᴠʏᴄʜᴋɪ ɪ ᴋᴀᴋ sʜᴀʟᴀᴠᴀ ᴛᴜᴛ sᴏsᴇᴛ ᴅᴀᴠᴀᴊ ᴢᴀᴋᴏɴᴄʜɪᴍ s ᴇᴛɪᴍ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ʀᴀɴьsʜᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴠ ᴛʀɪ sᴄʜᴇʟɪ ᴇʙᴀʟɪ ᴛᴇᴘᴇʀь ᴏɴᴀ ʜᴏᴄʜᴇᴛ ʙᴏʟьsʜᴇ ɴᴇ ᴍᴏᴢʜᴇᴍ ᴏᴛᴋᴀᴢᴀᴛь ᴇᴛᴏᴊ sʜᴀʟᴀᴠᴇ ɪ ᴢᴏᴠᴇᴍ ᴛᴏʟᴘʏ ɴᴀ ᴇᴇ ᴘɪᴢᴅᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴢᴀᴋᴏɴᴄʜɪʟɪ s ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀьʏᴜ ᴅᴀᴠᴀᴊ ᴛᴀsᴄʜɪ ᴇᴇ sʏᴜᴅᴀ ɪ ɴᴇ ᴘʀᴏʙᴜᴊ ᴍɴᴇ ᴛᴜᴛ ᴏᴋɪɴᴜᴛьsʏᴀ ᴛᴀᴋ ᴋᴀᴋ ᴛᴠᴏʏᴀ ᴍᴀᴛь sʜʟʏᴜʜᴀ ʀᴀᴢɢᴠᴏʀ s ɴᴇᴊ ᴋᴏʀᴏᴛᴋɪᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴠɴᴀᴛᴜʀᴇ ᴛᴠᴏʏᴜ ᴘᴇᴄʜᴇɴᴋᴜ ᴛᴜᴛ ɴᴀ ʜᴜᴊ ɴᴀᴍᴏᴛᴀʟ ɴᴇ ᴜᴠᴇʀᴇɴɴᴏ ᴍɴᴇ ᴛᴜᴛ sᴏsᴇsʜь ᴅᴜʀᴀᴄʜᴏᴋ ᴏᴘʏᴀᴛь ᴛᴇʙᴇ ɴᴀᴅᴏ ᴘᴇᴄʜᴇɴᴋᴏᴊ ᴘᴏᴢʜᴇʀᴛᴠᴏᴠᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴛʏᴀᴢʜᴇʟʏᴊ ᴇᴛᴏ ᴛʀᴜᴅ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀᴛь ɴᴏ ᴢᴀɴɪᴍᴀᴇᴛ ᴠʀᴇᴍʏᴀ ᴛᴀᴋ ᴋᴀᴋ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇɴᴀsʏᴛɴᴀʏᴀ sʜʟʏᴜʜᴀ ɴᴜ ᴄʜᴛᴏ ᴘᴏᴅᴇʟᴀᴛь ᴍʏ ᴘᴏᴘʀᴏʙᴜᴇᴍ ᴜᴅᴠᴏʟᴇᴛᴠᴏʀɪᴛь ᴇᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴅᴀᴠᴀᴊ ᴢᴀᴠᴏᴅɪ ᴜᴢʜᴇ sᴠᴏʏᴜ ᴍᴀᴛь ᴏɴᴀ ᴏᴘʏᴀᴛь ɴᴀ ᴋᴏʟᴇɴʏᴀʜ ᴘʀɪʙᴇᴢʜɪᴛ ɪ ʙᴜᴅᴇᴛ ᴘʀᴏsɪᴛь ᴘʀᴏsᴄʜᴇɴɪʏᴀ ᴢᴀ ᴛᴇʙʏᴀ ᴛʏ ᴅᴀᴢʜᴇ ɴᴇ ᴍᴏᴢʜᴇsʜь ᴘᴏɴʏᴀᴛь ᴄʜᴛᴏ ᴏɴᴀ ᴅᴀᴠɴᴏ ᴘʀᴏᴅᴀʟᴀsь ᴢᴀ ᴋᴏᴘᴇᴊᴋɪ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍᴀᴍᴜʟьᴋᴜ ᴛᴠᴏʏᴜ ᴠɴᴀᴛᴜʀᴇ ɴᴀ sᴜᴅᴇ ᴘᴏᴅsᴛᴀᴠɪʟ ᴠsᴇ ɢᴏᴠᴏʀɪʟɪ ᴄʜᴛᴏ ᴏɴᴀ ᴘᴏʀʏᴀᴅᴏᴄʜɴᴀʏᴀ ᴢʜᴇɴsᴄʜɪɴᴀ ɴᴏ ʏᴀ ɪᴍ ᴘᴏᴋᴀᴢᴀʟ ᴠɪᴅᴇᴏ ɢᴅᴇ ᴇᴇ ᴛʀᴏᴇ ᴇʙᴀʟɪ ᴠɴᴀᴛᴜʀᴇ ᴏʀɴᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴋᴀᴋ ᴠᴇʀᴛᴏʟᴇᴛ sᴀsᴇsʜь ᴠɴᴀᴛᴜʀᴇ ʏᴀ ᴛᴇʙᴇ ᴘʀᴏᴘᴇʟᴇʀᴏᴍ ᴠɴᴀᴜᴛʀᴇ sᴄʜᴀ ᴀɴᴀʟьɴᴏᴇ ᴏᴛᴠᴇʀsᴛɪᴇ ᴠᴢᴏʀᴠᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍᴀᴛь ᴛᴠᴏʏᴀ ᴘᴏᴅsᴛɪʟᴋᴀ ᴠɴᴀᴛᴜʀᴇ ᴛʏ ᴢɴᴀᴇsʜь ᴄʜᴛᴏ ᴏɴᴀ sᴛᴏʀᴏᴢʜᴜ ᴢᴀ ᴄʜᴇᴋᴜsʜᴋᴜ ᴅᴀʟᴀ ᴢᴀ ᴢᴀʙᴏʀᴏᴍ ᴀ ᴛʏ ᴅᴜᴍᴀʟ ᴘʀɪʟɪᴄʜɴᴀʏᴀ ʜᴇ ʜᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴅᴀᴠᴀᴊ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴇᴍ ᴘʀɪɢʟᴀsʜᴀᴊ ᴇᴇ ɴᴀ ʙᴀʟ ʜᴏᴄʜᴇsʜь ᴘᴏssᴀᴛь ᴠᴍᴇsᴛᴇ s ɴᴇᴊ ᴘʀɪʜᴏᴅɪ ɴᴏ sɴᴀᴄʜᴀʟᴀ ᴘᴏᴛᴀɴᴛsᴜᴇᴍ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ʙᴜᴅь ᴅᴜʀᴀᴋᴏᴍ ᴘᴏᴠᴇʀь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь sʜʟʏᴜʜᴀ ᴠɴᴀᴜʀᴇ ᴛᴜᴛ ᴘᴏɢɪʙɴᴇᴛ ɪʟɪ ᴛʏ ᴅᴜᴍᴀᴇsʜь ᴜ ɴᴇᴇ ʙᴜᴅᴜᴛ sʜᴀɴsʏ ᴠʏᴢʜɪᴛь ʜᴇ ʜᴇ ᴅᴜʀᴀᴋ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏᴇ ᴇʙᴀʟᴏ ᴠɴᴀᴛᴜʀᴇ ᴠ ʙᴇᴛᴏɴ ᴋᴀᴛɴᴜʟ ᴋᴏɢᴅᴀ ᴛʏ ᴘᴏsʜᴇʟ ᴘʀᴏᴛɪᴠ ᴍᴇɴʏᴀ ʏᴀ ᴛᴇʙʏᴀ ʜᴜᴇᴍ ᴄʜᴇʜʟɪʟ ᴅᴜʀᴀᴋ ᴇɢɪ ᴏᴛ sʏᴜᴅᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛʏ ɴᴇ ᴛᴀᴋᴏᴊ ᴋᴀᴋ ᴠsᴇ ᴘᴏᴛᴏᴍᴜ ᴄʜᴛᴏ ᴜ ᴠsᴇʜ ᴍᴀᴍᴀ ɢᴏᴛᴏᴠɪᴛ ᴋᴜsʜᴀᴛь ᴀ ᴛᴠᴏʏᴀ ᴍᴀᴍᴀ ᴠᴍᴇsᴛᴏ ᴇᴅʏ ᴠᴀᴍ ɴᴀ ᴜᴢʜɪɴ sᴘᴇʀᴍᴀᴄʜ ᴠʀᴀɪᴛ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴅᴀᴠᴀᴊ sᴄʜᴀs ᴍʏ s ᴛᴏʙᴏᴊ ᴘᴏᴢɴᴀᴋᴏᴍɪᴍsʏᴀ ɪ ʏᴀ sᴛᴀɴᴜ ᴛᴠᴏɪᴍ ɴᴏᴠʏᴍ ᴏᴛᴛsᴏᴍ ʜᴏᴛʏᴀ ᴘᴏ sᴜᴛɪ ʏᴀ ᴅᴀᴠɴᴏ ᴇʙᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴛᴀᴋ ᴄʜᴛᴏ ɴᴀᴢʏᴠᴀᴊ ᴍᴇɴʏᴀ ᴠsᴇᴠʏsʜɴɪᴍ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ʀɪʟɪ ᴛʏ ᴘʀᴏsᴛᴏ ᴘᴏᴘʟᴀᴛɪʟsʏᴀ sᴠᴏᴇᴊ ᴍᴀᴛᴇʀьʏᴜ ᴢᴀ sᴠᴏᴊ ʙᴀᴢᴀʀ ɪʟɪ ᴛʏ ᴅᴜᴍᴀʟ ᴄʜᴜᴛь ᴄʜᴜᴛь ᴘᴏsᴏsᴇsʜь ɪ sʙᴇᴢʜɪsʜь ɴᴇᴛ ᴛʏ ᴛᴜᴛ ɴᴀ ᴠsᴇɢᴅᴀ sᴄʜᴇɴᴏᴋ ᴢᴀᴠɪs <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴀ ᴋᴜʀᴏᴋ ɴᴀᴢʜᴀʟ ᴋᴏɢᴅᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴏsᴀʟᴀ ɪ ᴋᴏʀᴏᴄʜᴇ ᴇᴊ ʙᴀsʜᴋᴜ ᴠ ᴍʏᴀsᴏ ʀᴀᴢɴᴇsʟᴏ ɴᴏ sᴏsᴀᴛь ᴏɴᴀ ɴᴇ ᴘᴇʀᴇsᴛᴀʟᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ᴋᴏɢᴅᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴅ ᴘʀɪʜᴏᴅᴏᴍ ɢᴇʀʏᴄʜᴀ ᴇʙᴀʟ ᴏɴᴀ ᴋᴀᴢᴀʟᴀsь ᴋʀᴀsɪᴠᴏᴊ ᴠ ɪᴛᴏɢᴇ ᴋᴏɢᴅᴀ ᴍᴇɴʏᴀ ᴏᴛᴘᴜsᴛɪʟᴏ ʏᴀ ʙᴇᴢʜᴀʟ ᴠ sᴛʀᴀʜᴇ ᴏᴛ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ᴏʙʏᴄʜɴᴏ ᴘьʏᴜ ᴢᴀ ᴅᴠᴇ ᴠᴇsᴄʜɪ ɴᴀ ᴢᴀ sᴛᴏʟьᴇ ᴄʜᴛᴏʙʏ ʜᴜᴊ sᴛᴏʏᴀʟ ɪ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴘᴏʙʟɪᴢʜᴇ ʙʏʟᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴜ ᴅᴀᴠᴀᴊ ʏᴀ ᴛᴠᴏё ʀʏʟᴏ ᴠ ᴇᴛᴏᴊ ᴋғ ᴏʙᴋᴏɴᴄʜᴀʏᴜ ᴋᴀᴋ ᴛʏ ᴘᴏᴛᴏᴍ ʙᴜᴅᴇsʜь ʀᴀsᴋᴀᴢʏᴠᴀᴛь sᴠᴏɪᴍ ᴅʀᴜᴢьʏᴀᴍ ᴄʜᴛᴏ ᴛʏ ᴍᴇɴʏᴀ ᴠʏᴠᴇᴢ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴏᴛ ɴᴇᴅᴏᴛʀᴀʜᴀ ɴᴀ ᴋᴀᴢʜᴅʏᴊ ᴋᴏʟ ʟᴇᴢᴇᴛ ʏᴀ ᴜᴢʜᴇ ɴᴇ ᴢɴᴀʏᴜ ᴄʜё ᴅᴇʟᴀᴛь ᴍᴏᴢʜᴇᴛ ᴏsʜᴇᴊɴɪᴋ ᴋᴜᴘɪᴛь ᴋᴀᴋ ᴅᴜᴍᴀᴇsʜь <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ᴋᴀᴋ ɪᴍᴘᴇʀᴀᴛᴏʀ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜ ᴍᴇɴʏᴀ ᴠ ɴᴏɢᴀʜ ᴘᴏʟᴢᴀᴇᴛ ɴᴏ ᴘʀɪ ᴇᴛᴏᴍ ʏᴀ ᴢʜɪᴠᴜ ᴋᴀᴋ ᴠsᴇ ɴᴏ ᴘᴏᴄʜᴇᴍᴜ ᴛᴠᴏʏᴀ ɢᴏʀʏᴀ ᴍᴀᴛь ᴍɴᴇ ᴛᴏ sᴏsёᴛ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴇsᴛь ᴘʀɪʟᴏᴢʜᴇɴɪʏᴀ ᴇsʟɪ ᴋᴜᴘɪsʜь 3 ᴘᴀᴄʜᴋɪ sᴜʜᴀʀɪᴋᴏᴠ sᴋᴀɴɪʀᴜᴇsʜь ᴄʜᴇᴋ ɪ ᴛᴇʙᴇ ʙᴇsʟᴘᴀᴛɴᴏ ᴠʏᴘᴀᴅᴀᴇᴛ ёʙ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴏᴛ ᴏᴅɴᴏɢᴏ ᴅᴏ ᴅᴇsʏᴀᴛɪ ʀᴀᴢ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴜ ᴢʜᴇ ᴅᴀᴠᴀᴊ ᴏᴋʟᴇᴍᴀᴊsʏᴀ ᴏᴛ ᴘᴏʙᴏᴇᴠ ᴍᴏᴇɢᴏ ᴄʜᴇʟᴇɴᴀ ɪ sᴍᴇʀɪsь s ᴍʏsʟьʏᴜ ᴄʜᴛᴏ ᴇʙᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ɴᴇ ᴛᴏʟьᴋᴏ ʏᴀ ɴᴇʜᴜᴊ ɴᴀ ᴍᴇɴʏᴀ ʙʏᴄʜɪᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴋᴏɢᴅᴀ ᴄʜᴛᴏ ɴɪʙᴜᴅь ɢᴏᴛᴏᴠɪᴛ ɴᴇ ᴏʙʜᴏᴅɪᴛьsʏᴀ ʙᴇᴢ ᴍɪɴьᴇᴛᴀ ᴠᴇᴅь ᴇᴛᴀ sʜᴋᴜʀᴀ ʟʏᴜʙɪᴛ ᴏᴛsᴀsʏᴠᴀᴛь ᴠᴏ ᴠʀᴇᴍʏᴀ ɢᴏᴛᴏᴠᴋɪ ᴏʜᴜᴇsʜь ᴍᴀʟʏᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ʙʟʏᴀ ɴᴇ ᴢɴᴀʏᴜ ᴍᴏᴢʜᴇᴛ ɪ ʏᴀ ᴛᴠᴏᴊ ᴏᴛᴇᴛs ᴛʏ ᴇᴛᴏ ɴᴇ ʀᴀsᴛʀᴀᴇᴠᴀᴊsʏᴀ ʜᴜᴊ ᴢɴᴀᴇᴛ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴅᴏʜᴜʏᴀ ᴋᴛᴏ ᴇʙᴀʟ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴅᴀᴠᴀᴊ ᴘᴏɪɢʀᴀᴇᴍ ᴠ ᴋᴀʀᴛʏ ɴᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴅᴀᴢʜᴇ ᴇsʟɪ ʏᴀ ᴘʀᴏɪɢʀᴀʏᴜ ᴛʏ ᴢʜᴇ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴏɴᴀ ᴠsᴇ ʀᴀᴠɴᴏ ᴍᴏʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴅᴀ ɢᴏᴠᴏʀʏᴜ ᴛᴇʙᴇ ɴᴇ ᴅᴀᴍ ʏᴀ ᴛᴇʙᴇ ᴅᴅ ᴢᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇё ᴋᴛᴏ ᴛᴏʟьᴋᴏ ɴᴇ ᴇʙᴀʟ ɴᴀsʜёʟ ʀᴇʟɪᴋᴠɪʏᴜ ʙʟʏᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴅᴀᴠᴀᴊ ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴛᴜᴛ ᴢᴀᴛʀᴀʜᴀʏᴜ ᴅᴏ sᴍᴇʀᴛɪ ɪʟɪ ᴛʏ ᴄʜё ᴛʏᴜғʏᴀᴋ ᴅᴀᴢʜᴇ sᴏᴘʀᴏᴛɪᴠʟʏᴀᴛsьʏᴀ ɴᴇ ʙᴜᴅᴇsʜь ɴᴜ ᴢᴀ ᴇᴛᴏ ᴘʀɪᴅёᴛsьʏᴀ ᴛᴇʙʏᴀ ᴘʀᴏɢɪʙᴏᴍ sʜᴠʏʀɴᴜᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ᴛᴇʙᴇ sᴇᴊᴄʜᴀs ᴠɴᴀᴛᴜʀᴇ ʏᴀᴊᴛsᴀ ᴠ ʀᴏᴛ ᴢᴀsᴜɴᴜ ɪ ᴛʏ ɪʜ ʙᴜᴅь ᴘᴏʟᴏsᴋᴀᴛь ᴅᴏ ᴋᴏɴᴛsᴀ sᴠᴏɪʜ ᴅɴᴇᴊ ᴜёᴏᴋ ᴘᴏsʜёʟ ɴᴀʜᴜᴊ ᴏᴛ sʏᴜᴅᴀ ᴘᴏɴʏᴀʟ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴠᴏᴛ ᴇsʟɪ ʙʏ ᴛʏ ᴘʀᴏʏᴀᴠɪʟ ʜᴏᴛʏᴀ ʙʏ ᴋᴀᴘʟʏᴜ ᴜᴠᴀᴢʜᴇɴɪʏᴀ ʏᴀ ʙʏ ɴᴇ ᴇʙᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴀ ᴛᴀᴋ ɴᴀ sᴋᴏʀᴜʏᴜ ʀᴜᴋᴜ sᴇᴊᴄʜᴀs ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴅᴜᴘʟᴏ ᴘᴏʀᴠᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ᴛᴇʙᴇ ʜᴜᴇᴍ sᴇᴊᴄʜᴀs ᴘʀᴏsᴛʀᴇʟʏᴜ ᴄʜᴍᴏsʜɴɪᴋ ʏᴀ ᴛᴇ ᴠɴᴀᴛᴜʀᴇ sᴇᴊᴄʜᴀs ᴋᴀʀᴛᴇᴄʜь ᴠ ᴛᴠᴏᴊ ᴢʜɪᴠᴏᴛ ɴᴀʜᴜʏᴀᴄʜᴜ ᴛʏ ᴅʏʀᴋᴀ ᴇʙᴀɴᴀʏᴀ ᴜᴘᴏʟᴢᴀᴊ s ᴋғ ᴘᴏᴋᴀ ᴠᴏᴢᴍᴏᴢʜɴᴏsᴛь ᴇsᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ᴛᴠᴏʏᴜ ᴍᴛᴀь ɴᴀ ᴘᴏᴘᴜᴛᴋᴀʜ ᴇʙᴀʟ ᴏɴᴀ ᴘʏᴛᴀʟᴀsь ᴠ ᴍᴀsʜɪɴᴜ ᴘʀʏɢɴᴜᴛь ɴᴜ ʏᴀ ʜᴇʟᴜ ᴋᴀᴋ ᴄʜʟᴇɴ ᴇᴊ ᴠ ʀᴏᴛ ᴢᴀsᴜɴᴜʟ ᴛᴀᴋ sᴋᴀᴢᴀᴛь ᴘʀᴏᴋᴀᴛɪʟ ʙʟʏᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴇsʟɪ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴠ ᴛᴇᴄʜᴇɴɪᴇ 5 sᴇᴋᴜɴᴅ ɴᴇ ᴏᴘʀᴀᴠᴅᴀᴇᴛ sᴇʙʏᴀ ɴᴀ sᴄʜёᴛ ᴛᴏᴊ ᴛᴇᴍʏ ᴄʜᴛᴏ ᴏɴᴀ ɴᴀ ʀᴀᴊᴏɴᴇ sʜᴀʟᴀᴠᴀ ʏᴀ ᴇё ᴠʏᴇʙᴜ ʟᴏʟ ᴇᴛᴏ ʀᴏғʟ ʏᴀ ᴇё ɪ ᴛᴀᴋ ᴠʏᴇʙᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛʏ ᴇʙᴀɴɴʏᴊ ᴢᴀsʜᴋᴠᴀʀɴʏᴊ ᴜᴛёɴᴏᴋ ʏᴀ sᴇᴊᴄʜᴀs ᴘʀᴏsᴛᴏ ᴠᴏᴢьᴍᴜ ɪ s ʀᴀᴢɢᴏɴᴀ ᴠʏsʜɪʙᴜ ᴍᴏᴢɢɪ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘᴏsʟᴇ ᴇᴛᴏɢᴏ ɴᴇ ғᴀᴋᴛ ᴄʜᴛᴏ ᴏɴᴀ ᴏᴋʟɪᴍᴀᴇᴛьsʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴍʏ ᴋᴏɢᴅᴀ s ᴅʀᴜᴢьʏᴀᴍɪ ᴇᴢᴅɪʟɪ ɴᴀ ᴏʜᴏᴛᴜ ᴏʙᴇᴢᴀᴛᴇʟьɴᴏ ʙʀᴀʟɪ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴛʏ ᴘᴏᴜᴅᴍᴀᴇsʜь ᴏɴᴀ ᴇʙᴜᴄʜɪ ᴏʜᴏᴛɪᴛьsʏᴀ ɴᴇ ᴘʀᴏsᴛᴏ sʜᴀʟᴀᴠᴀ ɴᴀ ᴏʜᴏᴛᴇ ɴᴇ ᴘᴏᴍᴇsʜᴀᴇᴛ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴠ ʀᴜᴋᴀʜ ᴀᴠᴛᴏᴍᴀᴛ ᴘᴏᴛᴏᴍᴜ ᴄʜᴛᴏ sᴏʟᴅᴀᴛ ᴇʙᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь  ɪ ᴇʙᴜ ᴘᴏᴛᴏᴍᴜ ᴄʜᴛᴏ ᴠʏᴊɢʀᴀʟ ᴠᴏᴊɴᴜ ʏᴀᴊᴛsᴀ ɢʟᴏᴛᴀᴊ ᴢᴀ ᴏᴛᴄʜɪᴢɴᴜ sᴛʀᴇʟʏᴀᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴋᴀᴋ ᴘᴏᴛᴇʀᴇɴɴʏᴊ ᴍᴀᴍᴏɴᴛёɴᴏᴋ ᴠᴏʙsᴄʜᴇ ɴᴇ ᴏʀᴇɴᴛɪʀᴜᴇᴛьsʏᴀ ᴠ ᴘʀᴏsᴛʀᴀsɴᴛᴠᴇ ʏᴀ ᴇᴊ ɢᴏᴠᴏʀʏᴜ ᴄʜᴛᴏ ʏᴀ ᴇё ᴠʏᴇʙᴜ ᴏɴᴀ ɴᴇ sʜᴀʀɪᴛ ɪ ᴘʏᴛᴀᴇᴛьsʏᴀ ᴜᴇʜᴀᴛь ᴋ ᴍᴀᴍᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴍʏ ᴍᴀᴍᴜ ᴇʙᴀʟ ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ɴᴀsʜɪ ᴜᴢʏ ᴛʏᴀsɴᴏ sᴠʏᴀᴢᴀɴɴʏ ᴍᴇᴢʜᴅᴜ sᴏʙᴏᴊ ᴠᴀғᴇʟ ᴇʙᴀɴɴʏᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴢᴀ ᴅʀᴜᴢᴇᴊ ɪ ᴅᴠᴏʀ sᴛʀᴇʟʏᴀʏᴜ ᴠ ᴜᴘᴏʀ ᴛᴀᴋ ɢᴏᴠᴏʀɪʟᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴘᴏᴋᴀ ʏᴀ ᴇᴊ ʜᴜᴇᴍ ɴᴀ ʟʙᴜ ɴᴇ ᴠʏᴢʜɪɢ ᴋʟᴇᴊᴍᴏ ᴇʙᴀɴɴᴏᴊ sʜʟʏᴜʜɪ <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ɴᴀ ᴏʙᴇᴅ ʜᴜᴊ ᴠ ʀʏʟᴏ ᴢᴀᴠᴏʀᴀᴄʜɪᴠᴀʏᴜ ɪᴢᴠɪɴɪ ᴢᴀ ᴛᴀᴋᴏᴊ ᴠᴏᴘʀᴏs ᴛʏ ᴠʏʙʟʏᴀᴅᴏᴋ ɴᴏʀᴍᴀʟьɴᴏ ᴋ ᴇᴛᴏᴍᴜ ᴏᴛɴᴏsɪsʜьsʏᴀ ᴇsʟɪ ɴᴇᴛ ᴛᴏ ᴍᴏɢᴜ ᴢᴀᴠᴏʀᴀᴄʜɪᴠᴀᴛь ɴᴀ ᴜᴢʜɪɴ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴘᴏ ᴛᴀᴋᴏᴊ sʜᴇᴍᴇ ʏᴀ ᴍᴏɢᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀᴛь ʀᴀᴢ 40 ɴᴏ ᴍᴏʏᴀ sʜᴇᴍᴀ ᴇsᴄʜё ɴᴇ sᴏᴠᴇʀsʜᴇɴɴᴀ ᴛᴀᴋ ᴄʜᴛᴏ ᴛᴠᴏʏᴜ ᴍᴀᴛь sʜᴀʟᴀᴠᴜ ᴘᴏᴋᴀ ɴᴀ ʀᴀsʟᴏʙᴏɴᴇ ᴇʙᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ʙʟʏᴀ ᴇʙᴀᴛь ᴛʏ ᴄʜё ᴢᴀ ᴍᴜᴅᴀᴋ ᴛʏ ᴛᴀᴍ ᴄʜё ᴘɪᴢᴅᴇʟ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇ sʜʟʏᴜʜᴀ ʏᴀ ᴛᴠᴏʏᴜ ʀʏʟᴏ ᴄʜᴜʀᴋᴀsʜ ᴘᴏ ғᴀᴋᴛᴜ ᴠ ᴇᴛᴊᴏ ᴋғ ᴏᴘᴜsʜᴜ ᴢᴀ ᴛᴀᴋɪᴇ sʟᴏᴠᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴅᴀ ᴅᴀᴠᴀᴊ ɴᴇ ᴘᴏʀᴀᴠᴅʏᴠᴀᴊsʏᴀ ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴛʏ ᴄʜё ᴛsᴀᴘʟʏᴀ ʏᴀ sᴄʜᴀs ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴛᴜᴛ ᴛᴀᴋ ᴏᴛᴢʜᴀʀʏᴜ ᴄʜᴛᴏ ᴛʏ ʙᴏʟьsʜᴇ ɪᴢ ᴇᴛᴏᴊ ᴋғ ʙᴇᴢ ɢᴏʀʟᴏᴠᴏɢᴏ ᴍɪɴьᴇᴛᴀ sᴅᴇʟᴀɴɴᴏɢᴏ ᴍɴᴇ ɴᴇ ᴠʏᴊᴅᴇsʜь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴘᴏ ᴘʀɪɴᴛsɪᴘᴜ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴛᴀᴋ ᴛᴏ ɴᴏʀᴍᴀʟьɴᴀʏᴀ sᴏsᴋᴀ ɴᴇ ɴᴜ ᴇʟɪ ᴛᴀᴋ ʀᴀsᴜᴢʜᴅᴀᴛь ʏᴀ ʙʏ ᴍᴏɢ ᴘᴏᴜʜᴀᴢʜɪᴠᴀᴛь ᴢᴀ ɴᴇᴊ ɴᴏ ᴢʜɪᴢɴь ᴇsᴛь ᴢʜɪᴢɴь ᴇʙёᴍ ᴇё ɪ ᴢᴀᴇʙɪsь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴅᴀᴠᴀᴊ ᴜᴘᴏʀ ʟёᴢʜᴀ ᴘʀɪɴʏᴀʟ ɪ ᴢᴀʟᴜᴘᴜ ᴍɴᴇ ɴᴀᴄʜɪɴᴀᴊ ᴏʙsᴀsʏᴠᴀᴛь ᴛᴇʙᴇ sᴀʟᴀɢᴀ ᴄʜᴛᴏʙʏ ᴏᴛ sʏᴜᴅᴀ ᴜᴊᴛɪ ᴍɴᴇ ᴢᴀʟᴜᴘᴜ ᴇsᴄʜё ɢᴏᴅ ᴏʙsᴀsʏᴠᴀᴛь ᴘʀɪᴅёᴛьsʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ᴋᴀᴋ ᴛᴏ ᴠᴀᴍ ᴋʀʏsʜᴜ ᴅᴇʟᴀʟ ᴘᴏᴍɴɪsʜь ᴛʏ ᴍᴀʟᴇɴьᴋɪᴊ ʙʏʟ ɴᴏ ɴᴀ sᴀᴍᴏᴍ ᴅᴇʟᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴏɴᴀ ᴘʀᴏsᴛᴏ ɴᴇ ʜᴏᴛᴇʟᴀ ᴛʀᴀᴠᴍɪʀᴏᴠᴀᴛь ᴛᴠᴏʏᴜ ᴅᴇᴛsᴋᴜʏᴜ ᴘsɪʜɪᴋᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'ʙʟʏᴀᴛь sʜᴀᴋᴀʟ ᴛʏ ɴᴇ ᴠᴋᴜʀɪᴠᴀᴇsʜь ʏᴀ sᴄʜᴀs ᴛᴇʙʏᴀ ᴛᴜᴛ ᴋ sᴛᴇɴᴇ ᴘʀɪᴢʜᴍᴜ ɪ ᴛᴀᴋ ᴏᴛʀᴀʜᴀʏᴜ ᴋᴀᴋ ᴛᴇʙᴇ ᴇsᴄʜё ɴᴇ sɴɪʟᴏsь ᴇʙᴀɴɴʏᴊ ᴘɪᴢᴅᴏʟɪᴢ ᴅᴀᴠᴀᴊ ᴏᴛᴠᴀʟɪᴠᴀᴊ ᴏᴛ sʏᴜᴅᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ᴅᴀᴢʜᴇ ᴠ sʜᴋᴏʟᴇ ᴅᴇʟᴀʟ ᴘʀᴏᴇᴋᴛ ᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴜᴛь ᴘʀᴏᴇᴋᴛᴀ ᴢᴀᴋʟʏᴜᴄʜᴀʟᴀsь ᴠsᴇ ᴅʀᴇᴠɴɪᴇ ᴘʀᴏғᴇsɪɪ ɴᴏ ᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴏᴋᴀᴢᴀʟᴏsь sᴀᴍᴀʏᴀ ᴅʀᴇᴠɴʏᴀʏᴀ ᴘʀᴏғᴇsɪʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴘᴏᴄʜᴇᴍᴜ ᴠsᴇ ᴍʏ ᴇʙёᴍ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴏᴛᴠᴇᴛ ᴘʀᴏsᴛ ᴏɴᴀ sʜʟʏᴜʜᴀ ɴᴇ ɴᴀ ᴄʜᴛᴏ ɴᴇ sᴘᴏsᴏʙɴᴀʏᴀ ᴀ ᴛʏ ᴄʜᴛᴏ ᴅᴜᴍᴀʟ ᴄʜᴛᴏ ᴏɴᴀ ᴛᴏᴘ ᴍᴏᴅᴇʟь ᴄʜᴇʀᴛɪʟᴀ ᴇʙᴀɴɴᴀʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ɴᴇ ᴋᴏɢᴅᴀ ɴᴇ ᴅᴜᴍᴀʟ ᴄʜᴛᴏ ᴍᴏᴢʜɴᴏ ᴠʏᴇʙᴀᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴢᴀ sɪɢᴜ ɴᴜ ʜᴏᴅɪʟɪ sʟᴜʜɪ ɴᴀ ʀᴀᴊᴏɴᴇ ɴᴜ ʏᴀ ʜᴜʟᴇ ᴘᴏᴘʀᴏʙʏᴠᴀʟ ɪ ᴘʀᴏᴋᴀᴛɪʟᴏ <emoji document_id=5438153647345119196>💀</emoji>',
'ɪᴢɴᴀᴄʜᴀʟьɴᴏ ʏᴀ ᴘᴏᴅɴʏᴀʟsʏᴀ ɴᴀ ᴇʙᴀɴɪᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴠᴇᴅь ᴋᴏɢᴅᴀ ᴍᴇɴʏᴀ ɴᴀ ʀᴀʙᴏᴛᴇ sᴘʀᴏsɪʟɪ ᴄʜᴛᴏ ʏᴀ ᴜᴍᴇʏᴜ ʏᴀ ᴘʀᴏsᴛᴏ ᴘᴏᴋᴀᴢᴀʟ ᴄʜᴛᴏ ᴍᴏɢᴜ ᴠʏᴇʙᴀᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴄʜё ᴛʏ ᴛᴀᴍ ᴅᴏᴄʜь sʜᴀᴠᴇʀᴍʏ ʙʟʏᴀᴛь ʏᴀ ɪᴢ  ᴛᴇʙʏᴀ ᴛᴏᴢʜᴇ sᴅᴇʟᴀʏᴜ sʜʟʏᴜʜᴜ ᴠᴇᴅь ᴠsᴇ ᴍʏ ᴢɴᴀᴇᴍ ᴄʜᴛᴏ ʏᴀʙʟᴏɴʏᴀ ᴏᴛ ʏᴀʙʟᴏɴɪ ɴᴇ ᴅᴀʟᴇᴋᴏ ᴘᴀᴅᴀᴇᴛ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴅᴀᴢʜᴇ ʟʏᴜᴅɪ ʙᴏʟᴇʏᴜsᴄʜɪᴇ sʜɪᴢᴏғʀɪɴᴇᴊ ᴇʙᴀʟɪ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇᴛᴏ ɴᴀsᴋᴏʟьᴋᴏ ɴᴀᴅᴏ ʙʏᴛь ᴏᴘᴜsᴄʜᴇɴʏᴍ ᴄʜᴛᴏʙʏ ᴋᴀᴢʜᴅᴏᴍᴜ ᴏᴘᴜsᴄʜᴇɴᴏᴍᴜ ᴅᴀᴠᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴠ ɪsᴛᴏʀɪɪ ʀᴏssɪɪ ɴᴀᴘɪsᴀɴɴᴏ ᴄʜᴛᴏ ᴋᴏɢᴅᴀ ᴘёᴛʀ 1 ᴘʀᴀᴠɪʟ ʀᴏssɪᴊsᴋᴏᴊ ɪᴍᴘᴇʀɪᴇᴊ ʙʏʟᴀ ʟᴜᴄʜsʜᴀʏᴀ sʜᴀʟᴀᴠᴀ ᴋᴏᴛᴏʀᴀʏᴀ ᴏᴛsᴀsʏᴠᴀʟᴀ ᴇᴍᴜ ʏᴀ ɴᴀsʜёʟ ᴇё ᴇᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴇᴅᴜ ɴᴀ ᴛᴀsᴜ ᴋᴏʀᴏᴄʜᴇ sᴋᴀᴢᴀʟɪ ᴛᴀᴍ ᴇsᴛь ᴠᴀʀɪᴀɴᴛ ᴠsᴛʀᴇᴛɪᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь ɴᴜ ʏᴀ ᴠᴢʏᴀʟ 67 ᴘᴀᴄʜᴇᴋ ᴘʀᴇᴢɪᴋᴏᴠ ᴠᴇᴅь ᴇsʟɪ ᴛᴀᴍ ʙᴜᴅᴇᴛ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴠsё ᴛᴀᴋ ʙʏsᴛʀᴏ ɴᴇ ᴢᴀᴋᴋᴏɴᴄʜɪᴛьsʏᴀ <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ɢᴜʙᴜ ʜᴜёᴍ ʀᴀsᴘᴏᴛʀᴏsʜɪʟ ᴀ ᴛʏ ᴅᴏsɪʜᴘᴏʀ ᴠᴇʀɪsʜь ᴠ ᴛᴏ ᴄʜᴛᴏ ᴏɴᴀ ᴍᴏᴢʜᴇᴛ ᴘᴏsᴛᴏʏᴀᴛь ᴢᴀ ᴠᴀs ɴᴀɪᴠɴʏᴊ ᴘɪᴢᴅᴏʟɪᴢ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴠ ɢʀᴀᴢʜᴅᴀɴsᴋᴜʏᴜ ᴏᴊɴᴜ ᴍʏ ᴇʙᴀʟɪ ᴍᴀᴍᴜ ᴛᴠᴏʏᴜ ɪ ᴛᴀᴋ ɪ sʏᴀᴋ ɴᴜ ᴠᴏᴏʙsᴄʜᴇᴍ ɴᴇ ᴠ ᴇᴛᴏᴍ ᴅᴇʟᴏ ᴍʏ ᴇё ᴇʙᴀʟɪ ᴠsᴇɢᴅᴀ ᴀ ᴛʏ ᴛᴏ ᴄʜᴍᴏ ᴄʜᴛᴏ sᴍᴏᴢʜᴇsʜь ᴘʀᴏᴛɪᴠᴏᴘᴏsᴛᴀᴠɪᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴠᴏᴛ ᴛʏ ᴅɪᴋɪᴊ ᴏᴘᴜsᴄʜᴇɴᴇᴛs ᴏᴘᴜʜsʜᴇᴇ ᴅɪᴛᴇ sᴏʙᴀᴋɪ,ᴏɴᴀ ᴄʜᴏᴛ ɴᴀʙɪʀᴀᴇᴛ ɪ sᴍs ɪ ʏᴀ ᴜᴢʜᴇ ᴘᴏɴʏᴀʟ ᴄʜᴛᴏ ᴏɴᴀ sᴏsᴇᴛ ʜᴜᴊ ᴋᴀᴋ ɪ ᴇᴇ ᴍᴀᴛь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴢᴀʟᴜᴘᴇɴᴇᴛs ᴇʙᴀɴɴʏᴊ ʏᴀ ᴛᴇʙᴇ ʜᴜᴇᴍ ᴘᴏ ɢᴜʙᴀᴍ ᴅᴀᴍ sᴀʙʟᴇᴢᴜʙʏᴊ ᴘɪᴅᴏʀᴀs)ᴛʏ ᴘʀᴏsᴛᴏ ᴍᴏɪᴍ ʜᴜᴇᴍ ᴏᴛʙɪᴛʏᴊ)ᴜʙɪᴛʏᴊ)ᴠ ᴍᴜsᴏʀᴋᴜ ᴠʏᴋɪɴᴜᴛʏᴊ)ᴋᴀᴋ ᴘɪᴅᴏʀᴀs ᴘᴏᴛᴇʀʏᴀɴɴʏᴊ ᴛsᴇʟᴜᴇsʜь ᴍᴏʏᴜ ᴍᴀsʜᴏɴᴋᴀ ɪ sʟɪᴢʏᴠᴀᴇsʜь ʟᴇᴄʜᴇʙɴᴜʏᴜ sᴍᴇᴛᴀɴᴜ s ᴍᴏᴇɢᴏ ʜᴜʏᴀ)ʏᴀ ᴢʜᴇ ʙʟʏᴀᴛь ᴛᴠᴏʏᴜ ᴠsʏᴜ sᴇᴍьʏᴜ ʜᴜᴇᴍ ᴅᴜsʜɪʟ ᴇʙᴀɴɴᴀʏᴀ ᴛʏ sᴘɪᴅᴏᴢɴᴀʏᴀ ᴍᴀᴋᴀᴋᴀ ᴋᴏᴛᴏʀᴀʏᴀ ɴᴀ ᴍᴏᴊ ʙᴀɴᴀɴ ᴏʜᴏᴛᴜ ᴜsᴛʀᴏɪʟᴀ)ᴛʏ ᴛᴀᴍ ɴᴇ ᴠᴇsɪ ɴᴀ ᴍᴏᴇᴍ ʜᴜᴇ ᴋᴀᴋ ɴᴀ ʟɪᴀɴᴇ <emoji document_id=5438153647345119196>💀</emoji>',
'sʟʏsʜ ʏᴀ sᴄʜᴀ ɴᴀ sᴠᴏʏᴜ ᴢᴀʟᴜᴘᴜ ᴠᴏᴢɴᴇsᴜ ᴛᴠᴏʏᴜ ᴘɪᴢᴅᴀᴋ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴏᴄʜᴋɪ ɪ ɴᴀᴄʜɴᴜ ᴠsᴛᴜᴘᴀᴛь sᴠᴏɪᴍ ʜᴜᴇᴍ ᴠ ᴘᴏʟᴏᴠᴏᴊ ᴋᴏɴᴛᴀᴋᴛ s ᴛᴠᴏɪᴍɪ ᴜsʜᴀᴍɪ))) <emoji document_id=5438153647345119196>💀</emoji>',
'ᴘᴏᴍɴɪsʜь ᴋᴀᴋ ʏᴀ sᴘɪᴢᴅᴇʟ ᴋᴏᴘьᴇ ᴜ ʀʏᴛsᴀʀʏᴀ ɪ ᴇᴛɪᴍ ᴢʜᴇ ᴋᴏᴘьᴇᴍ ᴏᴛъᴇʙᴀʟ ᴛᴠᴏʏᴜ ʙᴀʙᴜsʜᴋᴜ!) <emoji document_id=5438153647345119196>💀</emoji>',
'ʜᴜᴇsᴏs?) ᴛʏ ᴜᴠɪᴅᴇʟ ᴘɪᴢᴅᴜ sᴠᴏᴇᴊ ᴍᴀᴍʏ ɪsᴘᴜɢᴀʟsʏᴀ ɪ sъᴇʙᴀʟsʏᴀ? <emoji document_id=5438153647345119196>💀</emoji>',
'ᴅᴀ ᴛʏ ʙʟʏᴀᴛь ᴀʟᴀᴘᴇᴢᴅʏʀь))ᴛᴠᴏʏᴀ ᴍᴀᴍᴋᴀ ᴠʏᴛᴠᴏʀʏᴀᴇᴛ ᴀᴋʀᴏʙᴀᴛɪᴄʜᴇsᴋɪᴇ ᴛʀʏᴜᴋɪ sᴠᴏɪᴍ ʀᴛᴏᴍ ɴᴀ ᴍᴏᴇᴍ ʜᴜʏᴜ))) <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ᴇʙᴜ ᴛᴠᴏʏᴜ ᴍᴀᴍᴋᴜ ᴠ ᴘᴏᴘᴇʀᴇᴄʜɴᴜʏᴜ ᴋɪsʜᴋᴜ ɪ ᴏɴᴀ ᴅᴏʜɴɪᴛ) <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛʏ ʀᴇsʜɪʟ ᴠsᴋᴀʀᴀʙᴋᴀᴛьsʏᴀ ɴᴀ ᴍᴏᴊ ʜᴜᴇᴛs ᴘsɪɴᴀ ʀᴀᴢᴏʀᴠᴀɴɴᴀʏᴀ ɴᴜ ʏᴀ sᴄʜᴀ ᴠᴏᴢьᴍᴜ sᴠᴏʏᴜ ʙɪᴛᴜ ʙʟʏᴀᴛь ɪ ʀᴀssʜɪʙᴜ ᴛᴇʙʏᴀ ɢᴏʟᴏᴠᴏᴊ ᴏʙ ᴋᴀғᴇʟь <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛʏ ᴠᴏsᴛᴏʀᴢʜᴇɴɴᴏ ᴜʜɴᴜʟ ɪ ᴛᴜᴛ ᴘᴀʀᴜ ᴠᴏʟᴏsᴀᴛʏʜ ʏᴀɪᴛs ᴜᴅᴀʀɪʟɪ ᴛᴇʙʏᴀ ᴛᴀᴋ ᴄʜᴛᴏ ᴛʏ ɴᴇ ᴍᴏɢ ᴏᴘʀᴀᴠɪᴛьsʏᴀ ɪ ᴛᴏʟьᴋᴏ ᴘᴏsʟᴇ ᴛᴏɢᴏ ,ᴋᴀᴋ ᴛʏ ᴏᴄʜɴᴜʟsʏᴀ ᴛʏ ᴘᴏᴄʜᴜᴠsᴛᴠᴏᴠᴀʟ ,ᴋᴀᴋ ᴛᴠᴏᴊ ʏᴀᴢʏᴋ ʟᴏᴠᴋᴏ ʀᴀʙᴏᴛᴀᴇᴛ ᴠ ᴄʜёʀɴᴏᴊ ɢʀʏᴀᴢɴᴏᴊ ᴢʜᴏᴘᴇ ᴏᴅɴᴏɢᴏ ᴘᴏᴅᴢᴀʙᴏʀɴᴏɢᴏ ᴜʙʟʏᴜᴅᴋᴀ ... <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴋᴏɢᴅᴀ ᴍᴏᴊ ʜᴜᴊ ᴠsᴛᴀᴇᴛ ᴇᴛᴏ ᴢɴᴀᴄʜɪᴛ ᴄʜᴛᴏ ᴛᴠᴏᴊ ʀᴏᴛɪᴋ ʜᴏᴄʜᴇᴛ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ʙᴏʟьsʜᴇ ᴄʜᴇᴍ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ? ʏᴀ sᴄʜᴀs ʜᴜᴇᴍ ᴛᴇʙᴇ ʀᴏᴛ ᴅʏʀʏᴀᴠɪᴛь ʙᴜᴅᴜ ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ.  <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛʏ ʙʟʏᴀᴛь ᴘsɪɴᴀ ᴛʏ ᴛᴀᴋɪ ɴᴇ ᴘᴏɴʏᴀʟ ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴅʟʏᴀ ᴛᴇʙʏᴀ ᴛsᴀʀь ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ ᴛᴇʙʏᴀ ᴄʜᴛᴏ ʜᴜᴇᴍ ᴜᴇʙᴀᴛь ᴄʜᴛᴏʙ ᴛʏ sʟᴜsʜᴀʟsʏᴀ ᴍᴇɴʏᴀ, <emoji document_id=5438153647345119196>💀</emoji>',
'ʙʟʏᴀʏᴀʏᴀ ʏᴀ ᴛᴜᴛ ᴘᴏɴʏᴀʟ ᴢᴀᴄʜᴇᴍ ᴛᴇʙʏᴀ ᴇʙᴀᴛь ᴠᴏᴛ sᴍᴏᴛʀɪ ᴘᴏᴍɴɪsʜь ᴋᴀᴋ ᴛʏ ᴍɴᴇ ᴢᴀ sᴠᴏᴊ ᴏᴛsᴏs ɴᴇ ᴘʟᴀᴛɪʟ? ᴛʏ ᴘʏᴛᴀʟsʏᴀ ᴍɴᴇ sᴅᴇʟᴀᴛь ᴏᴛsᴏs ᴢᴀ ᴋʀᴇᴅɪᴛ? ᴘᴏɴɪᴍᴀᴇsʜь? ʙʙʟʏᴀ ᴛʏ ʀɪʟɪ ᴅᴜᴍᴀᴇsʜь ᴠʏᴠᴇᴢᴇsʜь ᴍᴇɴʏᴀ? ʜᴜᴇsᴀs ᴛʏ ᴇʙᴀɴʏᴊ ᴘɪᴅᴏʀᴀs <emoji document_id=5438153647345119196>💀</emoji>',
'sʟʏsʜɪsʜь ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴋᴀᴋ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟɪ sᴛɪʟᴇᴍ ᴢʜᴜʀᴀᴠʟʏᴀ? ᴘᴏᴍɴɪsʜь ᴋᴀᴋ ᴏɴᴀ sᴛᴀɴᴀʟᴀ ɴᴀʜᴜᴊ sᴜᴠᴀʟᴀ sᴠᴏʏᴜ ɢᴏʟᴏᴠᴜ ᴠ ᴢᴇᴍʟʏᴜ ᴇʙᴀᴛь ʏᴀ ᴛᴏɢᴅᴀ ᴏʀᴀʟ ᴜʜʜʜᴀ ᴋᴀᴋ sʜᴀs ɴᴀᴅ ᴛᴏʙᴏᴊ ᴋᴀᴋ ʀᴠᴜᴛ ᴛᴇʙᴇ sᴄʜᴇᴋᴜ ᴍᴏɪᴍ ʜᴜᴇᴍ <emoji document_id=5438153647345119196>💀</emoji>',
'ʙʟʏᴀᴛь ᴛʏ ᴄʜᴇ ɴᴀᴢᴜᴊ ɴᴀʜᴜᴊ ᴀʜᴜᴇʟᴀ ᴘɪᴢᴅᴀʟɪᴢᴋᴀ ᴇʙᴀɴᴀʏᴀ ᴛᴇʙʏᴀ ᴄʜᴛᴏ ɴᴀʜᴜᴊ ᴇʙᴀᴛь ᴇᴀᴋ sʜʟʏᴜʜᴜ ᴅʀᴀɴᴜʙ ɪʟɪ ᴄʜᴛᴏ ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ ᴅᴀ ʏᴀ/ᴛᴇʙʏᴀ ᴇʙᴀᴛь ᴋᴀᴋ sʜʟʏᴜʜᴜ ʙᴜᴅᴜ ᴘɪᴅᴏʀᴀs ᴛʏ ᴇьᴀɴʏᴊ ɴᴀᴢᴜᴊ ᴘᴏsʜᴇʟ ᴘᴇᴛᴜʜ ᴅʀᴀɴɴʏᴊ ʏᴀ ᴢʜᴇ ɴᴀʜᴜᴊ ᴇʙᴀᴛь ᴛᴇʙʏᴀ ʙᴜᴅᴜ ᴘᴏᴍɴɪsʜь ᴋᴀᴋ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀᴄʜᴀʟᴀ sᴏsᴀᴛь ᴍɴᴇ ʜᴜᴊ ɪ ᴘᴏʙᴇᴢʜᴀʟᴀ ᴠ ᴛᴜᴀʟᴇᴛ ᴠᴏ ᴠʀᴇᴍʏᴀ ᴋᴏɢᴅᴀ ᴜ ᴛᴇʙʏᴀ ᴘᴏɴᴏsɪʟ ɪ ᴛʏ ɴᴀsʀᴀʟ ɴᴀ sᴠᴏʏᴜ ᴍᴀᴛь ᴀ ᴏɴᴀ ᴢᴀ ᴇᴛᴏ ᴛᴇʙʏᴀ ᴇʀsʜɪᴋᴏᴍ ᴠʏᴇʙᴀʟᴀ ᴘᴏᴍɴɪsʜь ᴛʏ ᴢʜᴇ ɴᴀʜᴜᴊ ɴᴇᴋᴄʜᴇᴍɴʏᴊ ᴘɪᴅᴏʀᴀs ᴛᴇʙʏᴀ ᴍᴀʟᴏ ᴠʏᴇʙᴀᴛь ɪ ᴛʏ ᴇsᴄʜё ᴘʏᴛᴀᴇsʜьsʏᴀ ᴄʜᴛᴏ ᴛᴏ ᴘɪsᴀᴛь ʜᴜᴇsᴀs ᴛʏ ᴇʙᴀɴʏᴊ )ᴘᴏᴍɴɪsʜь ᴋᴀᴋ ᴜᴄʜᴇɴʏᴇ ɴᴀsʜʟɪ ᴠ ᴘɪᴢᴅᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴋᴍ ᴋᴏsᴛь ᴅɪɴᴏᴢᴀᴠʀᴀ? ᴛʏ ɴᴀʜᴜᴊ ᴍᴏᴇɢᴏʜᴜʏᴀ ɴᴇ sᴛᴏɪsʜь ᴘʀɪᴄʜᴇᴍ ᴛᴜᴛ ᴛᴠᴏᴊ ᴏᴛsᴏs ᴇʙᴀɴʏᴊ ᴛʏ ᴢᴜɴsᴀᴀ ᴛʏ ᴜ ᴍᴇɴʏᴀ ʙᴇsᴘʟᴀᴛɴᴏ sᴘᴀsᴀᴛь ᴅᴏʟᴢʜᴇɴ ᴘᴏɴɪᴍᴀᴇsʜь ʜᴜᴇsᴀs ᴛʏ ᴇʙᴀɴʏᴊ ᴠ ʀᴏᴛ ᴛʏ ʙʟʏᴀᴛь ᴘᴇᴛᴜʜ ᴇʙᴀɴʏᴊ ᴘᴏsʜᴇʟ ʏᴀ ᴛᴇʙᴇ ɢᴏᴠᴏʀʙ ɴᴀ ʜᴜᴊ ᴘɪᴅᴏʀᴀs <emoji document_id=5438153647345119196>💀</emoji>',
'sʟʏsʜь ᴛʏ ᴘɪᴅᴏʀᴀs ᴛʏ ᴍᴇɴʏᴀ ɴᴇ ᴢᴀᴛʀᴏʟɪsʜь ɪʙᴏ ᴛʏ ʜᴜᴊ ᴍɴᴇ ʏᴀᴢʏᴋᴏᴍ ᴍᴏᴢᴏʟɪsʜь, ʏᴀ ᴇʙᴀʟ ᴛᴇʙʏᴀ ᴠ ʀᴏᴛ ᴛᴀᴋ ᴄʜᴛᴏ ɪᴅɪ ɴᴀʜᴜᴊ ᴇʙᴀɴʏᴊ ᴠ ʀᴏᴛ) ᴇʙᴀʟɪ ᴛᴇʙʏᴀ ᴄʜᴜʀᴋɪ ᴛʏ ᴇsᴄʜё ʜᴏᴄʜᴇsʜь ᴍɴᴇ ᴄʜᴛᴏ ᴛᴏ ᴘɪᴢᴅᴇᴛь? ʜᴜᴇsᴀs ᴛʏ ᴇʙᴀɴʏᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ᴛʏ ᴄʜᴇ ᴇʙᴀᴛь ᴀʜᴜᴇʟᴀ ɴᴀʜᴜᴊ ᴘɪᴅᴏʀᴀsᴋᴀ ɴᴀᴢᴜᴊ sᴄʜᴀs ᴍᴏᴊ ʜᴜᴊ ᴠsɪᴀɴᴇᴛ ᴀ ᴛʏ ʟʏᴀᴢʜᴇsʜь ᴘᴏɴɪᴍᴀᴇsʜь? ʜᴜᴇsᴀs ᴇьᴀɴʏᴊ ᴛʏ ᴍᴏᴊ ʜᴜᴊ sᴏsᴀᴛь ʙᴜᴅᴇsʜь ᴋᴀᴋ ɴɪᴋᴛᴏ ᴅʀᴜɢᴏᴊ ᴘɪᴅᴏʀᴀs ᴛʏ ᴇʙᴀɴʏᴊ ʙʟʏᴀᴛь ᴘᴇᴛᴜʜ sᴜᴋᴀ ɴᴀʜᴜᴊ ɪᴅɪ ʏᴀ ɴᴀʜᴜᴊ ɴᴀᴄʜɴᴜ ᴛᴇʙʏᴀ ᴇʙᴀᴛь ɪ ᴅᴀᴢʜᴇ ɴᴇ ᴘɪᴋɴᴜ <emoji document_id=5438153647345119196>💀</emoji>',
'sʜʟʏᴜʜᴀ ᴇʙᴀᴛь ᴘɪsʜɪ ɴᴏʀᴍᴀʟьɴᴏ ᴛʏ ᴅʟʏᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ᴘɪsʜᴇsʜь ᴘᴏɴɪᴍᴀᴇsʜь? ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ ᴛʏ ʙʟʏᴀᴛь ɴᴀ ᴍᴏᴊ ʜᴜᴊ ᴀɢʀ sᴠᴏᴊ ɴᴇ ᴏᴛᴘᴜsᴋᴀᴊ ᴇʙᴀɴʏᴊ ᴠ ʀᴏᴛ ᴘᴇᴛᴜʜ ᴛʏ ᴇʙᴀɴʏᴊ ᴇʙᴀʟɪ ᴛᴇʙʏᴀ ᴘsʏ ɴᴀʜᴜᴊ ᴘɪᴅᴏʀᴀs ᴛʏ ɢᴀʟɪᴍʏᴊ ʜᴜᴇsᴀs ᴇʙᴀɴʏᴊ ᴘᴇʀᴇᴠᴀʀɪᴠᴀᴊ ᴠsᴇ ᴄʜᴛᴏ ʏᴀ ᴘɪsʜᴜ ᴘɪᴅʀ ?? <emoji document_id=5438153647345119196>💀</emoji>',
'sʟʏsʜɪsʜь ᴛʏ ᴢʜɪᴠᴏᴛɴᴏᴇ ᴛᴇʙʏᴀ sᴄʜᴀs ʙᴏɢᴀᴛʏʀь ᴠ ᴢʜᴏᴘᴜ ᴅʀᴀᴛь ʙᴜᴅᴇᴛ ᴘᴏɴɪᴍᴀᴇsʜь? ʜᴜᴇsᴀs ᴛʏ ᴇʙᴀɴʏᴊ ʏᴀ ᴛᴇʙʏᴀ ᴇʙᴀᴛь ᴠʏᴇʙᴜ ᴋᴀᴋ sʜʟʏᴜʜᴜ sᴘɪᴅᴏᴢɴᴜʏᴜ ɴᴀʜᴜᴊ <emoji document_id=5438153647345119196>💀</emoji>',
'ʙʟʏᴀᴛь ᴇʙᴀᴛь ᴛᴇʙʏᴀ ᴢᴀ sᴄʜᴇᴋᴜ ᴛʏ ᴄʜᴛᴏ ɴᴀʜᴜᴊ ᴘᴇʀᴇᴅᴏᴍɴᴏᴊ ᴜɴɪᴢʜᴀᴇsʜьsʏᴀ? ᴘɪᴅᴏʀᴀs ɴᴀʜᴜᴊ ᴛᴇʙʏᴀ ᴄʜᴛᴏ ᴠʏᴇʙᴀᴛь? ᴄʜᴛᴏ ʟᴇ? ʜᴜᴇsᴀs? <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ᴇʙᴀᴛь ᴋᴏɢᴅᴀ ᴠ ᴢᴇʀᴋᴀʟᴏ sᴍᴏᴛʀʏᴜ ᴠɪᴢʜᴜ ᴛᴠᴏᴇ ᴇʙᴀɴᴏᴇ ʟɪᴛsᴏ ᴠ sᴘᴇʀᴍᴇ ᴘᴏɴɪᴍᴀᴇsʜь? ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ? ʏᴀ ᴛᴇʙʏᴀ ᴇʙᴀᴛь ʙᴜᴅᴜ ᴋᴀᴋ sʜʟʏᴜʜᴜ ᴇʙᴀɴᴜʏᴜ ?? ᴛʏ ɴᴇ ᴘᴏɴɪᴍᴀᴇsʜь ᴘᴏʜᴏᴅ? <emoji document_id=5438153647345119196>💀</emoji>',
'ʙʟʏᴀ ᴇʙᴀᴛь ᴛʏ ɴᴀʜᴜᴊ ʜᴜᴇᴘʟᴇᴛ ᴛʏ ᴄʜᴛᴏ ᴇʙᴀᴛь ʜᴜʏᴀᴍɪ ᴢᴀsᴄʜɪsᴄʜᴀᴇsʜьsʏᴀ? ᴘɪᴅᴏʀᴀs ɴᴀʜᴜᴊ sʜᴇʟ ᴏᴛsʏᴜᴅᴀ ᴇʙᴀᴛь ᴛᴇʙʏᴀ sᴄʜᴀs ɴᴀᴄʜɴᴜ ɴᴀʜᴜᴊ ?? ʙʟʏᴀ ᴍɴᴇ ᴘᴏʜᴜᴊ ɴᴀ ᴛᴇʙʏᴀ ᴅᴢʜ <emoji document_id=5438153647345119196>💀</emoji>',
'ʏᴀ ɴᴀʜᴜᴊ ᴋᴏɴᴠᴇsᴋᴜʏᴜ ᴛᴠᴏᴊ ʀᴏᴛ ɪ ᴢᴀsᴛᴀᴠʟʏᴜ sᴏsᴀᴛь ᴘᴏɴʏᴀᴛɪᴇ ɪᴍᴇᴇsʜь? ʏᴀ ᴛᴠᴏᴊ ʜᴜᴊ ᴠ ᴍʏᴀsᴏʀᴜʙᴋᴜ sᴜᴠᴀᴛь ʙᴜᴅᴜ ᴀ ᴘɪᴢᴅᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴋɪ ɴᴀ ᴍᴏᴊ ʜᴜᴊ) ᴘɪᴅᴏʀᴀs ᴛʏ ᴇʙᴀɴʏᴊ ᴏᴅɴᴀᴋᴏ <emoji document_id=5438153647345119196>💀</emoji>' ]
        self.db.set(self.strings['name'], 'state', True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl))
            await sleep(0.1)
            await sleep(time)
            
    async def крестcmd(self, message):
        """— Запустить модуль по указанной команде"""
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b><emoji document_id=5420526968418345993>🤍</emoji> ⲙ૦∂ƴʌь #κƿ૯ς੮ η૯ƿ૯ς੮ɑʌ κɑƿɑ੮ь ੮ɞ૦ю ⲙɑ੮ь. <emoji document_id=5420526968418345993>🤍</emoji></b>")
            return
        await utils.answer(
            message,
            "<b><emoji document_id=5420526968418345993>🤍</emoji> ⲙ૦∂ƴʌь #κƿ૯ς੮ ⲏɑ૫ɑʌ κɑƿɑ੮ь ੮ɞ૦ю ⲙɑ੮ь. <emoji document_id=5420526968418345993>🤍</emoji></b>\n\n"
            "<b><emoji document_id=5420526968418345993>🤍</emoji> ૫੮૦ઠы ૦ς੮ɑⲏ૦ɞυ੮ь ηƿ૦ηυਘυ.</b> <code>.крест</code>",
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl = [
        '[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы жᴇ ʙ ᴋᴀчᴇᴄᴛʙᴇ ᴋиᴄᴛᴏчᴋи нᴀ иɜᴏ ʙ ɯᴋᴏᴧᴇ иᴄᴨᴏᴧьɜᴏʙᴀᴧ ʍᴏй хуй) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ʍнᴇ ᴄᴏᴄᴀᴧ ᴛᴀᴋ дᴏᴧᴦᴏ чᴛᴏ у ᴛᴇбя ɸᴧюᴄ ʙыᴄᴋᴏчиᴧ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я нᴀ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴋᴀᴩᴛᴏɯᴋу ᴄᴀжᴀᴛь щᴀᴄ буду) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ʍᴏй хуй ᴏбниʍᴀᴇɯь ᴋᴀᴋ ʍᴀʍᴋу ᴄʙᴏю) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴛᴇбя хуᴇʍ ʙыбиʙᴀᴧ ᴋᴀᴋ ᴋᴏʙᴩиᴋ нᴀхуй) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏй ᴩᴏᴛ ᴋ ʍᴏᴇʍу хую ᴨᴩиᴧиᴨ ᴋᴀᴋ ᴨияʙᴋᴀ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы нᴀ ʍᴏᴇʍ хую жиᴩᴏʍ ᴛᴏᴋ ᴛᴩяᴄᴇɯь ᴀ нᴇ ᴨиɜдᴏй) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ʍнᴇ ᴄᴏᴄᴀᴧ ᴛᴀᴋ чᴛᴏ ᴀж ᴏбᴧᴀᴋᴀ нᴀ нᴇбᴇ ᴩᴀɜᴏɯᴧиᴄь) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ᴄ ʍᴏᴇᴦᴏ хуя ᴄʙᴏю ʍᴀᴛь ᴩᴀᴄᴛᴩᴇᴧиʙᴀᴧ ᴄᴨᴇᴩʍᴏй) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴛʙᴏю ʍᴀᴛь хуᴇʍ ᴩᴀɜᴏбᴩᴀᴧ нᴀ ʍᴇᴛᴀᴧᴀᴧᴏʍ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʍᴏй хуй дᴧя ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴋᴀᴋ ᴨᴩᴏʙᴏдниᴋ ʙ жиɜнᴇ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ʍᴏй хуй ʙᴏɜдуɯныʍи ᴨᴏцᴇᴧуяʍи ɜᴀцᴇᴨиᴛь ᴨыᴛᴀᴧᴄя) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы нᴀ ᴨᴏᴄᴧᴇдᴏᴋ ʍᴏй чᴧᴇн ᴄᴏᴄᴀᴧ ᴋᴀᴋ ʍᴀɯинᴀ ᴇбᴀнᴀя) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴛʙᴏю ʍᴀᴛь хᴏᴛᴇᴧ ᴨᴏᴇбᴀᴛь ,ᴀ ᴏнᴀ и ᴛᴀᴋ ужᴇ дыᴩяʙᴀя) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ᴨиɜду ᴄʙᴏю ᴄᴛᴇᴧиɯь ᴨᴏд дʙᴇᴩи ʍᴏи) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я хуᴇʍ ᴛᴇбᴇ ʙ ᴧᴏб щᴀᴄ ᴨᴏᴄᴛучу нᴀхуй) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴛʙᴏю ʍᴀᴛь щᴀᴄ нᴀ хуй ᴨᴏᴧᴏжу ᴋᴀᴋ бᴧин ᴇбᴀᴛь) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я нᴀ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯᴋи ʍᴀᴋᴀᴩᴏны жᴀᴩиᴧ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я нᴀ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴋᴀньᴋᴀʍи ᴋᴀᴛᴀᴧᴄя) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я чᴇᴩᴇɜ ᴨиɜду ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴛᴇбя ᴋᴏᴩʍиᴧ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʙ ᴨиɜдᴀᴋᴇ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ʍуᴄᴏᴩ хуᴇʍ ʙыᴛᴀщу щᴀᴄ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴛʙᴏю ʍᴀᴛь нᴀ хуй нᴀᴄᴀдиᴧ ᴋᴀᴋ нᴀ ᴄᴛуᴧ ᴨᴏᴄᴀдиᴧ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ʙ ʍᴏй хуй ʙᴇᴩиɯь ᴋᴀᴋ ʙ чудᴏ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ʍᴏй хуй ᴨыᴛᴀᴇɯьᴄя ᴋуᴩиᴛь ᴋᴀᴋ ᴄиᴦу) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴛʙᴏю ʍᴀᴛь хуᴇʍ ᴨну ᴏнᴀ ʙ дᴇᴩᴇʙᴏ уᴇбᴇᴛᴄя) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴛʙᴏю щᴇᴋу хуᴇʍ ᴨᴩᴏᴛᴋнуᴧ ᴋᴀᴋ ᴏᴩᴦᴀᴧиᴛ ᴇбᴀᴛь) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы нᴀ ʍᴏᴇʍ хую ᴋᴀᴋ ɸуᴛбᴏᴧьный ʍяч, ʍᴏй хуй ᴛᴇбя ᴨинᴀᴇᴛ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я щᴀᴄ ʙ ᴛʙᴏᴇʍ ᴨиɜдᴀᴋᴇ хуᴇʍ ᴨᴏᴩядᴏᴋ нᴀʙᴏдиᴛь буду) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ʙ ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴋᴇ хуᴇʍ ɜᴀɯᴇᴧ ᴋᴀᴋ бᴀᴛьᴋᴀ ʙ дᴏʍ нᴀхуй) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʍнᴇ ᴛᴇбя ᴄ хуя ᴄᴛᴩяхнуᴛь ᴋᴀᴋ ᴨᴇᴨᴇᴧ ᴄ ᴄиᴦᴀᴩᴇᴛы чᴛᴏᴧᴇ?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я уᴄᴨᴇʙᴀᴧ ᴛʙᴏᴇй ʍᴀᴛᴇᴩи ᴇщᴇ нᴀ ᴨᴇᴩᴇʍᴇнᴀх ʙ ɯᴋᴏᴧᴇ щᴀ щᴇᴋу ᴄунуᴛь) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы жᴇ нᴀ 23 ɸᴇʙᴩᴀᴧя будᴇɯь ᴄʙᴏю ᴨиɜду ᴋ ʍᴏᴇʍу хую ᴨᴩиᴨᴏднᴏᴄиᴛь) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴧюдяʍ ᴏбычнᴏ ʙ ʍᴀᴇ ᴛᴇᴨᴧᴏ, ну ᴀ ᴛы ᴋ ᴀᴋ ᴨидᴀᴩᴀᴄ у ʍᴇня ᴨᴏд яйцᴀʍи ᴄидиɯь и ᴦᴩᴇᴇɯьᴄя) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴛᴇбᴇ щᴀᴄ ᴋᴩч ʙ ухᴏ ᴋᴏнчу ᴄᴏ ᴩᴛᴀ ʙыᴧьᴇᴛᴄя ᴋᴀᴋ биɸидᴏᴋ нᴀхуй) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ʙ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯᴋи ᴨᴩᴀʙᴧю ᴄʙᴏиʍ хуᴇʍ ᴋᴀᴋ ᴧᴇнин ᴧᴇнинᴦᴩᴀдᴏʍ ʙ 41 ᴄуᴋᴀ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы бᴧяᴛь ᴋ ʍᴏᴇʍ хую ᴄᴏ ʙᴄᴇʍ ᴄᴇᴩдцᴇʍ ᴀ ᴏн нᴀ ᴛᴇбя ᴄᴄыᴛ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴛʙᴏᴇй ʍᴀᴛᴇᴩи нᴀ нᴏʙый ᴦᴏд ʙ ᴨиɜду ᴀᴧᴇʙьᴇху ɜᴀᴋинуᴧ и ʍᴇᴄиᴧ ᴇбᴧᴏʍ ᴛʙᴏиʍ :d [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы нᴀхуй ᴄʙᴏᴇй ᴨиɜдᴏй нᴀ ʍᴏᴇʍ хую ᴛᴀнᴇц бᴏйцᴀ иᴄᴨᴩᴀʙᴧяᴧ, ᴨиᴛух ᴇбᴀный) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏя ʍᴀᴛь нᴀ ʍᴏй хуй ᴋᴧюᴇᴛ, ᴨᴧᴀᴛʙᴀ ᴇбᴀнᴀя) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴄᴧыɯ, ᴨидᴏᴩᴀᴄ, ᴄюдᴀ иди ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴛʙᴏᴇй ʍᴀᴛᴇᴩи дᴀᴧ ᴋᴏᴧбᴀᴄᴏй ᴨᴏ ᴇбᴀᴧу, и ᴄᴋᴀɜᴀᴧ, чᴛᴏ ᴛᴀᴋ быᴧᴏ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴇбᴀᴛь ᴛы ᴋуб ᴋʙᴀдᴩᴀᴛный ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏя ʍᴀʍᴀɯᴀ ʙ ᴧᴇᴄу нᴀᴛᴋнуᴧᴀᴄь нᴀ ʍᴏй хуй,ᴋᴀᴋ ᴋᴩᴀᴄнᴀя ɯᴀᴨᴏчᴋᴀ нᴀ ʙᴏᴧᴋᴀ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏя ʍᴀᴛь ɜᴀдᴇᴩжиʙᴀᴇᴛ дыхᴀниᴇ ᴨᴩи ʙидᴇ ʍᴏᴇᴦᴏ хуя) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏ ɸᴀᴋᴛу ᴛы ᴄᴏᴄᴇɯь ʍнᴇ хуй) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏя ʍᴀᴛь бᴇᴧый ᴧᴇбᴇдь ʍᴏᴇᴦᴏ хуя ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ɯёᴧ нᴀ ɸᴩᴏнᴛ ʙ нᴀдᴇждᴇ уʙидᴇᴛь и ᴄᴨᴀᴄᴛи ᴏᴛ ᴨᴧᴇнᴀ ᴨиɜду ᴛʙᴏᴇй ʍᴀʍᴀɯи ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ϶ᴛᴏ нᴏʙᴀя ϶ᴩᴀ ᴛᴩᴏᴧᴧинᴦᴀ, ᴛуᴛ ᴄᴏɯᴧиᴄь ʙ ᴨᴏᴇдинᴋᴇ ɜубы ᴛʙᴏᴇй ʍᴀᴛᴇᴩи и ʍᴏй чᴧᴇн ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ᴋудᴀ ᴄъᴇбыʙᴀᴇɯь? ) ɜʙᴇᴩᴏᴄᴏʙхᴏɜ ᴀнᴀᴧьный ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь ʙ ᴨᴀᴩᴋᴇ юᴩᴋᴄᴋᴏᴦᴏ ᴨᴇᴩᴇᴏдᴀ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ɸу, ᴄᴛᴩᴇᴧᴏчниᴋ, ᴛʙᴏя ʍᴀᴛь ᴛᴏжᴇ ᴄᴛᴩᴇᴧяᴇᴛ ᴦубᴏй ᴨᴏ ʍᴏᴇʍу хую ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧ ᴋᴏᴦдᴀ нᴀ ᴨᴏᴧянᴋᴇ ɜᴀжᴦᴧиᴄь ɸᴏнᴀᴩи ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏя ʍᴀᴛь уʙидᴇʙ ʍᴏй хуй ᴄᴋᴀɜᴀᴧᴀ -" чᴛᴏ ɜᴀ ᴋᴩᴀᴄᴀʙᴇц " [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы нᴀʙᴇᴩнᴏᴇ нᴇ ɜнᴀᴧ, нᴏ ʍᴏй хуй ᴨᴩᴏяʙᴧяᴧ ᴀᴋᴛиʙнᴏᴄᴛь ᴇщё ʙ ᴀнᴛичнᴏᴄᴛи, ʍᴏй хуй ᴨᴏ ᴄᴧᴏʙᴀʍ учᴇных быᴧ ᴄᴨᴀᴄиᴛᴇᴧᴇʍ ᴧюдᴄᴋᴏᴦᴏ ᴩᴏдᴀ. ʍᴏй хуй ᴄᴨᴀᴄ ᴧюдᴇй ᴏᴛ ᴦᴏᴧᴏдᴀ и жᴀжды ʙ ᴛᴏʍ чиᴄᴧᴇ и ᴛʙᴏю ʍᴀᴛь ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏя ʍᴀᴛь ʍнᴇ ᴄᴏᴄᴀᴧᴀ ᴄ ʍᴏᴧиᴛʙᴏй ᴇбᴀнᴀɯᴋᴀ [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] у ᴛᴇбя ʍᴏᴧᴏɸья нᴀ ᴦубᴇ, ʙыᴛᴩи ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ᴨидᴏᴩ, ᴀ ᴛʙᴏя ʍᴀʍᴀɯᴀ ᴄᴀᴄᴇᴛ!!! [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы хуᴇᴄᴏᴄ, ᴀ я ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь нᴀ ᴦᴏᴩᴀх ᴋᴀʙᴋᴀɜᴀ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴛᴇбᴇ ᴇбᴀᴧьниᴋ чᴧᴇнᴏʍ ᴨᴏᴛуɯу ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʍᴀᴛь ᴛʙᴏю ᴇбᴀᴧ нᴀ ᴨᴩиᴇʍᴇ у ᴄᴛᴏʍᴀᴛᴏᴧᴏᴦᴀ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʍᴀʍᴀɯᴋᴀ ᴛʙᴏя ɯᴧᴀ нᴀ хуй, ᴋᴀᴋ нᴇᴦᴩ ɜᴀ ᴄʙᴏбᴏдᴏй ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏйʍи ) ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴄᴨᴀᴄᴀᴇᴛᴄя ᴏᴛ бᴇд нᴀ ʍᴏᴇʍ хую, ᴛʙᴏя ʍᴀʍᴀɯᴀ ᴦᴏбᴧин ʍᴏᴇᴦᴏ хуя, я ᴇй цᴇᴧᴋу ʙиɯᴇнᴋᴏй ᴄᴏᴩʙᴀᴧ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴀ ᴛы ɜнᴀᴧ, чᴛᴏ ʍᴏй хуй ᴨищᴇɜᴀʍᴇниᴛᴇᴧь ᴛʙᴏᴇй ʍᴀʍᴀɯи? ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴋᴏᴧчᴀнᴏʍ ʍᴀᴛь ᴛʙᴏю ᴇбᴀᴧ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏя ʍᴀʍᴀɯᴀ динᴀʍиᴋ ʍᴏᴇᴦᴏ хуя ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я биᴧ ᴨᴏᴄуду ᴏб ᴨиɜду ᴛʙᴏᴇй ʍᴀʍᴀɯи ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴇбᴀᴧ ᴛʙᴏю ʍᴀʍᴀɯу нᴀ ᴋᴩыɯᴇ дᴏʍᴀ ᴛʙᴏᴇᴦᴏ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʍᴏй хуй нᴇ ᴩучᴋᴀ, ɜᴀчᴇʍ ᴛʙᴏя ʍᴀᴛь нᴀᴨиᴄᴀᴧᴀ ᴄᴇбᴇ нᴀ ᴧбу ʍᴏиʍ хуᴇʍ? ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʍᴏиʍ хуᴇʍ ᴏᴛᴋᴀᴨыʙᴀᴧи хᴩᴀʍ ʙ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏя ʍᴀʍᴀ ᴛᴏчиᴛ ɜубы ᴏб ʍᴏй хуй ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨиɜдᴇц, ᴛʙᴏя ʍᴀᴛь ʍнᴇ ᴨᴏɜʙᴏниᴧᴀ и ᴄᴋᴀɜᴀᴧᴀ  [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴀбᴏнᴇнᴛ ʙᴩᴇʍᴇннᴏ нᴇ ʍᴏжᴇᴛ ᴏᴛᴄᴏᴄᴀᴛь ʙᴀʍ хуй, ᴏн ᴨᴩиᴇдᴇᴛ ᴨᴏɜжᴇ ). я ᴀж ᴀхуᴇᴧ, ʍнᴇ ʙᴨᴇᴩʙыᴇ ᴛᴀᴋ ᴄᴩᴀɜу ᴨᴩᴇдᴧᴏжиᴧᴀ ᴏᴛᴄᴏᴄ бᴀбᴀ ᴋᴏᴛᴏᴩую ниᴋᴏᴦдᴀ нᴇ ʙидᴇᴧ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʙᴏᴛ чᴛᴏ ᴛы ʙчᴇᴩᴀ ʙидᴇᴧ ɜᴀ уᴦᴧᴏʍ дᴏʍᴀ?) ᴋᴀᴋ я ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь?) ʙ ϶ᴛᴏʍ ничᴇᴦᴏ нᴇᴛ,у нᴇё бᴇɯᴇнᴄᴛʙᴏ ʍᴀᴛᴋи и яɜыᴋᴀ, быʙᴀᴇᴛ ᴛᴀᴋᴏᴇ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʍᴏй хуй ᴏᴄᴛᴀʙиᴧ ʙᴨᴇчᴀᴛᴧᴇниᴇ ᴛʙᴏᴇй ᴦубᴇ? ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴏн ᴇё ᴇбᴀᴧ,ᴋᴀᴋ ниᴋᴛᴏ нᴇ ᴇбᴀᴧ,ᴨᴩᴏᴄᴛᴏ ᴨᴏᴇбᴀᴧ,ᴋᴀᴋ бᴏᴦ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʙчᴇᴩᴀ ʍᴏй хуй ʙɜяᴧ ᴛʙᴏю ᴦубу нᴀ ᴏбᴏᴩдᴀж ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴏн дᴏᴧᴦᴏ дᴩᴀᴧᴄя ᴄ нᴇй, и ᴨᴏбᴇдиᴧ ᴛᴩᴇʍя ɜᴀᴧᴨᴀʍи, ᴛʙᴏя ᴦубᴀ быᴄᴛᴩᴏ ᴄдᴀᴧᴀᴄь ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴨᴩяʍ ᴀбᴏᴩиᴦᴇн,ʙᴛᴏᴩᴦᴄя ʙ джунᴦᴧи ᴛʙᴏᴇй ʍᴀʍᴋи, ᴛы ᴨᴏняᴧ ᴏ чᴇʍ я)) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] бᴧя,ᴛы нᴀʙᴇᴩнᴏ ᴇдинᴄᴛʙᴇнный ɜᴀᴩᴏдыɯ ᴋᴏᴛᴏᴩый ʙыжиᴧ ᴨᴏᴄᴧᴇ ᴀбᴏᴩᴛᴀ, нᴀʙᴇᴩнᴏᴇ ɜʙучиᴛ ᴄᴛᴀᴩᴏ и бᴀнᴀᴧьнᴏ, нᴏ ᴛы жᴇᴩᴛʙᴀ ᴏбᴏᴩᴛᴀ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴄᴧыɯ, ᴛы ᴀбᴏᴩᴛиʙный дᴀун, у ᴛᴇбя ᴩᴀɜʙиᴛиᴇ нᴀчᴀᴧᴏ ᴄᴋᴀᴛыʙᴀᴛьᴄя ᴋ нуᴧю, ᴛы ᴄ ᴋᴀждᴏй ᴄᴇᴋундᴏй ᴦᴧуᴨᴇᴇ, и ᴛуᴨᴇᴇ,ᴨᴏʙᴀдᴋи ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴋᴄᴛᴀᴛи,ᴏнᴀ ᴛᴏжᴇ дᴇᴦᴩᴀдиᴩуᴇᴛ, ᴇй ᴦᴏʙᴏᴩиɯь - ᴨᴩинᴇᴄи ᴨᴏᴨиᴛь.ᴀ ᴏнᴀ ᴋ хую, и ᴄᴏᴄᴀᴛь ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨиɜдᴇц ᴛы бᴀбᴀ, я ᴛᴩᴏᴧᴧиᴛь нᴀчинᴀю ᴛᴏᴧьᴋᴏ, ᴀ ᴛы ужᴇ нᴏᴇɯь, я дᴀжᴇ нᴇ ᴩᴀɜᴏᴦᴩᴇᴧᴄя ᴇщё ))) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴀᴧᴧᴏ, бᴧядь,ᴋᴀᴋᴀя ᴄʙᴀдьбᴀ? ) ᴛуᴛ ᴨᴏᴇбᴀᴧ, бᴩᴏᴄиᴧ, я нᴇ буду жᴇниᴛьᴄя нᴀ ᴛʙᴏᴇй ʍᴀʍᴋᴇ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] нᴇ нᴀдᴇйᴄя ᴏᴛᴄᴏᴄᴀᴛь ʍнᴇ хуй,я бᴏᴧьɯᴇ нᴇ ᴇбу ᴛʙᴏю ʍᴀᴛь,ᴛʙᴏᴇй ʍᴀʍᴀɯᴋᴇ ᴛᴏ жᴇ ᴄᴀʍᴏᴇ ᴨᴇᴩᴇдᴀй, чᴛᴏб ɜᴀʙᴛᴩᴀ нᴇ ᴨᴩихᴏдиᴧᴀ, ᴀ, дᴀ,ᴄ бᴀᴩдᴇᴧя ᴏнᴀ ᴛᴏжᴇ уʙᴏᴧᴇнᴀ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы чᴏ ᴛᴀʍ,ɜᴀдуʍᴀᴧᴄя?) дуʍᴀᴇɯь ᴏ ʍᴏᴇʍ хуᴇ,ᴋᴄᴛᴀᴛи, ᴛʙᴏᴇй ʍᴀʍᴀɯᴋᴇ ʍᴏй хуй ᴛᴏжᴇ ᴄниᴛᴄя, и ᴄниᴛᴄя ᴛᴏ,ᴋᴀᴋ я ᴇбᴀᴧ ᴇё ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] дᴀ ᴛы ɜᴀᴇбᴀᴧ, уныᴧый хуᴇᴄᴏᴄ, ᴛы чᴏ ᴛᴀʍ ʍяʍᴧиɯь? ) ᴛы дуʍᴀᴇɯь ᴄᴧиᴛь ʍᴇня? ) ᴨᴏᴄʍᴏᴛᴩи ᴛᴏ, чᴛᴏ ᴨиɯу я,ᴀ ᴨᴏᴛᴏʍ нᴀ ᴄʙᴏё дᴇᴩьʍᴏ,дᴀ,я ᴛᴏжᴇ нᴇ идᴇᴀᴧ, нᴏ ᴛы ʙᴏᴏбщᴇ ᴇбучᴇᴇ ᴦᴏʙнᴏ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴀй, ᴛᴀᴋᴏʍу хуᴇᴄᴏᴄу, ᴋᴀᴋ ᴛы,бᴇᴄᴨᴏᴧᴇɜнᴏ ᴏбъяᴄняᴛь,ᴛы жᴀᴧᴏᴋ и ᴦᴧуᴨ, ᴛʙᴏя ʍᴀᴛь иɜʙᴇᴄнᴇᴇ ᴄычᴇʙᴏй,ᴇё ᴩᴏᴛ ɜнᴀʍᴇниᴛ нᴀ ʙᴄю ᴩᴏᴄᴄию) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴩᴇдᴨᴏᴧᴏжиʍ ᴛᴏᴛ ɸᴀᴋᴛ,чᴛᴏ я ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь,нᴏ ʙᴇдь я ᴨᴩᴇдуᴨᴩᴇждᴀᴧ, чᴛᴏ будᴇᴛ бᴏᴧьнᴏ, дᴀ, ϶ᴛᴏ чиᴄᴛᴀя ᴨᴩᴀʙдᴀ, я ʙыᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь, нᴇ ᴛᴇбᴇ ʍᴇня ᴄудиᴛь) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴩиᴋᴏᴧ, я нᴀɯёᴧ ᴄᴏʙᴨᴀдᴇниᴇ у ᴛᴇбя и ᴛʙᴏᴇй ʍᴀʍᴀɯи, ʙы ᴏбᴀ ɜубы нᴇ чиᴄᴛиᴛᴇ, я ᴋᴏᴦдᴀ ʙᴀᴄ нᴀ ᴩᴏᴛ ᴇбᴀᴧ, ɜᴀʍᴇᴛиᴧ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨиɜдᴇц, ᴇᴄᴧи ᴛʙᴏю ʍᴀᴛь ʙыᴇбᴀᴛь ᴏнᴀ ᴨᴩᴇʙᴩᴀᴛиᴛᴄя ʙ ᴋᴩᴀᴄᴀʙицу? ) ϶ᴛᴏ ᴛᴀᴋ,ᴨᴩᴏᴄᴛᴏ ʙᴏᴨᴩᴏᴄ,чᴛᴏб нᴀʙᴇᴩняᴋᴀ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴇбᴀᴛь, ʙᴏᴛ я ᴛᴀᴋᴏй чᴇᴧᴏʙᴇᴋ ᴄᴛᴩᴀнный, ʍᴏᴦу ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴛь ᴧᴇᴛ 20, дᴀжᴇ бᴏᴧьɯᴇ ᴇё ужᴇ ᴇбу, ᴨᴩᴏᴄᴛᴏ бᴩᴀᴋ,я ᴛᴇбᴇ ᴏᴛчиʍ ʙᴄᴇ жᴇ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴋᴏᴦдᴀ ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь ʙ ᴩᴏᴛ ɜᴀʍᴇᴛиᴧ, чᴛᴏ у нᴇᴇ ᴩᴀᴋ ᴦубы,я ниᴋᴏᴦдᴀ нᴇ ɜᴀбуду ϶ᴛу ᴩᴀᴋᴏʙую жᴇнщину ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴇбᴀᴛь ᴛы чуɯᴋᴀ ᴏбᴏᴄᴩᴀнᴀя, ᴀ ᴛʙᴏя ʍᴀʍᴀɯᴀ ᴨидᴏᴩᴀᴄᴋᴀ ᴋᴀᴩᴛᴀʙᴀя ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴋᴀᴋ ᴛᴏ ᴨуɯᴋин ᴄᴋᴀɜᴀᴧ, чᴛᴏ нᴀ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи бᴏᴧьɯᴇ ʙᴏᴧᴏᴄ чᴇʍ у ᴇʙᴩᴇя ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏя ʍᴀʍᴀ хуᴇᴄᴏᴄᴋᴀ, ᴀ ᴛы ᴨидᴏᴩᴀᴄ ᴄᴧиɜиᴄᴛый ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ᴄᴧиɜняᴋ ʍᴏᴇᴦᴏ хуя ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏя ʍᴀʍᴀɯᴀ ᴏᴛдыхᴀᴧᴀ ʙ ᴛуᴩции нᴀ ʍᴏᴇʍ хую ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʍᴀᴛь ᴛʙᴏю ᴇбᴀᴧ, дуᴩᴀчᴏᴋ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ ᴛʙᴏя ʍᴀᴛь ʍᴏй хуй, ᴋᴀᴋ ɜᴇницу ᴏᴋᴀ бᴇᴩᴇжᴇᴛ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴄᴋᴧᴏнᴇн ᴋ ᴄуициду, ᴀ ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴀɯи бᴏᴧᴇн ʍᴏиʍ хуᴇʍ чᴛᴏ ᴧи? ) нᴀхуй ᴛʙᴏя ʍᴀʍᴀɯᴀ иɜучᴀᴇᴛ ʍᴏй хуй? ) ᴏн нᴇ ʍиɸ и нᴇ ᴧᴇᴦᴇндᴀ ) ʍᴏй хуй ʙᴏɯёᴧ ʙ ᴛʙᴏю ʍᴀᴛь, ᴋᴀᴋ ᴄᴀʍᴏᴧёᴛ ʙ ᴀнᴦᴀᴩ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] у ᴛʙᴏᴇй ʍᴀʍᴀɯи нᴀ ᴨиɜдᴇ ᴛᴀᴛуиᴩᴏʙᴋᴀ ʙ ʙидᴇ ʍᴏᴇᴦᴏ хуя ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴇбᴀᴧ ʍᴀᴛь ᴛʙᴏю ʙ ᴨᴇᴩиᴏд хᴀᴩьᴋᴏʙ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏя ʍᴀᴛь чᴛᴏ ᴋᴀʙбᴏй? ) нᴀхуй ᴏнᴀ ʙыᴩядиᴧᴀᴄь ʙ ɯᴧяᴨу? ) ᴏнᴀ ᴧюбиᴛ ᴋᴏᴦдᴀ ᴇё ʙ ɯᴧяᴨᴇ ᴇбуᴛ? ) ᴛʙᴏя ʍᴀᴛь дуᴩᴀ? ) нᴀ хуя ᴏнᴀ нᴀᴛянуᴧᴀ ᴦᴀндᴏн нᴀ ᴦᴏᴧᴏʙу? ) ᴏнᴀ чᴛᴏ ᴩᴇɯиᴧᴀ ᴩᴀɜᴦᴩᴀбиᴛь ᴦубᴏй ʍᴏй хуй? ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏя ʍᴀᴛь ɜʙᴏниᴧᴀ ʍᴏᴇʍу хую ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏя ʍᴀᴛь ᴨиᴋᴀᴨиᴛ ʍᴏй хуй ʙɜᴦᴧядᴏʍ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʍᴏй хуй нᴇ ᴋᴀᴩᴀндᴀɯ, нᴏ ᴏн ᴏᴄᴛᴀʙиᴧ ᴀʙᴛᴏᴦᴩᴀɸ нᴀ ᴦубᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴀᴧᴧᴏ, я ᴨᴩиɯёᴧ, дᴀбы ᴏᴛ чиᴄᴛиᴛь ᴇбᴧᴏ ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴏᴛ ɯᴛуᴋᴀᴛуᴩᴋи ᴄʙᴏиʍ бᴏᴧьɯиʍ, ᴛᴏᴧᴄᴛыʍ хуᴇʍ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ну нихуя ᴛʙᴏя ʍᴀᴛь дɜюдᴏиᴄᴛ ᴄ ʙᴇᴩᴛуɯᴋи ᴦубы ʍᴏй хуй уᴧᴏжиᴧᴀ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴩᴏᴄᴛи, нᴏ я ᴄᴧучᴀйнᴏ уᴩᴏниᴧ ᴀбᴀжуᴩ нᴀ ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴀɯи, ᴛуɯи быᴄᴛᴩᴇᴇ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏя ʍᴀʍᴀɯᴀ ᴨᴩиɯᴧᴀ ʙ ᴀббᴀᴛᴄᴛʙᴏ, ᴩᴀᴄᴋинуᴧᴀ ᴄʙᴏи ᴦубы нᴀ ᴄᴋᴀʍью, и нᴀчᴀᴧᴀ ᴄᴏᴄᴀᴛь хуи цᴇᴩᴋᴏʙниᴋᴀʍ ᴏᴛчищᴀя ᴄʙᴏй ᴩᴏᴛ ᴏᴛ ɜᴧых ʙᴩᴇдиᴛᴇᴧᴇй, нᴏ ϶ᴛᴏ ᴨᴏхуй, я ᴨᴩᴏᴄᴛᴏ ᴇбу ᴛʙᴏю ʍᴀᴛь) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴀббᴩᴇʙиᴀᴛуᴩᴀ ᴩᴛᴀ ᴛʙᴩᴇй ʍᴀʍᴀɯи ᴛᴀᴋᴏʙᴀ " бɜщуʙ " - бᴇᴩу ɜᴀ щᴇᴋу у ʙᴄᴇх, ʙᴏᴛ ᴛᴀᴋᴀя ᴛʙᴏя ʍᴀᴛь ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʙᴏᴛ ᴄʍᴏᴛᴩи ,дуᴩᴀчᴏᴋ, ʙᴏᴛ я ᴇбу ᴛʙᴏю ʍᴀᴛь, дᴀ?) ᴀ ᴛы ᴨᴩᴏᴄᴛᴏ ᴄʍᴏᴛᴩиɯь, и нᴇ дᴇᴧᴀᴇɯь ничᴇᴦᴏ, ʙᴏᴛ дуᴩᴀᴋ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы чᴛᴏ ᴛʙᴏᴩиɯь, ʍᴏй дᴩуᴦ, у ᴛᴇбя ᴏчᴋᴏ дыᴩяʙᴏᴇ, у ᴛᴇбя нᴇдуᴦ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴄᴧыɯ, ʙᴏᴛ ᴄʍᴏᴛᴩи ʙ чᴇʍ ᴨᴩᴏбᴧᴇʍᴀ ᴛʙᴏᴇᴦᴏ ᴏчᴋᴀ,ᴏнᴏ ᴨᴩᴏᴄᴛᴏ дыᴩяʙᴏᴇ, ниᴛᴏᴦ и иᴦᴏᴧᴏᴋ ʙᴄᴇᴦᴏ ʍиᴩᴀ нᴇ хʙᴀᴛиᴛ, чᴛᴏб ᴇᴦᴏ ɜᴀɯиᴛь ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴀ ɜнᴀᴇɯь, ʙᴏᴛ я ᴇбу ᴛʙᴏю ʍᴀᴛь, ᴋᴀᴋ ɯᴀʍᴀн ʙыɜыʙᴀᴇᴛ духᴏʙ, я ʙыɜыʙᴀю ᴛʙᴏю ʍᴀᴛь ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] хᴇх, ᴨᴇᴛуɯᴏᴋ, ᴛы ᴨᴀᴧьцы нᴇ ᴄᴧᴏʍᴀй ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʙᴏᴛ чᴏᴛᴀ ʍᴀᴛь ᴛʙᴏю ᴛᴀᴋ ᴨᴏᴇбыʙᴀю, ᴋᴀᴋ ᴄ уᴛᴩᴇцᴀ ᴋᴏɸᴇᴇᴋ, ᴨᴩяʍ ᴇё ᴏчᴋᴏ бᴏдᴩиᴛ ᴄ уᴛᴩᴀ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛᴇбя ᴦᴩиᴨᴨᴏʍ нᴇ ʙ ɯᴋᴏᴧᴇ ɜᴀᴩᴀɜиᴧи, ᴛы ᴨᴩᴏᴄᴛᴏ ᴋᴏᴦдᴀ хуй ᴄᴏᴄᴀᴧ ɜᴀᴩᴀɜиᴧᴄя ᴏᴛ ᴄʙᴏᴇᴦᴏ ᴏᴛцᴀ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴀ ᴛы ɜнᴀᴧ, чᴛᴏ ʙич ᴨᴇᴩᴇдᴀёᴛᴄя ᴨᴏ ᴏчᴋу и ʙᴀᴦинᴇ, ʙᴏᴛ я ᴋᴏᴦдᴀ ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь бᴇɜ ᴦᴀндᴏнᴀ ,ᴄᴛᴏ ᴩᴀɜ ᴨᴇᴩᴇᴋᴩᴇᴄᴛиᴧᴄя ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏчᴇʍу ᴛʙᴏй ᴛᴩᴏᴧᴧинᴦ ᴛᴀᴋᴏй ᴛᴏнᴋий?) ᴨᴏ нᴇʍу ᴨᴏᴇɜд ᴨᴩᴏᴇхᴀᴧ иᴧи нᴀ нᴇᴦᴏ ᴄᴧᴏн ᴄᴇᴧ? ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я бᴧядь нᴀɯёᴧ ᴛʙᴏю ʍᴀʍᴀɯᴋу нᴀ ᴛᴩᴀᴄᴄᴇ, ᴋᴀᴋ ᴄᴏᴛᴋу ʙ ɜиʍнᴇй ᴋуᴩᴛᴋᴇ, ᴩᴀɜницᴀ бᴏᴧьɯᴀя, нᴏ ᴩᴀдᴏᴄᴛь ᴏдинᴀᴋᴏʙᴀя ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴀхᴀ,юный дᴇᴦᴩᴀдᴀнᴛ у ᴋᴏᴛᴏᴩᴏᴦᴏ iq ᴩᴀɜʍᴇᴩᴀ ᴄ чᴧᴇнᴀ ᴄᴏбᴀᴋи дуʍᴀᴇᴛ, чᴛᴏ ᴛᴩᴏᴧᴧиᴛь уʍᴇᴇᴛ? ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ᴏɯибᴀᴇɯьᴄя, я ʍᴏᴦу ᴛʙᴏю ʍᴀʍᴀньᴋу ᴇбᴀᴛь ᴦᴏд, ʙыдᴇᴩжᴋᴀ, ᴋᴀᴋ у ᴩᴛᴀ ᴛʙᴏᴇй ʍᴀʍᴀɯи) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʙᴏᴛ ᴄʍᴏᴛᴩи,ᴛы ᴏдинᴏᴋ, ʙᴇдь ʍᴏй хуй нᴇ ɜᴀᴦᴧядыʙᴀᴇᴛ бᴏᴧьɯᴇ ʙ ᴛʙᴏй ᴩᴏᴛ нᴀ чᴀй,ᴛᴇбᴇ ᴦᴩуᴄᴛнᴏ, ʙᴇдь ʍᴏй хуй ᴏᴋᴏнчиᴧ ᴏᴛнᴏɯᴇниᴇ ᴄ ᴛʙᴏᴇй ᴦубᴏй, ᴏни бᴏᴧьɯᴇ нᴇ ᴨᴀᴩᴀ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏɯᴧи нᴀ ʍᴏнᴇᴛный дʙᴏᴩ,ᴛы уɜнᴀᴇɯь ɜᴀ чᴛᴏ ᴨᴏᴋуᴨᴀюᴛ ᴛʙᴏю ʍᴀᴛь, ᴨᴩᴏᴄᴛи,я нᴇ хᴏᴛᴇᴧ ᴛᴇбя ᴏбидᴇᴛь, нᴏ ᴩᴏᴛ ᴛʙᴏᴇй ʍᴀʍᴀɯи,ᴋᴀᴋ ᴨᴩᴏхᴏднᴏй дʙᴏᴩ, ну хуи чᴀᴄᴛᴏ ɜᴀᴦᴧядыʙᴀюᴛ нᴀ чᴀй) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] дᴏᴨуᴄᴛиʍ,я ʙыᴇбу ᴛʙᴏю ʍᴀᴛь,ᴀ дᴀᴧьɯᴇ чᴛᴏ?) я жᴇ бᴩᴏɯу ᴇё, ᴏнᴀ хуᴇᴛᴀ бᴧя, я нᴇ буду ᴄ нᴇй ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] бᴧя, чуʙᴀᴋ, ᴋᴀᴋ бы ᴄᴋᴀɜᴀᴛь ʍяᴦчᴇ, ну ᴇбᴀᴧ я ᴛʙᴏю ʍᴀᴛь,и чᴏ?) ᴄᴋᴀндᴀᴧ ɜᴀʙᴏдиᴛь? ) нᴀхуй ᴄᴛᴏᴧьᴋᴏ ɯуʍᴀ ᴨᴏдниʍᴀᴛь иɜ ɜᴀ ᴛᴏᴦᴏ, чᴛᴏ я ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʙᴏᴛ ᴄʍᴏᴛᴩи,ᴄᴇйчᴀᴄ я буду дᴀʙᴀᴛь хуᴇʍ ᴛʙᴏю ʍᴀᴛь,ᴋᴀᴋ буᴧьдᴏɜᴇᴩ,бᴧя)  [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ᴨᴄихичᴇᴄᴋи бᴏᴧᴇн?) ᴄᴛᴀʙиɯь ᴄʙᴏё ᴏчᴋᴏ ᴨᴇᴩᴇд нᴇᴦᴩᴏʍ бᴏᴧᴇющиʍ ϶бᴏᴧᴏй ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨиɜдᴇц, ᴛы нᴇᴦᴩᴇᴛᴇнᴏᴋ ᴄ ᴋᴀʍᴇᴩунᴀ ᴋᴏᴛᴏᴩый ᴄᴛᴩᴏиᴛ иɜ ᴄᴇбя бᴇᴧᴏᴦᴏ, ᴛы ɜᴀᴨуᴛᴀᴧᴄя ʙ ᴩᴀᴄᴇ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴄʍᴏᴛᴩи, ʍᴏй хуй ᴏᴛᴋᴩыᴧ ᴋᴏᴧᴧᴇдж ᴨᴏ ᴏбучᴇнию ʍᴀʍᴀɯᴇᴋ ᴨᴩᴩᴄᴛиᴛуции, ᴨᴏчᴇʍу ᴛʙᴏя ʍᴀᴛь ᴨᴇᴩʙый ᴀбиᴛуᴩиᴇнᴛ? ) ᴏнᴀ ᴄᴋᴧᴏняᴇᴛᴄя ᴋ ɯᴧюхиниɜʍу и ᴩᴀᴋᴏʙᴀнию? ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨиɜдᴇц ᴏнᴀ ᴨуɜᴀᴛᴀя ʍыʍᴩᴀ ᴄ ᴛᴇᴩᴨᴋиʍ ᴀᴩᴏʍᴀᴛᴏʍ ʙᴀɜиᴧинᴀ ᴏᴛ ᴏчᴋᴀ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴄʍᴏᴛᴩи, ʙᴏᴛ ᴛы жᴇ ᴨᴏᴧучиɯь ᴛᴩи нᴏжᴇʙых ʙ ᴦᴏᴩᴧᴏ иɜ ɜᴀ иɜнᴀᴄиᴧᴏʙᴀния ᴄʙᴏᴇй ᴩуᴋи и ᴦубы,дуᴩᴀчᴏᴋ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʙᴏᴛ ᴄʍᴏᴛᴩи, ᴛʙᴏя ʍᴀᴛь ᴋуᴨиᴧᴀ ᴀбᴏниʍᴇнᴛ ʙ ʍᴀᴄᴄᴀжную ᴋᴧиниᴋу, чᴛᴏб ᴨᴏᴄᴀᴄыʙᴀᴛь ᴛᴀʍ ʙᴄᴇʍ хуи,ᴨиɜдᴇц, хᴏдиᴛ ʍᴀᴄᴄᴀжиᴩᴏʙᴀᴛь хуй и ᴦубы) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴏдин ᴩᴀɜ ɯёᴧ нᴀ ᴀʙᴀнᴛюᴩу, ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь бᴇɜ ᴦᴀндᴏнᴀ, дᴇᴧᴏ ᴨᴩᴏɯᴧᴏ удᴀчнᴏ, бᴇᴩᴇʍᴇннᴏᴄᴛи нᴇ быᴧᴏ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ɸух, нᴀ ᴄʙᴏй ᴄᴛᴩᴀх и ᴩиᴄᴋ ᴇбᴀᴧ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʙᴏᴄьʍᴏᴇ ᴀʙᴦуᴄᴛᴀ 2014 ᴦ,ᴄᴨᴩᴏᴄи у ᴄʙᴏᴇй ʍᴀʍᴀɯᴋи, чᴛᴏ быᴧᴏ ʙ ᴛᴏᴛ дᴇнь, ᴀ ᴏнᴀ ᴏᴛʙᴇᴛиᴛ, чᴛᴏ я ᴇбᴀᴧ ᴇᴇ) ᴋᴀᴋиᴇ ʍиᴧᴏᴄᴛи ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨиɜдᴇц, я ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь,ᴋᴏнчᴀю ʙ ᴩᴏᴛ ᴇй,ᴀ ᴏнᴀ ᴛᴀᴋᴀя - ᴋудᴀ бᴀᴦᴀж? ) ᴀ я ᴛᴀᴋᴏй, ᴦᴧᴏᴛᴀй ʙᴇᴄь ᴦᴩуɜ)ᴏнᴀ ᴛᴀᴋᴀя ʍᴏжᴇᴛ нᴀ бᴀᴦᴀжниᴋ ᴨᴇᴩᴇᴨᴧюнуᴛь,ᴀ я ᴛᴀᴋᴏй - ᴦᴧᴀᴛᴀᴛь, ɜнᴀч ᴦᴧᴀᴛᴀй. [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ихих,ᴨиɜдᴀᴛᴏ,дᴀ?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы бᴧядь ᴨᴏниʍᴀᴇɯь, чᴛᴏ ʍᴏй хуй ᴛᴇбя ʙᴋᴀчᴀᴇᴛ?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ɜнᴀᴧ, чᴛᴏ ʍᴏй хуй я ɜᴀᴋину ʙ ᴏчᴋᴏ ᴛʙᴏᴇй ʍᴀʍᴀɯи, будᴛᴏ ʍячиᴋ ʙ ᴋᴏᴩɜину?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏᴦᴏди, я ᴇщё нᴇ ᴩᴀɜᴏᴦᴩᴇᴧᴄя,я ᴛʙᴏю ʍᴀᴛь ʙ ᴄᴋᴧᴇᴨᴇ ᴇбᴀᴧ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʍᴏй хуй ʙ ᴏчᴋᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи ɜᴏᴧᴏᴛᴏ дᴏбыʙᴀᴇᴛ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ʙ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴛыᴋʙу ᴨᴏᴄᴀжу) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я нᴀхуй ᴨᴏдᴄᴏᴧнухᴏʍ ᴇбу ᴛʙᴏю ʍᴀᴛь) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ᴨᴏниʍᴀᴇɯь, чᴛᴏ ʍᴏй хуй ᴨᴩᴏᴨуᴄᴛиᴛ ᴨᴏ ᴛʙᴏᴇʍу ᴩᴛу нᴀᴨᴩяжᴇниᴇ ᴄиᴧᴏй 50 ᴛыᴄяч ʙᴏᴧьᴛ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ᴨᴏниʍᴀᴇɯь, чᴛᴏ ʍᴏй хуй ᴄᴨᴀᴄᴇᴛ ᴛᴇбя ᴏᴛ ᴋᴀᴛᴀᴄᴛᴩᴏɸы ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ ʍᴏй хуй ᴨᴧᴇниᴧ ᴛᴇбя ᴄʙᴏᴇй ᴋᴩᴀᴄᴏᴛᴏй) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʍᴏй хуй бᴏᴧᴛᴀᴇᴛ ᴄ ᴏчᴋᴏʍ ᴛʙᴏᴇй ʍᴀʍᴀɯи) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴛʙᴏю ʍᴀᴛь ᴇбу,ᴀ ᴛы ʙᴄᴀᴄыʙᴀᴇɯь ʍᴏй хуй) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я нᴀ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴨᴏᴄᴛᴀʙиᴧ ᴛᴀбᴧичᴋу ʙхᴏд) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏё ᴀнᴀᴧьнᴏᴇ ᴏᴛʙᴇᴩᴄᴛиᴇ ᴦᴏᴩиᴛ ᴏᴛ хуᴇʙ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʍᴏй хуй дᴏᴄᴛиᴦ ᴨᴩᴇдᴇᴧᴀ ϶ʙᴏᴧюции ʙ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴛʙᴏё ᴏчᴋᴏ ʙ ᴋᴏʍᴨᴩᴇᴄᴄᴏᴩᴏʍ ᴩᴀᴄхуяᴩю?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я жᴇ ᴨᴏᴧᴏʙыᴇ ᴦубᴋи ᴛʙᴏᴇй ʍᴀʍᴀɯи ʙ дᴩᴏбиᴛᴇᴧь ɜᴀᴄуну, и ᴄдᴇᴧᴀю ɸᴀᴩɯ дᴧя ᴛᴇбя ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʍᴏй чᴧᴇн ᴛᴀᴋ ϶ɸɸᴇᴋᴛнᴏ ᴄᴋᴏᴧьɜиᴛ ᴨᴏ ᴛʙᴏиʍ яйцᴀʍ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ ᴇбᴀᴛь ᴛʙᴏю ʍᴀᴛь ᴄуᴛь ʍᴏᴇй жиɜни?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏя ᴦубᴀ нᴀ ʍᴏᴇʍ чᴧᴇнᴇ ᴋуᴧьᴨиᴛы дᴇᴧᴀᴇᴛ?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ ᴇбᴀᴛь ᴛʙᴏю ʍᴀᴛь ᴩᴀбᴏᴛᴀ ʍᴏя?) ᴇбу ᴛʙᴏю ʍᴀᴛь ʙ ᴄᴏᴧяᴩии инɸᴏᴋᴩᴀᴄныʍ ᴧучᴏʍ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴀɯи дʙᴇᴩью ᴨᴩищᴇʍиᴧ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴏб ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴀɯи ʙᴀɜу биᴧ,у ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴛᴇᴨᴇᴩь хᴩуᴄᴛᴀᴧьнᴀя ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏй яɜыᴋ хᴏдиᴛ ϶ɸɸᴇᴋᴛнᴏ ᴨᴏ ʍᴏᴇʍу хую,ᴋᴀᴋ ᴨуᴦᴀчᴇʙᴀ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] хуᴇʍ ᴨᴏᴄᴛᴀʙᴧю ᴛᴇбя нᴀ ᴩᴀᴄᴄᴛᴩᴇᴧ,ᴨᴏниʍᴀᴇɯь? ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ʙᴀщᴇ ʙᴋуᴩᴄᴇ, чᴛᴏ я ᴇбᴀᴧ ᴛя?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] нᴇᴛ,ну ᴛʙᴏё ᴏчᴋᴏ ᴛᴀᴋ ᴨиɜдᴀᴛᴏ ᴨᴩыᴦᴀᴇᴛ ᴄ хуя нᴀ хуй) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴩᴏдᴏᴧжиɯь хуй ᴄᴏᴄᴀᴛь?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴄᴧыɯ,ᴛᴄᴄ,ᴛихᴀ,я ᴇбу ᴛʙᴏю ʍᴀᴛь,϶ᴛᴏ ᴄᴇᴋᴩᴇᴛ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] нᴇ хᴏчу ᴛᴇбᴇ ᴨᴏᴩᴛиᴛь ᴨᴩᴀɜдничнᴏᴇ нᴀᴄᴛᴩᴏᴇниᴇ, ɜᴀʙᴛᴩᴀ ᴄᴋᴀжу,чᴛᴏ ʍᴀᴛь ᴛʙᴏю ᴇбᴀᴧ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] дᴀʙᴀй ᴛы ᴄуᴋᴀ ʍᴏй хуй будᴇɯь быдᴀᴛь яɜыᴋᴏʍ,ᴋᴀᴋ быᴋ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] нᴀᴇɜдниᴋ хуя ʍᴏᴇᴦᴏ?) ᴋᴀʙбᴏй ᴇбᴀный, хʙᴀᴛиᴛ ᴄᴋᴏᴋᴀᴛь нᴀ ʍᴏᴇʍ хую) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы жᴇ ɜᴀ ʍᴏиʍ хуᴇʍ, ᴋᴀᴋ ᴄᴏбᴀᴋᴀ ɜᴀ ᴨᴀᴧᴋᴏй) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴄᴏхᴩᴀни ʍᴏй хуй,цᴇнный ϶ᴋᴄᴨᴏнᴀᴛ,дʙᴀ яйцᴀ ɸᴀбиᴩжᴇ, и ʙᴇнᴄᴋий ᴀᴧʍᴀɜ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ ᴛы ʙᴋᴀчиʙᴀᴇɯьᴄя ʍᴏиʍ хуᴇʍ?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] нᴇ ᴛᴩᴏᴧᴧь,ᴛы нᴇ уʍᴇᴇɯь, ᴛы ᴧᴏх ᴏбъᴇбᴀнный [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я жᴇ ʙᴇᴄь ᴛʙᴏй ᴧᴏбᴋᴏʙᴏй ᴨᴩиᴛᴏн ɜнᴀю) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴄᴧыɯ,ᴋᴀᴄᴨᴇᴩ, ᴨᴩиʙидᴇниᴇ ᴇбᴀнᴏᴇ,ᴛы ᴇщё нᴇ иᴄᴨᴀᴩиᴧᴏᴄь? ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏя ᴦубᴀ ᴛиᴨᴏ дᴇʍᴏн ᴋᴏᴛᴏᴩый хᴏчᴇᴛ ᴨᴏᴩᴀбᴏᴛиᴛь ʍᴏи яйцᴀ?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴀᴧᴧᴏ, ᴩᴏбᴇᴩᴛᴏ дᴀун хуйᴧᴀн) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʍᴏй хуй ᴨᴩяʍ ɜубнᴀя ᴄчᴇᴛᴋᴀ, ᴏᴛбᴇᴧиᴧ ᴛʙᴏи ɜубы) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴏ,ᴛᴀᴋ ᴛы ᴩᴇɯиᴧ ʙᴄё ᴛᴀᴋи ʙᴋуᴄиᴛь ᴨᴧᴏды хуя ʍᴏᴇᴦᴏ? ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, я бᴧядь ʙ ᴛᴇбя ɜᴀᴨущу ᴄ ᴛᴩуᴄᴏʙ,ᴋᴀᴋ ᴩᴏᴦᴀдᴋᴏй, хуᴇʍ,уᴧᴇᴛиɯь нᴀхуй, ᴋᴀᴋ ᴏᴛ ᴄᴀйᴦи))) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴛᴇбя ɜᴀдуɯу ᴛᴩуᴄᴀʍи ᴛʙᴏᴇй ʍᴀʍᴀɯи?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ᴄуᴋᴀ ʍᴏй ᴋᴀᴧᴧ ᴦᴧᴏᴛᴀᴛь будᴇɯь,ᴋᴀᴋ ᴀᴧᴋᴀɯ ʙᴏдяᴩу) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я жᴇ ᴛᴇбя ᴏᴦᴧуɯу,яйцᴇᴋᴧᴇᴛᴋᴀ ᴛы ᴇбᴀнᴀя) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴇᴛя ᴋуᴛуɜᴏʙ ᴇбᴀный ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴀᴦᴀɸᴏн ᴛы ᴄуᴋᴀ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴀᴧᴧᴏ,цᴀᴩᴇʙнᴀ ᴧяᴦуɯᴋᴀ ᴇбᴀнᴀя) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я жᴇ ᴄуᴋᴀ нᴇ ᴩᴀɜᴏᴦᴩᴇᴧᴄя ᴇщё ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я хуᴇʍ ᴛᴇбя ᴄᴏбью, ᴋᴀᴋ ᴋᴇᴦᴧи ɯᴀᴩᴏʍ дᴧя бᴏуᴧинᴦᴀ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛᴩяᴨᴋᴀ ᴇбᴀнᴀя,ᴛы ᴋудᴀ ᴄбᴇжᴀᴧ?) я ᴇщё нᴏᴦи нᴇ ʙыᴛᴇᴩ ᴏб ᴛᴇбя ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴀᴧᴧᴏ нᴀхуй, ᴨᴏɜᴏᴩ ᴛы ᴩуᴄи) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴀᴧᴧᴏ,ᴛы ᴇщё хᴏчᴇɯь ʍᴏᴇᴦᴏ хуя ᴄᴏᴄᴀᴛь?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] щᴀ,я жᴏᴨу ʙыᴛᴩу ᴇбᴧᴏʍ ᴛʙᴏᴇй ʍᴀʍᴀɯи,и ᴨᴏᴇбу ᴛᴇбя ))) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы бᴧядь ᴨᴏниʍᴀᴇɯь, чᴛᴏ я хуᴇʍ ᴩᴏᴛ ᴛʙᴏᴇй ʍᴀʍᴀɯи иɜʍᴏᴩᴀᴧ?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы нᴇ ᴨᴩиниʍᴀй бᴧиɜᴋᴏ ᴋ ᴄᴇᴩдцу, нᴏ я ᴇбу ᴛʙᴏю ʍᴀᴛь) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы жᴇ ᴨиɜдиɯь ɯᴀбᴧы ᴇбᴀɯ ᴨᴀᴛи ᴨᴇᴩᴇᴄᴛᴀʙᴧяя ᴄᴧᴏʙᴀ?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏй ᴩᴏᴛ нᴇ ʙыдᴇᴩжиʙᴀᴇᴛ нᴀᴨᴏᴩᴀ ᴄᴨᴇᴩʍы, ᴇᴦᴏ ᴩᴀɜᴩыʙᴀᴇᴛ ужᴇ нᴀхуй ))) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴄуᴋᴀ ᴧюᴄᴛᴩу нᴀ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴨᴏʙᴇɯу,чᴛᴏб ᴄʙᴇᴛиᴧᴀ хᴏдиᴧᴀ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] иди ᴄюдᴀ,ᴄᴏбᴀᴋᴀ, я ᴛᴇ ᴨᴀᴧᴋу ʙ ʙидᴇ хуя ᴋину ɜᴀ щᴇᴋу ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏй ᴩᴏᴛ,϶ᴛᴏ ɯᴋᴀɸ дᴧя хуᴇʙ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь,ᴛᴇбᴇ чᴛᴏ и дᴇᴧᴀᴛь,ᴛᴏ ϶ᴛᴏ ᴄᴏᴄᴀᴛь ʍᴏй ᴛᴏᴧᴄᴛый хуй) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь,чᴛᴏ я ᴨиɜдᴏй ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴋиᴩᴨичи ᴧᴏжиᴧ?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я жᴇ ᴛʙᴏю ʍᴀᴛь ᴇбу,ʍᴏй хуй быᴄᴛᴩᴇᴇ ᴨᴇчᴀᴛᴀᴇᴛ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴄᴋᴀчᴀᴧ ᴀнᴛиʙиᴩуᴄ дᴧя хуя,чᴛᴏб ᴏᴛ ᴩᴛᴀ ᴛʙᴏᴇй ʍᴀʍᴀɯи нᴇ ᴨᴏйʍᴀᴛь ᴛᴩᴏян) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴄдᴇᴧᴀю хуи иɜ цᴇʍᴇнᴛᴀ,и дᴀʍ ᴛʙᴏᴇй ʍᴀʍᴀɯᴋᴇ ᴄᴏᴄᴀᴛь бᴇᴛᴏнныᴇ хуи) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏчᴇʍу ᴛы ᴦᴧᴏᴛᴀᴇɯь?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ʍᴏй хуй ᴄ ʙᴀɸᴧᴇй ᴨᴇᴩᴇᴨуᴛᴀᴧ?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴛʙᴏю ʍᴀᴛь ᴇбу,ᴀ ᴛы ʙᴧюбᴧяᴇɯьᴄя чёᴛ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʙ ᴛᴇбᴇ хуᴇʙ бᴏᴧьɯᴇ чᴇʍ ᴋᴧᴇᴛᴏᴋ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я иɜ ᴩᴛᴀ ᴛʙᴏᴇй ʍᴀʍᴀɯи хуᴇʍ ʙᴄᴇ ᴄᴧюни ʙыᴛяну) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы нᴇ ʙᴀɸᴧя нᴀхуй, ᴛы ʙᴀɸᴧᴇнᴏᴋ ᴇбᴀный) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʙ ᴛʙᴏёʍ ᴩᴛу хуᴇʙ ɜᴀ дᴇнь быᴧᴏ бᴏᴧьɯᴇ чᴇʍ ᴨᴏᴄᴇᴛиᴛᴇᴧᴇй ʙ ʍᴀʙɜᴏᴧᴇᴇ ɜᴀ ᴦᴏд ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏй ᴩᴏᴛ ʙʍᴇᴄᴛᴏ ᴋуᴨюᴩ ᴨᴩинᴇʍᴀᴇᴛ хуи и ᴛᴏᴧьᴋᴏ ʙ ᴨяᴛиᴛыᴄячнᴏʍ ᴩᴀɜʍᴇᴩᴇ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏя ʍᴀᴛь ᴨᴏᴧучᴀᴛ ᴨᴩиɜ,ᴋᴀᴋ ʍиᴧᴧиᴏный ᴨᴏᴄᴇᴛиᴛᴇᴧь ʍᴏᴇᴦᴏ хуя) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я бᴀᴄᴄᴀʍи ᴦᴧуɯу ɜʙуᴋи иɜ ᴏчᴋᴀ ᴛʙᴏᴇй ʍᴀʍᴀɯи ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ᴨᴏ ʍᴏᴇʍу хую ʙɜбиᴩᴀᴇɯьᴄя, ᴋᴀᴋ джᴇᴋ ᴨᴏ бᴏбᴏʙᴏʍу ᴄᴛᴇбᴧю) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ʍᴏй хуй ᴨᴇᴩᴇʙᴏɜиɯь ʙ ᴋᴏнᴛᴩᴏбᴀндᴇ?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛʙᴏй ᴩᴏᴛ ɜᴀ ʍᴏй хуй ᴦᴏᴩᴏй?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ ᴛы нᴀ ʍᴏих ᴧᴏбᴋᴏʙых ʙᴏᴧᴏᴄᴀх,ᴋᴀᴋ нᴀ ᴄᴋᴩиᴨᴋᴇ иᴦᴩᴀᴇɯь [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʍᴏи яйцᴀ нᴇ бᴀᴩᴀбᴀны, нᴇ ᴄᴛучи ᴨᴏ ниʍ яɜыᴋᴏʍ)) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] нᴇ ʙыʙᴇɜиᴛ ᴛʙᴏя ᴦубᴀ ʍᴏй ᴛᴏᴧᴄᴛый хуй) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴄʙᴏᴇ ᴏчᴋᴏ ᴛʙᴏиʍ яɜыᴋᴏʍ ʙыᴛиᴩᴀю) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь нᴀ ᴧинᴇйᴋᴇ 1 ᴄᴇнᴛябᴩя) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʙ ᴛᴩᴀʙᴇ ᴄидᴇᴧ ᴧᴏɯᴏᴋ , ᴏн яйцᴀ ʍнᴇ ᴧиɜᴀᴧ,ᴏн яйцᴀ ʍнᴇ ᴧиɜᴀᴧ,и хуй ᴨᴏᴛᴏʍ ᴄᴏᴄᴀᴧ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛᴇбᴇ ʍᴏй хуй нᴇ ɜᴀᴛᴩᴀᴧᴧиᴩᴀʙᴀᴛь) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ у ᴛᴇбя ᴏᴛ ʍᴏᴇᴦᴏ хуя ʍиᴦᴩᴇнь?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я бᴧядь ʙᴏбью ᴛᴇбя ʙ ᴨᴏᴧ, ᴋᴀᴋ ᴦʙᴏɜдь нᴀ 60 хуᴇʍ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ужᴇ ᴄᴧᴏʙᴀ ᴋᴏнчиᴧиᴄь,и ᴛы ᴨᴩᴏᴄᴛᴏ ᴄᴏᴄᴇɯь хуй) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴛя ᴄʙинью ᴨᴩидуɯу нᴀхуй ))) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ ᴛы ᴄуᴋᴀ ᴋᴧᴇщь ᴇбᴀный,ɜᴀᴧᴇɜ ᴨᴏд ʍᴏю ɜᴀᴧуᴨу,ʍ ᴨиᴛᴀᴇɯьᴄя ᴨᴏдɜᴀᴧуᴨныʍ ᴛʙᴏᴩᴏᴦᴏʍ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] учᴇныᴇ ʙыдʙинуᴧи ᴛᴇᴏᴩию,чᴛᴏ ʙᴄᴇ ᴋᴛᴏ ᴨыᴛᴀᴇᴛᴄя ᴛᴩᴏᴧᴧиᴛь ʍᴇня ᴨᴏдᴄᴏɜнᴀᴛᴇᴧьнᴏ ᴄᴏᴄуᴛ хуи ))) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ ʍᴏя бᴩᴀᴛʙᴀ иᴦᴩᴀᴧᴀ ʙ ɸуᴛбᴏᴧ нᴀ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи?) ʍы ᴄᴛᴏᴧьᴋᴏ ᴦᴏᴧᴏʙ ɜᴀбиᴧи ʙ ᴇё ʙᴩᴀᴛᴀ,чᴛᴏ у нᴀᴄ яйцᴀ ᴏᴨухᴧи) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴄᴇйчᴀᴄ ᴛʙᴏй ᴇбᴧᴇᴛ иɜʍᴀжу ᴦᴀʙнᴏʍ,ᴄᴋᴀжу, чᴛᴏ ᴛы ᴀɜиᴀᴛ, и ᴏᴛᴨᴩᴀʙᴧю ʙ ᴋиᴛᴀй) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴩᴇбяᴛ,ᴨᴏɯᴧиᴛᴇ нᴀ бᴀᴧᴧ?) я ᴛᴀʍ ʍᴀᴛь ʍᴏᴇᴦᴏ ᴨᴩᴏᴛиʙниᴋᴀ ʙчᴇᴩᴀ ᴇбᴀᴧ ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴨᴇᴩдᴇᴧ ᴛᴇбᴇ нᴀ ухᴏ,ᴄуᴋᴀ ᴛы ᴦᴧухᴀя) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴨᴇᴩдᴇᴧ ᴛᴇбᴇ нᴀ ухᴏ,ᴄуᴋᴀ ᴛы ᴦᴧухᴀя) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴏдин ᴩᴀɜ я ᴨᴩиɯᴇᴧ ᴋ ᴛʙᴏᴇй ʍᴀʍᴋᴇ ᴄуᴋᴀ,и ᴄᴛᴩᴇᴧяᴧ ᴨᴏ нᴇй ᴄ хуя,ᴋᴀᴋ ᴄ ᴛᴀнᴋᴀ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы бᴧя чᴏ ᴋᴀᴩыᴛᴏ?) я ᴛя хуᴇʍ ᴄʍᴀᴄᴛᴇᴩю,нᴀᴧᴏжу бᴏʍбящих ᴨуᴋᴀнᴏʙ,и ʙɜᴏᴩʙу нᴀхуй )))) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴛʙᴏю ᴋᴀᴩдиᴏᴦᴩᴀʍʍу иɜучиᴧ хуᴇʍ,чᴛᴏб биᴛь ᴨᴏ ᴛʙᴏᴇʍу бᴏᴧьнᴏʍу ᴄᴇᴩдцу) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы чᴏ ᴄуᴋᴀ,ᴄ ʍᴏᴇᴦᴏ хуя дᴇʍᴏнᴀ ᴄʙᴏᴇй ᴦубы иɜᴦᴏняᴛь ᴄᴏбᴩᴀᴧᴄя?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴛᴇбя щᴀ хуᴇʍ ʙ днᴏ ʍᴏᴩя ᴄᴋину,ᴋᴀᴋ бᴀᴧᴧᴀᴄᴛ ᴄ ᴋᴏᴩᴏбᴧя) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] щᴀ,я ʙᴇдь ᴄуᴋᴀ ᴇщё нᴇ ᴩᴀɜᴏᴦᴩᴇᴧᴄя,ууух,ᴋᴀᴋ ᴨᴏᴇбу ᴛʙᴏю ʍᴀᴛь ᴄᴇᴦᴏдня ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʍы ᴄ ᴩᴏʍᴋᴏй нᴀ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи хуяʍи ᴋᴏᴄᴛᴇᴩ ᴩᴀɜᴏжᴦᴧи,чᴛᴏб нᴀ ᴇё ᴨуᴄᴛыннᴏй ᴨиɜдᴇ ᴄᴏᴦᴩᴇᴛᴄя) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, я ᴨиɯу ᴨᴏ ᴨяᴛь ᴄᴧᴏʙ, и ᴨᴩᴏᴄᴛᴏ ɜᴀᴨиныʙᴀю ᴛʙᴏю ʍᴀᴛь) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴇбᴀɯих ʍᴀʍ ᴋᴏʍуниᴄᴛы чᴛᴏ ᴧи ᴇбуᴛ?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴀɯи иɜбиᴩᴀᴧ ʍᴏй хуй ʍᴇᴩᴏʍ ᴇё ᴦубы) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴄидя ᴇᴀ ɜᴏнᴇ ᴨᴏᴨиʙᴀя чиɸиᴩ ᴇбᴀᴧ ᴛʙᴏю ʍᴀᴛь?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ᴄуᴋᴀ ᴋуɯᴀᴇɯь ᴄидя нᴀ ʍᴏᴇʍ хуᴇ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴄуᴋᴀ ᴄᴨᴏᴄᴏбᴇн ᴇбᴀᴛь ᴛʙᴏю ʍᴀᴛь ʍиниʍуʍ 10 чᴀᴄᴏʙ? ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я хᴏжу ᴨᴏ ᴧучу ᴇбя ᴛʙᴏю ʍᴀᴛь?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇᴛᴇ,чᴛᴏ я ʙᴀᴄ ᴄ хуя ᴋᴏᴩʍиᴛь буду, ᴄᴏбᴀᴋи ᴇбᴀныᴇ?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] нᴇᴛ,ну ʍнᴇ чᴏ,ʙɜяᴛь хуй ʙ ᴩуᴋу,и биᴛь ʙᴀʍ ᴨᴏ ᴦубᴀʍ? ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʙы ᴨᴏниʍᴀᴇᴛᴇ,чᴛᴏ я ʙᴀʍ ᴄуᴋᴀ ᴨᴏд нᴏᴄ ᴨᴇᴩжу,дʙᴀ чухᴀнᴀ бᴧядь ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʙᴀᴄ дʙух ɯᴧюх нᴀ ʍᴏй хуй ᴩᴀɜдᴇᴧиᴛь? ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ʙ ᴋᴀᴛᴏᴧичᴇᴄᴋᴏй цᴇᴩᴋʙи ᴄ ᴛᴩᴇʍя ᴨᴏᴨᴀʍи ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь чᴛᴏ я хуᴇʍ ᴛᴇбᴇ ᴄᴋᴀжу " ᴀᴩиʙуᴀᴩ, хуйᴧᴏ " [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴛʙᴏю ʍᴀᴛь ʙᴏᴄᴨиᴛыʙᴀᴧ хуᴇʍ? ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я бᴧядь ᴛʙᴏи нᴏᴦи хуᴇʍ ᴏᴛᴩᴇжу,будᴛᴏ ᴄᴀбɜиᴩᴏ нᴀхуй) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я жᴇ ᴄуᴋᴀ буду ᴋᴀᴋ ʙ ᴧᴇᴄу ᴇбᴀᴛь ᴛʙᴏю ʍᴀᴛь ᴨᴏд ᴨᴇньᴋᴏʍ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ ᴩᴀдиуᴄ ᴨᴏᴩᴀжᴇния ᴦубы ᴛʙᴏᴇй ʍᴀʍᴀɯи ʍᴏиʍ хуᴇʍ ᴩᴀʙᴇн 1000 ᴋʍ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ʙыᴇбᴀᴧ ʍᴀᴛь ᴨᴏᴧᴏʙины ᴛᴩᴏᴧᴧинᴦᴀ,ᴀ ᴛʙᴏю ᴨᴏдᴀʙнᴏ ʙыᴇбу) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я жиʙу ɜᴀ ᴄчᴇᴛ ᴨиɜдᴀᴋᴀ ᴛʙᴏᴇй ʍᴀʍᴀɯи?) я ᴇё ᴄуᴛᴇнᴇᴩ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ɜнᴀᴧ,чᴛᴏ я ᴇбу ᴛʙᴏю ʍᴀᴛь нᴀ ᴄᴋᴏᴩᴏᴄᴛи 150 ᴋʍ ʙ чᴀᴄ?) ʍᴏи яйцᴀ ᴨᴏ 7 ᴩᴀɜ ʙ ᴄᴇᴋунду ᴄᴛыᴋᴀᴧиᴄь ᴄ ᴇё бᴀᴩдюᴩᴏʍ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴇбу ᴛʙᴏю ʍᴀᴛь нᴀ ɜᴀᴨᴩᴀʙᴋᴇ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴄᴇйчᴀᴄ хуᴇʍ иᴄᴨᴇᴨᴇᴧю чᴇᴩᴇᴨ ᴛʙᴏᴇй ʍᴀʍᴋи?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я ᴨᴏдᴀᴩᴏжниᴋ ᴨᴩиᴧᴏжу ᴋ ᴨиɜдᴇ ᴛʙᴏᴇй ʍᴀʍᴀɯи,чᴛᴏб ᴨᴏᴄᴧᴇ ʍᴏᴇᴦᴏ хуя нᴇ ᴛᴇᴋᴧᴀ ᴋᴩᴏʙь ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] днᴏ ᴛы ᴄуᴋᴀ ᴋᴀᴩыᴛнᴏᴇ) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я хуᴇʍ ᴛʙᴏё ᴇбᴀᴧᴏ иɜᴩиᴄую) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏниʍᴀᴇɯь, чᴛᴏ я щᴀ хуᴇʍ ᴄнᴇᴄу ᴋᴩыɯу ᴄ дᴏʍᴀ ᴛʙᴏᴇй ʍᴀʍᴀɯи?) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ʙᴋуᴩᴄᴇ чᴇй хуй ᴏᴄᴀдиᴧ?) ᴄᴀдниᴋ ᴛы ᴄуᴋᴀ бᴇɜ ᴦᴏᴧᴏʙы, я ᴛᴇбя жᴇ хуᴇʍ убью) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴀ ну ᴄюдᴀ иди иᴧи ʍнᴇ ᴨᴩидᴇᴛᴄя ʙ ᴨиɜду ᴛʙᴏᴇй ʍᴀʍᴀɯᴇ, ᴋудᴀ ᴛы ᴄᴨᴩяᴛᴀᴧᴄя хуй ɜᴀᴨихиʙᴀᴛь и ᴧᴏʙиᴛь ᴛᴇбя ᴋᴀᴋ ᴩыбу нᴀ удᴏчᴋу)) ɯᴋᴀᴛуᴧᴋᴀ бᴧяᴛь ᴛы ᴇбᴀнᴀя)) я жᴇ бᴧяᴛь ᴩᴏᴛᴀн ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴄᴋᴩучу и буду иɜ нᴇᴦᴏ ᴄᴏᴄиᴄᴋи дᴇᴧᴀᴛь)) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] у ᴛʙᴏᴇй ʍᴀʍᴀɯᴇ нᴀ жᴏᴨᴇ ᴛᴀᴋᴀя ɜдᴏᴩᴏʙᴀя ᴨᴏʍидᴏᴩинᴀ ᴇбᴀᴛь ᴋᴩᴀᴄнᴀя ᴇщᴇ дᴏ ᴨиɜды)) я жᴇ бᴧяᴛь хуᴇʍ ᴇᴇ ᴄнᴇᴄу и ᴄᴏдᴇᴩжиʍᴏᴇ ᴛᴇбᴇ нᴀ ᴇбᴧᴇᴛ ʙыбᴩыɜниᴛ))) ᴄᴋинхᴇд ᴛы ᴇбᴀный)) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴄᴧыɯ?) ᴦᴏʙнᴏᴨᴀдищᴇ ᴇбᴀнᴏᴇ?) ʍнᴇ ᴛʙᴏй ᴏчᴋᴇᴄᴛᴀн ᴩᴀɜᴩыʙᴀᴛь ᴧᴇᴦчᴇ чᴇᴛ нᴇ ᴨᴏняᴧ нихуя я жᴇ бᴧяᴛь ᴛᴇбя нᴀ ᴄʙᴏй хуй нᴀᴛяᴦиʙᴀю ᴨᴩяʍᴏ ᴋᴀᴋ нᴏᴄᴋи нᴀ ᴄᴛᴏᴨы ᴇбᴀᴛь [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛᴩᴀхᴛынбых ᴇбᴀный ᴛы ᴦдᴇ ᴛᴀʍ бᴧяᴛь ᴨᴩячᴇɯьᴄя?) ʍнᴇ ᴛᴇбя ᴨᴏ ᴛᴇʍныʍ ᴨᴇᴩᴇуᴧᴋᴀʍ дᴧя ᴏᴛᴄᴏᴄᴀ хуя иᴄᴋᴀᴛь нᴀдᴏ иᴧи чᴛᴏ?)) я ᴛʙᴏю ʍᴀᴛь ᴛᴀᴋжᴇ ʙыᴇбᴀᴧ ᴛᴇʍнᴏʍ ᴨᴇᴩᴇуᴧᴋᴇ нᴏ ᴛᴀʍ ᴋᴀʍᴇᴩы ᴄᴛᴏяᴧи и ʍнᴇ нᴀ хуй ᴨᴩᴇᴧᴇᴨиᴧи ɯᴛᴩᴀɸ )) [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ ᴛы ᴛуᴨᴏ ᴨᴀчᴋᴀ ᴄиᴦᴀᴩᴇᴛ) ᴛы ᴄᴏᴄᴇɯь ниᴋᴀᴋ)) ᴀ ʙᴏᴛ ᴛʙᴏя ʍᴀʍᴀɯᴀ ᴄᴏʙᴄᴇʍ дᴩуᴦᴏᴇ дᴇᴧᴏ бᴧяᴛь) нᴏ бᴇдᴀ ʙ ᴛᴏʍ чᴛᴏ ᴏнᴀ ᴄʙинья и ᴏнᴀ ᴋᴏᴦдᴀ ᴄᴏᴄᴇᴛ хᴩюᴋᴀᴇᴛ ᴀ ʙᴏᴛ ᴛʙᴏй ᴨᴀᴨᴀɯᴀ ᴦᴏᴩиᴧᴧᴀ бᴧяᴛь ᴇбᴀнᴀя ʙᴏᴏбщᴇ)) ᴏни ᴛᴇбя ᴄдᴇᴧᴀᴧи нᴇ чᴇᴩᴇɜ ᴨᴏᴧᴏʙыᴇ ᴏᴩᴦᴀны , ᴀ ᴛʙᴏ ᴨᴀᴨᴀɯᴀ ɜᴀᴧᴇɜ бᴏɯᴋᴏй ʙ ᴨиɜду ᴛʙᴏᴇй ʍᴀʍᴀɯи и ᴨᴧюнуᴧ ᴛудᴀ)) ᴄᴧиɜᴇнь ᴛы ᴄуᴋᴀ ᴇбᴀный [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я буду ᴩᴀᴄᴋᴩучиʙᴀᴛь ᴨиɜдᴀᴋ ᴛʙᴏᴇй ʍᴀʍᴀɯи и ᴨᴩиʙяжу ᴋ нᴇʍу ᴇᴇ ᴩᴏᴛᴀн. ᴏн жᴇ ᴄуᴋᴀ ᴋᴀᴋ ᴧᴏᴨᴏᴄᴛи будᴇᴛ ᴋᴩуᴛиᴛьᴄя ʙᴇᴩᴛᴏᴧᴇᴛᴀ и ᴨᴏдниʍᴀᴛь ᴇᴇ ᴨиɜдᴀᴋ ʙʙᴇᴩх ᴛы ᴨᴏниʍᴀᴇɯь?) ʍиᴧᴧиᴀᴩдᴇᴩ ᴛы ᴀнᴀᴧьный ᴄʙᴏᴇй ʍᴀʍᴀɯи [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я жᴇ бᴧяᴛь нᴀ ᴛʙᴏи хᴏхᴧяцᴋиᴇ ᴧᴀᴨᴛи ᴨᴩиᴋᴧᴇю ᴄʙᴏй ᴄᴨᴇᴩʍᴀᴋ, ᴀ ᴛы будᴇɯь дуʍᴀᴛь , чᴛᴏ ϶ᴛᴏ ᴄуᴨᴇᴩ ᴋᴧᴇй)) я ᴇᴦᴏ ʙыᴄᴋᴩᴇб иɜ ᴨиɜдᴀᴋᴀ ᴛʙᴏᴇй ʍᴀʍᴀɯи ᴋᴏᴦдᴀ ᴏн ᴨᴩиᴧиᴨ ᴋ ᴇᴇ ᴨиɜдᴇ 3 ᴦᴏдᴀ нᴀɜᴀд ᴛы ᴨᴏниʍᴀᴇɯь бᴧяᴛь?)) ᴛᴩубᴏчиᴄᴛ ᴛы ᴇбᴀный [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ϶ᴛᴏᴦᴏ нᴇ ɜнᴀю ʙᴇдь нᴇ ʙидᴇᴧ ᴛᴇбя, ᴀ ᴇᴄᴧибы уʙидᴇᴧ, ᴛᴏ ᴛᴩᴀхнуᴧ бы ᴛᴇбя ʙᴏ ʙᴄᴇ ᴨихᴀᴛᴇᴧьныᴇ и дыхᴀᴛᴇᴧьныᴇ, ʙᴏ ʙᴄᴇ ᴄущᴇᴄᴛʙующиᴇ и нᴇ ᴄущᴇᴄᴛʙующиᴇ, ᴀ ᴛᴇ чᴛᴏ нᴇ ᴄущᴇᴄᴛʙуюᴛ ᴨᴩидуʍᴀᴧ бы, и ᴨᴏʙᴇᴩь ʍнᴇ ᴦнидᴀ ɜᴀᴛᴩᴀхᴀннᴏ-уᴩᴏдᴧиʙᴀя ᴛᴇбᴇ бы ϶ᴛᴏ ᴨᴏнᴩᴀʙиᴧᴏᴄь  [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] у ᴛʙᴏᴇй ʍᴀʍы ну ᴨᴩᴏᴄᴛᴏ ᴨиɜдᴇц ᴋᴀᴋᴀя бᴏᴧьɯᴀя ᴨиɜдᴀ, я ᴛудᴀ ᴨᴏᴧнᴏᴄᴛью ʙхᴏдиᴧ. ϶ᴛᴏ ᴨиɜдᴇц, я ᴋᴀᴩч ʙᴏɜᴧᴇ ᴇᴇ ᴨиɜды ᴋᴏʙᴩиᴋ ᴨᴏᴧᴏжиᴧ, чᴛᴏб нᴏᴦи ʙыᴛиᴩᴀᴛь бᴧяᴛь  [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴛы ᴨᴏᴇбᴀнᴇц, дᴩᴀᴋᴏн ᴛᴩяᴨᴏчный, ᴧᴏхᴏдᴩᴏʍ ᴦᴀᴧиʍый, уёбᴏᴋ ᴨиɜдᴧяʙый, ᴋᴏнчинᴀ ᴇбᴀнᴀя, уёбищᴇ ᴧᴇᴄнᴏᴇ. ᴏᴛᴄᴏᴄи нᴇ нᴀᴦибᴀяᴄь и ᴨᴏдʍыᴛьᴄя нᴇ ɜᴀбудь. нᴇ бɜди ᴋᴀᴨуᴄᴛин, ʙыᴇбᴇʍ ᴏᴛᴨуᴄᴛиʍ.  [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴛʙᴏю ʍᴀᴛь ᴇбᴀᴧ ᴋᴏᴦдᴀ ᴛы ᴄᴏᴄᴀᴧ ʍнᴇ хуй нᴀ 10 ϶ᴛᴀжᴇ - ᴀ ᴨᴏᴛᴏʍ я ᴛʙᴏю бᴀбуɯᴋу ᴇбᴀᴧ нᴀ ?? -ᴨᴏᴛᴏᴧᴋᴇ  [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] ᴨᴏɜᴏʙи ᴄʙᴏю ᴛянᴏчᴋу я хᴏчу ᴇй ᴧичнᴏ ᴄᴋᴀɜᴀᴛь ᴄᴨᴀᴄибᴏ ɜᴀ ʙчᴇᴩᴀɯний ᴨᴩᴇᴋᴩᴀᴄный ᴏᴛᴄᴏᴄ  [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] дᴏчᴋᴀ ϶ᴧиᴛнᴏй ɯᴧюхи и ᴏᴛцᴀ бᴏʍжᴀ?___)))) ᴛы ᴨᴏниʍᴀᴇɯь чᴛᴏ ʍᴀʍᴋу ᴛʙᴏю ᴇбуᴛ у ᴛя ʙ ᴋᴏʍнᴀᴛᴇ ᴋᴏᴦдᴀ ᴛы ᴄᴨиɯь ᴛᴇ ᴇё нᴇ жᴀᴧᴋᴏ?)  [<emoji document_id=5420526968418345993>🤍</emoji>]',
'[<emoji document_id=5420526968418345993>🤍</emoji>] я ᴇбᴀᴧ ᴛʙᴏю ʍᴀʍᴀɯᴋу нᴀ ᴄᴛᴏᴧᴇ и нᴀ ᴨᴏдᴏᴋᴏнниᴋᴇ)) ᴀ ну нᴇᴄи ʙᴇᴩᴇʙᴋу и ᴏᴦнᴛуɯиᴛᴇᴧь:ɜᴀᴧᴇɜиɯь ᴨᴏᴛуɯиɯь ᴇй ᴨиɜду ᴀ ᴨᴏᴛᴏʍ я ᴏᴛдᴀʍ ʙᴀᴄ нᴀ ᴩᴀᴄᴛᴇᴩɜᴀниᴇ нᴇᴦᴩᴀʍ  [<emoji document_id=5420526968418345993>🤍</emoji>]' ]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl))
            await sleep(0.1)
            await sleep(time)    


    async def звездаcmd(self, message):
        """— Запускает модуль по указанной команде"""
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b><emoji document_id=5420085673413583049>🤍</emoji> Ϻσɠγλƅ #Ӡɞεӡɠα ηερεϲταλ γδμɞατƅ τɞσબ ϻατƅ ɞϲελεϰϰσύ. <emoji document_id=5420085673413583049>🤍</emoji></b>")
            return
        await utils.answer(
            message,
            "<b><emoji document_id=5420085673413583049>🤍</emoji> Ϻσɠγλƅ #Ӡɞεӡɠα ϰαɥαλ γδμɞατƅ τɞσબ ϻατƅ ɞϲελεϰϰσύ. <emoji document_id=5420085673413583049>🤍</emoji></b>\n\n"
            "<b><emoji document_id=5420085673413583049>🤍</emoji> Ϥτσδƅɩ σϲταϰσɞμτƅ ηρσημωμ. <code>.звезда</code></b>"
        )

        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl5 = [
        "<emoji document_id=5420085673413583049>🤍</emoji>Ⲥⲁⲥⲉⲱ ⲙⲏⲉ ⲇⲩⲣⲁⲃⲗυⲃⲁя 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲃ ⲇⲃυⲯⲉⲏυυ ⲥⲁⲥⲉⲱ ⲙⲏⲉ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲣⲁⲥⲗⲁⳝυⲗ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲟⳝυⲇⲉⲗ ⲧя ⲭⲩύⲉⲙ ⲱⲁⲗⲁⲃⲁ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲣⲁⳅⲯⲁⲗ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲅⲣⲉю ⲧя ⲭⲩⲉⲙ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⳝⲉⳅ ⲥⲟⲃⲉⲥⲧυ ⲥⲁⲥⲉⲱ ⲙⲏⲉ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Эⲕⲁⲏⲟⲙⲏⲁ ⲉⲡⲩ ⲧя 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲭⲩⲉⲙ ⲃ ⲧя ⲡⲱυⲕⲁⲗ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲥⲡⲁⲣⲧυⲃⲏⲁ ⲥⲁⲥⲉⲱ ⲙⲏⲉ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲭⲩύⲉⲙ ⲧя ⲙⲁⲧⲏⲩⲗ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⳝⲗⲉⲥⲧяⳃⲉ ⲉⲡⲩ ⲧя 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲥⲡⲉⲣⲙⲩ ⲃ ⲧя υⳅⲉ ⳅⲁⲗυⲗ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲟⲧⳝⲉⲗυⲗ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲥⲃⲁⳝⲟⲇⲏⲁ ⲥⲁⲥⲉⲱ ⲙⲏⲉ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⳅⲁⲧⲁυⲗ ⲃ ⲧⲉ ⲥⲃⲟύ ⲭⲩύ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲥⲗⲉⲧⲁя ⲇⲟⲭⲏⲉⲱ ⲗⲉⲭⲕⲟ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲡⲣⲁⲃⲉⲣυⲗ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲕⲁⲏцⲉⲧⲣυⲣⲟⲃⲁⲗ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲟⳝⲗⲉⲭⳡυⲗ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲥⲁⲥⲁⲗⲁ ⲧы ⲙⲏⲉ ⲗⲉⲭⲕⲟ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⳅⲩⳝы ⲧⲉ ⲭⲩύⲉⲙ ⲧⲣⲩ ⲧⲁⲕⲧⲁ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲣⲁⲥⲡυⲗυⲗ ⲧя ⲭⲩⲉⲙ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲇⲁⲃⲗю ⲏⲁ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⳡⲟⲧ ⲃ ⲣⲟⲧ ⲧя ⲉⲡⲩ ⲗⲉⲭⲕⲟ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲥ ⳡυⲥⲧⲟⲅⲟ ⲗυⲥⲧⲁ ⲥⲁⲥⲉⲱ ⲙⲏⲉ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲣⲁⳅⲇⲣⲁⲯυⲗ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲟⲧⲕⲣыⲗ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲭⲟⲯⲩ ⲃ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲡⲣυⳝυⲗ ⲧя ⲭⲩύⲉⲙ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲡⲟяⲃυⲗⲥя ⲃ ⲧⲉ ⲭⲩύⲉⲙ ⲥⲗⲉⲧⲁя 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟύ ⲇⲉⲇ ⲃ 45 ⲙⲏⲉ ⲭⲩύ ⳅⲁ ⲕⲩⲥⲟⲕ ⲥⲁⲗⲟ ⲥⲁⲥⲁⲗ ⲣυⲗυ ⲏⲉⲙⲟⳃь ⲟⲏ ⲉⳝⲁⲏыύ ⲇⲁ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>υ ⳡё ⳝⲩⲇⲩ ⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲧь ⲇⲟ ⲧⲁⲗⲟⲃⲁ υ ⲧы ⲏⲉ ⲥⲙⲟⲯⲉⲱь ⲙⲏⲉ ⲏⲉ ⳡⲉⲅⲟ ⲥⲕⲁⳅⲁⲧь ⲃⲉⲇь ⲥⲁⲙ ⲃ ⲧⲁύⲏⲉ ⲙⲏⲉ ⲥⲟⲥёⲱь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲧь ⲩⲯⲉ ⲇⲁⲃⲏⲟ ⲏⲁⳡⲁⲗⲁ ⲡⲣⲟяⲃⲗяⲧь ⲩⲃⲁⲯⲉⲏυя ⲕ ⲙⲟⲉⲙⲩ ⲭⲩю υ ⳅⲇⲁⲣⲟⲃⲁⲉⲧьⲥя ⲥ ⲏυⲙ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲉ ⲧы ⳡё ⲇⲩⲙⲁⲗ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲇⲟⲗⲅⲟ ⲥⲙⲟⲯⲉⲧ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲣыⲡⲁⲉⲧьⲥя я ⲉύ ⳅⲁ эⲧⲟ ⲭⲩёⲙ ⲡⲟ ⲅⲟⲣⳝⲩ ⲏⲁⲃⲉⲣⲏⲩ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲃ ⲏⲁⲥⲗⲉⲇⲥⲧⲃⲟ ⳅⲁⲃⲉⳃⲁⲗⲁ ⲧⲃⲟύ ⲣⲟⲧ ⲉⲥⲗυ ⳝⲩⲇⲉⲱь эⲧⲟ ⲟⲧⲣυцⲁⲧь я ⲉё ⲭⲩёⲙ υⳅ ⲅⲣⲟⳝⲁ ⲇⲟⲥⲧⲁⲏⲩ ⳡⲧⲟⳝы ⲟⲏⲁ ⲡⲟⲇⲧⲃⲉⲣⲇυⲗⲁ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲩ ⳡё ⲡⲣυⲥⲧⲩⲡυⲙ ⲣⲁⲥⳡⲉⲭⲗяⲧь ⲧⲃⲟю ⲙⲁⲧь υⲗυ ⲧы ⲇⲁⲯⲉ ⲡⲟⳝⲟυⲱьⲥя ⲣыⲡⲏⲩⲧьⲥя ⲏⲁ ⲙⲉⲏя 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲧь ⲏⲉ ⲣⲁⳅ ⲡⲁⲇⲁⲗⲁ ⲏⲁ ⲙⲟёⲙ ⲭⲩю ⲏⲟ ⲟⲏⲁ ⲥⲧⲣⲉⲙυⲗⲟⲥь ⲕ ⲃⲉⲣⲱυⲏⲉ ⲇⲩⲣⲁ ⲉⳝⲁⲏⲁя 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲣⲁⲕⲩⲱⲕⲁ ⲏⲁⲭⲩύ ⲧы ⲡⲣяⳡⲉⲱьⲥя ⲥⲃⲟю ⲙⲁⲧь ⲟⲧ ⲭⲩя ⲙⲟⲉⲅⲟ ⲩ ⲏⲉё ⲏⲁ ⲡυⳅⲇⲉ ⲅⲉⲟⲗⲟⲕⲁⲧⲟⲣ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲧь ⲗⲉⲅⲗⲁ ⲡⲟⲇ ⲙⲟύ ⲭⲩύ υ ⲃⲣёⲧ ⳡⲧⲟ ⲏⲉ ⲙⲟⲯⲉⲧ ⲃыⲗⲉⳅⲧυ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲉ ⲭⲟⳡⲩ ⲧⲉⳝя ⲟⲥⲕⲟⲣⳝυⲧь ⲏⲟ ⲧⲃⲟя ⲙⲁⲧь ⲟⲧⲥⲁⲥыⲃⲁⲗⲁ ⲙⲏⲉ ⲡⲟ 100 ⲣⲁⳅ ⲏⲁ ⲇⲏю ⲏⲟ ⲇⲗя ⲏⲉё эⲧⲟ ⲏⲉ ⲣⲉⲕⲟⲣⲇ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲩ υ ⳡё ⲧы ⲇⲟⲥυⲭⲡⲟⲣ ⲇⲩⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⳝⲩⲇⲉⲧ ⲉⳝⲁⲧь ⲃⲁⲱⲩ ⲥⲉⲙύⲕⲩ ⳅⲁ ⳝⲉⲥⲡⲗⲁⲧⲏⲟ ⲥⲕⲟⲣⲟ ⲃⲁⲙ ⲡⲣυⲇёⲧьⲥя ⲡⲗⲁⲧυⲧь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲡⲣⲉⲯⲇⲉ ⳡⲉⲙ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁⳡυⲏⲁⲉⲧ ⲥⲟⲥⲁⲧь я ⳝью ⲉύ ⲭⲩёⲙ ⲡⲟ ⲅⲩⳝⲉ ⲉύ ⲏⲣⲁⲃυⲧьⲥя ⲃⲉⲇь эⲧⲟ ⲡⲁⲥⲧⲁ ⲇⲁⲃⲏⲟ ⲃⲟ ⲃⲗⲁⲥⲧυ ⲙⲟⲉⲅⲟ ⲭⲩя 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧы ⲇⲁⲯⲉ ⲏⲉ ⳅⲁⲙⲉⲧυⲱь ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲙⲟύ ⲭⲩύ ⲯυⲧь ⲡⲉⲣⲉⲉⲇⲉⲧ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲧь ⳃⲁ ⲙⲟύ ⲭⲩύ ⲣⲉⲱυⲗⲁ ⲃ ⲙⲩⳅⲉύ ⲡⲣⲉⲏⲉⲥⲧυ υ ⲥⲕⲁⳅⲁⲧь ⳡⲧⲟ эⲧⲟ ⲃⲉⲗυⲕυύ ⲁⲣⲧⲉⲫⲁⲕⲧ ⳡё ⲟⲏⲁ ⲱⲁⲗⲟⲃⲁ ⲧⲟ ⲧⲁⲕⲁя 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⳝⲉⳅ ⲱⲩⲧⲟⲕ ⲉⲥⲗυ ⲧⲃⲟя ⲙⲁⲧь ⲏⲉ ⲏⲁⳡⲏёⲧ ⲃ ⲧⲉⲙⲡⲉ ⲥⲟⲥⲁⲧь я ⲉύ ⳅⲁⲗⲩⲡⲟύ ⲡⲟ ⲉⳝⲁⲗⲩ ⲥⲉⳅⲯⲩ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>υ ⳡё ⲧы ⳃⲁⲥ ⲧⲟⲯⲉ ⳝⲩⲇⲉⲱь ⲟⲧ ⲭⲩя ⲩⲃυⲗυⲃⲁⲧь ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь υⲗυ ⲏⲁⳡⲏёⲱь ⲏⲁ ⲏⲟⲣⲙⲉ ⲥⲟⲥⲁⲧь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲉ ⲙⲟⲅⲩ ⲡⲉⲣⲉⲇⲁⲧь ⲧⲉ ⳡⲩⲃⲥⲧⲃⲁ ⲕⲟⲅⲇⲁ ⲧⲃⲟя ⲥⲡυⲇⲟⳅⲏⲁя ⲙⲁⲙⲁⲱⲁ ⲙⲏⲉ ⲥⲟⲥёⲧ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳃⲁ ⲙⲟύ ⲭⲩύ ⳅⲁ ⳃⲉⲕⲩ ⲡⲩⲥⲧυⲗⲁ υ ⲏⲉ ⲭⲟⳡⲉⲧ ⲃыⲥⲟⲃыⲃⲁⲧь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲧь ⲩⲯⲉ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲡⲣыⲅⲁⲉⲧ ⲕⲁⲕ ⲏⲁ ⲣⲁⳝⲟⲧⲩ υⲇёⲧ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⳅⲁⳡⲉⲙ ⲧⲃⲟя ⲙⲁⲧь ⲟⲡяⲧь ⲙⲏⲉ ⲥⲟⲥёⲧ ⲙⲟⲯⲉⲧ ⲟⲏⲁ ⲡⲟⲇⲩⲙⲁⲗⲁ ⳡⲧⲟ ⲙⲟⲯⲉⲧ ⲟⲧⲥⲁⲥыⲃⲁⲧь ⲙⲏⲉ ⳝⲉⳅⲗⲉⲙυⲧⲏⲟ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲧь ⲩⲡⲁⲗⲁ ⲡⲉⲣⲉⲇ ⲙⲟυⲙ ⲭⲩёⲙ ⲕⲟⲅⲇⲁ ⲡⲟⲇⲥⲧⲁⲃυⲗ ⲡⲉⲣⲇⲁⲕ ⲡⲉⲣⲉⲇ ⲥⲃⲟυⲙ ⳝⲁⲧⲉύ ⲏⲟ эⲧⲟⲧ ⲟⲥёⲗ ⲡⲟⳝⲟяⲗⲥя ⲉⲅⲟ ⲡⲟⲉⳝⲁⲧь ⲃⲉⲇь ⲟⲏ ⳅⲏⲁⲉⲧ ⳡⲧⲟ ⲙⲟя ⳅⲁⲗⲩⲡⲁ ⲟⲡяⲧь ⲡⲣⲟⳝьёⲧ ⲉⲅⲟ ⲅⲟⲣⳝ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲙⲩⲗьⲕⲁ ⳃⲁ ⲙⲟύ ⲭⲩύ ⲡⲟ ⲅⲗⲁⲏⲇы ⲡⲩⲥⲧυⲗⲁ я ⲡⲣⲉⲇⲗⲁⲅⲁю ⲇⲁⲧь ⲉύ ⲙⲉⲇⲁⲗьⲕⲩ ⳅⲁ ⲅⲟⲇⲟⲃⲟύ ⲟⲧⲥⲟⲥ ⳝⲉⳅ ⲡⲉⲣⲉⲣыⲃⲁ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲩ ⲏⲩ ⲥⲕⲁⲯυ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲕⲁ ⲏⲉ ⲱⲁⳝⲟⲗⲇⲁ я ⲥⲃⲟυⲙ ⲭⲩёⲙ эⲧⲟ ⲟⲡⲣⲟⲃⲉⲣⲅⲏⲩ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲣⲁⳅⲃⲟⲣⲟⲱυⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲕⲩ ⲭⲩёⲙ υ ⲃыⲏⲉⲥ ⲟⲧ ⲧⲩⲇⲁ ⲃⲥё ⳡⲧⲟ ⲙⲟⲯⲏⲟ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>я ⲧⲃⲟю ⲇⲩⲣⲏⲩю ⲙⲁⲙⲁⲱⲩ ⳃⲁ ⲏⲁ ⲭⲩⲉ ⳅⲁ ⲧⲁⲕυⲉ ⲇⲃυⲯⲉⲏυя ⲡⲣⲟⲃⲉⲣⲏⲩ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲉ ⲃⲉⲣυⲱь ⲙⲏⲉ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲙⲟύ ⲭⲩύ ⳝⲉⳅⲁⲥⲧⲟⲏⲟⲃⳡⲏⲟ ⲥⲟⲥёⲧ ⲧⲁⲕ ⲡⲣυⲭⲟⲇυ ⲟⲏⲁ ⲇⲁⲥⲧ ⲧⲉ ⲩⲣⲟⲕυ ⲟⲧⲥⲟⲥⲁ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲉ ⲙⲟⲅⲩ ⲡⲟⲏяⲧь ⲡⲟⳡⲉⲙⲩ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲧⲁⲕⲁя ⲥⲗⲁⳝⲁя ⲱⲗюⲭⲁ ⳡⲧⲟ ⲇⲁⲯⲉ ⲙⲟύ ⲭⲩύ ⲩⲯⲉ ⲟⲥυⲗυⲧь ⲏⲉ ⲙⲟⲯⲉⲧ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⳃⲁ ⲭⲩёⲙ ⲡⲉⲣⲉⲃⲉⲣⲏⲩ ⲭⲟⲧя эⲧⲟ ⲯⲁⲗⲕⲁя ⲏⲁⳡⲏёⲧ ⲟⲡяⲧь ⲃ ⲕⲟⲏⲃⲩⲗьⲥυяⲭ ⳝυⲧьⲥя 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲩ ⲩⲯⲉ ⳝⲉⳅ ⲱⲩⲧⲟⲕ ⲃ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⳅⲁⲅⲏⲁⲗⲥя ⲁ ⲟⲏⲁ ⲏⲁⳡυⲏⲁⲉⲧ ⲕⲁⲕ ⲥⲃυⲏья ⲃυⳅⲯⲁⲧь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲃыⲥⲉⲕ ⳅⲁ ⲧⲟ ⳡⲧⲟ ⲟⲏⲁ ⲧⲃⲟⲉⲙⲩ ⳝⲁⲧυ ⲟⲧⲥⲟⲥⲁⲧь ⲡыⲧⲁⲗⲁⲥь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲧь ⲗⲉⳅⲗⲁ ⲕⲟ ⲙⲏⲉ цⲉⲗⲟⲃⲁⲧьⲥя ⲏⲟ ⲉύ ⳅⲁⲗⲩⲡⲟύ ⲗⲟⳝ ⲣⲁⲥⲕⲣⲟⲱυⲗ ⲡⲩⲥⲧь ⳅⲏⲁⲉⲧ ⲥⲃⲟё ⲙⲉⲥⲧⲟ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲩ υ ⳡё ⲧⲃⲟя ⲙⲁⲧь ⲩⲯⲉ ⲅυⲗьⲇυю ⲥⲟⳅⲇⲁⲗⲁ ⳡⲧⲟⳝы ⲙⲟύ ⲭⲩύ ⲃⲟⲥⲭⲃⲁⲗяⲧь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲧь ⳃⲁ ⲙⲟύ ⲭⲩύ ⲡⲣυ ⲡⲟⲇⲣⲩⲅⲁⲭ ⲣⲁⲥⲭⲃⲁⲗυⲃⲁⲗⲁ υ ⲟⲏυ ⲧⲟⲯⲉ ⲣⲉⲱυⲗυ ⲙⲏⲉ ⲟⲧⲥⲟⲥⲁⲧь ⲏⲟ ⲗⲩⳡⲱⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲩⲭⲉ ⲏⲉ ⲕⲧⲟ ⲏⲉ ⲥⲟⲥёⲧ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲉⲥⲗυ ⲧы ⲭⲟⳡⲉⲱь ⲙⲟύ ⲭⲩύ ⲧⲟⲅⲇⲁ ⲧⲉ ⲡⲣυⲇёⲧьⲥя ⲡⲟⲕⲟⲏⲕⲩⲣυⲣⲟⲃⲁⲧь ⲥ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉύ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲩ υ ⳡё ⲧы ⳃⲁⲥ ⲡⲟⲇⲟⲭⲏⲉⲱь ⲏⲁ ⲙⲟёⲙ ⲭⲩю ⳡⲉⲙ ⲟⲡⲟⳅⲟⲣυⲱь ⲥⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲭⲟⲧя ⲙⲟύ ⲭⲩύ υ ⲧⲁⲕ ⲉё ⲟⲡⲩⲥⲧυⲗ ⲉⳅ ⲉⳅ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲧⲩⲱⲕⲁ ⲙⲟⲯⲉⲧ ⲟⲧⲣυцⲁⲧь ⳡⲧⲟ ⲥⲟⲥⲁⲗⲁ ⲙⲏⲉ ⲏⲟ ⲩ ⲙⲉⲏя ⲉⲥⲧь ⲡⲣяⲙⲟⲉ ⲇⲟⲕⲁⳅⲁⲧⲉⲗьⲥⲧⲃⲟ ⲃⲉⲇь я ⳅⲁⲕⲁⳡⲁⲗ ⲉё υⳅⲏⲩⲧⲣυ ⲥⲡⲉⲣⲙⲟύ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲧь ⲡⲣⲟⲃυⲏυⲗⲁⲥь ⲡⲉⲣⲉⲇ ⲙⲟυⲙ ⲭⲩёⲙ υ ⲉύ ⲡⲣυⲱⲗⲟⲥь υⳅⲃⲉⲏяⲧьⲥя ⲥⲃⲟⲉύ ⲯⲁⲗⲕⲟύ ⲅⲗⲟⲧⲕⲟύ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲩ ⲧы ⲣυⲗυ ⲏⲉ ⲃⲇⲩⲡⲗяⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲙⲟύ ⲭⲩύ ⲣⲉⲱυⲗⲁ ⲃ ⲁⲣⲉⲏⲇⲩ ⲃⳅяⲧь ⲏⲁ ⲇⲉⲏь υⳅ ⳅⲁ ⳡⲉⲅⲟ ⲡⲣⲟⲇⲁⲗⲁ ⲡⲟⳡⲕⲩ ⲧⲃⲟⲉⲅⲟ ⳝⲁⲧυ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲩ ⳡё ⳝⲩⲇⲉⲙ ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲧь υⲗυ ⲧы ⲟⲡяⲧь ⲣⲉⲱυⲗ ⲙⲟύ ⲭⲩύ ⲏⲉ ⲥ ⲕⲉⲙ ⲏⲉ ⲇⲉⲗυⲧь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲭⲩёⲙ ⲧⲃⲟю ⲙⲁⲧь ⳃⲁ ⲣⲁⳅⲙⲉⲏυⲣⲟⲃⲁⲗ ⲁ ⲟⲏⲁ ⲟⲧ ⳝⲗⲁⲅⲟⲇⲁⲣⲏⲟⲥⲧυ ⲟⳝ ⲙⲟύ ⲭⲩύ ⲥⲃⲟю ⲡυⳅⲇⲩ ⲥⲧёⲣⲗⲁ ⲏⲁ ⲉⳅ ⲉⳅ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟю ⲙⲁⲧь ⳃⲁ ⲭⲩёⲙ ⲣⲁⲥⳡⲉⲗⲉⲏυⲗ ⲁ ⲟⲏⲁ ⲇⲁⲯⲉ ⲃ ⲧⲁⲕⲟⲙ ⲡⲟⲗⲟⲯⲉⲏυυ ⲥⲙⲟⲅⲗⲁ ⲟⲧⲥⲟⲥⲁⲧь ⲙⲏⲉ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲧь ⲏⲉ ⲙⲟⲯⲉⲧ ⲡⲟⲏяⲧь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲏⲉ ⲃⲥⲉⲅⲇⲁ ⳝⲩⲇⲉⲧ ⲇⲉⲣⲯⲁⲧь ⲏⲁⲇ ⲏⲉύ ⲃⲗⲁⲥⲧь ⲧⲁⲕ ⲧⲟ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲭⲩёⲙ ⲧⲃⲟю ⲙⲁⲧь ⲡⲗⲟⲙⳝυⲣⲟⲃⲁⲗ ⲉύ ⲇⲁⲯⲉ ⲕ ⲥⲧⲁⲙⲁⲧⲟⲗⲟⲅⲩ ⲭⲟⲇυⲧь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲣⲁⳅⲣⲉⳅⲁⲗ ⲁ ⲟⲏⲁ ⲡⲟⳝⲉⲯⲁⲗⲁ ⲕ ⲧⲃⲟⲉⲙⲩ ⳝⲁⲧυ υ ⲡⲟⲕⲁⳅⲁⲗⲁ ⲟⲧⲣⲉⳅⲁⲏⲩю ⲡυⳅⲇⲩ ⲕⲁⲕ ⲡⲣυⲕⲟⲗ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲭⲩёⲙ ⲧⲃⲟю ⲙⲁⲧь ⲏⲁⲩⳡυⲗ ⲡυⲥⲁⲧь ⲏⲟ ⲟⲏⲁ ⲡⲗⲟⲭⲟ ⲃⲟⲥⲡⲣυⲏυⲙⲁⲉⲧ ⲩⳡⲉⲏυя υ ⲏⲁⳡυⲏⲁⲉⲧ ⲥⲟⲥⲁⲧь ⲏⲁ ⲁⲃⲧⲟⲙⲁⲧⲉ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>я ⲥⲧⲣⲉⲗяⲗ ⲃ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲃыⲥⲧⲣⲉⲗυⲗ υ ⲟⲏⲁ ⲧⲃⲁⲣь ⲟⲯυⲗⲁ υ ⲏⲁⳡⲁⲗⲁ ⲡⲟⲗⳅⲧυ ⲕ ⲙⲟⲉⲙⲩ ⲭⲩю 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲧь ⲣⲉⲕⲟⲣⲧⲥⲙⲉⲏⲕⲁ ⲡⲟ ⲥⲟⲥⲁⲏυю ⲙⲟⲉⲅⲟ ⲭⲩя ⲉё ⲣⲉⲕⲟⲣⲇ ⲇⲁⲯⲉ ⲧⲃⲟύ ⳝⲁⲧя ⲏⲉ ⲙⲟⲯⲉⲧ ⲡⲟⳝυⲧь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲩ υ ⳡё ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲥⲟⲥⲁⲗⲁ ⲏⲉ ⲏⲁⲇⲟ ⲟⲧⲣυцⲁⲧь ⲃⲉⲇь ⲧы ⲧⲟⲯⲉ ⳅⲁⲡⲟⲇⲟⳅⲣⲉⲏ ⲃ эⲧⲟⲙ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲣⲁⳅⲕⲩⲙⲁⲣυⲗ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲇⲁ ⲧⲁⲕⲟύ ⲥⲧⲉⲡⲉⲏυ ⳡⲧⲟ ⲟⲏⲁ ⲉⲗυ ⲉⲗυ ⲇⲟⳝⲣⲁⲗⲁⲥь ⲇⲟ ⲇⲟⲙⲁ ⲇⲁⲯⲉ ⲡⲟ ⲇⲟⲣⲟⲅⲉ ⲟⲏⲁ ⲩⲥⲡⲉⲗⲁ ⲕⲟⲙⲩ ⲧⲟ ⲟⲧⲥⲟⲥⲁⲧь ⲱⲁⲗⲁⲃⲁ ⲯⲁⲗⲕⲁя 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲩ υ ⳡё ⲧы ⲙⲟⲯⲉⲱь я ⲯⲉ ⲥⲃⲟυⲙ ⲭⲩёⲙ ⲧⲃⲟυ ⲙыⲥⲗυ ⲧⲁⲕ ⲧⲟ ⲡⲉⲣⲉⲥⲧⲣⲟυⲗ ⲇⲩⲣⲉⲏь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲉ ⲙⲟⲅⲩ ⲥⲕⲁⳅⲁⲧь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲥⲟⲥёⲧ ⲃⲥⲉⲙ ⲟⳡⲉⲏь ⳡⲁⲥⲧⲟ ⲃⲉⲇь ⲃⲟⳅⲗⲉ ⲥⲃⲟⲉⲅⲟ ⲭⲩя я ⲃυⲯⲩ ⲉё ⲕⲁⲯⲇыύ ⲇⲉⲏь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯", 
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲩ ⲧⲃⲟя ⲙⲁⲧь ⲩⲯⲉ ⲡⲟ ⳝⲗⲁⲧⲩ ⲙⲏⲉ ⲥⲟⲥёⲧ ⲏⲟ ⲉύ ⲏⲉ ⲭⲃⲁⲧⲁⲉⲧ ⲥⲧυⲙⲩⲗⲁ ⲙⲟⲯⲉⲧ ⲧⲃⲟⲉⲙⲩ ⳝⲁⲧυ ⲭⲩёⲙ ⲃⲉⲏы ⲃⲥⲕⲣыⲧь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟύ ⲭⲩύ ⲃ ⲣⲁⲙⲕⲩ ⲡⲟⲥⲧⲁⲃυⲗ υ ⲧⲉⲡⲉⲣь ⲃы ⲃⲥⲉύ ⲥⲉⲙьёύ υⲙ ⲗюⳝⲩⲉⲧⲉⲥь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲡⲟ ⲡⲣυⲕⲟⲗⲩ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲏⲁ ⲗⲩⲏⲩ ⳅⲁⲕυⲏⲩⲗ ⲁ ⲟⲏⲁ ⲇⲁⲯⲉ ⲧⲁⲙ ⲃ ⲡⲉⲣⲇⲁⳡⲉⲗⲟ ⲕⲟⲙⲩ ⲧⲟ ⲇⲁⲗⲁ ⲟⲣⲏυ ⲥ эⲧⲟύ ⲱⲗюⲭυ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲙⲟⲅⲩ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲭⲩёⲙ ⲃⳅяⲧь ⲏⲁ ⲡⲣⲟⲅυⳝ ⲏⲟ ⲏⲉ ⲭⲟⳡⲩ ⲃⲉⲇь ⲟⲏⲁ ⲥⲧⲟυⲧ ⲣⲁⲕⲟⲙ υ ⲯⲇёⲧ ⲕⲟⲅⲇⲁ я ⲉё ⲃыⲉⳝⲩ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲣⲁⲥⲱυⲣυⲗ ⲅⲗⲁⲏⲇы ⲭⲩёⲙ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲧⲟ ⲧⲉⲡⲉⲣь ⲟⲏⲁ ⳝⲟⲗьⲱⲉ ⲙⲟⲯⲉⲧ ⲟⲡⲣⲁⳝⲁⲧыⲃⲁⲧь ⲙⲟύ ⳡⲗⲉⲏ ⲥⲃⲟυⲙ ⲣⲧⲟⲙ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲉ ⲥυⲗьⲏⲟ ⲃьⲉⳝⲁⲗ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲗⲩⲡⲟύ ⲏⲟ ⲟⲏⲁ ⲟⲧⲕⲗюⳡυⲗⲁⲥь ⳃⲁ ⲡⲣⲟⲥⲏёⲧьⲥя ⲡⲟ ⲏⲟⲃⲟύ ⲉё ⲡⲟⲉⳝⲩ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲁ ⲏⲉⲅⲁⲧυⲃⲉ ⲉⳝⲁⲗ ⲙⲁⲧь ⲧⲃⲟю ⲃⲉⲇь ⲟⲏⲁ ⳅⲁⲉⳝⲁⲗⲁ ⲃыⲣыⲃⲁⲧьⲥя ⳅⲁ ⳡⲧⲟ я ⲉύ ⲩⲉⳝⲁⲗ ⲗⲉⳃⲁ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲣⲁⳅⲟⲣⲃⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲏⲁ ⳡⲁⲥⲧυ ⲧⲉⲣь ⲧы ⲉⲇυⲏⲥⲧⲃⲉⲏыύ ⲕⲧⲟ ⳝⲩⲇⲉⲧ ⲙⲟύ ⲭⲩύ ⲇⲟ ⲩⳝⲟя ⲥⲟⲥⲁⲧь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲣⲁⲥⲧⲣⲟⲅⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲕⲟⲅⲇⲁ ⲭⲩёⲙ ⲃьⲉⳝⲁⲗ ⲉύ ⲡⲟ ⲅⲩⳝⲁⲙ ⲃⲉⲇь ⲕⲁⲕ ⲙы ⲡⲟⲙⲏυⲙ я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⲏьⲱⲉ ⲣⲁⳅυⳝⲃⲁⲗ ⲁ ⳃⲁⲥ ⲡⲣⲟⲥⲧⲟ ⲣⲁⲥёⲕ ⲟⲏⲁ ⲣⲁⲇⲁ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲧь ⲡⲟⲥⲧⲣⲟυⲗ ⲟⳝⲟⲣⲟⲏⲩ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⲏⲟ ⲥ ⲕⲁⲯⲇыⲙ ⲩⲇⲁⲣⲟⲙ ⲡⲟ ⲥⲧⲉⲏⲁⲙ эⲧⲟύ ⲟⳝⲟⲣⲟⲏы я ⲃⲥё ⳝⲗυⲯⲉ ⲕ ⲅⲗⲟⲧⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲩⲭⲉ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲙⲟύ ⲭⲩύ ⲩⲯⲉ ⲏⲁ ⲥⲧⲟⲗьⲕⲟ ⲃыⲣⲟⲥ ⲃ ⲅⲗⲁⳅⲁⲭ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳡⲧⲟ ⲟⲏⲁ ⲥⲟⲥёⲧ ⲉⲅⲟ ⲙⲉⲥⲧⲟ ⳅⲁⲃⲧⲣⲁⲕⲁ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲣⲁⳅⲙⲩⲣⲟⲃⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲕⲟⲅⲇⲁ ⲟⲏⲁ ⲏⲉ ⲙⲟⲅⲗⲁ ⲃыⳝⲣⲁⲧьⲥя υⳅ ⳅⲁ ⳡⲉⲅⲟ ⲧⲉⲡⲉⲣь ⲟⲏⲁ ⲡⲟ ⲯυⳅⲏⲉⲏⲟ ⲙⲏⲉ ⲇⲟⲗⲯⲏⲁ ⲟⲧⲥⲁⲥыⲃⲁⲧь ⲁ ⲡⲟⲧⲟⲙ ⲧы ⲉё ⲥⲙⲉⲏυⲱь ⲡⲣⲁⲃⲇⲁ ⲯⲉ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲁⲕυⲏⲩⲗ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲕⲁⳝυⲏⲩ ⳅⲁ ⲧⲟ ⳡⲧⲟ ⲟⲏⲁ ⲣⲉⲱυⲗⲁ ⲟⲥυⲗυⲧь ⲙⲟύ ⲭⲩύ ⲥⲃⲟυⲙ ⲣⲧⲟⲙ ⲡⲩⲥⲧь ⲧⲁⲕⲁя ⲱⲁⲃⲕⲁ ⲇⲁⲯⲉ ⲏⲉ ⲡυⲧⲁⲉⲧ ⲏⲁⲇⲉⲯⲇы 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲁⲅⲟⲣⲏⲩⲗ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩёⲙ ⲡⲣⲟⲥⲧⲟ ⲡⲟ ⲡⲣυⲏцυⲡⲩ ⲏⲟ ⲟⲏⲁ ⲇⲁⲯⲉ ⲧⲁⲕ ⲣⲉⲱυⲗⲁ ⲇⲁⲧь ⲙⲏⲉ ⲃ ⲡυⳅⲇⲩ ⲕⲁⲕ ⳝыⲗⲁ ⲱⲗюⲭⲟύ ⲧⲁⲕ υ ⲟⲥⲧⲁⲗⲁⲥь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲙы ⲡⲟⲥⲡⲟⲣυⲗυ ⲥ ⲟⲧцⲟⲙ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲥⲟⲥⲁⲗⲁ ⲙⲏⲉ ⲏⲉ ⳝⲟⲗьⲱⲉ 200 ⲣⲁⳅ ⲃ ⲇⲉⲏь ⲏⲟ ⲟⲏ ⲡⲣⲟυⲅⲣⲁⲗ ⲃⲉⲇь ⲩⲃυⲇⲉⲗ ⲕⲁⲕ ⲟⲏⲁ ⲟⲧⲥⲁⲥыⲃⲁⲉⲧ ⲙⲏⲉ ⲃ ⲯυⲃⲩю 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟю ⲙⲁⲧь ⲡⲉⲣⲃыύ ⲣⲁⳅ ⳅⲁ ⲕⲩⲥⲟⲕ ⲥⲁⲗⲟ ⲃыⲉⳝⲁⲗ ⲁ ⲟⲏⲁ ⲣⲁⲇⲟⲃⲁⲗⲁⲥь ⳡⲧⲟ ⲙⲟⲯⲉⲧ ⲏⲁⲕⲟⲣⲙυⲧь ⲧⲉⳝя ⲏⲟ ⲕⲁⲕ ⲡⲟⲉⲗ ⲥⲗυⳅⲉⲏь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲡⲟⲡⲣⲟⳝⲩύ ⲉⳃё ⲣⲁⳅ ⲥⲕⲁⳅⲁⲧь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲡⲉⲣⲉⲃⲉⲇⲁⲗⲁ ⲥⲧⲟⲗьⲕⲟ ⲕⲗёⲃыⲭ ⲭⲩёⲃ я ⲧⲉⳝя ⲩⲉⳝⲩ ⲭⲩёⲙ ⲃⲉⲇь ⲟⲏⲁ ⲏⲁ ⲟⲧⲥⲟⲥⲉ ⲡⲣυⳅⲏⲁⲃⲁⲗⲥь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥⲁⲙыύ ⲗⲩⳡⲱυύ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲡⲟ ⳅⲃⲉⲣⲥⲕυ ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ ⲟⲏⲁ ⲃ ⲱⲟⲕⲉ υ ⲇⲩⲙⲁⲉⲧ ⳡⲧⲟ эⲧⲟ ⲗюⳝⲟⲃь ⲏⲟ я ⲡыⲧⲁюⲥь ⲃⲕⲁⳡⲁⲧь ⲉё ⲥⲡⲉⲣⲙⲁⲕⲟⲙ ⳡⲧⲟⳝы ⲟⲏⲁ ⲡⲉⲣⲉⲇⲟⳅⲏⲩⲗⲁⲥь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲩ υ ⳡё ⲙы ⲧⲉⲡⲉⲣь ⲥ ⲧⲃⲟυⲙ ⳝⲁⲧⲉύ ⲇⲣⲩⳅья ⲡⲟⲥⲗⲉ ⲧⲟⲅⲟ ⲕⲁⲕ я ⲇⲁⲗ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕⲉ ⲏⲁ ⲕⲗыⲕ ⲟⲏ ⲩⳅⲏⲁⲗ ⳡⲧⲟ ⲟⲏⲁ ⲯⲁⲗⲕⲁя ⲱⲗюⲭⲁ υ ⲥⲇⲁⲗ ⲉё ⲙⲏⲉ ⲃ ⲣⲁⳝⲥⲧⲃⲟ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲧь ⲥⲏⲁⳡⲁⲗⲁ ⲇⲩⲙⲁⲗⲁ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲏⲉ ⲃыⳅыⲃⲁⲉⲧ ⳅⲁⲃυⲥυⲥⲙⲟⲥⲧ ⲏⲟ ⲥ ⲕⲁⲯⲇыⲙ ⲣⲁⳅⲟⲙ ⲥⲟⲥⲁⲗⲁ ⲃⲥё ⳝⲟⲗьⲱⲉ υ ⳝⲟⲗьⲱⲉ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲁ ⲣⲁⳅⲟⲅⲣⲉⲃ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲟⲉⳝⲁⲗ ⲁ ⲡⲟⲧⲟⲙ ⲧⲃⲟύ ⳝⲁⲧя ⲣⲉⲱυⲗ ⲙⲏⲉ ⲡⲟ ⲫⲁⲏⲩ ⲟⲧⲥⲟⲥⲁⲧь я ⲧⲉⲡⲉⲣь ⲇⲩⲙⲁю ⲩ ⲃⲁⲥ ⲃⲣⲟⲯⲇёⲏⲟⲉ ⲙⲟύ ⲭⲩύ ⲥⲟⲥⲁⲧь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲙⲁⲙⲩⲗьⲕⲁ ⲧⲃⲟя ⲣⲟⲇⲏⲉⲏьⲕⲁя ⳅⲁⲉⳝⲁⲏⲏⲁя ⲕⲩⲣυцⲁ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟυ ⲣⲟⲇυⲧⲉⲗυ ⲟⲡⲩⳃⲉⲏы ⲃыⳝⲗяⲇⲕυ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲩ ⲧⲉⳝя ⲙⲁⲧь ⲥⲣⲁⲏⲁя ⲱⲗюⲭⲁ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>υⲥⲡυⳅⲇяⳡⲩ я ⲧⲃⲟю ⲙⲁⲙⲕⲩ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⳃⲁⲥ ⲃъⲉⳝⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲧь υⲙⳝⲉцυⲗⲕⲁ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲇⲁ ⲧⲃⲟя ⲙⲁⲧь ⲅⲟⲃⲏⲟⲉⲇⲕⲁ ⲧⲩⲡⲁⲣыⲗⲁя 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲩ ⲧⲉⳝя ⲃⲥя ⲥⲉⲙья ⲥⲟⲥⲧⲟυⲧ υⳅ ⲡυⲇⲟⲣⲟⲃ υ ⲗⲉⳅⳝυяⲏⲟⲕ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧы ⳝⲗя ⲧⲩⲧ ⲥⲗυⲱⲕⲟⲙ ⲧⲟ ⲏⲉ ⲁⲭⲩⲉⲃⲁύ ⲩⲉⳝⲟⲕ ⲃⲁⲫⲉⲗьⲏыύ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲥⲩⳡⲁⲣⲁ ⲧы ⲡⲣυⲡυⳅⲇⲏⲩⲧⲁя 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲥⲇⲟⲭⲏυ ⲅⲏυⲇⲁ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⳅⲩⳝы ⲧⲟ ⲃыⲡⲁⲗυ ⲉⲡⲧυ,ⲟⲧ υⳅⳝыⲧⲕⲁ ⲥⲡⲉⲣⲙы ⲃ ⲧⲃⲟⲉⲙ ⲃⲇⲟⲗь ⲡⲣⲟⲉⳝⲁⲏⲏⲟⲙ ⲏⲁ ⲭⲩύ ⲉⳝⲁⲗьⲏυⲕⲉ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧы ⲥⲁⲙ ⲃыⳝⲗяⲇⲟⲕ ⲟⲡυⳅⲇⲉⲏⲉⲃⲱυύ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>Ⲕⲁⲕ ⲃы υ ⲡⲣⲟⲯυⲃⲉⲧⲉ... ⲡⲣⲁⲃⲇⲁ ⲏⲉ ⲇⲟⲗⲅⲟ..... ⲩⲣⲟⲇы υ ⲡυⲇⲟⲣы ⲇⲟⲗⲅⲟ ⲏⲉ ⲯυⲃⲩⲧ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧы ⲥⲁⲙ ⲃыⳝⲗяⲇⲟⲕ ⲟⲡυⳅⲇⲉⲏⲉⲃⲱυύ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧы ⲡⲟⲉⳝⲉⲏь ⲱⲁⲗяⲃυⲥⲧⲁя 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲙы ⲥ ⲡⲣυяⲧⲉⲗяⲙυ ⲥⲉⲇⲏя ⲃⲙⲉⲥⲧⲟ ⲣⲁⳝⲟⲧы ⲇⲗя ⲡⲣυⲕⲟⲗⲁ ⲥ ⲧⲃⲟⲉύ ⲙⲁⲙⲟύ ⳝⲁⲗⲟⲃⲁⲗυⲥь ⲡⲟⲇ ⲩⳝⲟύⲏыύ ⲙⲩⳅⲟⲏ, ⲁ ⲧы ⲏⲁⲙ ⲡυⲃⲟ ⲡⲟⲇⲏⲟⲥυⲗ υ ⲟⳝⲟυ ⲡⲟⲡⲣⲁⲃⲗяⲗ ⲅыⲅы ⳝⲗя 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲉⳝя ёⳝⲁⲏⲏыύ ⲧы ⲥⲧⲣⲁⲭⲟⳅⲁⲗⲩⲡυⳃⲉ ⲇⲁⲯⲉ ⲏⲉⲕⲟⲙⲩ ⳝⲩⲇⲉⲧ ⲃⲥⲡⲟⲙⲏυⲧь,ⲕⲟⲅⲇⲁ ⲧы ⲥⲇⲟⲭⲏυⲱь ⲩⲉⳝⲁⲕ!!! 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>я ⲧⲉⳝя ⲥⲟⳝⲥⲧⲃⲉⲏⲏⲟⲣⲩⳡⲏⲟ ⲩⲏυⳡⲧⲟⲯⲩ ⲡⲁⲇⲗⲁ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧы ⳡⲉⲣⲧ ⲇⲉⲃяⲧυⲥⲧⲃⲟⲣⳡⲁⲧыύ υⲇυ ⳅⲁⲗⲩⲡⲩ ⲟⳝⲗυⳅыⲃⲁύ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲇⲁ я  ⲥⲙⲉⲣⲧь ⲧⲃⲟя ⲙⲗⲁⲇⲉⲏⳡⲉⲥⲕⲁя 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲥⲩⳡⲕⲁ ⲡⲟⲅⲁⲏⲁя ⳡⲧⲟ ⲯⲉ ⲧы ⲡⲁⲥⲧь ⲥⲃⲟю ⳅⲁⲭⲗⲟⲡⲏⲩⲗ ⲡⲉⲧⲩⲭ ⲡⲟⲧыⲕⲁⲏыύ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>я ⲇⲣⲁⲗ ⲧⲃⲟύ ⲣⲟⲧ ⲕⲟⲧⲟⲣыύ ⳝыⲗ ⲏⲁⲡⲟⲗⲏⲉⲏ ⲙⲟⲉύ ⲙⲟⳡёύ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⳝⲉⲗⲁя ⲕⲟⲏⳡь ⲡⲣⲟⲏⳅυⲗⲁ ⲅⲗⲁⲏⲇы ⲧⲃⲟⲉύ ⲡⲣⲟⲥⲧυⲧⲩⲧⲟⳡⲏⲟύ ⲙⲁⲙы ⲁ ⲟⲧⲉц ⲏⲉ ⳅⲏⲁя ⳡⲧⲟ ⲇⲉⲗⲁⲧь ⲏⲁⳡⲁⲗ ⲗυⳅⲁⲧь ⲙⲟⲉύ ⳝⲁⳝⲕⲉ ⲥⲉⲇыⲉ ⲃⲟⲗⲟⲥы ⲏⲁ ⲙⲟⲣⳃυⲏυⲥⲧⲟⲙ ⲗⲟⳝⲕⲉ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧы ⲕⲁⲣⲗⲁⲏ ⲉⳝⲏⲩⲧыύ υⲇυ ⲥⲟⲥυ ⲭⲩύ ⲡⲁⲡυⲏ ⲙⲣⲁⳅь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲙⲟⲭⲏⲁⲣыⲗⲁя ⲧⲉⳝⲉ ⲃ ⲣⲟⲧ ⲕⲟⲏⳡⲁⲗυ 3000 ⲭⲁⳡⲉύ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲁ, ⲭⲩύ ⲥ ⲧⲟⳝⲟύ , υⲧⲁⲕ ⲥⲉⲅⲟⲇⲏя ⲧы ⳝыⲗ ⲥⲗυⲱⲕⲟⲙ ⳝⲗυⳅⲕⲟ ⲡⲟⲇⲡⲩⳃⲉⲏ ⲕ ⲭⲩю 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⳅⲁⲃⲁⲗυ ⲥⲃⲟύ ⲡⲉⲣⲇⲁⲕ, υ ⲏⲉ ⲣⲁⲥⲥⲕⲣыⲃⲁύ ⲉⲅⲟ! 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧы ⲯ ⲕⲟⳡⲉⲅⲁⲣ ⲡⲟ ⲯυⳅⲏυ ⲥⲩⲕⲁ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟё ⲙⲉⲥⲧⲟ ⲏⲁ ⳝⲟⲗⲟⲧⲉ ⲧⲣⲁⲭⲁⲧь ⲗяⲅⲩⲱⲉⲕ. 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲙⲁⲧь ⲕⲣыⲥⲁ ⲡⲟⲗⲩⲇⲟⲭⲗⲁя 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲕⲁⲣⲟⳡⲉ ⲧⲃⲟя ⲙⲁⲧь ⲃⲁⲅυⲏⲁ ⲧⲩⲡⲁя 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲏⲁⲭⲩя ⲙⲏⲉ ⳡⲧⲟ ⲧⲟ ⲇⲟⲕⲁⳅыⲃⲁⲧь ⲧⲁⲕⲟⲙⲩ ⲟⲧⲣⲉⳝью ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲙⲁⲙⲕⲁ ⲧⲃⲟя ⲅⲏυⲇⲁⲣⲁⲥⲕⲁ ⲟⲧⲭⲩяⲣυⲏⲁя 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟύ ⲟⲧⲉц ⲇⲣⲟⳡⲗυⲃыύ ⲭⲩⲉⲥⲟⲥⲏυⲕ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟⲉ ⲇⲉⲗⲟ ⲥⲟⲥⲁⲧь ⲁ ⲏⲉ ⲅⲁⲃⲕⲁⲧь ⲙⲩⲇⲗⲁⲏ. 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧы ⲡⲟⲏυⲙⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥυⲏⲟⲙⲡυⲕ ⲡυⳅⲇⲁⲕⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲱⲕυ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧы ⲡⲟⲏυⲙⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲇⲟⲣⲟⲯυⲧ ⲡυⳅⲇⲟύ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕυ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲙⲟύ ⲭⲩύ ⲧⲁⲏцⲉⲃⲁⲗ ⲧⲁⲏⲅⲟ ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>я ⲯⲉ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲣυⲭⲗⲟⲡⲏⲩⲗ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲕⲁⲕ ⲙⲩⲭⲩ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>я ⲧⲃⲟю ⲙⲁⲧь ⲅⲩⲥⲗяⲙυ ⲟⲧ ⲧⲁⲏⲕⲁ ⲉⳝⲁⲗ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲩ ⲧⲉⳝя ⲣⲟⲧ ⲕⲁⲕ ⲡыⲗⲉⲥⲟⲥ ,ⲃⲥⲁⲥыⲃⲁⲉⲧ ⲭⲩυ ⲥⲧⲣⲉⲙυⲧⲉⲗьⲏⲟ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>я ⲧⲃⲟю ⲙⲁⲧь ⳅⲁⲡⲉⲣⲁю ⲏⲁ ⳝⲁⲗⲕⲟⲏⲉ ⳡⲧⲟⳝы ⲟⲏⲁ ⲏⲟⳡью, ⲏⲉ υⲅⲣⲁⲗⲁ ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>я ⲯⲉ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲟⲧⲩⲱⲩ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ, ⲉⳝⲁⲏⲏⲁя ⲧы ⲥⲟⳝⲁⲕⲁ. ⲙⲟύ ⲭⲩύ ⲇⲉⲗⲁⲉⲧ ⲁⲭⲩⲉⲏⲏыⲉ υ ⲇⲟⳝⲣыⲉ ⲇⲉⲗⲁ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲣⲁⲃ ⲕⲟⲅⲇⲁ ⲉⳝⲉⲧ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲁⲏⲁⲗьⲏⲟύ. ⲕⲟⲏⳡⲉⲏⲏⲁя ⲧы ⲅⲁⲏⲇⲟⲏⲕⲁ?). я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲕⲉⲏⲧⲩⲭⲩ ⲃыⲉⳝⲩ), ⲥⲗыⲱυⲱь ⲏⲁⲉⳝⲁⲏⲏыύ ⳡⲉⲡⲩⲱⲏяⲕ. я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃ ⲣⲟⲧ ⲃыⲉⳝⲩ ⲕⲟⲏⳡⲏⲉⲏыύ ⲧы ⲣⲟⲧ ⳝⲗяⲇь ⲕⲟⲧⲟⲣыύ ⳝⲉⲣⲉⲧ ⲏⲁ ⲥⲉⳝя ⲥⲗυⲱⲕⲟⲙ ⲇⲟⲭⲩя. ⲥⲗыⲱυⲱь ⲟⲧьⲉⳝⲁⲏⲏыύ ⲉⲃⲣⲉύ?), я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃыⲧⲣⲁⲭⲁю υ ⲃыⲕυⲏⲩ ⲉё ⳅⲁⲥⲥⲁⲏыⲉ ⲧⲣⲩⲡ ⲥⲟⳝⲁⲕⲁⲙ ⳡⲧⲟ-ⳝы ⲟⲏυ ⲉё ⲥⲭⲁⲃⲁⲗυ ⲉⳝⲁⲏⲏⲩю ⲱⲁⲗⲁⲃⲩ. ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳡυⲥⲧⲟ ⲏⲁⲉⳝⲁⲏⲁⲏя ⲙⲟυⲙ ⲭⲩⲉⲙ. ⲥⲗыⲱυⲱь ⲃыⲥⲥⲁⲏыύ ⲡυⲇⲟⲣⲁⲥ. ⲙⲟύ ⲭⲩύ ⲃыⳝⲉⲣⲉⲧ ⲡⲟⳅⲩ ⲇⲗя ⲧⲟⲅⲟ ⳡⲧⲟ-ⳝы ⲃыⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ, υ ⲃыⳝⲉⲣⲉⲧ ⲁⲭⲩⲉⲏⲏю ⲡⲟⳅⲩ ⳡⲧⲟ-ⳝы ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⳝыⲗⲁ ⲇⲟⲃⲟⲗьⲏⲟύ. ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃⲥⲉⲣⲟⲃⲏⲟ ⲃыⲉⳝⲉⲧ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲁⲉⳝⲁⲏⲏⲩю, ⲧы ⳅⲏⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⳡυⲥⲧⲟ ⲱⲟⲱⲕⲁ ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя. ⲥⲗыⲱυⲱь ⲙⲣⲁⳅⲟⲧⲁ ⲉⳝⲁⲏⲏⲁя,я ⲕⲁⲕ-ⲧⲟ ⲣⲁⳅ ⲧⲣⲁⲭⲏⲩⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ υ ⲩ ⲏⲉё ⲡⲟⲧⲟⲙ ⲏⲁⳡⲁⲗⲥя ⲥⲡⲁⳅⲙ ⲡυⳅⲇы, ⲧы ⲙⲟⲯⲉⲱь ⳅⲁⲗⲉⳡυⲧь ⲟⳡⲕⲟ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲉⳝⲁⲏⲁя ⲧы ⲅⲁⲏⲇⲟⲏⲕⲁ?), я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲃыⲉⳝⲩ ⳝⲉⳅ ⲟⳝυⲇ ⲡⲟⲏυⲙⲁⲉⲱь ⲉⳝⲁⲏⲏыύ ⲧы ⲡⲉⲇυⲕ. 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯",
"<emoji document_id=5420085673413583049>🤍</emoji>ⲧⲃⲟя ⲥⲉⲙⲉύⲕⲁ ⲥⲟⳝⲥⲧⲃⲉⲏⲟⲥⲧь ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ! 𖥜<emoji document_id=5420085673413583049>🤍</emoji>𖦯"]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl5))
            await sleep(0.1)
            await sleep(time)

    async def демонcmd(self, message):
        """— Запускает модуль по указанной команде """
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message,
            "<b>Ⲙⲟⲇⲩⲗь #Ⲇⲉⲙⲟⲏ ⲡⲉⲣⲉⲥⲧⲁⲗ ⲉⳝⲁⲱυⲣⲟⲃⲁⲧь ⲧⲩⲱⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲱⲕⲉ. <emoji document_id=5175094382298137311>🌟</emoji></b>")
            return
        await utils.answer(
            message,
            "<b>Ⲙⲟⲇⲩⲗь #Ⲇⲉⲙⲟⲏ ⲏⲁⳡⲁⲗ ⲉⳝⲁⲱυⲣⲟⲃⲁⲧь ⲧⲩⲱⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲱⲕⲉ. <emoji document_id=5175094382298137311>🌟</emoji></b>"
            "<b>Ⳡⲧⲟⳝы ⲟⲥⲧⲁⲏⲟⲃυⲧь ⲡⲣⲟⲡυⲱυ.<code>.демон</code></b>"
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl6 = [ "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲁ ⳡⲗⲉⲏ ⲁⲃⲁⲏⲧⲁⲯⲏыύ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳡⲟ ⲙⲁⲙυⲏⲟύ ⲥⲣⲁⲕⲟύ ⲕⲣⲟⲙⲉ ⲭⲩёⲃ ⲗⲟⲃυⲗ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲁⲧцⲉⲡυⲗ ⲧя ⲃ ⲇⲩⲱⲉ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧёⲗⲕⲁ,ⲙⲟύ ⲭⲩύ ⲧⲃⲟύ ⲙυⲕⲣⲟ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲩⲣυⲏⲟύ ⲧя ⲟⲱⲡⲁⲣυⲙ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲕⲁⲕ ⲃⲉⲇьⲙⲁⲕ,ⲩ ⲙⲉⲏя ⲉⲥⲧь ⳅⲁⲇⲁⲏυⲉ ⲏⲁ υⲥⲧⲣⲉⳝⲗⲉⲏυя ⳡⲩⲇυⳃь,ⲏⲁ ⲟⳡⲉⲣⲉⲇυ ⲧⲃⲟя ⲙⲁⲙⲕⲁ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲯⲉ ⲧⲉ ⲧⲃⲟυ ⲅⲗⲁⳅⲏυцы ⲏⲁⲭⲩύ ⲃыⳝью υ ⲏⲁ ⲭⲩύ ⲥⲉⳝⲉ ⲟⲇⲉⲏⲩ υ ⲏⲁⳡⲏⲩ ⲉⳝⲁⲣυⲣⲟⲃⲁⲧь ⲧⲃⲟю ⲙⲁⲙⳅⲉⲗь <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲡⲟⳡⲉⲙⲩ ⲏⲁ ⲡⲉⲏυⲥⲉ ⲥⲧⲁⲅⲏυⲣⲩⲉⲱь <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳝⲉⳅ ⲱⲁⲏⲥⲟⲃ ⲉⳝёⲙ ⲙя<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳝⲉⳅ ⲕⲇ ⲉⳝёⲙ ⲧя<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲁⲙⲁⲏⲉύ ⲧⲃⲟⲉύ ⲃ ⲅⲟⲗьⲫ υⲅⲣⲁⲗ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲡⲉⲇυⲕⲁ ⲏⲁ ⳅⲟⲏⲉ ⲭⲩⲉⲙ ⲃⲟⲥⲡυⲧⲁⲗ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲟⲅⲟⲏяⲗⲁ ⲥыⲏⲕⲁ ⲱⲗюⲭυ ⲥⲡⲉⲣⲙⲟύ ⲏⲁ ⲉⳝⲗⲉ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲫⲣυⲕⲁ ⲃыⳝьⲉⲙ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲃ ⲙⲟⲙⲉⲏⲧⲉ ⲥⲟⲥёⲱь ⲙⲏⲉ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⲡⲁⲡⲁⲏя ⲧⲃⲟύ) <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲧⲉ ⲙⲉⲯⳝⲣⲟⲃьⲉ ⲣⲁⲥⲥⲉⳡёⲙ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳅⲁⲗⲩⲡⲁⲙυ ⲏⲁⳝⲉⲅυ ⲏⲁ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧυⲗьⲇы ⲙⲁⲧⲉⲣυ ⲩⲥⲧⲣⲟυⲙ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]υⲥⲕⲩⲥⲥⲏⲟ ⲣⲁⲥⲥⲉⲕⲕⲁю ⲏⲁ ⲇⲃⲟⲉ ⳅⲁⳝⲃⲉⲏⲏⲩю ⲧⲩⲱⲕⲉⲏцυю ⲡⲁⲡⲁⲏυ ⲧⲃⲟⲉⲅⲟ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲁⲙⲁⲏю ⲧⲃⲟю ⲃⲟ ⲃⲥⲉⲭ ⲡⲟⳅⲁⲭ ⲕⲁⲙⲁⲥⲩⲧⲣы ⲉⳝⲁⲗ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲉⳝⲁⲣυⲣⲩю υ ⲉⳝⲁⲱυⲣⲩⳝ ⲙⲉⲱⲟⲉ ⲉⳝⲁⲏⲏыύ ⲏⲁ ⲧⲉⳝⲉ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲇⲁⲃⲁύ ⲧⲁⲙ ⳅⲁⲭⲗёⳝыⲃⲁύⲥя ⲙⲟⳡёύ ⲙⲟⲉύ ⲩⲯⲉ))ⲭⲃыⲭыыⲃ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲗⲁⳝⲟⲏⲉⲣⲃⲏыύ ⲟⲏυⳃⲁⲗыύ ⲥыⲏⲟⲕ ⲇυⲕⲁⲣⲕυ ⲥⲟⲥυⲣⲩύ υ ⲙⲁⲥⲥυⲣⲩύ ⲃⲥяⳡⲉⲥⲕυ яύцⲁ ⲙⲟυ ⲩⲯⲉ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲩ ⲧы ⲧёⲗⲕⲁ ⲏⲁⲧⲩⲣⲉ ⲙⲟύ ⲭⲩύ ⲩⲧⲟⲙυⲗⲁ яⳅыⲕⲟⲙ ⲥⲃⲟυⲙ ⲱⲉⲣⲱⲁⲃыⲙ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ υⳅ ⲧⲉⳝя ⲇⲉⲙⲟⲏⲟⲃ υⳅⲅⲟⲏяⲉⲙ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳡⲗⲉⲏⲟⲙ ⲡⲣⲟⳝυⲗ ⲥⲉⲣⲇцⲉ ⲧⲃⲟё ⲥⲗⲟⲃⲏⲟ ⲟⲥⲥυⲏⲟⲃыⲙ ⲕⲟⲗⲟⲙ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲏⲉ ⲃⲁⲙⲡυⲣ я ⲧⲉⳝⲉ ⲥⲡⲉⲣⲙⲟύ ⲥⲃⲟⲉύ ⳡⲉⲥⲏⲟⳡⲏⲟύ ⲟⳝⲉⲥⲥυⲗυⲗ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲇυⲁⲅⲏⲟⲥⲧυⲣⲟⲃⲁⲗ ⲩ ⲧⲉⳝя ⲣⲁⲕ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲩⲥⲉⲗⲁⲥь ⲏⲁ ⲙⲟύ ⳡⲗⲉⲏ ⲥⲗⲟⲃⲏⲟ ⲏⲁ ⲧⲣⲟⲏ υ ⲃⲟⲟⳝⲣⲁⳅυⲗⲁ ⲥⲉⳝя цⲁⲣⲉⲃⲏⲟύ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲁ ⲭⲩύ ⲥⲁⳝⲗⲉⳅⲩⳝыύ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳝⲩⲕⲃⲉⲏⲏⲟ ⲥⲟⲥυ ⳡⲧⲟⲗⲉ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲩⲙⲥⲧⲃⲉⲏⲏⲟ ⲉⳝⲁⲗ ⲧя <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲡⲟⳡⲉⲙⲩ ⲟⲧ ⳡⲗⲉⲏⲁ ⲙⲟⲉⲅⲟ ⲡⲣяⳡⲉⲱьⲥя<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲃ ⲟⲕⲟⲡⲉ ⲧⲃⲟю ⲙⲁⲧь ⲥ ⲡⲁцⲁⲏⳡυⲕⲁⲙυ ⲉⳝⲁⲗυ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲃⲟю ⳝⲁⳝⲕⲩ ⲥⲟⲃⲕⲟⲃⲩю ⳝⲗяⲇь ⲉⳝⲁⲗ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲣⲁⲗⲗяⲕⲩ ⲣⲩⲏⲉⲧⲟⲃⲥⲕⲩю ⲭⲩⲉⲙ ⲡⲏⲩⲗ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲁⲇ ⳝⲉⳅⲇыⲭⲁⲏⲏыⲙ ⲧⲣⲩⲡⲟⲙ ⲧⲃⲟⲉύ ⲱⲗюⲭⲟⲙⲁⲧⲉⲣυ ⲏⲁⲇⲣⲩⲅⲁⲗⲥя <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲁⲏэⲡυⲇⲉⲙⲥⲧⲁⲏцυю ⲡⲟⲥⲧⲣⲟυⲗ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲃⲟя ⲙⲁⲧь υⳅ ⲥⲧⲗьⲏⲟύ ⲗюⳝⲃυ ⲕ ⲙⲟⲉⲙⲩ ⳡⲗⲉⲏⲩ ⲃыⲥⲧⲣⲟυⲗⲁ ⲇⲗя ⲏⲉⲅⲟ ⲡⲁⲙяⲧⲏυⲕ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲩ цⲉⲕⲃυ υⳅ ⲙⲁⲧⲉⲣυ ⲧⲃⲟⲉύ ⳡⲉⲣⲧⲉύ υⳅⲅⲟⲏяⲗ ⲭⲩⲉⲙ ⲥⲃⲟυⲙ цⲉⲗⲉⳝⲏыⲙ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲉⲏυⲥⲟⲡⲟⲇⲟⳝⲏыύ ⲁⲅⲣⲉⲅⲁⲧⲟⲙ ⲃыⳝьⲉⲙ ⲧⲉⳝя υⳅ ⲕⲟⲗυυ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲃⲁⲏⲱⲟⲧⲏⲩⲗ ⲧя <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲉⲏυⲥⲟⲙ ⲯⲃⲁⲗы ⲧⲉ ⲧⲃⲟυ ⲟⲧⲟⳝью<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲟⲧⲇⲁύ ⲇⲟⲗⲯⲏⲟⲉ ⲙⲏⲉ,я ⲥⲩⲙⲉⲗ ⲃыⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲧь υ ⲡⲣυ эⲧⲟⲙ ⲟⲥⲧⲁⲧьⲥя ⲥ ⳡⲗⲉⲏⲟⲙ, ⲁ ⲩ ⲏⲉё ⲧⲁⲙ ⳝⲗя ⲭυⲗυцⲉⲣы ⲃⲥяⲕυⲉ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳡⲗⲉⲏⲟⲇⲣⲟⳝυⲧⲉⲗьⲏⲟ ⲙⲟⳃью ⲩⲡⲣяⲙыⲙ ⲏⲁⲧυⲥⲕⲟⲙ ⲥυⲗы ⳡⲧⲟ ⲉⲥⲧь ⲇⲗя ⲧⲉⳝя ⲥⲙⲉⲣⲧⲉⲗьⲏⲟύ υⳅьⲉⳝⲁⲱυⲣⲩⲉⲙ ⲧя<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲃ ⲡⲟⳅⲉ ⲯⲩⲣⲁⲃⲗя <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲃⲟя ⲙⲁⲧь ⲯⲉⲣⲧⲃⲁ ⲙⲟⲉύ ⲕⲉⲫυⲣⲏⲟύ ⲥⲡⲉⲣⲙы <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥυⲫυⲗυⲥ ⲭⲩⲉⲙ ⲥⲃⲟυⲙ υⲥцⲉⲗυⲗ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲁⲕⲣⲟⲧⲟⲥⳝⲟⲣⲏυⲕ υⲗυ ⲧⲁⲕ ⲏⲁⳅыⲉⲙⲁя ⲣⲟⲧⲟⲃⲟя ⲡⲟⲗⲟⲥⲧь ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲧⲉⲣⲡⲉⲗⲁ ⲕⲣⲩⲱⲉⲏυⲉ ⲟⳝ ⲙⲟύ ⲭⲩύ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲁⲥⲧь ⲧⲃⲟⲉύ ⳝⲗяⲇⲟⲙⲁⲧⲉⲣυ ⲧⲉⲣⲡυⲧь ⲡⲟⲣⲁⲯⲁⲏυⲉ ⲡⲣⲟⲧυⲃ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ ⲃⲥⲉⲙⲟⲅⲩⳃⲉⲅⲟ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲧⲉⳝⲉ ⲏⲉ ⲡⲟⳅⲩⳝⲁⲙ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲧⲉⳝⲉ ⲇыⲣⲩ ⲃ ⲗⲟⳝⲉⲱⲏυⲕⲉ ⲧⲃⲟёⲙ ⲃыⲥⲃⲉⲣυⲗ υ яύцⲁⲙυ ⲅⲗⲁⳅⲏυцы ⲟⲧⳝυⲗ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲃ ⲥⲟⳡⲉⲗьⲏυⲕ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲡⲟⳡⲉⲙⲩ ⲧёⲗⲕⲁ ⲉⳝⲁⲏⲏⲁя ⲣⲉⲱυⲗⲁ ⲙⲏⲉ ⳅⲇⲉⲥь ⳡⲗⲉⲏ ⲙⲟύ ⳝⲟⲅⲟцⲁⲣⲥⲕυύ ⳅⲁⲧⲉⲣⲡⲉⲧь<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲡⲉⲣⲙⲟⲧⲟⳅⲟυⲇы ⲏⲁ ⲗⲟⳝⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲇⲏяⲗυ ⲫⲗⲁⲅ ⲥ ⲙⲟυⲙ ⲏⲉύⲙⲟⲙ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲩ ⲧя ⲡⲟ ⲃⲥⲉⲙ ⲡⲟⲏяⲧυяⲙ ⲙⲁⲧь ⲱⲁⲗⲁⲃⲁ ⲕⲣⲟⲙⲉ ⲃⲉⲣⲏⲟⲥⲧυ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲟⲙⲏю ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь ⲧⲣⲉⲡⲁⲗⲁ ⲡⲟⲇⲣⲩⲇⲁⲏяⲙ ⲥⲃⲟυⲙ ⲕⲁⲕ я ⲉё ⲏⲁ ⳡⲗⲉⲏⲉ ⲥⲃⲟёⲙ ⲕⲁⲧⲁⲗ,ⲟⲏυ ⳝыⲗυ ⲃⲟⲥⲧⲟⲣⲅⲉ υ ⲡыⲧⲁⲗυⲥь ⲃⲥяⳡⲉⲥⲕυ ⲃⲥⲧⲣⲉⲧυⲧьⲥя ⲥⲟ ⲙⲏⲟύ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲟⳡⲉⲙⲩ ⲧⲃⲟя ⲙⲁⲧь ⲥⲟⲥёⲧ ⳅⲁ ⲇⲃⲟυⲭ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⳅⲁⳡⲉⲙ ⲥⲡⲉⲣⲙⲟⲧⲟύ ⲙⲟⲉύ ⲃⲕυⲇыⲃⲁⲉⲱьⲥя υ ⲙⲁⲧⲉⲣυ ⲥⲃⲟⲉύ ⲟⲧⲭⲟⲇⲏяⲕ ⲟⲥⲧⲁⲃⲗяⲉⲱь<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁⲕⲟⲥⲧыⲗяⲗ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧⲟⲗьⲕⲟ ⳅⲁ ⲧⲟ ⳡⲧⲟ ⲟⲏⲁ ⲥⲇⲉⲗⲁⲗ ⲙⲏⲉ ⲡⲗⲟⲭⲟύ ⲙυⲏⲉⲧ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲙⲟυⲙ ⲙⲟⲅυⲗⲩ ⲥⲉⳝⲉ ⲣⲟύ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲯⲉ ⳅⲏⲁю ⳡⲧⲟ ⲧы ⲩⳝυⲃⲁⲉⲱьⲥя ⲡⲟ ⲏⲁⲱυⲙ ⲧⲉⲅⲁⲙ ⲕⲁⲕ ⲧⲃⲟя ⲙⲁⲧь ⲟⳝ ⲙⲟύ ⲡⲟⲗⲟⲃⲟύ ⲁⲅⲣⲉⲅⲁⲧ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲃыⲥⲉⲕⲩ ⲡⲣⲟⲡⲗⲉⲱυⲏы ⲏⲁ ⲉⳝⲗⲉ ⲧⲃⲟⲉⲅⲟ ⲗⲁⲧⲉⲏⲧⲁ ⲟⲧцⲁ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲣⲟⲡⲗⲉⲱυⲏы ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲥⲃⲟυⲙ ⲟⲥⲧⲁⲃⲗяю <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲟ ⳡⲉⲣⲉⲡⲩⲱⲕⲉ ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⲥⲧⲩⲕⲁⲗ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲟⲇυⳡⲁⲃⲱυύ ⳝⲗяⲇⲟⲫⲣυⲕⲟⲃыύ ⲥыⲏяⲣⲁ ⲃⲟⳅⲟⲙⲏυⲗ ⲥⲉⳝя ⲇⲟⲭⲩя ⲃⲁⲯⲏыⲙ υ ⲡⲟⲗⲩⳡυⲗ υⳅьёⳝ ⲧⲣⲉⲧьⲉύ ⲥⲧⲉⲡⲉⲏυ ⲃⲏⲉⲟⳡⲉⲣёⲇⲏⲟ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲁⳝⲉⲅυ ⲏⲁ ⲕⲩⲣⲅⲁⲏ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲅⲣⲩⲡⲡⲁⲙυ ⲇⲉⲗⲁⲉⲙ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲟⲗⲥⲧⲟⲙяⲧⲏыύ ⲃⲁⲫⲗⲟⲯⲟⲣ ⲧы ⲡⲟⳡⲉⲙⲩ ⲉⳃё ⲙⲟю ⳅⲁⲗⲩⲡⲩ ⲥⲟ ⲣⲧⲁ ⲏⲉ ⲇⲟⲥⲧⲁⲗ)<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⳝⲗⲁⲅⲟⲥⲗⲟⲃⲉⲏⲏыύ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⲟⲥⲉⲧⲣυⲏⲟⲃыύ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲟⲥёⲱь υⲙⲡⲉⲣⲁⲗυⲥⲧυⳡⲉⲥⲕυ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⲙⲁⲧь ⲧⲃⲟя<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⲥⲕⲩⲇⲟⲩⲙⲏыύ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⲟⲡⲟⲗⲟⲩⲙⲉⲃⲱυύ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⲧёⲗⲕⲁ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⲡⲣυⲏⲩⲯⲇёⲏⲏыύ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⲥⲗⲁⳝⲁⲕ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲟⲥёⲱь ⲟⳝыⲕⲏⲟⲃⲉⲏⲏⲟ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⲟⳝⲉⳅⲩⲙⲃⲱυύ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲉⲧⲉⲣⲡⲉⲗυⲃⲁ ⳝⲁⲗⲇⲩ ⲙⲟю юⲗⲟⳅυⲱь <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⳅⲁⳡⲉⲙ ⲡⲣυⲏяⲗⲥя ⲥⲟⲥⲁⲧь ⲕⲁⲕ ⲙⲁⲧь ⲧⲃⲟя<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲃⲩⲗьⲅⲁⲣⲏⲟ ⲉⳝⲁⲗ ⲧя <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲁⲙⲁⲱⲕⲩ ⲧⲃⲟю ⲏⲁ ⲥⲡυⲏⲉ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲉⳝⲁⲗυ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲗⲉⲉⲉ ⲭⲩⲉⲙ ⲩⲙⲁⲗυⳃⲁю ⲧя <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲃ ⲡⲣυⲡⲁⲇⲕⲉ ⳡⲗⲉⲏ ⲥⲟⲥёⲱь<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲟύ ⲭⲩύ ⳝⲟⲣⲟⳅⲇυⲗ ⲡⲣⲟⲥⲧⲟⲣыύ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲯⲉ ⲩⲯⲉ ⲃⲥⲉ ⲃⲟⳅⲙⲟⲯⲏыⲉ υ ⲏⲉ ⲃⲟⳅⲙⲟⲯⲏыⲉ υⲏⲧυⲙⲏыⲉ ⳅⲟⲏы ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲟⳝⲗⲁⳅυⲗ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲟⲥёⲱь ⲕⲁⲕ ⳡⲉⲱυⲣⲥⲕυύ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲧⲉⳝⲉ ⲩⲱυ ⲧⲃⲟυ ⲟⲧⲧяⲏⲉⲙ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲃ ⲙⲅⲏⲟⲃⲉⲏьⲉ ⳅⲁⲙⲩⲧυ ⲥⲃⲟύ ⲟⲧⲥⲟⲥ ⲫυⲣⲙⲉⲏⲏыύ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲁⲗⲟⲣⲁⳅⲩⲙⲏыύ ⲃыⳝⲗяⲇⲟⲕ ⲁⲗё ⲏⲁⲭⲩύ ⲏⲉ ⲥⲗыⲱⲩ ⲡυⲥⲕυ ⲧⲃⲟⲉύ ⲱⲗюⲭⲟⲙⲁⲧⲉⲣυ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲟⲣⲩ ⲧⲃⲟю ⲣⲁⳝⲥⲕⲟⲡυⲇⲟⲣⲥⲕⲩю ⲟⳝⲏⲉⲥёⲙ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲉⲏυⲥⲟⲙ ⲥⲃⲟυⲙ ⲡⲣυⲙⲯⲁю ⲡⲩⲗьⲥⲁⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳝⲗυⲯⲉ ⲕ ⳅⲟⲏⲉ ⲥⲟⲡⲣυⲕⲟⲥⲏⲟⲃⲉⲏυя<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲁυⳡⲉύⲣⲏⲉⲱυύ ⲥыⲏⲟⲕ ⲱⲗюⲭυ ⲧы ⲧⲟⲗьⲕⲟ ⲕⲟⲥⲧυ ⲥⲃⲟυⲙ ⲏⲉ ⲧⲉⲣяύ ⲡⲟ ⲡⲩⲧυ ⲕ ⲟⲧⲥⲧⲩⲡⲗⲉⲏυю<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲃⲉⲣⲱυⲙ ⲡⲣⲁⲃⲟⲥⲩⲇυⲉ ⲏⲁ ⲉⳝⲁⲗⲟⲙ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲃⲟύ ⲟⲧⲉц ⲡⲟⲅⲟⲗⲟⲃⲏыύ ⲃⲁⲫⲗυⲧⲉⲗь ⲙⲟⲉύ ⳅⲁⲗⲩⲡы<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲡⲟⳡⲉⲙⲩ ⲉⳃё ⲏⲉ ⲥⲟⲙⲕⲏⲩⲗⲥя ⲃ ⲕⲟⲗⲗⲉⲏⲟⲗⲉⲕⲧⲉⲃⲟⲙ υ ⲏⲉ ⲏⲁⳡⲁⲗⲁ ⲙⲟⲗυⲧь ⲙⲉⲏя ⲟ ⲡⲟⳃⲁⲇⲉ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥ ⲏⲉⲧⲉⲣⲡⲉⲏυⲉⲙ ⲭⲩⲉⲙ ⲧя υⳅⳝυⲃⲁю <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲧя ⳝⲩⲇⲁⲣⲁⲯⲩ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲁⳑⳑⲁⲏ ⲁⲕⲃⲁʀ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲣⲟⲯёⲅ ⲧⲉⳝⲉ ⲅⲗⲟⲧⲕⲩ ⲥⲃⲟυⲙ υⲏⲫⲉⲣⲏⲁⲗьⲏыⲙ ⳡⲗⲉⲏⲟⲙ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲟⲥⲉⲕⲩ ⲧⲉⳝя ⲏⲁⲇⲃⲟⲉ ⲥⲃⲟυⲙ ⲁⲫⲣⲟⳡⲗⲉⲏⲟⲙ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲧυⲡⲁ ⲕⲁⲕ ⲡⲉⲱⲕⲁ ⲉⳝⲁⲏⲏⲁя ⲥⲟⲥёⲱь ⲙⲏⲉ ⲧⲩⲧ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙы ⳃⲁⲥ ⲥ ⳡⲉⳡⲉⲏцⲁⲙυ ⲡⲟⲇьⲉⲇⲉⲙ ⲧⲉⳝⲉ ⲱⲩⲫⲗяⲇⲕⲩ ⲣⲟⲃⲏяⲧь <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲁⲏυⲁⲕⲁⲗьⲏⲟ ⲉⳝⲁⲣυⲣⲟⲃⲁⲗ ⲧя <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲣυⲯⲙυⲥь ⲩⲯⲉ ⲕ ⲙⲟⲉⲙⲩ ⳡⲗⲉⲏⲩ ⲥⲇⲉⲗⲁύ ⲏⲁⲙ ⲟⳝⲟυⲙ ⲡⲣυяⲧⲏⲟ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲕⲁⲕ ⲧы ⲙⲟⲯⲉⲱь ⲃⲗⲁⲥⲧⲃⲟⲃⲁⲧь ⲥⲃⲟⲉύ ⲥⲩⲇьⳝⲟύ ⲉⲥⲗυ ⲏⲁⲇ ⲧⲟⳝⲟύ ⲥⲧⲟυⲧ ⲙⲟύ ⳝⲟⲅⲟⲡⲟⲇⲟⳝⲏыύ ⲡⲉⲏυⲥ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳡⲟ ⲧы ⲧⲁⲕ ⳝыⲥⲧⲣⲟ ⲕ ⲱⲉⲣυⲏⲕⲉ ⲧⲟ ⲙⲟⲉύ ⲡⲣυⲡⲁⲗ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲉⳝⲉ ⲃυⲥⲗⲟⲩⲭⲟⲙⲩ ⲥыⲏⲕⲩ ⳝыⲥⲧⲣⲟ ⲧⲩⲧ ⲡⲁⲕⲗυ ⲃыⲣⲃⲉⲙ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⳃⲁⲥ ⲡⲟⲇⲕυⲏⲩ ⲙⲟⲏⲉⲧⲕⲩ ⲃⲃⲉⲣⲭ υ ⳅⲁ ⲃⲣⲉⲙя ⲉё ⲡⲟⲗёⲧⲁ ⲧⲃⲟя ⲙⲁⲧь ⲇⲟⲗⲯⲏⲁ ⳝⲩⲇⲉⲧ ⲟⲧⲥⲟⲥⲁⲧь ⲙⲏⲉ ⳡⲗⲉⲏ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲡⲟⳡⲉⲙⲩ ⲃⲥⲉ ⲉⳃё ⲭⲩύ ⲙⲟύ ⲃⲧⲉⲣⲡⲗυⲃⲁⲉⲱь<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳡⲟ ⲧы ⲧⲁⲕ ⲧⲩⲅⲟ ⲏⲁ ⲉⳝⲁⲗυⳃⲉ ⲥⲃⲟё ⲅυⳝⲣυⲇⲏⲟⲉ ⲡⲉⲏυⲥ ⲙⲟύ ⲡⲣυⲏυⲙⲁⲉⲱь <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲏⲁⲥⲧⲟⲗьⲕⲟ ⳝыⲥⲧⲣⲟ ⲉⳝⲁⲱυⲣⲟⲃⲁⲗ ⲃⲁⲅυⲅυⲗьⲏⲟⲉ ⲡⲣⲟⲥⲧⲣⲁⲏⲥⲧⲃⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳡⲧⲟ ⲩⲥⲡⲉⲗ ⲣⲁⲥⲥⲉⳡь ⲃⲣⲉⲙⲉⲏⲏⲩю ⲗυⲏυю υ ⲩⲃυⲇⲉⲧь ⲥⲃⲟυⲙυ ⲅⲗⲁⳅⲁⲙυ ⲕⲁⲕ ⲅⲏⲟⳝяⲧ ⲧⲃⲟю ⲥⲟⲃⲕⲟⲃⲩю ⲡⲣⲟⳝⲗяⲧь ⳝⲁⳝⲕⲩ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟυⲙ ⳡⲗⲉⲏⲟⲙ ⲃ 18 ⲃⲉⲕⲉ ⲗⲟⳝⲟⲧⲟⲙυю ⲡⲣⲟⲃⲟⲇυⲗυ,ⲏⲟ ⲃⲥⲉ ⲡⲟⲡыⲧⲕυ ⲥⲇⲉⲗⲁⲧь ⲥ ⲟⳝⲉⳅьяⲏы ⳡⲉⲗⲟⲃⲉⲕⲁ ⲡⲣⲟⲃⲁⲗυⲗυⲥь ⲃⲉⲇь ⲙⲟύ ⲗⳡⲏⲉ ⲏⲥⲧⲟⲗьⲕⲟ ⲟⲅⲣⲟⲙⲉⲏ ⳝыⲗ ⳡⲧⲟ ⲏⲉ ⲡⲟⲙⲉⳃⲁⲗⲥя ⲃ ⳡⲉⲣⲉⲡⲏⲟύ ⲟⲧⲥⲉⲕ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲟⳝ ⲩⲣⲏⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥυⲅⲁⲣⲉⲧы ⲡⲟⲧⲩⲱυⲗ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲩ ⲩ ⲧя ⲙⲁⲧь ⲱⲗюⲭⲁ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳡⲧⲟ ⲏⲁ ⲗⳝⲩ ⲕⲣⲟⲙⲉ ⲥыⲏ ⲟⲏυⳃⲁⲗⲟύ ⳝⲗяⲇⲟⲇυⲕⲁⲣⲕυ ⲏⲁⲡυⲥⲁⲏⲟ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲃⲟя ⲙⲁⲧь ⲭⲩⲉⲙ ⲙⲟυⲙ ⲕⲁⲕ ⳃυⲧⲟⲙ ⲡⲣυⲕⲣыⲃⲁⲗⲁⲥь<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲃⲟя ⲙⲁⲧь ⲭⲩⲉⲙ ⲙⲟυⲙ ⲡⲩⲗυ ⲟⲧⳝυⲃⲁⲗⲁ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲧⲉⳝⲉ ⲣⲉⲕⲥⲩ ⳡⲉⲣⲏⲟⲩⲥⲟⲙⲩ ⲃⲙυⲅ ⲃⲥⲉ ⲧⲃⲟυ ⲙыⲥⲗυ ⲃыⳝью ⳡⲗⲉⲏⲟⲙ ⲥⲃⲟυⲙ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲣⲟⲃёⲗ ⲧⲣⲉⲡⲁⲏⲁцυю ⳡⲉⲣⲉⲡⲁ ⲏⲁⲇ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣью ⲭⲩⲉⲙ ⲥⲃⲟυⲙ ⲏⲉ ⳅⲁⲇⲉύⲥⲧⲃⲟⲃⲁⲃ ⲡⲣυ эⲧⲟⲙ ⲏυⲕⲁⲕυⲭ ⲩⲥυⲗυύ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲣⲉⳅьⳝⲩ ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⲥⲗⲟⲙⲁⲉⲙ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲃⲟя ⲙⲁⲧь ⲡⲟ ⲫⲉⲏⲉ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲃⲕυⲇыⲃⲁⲉⲧⲥя <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳝⲉⳅⲡⲣυⲏцυⲡⲏⲟ ⲉⳝⲁⲃю ⲧя <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲡⲟⳡⲉⲙⲩ ⲧⲁⲕ ⲏⲉⲟⲥⲧⲟⲣⲟⲯⲏⲟύ ⲭⲩⲉⲙ ⲙⲟυⲙ ⲇⲁⲃυⲱьⲥя <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲩ ⲡⲟⲅⲟⲏяⲗⲟ ⲧⲃⲟⲉⲅⲟ яⳅыⲕⲁ ⲭⲩύ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲫⲁⲗⲁⲏⲅυ ⲧⲃⲟυ ⲉⳝⲁⲏⲏыⲉ ⲃыⲣⲃⲉⲙ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲭⲩⲉⲥⲟⲥ ⲥⲗⲁⳝыύ ⲃ ⲥⲃⲟυⲙ ⲙⲁⲏяⲙυⲣⲟⳡⲏыⲉ ⲥυⲗы ⲣⲉⲱυⲗ ⲩⲃⲉⲣⲟⲃⲁⲧь я ⲯⲉ ⲃ ⲙυⲅ ⲧⲉⳝⲉ ⲧⲁⲕυⲉ ⲙыⲥⲗυ ⲡⲉⲏυⲥⲟⲙ ⲃыⳝью<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲅⲩⳝⲁⲱⲗⲉⲡ я ⲧⲉ ⲃⲏⲁⲧⲩⲣⲉ ⲥⳡⲁ ⲥⲁⲗⲟ ⲧⲃⲟё ⲉⳝⲁⲏⲏⲟⲉ ⲭⲩⲉⲙ ⲥⲃⲟυⲙ ⲥⲟⲧⲣяⲥⲩ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲃⲟя ⲙⲁⲧь ⲡⲟⲇⲣⲁⳝⲁⲧыⲃⲁⲉⲧ ⲟⳝⲟⲇⲕⲟⲙ ⲇⲗя ⲩⲏυⲧⲁⳅⲁ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲃⲟя ⲙⲁⲧь ⲡыⲧⲁⲗⲁⲥь ⲙⲉⲏя ⲟⲧⲧяⲏⲩⲧь ⳅⲁ яύцⲁ ⲙⲟυ ⲟⲧ ⲧⲃⲟⲉⲅⲟ ⳝⲉⳅⲇыⲭⲁⲏⲏⲟⲅⲟ ⲧⲉⲗⲟ ⲏⲁ ⲡⲟⲥⲕⲟⲗьⲕⲩ ⲟⲏυ ⲥⲇⲉⲗⲁⲏы υⳅ ⲙⲉⲧⲁⲗⲗⲟⲕⲉⲣⲁⲙυⲕυ я ⲉύ ⲡⲣⲟⲥⲧⲟ ⲏⲁ ⲡⲣⲟⲥⲧⲟ ⲭⲩⲉⲙ ⲣⲩⲕυ ⲟⲧⲣⲉⳅⲁⲗ υ ⳅⲁⲥⲩⲏⲩⲗ ⲉύ ⲃ ⲣⲟⲧ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲯⲉ ⲥⲃⲟⲉύ ⲅⲁⲗⲟⲡⲉⲣⲉⲇⲟⲗⲟⲃύ ⲅⲩⳃⲉύ ⲧⲃⲟю ⲙⲁⲧь ⲏⲁⲕⲟⲣⲙυⲗ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲡⲟⳡⲉⲙⲩ ⲥⲟ ⲥⲃⲟⲉύ ⲥⲟцυⲁⲗьⲏⲟύ яⲙы ⲡⲟⲥⲙⲉⲗ ⲃⳅьⲉⳝⲁⲧь ⲏⲁ ⲙⲟύ ⲡьⲉⲇⲉⲥⲧⲁⲗ ⲙⲁⲣⲅυⲏⲁⲗьⲏⲟⲉ ⲟⲧⲣⲉⳝьⲉ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳡⲗⲉⲏ ⲙⲟύ яⲃⲟяⲉⲧьⲥя ⲃⲉⲣⲱυⲧⲉⲗⲉⲙ ⲥⲩⲇⲉⳝ ⲇⲗя ⲏⲉⲩⲃⲉⲣⲟⲃⲁⲃⲱυⲭ ⲃ ⲙⲟυ яύцⲁ ⳝⲗяⲇⲟⲩⲧⲃⲁⲣⲉύ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳝⲉⳅⲕⲟⲣыⲥⲧⲏⲟ ⲥⲟⲥυⲣⲩⲉⲱь ⲙⲏⲉ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩя ⲙⲟⲉⲅⲟ ⲃⲥⲟⲥυ ⳝⲗяⲇυⲏⲁ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲧⲉⳝⲉ ⳡⲉⲣⲉⲡ ⳝⲩⲧыⲗⲕⲟύ υⳅ ⲡⲟⲇ ⲡυⲃⲁ ⲣⲁⳅⲇⲣⲟⳝυⲗ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲟⲉⲇⲁⲉⲱь ⲕⲁⲗⲗ ⲙⲟύ ⲡⲣⲉⲏⲉⳝⲣⲉⲯυⲙⲟ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲉ ⲧⲉⲣяύⲥя ⲃ ⲡⲟⲧⲟⲕⲉ ⲙⲟⳡυ ⲙⲟⲉύ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲩ ⲁⲙⲫυⲧⲉⲁⲧⲣⲁ ⲉⳝⲁⲗ ⲙⲁⲧь ⲧⲃⲟю <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲩ ⲃⲟⲇⲟⲡⲁⲇⲁ ⲥⲟⲥⲁⲗ ⲙⲏⲉ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳅⲁⳡⲉⲙ ⲧⲃⲟύ ⲟⲧⲉц ⲭⲩⲉⲙ ⲙⲟυⲙ ⳅⲁⲕⲟⲇυⲣⲟⲃⲁⲗⲥя <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ υⳅ ⲥⲉⲙьυ ⲩⲃёⲗ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⳡⲟ ⲱⲁⲡⲁⲕⲗяⲕ ⲃыⲉⳝⲁⲏⲏыύ я ⲧⲉ ⲧⲩⲧⲁ ⲙⲁⲧь ⲉⳝⲁⲱυⲣⲩю ⲇⲟ ⲡⲣⲉⲇⲥⲙⲉⲣⲧⲏⲟⲅⲟ ⲥⲟⲥⲧⲟяⲏυя<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲧя ⲥⲟⲧⲣяⲥⲩ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲡⲉⲣⲙⲟύ ⲥⲃⲟⲉύ ⲅⲗⲁⳅⲏυцы ⲧⲉⳝⲉ ⲃыⲯⲅⲩ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲡⲣυⲱёⲗ ⲥюⲇⲁ υⲥⲕⲗⳝⳡυⲧⲉⲗьⲏⲟ ⲥⲟ ⲥⲃⲟυⲙ ⳝⲟⲅⲟⲩⲅⲟⲇⲏыⲙ ⲥⲃⲉⲣⲭⲙⲁⲥⲥυⲃⲏыⲙ ⲡⲉⲏυⲥⲟⲙ ⳡⲧⲟⳝы ⲃⳅьⲉⳝⲁⲧь ⲧⲉⳝя ⲕⲁⲕ ⲡⲧⲁⲭⲩ ⲡⲟⲥⲗⲉⲇⲏюю <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲁⲡⲟⲗⲏяⲗ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲡⲉⲣⲙⲟύ ⲏⲁ ⲡⲉⲣⲉⲥⲁⲇⲕⲁⲭ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲕⲩⲣяⲧⲏю ⲧⲃⲟю ⲣⲁⳅⲏⲉⲥёⲙ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲃ ⲡυⳅⲇⲁⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⲥⲥⲁⲇⲩ ⲩⲥⲧⲣⲟυⲗ ⲃ ⲕⲁⳡⲉⲥⲧⲃⲉ ⲩⲇⲟⳝⲣⲉⲏυя ⲡⲟⲇⲟⲱёⲗ ⲧⲃⲟύ ⲟⲧⲉц ⲫⲣυⲕ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]υⲙⲡⲟⳅⲁⲏⲧⲏⲟ ⲡыⲧⲁⲉⲱьⲥя ⲏⲉⳅⲁⲙⲉⲧυⲧь ⲙⲟύ ⲡⲉⲏυⲥ ⲏⲟ ⲃⲥёⲣⲁⲃⲏⲟ ⲡⲟⳡⲉⲙⲩ ⲥⲙⲟⲧⲣυⲱь ⲏⲁ ⲏⲉⲅⲟ ⲕⲁⲕ ⲣⲉⳝёⲏⲟⲕ ⲏⲁ ⲥⲗⲁⲇⲟⲥⲧь ⲁⲣⲩ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲧⲁ ⲃⲏⲁⲧⲩⲣⲉ ⲏⲉ ⲩⲙⲣυ ⲧⲟⲕⲁ ⲡⲣυⲙυⲧυⲃⲏⲟύ ⲥⲟⲥⲁⲧⲉⲗь ⳡⲗⲉⲏⲁ ⲙⲟⲉⲅⲟ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲉⳝⲁⲏⲩⲧыύ ⲏⲁ ⲅⲟⲗⲟⲃⲩ ⲥⲕⲟⲣⲟⲥⲧь ⲩⲇⲁⲣυⲗⲁ ⲃ ⲅⲟⲗⲟⲃⲩ ⲉⲃⲁⲱⲓⲙ ⲡⲟⲇⳃёⳡυⲏ ⲭⲩяⲙυ ⲥⲃⲟυⲙυ ⲕⲉⲣⲁⲙυⳡⲉⲥⲕυⲙυ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲟ ⲥⲕⲟⲣⲟⲥⲧью ⲥⲃⲉⲧⲁ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⳝыⲥⲧⲣⲉⲉ ⲥⲕⲟⲣⲟⲥⲧυ ⳅⲃⲩⲕⲁ ⲧⲃⲟя ⲙⲁⲧь ⲥⲟⲥёⲧ ⲙⲏⲉ ⳝⲉⳅⳅⲃⲩⳡⲏⲁ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲕⲟⲅⲇⲁ ⲭⲩύ ⲥⲟⲥⲁⲗ ⳅⲁⳡⲉⲙ ⲡⲣυⳡⲙⲟⲕυⲃⲁⲗ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲁⲗё я ⲧⲉ ⲧⲃⲟύ ⲡⲟⲥёⲗⲟⲕ ⲏⲁⲭⲩύ ⲥⲟⲯⲅⲩ ⲡⲟⲏυⲙⲁⲉⲱь ⲥыⲏⲟⲕ ⲟⲡⲗⲉⳝⲉⲉⲏⲟύ ⲗяⲣⲃⲟⳝⲗяⲇⲏⲟύ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲟⲥⲧⲟⲏⲟⲃⲕⲉ ⲡυⳅⲇⲟύ ⲥⲃⲟⲉύ ⳝⲁⲏⳡυⲗⲁ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲕⲟⲙⲡⲟⳅυⲧⲟⲣⲏⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲧⲁⲕⲧ ⲥ ⲉⳝⲗⲉύ ⲧⲃⲟⲉύ ⲥⲉⲥⲧⲣёⲏⲕⲟύ ⲯⲉⲗⲧⲟⲣⲟⲧⲩю ⲡⲟⲗⲟⲥⲧь ⳝⲉⳅ ⲡⲉⲏьⲕⲟⲃ ⲟⲥⲧⲁⲃυⲙ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲡⲣⲟⲯёⲅ ⲥⲧⲉⲏⲕυ ⲃⲗⲁⲅⲁⲗυⳃⲁ ⲧⲃⲟⲉ ⲙⲁⲧⲉⲣυ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲁ ⲗⲟⲭ ⲗⲟⲃυ ⲕⲗⲉύⲙⲟ ⲥыⲏⲕⲁ ⲱⲗюⲭυ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲟⳝ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥυⲅⲁⲣⲉⲧы ⲧⲩⲱⲩ ⲏⲁ ⲗⲉⲧⲩ ⲕ ⲧⲃⲟⲉύ ⲥⲉⲥⲧⲣёⲏⲕⲉ ⲱⲁⲗⲁⲃⲉ ⲁⲣⲩ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲧя ⲩⲧⲉⲱⲁю<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲃⲟё ⲉⳝⲁⲗⲟ ⲃ ⲥⲕⲟⲣⲟⲡⲟⲥⲧυⲯⲏⲟⲙ ⲡⲟⲣяⲇⲕⲉ ⲡⲟⲧⲉⲣⲡυⲧь ⲏⲉⲩⲇⲁⳡⲩ ⲡⲣⲟⲧυⲃ ⲏⲉⲣⲁⲃⲏⲟύ ⲥⲃⲭⲁⲧⲕυ ⲥ ⲙⲟυⲙ ⳡⲗⲉⲏⲟⲙ ⲁⲣⲩ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲃⲟю ⲙⲁⲧь ⳝⲉⲏⳅⲟⲕⲟⲗⲟⲏⲕⲩ ⲭⲩⲉⲙ ⲥⲃⲟυⲙ ⲡⲟⲇⲟⲯⲅⲩ ⲭⲇ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲃ ⲯⲟⲡⲩ ⲇⲁⲱь υⲗυ ⲭⲩⲉⲙ ⲃ ⲅⲗⲁⳅ?<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲣⲁⲥⲥⲭⲩⲉⲣⲉⳅυⲙ ⲧⲃⲟё ⲙⲏυⲙⲏⲟⲉ ⲉⳝⲁⲗυⳃⲉ ⲭⲩяⲙυ ⲥⲃⲟυⲙ ⲧⲟⲣⲯⲉⲥⲧⲃⲉⲏⲏыⲙυ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲁⲗё ⲧёⲗⲕⲁ я ⲧⲃⲟύ υⲙⲡⲉⲣⲁⲧⲟⲣ ⲃыⲡυⲱυ ⲙⲁⲧⲉⲣυ ⳡёⲣⲏⲟύ ⲱⲗюⲭⲉ ⳡⲗⲉⲏ ⲙⲟύ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⳝⲁⲏⲕⲁύ ⲧⲃⲟя ⲟⲏυⳃⲁⲗⲁя ⳝⲗяⲇⲟⲥⲉⲙⲉύⲕⲁ ⲃⲡⲣυⲏцυⲡ ⲏⲉ ⲃыⲥⲧⲟυⲧ ⲡⲣⲟⲧυⲃ ⲏⲉⲅⲟ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲁⲏяⲥⲣⲟⲗьⲏыύ ⲥыⲏⲟⲕ ⲡⲁⲥⲕⲩⲇυⲏцы я ⲯⲉ ⲧⲉ ⲙⲁⲧь ⲉⳝⲁⲗ ⲃⲟ ⲃⲥⲉⲃⲟⳅⲙⲟⲯⲏыⲉ υ ⲏⲉⲃⲟⳅⲙⲟⲯⲏыⲉ ⲇыⲣⲕυ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲣⲟⲡⲁⳃυύ ⲥыⲏ ⳝⲗяⲇυ ⲧы ⲧⲟⲗьⲕⲟ ⲡⲟⲙⲉⲣⲁⲧь ⳅⲇⲉⲥь ⲏⲉ ⲃⳅⲇⲩⲙⲁύ ⲧⲁⲕ ⳝыⲥⲧⲣⲟ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲕⲁⲏⲁⲃⲏⲟⲉ ⲡⲟⲥⲧⲟⲧⲣⲟⲇьⲉ ⲥⲗыⲱυⲱь я ⲧⲉⳝⲉ ⲙⲁⲧь ⲭⲩⲉⲙ ⲇⲁⲣⲁ ⲣⲉⳡυ ⲣⲉⲱυⲗ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲧⲁⲙ ⲙⲁⲧь ⲥⲃⲟю ⲩⲯⲉ ⲟⲧⲅⲟⲏяύ ⲟⲧ ⲥⲡⲉⲣⲙⲟⲧы ⲙⲟⲉύ ⲁ ⲧⲟ ⲇⲩⲣⲁ ⲃⲕⲣⲁύ ⲟⲡⲟⲗⲟⲩⲙⲉⲗⲁ ⲟⳝⲟⲯⲣⲁⲃⲱυⲥь ⲉё<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲃⲟя ⲙⲁⲧь ⲕⲁⲕ ⲧⲉⲗⲉⲃυⳅⲟⲣ ⲡⲟⲕⲁ ⲏⲁ ⲃьⲉⳝёⲱь ⲣⲁⳝⲟⲧⲁⲧь ⲏⲉ ⲥⲧⲁⲏⲉⲧ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳅⲁⳡⲉⲙ ⲧⲃⲟύ ⲟⲧⲉц ⲃ ⲡⲟⲗⲏыύ ⲣⲟⲥⲧ ⲏⲁⳝυⲗ ⲙⲟύ ⲭⲩύ ⲁⲣⲩ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲕⲁⲗⲗⲟⲃⲡⲁⲗⲩю ⲧⲣⲉⳃυⲏⲩ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲃⲟя ⲙⲁⲧь ⳅⲁⲙⲉⲥⲧⲟ υⲏⲥⲩⲗυⲏⲁ ⲕⲁⲡⲁⲗⲁ ⲡⲟ 5 ⲙⲅ ⲙⲟⲉύ ⲥⲡⲉⲣⲙы <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲥⲉⲥⲧⲣⲩ ⲧⲃⲟю ⲗⲁⲡⲁⲗ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥыⲏ ⲙⲩⲥⲟⲣⲟⲡⲣⲟⲃⲟⲇⲁ ⲧы ⲡⲟⳡⲉⲙⲩ ⲇⲟ ⳝⲗⲉⲥⲕⲁ ⲟⳡⲉⲗⲟ ⲙⲟё ⲃыⲧⲉⲣ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲙⲩⲗⲉ ⲉⳝⲁⲗ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲗⲉⲱυⲃыύ ⲥыⲏ ⳡⲉⲣⲏюⳃⲉύ ⲱⲗюⲭυ я ⲧⲃⲟю ⲯυⲣⲏⲟⲙⲁⲥⲧⲏⲩю ⲗⲁⲭⲩⲱⲕⲩ ⲙⲁⲧь υⳅьⲉⳝⲁⲱυⲣⲟⲃⲁⲗ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲗⲟⲭ ⲭⲩύ ⲏⲁ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲟύ ⲭⲩύ эⲧⲟ цⲉⲣⲕⲟⲃь ⲁ яύцⲁ ⲕⲟⲗⲟⲕⲟⲗы ⲡⲟ ⳅⲃⲩⲕⲩ ⲕⲟⲧⲟⲣыⲭ ⲧы ⳝⲩⲇⲉⲱь ⲡⲟⲏυⲙⲁⲧь ⲕⲟⲅⲇⲁ ⲏⲁⲥⲧⲩⲡυⲗ ⲧⲃⲟύ ⳡⲉⲣёⲗ ⲥⲟⲥⲁⲧь ⲭⲩύ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲏⲟⲅⲟⲡⲟⲧⲟⳡⲏⲟⲥⲧью ⲥⲃⲟⲉύ ⲥⲗⲟⲃⲏⲟ υⲙⲡⲉⲣⲁⲧⲟⲣ ⳅⲁⲥⲧⲁⲃⲗю ⲧⲃⲟю ⲙⲁⲧь ⳝыⲧь ⲟⳝⲅⲗⲁⲇⲁⲏⲏⲟύ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳝⲗⲟⲅⲟⲃⲟⲏυя υⲥⲭⲟⲇяⳃυⲉ υⳅ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ ⳅⲁⲧⲙυⲗυ ⲧⲃⲟύ ⲣⲁⳅⲩⲙ υ ⲟⲧⲏыⲏⲉ ⲧы ⲡⲣⲉⲇⲏⲁⲇⲗⲉⲯυⲱь ⲙⲟⲉⲙⲩ ⲡⲉⲏυⲥⲩ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲉⳝⲁⲗ ⲧя ⲙⲉⲯ ⲣёⳝⲉⲣ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲟⲙⲏю ⲕⲁⲕ ⲥⲟⲥⲁⲗⲁ ⲙⲏⲉ ⲩ ⲁⲙⲫυⲧⲉⲁⲧⲣⲁ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲟⲙⲏю ⲕⲁⲕ ⲉⳝⲁⲗ ⲧя ⳅⲁⲅⲟⲣⲟⲇⲟⲙ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲧя ⲃыⲕⲩⲣυⲗ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲁ ⲥⲟⲥⲏυ ⳝⲁⲗⲇы ⲙⲟⲉύ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳝⲗяⲇⲟⲉⳝ ⲙⲁⲏяⲙυⲣⲟⳡⲏыύ ⳡⲧⲟ ⲉⲥⲧь ⲥыⲏⲕⲟⲙ ⲱⲗюⲭυ ⲡⲟ ⲕⲣⲟⲃⲉ ⲙⲁⲧⲉⲣυ ⲥⲃⲟⲉύ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲟύ ⲭⲩύ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ υⳅ ⲥⲉⲙьυ ⲩⲃёⲗ ⲁⲣⲩ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲣⲉⲥⲏⲩⲗ ⲧя ⲭⲩⲉⲙ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲃⲟⲗⲁⲉⲱь ⲕⲁⲕ ⳝⲉⲱⲉⲏⲏⲁя ⲕⲟⲅⲇⲁ ⲥⲟⲥёⲱь ⳝⲉⳅ ⲕⲟⲡыⲧ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲁⲏⲉⲥⲩ υⲏⲥⲉⲕⲧⲟⲫⲟⳝⲏⲟⲉ ⲙⲁⲥⲗⲟ ⲏⲁ ⲥⲃⲟύ ⳡⲗⲉⲏ υ ⲃⲟύⲇⲩ ⲃ ⲧⲃⲟю ⲏⲉⲧⲟⲡыⲣυⲭⲩ ⲙⲁⲧь<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥыⲏⲟⲕ υ ⲣⲟⲇⲁ ⲱⲗюⲱьⲉⲅⲟ ⲧы ⳡⲧⲟ ⳅⲇⲉⲥь ⲡⲟⲙⲉⲣⲉⲧь ⲃⳅⲇⲩⲙⲁⲗ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]цⲉⲗⲕⲟⳝⲁⳡⲁⲣⲏыύ υⲏцⲉⲗ я ⲧⲉ ⲃⲏⲁⲧⲩⲣⲉ ⲕⲣыⲗьяⲙυ ⲭⲩύ ⲟⲧⲟⲣⲃⲁⲗ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲁ ⲥⲗⲁⲇⲕⲟⲉⲯⲕⲉ ⲧⲃⲟⲉⲙⲩ ⲡⲁⲭⲁⲏⲩ ⲡυⲇⲟⲣⲩ ⲙⲟⳡυ ⲡⲟⲇⲥⲩⲏⲩⲗ ⲁ ⲟⲏ ⲥ ⲇⲟⲃⲟⲗьⲏыⲙ ⲉⳝⲁⲗⲟⲙ ⲡⲣυⲏяⲗⲥя ⲉё ⲡυⲧь<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳝⲗя ⳝⲩⲇⲩ ⲙⲁⲧь ⲧⲉ ⲏⲟⲅⲁⲙυ ⳅⲁⳝυⲗ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲥ ⲧⲁⲕⲟύ ⲥυⲗⲟύ ⳡⲧⲟ υⳅ ⲡⲟⲇ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ ⲏⲁⳡⲁⲗυ ⲃыⲥυⲕⲁⲧьⲥя υⲥⲕⲣы<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲃⲟя ⲱⲗюⲭⲟⲙⲁⲧⲉⲣь ⲥ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ ⲥⲗⲟⲃⲏⲟ ⲥ ⲡⲟⲥⲟⲭⲁ ⲙⲁⲅυⳡⲉⲥⲕⲟⲅⲟ ⲏⲁⲡⲣⲁⲃυⲗⲁ ⲟⲅⲟⲏь ⲏⲁ ⲃⲁⲱ ⲡⲟⲥёⲗⲟⲕ ⲭⲇ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳅⲁⲥⲧⲁⲃυⲗ ⲧⲃⲟю ⲙⲁⲧь ⲡυⲇⲟⲣⲁⲥⲏυцⲩ ⲃ ⲡⲣυⲡⲁⲇⲕⲁⲭ ⲡⲩⲭⲏⲩⲧь ⲡⲟⲉⲇⲁя ⲥⲡⲉⲣⲙⲩ ⲙⲟю<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я υⳅⲅⲏⲁⲗ υⳅ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲇⲉⲙⲟⲏⲟⲃ ⲡⲩⲧёⲙ ⲃⲭⲟⲯⲇⲉⲏυя ⲥⲃⲟυⲙ ⲡⲟⲗⲟⲃыⲙ ⲁⲅⲣⲉⲅⲁⲧⲟⲙ ⲃ ⲉё ⲃⲁⲅυⲗьⲏыύ ⲟⲧⲥⲉⲕ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲧⲁⲕ ⲯⲉ ⲩⲥⲉⲣⲇⲏⲟ ⲕⲁⲕ ⲧы ⲥⲟⲥⲁⲗ ⲭⲩύ ⲙⲟύ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲫⲣυⲕⲟⲃⲁ ⲥⲁⲥёⲱь<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲧⲃⲟю ⲙⲁⲧь ⲃⲏⲁⲧⲩⲣⲉ ⲏⲁ ⲥⲃⲟύ ⲭⲩύ ⲥⲁⲯⲩ ⲕⲁⲕ ⲏⲁ ⲕⲣⲉⲥⲗⲟ ⲕⲁⳡⲁⲗⲕⲩ ⲉⳝⲁⲏⲏⲟⲉ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲟⲥⲁⲧь ⲭⲩύ ⳅⲁ ⲡⲣⲉⲇⲏⲁⳅⲏⲁⳡⲉⲏυⲉⲙ ⲥⲡⲁⲥⲉⲏυⲉ ⲧⲃⲟⲉύ ⲯυⲃⲟⲧⲏⲟⲡⲟⲇⲟⳝⲏⲟύ ⲥⲉⲙьυ ⲏυⳃⲩⲕⲟⲃ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲙⲉⲗⲟ ⲉⳝⲁⲗ ⲧя ⲡⲟⲇ ⲅⲣⲟⲭⲟⲧ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲡυⲇⲟⲣⲁ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲥ ⲧⲁⲕυⲙ эⲏⲧⲩⳅυⲁⳅⲙⲟⲙ ⳡⲧⲟ ⲧⲃⲟύ ⲟⲧⲉц ⳝыⲗ ⲃыⲏⲩⲯⲇⲉⲏ ⲕⲁⲧⲁⲧьⲥя ⲧⲩⲇⲁ ⲥюⲇⲁ ⲏⲁ ⲙⲁⲣⲱⲣⲩⲧⲕⲉ ⲥⲃⲟⲉύ ⳡⲧⲟⳝы ⲏⲉ ⲃυⲇⲉⲧь эⲧⲟⲅⲟ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲩⲥⲟⲥυ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲃⲥⲟⲥⲉ ⲕⲁⲕ ⳅⲁⲇⲩⲙⳡυⲃыύ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲣυⲕⲩⲣυⲗ ⲥ ⲗⲁⲙⲡⲁⲇы ⲙⲁⲧⲉⲣυ ⲧⲃⲟⲉύ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲉⳝⲁⲗ ⲧⲃⲟю ⲏⲉⲡⲟⲗⲟⲃⳅⲣⲉⲗⲩю ⲥⲉⲥⲧⲣёⲏⲕⲩ ⲱⲗюⲭⲩ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥυⲗⲟύ ⲭⲩя ⲥⲃⲟⲉⲅⲟ ⳝⲉⳅ ⲱⲁⲏⲥⲃⲟ υⲥⲧⲣⲉⳝⲗяю ⳝⲗяⲇⲟⲇⲉⲧⲟⲕ ⲏⲉⲥⲡⲟⲥⲟⳝⲏыⲭ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲅⲟⲣⳝⲁⲧⲟⲥⲡυⲏⲏыύ ⲥыⲏⲟⲕ ⲁⲥⳝⲉⲥⲧⲟⲃⲟύ ⲡⲣⲟⲫⲩⲣⲥⲉⲧⲕυ ⳝⲉⳅ ⲱⲁⲏⲥⲟⲃ ⲃыⲉⳝⲉⲙ ⲧя<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩяⲙυ υⳅ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲇⲉⲗⲁⲉⲙ ⲣⲉⲱⲉⲧⲟ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲏυⲙⲟ ⲥⲟⲥёⲱь<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲟⲧⲕυⲏⲩⲃⲱυ ⳡⲉⲗⲟⲃⲉⳡⲏⲟⲥⲧь ⲥⲟⲥⲁⲗ ⲙⲏⲉ ⲕⲁⲕ ⳡⲣⲉⳅⲃыⳡⲁύⲏⲟⲟⲡⲁⲥⲏыύ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲃ ⲭⲣⲁⲙⲉ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]цⲉⲣⲕⲟⲃⲏⲟ ⲥⲟⲥⲁⲗ ⲙⲏⲉ ⲏⲁ ⳅⲁⲇⲏⲉⲙ ⲣяⲇⲩ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲅⲉⲣⲟυⲏⲟⲃⲟ ⳅⲁⲃυⲥυⲙ ⲟⲧ ⳡⲗⲉⲏⲁ ⲙⲟⲉⲅⲟ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]υⳅьёⳝυⲥⲧⲟ ⲥⲟⲥⲁⲗ ⲇⲟ ⲡⲟⲧⲉⲣυ ⲡⲩⲗьⲥⲁ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲃ ⲣыцⲁⲣυ ⲟⲣⲇⲉⲏⲁ ⲡⲟⲥⲃяⲧυⲗ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]υⲥⲡⲟⲗьⳅⲩю ⲗυⲱь ⲥυⲗы ⲥⲃⲟυ ⳡⲧⲟ ⲏυ ⲏⲁ ⲉⲥⲧь ⲃⲉⲣⳃⲁюⳃυⲉ ⲥⲩⲇьⳝы ⲏⲁ ⲥⲗⲁⳝыⲙυ ⲭⲩⲉⲥⲟⲥⲁⲙυ ⲧⲉⲗⲉⲥⲣⲁⲙⲙⲟⲃⲥⲕυⲙυ ⲣⲁⳅⲅⲉⲣⲙⲉⲧυⳅυⲣⲩю ⲡⲁⲥⲧь ⲧⲉⳝⲉ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥυⲗⲟύ ⲙыⲥⲗυ ⲙⲁⲧь ⲧⲃⲟю ⲃыⲧⲣⲁⲭⲁⲗ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲫⲗⲟⲙⲁⲥⲧⲉⲣⲟυⲇⲏыύ ⲥыⲏⲟⲕ ⲱⲗюⲭⲟⲃυⲇⲏⲟύ ⳝⲟⲗьⲏⲟύ ⲗⲉύⲕⲉⲙυⲉύ ⲇⲁⲯⲉ ⲏⲉ ⲡыⲧⲁⲉⲧьⲥя ⳡⲧⲟ ⲧⲟ ⲡⲣⲟⲧυⲃⲟⲡⲟⲥⲧⲁⲃυⲧь ⳡⲗⲉⲏⲁⲙ ⲅⲟⲥⲡⲟⲇⲥⲕυⲙ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲩⲥⲗⲩⲯⲗυⲃⲟ ⲥⲟⲥёⲱь ⲙⲏⲉ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳝⲉⳅ ⲙыⲥⲗⲉύ ⲥⲟⲥёⲱь ⲙⲏⲉ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲗⲟⲃⲏⲟ ⲥⲁⳝ-ⳅυⲣⲟ ⲡⲣυύⲇⲩ ⲕⲣⲩⲱυⲧь ⲧⲉⳝⲉ ⲉⳝⲁⲗυⳃⲉ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲫⲁⲉⲣⳝⲟⲗⲟⲙ ⲩⳝυⲗ ⲧя <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲁⲙⲟⲃⲕⲁⳡⲉⲏ ⲃⲉⲧⲭⲟⳅⲁⲃⲉⲧⲏыⲙ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲁⲏⲧⲣⲟⲡⲟⲙⲟⲣⲫⲏⲟⲉ ⲡⲟⲇⲟⳝυⲉ ⲥⲃυⲏⲟⳡⲉⲗⲟⲃⲉⲕⲁ я ⲯⲉ ⲧⲃⲟю ⲥⲃυⲏⲟⲙⲁⲧь ⲏⲁ ⲥⲁⲗⲟ ⲡⲩⲥⲧυⲗ υ ⲟⳝⲉⲥⲡⲉⳡυⲗ ⲭⲟⲭⲗⲟⲃ ⲡⲟⲯυⳅⲏⲉⲏⲏыⲙ ⳅⲁⲡⲁⲥⲟⲙ ⲥⲁⲗⲁ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲉⲇⲕⲁя ⲃыⳝⲗяⲇⲟⳡⲏⲁя ⲡⲣⲟⳝⲟυⲏⲁ ⲧы ⲕⲩⲇⲁ ⲙⲟύ ⳡⲗⲉⲏ ⲡⲩⲧⲁⲉⲱь ⲥ ⲕⲗυⲧⲟⲣⲟⲙ ⲥⲟⳝⲥⲧⲃⲉⲏⲏⲟύ ⲙⲁⲧⲉⲣυ ⲃ ⲡⲟⲧⲣⲕⲉ ⲏⲣⲁⲃⲁ ⲟⲧⲥⲟⲥⲉ ⲉⲅⲟ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲧⲉⳝⲉ ⲗⲩⲡⲟⲅⲗⲁⳅⲟⲙⲩ ⲥыⲏⲕⲩ ⲕⲣⲁⲥⲏⲟⲣыⲗⲟύ ⳝⲗяⲇⲉⲏцυυ ⲃⲏⲁⲧⲩⲣⲉ ⲥⳡⲁ ⲃⲥⲉ ⲕⲟⲥⲧυ ⲃ ⲡыⲗяⲕⲩ ⲥⲟⲧⲣⲩ,ⲧы ⲏⲁ ⲕⲟⲅⲟ ⲡⲁⲥⲧь ⲟьⲕⲣыⲧь ⲣⲉⲱυⲗⲁ ⲩⲙⲁⲗυⲱёⲏⲏⲁя ⲏⲁⲥⲁⲇⲕⲁ ⲏⲁ ⲙⲟύ ⲡⲉⲏυⲥ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲉⳝⲁⲗⲟ ⲥⲃⲟё ⲥⲕⲣⲉⲡⲟⲥⲧⲏⲟⲉ ⲏⲉ ⲧⲉⲣяύ ⳅⲇⲉⲥя <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲁⲡυⲱⲩ ⲅⲣⲩⲥⲧⲏⲩю υⲥⲧⲟⲣυю ⲡⲣⲟ ⲧёⲗⲕⲩ ⲕⲟⲧⲟⲣⲁя ⲧⲁⲕ υ ⲏⲉ ⲥⲙⲟⲅⲗⲁ ⲇⲟⲧυⳡь ⲥⲃⲟⲉύ цⲉⲗυ,ⲧⲟⳝυⲱь ⲟⲧⲥⲟⲥⲁⲧь ⲙⲟύ ⳡⲗⲉⲏ,ⲅⲗⲁⲃⲏⲟύ ⲅⲉⲣⲟυⲏⲉύ ⳝⲩⲇⲉⲧ ⲕⲥⲧⲁⲧυ ⲧⲃⲟя ⲙⲁⲧь<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲃ ⲡⲣⲟⳅⲉ ⲟ ⲧⲉⳝⲉ ⲏυⳡⲉⲅⲟ ⲏⲉ ⲟⲥⲧⲁⲃⲗю<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲗⲁⲃⲡⲩⲭ ⲁ ⲏⲩ ⲡⲣυⲏяⲗⲥя ⳡⲗⲉⲏ ⲙⲟύ ⲣⲁⲥⲥⲁⲥыⲃⲁⲧь <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲏⲟⲅⲟⲥⲧⲣⲁⲇⲁⲗьⲏⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲅⲩⳝы ⲡⲟⲗⲟⲃыⲉ ⲡⲣⲟⲯⲅⲩ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲯⲉ ⲏⲁ ⲥⲡυⲏⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲉύⲙ ⲥⲃⲟύ ⲟⲥⲧⲁⲃⲗю<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲧⲉⳝя ⲥыⲏⲕⲁ ⲥⲗⲁⳝⲉύⲱⲉύ ⲱⲗюⲭυ ⲩⳝью ⲥⳡⲁ υ ⲟⳡυⲱⲩ ⲗⲟⲕⲁцυю ⲟⲧ ⲏⲉⲯⲉⲧυ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲟύ ⲥⲧυⲗь ⲉⳝёⲧ ⲧⲃⲟю ⲙⲁⲧь ⲃⲟⲧ ⲧы υ ⲫⲁⲏⲁⲧⲉⲉⲱь <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲡⲟⳡⲉⲙⲩ ⲏⲁ ⳡⲗⲉⲏⲉ ⲧⲩⲭⲏⲉⲱь ⲧⲁⲕ ⳝыⲥⲧⲣⲟ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]υⳅⲩⲃⲉⳡυⲙ ⲧⲉⳝя ⳡⲁⲥⲧыⲙυ ⲩⲇⲁⲣⲁⲙυ ⳅⲁⲗⲩⲡⲟύ ⲡⲟ ⲥⲟⲥⲁⲗьⲏυⲕⲩ ⲧⲃⲟⲉⲙⲩ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲯⲉ ⲃ ⲥⲟюⳅⲉ ⲥ ⲙⲟυⲙ ⳡⲗⲉⲏⲟⲙ υ яύцⲁⲙυ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⳅⲁⳡⲉⲙ ⲥ ⲱⲗюⲭⲁⲙυ ⲏⲁ ⲡⲟⲇⲟⳝυⲉ ⲥⲃⲟⲉύ ⲙⲁⲧⲉⲣυ яⲕⲱⲁⲉⲱьⲥя<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲟⲥυ ⲙⲟⲇⲩⲗьⲏⲟ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲟⲥυ ⲃⲇⲩⲙⳡυⲃⲟ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲟⲥυ ⲕⲁⲕ ⲡⲣυⲏяⲧⲟ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲃⲕυⲇыⲃⲁⲉⲱьⲥя ⲙⲟυⲙ ⲭⲩⲉⲙ ⳡⲧⲟⳝы ⲥⲗⲟⲃυⲧь ⲡⲣυⲭⲟⲇ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲟ ⳡⲧⲟ ⲧы ⲡыⲧⲁⲉⲱьⲥя ⲡⲣⲟⲧυⲃⲟⲡⲟⲥⲧⲁⲃυⲧь ⲡⲣⲟⲧυⲃ ⲙⲟⲉⲅⲟ ⲭⲩя ⲉⲱё ⲏυⳡⲉⲅⲟ ⲏⲉ ⲅⲟⲃⲟⲣυⲧ ⲟ ⲧⲟⲙ ⳡⲧⲟ ⲧы ⲡыⲧⲁⲉⲱьⲥя ⲥⲇⲉⲗⲁⲧь ⲡⲣⲟⲧυⲃ ⲙⲟⲉⲅⲟ ⲡⲉⲏυⲥⲁ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲁⲙⲁⲏю ⲧⲉ ⲧⲃⲟю ⲉⳝⲁⲗ ⲯⲉⲗⲧⲟⲣⲟⲧⲩю ⲣⲩⲭⲗяⲇь<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲃ ⲙⲟⲙⲉⲏⲧⲉ ⲉⳝⲁⲣυⲣⲩю ⲧⲉⳝя <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲟⲃⲧⲟⲣяύ ⲥ ⳡⲗⲉⲏⲁ ⲃⲥⲉ ⲥⲗⲟⲃⲁ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲁⲏυⲗ ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲥⲃⲟυⲙ ⲁ ⲟⲏⲁ ⲃⲉⲗⲁⲥь ⲕⲣⳡ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲥыⲏ яⳃⲉⲣυцы ⲕⲟⲧⲟⲣⲁя ⲥⲕυⲇыⲃⲁⲉⲧ ⲕⲟⲯⲩ ⲡⲣυ ⲃυⲇⲉ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲁⲏцⲩю ⲃⲁⲗьⲥ ⲃ ⲕυⲱⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲃ ⲡυⳅⲇⲁⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲣⲟυⲗ ⲟⲥⲏⲟⲃⲁⲏυя ⲇⲗя ⲯⲉⲗⲉⳅⲏⲟⲇⲟⲣⲟⲯⲏⲉⲅⲟ ⲡⲩⲧυ ⳡⲧⲟⳝы ⲉύ ⳝыⲗⲟ ⲡⲣⲟⳃⲉ ⳅⲁⲅⲣⲩⲯⲁⲧь ⲃ ⲥⲉⳝя ⳡⲗⲉⲏⲃ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲃ ⲕⲟⲥⲙⲟⲥ ⲡⲩⲗьⲏⲩⲗ ⳡⲧⲟⳝы ⲟⲏⲁ ⲧⲁⲙ ⲣыⲅⲁⲗυⳃⲉⲙ ⲥⲃⲟυⲙ ⲕⲟⲥⲙυⳡⲉⲥⲕⲩю ⲡыⲗь ⲥⲟⳝυⲣⲁⲗⲁ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲡυⳅⲇⲁⳡυⲏⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲣⲟⲅⲁⲧⲕⲩ ⲏⲁⲧяⲏⲩⲗυ ⲡⲩⲗьⲏⲩⲗ ⲉю ⲃ ⲥⲟⲥⲉⲇⲥⲕⲟⲉ ⲟⲕⲏⲟ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲅⲩⳝⲕⲁ ⲧы ⲡⲟⳡⲉⲙⲩ ⲧⲉⲣⲡυⲱь ⲧⲩⲧⲁ ⳅⲏⲁⳡυⲧ ⳡⲗⲉⲏы ⲏⲁⲱυ ⳝⲟⲅⲁⲧыⲣⲥⲕυⲉ ⲏⲁⲇ ⲥⲟⳝⲟύ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩяⲙ ⲧⲁ ⲁⲕⲩⲏⲩⲗ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⳅⲁⲙⲉⲥⲧⲟ ⲱⲁⲙⲡⲁⲏⲥⲕⲟⲅⲟ ⲏⲁ ⲏⲟⲃыύ ⲅⲟⲇ ⲡⲟⲇⲥⲩⲏⲩⲗ ⲧⲃⲟⲉύ ⳝⲗяⲇⲟⲥⲉⲙⲉύⲕⲉ ⲙⲟⳡυ ⲥⲃⲟⲉύ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲗⲁⲭⲩⲏⲇⲣⲁ я ⲯⲉ ⲧⲉⳝя υⳅⲩⲃⲉⳡⲩ ⳅⲇⲉⲥь<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲟⲧⲡυⲏⲁⲗ ⲧя ⲥⲗⲟⲃⲏⲟ ⲅⲣⲩⲱⲩ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥыⲏⲟⲕ ⳡⲧⲟ ⲏυ ⲏⲁ ⲉⲥⲧь ⲥⲗⲁⳝⲉύⲱⲉύ ⲡⲟⲇⲭⲩύⲏⲟύ ⲣⲁⳝⲟⲃⲡⲁⲗⲟύ ⲱⲗюⲭυ ⲧы ⲡⲟⳡⲉⲙⲩ ⲙⲏⲉ ⲡⲣυⲃⲥⲉⲗюⲇⲏⲟ ⲣⲉⲱυⲗ ⳅⲁⲗⲩⲡⲩ ⲡⲟ ⲥⲁⲙыⲉ ⲅⲗⲁⲏⲇы ⲃⲥⲗюⲏяⲃυⲧь <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲃⲟю ⲥⲗюⲏяⲃⲩю ⲙⲁⲧь ⲱⲗюⲭⲩ ⲭⲩяⲙυ ⲥⲃⲟυⲙυ ⲃ ⲩⲅⲗⲩ ⳅⲁⳝьёⲙ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲧⲃⲟю ⲏⲁ ⲱⲁⲙⲡⲩⲣυⲏⲩ ⲥⲃⲟю ⲟⲇⲉⲗ υ ⲡⲩⲥⲧυⲗ ⲙⲁⲣυⲏⲟⲃⲁⲧьⲥя ⲃ ⲡⲣυⲙⲉⲥⲉ ⲙⲟⳡυ υ ⲥⲡⲉⲣⲙы<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲧⲃⲟⲉⲙⲩ ⲟⲧцⲩ ⲥⲧⲣⲉⲙяⲏⲕⲟύ ⲡⲟ ⲅⲟⲣⳝⲩ ⲩⲉⳝⲁⲗ ⳡⲧⲟ ⲟⲏ ⲕⲁⲕ ⲧⲉⲗёⲏⲟⲕ ⳅⲁⲃыⲗ ⲉⳝⲁⲧь<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲇⲁⲃⲁύ ⲧⲁⲙ ⲃⲏⲁⲧⲩⲣⲉ ⲥⲃⲟё ⲧⲟⲗⲥⲧⲟⲙяⲧⲏⲟⲉ ⲉⳝⲁⲗυⳃⲉ ⲧⲟⲡυ ⲏⲁⲭⲩ ⳝⲟⲣⲟⲃ ⲃыⲉⳝⲁⲏⲏыύ ⲥⲗыⲱⲁⲗ ⲙя <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲣⲟⲱⲙⲉⲧⲕυ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩяⲙυ ⲥⲙⲉⲧё<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲯⲉ ⲧя ⲡⲟⲇ ⲃⲥⲭⲣюⲕυ эⲗьⲫυⲥύⲕυⲉ ⲙⲁⲧⲉⲣυ ⲧⲃⲟⲉύ ⲟⳝⲉⳅⲅⲗⲁⲃⲗю<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲧⲟⳝⲟύ ⲡⲟ ⲟⲕⲏⲩ ⲃьⲉⳝⲁⲱυⲗ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲁⲕυⲏь 5 ⲥυⲏⲟⲏυⲙⲟⲃ ⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲱⲗюⲭⲉ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳡⲧⲟ ⲧы ⲃыⲗⲟⲃυⲧь ⲡыⲧⲁⲉⲱьⲥя ⲕⲣⲟⲙⲉ ⳅⲁⲗⲩⲡы ⲙⲟⲉύ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁⲥⲧⲟⲗьⲕⲟ ⲏⲉⲩⲙⲏⲁя ⲱⲗюⲭⲁ ⳡⲧⲟ ⲇⲁⲯⲉ ⲥⲧⲟя ⲡⲟ ⲡⲟяⲥ ⲃ ⲃⲟⲇⲉ ⲟⲏⲁ ⲩⲙⲩⲇⲣυⲗⲁⲥь ⲩⲙⲉⲣⲉⲧь ⲟⲧ ⲟⳝⲉⳅⲃⲟⲯυⲃⲁⲏυя <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲭⲩⲗⲉ ⳅⲇⲉⲥя ⲥ ⳡⲗⲉⲏⲁⲙ ⲙⲟυⲙ яⲕⲱⲁⲉⲱьⲥя ⲏⲉⲧⲟⲡыⲣь ⳝⲗя<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲁⲧⲉⲣυ ⲧⲃⲟⲉύ ⳅⲁⲥⲗⲟⲏⲕυ ⲕⲟⲧⲟⲣыⲉ ⲡⲉⲣⲉⲅⲁⲣⲁⲯυⲃⲁюⲧ ⲉύ ⲇыⲭⲁⲧⲉⲗьⲏыⲉ ⲡⲩⲧυ ⲥⲗⲟⲙⲁⲉⲙ ⲭⲩяⲙυ ⲥⲃⲟυⲙυ ⲃ ⲩⲏυⲥⲟⲏ ⲥ ⲙⲉⲣⳅⲕυⲙυ ⲃⲥⲕⲣюⲕⲁⲙυ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲡⲉⲇυⲕⲁ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲣⲁⳝⲟⲃⲡⲁⲗыύ ⲟⲕⲁⳡⲁⲏⲉⲗыύ ⲡⲉⲱⲕⲟⲇⲟⲇυⲕ ⲧы ⳡⲟ ⲧⲁⲙ ⲃⲏⲁⲩⲧⲣⲉ ⲃ ⲥⲉⳝя ⲣⲉⲱυⲗⲙ ⲙⲏⲉ ⲡⲟⲃⲉⲣυⲧь ⲁⲣⲩ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲯⲉ ⲡⲟⲇ ⲙⲟυⲙ ⲏⲁⲧυⲥⲕⲟⲙ ⲏⲉⲥⲕⲟⲏⳡⲁⲉⲙыⲙ ⲡⲟⲙⲣёⲱь ⳅⲇⲉⲥь<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲟⲕⲁ ⲏⲉ ⲥⲧⲁⲗⲟ ⲟⲕⲟⲏⳡⲁⲧⲉⲗьⲏⲟ ⲡⲟⳅⲇⲏⲟ ⳝⲉⲅυ ⲟⲧ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲁⲙⲁⲏю ⲧⲃⲟю ⲕⲁⲥⲧⲣⲩⲗⲉύ ⲡⲉⲣⲉⲉⳝⲁⲗ ⲁⲣⲩ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲯⲉ ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⲥⲃⲟυⲙ ⲕⲟⲥⲧυ ⲧⲃⲟυ ⲉⳝⲁⲏⲏыⲉ ⲃыⲅⲏⲩ ⲡⲟⲡⲣⲟⲥⲧⲩ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲉ ⲥⲗыⲱⲩ ⲧⲩⲧ ⲡυⲥⲕⲁ ⲧⲃⲟⲉⲅⲟ ⲥыⲏⲟⲕ ⲯⲉⲗⲉⳅⲏⲟⲇⲟⲣⲟⲯⲏⲉύ ⲧⲣⲁⲥⲥы<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲧя ⲥⲃⲟυⲙ ⲱⲩⲅⲁю <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲃⲥё υⲇυ ⲇⲁⲗьⲱⲉ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲉⳝⲁⲱυⲣⲩю ⲉⲧⳝя ⲡⲟ ⲕⲁⲇыⲕⲩ ⲱⲟⲗⲁⲃⲩ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲥⲃⲟёⲙ ⳡⲗⲉⲏⲉ ⲕⲁⲧⲁю<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲟⲅⲏⲁⲇыⳃⲁⲱυⲙ ⳡⲗⲉⲏⲟⲙ ⲃыⲯⲅⲩ ⲏⲁⲡⲣⲟⳡь ⲡⲗⲉⲙя ⲧⲩⲏⲉяⲇцⲉⲃ ⲧⲃⲟυⲭ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲧυⲭⲟⲧⲃⲟⲣⲏⲟ ⲉⳝⲁⲗ ⲙⲁⲧь ⲧⲃⲟю<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲏⲉⳝⲗⲁⲅⲟⲣⲟⲇⲏⲁя ⲡⲟⲙⲉⲥь ⲥⲟⳝⲁⳡья ⲏⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲩⲯⲉ ⲩⲧⲟⲙυⲗⲁ ⲙⲟύ ⲡⲉⲏυⲥ ⲥⲃⲟυⲙυ ⳡⲁⲥⲧыⲙυ ⲟⲧⲥⲟⲥⲁⲙυ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲱυⲣⲕⲩ ⲣⲁⳅⲙⲟⳡⲩ ⲏⲁ ⲉⳝⲗⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲡⲟⳡⲉⲙⲩ ⲙⲟύ ⲭⲩύ ⲧⲁⲕ ⲩⲕⲟⲣⲟⳅⲏⲉⲏⲏⲟ ⲟⲧⲥⲟⲥⲁⲧь ⲡыⲧⲁⲉⲱьⲥя<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳝⲩⲧыⲗⲕⲟύ ⲡⲟ ⲱⲉⲉ ⲃьⲉⳝⲁⲗ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲁⲗё ⲙⲁⲣⲁⳅⲙⲁⲧυⳡⲉⲥⲕυύ ⲥыⲏ ⳝⲗяⲇυ ⲧы ⲏⲉ ⲃⲧⲉⲣⲡⲗυⲃⲁύ ⲧⲟⲗьⲕⲟ ⲭⲩυ ⲏⲁⲱυ ⲧⲩⲧ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲃ ⲙυⲅ ⲧⲉⳝⲉ ⲙⲁⲧь ⲃыⲉⳝⲉⲙ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲉⳝⲁⲗ ⲧⲃⲟⲉⲅⲟ ⲁⲃⲥⲧⲣⲁⲗⲟⲡυⲧⲉⲕⲁ ⲟⲧцⲁ ⲡⲉⲇυⲕⲟⲃⲁⲧⲟⲅⲟ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩⲉⲙ ⲧⲉ ⲡυⲣⲥυⲏⲅ ⲥⲇⲉⲗⲁⲗ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲙⲁⲙⲁⲏⲉ ⲧⲃⲟⲉ ⲙⲟⳡⲕⲩ ⲭⲩⲉⲙ ⲡⲣⲟⲕⲟⲗⲟⲗ <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⳝⲉⳅ ⲱⲁⲏⲥⲟⲃ ⲉⳝⲁⲗⲟⲇⲣⲟⳝυⲧⲉⲗьⲏⲟ ⲥⲙⲉⲥью ⲥⲡⲉⲣⲙы υ ⲙⲟⳡυ υⳅⲅⲟⲏυⲙ ⲧⲉⳝя <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲡⲟⲧⲩⲥⲧⲁⲣⲟⲏⲏⲉ ⲥⲟⲥёⲱь <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲥⲗюⲏяⲃⲟ υⳅⲩⲃⲉⳡⲩ ⲧⲉⳝя<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲣⲉⲕⲧⲁⲗьⲏⲟ ⲉⳝⲁⲣυⲣⲩю ⲧⲉⳝя <emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲧы ⲕⲩⲇⲁ ⲡⲟⲥⲙⲉⲗ ⲧⲩⲧ ⲡⲣⲟⲧυⲃ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ ⲡⲟⲡⲉⲣⲉⲧь ⲥыⲏⲟⲕ ⲁⲡⲣυⲟⲣυ ⲏⲉⲇⲉⲉⲥⲡⲟⲥⲟⳝⲏⲟύ ⳝⲗяⲇυ<emoji document_id=5175094382298137311>🌟</emoji>"
, "[<emoji document_id=5175094382298137311>🌟</emoji>]ⲭⲩяⲙυ ⲩⳃⲉⲗьⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲕⲣⲟⲉⲙ <emoji document_id=5175094382298137311>🌟</emoji>"
]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl6))
            await sleep(0.1)
            await sleep(time)

    async def смертьcmd(self, message):
        """— Запускает модуль по указанной команде """
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message,
             "<b>Смерть ɜᥲκ᧐нчᥙ᧘а ɜᥲδᥙρᥲᴛь хуᥱᥴ᧐ᥴ᧐ʙ ʙ ʍᥙρ ɜ᧘ᥲ <emoji document_id=5784974820592586088>🔥</emoji></b>")
            return
        await utils.answer(
            message,
            "<b>Смерть нᥲчᥲ᧘ᥲ ɜᥲδᥙρᥲᴛь хуᥱᥴ᧐ᥴ᧐ʙ ʙ ʍᥙρ ɜ᧘ᥲ <emoji document_id=5784974820592586088>🔥</emoji></b>"
            "<b>Чтобы остановить пропиши. <code>.смерть</code></b>"
        )
        try:
            time = float(args[0])
        except ValueError:
            return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl7 = [
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь, ᴄʜᴛᴏ ᴋʟɪᴛᴏʀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴇᴛᴏ ᴄʜʀᴇᴢᴠʏᴄʜᴀᴊɴᴏ ᴏᴘᴀsɴᴀʏᴀ ᴢᴏɴᴀ? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴅᴀᴠᴀᴊ ɴᴇ ᴘɪᴢᴅɪ, ᴀ ʜᴜᴊ ᴍᴏᴊ ᴠsᴀsɪ ᴘɪᴢᴅᴀʙᴏʟ ᴇʙᴀɴʏᴊ. ᴛʏ ᴢʜᴇ ᴛᴜᴛ ɪ sᴜᴛᴏᴋ ɴᴇ ᴘʀᴏᴛʏᴀɴᴇsʜь, ᴜʙᴇᴢʜɪsʜь sᴠᴏᴇᴊ ᴍᴀᴍᴀsʜᴇ ᴘɪᴢᴅᴜ ʟɪᴢᴀᴛь ɪ ʜᴠᴀsᴛᴀᴛьsʏᴀ ᴛᴇᴍ, ᴄʜᴛᴏ ᴏᴛsᴏsᴀʟ ʜᴜᴊ ᴠᴇʟɪᴋᴏᴍᴜ ᴢʟᴏᴅᴇʏᴜ. <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴢɴᴀʟ ᴄʜᴛᴏ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ɪᴢ ᴏᴋɴᴀ ᴠʏᴋɪɴᴜʟ ᴀ ᴏɴᴀ ᴠsᴛᴀʟᴀ ɪ ᴅᴀʟьsʜᴇ ᴘᴏʙᴇᴢʜᴀʟᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛᴜʜᴀ s 5 ʟᴇᴛ ɴᴀ ᴍᴏᴊ ʜᴜᴊ ᴍᴏʟɪʟᴀsь ʟʏᴀᴠʀᴀ ᴇʙᴜᴄʜᴀʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴜ ᴍᴀᴍᴜ ʜᴜёᴍ ᴛᴀᴋ ʀᴀᴢᴠёʟ ᴄʜᴛᴏ ᴏɴᴀ ᴠsᴇᴍᴜ ʀᴀᴊᴏɴᴜ ɢᴏᴠᴏʀɪʟ ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴇᴛᴏ ʀᴇʟɪᴋᴠɪʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ᴛᴀᴋ ᴛᴏ ᴅᴏ ᴏʀɢᴀᴢᴍᴀ ᴅᴏᴠёʟ ᴀ ᴛᴠᴏᴊ ʙᴀᴛʏᴀ ᴠ ᴇᴛᴏ ᴠʀᴇᴍʏᴀ ᴠ ᴀʜᴜᴇ sᴛᴏʏᴀʟ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴢʜᴇ ᴅᴀᴠɴᴏ ɴᴀ ʜᴜᴇ ᴍᴏёᴍ sɪᴅɪᴛ ᴏɴᴀ ᴅᴜᴍᴀᴇᴛ ᴄʜᴛᴏ ᴇsʟɪ ᴘᴜsᴋᴀᴇᴛ sᴘᴇʀᴍᴀᴋ ᴘᴏ ᴋʀᴏᴠɪ ᴛᴏ ᴇᴛᴏ ɴᴏʀᴍᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴅᴜᴍᴀʟ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀ sʜᴀʟᴀᴠᴀ ᴍʏ ᴇё s ᴘᴀᴛsᴀɴᴀᴍɪ ᴢᴀ ᴅᴠᴏʀᴀᴍɪ ʜᴜʏᴀᴍɪ ᴘᴏʟᴏsᴏᴠᴀʟɪ ᴛᴏʟьᴋᴏ ɴᴇ ᴋᴏᴍᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴇsᴄʜё ᴍᴏʟɪsʜьsʏᴀ ᴢᴀ ᴛᴏ ᴄʜᴛᴏʙʏ ᴛᴠᴏʏᴀ ᴍᴀᴛᴜʜᴀ ᴍɴᴇ ʜᴜᴊ sᴏsᴀʟᴀ ᴇsʟɪ ᴅᴀ ᴛᴏ ᴍᴏɢᴜ ᴘᴏᴢᴅʀᴀᴠɪᴛь ᴏɴᴀ ᴅᴏsɪʜᴘᴏʀ ᴢᴀᴠɪsɪᴍᴀ ᴏᴛ ʜᴜʏᴀ ᴍᴏᴇɢᴏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍᴏɢᴜ sᴋᴀᴢᴀᴛь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴠ ʀᴀᴅᴏsᴛь sᴏsёᴛ ᴍᴏᴊ ʜᴜᴊ ɪ ᴇᴛᴏ ᴇᴊ ᴅᴀёᴛ ᴍᴏʀᴇ ᴘᴏʟᴏᴢʜɪᴛᴇʟьɴʏʜ ᴇᴍᴏᴛsɪᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɪ ᴄʜё ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴅᴏʟɢᴏ ʙᴜᴅᴇᴛ ʙɪᴛьsʏᴀ ᴠ ᴋᴏɴᴠᴜʟьsɪʏᴀʜ ᴏᴛ ʜᴜʏᴀ ᴍᴏᴇɢᴏ ᴢᴀʙɪʀᴀᴊ ᴇё sᴋᴏʀᴇᴊ ᴅᴜʀɴᴏᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴄʜё ᴅᴜᴍᴀᴇsʜь ʏᴀ sᴄʜᴀs ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘʀᴏsᴛᴏ ᴛᴀᴋ ᴏᴛᴘᴜsᴄʜᴜ ɴᴇ ᴘᴜsᴛь ɢᴏᴅ ᴍɴᴇ ᴘᴏsᴏsёᴛ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀ ᴛʀᴀssᴇ sᴛᴏʏᴀʟᴀ ɪ ᴋᴀᴢʜᴅʏᴊ ʀᴀᴢ ᴢʜᴅᴀʟᴀ ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴇё ᴢᴀʙᴇʀёᴛ ɴᴏ ʏᴀ ᴇᴊ ʟɪsʜь ɴᴀ ʀᴏᴛᴀɴ ᴋɪᴅᴀʟ ɪ ᴜᴇᴢᴢʜᴀʟ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɪ ᴄʜё ᴛʏ ᴅᴜʀᴀ ᴇʙᴀɴᴀʏᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴢᴀ ᴍᴏᴊ ʜᴜᴊ ᴅʀᴀʟᴀsь s ᴅᴇᴠᴋᴀᴍɪ ᴏɴᴀ ᴅᴜᴍᴀʟᴀ ᴄʜᴛᴏ sᴛᴀɴᴇᴛ ʟᴜᴄʜsʜᴇᴊ ᴏᴛsᴏsᴋᴏᴊ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ᴏɴᴀ ᴘᴏᴄʜᴛɪ ᴅᴏsᴛɪɢʟᴀ ᴇᴛᴏᴊ ᴛsᴇʟɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴇsʟɪ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏsᴀᴅɪᴛь ɴᴀ ᴍᴏᴊ ʜᴜᴊ ᴘᴏᴠᴇʀь ᴏɴᴀ ɴᴇ sʟᴇᴢᴇᴛ ᴘᴏᴋᴀ ɴᴇ ᴜᴍʀёᴛ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʀɪʟɪ ʜᴜёᴍ ᴘᴏʜᴏʀᴏɴɪʟ ᴏɴᴀ ᴜᴍᴜᴅʀɪʟᴀsь ᴠʏʙʀᴀᴛьsʏᴀ ᴄʜᴛᴏʙʏ ɴᴀ ᴘᴏsʟᴇᴅᴏᴋ ᴇsᴄʜё ᴍɴᴇ ᴏᴛsᴏsᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴜ ᴇᴛᴏ ᴜᴢʜᴇ sᴛʀᴀɴɴᴏ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴛᴀᴋ ᴄʜᴀsᴛᴏ ᴠʀёᴛ ᴛᴠᴏᴇᴍᴜ ᴏᴛᴛsᴜ ᴄʜᴛᴏ ᴏᴛsᴀsʏᴠᴀᴇᴛ ᴍɴᴇ ᴠsᴇɢᴏ ᴘᴏ 10 ʀᴀᴢ ᴠ ᴅᴇɴь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏᴊ ᴘᴀʜᴀɴ sɴɪᴍᴀʟ ɴᴀ ᴠɪᴅᴇᴏ ᴋᴀᴋ ʏᴀ ᴇʙᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ɪ ʀᴀᴅᴏᴠᴀʟsʏᴀ ᴠᴇᴅь ʏᴀ ᴛᴏᴢʜᴇ ᴠᴇʟɪᴋɪᴊ ᴅʟʏᴀ ᴛᴠᴏᴇɢᴏ ᴘᴀʜᴀɴᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍᴏᴢʜᴇsʜь ɢᴏᴠᴏʀɪᴛь ᴠsё ᴄʜᴛᴏ ᴜɢᴏᴅɴᴏ ɴᴏ ʏᴀ ʙᴜᴅᴜ ᴇʙᴀᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴋᴀ ᴏɴᴀ ɴᴇ sᴏᴠᴇʀsʜɪᴛ sᴜɪᴛsɪᴅ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴅᴀᴢʜᴇ ɴᴇ ᴍᴏᴢʜᴇᴛ ᴀʀɢᴜᴍᴇɴᴛɪʀᴏᴠᴀᴛь sᴠᴏё sᴏsᴀɴɪʏᴀ ᴇᴛᴏ sᴛᴀʟᴏ ᴇё ʜᴏʙɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴅᴜᴍᴀʟ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴏᴢᴅᴀsᴛ ғᴀɴ ᴋʟᴜʙ ᴅʟʏᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ɪ ᴅᴏᴋᴀᴢʏᴠᴀᴛь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ sᴀᴍʏᴊ ʟᴜᴄʜsʜɪᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɪ ᴄʜё ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴍɴᴇ sᴏsёᴛ ᴀ ᴛʏ ɴᴇᴍᴏsᴄʜь ᴅᴀᴢʜᴇ ɴᴇ ᴍᴏᴢʜᴇsʜь ᴇё ᴢᴀᴍᴇɴɪᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴄʜё ʙʟʏᴀᴛь ʏᴀ sᴄʜᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴠ ᴘᴇʀᴅᴀᴋ ʜᴜʏᴀʀʏᴜ ᴀ ᴏɴᴀ ᴘʏᴛᴀᴇᴛьsʏᴀ ᴋᴜᴅᴀ ᴛᴏ ᴜʙᴇᴢʜᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴍᴏɢᴜ ᴘᴏɴʏᴀᴛь ᴘᴏᴄʜᴇᴍᴜ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀ sᴛᴏʟьᴋᴏ ᴜsᴇʀᴅɴᴏ sᴏsёᴛ ᴍᴏᴊ ʜᴜᴊ ᴋ ᴄʜᴇᴍᴜ ᴏɴᴀ sᴛʀᴇᴍɪᴛьsʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴜᴢʜᴇ sʙɪʟsʏᴀ s ᴄʜёᴛᴜ sᴋᴏʟьᴋᴏ ʏᴀ ᴇʙᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ɴᴀᴅᴏ sᴘʀᴏsɪᴛь ᴜ ᴛᴠᴏᴇɢᴏ ᴏᴛᴛsᴀ ᴠᴇᴅь ᴏɴ ᴅʀᴏᴄʜɪʟ ɴᴀ ᴇᴛᴏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏᴊ ᴏᴛᴇᴛs ᴅᴀᴠɴᴏ ᴜᴢʜᴇ ᴜʜᴏᴅɪ s ᴋᴠᴀʀᴛɪʀʏ ɪ ᴢʜᴅёᴛ ᴘᴏᴋᴀ ʏᴀ ᴘᴏᴇʙᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴀ ᴘᴏᴛᴏᴍ ᴘʀɪʜᴏᴅɪᴛ ᴋᴀᴋ ɴᴇ ᴠ ᴄʜёᴍ ɴᴇ ʙʏᴠᴀʟ ᴏʟᴜʜ ᴛʏ ᴇʙᴀɴʏᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴇʙᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴋᴀ ᴇᴛᴏ ɴᴇ sᴛᴀʟᴏ ᴍᴇᴊɴsᴛʀɪᴍᴏᴍ ʀɪʟɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "sᴄʜᴀs ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴋᴜᴅᴀ ᴛᴏ ᴘᴏʙᴇᴢʜᴀʟᴀ ɪ ᴅᴜᴍᴀᴇᴛ ᴄʜᴛᴏ ᴇᴊ ᴇᴛᴏ ᴘᴏᴍᴏᴢʜᴇᴛ ɴᴏ ᴠᴇᴅь ᴍᴏᴊ ʜᴜᴊ ᴇё ᴠsᴇ ʀᴀᴠɴᴏ ᴅᴏɢᴏɴɪᴛ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏᴊ ᴅᴇᴅ ᴠ 45 ᴍɴᴇ ʜᴜᴊ ᴢᴀ ᴋᴜsᴏᴋ sᴀʟᴏ sᴀsᴀʟ ʀɪʟɪ ɴᴇᴍᴏsᴄʜь ᴏɴ ᴇʙᴀɴʏᴊ ᴅᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɪ ᴄʜё ʙᴜᴅᴜ ᴇʙᴀᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴅᴏ ᴛᴀʟᴏᴠᴀ ɪ ᴛʏ ɴᴇ sᴍᴏᴢʜᴇsʜь ᴍɴᴇ ɴᴇ ᴄʜᴇɢᴏ sᴋᴀᴢᴀᴛь ᴠᴇᴅь sᴀᴍ ᴠ ᴛᴀᴊɴᴇ ᴍɴᴇ sᴏsёsʜь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴢʜᴇ ᴅᴀᴠɴᴏ ɴᴀᴄʜᴀʟᴀ ᴘʀᴏʏᴀᴠʟʏᴀᴛь ᴜᴠᴀᴢʜᴇɴɪʏᴀ ᴋ ᴍᴏᴇᴍᴜ ʜᴜʏᴜ ɪ ᴢᴅᴀʀᴏᴠᴀᴇᴛьsʏᴀ s ɴɪᴍ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴛʏ ᴄʜё ᴅᴜᴍᴀʟ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴅᴏʟɢᴏ sᴍᴏᴢʜᴇᴛ ɴᴀ ᴍᴏᴊ ʜᴜᴊ ʀʏᴘᴀᴇᴛьsʏᴀ ʏᴀ ᴇᴊ ᴢᴀ ᴇᴛᴏ ʜᴜёᴍ ᴘᴏ ɢᴏʀʙᴜ ɴᴀᴠᴇʀɴᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴍɴᴇ ᴠ ɴᴀsʟᴇᴅsᴛᴠᴏ ᴢᴀᴠᴇsᴄʜᴀʟᴀ ᴛᴠᴏᴊ ʀᴏᴛ ᴇsʟɪ ʙᴜᴅᴇsʜь ᴇᴛᴏ ᴏᴛʀɪᴛsᴀᴛь ʏᴀ ᴇё ʜᴜёᴍ ɪᴢ ɢʀᴏʙᴀ ᴅᴏsᴛᴀɴᴜ ᴄʜᴛᴏʙʏ ᴏɴᴀ ᴘᴏᴅᴛᴠᴇʀᴅɪʟᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴜ ᴄʜё ᴘʀɪsᴛᴜᴘɪᴍ ʀᴀsᴄʜᴇʜʟʏᴀᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь ɪʟɪ ᴛʏ ᴅᴀᴢʜᴇ ᴘᴏʙᴏɪsʜьsʏᴀ ʀʏᴘɴᴜᴛьsʏᴀ ɴᴀ ᴍᴇɴʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇ ʀᴀᴢ ᴘᴀᴅᴀʟᴀ ɴᴀ ᴍᴏёᴍ ʜᴜʏᴜ ɴᴏ ᴏɴᴀ sᴛʀᴇᴍɪʟᴏsь ᴋ ᴠᴇʀsʜɪɴᴇ ᴅᴜʀᴀ ᴇʙᴀɴᴀʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʀᴀᴋᴜsʜᴋᴀ ɴᴀʜᴜᴊ ᴛʏ ᴘʀʏᴀᴄʜᴇsʜьsʏᴀ sᴠᴏʏᴜ ᴍᴛᴀь ᴏᴛ ʜᴜʏᴀ ᴍᴏᴇɢᴏ ᴜ ɴᴇё ɴᴀ ᴘɪᴢᴅᴇ ɢᴇᴏʟᴏᴋᴀᴛᴏʀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ʟᴇɢʟᴀ ᴘᴏᴅ ᴍᴏᴊ ʜᴜᴊ ɪ ᴠʀёᴛ ᴄʜᴛᴏ ɴᴇ ᴍᴏᴢʜᴇᴛ ᴠʏʟᴇᴢᴛɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ʜᴏᴄʜᴜ ᴛᴇʙʏᴀ ᴏsᴋᴏʀʙɪᴛь ɴᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴏᴛsᴀsʏᴠᴀʟᴀ ᴍɴᴇ ᴘᴏ 100 ʀᴀᴢ ɴᴀ ᴅɴʏᴜ ɴᴏ ᴅʟʏᴀ ɴᴇё ᴇᴛᴏ ɴᴇ ʀᴇᴋᴏʀᴅ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴜ ɪ ᴄʜё ᴛʏ ᴅᴏsɪʜᴘᴏʀ ᴅᴜᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ʙᴜᴅᴇᴛ ᴇʙᴀᴛь ᴠᴀsʜᴜ sᴇᴍᴊᴋᴜ ᴢᴀ ʙᴇsᴘʟᴀᴛɴᴏ sᴋᴏʀᴏ ᴠᴀᴍ ᴘʀɪᴅёᴛьsʏᴀ ᴘʟᴀᴛɪᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘʀᴇᴢʜᴅᴇ ᴄʜᴇᴍ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀᴄʜɪɴᴀᴇᴛ sᴏsᴀᴛь ʏᴀ ʙьʏᴜ ᴇᴊ ʜᴜёᴍ ᴘᴏ ɢᴜʙᴇ ᴇᴊ ɴʀᴀᴠɪᴛьsʏᴀ ᴠᴇᴅь ᴇᴛᴏ ᴘᴀsᴛᴀ ᴅᴀᴠɴᴏ ᴠᴏ ᴠʟᴀsᴛɪ ᴍᴏᴇɢᴏ ʜᴜʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴅᴀᴢʜᴇ ɴᴇ ᴢᴀᴍᴇᴛɪsʜь ᴋᴀᴋ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀ ᴍᴏᴊ ʜᴜᴊ ᴢʜɪᴛь ᴘᴇʀᴇᴇᴅᴇᴛ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴄʜᴀ ᴍᴏᴊ ʜᴜᴊ ʀᴇsʜɪʟᴀ ᴠ ᴍᴜᴢᴇᴊ ᴘʀᴇɴᴇsᴛɪ ɪ sᴋᴀᴢᴀᴛь ᴄʜᴛᴏ ᴇᴛᴏ ᴠᴇʟɪᴋɪᴊ ᴀʀᴛᴇғᴀᴋᴛ ᴄʜё ᴏɴᴀ sʜᴀʟᴏᴠᴀ ᴛᴏ ᴛᴀᴋᴀʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʙᴇᴢ sʜᴜᴛᴏᴋ ᴇsʟɪ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇ ɴᴀᴄʜɴёᴛ ᴠ ᴛᴇᴍᴘᴇ sᴏsᴀᴛь ʏᴀ ᴇᴊ ᴢᴀʟᴜᴘᴏᴊ ᴘᴏ ᴇʙᴀʟᴜ sᴇᴢᴢʜᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɪ ᴄʜё ᴛʏ sᴄʜᴀs ᴛᴏᴢʜᴇ ʙᴜᴅᴇsʜь ᴏᴛ ʜᴜʏᴀ ᴜᴠɪʟɪᴠᴀᴛь ᴋᴀᴋ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɪʟɪ ɴᴀᴄʜɴёsʜь ɴᴀ ɴᴏʀᴍᴇ sᴏsᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴍᴏɢᴜ ᴘᴇʀᴇᴅᴀᴛь ᴛᴇ ᴄʜᴜᴠsᴛᴠᴀ ᴋᴏɢᴅᴀ ᴛᴠᴏʏᴀ sᴘɪᴅᴏᴢɴᴀʏᴀ ᴍᴀᴍᴀsʜᴀ ᴍɴᴇ sᴏsёᴛ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴀ sᴄʜᴀ ᴍᴏᴊ ʜᴜᴊ ᴢᴀ sᴄʜᴇᴋᴜ ᴘᴜsᴛɪʟᴀ ɪ ɴᴇ ʜᴏᴄʜᴇᴛ ᴠʏsᴏᴠʏᴠᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴢʜᴇ ɴᴀ ᴍᴏᴊ ʜᴜᴊ ᴘʀʏɢᴀᴇᴛ ᴋᴀᴋ ɴᴀ ʀᴀʙᴏᴛᴜ ɪᴅёᴛ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴢᴀᴄʜᴇᴍ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴏᴘʏᴀᴛь ᴍɴᴇ sᴏsёᴛ ᴍᴏᴢʜᴇᴛ ᴏɴᴀ ᴘᴏᴅᴜᴍᴀʟᴀ ᴄʜᴛᴏ ᴍᴏᴢʜᴇᴛ ᴏᴛsᴀsʏᴠᴀᴛь ᴍɴᴇ ʙᴇᴢʟᴇᴍɪᴛɴᴏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴘᴀʟᴀ ᴘᴇʀᴇᴅ ᴍᴏɪᴍ ʜᴜёᴍ ᴋᴏɢᴅᴀ ᴘᴏᴅsᴛᴀᴠɪʟ ᴘᴇʀᴅᴀᴋ ᴘᴇʀᴇᴅ sᴠᴏɪᴍ ʙᴀᴛᴇᴊ ɴᴏ ᴇᴛᴏᴛ ᴏsёʟ ᴘᴏʙᴏʏᴀʟsʏᴀ ᴇɢᴏ ᴘᴏᴇʙᴀᴛь ᴠᴇᴅь ᴏɴ ᴢɴᴀᴇᴛ ᴄʜᴛᴏ ᴍᴏʏᴀ ᴢᴀʟᴜᴘᴀ ᴏᴘʏᴀᴛь ᴘʀᴏʙьёᴛ ᴇɢᴏ ɢᴏʀʙ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴍᴜʟьᴋᴀ sᴄʜᴀ ᴍᴏᴊ ʜᴜᴊ ᴘᴏ ɢʟᴀɴᴅʏ ᴘᴜsᴛɪʟᴀ ʏᴀ ᴘʀᴇᴅʟᴀɢᴀʏᴜ ᴅᴀᴛь ᴇᴊ ᴍᴇᴅᴀʟьᴋᴜ ᴢᴀ ɢᴏᴅᴏᴠᴏᴊ ᴏᴛsᴏs ʙᴇᴢ ᴘᴇʀᴇʀʏᴠᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴜ ɴᴜ sᴋᴀᴢʜɪ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴋᴀ ɴᴇ sʜᴀʙᴏʟᴅᴀ ʏᴀ sᴠᴏɪᴍ ʜᴜёᴍ ᴇᴛᴏ ᴏᴘʀᴏᴠᴇʀɢɴᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʀᴀᴢᴠᴏʀᴏsʜɪʟ ᴛᴠᴏʏᴜ ᴍᴀᴍᴀsʜᴋᴜ ʜᴜёᴍ ɪ ᴠʏɴᴇs ᴏᴛ ᴛᴜᴅᴀ ᴠsё ᴄʜᴛᴏ ᴍᴏᴢʜɴᴏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴛᴠᴏʏᴜ ᴅᴜʀɴᴜʏᴜ ᴍᴀᴍᴀsʜᴜ sᴄʜᴀ ɴᴀ ʜᴜᴇ ᴢᴀ ᴛᴀᴋɪᴇ ᴅᴠɪᴢʜᴇɴɪʏᴀ ᴘʀᴏᴠᴇʀɴᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴠᴇʀɪsʜь ᴍɴᴇ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴀ ᴍᴏᴊ ʜᴜᴊ ʙᴇᴢᴀsᴛᴏɴᴏᴠᴄʜɴᴏ sᴏsёᴛ ᴛᴀᴋ ᴘʀɪʜᴏᴅɪ ᴏɴᴀ ᴅᴀsᴛ ᴛᴇ ᴜʀᴏᴋɪ ᴏᴛsᴏsᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴍᴏɢᴜ ᴘᴏɴʏᴀᴛь ᴘᴏᴄʜᴇᴍᴜ ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴀ ᴛᴀᴋᴀʏᴀ sʟᴀʙᴀʏᴀ sʜʟʏᴜʜᴀ ᴄʜᴛᴏ ᴅᴀᴢʜᴇ ᴍᴏᴊ ʜᴜᴊ ᴜᴢʜᴇ ᴏsɪʟɪᴛь ɴᴇ ᴍᴏᴢʜᴇᴛ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴜ ᴍᴀᴍᴀsʜᴜ sᴄʜᴀ ʜᴜёᴍ ᴘᴇʀᴇᴠᴇʀɴᴜ ʜᴏᴛʏᴀ ᴇᴛᴏ ᴢʜᴀʟᴋᴀʏᴀ ɴᴀᴄʜɴёᴛ ᴏᴘʏᴀᴛь ᴠ ᴋᴏɴᴠᴜʟьsɪʏᴀʜ ʙɪᴛьsʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴜ ᴜᴢʜᴇ ʙᴇᴢ sʜᴜᴛᴏᴋ ᴠ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ʀᴀᴢᴀɢɴᴀʟsʏᴀ ᴀ ᴏɴᴀ ɴᴀᴄʜɪɴᴀᴇᴛ ᴋᴀᴋ sᴠɪɴьʏᴀ ᴠɪᴢᴢʜᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ᴠʏsᴇᴋ ᴢᴀ ᴛᴏ ᴄʜᴛᴏ ᴏɴᴀ ᴛᴠᴏᴇᴍᴜ ʙᴀᴛɪ ᴏᴛsᴏsᴀᴛь ᴘʏᴛᴀʟᴀsь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ʟᴇᴢʟᴀ ᴋᴏ ᴍɴᴇ ᴛsᴇʟᴏᴠᴀᴛьsʏᴀ ɴᴏ ᴇᴊ ᴢᴀʟᴜᴘᴏᴊ ʟᴏʙ ʀᴀsᴋʀᴏsʜɪʟ ᴘᴜsᴛь ᴢɴᴀᴇᴛ sᴠᴏё ᴍᴇsᴛᴏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴜ ɪ ᴄʜё ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴢʜᴇ ɢɪʟьᴅɪʏᴜ sᴏᴢᴅᴀʟᴀ ᴄʜᴛᴏʙʏ ᴍᴏᴊ ʜᴜᴊ ᴠᴏsʜᴠᴀʟʏᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴄʜᴀ ᴍᴏᴊ ʜᴜᴊ ᴘʀɪ ᴘᴏᴅʀᴜɢᴀʜ ʀᴀsʜᴠᴀʟɪᴠᴀʟᴀ ɪ ᴏɴɪ ᴛᴏᴢʜᴇ ʀᴇsʜɪʟɪ ᴍɴᴇ ᴏᴛsᴏsᴀᴛь ɴᴏ ʟᴜᴄʜsʜᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴜʜᴇ ɴᴇ ᴋᴛᴏ ɴᴇ sᴏsёᴛ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴇsʟɪ ᴛʏ ʜᴏᴄʜᴇsʜь ᴍᴏᴊ ʜᴜᴊ ᴛᴏɢᴅᴀ ᴛᴇ ᴘʀɪᴅёᴛьsʏᴀ ᴘᴏᴋᴏɴᴋᴜʀɪʀᴏᴠᴀᴛь s ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜᴇᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴜ ɪ ᴄʜё ᴛʏ sᴄʜᴀs ᴘᴏᴅᴏʜɴᴇsʜь ɴᴀ ᴍᴏёᴍ ʜᴜʏᴜ ᴄʜᴇᴍ ᴏᴘᴏᴢᴏʀɪsʜь sᴠᴏʏᴜ ᴍᴀᴍᴀsʜᴜ ʜᴏᴛʏᴀ ᴍᴏᴊ ʜᴜᴊ ɪ ᴛᴀᴋ ᴇё ᴏᴘᴜsᴛɪʟ ᴇᴢ ᴇᴢ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛᴜsʜᴋᴀ ᴍᴏᴢʜᴇᴛ ᴏᴛʀɪᴛsᴀᴛь ᴄʜᴛᴏ sᴏsᴀʟᴀ ᴍɴᴇ ɴᴏ ᴜ ᴍᴇɴʏᴀ ᴇsᴛь ᴘʀʏᴀᴍᴏᴇ ᴅᴏᴋᴀᴢᴀᴛᴇʟьsᴛᴠᴏ ᴠᴇᴅь ʏᴀ ᴢᴀᴋᴀᴄʜᴀʟ ᴇё ɪᴢɴᴜᴛʀɪ sᴘᴇʀᴍᴏᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴘʀᴏᴠɪɴɪʟᴀsь ᴘᴇʀᴇᴅ ᴍᴏɪᴍ ʜᴜёᴍ ɪ ᴇᴊ ᴘʀɪsʜʟᴏsь ɪᴢᴠᴇɴʏᴀᴛьsʏᴀ sᴠᴏᴇᴊ ᴢʜᴀʟᴋᴏᴊ ɢʟᴏᴛᴋᴏᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴜ ᴛʏ ʀɪʟɪ ɴᴇ ᴠᴅᴜᴘʟʏᴀᴇsʜь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴍᴏᴊ ʜᴜᴊ ʀᴇsʜɪʟᴀ ᴠ ᴀʀᴇɴᴅᴜ ᴠᴢʏᴀᴛь ɴᴀ ᴅᴇɴь ɪᴢ ᴢᴀ ᴄʜᴇɢᴏ ᴘʀᴏᴅᴀʟᴀ ᴘᴏᴄʜᴋᴜ ᴛᴠᴏᴇɢᴏ ʙᴀᴛɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴜ ᴄʜё ʙᴜᴅᴇᴍ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀᴛь ɪʟɪ ᴛʏ ᴏᴘʏᴀᴛь ʀᴇsʜɪʟ ᴍᴏᴊ ʜᴜᴊ ɴᴇ s ᴋᴇᴍ ɴᴇ ᴅᴇʟɪᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʜᴜёᴍ ᴛᴠᴏʏᴜ ᴍᴀᴛь sᴄʜᴀ ʀᴀᴢᴍᴇɴɪʀᴏᴠᴀʟ ᴀ ᴏɴᴀ ᴏᴛ ʙʟᴀɢᴏᴅᴀʀɴᴏsᴛɪ ᴏʙ ᴍᴏᴊ ʜᴜᴊ sᴠᴏʏᴜ ᴘɪᴢᴅᴜ sᴛёʀʟᴀ ɴᴀ ᴇᴢ ᴇᴢ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴜ ᴍᴀᴛь sᴄʜᴀ ʜᴜёᴍ ʀᴀsᴄʜᴇʟᴇɴɪʟ ᴀ ᴏɴᴀ ᴅᴀᴢʜᴇ ᴠ ᴛᴀᴋᴏᴍ ᴘᴏʟᴏᴢʜᴇɴɪɪ sᴍᴏɢʟᴀ ᴏᴛsᴏsᴀᴛь ᴍɴᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇ ᴍᴏᴢʜᴇᴛ ᴘᴏɴʏᴀᴛь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ɴᴇ ᴠsᴇɢᴅᴀ ʙᴜᴅᴇᴛ ᴅᴇʀᴢʜᴀᴛь ɴᴀᴅ ɴᴇᴊ ᴠʟᴀsᴛь ᴛᴀᴋ ᴛᴏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʜᴜёᴍ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘʟᴏᴍʙɪʀᴏᴠᴀʟ ᴇᴊ ᴅᴀᴢʜᴇ ᴋ sᴛᴀᴍᴀᴛᴏʟᴏɢᴜ ʜᴏᴅɪᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ʀᴀᴢʀᴇᴢᴀʟ ᴀ ᴏɴᴀ ᴘᴏʙᴇᴢʜᴀʟᴀ ᴋ ᴛᴠᴏᴇᴍᴜ ʙᴀᴛɪ ɪ ᴘᴏᴋᴀᴢᴀʟᴀ ᴏᴛʀᴇᴢᴀɴᴜʏᴜ ᴘɪᴢᴅᴜ ᴋᴀᴋ ᴘʀɪᴋᴏʟ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʜᴜёᴍ ᴛᴠᴏʏᴜ ᴍᴀᴛь ɴᴀᴜᴄʜɪʟ ᴘɪsᴀᴛь ɴᴏ ᴏɴᴀ ᴘʟᴏʜᴏ ᴠᴏsᴘʀɪɴɪᴍᴀᴇᴛ ᴜᴄʜᴇɴɪʏᴀ ɪ ɴᴀᴄʜɪɴᴀᴇᴛ sᴏsᴀᴛь ɴᴀ ᴀᴠᴛᴏᴍᴀᴛᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ sᴛʀᴇʟʏᴀʟ ᴠ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ᴠʏsᴛʀᴇʟɪʟ ɪ ᴏɴᴀ ᴛᴠᴀʀь ᴏᴢʜɪʟᴀ ɪ ɴᴀᴄʜᴀʟᴀ ᴘᴏʟᴢᴛɪ ᴋ ᴍᴏᴇᴍᴜ ʜᴜʏᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ʀᴇᴋᴏʀᴛsᴍᴇɴᴋᴀ ᴘᴏ sᴏsᴀɴɪʏᴜ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ᴇё ʀᴇᴋᴏʀᴅ ᴅᴀᴢʜᴇ ᴛᴠᴏᴊ ʙᴀᴛʏᴀ ɴᴇ ᴍᴏᴢʜᴇᴛ ᴘᴏʙɪᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴜ ɪ ᴄʜё ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴍɴᴇ sᴏsᴀʟᴀ ɴᴇ ɴᴀᴅᴏ ᴏᴛʀɪᴛsᴀᴛь ᴠᴇᴅь ᴛʏ ᴛᴏᴢʜᴇ ᴢᴀᴘᴏᴅᴏᴢʀᴇɴ ᴠ ᴇᴛᴏᴍ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʀᴀᴢᴋᴜᴍᴀʀɪʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ᴅᴀ ᴛᴀᴋᴏᴊ sᴛᴇᴘᴇɴɪ ᴄʜᴛᴏ ᴏɴᴀ ᴇʟɪ ᴇʟɪ ᴅᴏʙʀᴀʟᴀsь ᴅᴏ ᴅᴏᴍᴀ ᴅᴀᴢʜᴇ ᴘᴏ ᴅᴏʀᴏɢᴇ ᴏɴᴀ ᴜsᴘᴇʟᴀ ᴋᴏᴍᴜ ᴛᴏ ᴏᴛsᴏsᴀᴛь sʜᴀʟᴀᴠᴀ ᴢʜᴀʟᴋᴀʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴜ ɪ ᴄʜё ᴛʏ ᴍᴏᴢʜᴇsʜь ʏᴀ ᴢʜᴇ sᴠᴏɪᴍ ʜᴜёᴍ ᴛᴠᴏɪ ᴍʏsʟɪ ᴛᴀᴋ ᴛᴏ ᴘᴇʀᴇsᴛʀᴏɪʟ ᴅᴜʀᴇɴь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴍᴏɢᴜ sᴋᴀᴢᴀᴛь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴏsёᴛ ᴠsᴇᴍ ᴏᴄʜᴇɴь ᴄʜᴀsᴛᴏ ᴠᴇᴅь ᴠᴏᴢʟᴇ sᴠᴏᴇɢᴏ ʜᴜʏᴀ ʏᴀ ᴠɪᴢʜᴜ ᴇё ᴋᴀᴢʜᴅʏᴊ ᴅᴇɴь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴜ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴢʜᴇ ᴘᴏ ʙʟᴀᴛᴜ ᴍɴᴇ sᴏsёᴛ ɴᴏ ᴇᴊ ɴᴇ ʜᴠᴀᴛᴀᴇᴛ sᴛɪᴍᴜʟᴀ ᴍᴏᴢʜᴇᴛ ᴛᴠᴏᴇᴍᴜ ʙᴀᴛɪ ʜᴜёᴍ ᴠᴇɴʏ ᴠsᴋʀʏᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴠᴏᴊ ʜᴜᴊ ᴠ ʀᴀᴍᴋᴜ ᴘᴏsᴛᴀᴠɪʟ ɪ ᴛᴇᴘᴇʀь ᴠʏ ᴠsᴇᴊ sᴇᴍьёᴊ ɪᴍ ʟʏᴜʙᴜᴇᴛᴇsь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴏ ᴘʀɪᴋᴏʟᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ɴᴀ ʟᴜɴᴜ ᴢᴀᴋɪɴᴜʟ ᴀ ᴏɴᴀ ᴅᴀᴢʜᴇ ᴛᴀᴍ ᴠ ᴘᴇʀᴅᴀᴄʜᴇʟᴏ ᴋᴏᴍᴜ ᴛᴏ ᴅᴀʟᴀ ᴏʀɴɪ s ᴇᴛᴏᴊ sʜʟʏᴜʜɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍᴏɢᴜ ᴛᴠᴏʏᴜ ᴍᴀᴍᴀsʜᴜ ʜᴜёᴍ ᴠᴢʏᴀᴛь ɴᴀ ᴘʀᴏɢɪʙ ɴᴏ ɴᴇ ʜᴏᴄʜᴜ ᴠᴇᴅь ᴏɴᴀ sᴛᴏɪᴛ ʀᴀᴋᴏᴍ ɪ ᴢʜᴅёᴛ ᴋᴏɢᴅᴀ ʏᴀ ᴇё ᴠʏᴇʙᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʀᴀssʜɪʀɪʟ ɢʟᴀɴᴅʏ ʜᴜёᴍ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴢᴀᴛᴏ ᴛᴇᴘᴇʀь ᴏɴᴀ ʙᴏʟьsʜᴇ ᴍᴏᴢʜᴇᴛ ᴏᴘʀᴀʙᴀᴛʏᴠᴀᴛь ᴍᴏᴊ ᴄʜʟᴇɴ sᴠᴏɪᴍ ʀᴛᴏᴍ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ sɪʟьɴᴏ ᴠьᴇʙᴀʟ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴢᴀʟᴜᴘᴏᴊ ɴᴏ ᴏɴᴀ ᴏᴛᴋʟʏᴜᴄʜɪʟᴀsь sᴄʜᴀ ᴘʀᴏsɴёᴛьsʏᴀ ᴘᴏ ɴᴏᴠᴏᴊ ᴇё ᴘᴏᴇʙᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ɴᴇɢᴀᴛɪᴠᴇ ᴇʙᴀʟ ᴍᴀᴛь ᴛᴠᴏʏᴜ ᴠᴇᴅь ᴏɴᴀ ᴢᴀᴇʙᴀʟᴀ ᴠʏʀʏᴠᴀᴛьsʏᴀ ᴢᴀ ᴄʜᴛᴏ ʏᴀ ᴇᴊ ᴜᴇʙᴀʟ ʟᴇsᴄʜᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʀᴀᴢᴏʀᴠᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ɴᴀ ᴄʜᴀsᴛɪ ᴛᴇʀь ᴛʏ ᴇᴅɪɴsᴛᴠᴇɴʏᴊ ᴋᴛᴏ ʙᴜᴅᴇᴛ ᴍᴏᴊ ʜᴜᴊ ᴅᴏ ᴜʙᴏʏᴀ sᴏsᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʀᴀsᴛʀᴏɢᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴋᴏɢᴅᴀ ʜᴜёᴍ ᴠьᴇʙᴀʟ ᴇᴊ ᴘᴏ ɢᴜʙᴀᴍ ᴠᴇᴅь ᴋᴀᴋ ᴍʏ ᴘᴏᴍɴɪᴍ ʏᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ʀᴀɴьsʜᴇ ʀᴀᴢɪʙᴠᴀʟ ᴀ sᴄʜᴀs ᴘʀᴏsᴛᴏ ʀᴀsёᴋ ᴏɴᴀ ʀᴀᴅᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴘᴏsᴛʀᴏɪʟ ᴏʙᴏʀᴏɴᴜ ᴏᴛ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ɴᴏ s ᴋᴀᴢʜᴅʏᴍ ᴜᴅᴀʀᴏᴍ ᴘᴏ sᴛᴇɴᴀᴍ ᴇᴛᴏᴊ ᴏʙᴏʀᴏɴʏ ʏᴀ ᴠsё ʙʟɪᴢʜᴇ ᴋ ɢʟᴏᴛᴋᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴜʜᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍᴏᴊ ʜᴜᴊ ᴜᴢʜᴇ ɴᴀ sᴛᴏʟьᴋᴏ ᴠʏʀᴏs ᴠ ɢʟᴀᴢᴀʜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴄʜᴛᴏ ᴏɴᴀ sᴏsёᴛ ᴇɢᴏ ᴍᴇsᴛᴏ ᴢᴀᴠᴛʀᴀᴋᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʀᴀᴢᴍᴜʀᴏᴠᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ᴋᴏɢᴅᴀ ᴏɴᴀ ɴᴇ ᴍᴏɢʟᴀ ᴠʏʙʀᴀᴛьsʏᴀ ɪᴢ ᴢᴀ ᴄʜᴇɢᴏ ᴛᴇᴘᴇʀь ᴏɴᴀ ᴘᴏ ᴢʜɪᴢɴᴇɴᴏ ᴍɴᴇ ᴅᴏʟᴢʜɴᴀ ᴏᴛsᴀsʏᴠᴀᴛь ᴀ ᴘᴏᴛᴏᴍ ᴛʏ ᴇё sᴍᴇɴɪsʜь ᴘʀᴀᴠᴅᴀ ᴢʜᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀᴋɪɴᴜʟ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴠ ᴋᴀʙɪɴᴜ ᴢᴀ ᴛᴏ ᴄʜᴛᴏ ᴏɴᴀ ʀᴇsʜɪʟᴀ ᴏsɪʟɪᴛь ᴍᴏᴊ ʜᴜᴊ sᴠᴏɪᴍ ʀᴛᴏᴍ ᴘᴜsᴛь ᴛᴀᴋᴀʏᴀ sʜᴀᴠᴋᴀ ᴅᴀᴢʜᴇ ɴᴇ ᴘɪᴛᴀᴇᴛ ɴᴀᴅᴇᴢʜᴅʏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀɢᴏʀɴᴜʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ᴘʀᴏsᴛᴏ ᴘᴏ ᴘʀɪɴᴛsɪᴘᴜ ɴᴏ ᴏɴᴀ ᴅᴀᴢʜᴇ ᴛᴀᴋ ʀᴇsʜɪʟᴀ ᴅᴀᴛь ᴍɴᴇ ᴠ ᴘɪᴢᴅᴜ ᴋᴀᴋ ʙʏʟᴀ sʜʟʏᴜʜᴏᴊ ᴛᴀᴋ ɪ ᴏsᴛᴀʟᴀsь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍʏ ᴘᴏsᴘᴏʀɪʟɪ s ᴏᴛᴛsᴏᴍ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴀ sᴏsᴀʟᴀ ᴍɴᴇ ɴᴇ ʙᴏʟьsʜᴇ 200 ʀᴀᴢ ᴠ ᴅᴇɴь ɴᴏ ᴏɴ ᴘʀᴏɪɢʀᴀʟ ᴠᴇᴅь ᴜᴠɪᴅᴇʟ ᴋᴀᴋ ᴏɴᴀ ᴏᴛsᴀsʏᴠᴀᴇᴛ ᴍɴᴇ ᴠ ᴢʜɪᴠᴜʏᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴇʀᴠʏᴊ ʀᴀᴢ ᴢᴀ ᴋᴜsᴏᴋ sᴀʟᴏ ᴠʏᴇʙᴀʟ ᴀ ᴏɴᴀ ʀᴀᴅᴏᴠᴀʟᴀsь ᴄʜᴛᴏ ᴍᴏᴢʜᴇᴛ ɴᴀᴋᴏʀᴍɪᴛь ᴛᴇʙʏᴀ ɴᴏ ᴋᴀᴋ ᴘᴏᴇʟ sʟɪᴢᴇɴь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴏᴘʀᴏʙᴜᴊ ᴇsᴄʜё ʀᴀs sᴋᴀᴢᴀᴛь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴘᴇʀᴇᴠᴇᴅᴀʟᴀ sᴛᴏʟьᴋᴏ ᴋʟёᴠʏʜ ʜᴜёᴠ ʏᴀ ᴛᴇʙʏᴀ ᴜᴇʙᴜ ʜᴜёᴍ ᴠᴇᴅь ᴏɴᴀ ɴᴀ ᴏᴛsᴏsᴇ ᴘʀɪᴢɴᴀᴠᴀʟsь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ sᴀᴍʏᴊ ʟᴜᴄʜsʜɪᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴏ ᴢᴠᴇʀsᴋɪ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴜ ᴏɴᴀ ᴠ sʜᴏᴋᴇ ɪ ᴅᴜᴍᴀᴇᴛ ᴄʜᴛᴏ ᴇᴛᴏ ʟʏᴜʙᴏᴠь ɴᴏ ʏᴀ ᴘʏᴛᴀʏᴜsь ᴠᴋᴀᴄʜᴀᴛь ᴇё sᴘᴇʀᴍᴀᴋᴏᴍ ᴄʜᴛᴏʙʏ ᴏɴᴀ ᴘᴇʀᴇᴅᴏᴢɴᴜʟᴀsь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴜ ɪ ᴄʜё ᴍʏ ᴛᴇᴘᴇʀь s ᴛᴠᴏɪᴍ ʙᴀᴛᴇᴊ ᴅʀᴜᴢьʏᴀ ᴘᴏsʟᴇ ᴛᴏɢᴏ ᴋᴀᴋ ʏᴀ ᴅᴀʟ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜᴋᴇ ɴᴀ ᴋʟʏᴋ ᴏɴ ᴜᴢɴᴀʟ ᴄʜᴛᴏ ᴏɴᴀ ᴢʜᴀʟᴋᴀʏᴀ sʜʟʏᴜʜᴀ ɪ sᴅᴀʟ ᴇё ᴍɴᴇ ᴠ ʀᴀʙsᴛᴠᴏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь sɴᴀᴄʜᴀʟᴀ ᴅᴜᴍᴀʟᴀ ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ɴᴇ ᴠʏᴢʏᴠᴀᴇᴛ ᴢᴀᴠɪsɪsᴍᴏsᴛ ɴᴏ s ᴋᴀᴢʜᴅʏᴍ ʀᴀᴢᴏᴍ sᴏsᴀʟᴀ ᴠsё ʙᴏʟьsʜᴇ ɪ ʙᴏʟьsʜᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ʀᴀᴢᴏɢʀᴇᴠ ᴛᴠᴏʏᴜ ᴍᴀᴍᴀsʜᴜ ᴘᴏᴇʙᴀʟ ᴀ ᴘᴏᴛᴏᴍ ᴛᴠᴏᴊ ʙᴀᴛʏᴀ ʀᴇsʜɪʟ ᴍɴᴇ ᴘᴏ ғᴀɴᴜ ᴏᴛsᴏsᴀᴛь ʏᴀ ᴛᴇᴘᴇʀь ᴅᴜᴍᴀʏᴜ ᴜ ᴠᴀs ᴠʀᴏᴢʜᴅёɴᴏᴇ ᴍᴏᴊ ʜᴜᴊ sᴏsᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍᴏᴊ ʜᴜᴊ ᴘʀᴏsʜёʟsʏᴀ ᴘᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴏᴛ ɴᴀᴄʜᴀʟᴀ ɪ ᴅᴏ ᴋᴏɴᴛsᴀ ɪ ᴛʏ ᴅᴏʟᴢʜᴇɴ ʙʏᴛь ʙʟᴀɢᴏᴅᴀʀᴇɴь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴏsᴛᴀᴠɪʟ ᴇё ᴏʙʟɪᴛᴏᴊ sᴘᴇʀᴍᴀᴋᴏᴍ ᴀ ɴᴇ ʀᴀᴢᴍᴀᴛᴀʟ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʀᴀᴢᴋʀᴇᴘᴏsᴛɪʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ɪ ᴛᴇᴘᴇʀь ᴏɴᴀ ɴᴇ ᴛᴀᴋ sɪʟьɴᴏ ʙᴏɪᴛьsʏᴀ sᴏsᴀᴛь ᴍᴏᴊ ʜᴜᴊ ɴᴀ ɢʟᴀᴢ ᴜ ᴛᴠᴏᴇɢᴏ ᴜsᴄʜᴇʀʙɴᴏɢᴏ ᴏᴛᴛsᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴋᴀɴᴜɴᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ɪ ᴍᴏɢᴜ sᴋᴀᴢᴀᴛь ᴏᴅɴᴏ ᴏɴᴀ ʙʏʟᴀ ɴᴀsᴛᴏʟьᴋᴏ ʀᴀᴢᴠʀᴀᴛɴᴏᴊ sʜʟʏᴜʜᴏᴊ ᴄʜᴛᴏ sᴏsᴀʟᴀ ᴍɴᴇ ʜᴜᴊ ᴅᴀᴢʜᴇ ɴᴀ ʟᴀɴᴄʜᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍᴏᴢʜᴇᴛ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴅʟʏᴀ ᴛᴇʙʏᴀ ɪ ʟᴜᴄʜsʜᴀʏᴀ ɴᴏ ᴍʏ ʙᴜᴅᴇᴍ ᴢɴᴀᴛь ᴠsᴇɢᴅᴀ ᴄʜᴛᴏ s ᴍᴏᴇɢᴏ ʜᴜʏᴀ ᴏɴᴀ ᴠʏᴜᴄʜɪʟᴀsь ᴋᴀᴢᴀᴛь ᴏʙʀᴀᴢᴏᴠᴀɴɴᴏᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴜ sᴄʜᴀs ʏᴀ ɴᴀᴄʜɴᴜ ᴋʀᴜᴛɪᴛь ᴛᴠᴏʏᴜ ᴍᴀᴍᴀsʜᴜ ɴᴀ ʜᴜᴇ ʙᴇᴢ ᴏsᴛᴀɴᴏᴠᴋɪ ᴀ ᴛʏ ᴘᴏʀᴏʙᴜᴊ ᴏsᴛᴀɴᴏᴠɪᴛь ᴇᴛᴜ ᴋᴀʀᴜsᴇʟь ᴢʜᴀʟᴋɪᴊ ᴛᴏʟьᴋᴏ sᴍᴏᴛʀɪ sᴀᴍ ɴᴇ ᴘᴏᴘᴀᴅɪ ɴᴀ ɴᴇё <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴇsᴛь ᴋᴏʀᴏɴᴋᴀ ᴋᴏɢᴅᴀ sᴏʙɪʀᴀʏᴜᴛьsʏᴀ ʀᴏᴅsᴛᴠᴇɴɪᴋɪ ɪ ᴘʀᴏsʏᴀᴛ ᴘᴏᴋᴀᴢᴀᴛь ᴄʜᴇɢᴏ ᴏɴᴀ ᴅᴏsᴛɪɢʟᴀ ᴏɴᴀ ᴢᴏᴠёᴛ ᴍᴇɴʏᴀ ɪ sᴏsёᴛ ᴍᴏᴊ ʜᴜᴊ ɪ ᴠsᴇ ᴀᴘʟᴀᴅɪʀᴜʏᴜᴛ ᴘʀɪᴋɪɴь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴘᴇʀᴇᴠᴀʟᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ᴏɴᴀ ᴅᴜᴍᴀʟᴀ ᴄʜᴛᴏ ᴘʀᴏsᴛᴏ ᴏᴛᴅᴏʜɴёᴛ ɴᴏ ᴍᴏᴊ ʜᴜᴊ ᴅᴀᴢʜᴇ ɴᴇ ᴏsᴛᴀᴠɪʟ ᴇᴊ sʜᴀɴsᴏᴠ ɴᴀ ᴠʏᴢʜɪᴠᴀɴɪʏᴀ ᴢᴀᴛᴏ ᴛᴇᴘᴇʀь ᴏɴᴀ ɢʀᴀɴᴛ ᴍᴀsᴛᴇʀ ᴘᴏ sᴏsᴀɴɪʏᴜ ᴍᴏᴇɢᴏ ʜᴜʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛᴜsʜᴋᴀ ɴᴇ ᴛᴀᴋ ᴄʜᴀsᴛᴏ sᴛᴀʟᴏ sᴏsᴀᴛь ᴍɴᴇ ʜᴜᴊ ʏᴀ ʀᴇsʜɪʟ ʀᴀᴢᴏʙʀᴀᴛьsʏᴀ ᴠ ᴄʜёᴍ ᴅᴇʟᴏ ᴏᴋᴀᴢʏᴠᴀᴇᴛьsʏᴀ ᴛᴠᴏᴊ ʙᴀᴛʏᴀ ᴘᴏᴘʀᴏsɪʟ ᴄʜᴛᴏʙ ᴏɴᴀ sᴏsᴀʟᴀ ᴍɴᴇ ʀᴇᴢʜᴇ ʏᴀ ᴋᴀᴋ ᴜᴇʙᴀʟ ᴇɢᴏ ʜᴜёᴍ ᴘᴏsʟᴇ ᴄʜᴇɢᴏ ᴏɴ ᴘᴇʀᴇᴅᴜᴍᴀʟ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ʀʏɴᴋᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴢᴀ ᴘʀɪʟᴀᴠᴋᴏᴍ ᴀ ᴢɴᴀᴇsʜь ᴋᴀᴋ ᴠsё ɴᴀᴄʜᴀʟᴏsь ᴏɴᴀ ʀᴇsʜɪʟᴀ ᴘʀᴏᴅᴀᴛь ᴍɴᴇ ᴏɢᴜʀᴛsʏ ᴋᴏᴛᴏʀʏᴇ sᴏᴠᴀʟᴀ ᴠ sᴠᴏʏᴜ sᴘɪᴅᴏᴢɴᴜʏᴜ ᴘʀᴏsᴄʜᴇʟɪɴᴜ ᴘʀɪᴅёᴛьsʏᴀ ᴇsᴄʜё ᴏᴛʜᴜʏᴀʀɪᴛь ᴇё <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴠᴏᴢᴠʏsʜᴇɴɪɪ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ᴏɴᴀ ʀᴇsʜɪʟᴀ ᴘᴏʟʏᴜʙᴏᴠᴀᴛьsʏᴀ ᴠɪᴅᴀᴍ ᴘʀɪʀᴏᴅʏ ɴᴏ ᴍᴏᴊ ʙʏʟ ɴᴀsᴛᴏʟьᴋᴏ ʀᴇᴢᴠʏᴊ ᴄʜᴛᴏ ᴇᴊ ᴘʀɪsʜʟᴏsь ʟʏᴜʙᴏᴠᴀᴛьsʏᴀ ᴠɪᴅᴏᴍ ᴍᴏᴇɢᴏ ʜᴜʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ʀʏʙᴀʟᴋᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴏᴋᴀ ᴛᴠᴏᴊ ʙᴀᴛʏᴀ ɴᴀsᴀᴢʜɪᴠᴀʟ ᴄʜᴇʀᴠʏᴀᴋᴏᴠ ɴᴀ ᴜᴅᴏᴄʜᴋᴜ ɪ ᴘʏᴛᴀʟsʏᴀ ᴘᴏᴊᴍᴀᴛь ʀʏʙᴜ ʏᴀ ᴜᴢʜᴇ ᴠᴏ ᴠsʏᴜ ᴅᴏʙɪᴠᴀʟ sᴠᴏɪᴍ ʜᴜёᴍ ᴛᴠᴏʏᴜ sʜᴀᴋᴀʟьɴᴜʏᴜ ᴍᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʙᴇᴢ ᴠʏʜᴏᴅɴʏʜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴏᴋᴀ ɴᴇ ᴘᴏɴʏᴀʟ ᴄʜᴛᴏ ɴᴀᴅᴏ ᴄʜᴛᴏ ᴛᴏ ᴍᴇɴʏᴀᴛь ᴘᴏᴢᴠᴀʟ ᴛᴠᴏᴇɢᴏ ʙᴀᴛʏᴜ ɪ ᴍʏ ᴠᴍᴇsᴛᴇ s ɴɪᴍ ʀᴇsʜɪʟɪ ᴠʏᴇʙᴀᴛь ᴛʏᴀ ᴘᴏᴍɴɪsʜь ɴᴏʀᴍ ᴛᴏɢᴅᴀ ᴘᴏʟᴜᴄʜɪʟᴏsь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴋɪᴅᴀᴊsʏᴀ ᴛᴀᴋ ɴᴀ ᴍᴏᴊ ʜᴜᴊ ᴠᴇᴅь ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ɴᴇ ᴠʏᴠᴇᴢɪsʜь ᴇɢᴏ ʟᴜᴄʜsʜᴇ ᴘᴏᴢᴏᴠɪ sᴠᴏʏᴜ ᴍᴀᴛь ᴜ ɴᴇё ɪ ᴛᴏ ʙᴏʟьsʜᴇ sʜᴀɴsᴏᴠ ᴇɢᴏ ᴏᴅᴀʟᴇᴛь ᴄʜᴇᴍ ᴜ ᴛᴇʙʏᴀ ᴢʜᴀʟᴋᴀʏᴀ ᴍᴏɴᴀsʜᴋᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴅᴀᴢʜᴇ ɴᴀᴋᴜʀᴇɴʏᴍ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴏɴᴀ ᴅᴜᴍᴀʟᴀ ᴄʜᴛᴏ ʏᴀ ᴘʀᴏsᴛᴏ ʀᴀᴅ ᴇё ᴠɪᴅᴇᴛь ɴᴏ ᴋᴏɢᴅᴀ ᴍᴇɴʏᴀ ᴋʀʏʟᴏ ʏᴀ ᴘʀᴇᴅsᴛᴀᴠʟʏᴀʟ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇ sᴘɪᴅᴏᴢɴᴀʏᴀ ɪ ᴍɴᴇ sᴛᴀɴᴏᴠɪʟᴀsь ʟᴇɢᴄʜᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ʀᴇsʜɪʟᴀ ᴢᴀsɴʏᴀᴛь ᴋᴀᴋ ʏᴀ ᴇё ᴇʙᴜ ᴘᴏᴛᴏᴍ sᴋɪɴᴜʟᴀ ᴅʀᴜᴢьʏᴀᴍ ᴏɴɪ sᴍᴏᴛʀᴇʟɪ ᴠsᴇ ᴠɪᴅᴏsʏ ɪ ᴘᴏᴛᴏᴍ ʀᴇsʜɪʟɪ ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ɴᴀᴅᴏ ᴘɪᴀʀɪᴛь ᴠ ᴛᴠᴏᴇᴊ ɢʟᴏᴛᴋᴇ ᴇᴢ ᴇᴢ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴋᴏɢᴅᴀ ʏᴀ ᴜᴍɪʀᴀʟ ɴᴀ ᴅᴠɪᴢʜᴇ ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴅᴇʟᴀʟᴀ ᴍɴᴇ ɢᴏʀʟᴏᴠᴏᴊ ᴍɪɴьᴇᴛ ɪ ᴍɴᴇ sᴛᴀʟᴏ ᴛᴀᴋ ʟᴇɢᴄʜᴇ ᴄʜᴛᴏ ʏᴀ ɴᴀᴄʜᴀʟ ᴠᴏᴢʀᴏᴢʜᴅᴀᴛьsʏᴀ ᴏsᴍᴏᴛʀᴇʟsʏᴀ ᴠᴏᴋʀᴜɢ ᴀ ᴏᴋᴀᴢᴀʟsʏᴀ ɴᴀ ʀᴇᴊᴠᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴠᴋᴀᴄʜᴀʟ ᴛᴠᴏᴇɢᴏ ᴏᴛᴛsᴀ ʜᴜёᴍ ɪ ᴍᴏɢᴜ ᴅᴀᴢʜᴇ s ᴄʜɪsᴛᴏᴊ sᴏᴠᴇsᴛьʏᴜ sᴋᴀᴢᴀᴛь ᴄʜᴛᴏ ᴛᴠᴏᴊ ᴏᴛᴇᴛs ᴋᴀᴋ ᴍᴏɢ ᴘʏᴛᴀʟsʏᴀ ᴍɴᴇ ᴏᴛsᴏsᴀᴛь ɴᴏ ᴏɴ ᴘᴏʟᴜᴄʜɪʟ ᴍɴᴏɢᴏᴄʜɪsʟᴇɴɴʏᴊ ᴜʀᴏɴ ᴏᴛ ᴍᴏᴇɢᴏ ʜᴜʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴋᴏɢᴅᴀ ʏᴀ sᴇʟ ᴠ ᴛʏᴜʀьᴍᴜ ᴛᴠᴏʏᴀ ᴍᴀᴛь ʙᴇɢᴀʟᴀ ᴋᴏ ᴍɴᴇ ɴᴀ ᴋɪᴄʜᴜ ɪ ᴏᴛsᴀsʏᴠᴀʟᴀ ᴋᴀᴋ ʙᴇsʜᴇɴᴀʏᴀ ʏᴀ ɴᴀᴄʜᴀʟ ᴋᴏʀᴍɪᴛь ᴇё ʟᴇsᴄʜᴀᴍɪ ᴘᴏᴛᴏᴍᴜ ᴄʜᴛᴏ ᴋᴀᴋ ᴏɴᴀ ᴠᴏʙsᴄʜᴇ ᴢᴀʙʀᴀʟᴀsь ᴠ ᴋᴀᴍᴇʀᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴋᴏɢᴅᴀ ɴᴇ ᴘᴏᴊᴍᴜ ᴏᴅɴᴏɢᴏ ᴢᴀᴄʜᴇᴍ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴛᴀᴋ ᴏʙɪʟьɴᴏ sᴏsёᴛ ɪ ᴋ ᴄʜᴇᴍᴜ ᴏɴᴀ sᴛʀᴇᴍɪᴛьsʏᴀ ᴍᴏᴢʜᴇᴛ ᴜ ɴᴇё ᴇsᴛь ᴋᴏɴᴇᴄʜɴᴀʏᴀ ᴛsᴇʟь ɪ ʏᴀ ᴢɴᴀʏᴜ ᴋᴀᴋᴀʏᴀ ʙʏᴛь sᴀᴍᴏᴊ ᴠᴇʀɴᴏᴊ ᴍᴏᴇɢᴏ ʜᴜʏᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʀᴀsᴋᴏʀᴍɪʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ᴄʜᴛᴏ ᴏɴᴀ ᴛᴇᴘᴇʀь ʏᴀᴠʟʏᴀᴛьsʏᴀ ᴍᴇsᴛɴʏᴍ ʙᴏssᴏᴍ ɪ ᴇᴅɪɴsᴛᴠᴇɴʏᴍ ᴋᴛᴏ ᴇё ᴍᴏᴢʜᴇᴛ ᴋʀʏsʜᴏᴠᴀᴛь ᴇё ɴᴀ ᴅᴀɴɴʏᴊ ᴍᴏᴍᴇɴᴛ ᴇᴛᴏ ᴍᴊ ʜᴜᴊ ᴠᴇᴅь ᴏɴᴀ ᴠsᴇɢᴅᴀ sᴛᴀᴠɪʟ ᴢᴀ ɴᴇɢᴏ sᴠᴇᴄʜᴋɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴋᴏᴍᴜ ɴᴇ sᴋᴀᴢʜᴜ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴢʜᴇ ɴᴀʏᴀʀɪᴠᴀᴇᴛ ᴍᴏᴊ ʜᴜᴊ ᴘᴏ 100 ʀᴀᴢᴜ ᴠᴇᴅь ᴏɴᴀ ᴇᴛᴏ ᴅᴇʟᴀᴇᴛ s ᴄʜɪsᴛᴏᴊ sᴏᴠᴇsᴛьʏᴜ ɪ ᴅᴜᴍᴀᴇᴛ ᴄʜᴛᴏ ᴇsʟɪ sᴏsᴀᴛь ᴍᴏᴊ ʜᴜᴊ ᴛᴀᴋ ᴄʜᴀsᴛᴏ ᴏɴᴀ ᴘᴏᴘᴀᴅёᴛ ᴠ ʀᴀᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴛᴀᴋᴀʏᴀ ʙᴇsᴘᴏɴᴛᴏᴠᴀʏᴀ ᴄʜᴛᴏ ᴘʀᴇᴢʜᴅᴇ ᴄʜᴇᴍ ᴇё ᴠʏᴇʙᴀᴛь ʏᴀ ᴅᴀʏᴜ ɴᴀ ʀᴏᴛᴀɴ ᴛᴠᴏᴇᴍᴜ ᴏᴛᴛsᴜ ᴠᴇᴅь ᴛᴀᴋ ᴍᴏᴊ ʜᴜᴊ ᴜᴢʜᴇ ɢᴏᴛᴏᴠ ᴋ sᴛʀёᴍɴᴏᴊ ɢʟᴏᴛᴋᴇ ᴛᴠᴏᴇᴊ ᴇʙᴜᴄʜᴇᴊ ᴍᴀᴛᴜʜᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘᴏᴍɪɴᴋɪ sᴠᴏɪᴍ ʜᴜёᴍ ᴏʀɢᴀɴɪᴢᴏᴠᴀʟ ɪ ᴠsᴇ ʀᴏᴅsᴛᴠᴇɴɪᴋɪ ʙʏʟɪ ʀᴀᴅʏ ᴠᴇᴅь ᴍᴏᴊ ʜᴜᴊ ᴇᴛᴏ sᴀᴍʏᴊ ᴘᴏᴄʜёᴛɴʏᴊ ɢᴏsᴛь ɴᴀ ɪʜ ᴘᴏᴍɪɴᴋᴀʜ ᴇᴢ ᴇᴢ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴏsʟᴇ ᴛᴏɢᴏ ᴋᴀᴋ ᴛᴠᴏʏᴀ ᴍᴀᴛь ʀᴇsʜɪʟᴀ ᴢᴀʀᴇᴊᴅɪᴛь ᴍᴏᴊ ʜᴜᴊ ʏᴀ ᴏᴛʙɪʟ ᴇё ʀᴇᴊᴅ ɴᴏ ʀᴇsʜɪʟ ɴᴀᴋᴀᴢᴛь ᴢᴀ sᴛᴏʟь ɴɪᴢᴋᴏᴇ ᴅɪʏᴀɴɪʏᴀ ᴛᴇᴘᴇʀь ᴏɴᴀ ʟɪᴢʜᴇᴛ ᴍᴏᴇᴍᴜ ᴋᴇɴᴛᴜ ᴘʏᴀᴛᴋɪ ᴏʀᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴘᴀʟᴜʙᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ɴᴇ ᴏᴅɪɴ ᴍᴏʀʏᴀᴋ ᴀ ᴠsё ᴘᴏᴛᴏᴍᴜ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇ ᴍᴏᴢʜᴇᴛ ᴢʜɪᴛь ʙᴇᴢ ᴄʜᴜᴢʜɪᴠ ʜᴜёᴠ ɪ ᴅᴀᴢʜ ʙᴜᴅᴜᴄʜɪ ᴠ ᴢᴀᴘᴇʀᴛɪ ᴏɴᴀ ɴᴀᴊᴅёᴛ ᴋᴀᴋᴏᴊ ɴɪʙᴜᴅь ʜᴜᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴍᴏɢᴜ ᴘᴏᴠᴇʀɪᴛь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴛᴀᴋ ᴘʀᴏsᴛᴏ ᴘᴏᴅᴛᴀʟᴀsь ɴᴀ ᴘʀᴏᴠᴏᴋᴀᴛsɪʏᴜ ᴋɪɴᴜᴛᴜʏᴜ ᴍᴏɪᴍ ʜᴜёᴍ ᴄʜᴛᴏ ᴛᴇᴘᴇʀь ᴅᴇʟᴀᴛь ᴅᴀᴠᴀᴊ ᴘᴏ ɴᴀᴋᴀᴛᴀɴᴏᴊ ᴘʀᴏsᴛᴏ ʀᴀᴢᴏʀᴠёᴍ ᴇᴊ ᴘᴇʀᴅᴀᴋ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴀ ᴅᴀᴢʜᴇ ʀᴀᴜɴᴅᴀ ᴘʀᴏᴛɪᴠ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ɴᴇ ᴠʏsᴛᴏʏᴀʟᴀ ᴄʜᴛᴏ ᴛᴇᴘᴇʀь ɢᴠᴏᴏʀɪᴛь ᴏ ᴘᴏʟɴᴏᴛsᴇɴᴏᴍ ʙᴏᴇ ᴘᴜsᴛь ᴛʀᴇɴɪʀᴜᴇᴛьsʏᴀ ᴀ ᴘᴏᴋᴀ ᴏɴᴀ ᴇᴛᴏ ᴅᴇʟᴀᴛь ᴅᴀᴠᴀᴊ sᴏsɪ ʀᴀᴋᴀʟ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴛᴀʀᴢᴀɴᴋᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴋᴏɢᴅᴀ ᴏɴᴀ ᴘʏᴛᴀʟᴀsь sᴘʀʏɢɴᴜᴛь s ɴᴇё ʏᴀ ᴘᴏᴅʜᴠᴀᴛɪʟ ᴇё ʜᴜёᴍ ɪ ᴜᴇʙᴀʟ ᴏʙ ᴢᴇᴍʟʏᴜ ᴘᴜsᴛь ᴛᴏʟьᴋᴏ ᴇsᴄʜё ʀᴀᴢ ᴘᴏᴘʀᴏʙᴜᴇᴛ ᴠʏᴋɪɴᴜᴛь ᴄʜᴛᴏ ɴɪʙᴜᴅь ᴛᴀᴋᴏᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴍᴏɢᴜ ɴᴇ ᴄʜᴇɢᴏ sᴋᴀᴢᴀᴛь ᴘʟᴏʜᴏɢᴏ ɴᴀsᴄʜёᴛ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴜʟьᴋᴇ ɴᴏ ᴘʀɪᴅёᴛьsʏᴀ ʀᴀsᴋʀʏᴛь ᴛᴇʙᴇ ᴛᴀᴊɴᴜ ᴏᴛsᴏs ᴛʏ ᴍᴇʀᴢᴋɪᴊ ᴄʜᴛᴏ ᴏɴᴀ ʀᴀᴅɪ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ᴛᴠᴏᴊ ᴋᴏᴍᴘ ᴢᴀʟᴏᴢʜɪʟᴀ ᴏʀᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ sᴋᴀᴄʜᴋᴀʜ ᴠsᴇ ʙʏʟɪ ɴᴀ ᴋᴏɴʏᴀʜ ᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴇᴅɪɴsᴛᴠᴇɴᴀʏᴀ ᴜᴄʜᴀsᴛɴɪᴛsᴀ ᴋᴏᴛᴏʀᴀʏᴀ ʀᴇsʜɪʟᴀ ᴘʀᴏsᴋᴀᴛᴀᴛь ɴᴀ ᴍᴏёᴍ ʜᴜᴇ ɴᴇ ᴄʜё ᴛᴀᴋ ᴘᴏʟᴜᴄʜɪʟᴏsь ᴋsᴛᴀᴛɪ ᴍᴏᴊ ʜᴜᴊ ᴠᴢʏᴀʟ ᴛᴀᴍ ᴘᴇʀᴠᴏᴇ ᴍᴇsᴛᴏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴋᴀᴢʜᴅʏᴊ ᴅᴇɴь ʜᴜёᴍ ᴠ ᴍᴀɢᴀᴢ ɢᴏɴʏᴀʏᴜ ᴠᴇᴅь ʏᴀ ᴛᴀᴋ ᴢᴀᴇʙᴀʟsʏᴀ ᴇᴊ ɴᴀ ʀᴏᴛᴀɴ ᴅᴏᴠᴀᴛь ᴄʜᴛᴏ ᴛᴇᴘᴇʀь ᴍᴏё ʀᴀᴢᴠʟᴇᴄʜᴇɴɪʏᴀ ᴇᴛᴏ ᴅᴇʟᴀᴛь ɪᴢ ɴᴇё sᴀᴍᴜʏᴜ ᴘᴏsʟᴜsʜɴᴜʏᴜ sʜʟʏᴜʜᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍᴏᴢʜᴇsʜь ɴᴇ ᴠᴇʀɪᴛь ɴᴏ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴇʀᴇʙᴀʟᴀ ᴘᴏʟ ɢᴏʀᴏᴅᴀ ɴᴏ ʏᴀ ᴇᴅɪɴsᴛᴠᴇɴʏᴊ ᴢᴀ ᴄʜᴇᴊ ʜᴜᴊ ᴏɴᴀ ʙᴜᴅᴇᴛ sᴛᴏʏᴀᴛь ᴅᴏ ᴋᴏɴᴛsᴀ ɪ ɴᴇ ᴋᴏɢᴅᴀ ɴᴇ sᴅᴀsᴛ ᴢᴀᴅɴɪʏᴜ ʀɪʟɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴍᴏᴊ ʜᴜᴊ ᴍᴇsᴛᴏ ᴍᴀsᴏᴢʜᴏʀᴀ ʀᴇsʜɪʟᴀ ɪsᴘᴏʟьᴢʏᴠᴀᴛь ɴᴏ ʏᴀ ɴᴇ ᴢɴᴀʏᴜ ᴇsᴛь ʟɪ ᴍᴀsᴀᴢʜᴏʀ ᴘɪᴢᴅʏ ᴠᴇᴅь ᴇᴅɪɴsᴛᴠᴇɴɴᴏᴇ ᴄʜᴛᴏ ᴏɴᴀ ᴅᴇʟᴀᴇᴛ ᴇᴛᴏ sᴜёᴛ ᴇɢᴏ ᴠ sᴠᴏё ɢɴᴇᴢᴅᴏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴅᴀᴢʜᴇ ɴᴀ ʀᴀʙᴏᴛᴇ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴋᴏɢᴅᴀ ᴠsᴇ ᴅᴇʟᴀʏᴜᴛ ᴘʟᴀɴᴏᴠʏᴊ ᴏᴄʜёᴛ ɪʟɪ ᴠʏʜᴏᴅʏᴀᴛ ᴘᴏᴋᴜʀɪᴛь ᴏɴᴀ ᴍɴᴇ ᴘᴏ sᴋᴀᴊᴘᴜ sᴏsёᴛ ᴇsʟɪ ʙʏʟᴏ ʙʏ ᴠᴏᴢᴍᴏᴢʜɴᴏ ɴᴇ ᴘʟᴀᴛɪᴛь ᴢᴀ ᴍᴏᴊ ʜᴜᴊ ᴏɴᴀ ʙʏ ɴᴇ ʀᴀʙᴏᴛᴀʟᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴛᴇʀᴇᴏᴛɪᴘɴᴏᴇ ᴍʏsʜʟᴇɴɪʏᴀ ᴏɴᴀ ᴅᴜᴍᴀᴇᴛ ᴄʜᴛᴏ ᴇsʟɪ ʏᴀ ᴇᴊ ɴᴇ ɴᴀᴠᴇʀɴᴜʟ ᴘᴏ ɢᴏʀʙᴜ ᴢᴀ ᴘʟᴏʜᴏᴊ ᴍɪɴьᴇᴛ ᴛᴏ ʙᴏʟьsʜᴇ ᴛᴀᴋ ᴅᴇʟᴀᴛь ɪ ɴᴇ ʙᴜᴅᴜ ᴋᴀᴋ ɴᴀ ᴏsʜɪʙᴀᴇᴛьsʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ʟɪɴɪʏᴜ ᴢʜɪᴢɴɪ ʜᴜёᴍ ᴏʙᴏʀᴠᴀʟ ᴛᴇᴘᴇʀь ᴇᴊ ᴘʀɪᴅёᴛьsʏᴀ ᴏᴛᴘʀᴀᴠʟʏᴀᴛьsʏᴀ ᴠ ᴍɪʀ ɪɴᴏᴊ ɴᴀ ᴢɴᴀʏᴀ ᴋᴀᴋᴀʏᴀ ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴀ sʜʟʏᴜʜᴀ ᴏɴᴀ ᴅᴀᴢʜᴇ ᴛᴀᴍ ᴘᴏᴘʀᴏsɪᴛ ᴍᴏᴊ ʜᴜᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍᴏᴊ ʜᴜᴊ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴢʜᴇ ɴᴀ ᴠᴇʀʜᴋᴜsʜᴋᴜ ᴢᴀᴋɪɴᴜʟ ᴛᴇᴘᴇʀь ᴏɴᴀ ᴏʙsᴄʜᴀᴇᴛьsʏᴀ s ɪɴᴛᴇʟᴇɢᴇɴᴛɴʏᴍɪ ʟʏᴜᴅьᴍɪ ɴᴏ ᴍʏ ᴛᴏ ᴠsᴇ ᴢɴᴀᴇᴍ ᴋᴀᴋ ᴍʏ s ᴘᴀᴛsᴀɴᴀᴍɪ ᴇё ʀᴏᴛᴀɴ ᴘᴏ ᴋʀᴜɢᴜ ᴘᴜsᴋᴀʟɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴏᴛʀɪᴛsᴀᴊ ᴛᴏɢᴏ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴅᴀʟᴀsь ᴍᴏᴇᴍᴜ ʜᴜʏᴜ ᴏɴᴀ ᴘʏᴛᴀʟᴀsь sᴏᴘʀᴏᴛɪᴠʟʏᴀᴛьsʏᴀ ɴᴏ ᴍᴏᴊ ʜᴜᴊ ᴏᴋᴀᴢᴀʟsʏᴀ sɪʟьɴᴇᴇ ᴅᴀᴢʜᴇ ᴛᴠᴏᴊ ᴏᴘᴜsᴄʜᴇɴʏᴊ ᴏᴛᴇᴛs s ɴɪᴍ ɴᴇ sᴍᴏɢ sᴘʀᴀᴠɪᴛьsʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍᴏᴢʜᴇᴛ ᴛʏ ᴍɴᴇ sᴋᴀᴢʜᴇsʜь ᴘᴏᴄʜᴇᴍᴜ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴇʙᴜᴄʜᴀʏᴀ ᴍᴏʟᴇᴋᴜʟᴀ ᴏᴘʏᴀᴛь ʀᴇsʜɪʟᴀ ᴠʏᴠᴇsɪᴛь ɴᴀ sᴛᴇɴᴅ ᴍᴏᴊ ʜᴜᴊ ᴏɴᴀ ᴜᴢʜᴇ ᴘʀᴏᴅᴀʟᴀsь ᴇᴍᴜ ᴘᴏʟɴᴏsᴛьʏᴜ ʀɪʟɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴢᴀʙʏᴠᴀᴊ ᴋᴛᴏ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʜᴜёᴍ ᴜᴇʙᴀʟ ɪ ᴠsё ᴇᴛᴏ ʙʏʟᴏ ᴠᴏ ʙʟᴀɢᴏ ᴠᴇᴅь ᴛᴇᴘᴇʀь ᴏɴᴀ sᴛᴀʟᴀ ᴜᴍɴᴇᴇ ɪ ᴍᴇsᴛᴏ ᴏᴛsᴏsᴀ ᴛᴠᴏᴇᴍᴜ ʙᴀᴛɪ ᴛᴇᴘᴇʀь ᴏɴᴀ ᴅᴇʟᴀᴇᴛ ᴇɢᴏ ᴍɴᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍᴏᴢʜᴇᴛ ᴛʏ sᴄʜᴀs ᴜᴘᴀᴅёsʜь ɴᴀ ᴋᴏʟᴇɴɪ ɪ ɴᴀᴄʜɴёsʜь ᴍɴᴇ sᴏsᴀᴛь ᴀ ᴛᴏ ʏᴀ ᴘᴏᴢᴏᴠᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ɪ ᴏɴᴀ ᴜᴢʜᴇ ɴᴇ sᴍᴏᴢʜᴇᴛ ᴏᴛᴏʀᴠᴀᴛьsʏᴀ ᴏᴛ ᴍᴏᴇɢᴏ ʜᴜʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴢʜᴇ ʜᴜёᴍ ᴛᴠᴏᴊ ᴘɪᴢᴅᴀᴋ ᴘᴏᴅᴠᴇsɪʟ ɴᴀ ʟʏᴜsᴛʀᴜ ᴛᴇᴘᴇʀь ᴛᴠᴏᴊ ʙᴀᴛʏᴀ ᴋᴏɢᴅᴀ ᴘʀᴏʜᴏᴅɪᴛ ʀᴀᴅᴜᴇᴛьsʏᴀ ᴄʜᴛᴏ ᴛᴇʙʏᴀ ᴠʏᴇʙᴀʟ ɴᴇ ᴋᴀᴋᴏᴊ ᴛᴏ ᴅᴏᴠʀᴏᴠʏᴊ ᴘᴀᴛsᴀɴ ᴀ ʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍᴏᴢʜᴇᴛ ᴛʏ ᴍᴏᴊ ʜᴜᴊ sʙᴀʟᴀɴsɪʀᴏᴠᴀɴɴᴏ ɴᴀᴄʜɴёsʜь sᴏsᴀᴛь ᴀ ᴛᴏ ᴄʜё ᴛʏ ᴋᴀᴋ ʟᴀʜ ᴢᴀ ᴏᴅɴᴜ sᴄʜёᴋᴜ ᴘᴜsᴋᴀᴇsʜь ᴅᴀᴠᴀᴊ ᴘʀᴇsᴛᴜᴘᴀᴊ ɪʟɪ ᴏᴘʏᴀᴛь ᴛᴠᴏᴊ ʙᴀᴛʏᴀ ᴘʀɪᴅёᴛ ɪ ᴏᴛsᴏsёᴛ ᴍɴᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏᴊ ʙᴀᴛʏᴀ ɴᴜʟёᴠᴋᴀ ɴᴇ ᴄʜᴇɢᴏ ɴᴇ ᴍᴏᴢʜᴇᴛ ʙᴇᴢ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ᴠᴇᴅь ᴏɴ ɢᴏᴠᴏʀɪᴛ ᴄʜᴛᴏ ᴇᴛᴏ ᴇɢᴏ sᴠᴇᴛʟʏᴊ ʟᴜᴄʜɪᴋ ᴠ ʙᴜsᴄʜᴜᴇᴇ ᴠᴏᴛ ᴇᴛᴏ ʏᴀ ᴇᴍᴜ ʜᴜёᴍ ᴍᴏᴢɢɪ ᴏᴛʙɪʟ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴠᴇʀь sᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴋᴏɢᴅᴀ ᴏɴᴀ ɢᴏᴠᴏʀɪᴛ ᴄʜᴛᴏ ʏᴀ ᴛᴇʙʏᴀ ɴᴇ ʀᴀᴢᴜ ɴᴇ ᴇʙᴀʟ ʏᴀ ᴛʏᴀ ᴇsᴄʜё s ʀᴏᴢʜᴅᴇɴɪʏᴀ ᴇʙᴀʟ ᴋʀᴇᴠᴇᴛᴋᴀ ᴇʙᴜᴄʜᴀʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴇsᴄʜё ᴏᴅɴᴏ sʟᴏᴠᴏ ᴘʀᴏ ᴛᴠᴏʏᴜ ᴍᴀᴛь ʏᴀ ᴛᴇʙʏᴀ ʜᴜёᴍ ʀᴀsᴛᴇʀᴢᴀʏᴜ ᴅᴜʀᴀ ᴛʏ ᴇʙᴀɴᴀʏᴀ ᴠᴇᴅь ᴛᴠᴏʏᴀ ᴍᴀᴛь ɪᴅᴇᴀʟьɴᴀʏᴀ sʜᴀʟᴏᴠᴀ ɴᴇ ᴏʙɪᴢʜᴀᴊ ᴇё <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴢɴᴀʟ ᴄʜᴛᴏ ʏᴀ ᴛʏᴀ ʜᴜёᴍ ᴋʀᴇsᴛɪʟ ᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴍᴜᴅʀɪʟᴀsь ᴅᴀᴢʜᴇ ᴠ ᴛᴀᴋᴏᴊ ᴏᴛᴠᴇᴛsᴛᴠᴇɴʏᴊ ᴍᴏᴍᴇɴᴛ ᴏᴛsᴏsᴀᴛь sᴠʏᴀsᴄʜᴇɴɪᴋᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴛᴇʙʏᴀ ᴅᴀᴢʜᴇ ᴠ ᴅᴇᴛsᴋᴏᴍ sᴀᴅᴜ ᴇʙᴀʟ ᴋᴏɢᴅᴀ ᴛʏ ᴅʀᴀʟsʏᴀ ᴢᴀ ᴍᴀsʜɪɴᴋᴇ ɪ ᴘʟᴀᴋᴀʟ ᴄʜᴛᴏ ᴛᴇʙʏᴀ ɴᴇ ᴅᴀʟɪ ᴍᴀsʜɪɴᴋᴜ ᴋᴛᴏ ᴛᴇ ʜᴜᴊ ᴏᴛ ᴏʙɪᴅʏ sᴜᴠᴀʟ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ sᴛᴀʟ ᴘᴏʜᴏᴢʜɪᴍ ɴᴀ sᴠᴏʏᴜ ᴍᴀᴛь ᴛᴇʙᴇ ᴜᴢʜᴇ ᴛᴏᴢʜᴇ ɴᴇ ɴᴜᴢʜɴᴀ ᴘʀɪᴄʜɪɴᴀ ᴄʜᴛᴏʙʏ ᴏᴛsᴏsᴀᴛь ᴍɴᴇ ʜᴜᴊ ɴᴜ ᴇsʟɪ ᴛᴀᴋ ᴛᴏ ᴛʏ ᴛᴏᴢʜᴇ ᴅᴏsᴛᴏᴇɴ ᴢᴠᴀɴɪʏᴀ ᴘᴅᴢᴏʙᴏʀɴᴏᴊ sʜʟʏᴜʜɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴍᴏɢᴜ ᴘᴏᴠᴇʀɪᴛь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴏᴘʏᴀᴛь ᴠᴢʏᴀʟᴀsь ᴢᴀ sᴛᴀʀᴏᴇ ɪ ᴘʏᴛᴀᴇᴛьsʏᴀ ᴠʏsʟᴇᴅɪᴛь ᴍᴏᴊ ʜᴜᴊ ɴᴜ ᴇsʟɪ ᴏɴᴀ ᴘᴏᴘᴀᴅёᴛьsʏᴀ ᴍɴᴇ ɴᴀ ɢʟᴀᴢᴀ ʏᴀ ᴇё ʜᴜёᴍ ᴠ ᴀʀᴀʜɴɢᴇʟьsᴋ sʜᴠʏʀɴᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴅᴜᴍᴀᴊ ɴᴇ ᴄʜᴇɢᴏ ᴘʟᴏʜᴏɢᴏ ɴᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴋᴏsᴍᴏɴᴀᴠᴛ ʏᴀ ᴛᴇʙᴇ ɴᴇ ᴠʀᴜ ɴᴇ ᴠ ᴋᴏᴇᴍ sʟᴜᴄʜᴀᴇ ᴀ ᴢɴᴀᴇsʜь ɴᴀ ᴄʜёᴍ ᴘʀᴏʜᴏᴅɪʟ ᴇё ᴘᴇʀᴠʏᴊ ᴘᴏʟёᴛ ɴᴀ ᴍᴏёᴍ ʜᴜᴇ ᴏʀᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍᴏᴢʜᴇᴛ ʏᴀ ᴛᴇʙʏᴀ ᴏɢᴏʀᴄʜᴜ ɴᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛᴜsʜᴋᴀ sᴄʜᴀ ᴍɴᴇ ʜᴜᴊ sᴏsёᴛ ɪ ᴄʜᴛᴏ ᴛᴏ ʙᴏʀᴍᴏᴄʜᴇᴛ ᴇᴛᴏ sʜᴀʟᴏᴠᴀ ᴍᴇɴʏᴀ ᴛᴀᴋ ᴢᴀᴇʙᴀʟᴀ ʏᴀ sᴄʜᴀ ᴠsᴘᴏʀʏᴜ ᴇё ʜᴜёᴍ ᴘʀɪʜᴏᴅɪ ɪ ᴢᴀʙɪʀᴀᴊ ᴇё <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴠsё ɴᴇ ᴛᴀᴋ ᴘʀᴏsᴛᴏ ᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴇsᴛь sᴛɪᴍᴜʟ sᴏsᴀᴛь ᴍɴᴇ ʜᴜᴊ ᴠᴇᴅь ʏᴀ sᴋᴀᴢᴀʟ ᴇsʟɪ ᴏɴᴀ ᴏsᴛᴀɴᴏᴠɪᴛьsʏᴀ ᴛᴏ ᴛᴠᴏᴊ ɢʀʏᴀᴢɴʏᴊ ʙᴀᴛʏᴀ ᴜᴍʀёᴛ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀ ᴍᴏёᴍ ʜᴜᴇ ʜɪᴘ ʜᴏᴘ ᴛᴀɴᴛsᴇᴠᴀʟᴀ ɪ sᴜᴅьʏᴀ ᴅᴀʟɪ ᴇᴊ ᴘᴇʀᴠᴏᴇ ᴍᴇsᴛᴏ ɴᴏ ɴᴇ ᴢᴀ ᴇᴛᴏ ᴀ ᴢᴀ ᴠᴇʟɪᴋᴏʟᴇᴘɴʏᴊ ᴏᴛsᴏs ᴠ ᴋᴏɴᴛsᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʜᴏᴄʜᴇsʜь sᴘᴀsᴛɪ sᴠᴏʏᴜ ᴍᴀᴛь ɪᴢ ʀᴀʙsᴛᴀᴠᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ᴘʀɪɴᴇsɪ ᴇᴍᴜ ᴘᴏᴅɴᴏsʜᴇɴɪʏᴀ ᴛᴏɢᴅᴀ ᴍᴏᴢʜᴇᴛ ʙʏᴛь ᴍᴏᴊ ʜᴜᴊ ᴘʀᴏsᴛɪᴛ ᴛᴠᴏʏᴜ ᴍᴀᴛᴜʜᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴢʜᴇ ᴏᴛᴢʜɪʟᴀ sᴠᴏё ɴᴀ ᴍᴏёᴍ ʜᴜʏᴜ ᴋᴀᴋ ɪ ᴛᴠᴏᴊ ᴏᴛᴇᴛs ᴘʀɪsʜʟᴏ ᴛᴠᴏё ᴠʀᴇᴍʏᴀ ᴘʀʏɢᴀᴊ ɴᴀ ʜᴜᴊ ɪ ᴘᴏᴇʜᴀʟɪ ᴅᴜʀᴇɴь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴍᴇsᴛᴏ ᴛᴀʙʟᴇᴛᴏᴋ ᴏᴛ ɢᴏʟᴏᴠʏ ɢʟᴏᴛᴀᴇᴛ ᴍᴏᴊ ʜᴜᴊ sᴋᴀᴢʜᴇsʜь ᴄʜᴇᴍ ᴇᴛᴏ ᴘᴏᴍᴏᴢʜᴇᴛ sᴘʀᴏsɪ ᴜ ᴇᴛᴏᴊ ᴇʙᴜʏᴀᴇᴊ ᴅᴜʀʏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴘʏᴛᴀʟᴀsь ᴠʏᴠᴇᴢᴛɪ ᴍᴏᴊ ʜᴜᴊ ᴘᴏ ᴘᴏɴʏᴀᴛɪʏᴀᴍ ᴄʜᴛᴏʙʏ ᴏɴ ʙᴏʟьsʜᴇ ᴇё ɴᴇ ᴛʀᴏɢᴀʟ ɴᴏ ᴍᴏᴊ ʜᴜᴊ ɴᴇ sᴛᴀʟ ᴇё sʟᴜsʜᴀᴛь ɪ ʀᴀsёᴋ ᴇᴊ ʙʀᴏᴠь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍᴏᴢʜᴇᴛ ᴛʏ ʙᴜᴅᴇsʜь ᴅᴜᴍᴀᴛь ᴄʜᴛᴏ ʏᴀ ᴘʟᴏʜᴏᴊ ɴᴏ ʏᴀ ᴅᴏᴋᴀᴢʜᴜ ᴏʙʀᴀᴛɴᴏᴇ ᴇsʟɪ ʙʏ ʏᴀ ɴᴇ ᴇʙᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇё ʙʏ ᴇʙᴀʟ ᴠᴇsь ɢᴏʀᴏᴅ ɪ ᴠsᴇ ʙʏ ᴢɴᴀʟɪ ᴄʜᴛᴏ ᴏɴᴀ sʜᴀʟᴏᴠᴀ ᴀ ᴛᴀᴋ ᴢɴᴀᴇᴍ ᴛᴏʟьᴋᴏ ᴍʏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍᴏɢᴜ ᴏʙʀᴀᴛɪᴛьsʏᴀ s ᴘʀᴏsьʙᴏᴊ ᴋ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴛʏ sᴘʀᴏsɪsʜь ᴋᴀᴋᴏᴊ ɴᴜ ᴛʏ ᴄʜё ʟᴀʜ ɴᴇ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏʙʏ ᴏɴᴀ ᴏᴛsᴀsᴀʟᴀ ᴍɴᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴋᴀᴋᴏᴊ ᴇʙᴀʟ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴋᴏɢᴅᴀ ᴜ ᴍᴇɴʏᴀ ʙʏʟᴀ ᴛᴇᴍᴘᴇʀᴀᴛᴜʀᴀ ʀᴏᴛ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴢᴀᴍᴇɴʏᴀʟ ᴍɴᴇ ɢʀᴀᴅᴜsɴɪᴋ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ sᴘɪɴᴇ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀᴋᴏʟᴏʟᴀ ᴍᴏᴊ ʜᴜᴊ ɪ ᴛᴇᴘᴇʀь ʜᴠᴀsᴛᴀᴇᴛьsʏᴀ ᴠsᴇᴍ ᴄʜᴛᴏ ᴜ ɴɪʜ ɴᴇᴛ ʙᴏʟᴇᴇ ᴏʜᴜᴇɴᴇᴇ ᴛᴀᴛᴜɪʀᴏᴠᴋᴏᴊ ᴄʜᴇᴍ ᴜ ɴᴇё <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴠ ᴢɪᴍᴜ ᴇʙᴀʟ ᴛᴏɢᴅᴀ ᴋᴀᴋ ʀᴀᴢ ʙʏʟ ᴢʜᴇsᴛᴏᴋᴀʏᴀ ᴢɪᴍᴀ ɪ ᴍɴᴇ ᴘʀɪsʜʟᴏsь ᴇʙᴀᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴄʜᴛᴏʙʏ sᴏɢʀᴇᴛьsʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴍᴀsʜɪɴᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴠsᴇ sᴋᴀᴢʜᴜᴛ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴇʙᴜᴄʜᴀʏᴀ sʜᴀʟᴏᴠᴀ ᴋᴏᴛᴏʀᴀʏᴀ ᴠᴇᴅᴇᴛьsʏᴀ ɴᴀ ᴛᴀᴄʜᴋɪ ɴᴏ ᴏɴɪ ᴏsʜɪʙᴀʏᴜᴛьsʏᴀ ᴏɴᴀ ᴠᴇᴅёᴛьsʏᴀ ɴᴀ ᴍᴏᴊ ʜᴜᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴠɪʟᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ɪ ᴍᴏᴢʜɴᴏ sᴋᴀᴢᴀᴛь ᴄʜᴛᴏ ᴍʏ ᴠᴏʀᴠᴀʟɪsь ᴛᴜᴅᴀ ɴᴇ ᴢᴀᴋᴏɴɴᴏ ᴀ ᴢɴᴀᴇsʜь ᴘᴏᴄʜᴇᴍᴜ ᴘᴏᴛᴏᴍᴜ ᴄʜᴛᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴢᴀʜᴏᴛᴇʟᴏsь ᴘᴏsᴏsᴀᴛь ᴍᴏᴊ ʜᴜᴊ ᴇᴋsᴛʀᴇᴍᴀʟьɴᴏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴢɴᴀᴇsʜь ᴘᴏᴄʜᴇᴍᴜ ᴍᴇɴʏᴀ ᴠsᴇ ᴘᴀᴛsᴀɴʏ ɴᴀᴢʏᴠᴀʟɪ ʜᴜʟɪɢᴀɴᴏᴍ ᴘᴏᴛᴏᴍᴜ ᴄʜᴛᴏ ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛᴜʜᴀ ᴘᴏsʟᴇ 8 ᴇʙᴀʟ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍʏ ʟʏᴜʙɪʟɪ sᴏʙɪʀᴀᴛьsʏᴀ s ᴘᴀᴛsᴀɴᴀᴍɪ ɪ ɢᴏᴠᴏʀɪᴛь ᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ɴᴏ ʀᴀᴢɢᴏᴠᴏʀ ᴏʙʏᴄʜɴᴏ ᴢᴀᴋᴀɴᴄʜɪᴠᴀʟsʏᴀ ᴏᴅɴɪᴍ ᴍʏ ᴢᴠᴏɴɪʟɪ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴄʜᴛᴏʙʏ ᴏɴᴀ ᴏᴛsᴀsᴀʟᴀ ɴᴀᴍ ʜᴜᴊ ɴᴇ ʀᴀᴢᴜ ɴᴇ ᴏᴛᴋᴀᴢʏᴠᴀʟᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴠ ᴍᴜsᴏʀsᴋᴏᴍ ᴜᴄʜᴀsᴛᴋᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ᴋᴏɢᴅᴀ ᴇё ᴢᴀᴋʀʏʟɪ ᴢᴀ ᴅᴇʀᴢᴋᴏᴇ sᴏsᴀɴɪʏᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ʏᴀ ᴘʀᴏʙʀᴀʟsʏᴀ ᴛᴜᴅᴀ ɪ ᴠʏᴇʙᴀʟ ᴇё ᴘʀᴀᴠɪʟьɴᴏ ᴢʜᴇ ʜᴇʜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴅᴇɴь ᴏᴛᴋʀʏᴛʏʜ ᴅᴠᴇʀᴇᴊ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ᴋᴏɢᴅᴀ ᴠsᴇ sᴏʙɪʀᴀʟɪsь ɪ ʙʏʟɪ sᴏsʀᴇɢᴏᴛᴏᴄʜᴇɴʏ ʏᴀ ᴛᴏᴢʜᴇ ʙʏʟ ᴠ sᴠᴏёᴍ ᴘᴏɴɪᴍᴀɴɪʏᴀ ɴᴀᴠᴏsᴛʀёɴ ɴᴏ ʏᴀ ᴇʙᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴢᴀᴘʀᴀᴠᴋᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴏᴋᴀ ᴠsᴇ ᴢᴀᴘʀᴀᴠʟʏᴀʟɪ ᴍᴀsʜɪɴʏ ʏᴀ ᴢᴀᴘʀᴀᴠʟʏᴀʟ sᴘᴇʀᴍᴀᴋᴏᴍ ᴛᴠᴏʏᴜ ᴢʜᴀʟᴋᴜʏᴜ ᴍᴀᴛᴜʜᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴀᴠᴛᴏsᴛᴀɴᴛsɪɪ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴏᴋᴀ ʜᴏᴅɪʟɪ ᴀᴠᴛᴏʙᴜsʏ ᴍᴏᴊ ʜᴜᴊ ᴢᴏᴅɪʟ ᴠɴᴛᴜʀɪ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴜsʜᴋᴇ ᴏʀᴜ ᴅᴜʀᴇɴь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴍᴏʀᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ɴᴏ ᴛᴀᴍ ᴘᴏᴘʏᴛᴀʟɪsь ᴜ ᴍᴇɴʏᴀ ᴇё sᴘɪᴢᴅᴇᴛь ɴᴏ ᴏɴᴀ ᴠᴇʀɴᴜʟᴀsь ᴢᴀ 1000 ᴋᴍ ᴋᴏ ᴍɴᴇ ᴠᴇᴅь ᴏɴᴀ ᴠᴇʀɴᴀ ᴍᴏᴇᴍᴜ ʜᴜʏᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴋᴀʀɪʙsᴋɪʜ ᴏsᴛʀᴏᴠᴀʜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴏɴᴀ ʀᴇsʜɪʟᴀ sʜɪᴋᴀɴᴜᴛь ɪ ᴘᴏᴇʜᴀʟᴀ ɴᴀ ᴏsᴛʀᴏᴠᴀ ɴᴏ ᴠᴢʏᴀʟᴀ ᴍᴇɴʏᴀ ᴠᴇᴅь ᴋᴛᴏ ᴇᴊ ᴛᴀᴍ ɴᴀ ʀᴏᴛᴀɴ ᴋɪᴅᴀᴛь ʙᴜᴅᴇᴛ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴢᴀᴋᴀᴛᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴠsё ʙʏʟᴏ ᴛᴀᴋ ᴋʀᴀsɪᴠᴏ ᴋʀᴏᴍᴇ ᴇʙᴀʟᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘʀɪsʜʟᴏsь ɴᴀ ᴇᴛᴜ ᴅᴜʀᴜ ᴍᴇsʜᴏᴋ ɴᴀᴅᴇᴠᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴠᴇʀᴛᴏʟёᴛᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴇᴊ ʙʏʟᴏ sᴛʀᴀsʜɴᴏ ʟᴇᴛᴇᴛь ɪ ᴄʜᴛᴏʙʏ ᴜsᴘᴏᴋᴏɪᴛь ᴇё ᴍɴᴇ ᴘʀɪsʜʟᴏsь ᴘᴏʀᴠᴀᴛь ᴇᴊ ᴛᴀᴍ ᴀɴᴀʟ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴠᴇʟɪᴋᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴛʏ ᴢʜᴇ ᴅᴜʀᴇɴь ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɪsᴘᴏʟьᴢʏᴠᴀʟᴀ ᴍᴇsᴛᴏ sᴇᴅᴜsʜᴋᴇ ɴᴀ ᴠᴇʟɪᴋᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ʟᴜɴᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴏᴋᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь ʙʏʟᴀ ᴠ ᴠᴏsᴛᴏʀɢᴇ ᴏᴛ ᴋᴏsᴍᴏsᴀ ʏᴀ ᴇё ᴇʙᴀʟ ʟᴀᴊᴋɴɪ ᴢᴀᴘɪsɪ ᴇsʟɪ ʏᴀ ᴘᴏsᴛᴜᴘɪʟ ᴘʀᴀᴠɪʟьɴᴏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴘʀᴏᴠᴏᴅᴀʜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴏᴋᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛᴜʜᴀ ᴘʀᴏᴠᴀᴢʜᴀʟᴀ ᴛᴠᴏᴇɢᴏ ʙᴀᴛʏᴜ ᴠ ᴀʀᴍɪʏᴜ ᴏɴᴀ ᴘᴜsᴛɪʟᴀ sʟᴇᴢᴜ ɴᴏ ᴠsᴇ ᴢɴᴀʟɪ ᴋᴛᴏ ʙᴜᴅᴜsᴄʜɪᴊ ɢᴏᴅ ʙᴜᴅᴇᴛ ᴇᴊ ɴᴀ ʀᴏᴛᴀɴ ᴋɪᴅᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴘɪᴛ sᴛᴏᴘᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴋᴏɢᴅᴀ ᴏɴᴀ ᴘʀʏɢᴀʟᴀ ᴠ ᴛᴀᴄʜᴋᴇ ᴋ ᴄʜᴜᴢʜɪᴍ ᴍᴜᴢʜɪᴋᴀᴍ ᴏɴɪ ʀᴀsᴄʜɪᴛʏᴠᴀʟɪ ɴᴀ ᴄʜᴛᴏ ᴛᴏ ɴᴏ ᴘᴏᴛᴏᴍ ᴘᴏɴʏᴀʟɪ ᴄʜᴛᴏ sᴏsёᴛ ᴏɴᴀ ᴛᴏʟьᴋᴏ ᴍɴᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴢᴀᴠᴏᴅᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴏᴋᴀ ᴠsᴇ ᴄʜᴛᴏ ᴛᴏ ᴘʀᴏɪᴢᴠᴏᴅɪʟɪ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴠ ᴛsᴇʜᴇ ᴘᴏ ᴏʙʀᴀʙᴏᴛᴋᴇ ᴍᴏᴊ ʜᴜᴊ ᴏʙʀᴀʙᴀᴛʏᴠᴀʟᴀ ᴏʀᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴠᴏʟɴᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴏᴋᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇ ɴᴀᴜᴄʜɪʟᴀsь ᴇᴢᴅɪᴛь ɴᴀ ᴍᴏёᴍ ʜᴜʏᴜ ᴏɴᴀ ɴᴇ ᴘᴇʀᴇsʜʟᴀ ᴋ sёʀғɴᴏᴊ ᴅᴏsᴋᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴋᴏʀɴᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ sᴍᴇsʜɴᴀʏᴀ ɪsᴛᴏʀɪʏᴀ ᴏɴᴀ ᴋᴏᴘᴀʟᴀsь ᴠ ᴏɢᴏʀᴏᴅᴇ ɪ ᴜᴘᴀʟᴀ ɴᴀ ᴋᴏʀᴇɴь ᴀ ᴅᴀʟьsʜᴇ ʏᴀ ᴇё ᴠʏᴇʙᴀʟ ᴋᴀᴋ ᴢʜᴀʟᴋᴜʏᴜ sᴜᴋᴜ ᴀ ᴛʏ ᴄʜᴇɢᴏ ᴏᴢʜɪᴅᴀʟ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴘᴀsᴋᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ᴠʀᴏᴅᴇ ᴛsᴇʀᴋᴏᴠɴʏᴊ ᴘʀᴀᴢᴅɴɪᴋ ɴᴏ ᴇᴛᴀ sʜʟʏᴜʜᴀ ᴍᴇsᴛᴏ ᴋᴜʟɪᴄʜᴀ ᴍᴏᴊ ʜᴜᴊ ɴᴀᴠᴏʀᴀᴄʜɪᴠᴀʟᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴋʀᴇsᴛɪɴᴀʜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ sʜɪᴋᴀʀɴʏᴊ ᴘʀᴀᴢᴅɴɪᴋ ɴᴏ ᴅᴀᴢʜᴇ ᴛᴀᴍ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜᴍᴜᴅʀɪʟᴀsь ʀᴀsᴛᴀᴠɪᴛь ᴘᴇʀᴇᴅ ᴍɴᴏᴊ sᴠᴏɪ ɴᴏɢɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴋᴀᴘᴄʜᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴍᴇɴʏᴀ ᴘʏᴛᴀʟɪsь ʙʟᴏᴋɴᴜᴛь ᴢᴀ ᴛᴏ ᴄʜᴛᴏ ʏᴀ ɴᴇᴘʀᴀᴠɪʟьɴᴏ ᴠᴏᴅɪʟ ᴘᴀʀᴏʟь ᴘᴏ ᴘɪᴢᴅᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ʀᴜʟᴇᴛᴋᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ᴋᴏɢᴅᴀ ᴜ ᴠsᴇʜ ɪɢʀᴏᴋᴏᴠ ᴋᴏɴᴄʜɪʟɪsь ᴅᴇɴьɢɪ ᴋᴛᴏ ᴛᴏ ᴘᴏsᴛᴀᴠɪʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ɴᴜ ʏᴀ ᴇё ɪ ᴠʏᴇʙᴀʟ ᴘᴏ ᴛɪʜᴏᴍᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴋᴏʀᴀʙʟᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴘᴏᴋᴀ ᴠsᴇ ɴʏᴋᴀʟɪ ᴏᴛ sʜᴛᴏʀᴍᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴘᴇᴛsɪᴀʟьɴᴏ ᴠʏʙᴇɢᴀʟᴀ ɴᴀ ᴘᴀʟᴜʙᴜ ɪ sᴏsᴀʟᴀ ᴍɴᴇ ʜᴜᴊ ᴋᴀᴋ ɴᴇɴᴏʀᴍᴀʟьɴᴀʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ sᴠᴀʟᴋᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴛʏ sᴘʀᴏsɪsʜь ᴋᴀᴋ ʏᴀ ᴛᴜᴅᴀ ᴢᴀsʜёʟ ᴠsё ᴘʀᴏsᴛᴏ ʏᴀ ʜᴏᴛᴇʟ ᴠʏʙʀᴏsɪᴛь ᴍᴜsᴏʀ ᴀ ᴛᴀᴍ ʟᴇᴢʜᴀʟᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇᴘʟᴏʜᴏ ᴛᴏɢᴅᴀ ᴠʏᴇʙᴀʟ ᴇё <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ sᴏʙʀᴀɴɪᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ᴠsᴇ ᴅᴜᴍᴀʟɪ ᴄʜᴛᴏ ᴏɴᴀ ᴘʀɪsʜʟᴀ ʀᴀᴢʙɪʀᴀᴛьsʏᴀ ɴᴏ ᴏɴᴀ ᴠsᴇɢᴏ ʟɪsʜь ʜᴏᴛᴇʟᴀ ᴏᴛsᴏsᴀᴛь ᴍɴᴇ ʜᴜᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴠʀᴀᴛᴀʜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ᴏɴᴀ ᴘʏᴛᴀʟᴀsь ᴠᴏʀᴠᴀᴛьsʏᴀ ᴠ ᴄʜᴜᴢʜᴜʏᴜ ʜᴀᴛᴜ ɪ sʟᴏᴍᴀᴛь ᴠᴏʀᴏᴛᴀ ɴᴏ ᴍᴏᴊ ʜᴜᴊ ᴏᴛᴠᴇʀɢ ᴇё ɪ ᴏɴᴀ ᴏᴛᴏsʜʟᴀ s ᴘᴏʀᴀᴢʜᴇɴɪᴇᴍ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴠᴇsɪʟɪᴛsᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴀʟ ᴋᴏɢᴅᴀ ᴇᴛᴀ ᴅᴜʀᴀ ᴢᴀʜᴏᴛᴇʟᴀ ᴘᴏᴠᴇsɪᴛьsʏᴀ ᴍᴏᴊ ʜᴜᴊ sᴀᴍ ᴇё ᴘᴏᴅᴠᴇsɪʟ ɴᴏ ᴇᴊ ʙʏʟᴏ ʟᴇɢᴄʜᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴋʀᴀʏᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴜ ɴᴇё ᴘʀᴏsᴛᴏ ɴᴇ ʙʏʟᴏ ᴠʏʜᴏᴅᴀ ᴜʙᴇᴢʜᴀᴛь ᴏᴛ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ᴏʀᴜ ᴏɴᴀ ᴛᴀᴋ ɪ ɴᴇ ᴘᴏɴʏᴀʟᴀ ᴄʜᴛᴏ ᴏᴛ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ɴᴇ ᴏsᴠᴏʙᴏᴅɪᴛьsʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴘᴀʀᴀᴅᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴋᴏɢᴅᴀ ᴠsᴇ ᴋʀᴀsɪᴠᴏ ᴍᴀʀsʜᴇʀᴏᴠᴀʟɪ ʏᴀ ᴋʀᴀsɪᴠᴏ ᴇё ᴇʙᴀʟ ᴀ ᴢɴᴀᴇsʜь ᴋᴀᴋ ʏᴀ ᴇᴛᴏ ᴘᴏɴʏᴀʟ ᴠ ᴋᴏɴᴛsᴇ ᴘᴜsᴋᴀʟɪ sᴀʟʏᴜᴛ ᴠ ᴄʜᴇsᴛь ᴍᴏᴇɢᴏ ᴄʜʟᴇɴᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍᴀᴍᴀ ᴛᴠᴏʏᴀ sʜʟʏᴜʜᴀ ᴍʏ s ɴᴇᴊ ᴢɴᴀᴋᴏᴍʏ ɴᴇ ᴘᴇʀᴠʏᴊ ɢᴏᴅ ᴘʀᴇᴅsᴛᴀᴠь sᴋᴏʟьᴋᴏ ᴏɴᴀ ᴍɴᴇ sᴏsᴇᴛ  ᴜᴢʜᴇ sᴏ sᴄʜᴇᴛᴀ sʙɪʟsʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴋᴀᴋ ᴏsᴛᴀʟьɴʏᴇ ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴏsᴇᴛ ᴏɴᴀ ʟɪᴄʜɴᴏ ᴍᴏʏᴀ ʀᴀʙʏɴ ᴋᴏᴛᴏʀᴀʏᴀ ɴᴇ ᴘʀɪᴅᴀᴇᴛ sᴠᴏʏᴜ ʀᴀʙᴏᴛᴜ ɴᴇ ʙᴜᴅь ᴋᴀᴋ ᴏɴᴀ ᴘᴏsᴏsɪ ᴍɴᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴜ ʙᴜᴅᴇᴍ sᴛᴏʏᴀᴛь ᴢᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴍʏ ᴇᴇ ᴘʀᴏsᴛᴏ ᴏᴛьᴇʙᴇᴍ ᴅᴀᴢʜᴇ ɴᴇ ᴘʟᴀᴄʜь ᴘᴏᴛᴏᴍ ɪ ɴᴇ ʙᴇɢᴀᴊ ᴢᴀ ɴᴀᴍɪ ᴠᴇᴅь ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴘʀᴏᴅᴀᴢʜɴᴀʏᴀ ɪ sᴀᴍᴀ ᴘᴏᴅᴘɪsᴀʟsь ɴᴀ ᴇᴛᴏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ʀᴀɴьsʜᴇ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴏʀᴍᴀʟьɴᴏ sᴏsᴀʟᴀ ɴᴏ ᴛᴇᴘᴇʀь ᴏɴᴀ ɪᴢʙᴀᴠɪʟᴀsь ᴏᴛ ᴇᴛᴏᴊ ᴘʀɪᴠʏᴄʜᴋɪ ɪ ᴋᴀᴋ sʜᴀʟᴀᴠᴀ ᴛᴜᴛ sᴏsᴇᴛ ᴅᴀᴠᴀᴊ ᴢᴀᴋᴏɴᴄʜɪᴍ s ᴇᴛɪᴍ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ʀᴀɴьsʜᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴠ ᴛʀɪ sᴄʜᴇʟɪ ᴇʙᴀʟɪ ᴛᴇᴘᴇʀь ᴏɴᴀ ʜᴏᴄʜᴇᴛ ʙᴏʟьsʜᴇ ɴᴇ ᴍᴏᴢʜᴇᴍ ᴏᴛᴋᴀᴢᴀᴛь ᴇᴛᴏᴊ sʜᴀʟᴀᴠᴇ ɪ ᴢᴏᴠᴇᴍ ᴛᴏʟᴘʏ ɴᴀ ᴇᴇ ᴘɪᴢᴅᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴢᴀᴋᴏɴᴄʜɪʟɪ s ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀьʏᴜ ᴅᴀᴠᴀᴊ ᴛᴀsᴄʜɪ ᴇᴇ sʏᴜᴅᴀ ɪ ɴᴇ ᴘʀᴏʙᴜᴊ ᴍɴᴇ ᴛᴜᴛ ᴏᴋɪɴᴜᴛьsʏᴀ ᴛᴀᴋ ᴋᴀᴋ ᴛᴠᴏʏᴀ ᴍᴀᴛь sʜʟʏᴜʜᴀ ʀᴀᴢɢᴠᴏʀ s ɴᴇᴊ ᴋᴏʀᴏᴛᴋɪᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴠɴᴀᴛᴜʀᴇ ᴛᴠᴏʏᴜ ᴘᴇᴄʜᴇɴᴋᴜ ᴛᴜᴛ ɴᴀ ʜᴜᴊ ɴᴀᴍᴏᴛᴀʟ ɴᴇ ᴜᴠᴇʀᴇɴɴᴏ ᴍɴᴇ ᴛᴜᴛ sᴏsᴇsʜь ᴅᴜʀᴀᴄʜᴏᴋ ᴏᴘʏᴀᴛь ᴛᴇʙᴇ ɴᴀᴅᴏ ᴘᴇᴄʜᴇɴᴋᴏᴊ ᴘᴏᴢʜᴇʀᴛᴠᴏᴠᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴛʏᴀᴢʜᴇʟʏᴊ ᴇᴛᴏ ᴛʀᴜᴅ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀᴛь ɴᴏ ᴢᴀɴɪᴍᴀᴇᴛ ᴠʀᴇᴍʏᴀ ᴛᴀᴋ ᴋᴀᴋ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇɴᴀsʏᴛɴᴀʏᴀ sʜʟʏᴜʜᴀ ɴᴜ ᴄʜᴛᴏ ᴘᴏᴅᴇʟᴀᴛь ᴍʏ ᴘᴏᴘʀᴏʙᴜᴇᴍ ᴜᴅᴠᴏʟᴇᴛᴠᴏʀɪᴛь ᴇᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴅᴀᴠᴀᴊ ᴢᴀᴠᴏᴅɪ ᴜᴢʜᴇ sᴠᴏʏᴜ ᴍᴀᴛь ᴏɴᴀ ᴏᴘʏᴀᴛь ɴᴀ ᴋᴏʟᴇɴʏᴀʜ ᴘʀɪʙᴇᴢʜɪᴛ ɪ ʙᴜᴅᴇᴛ ᴘʀᴏsɪᴛь ᴘʀᴏsᴄʜᴇɴɪʏᴀ ᴢᴀ ᴛᴇʙʏᴀ ᴛʏ ᴅᴀᴢʜᴇ ɴᴇ ᴍᴏᴢʜᴇsʜь ᴘᴏɴʏᴀᴛь ᴄʜᴛᴏ ᴏɴᴀ ᴅᴀᴠɴᴏ ᴘʀᴏᴅᴀʟᴀsь ᴢᴀ ᴋᴏᴘᴇᴊᴋɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍᴀᴍᴜʟьᴋᴜ ᴛᴠᴏʏᴜ ᴠɴᴀᴛᴜʀᴇ ɴᴀ sᴜᴅᴇ ᴘᴏᴅsᴛᴀᴠɪʟ ᴠsᴇ ɢᴏᴠᴏʀɪʟɪ ᴄʜᴛᴏ ᴏɴᴀ ᴘᴏʀʏᴀᴅᴏᴄʜɴᴀʏᴀ ᴢʜᴇɴsᴄʜɪɴᴀ ɴᴏ ʏᴀ ɪᴍ ᴘᴏᴋᴀᴢᴀʟ ᴠɪᴅᴇᴏ ɢᴅᴇ ᴇᴇ ᴛʀᴏᴇ ᴇʙᴀʟɪ ᴠɴᴀᴛᴜʀᴇ ᴏʀɴᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴋᴀᴋ ᴠᴇʀᴛᴏʟᴇᴛ sᴀsᴇsʜь ᴠɴᴀᴛᴜʀᴇ ʏᴀ ᴛᴇʙᴇ ᴘʀᴏᴘᴇʟᴇʀᴏᴍ ᴠɴᴀᴜᴛʀᴇ sᴄʜᴀ ᴀɴᴀʟьɴᴏᴇ ᴏᴛᴠᴇʀsᴛɪᴇ ᴠᴢᴏʀᴠᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍᴀᴛь ᴛᴠᴏʏᴀ ᴘᴏᴅsᴛɪʟᴋᴀ ᴠɴᴀᴛᴜʀᴇ ᴛʏ ᴢɴᴀᴇsʜь ᴄʜᴛᴏ ᴏɴᴀ sᴛᴏʀᴏᴢʜᴜ ᴢᴀ ᴄʜᴇᴋᴜsʜᴋᴜ ᴅᴀʟᴀ ᴢᴀ ᴢᴀʙᴏʀᴏᴍ ᴀ ᴛʏ ᴅᴜᴍᴀʟ ᴘʀɪʟɪᴄʜɴᴀʏᴀ ʜᴇ ʜᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴅᴀᴠᴀᴊ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴇʙᴇᴍ ᴘʀɪɢʟᴀsʜᴀᴊ ᴇᴇ ɴᴀ ʙᴀʟ ʜᴏᴄʜᴇsʜь ᴘᴏssᴀᴛь ᴠᴍᴇsᴛᴇ s ɴᴇᴊ ᴘʀɪʜᴏᴅɪ ɴᴏ sɴᴀᴄʜᴀʟᴀ ᴘᴏᴛᴀɴᴛsᴜᴇᴍ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ʙᴜᴅь ᴅᴜʀᴀᴋᴏᴍ ᴘᴏᴠᴇʀь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь sʜʟʏᴜʜᴀ ᴠɴᴀᴜʀᴇ ᴛᴜᴛ ᴘᴏɢɪʙɴᴇᴛ ɪʟɪ ᴛʏ ᴅᴜᴍᴀᴇsʜь ᴜ ɴᴇᴇ ʙᴜᴅᴜᴛ sʜᴀɴsʏ ᴠʏᴢʜɪᴛь ʜᴇ ʜᴇ ᴅᴜʀᴀᴋ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏᴇ ᴇʙᴀʟᴏ ᴠɴᴀᴛᴜʀᴇ ᴠ ʙᴇᴛᴏɴ ᴋᴀᴛɴᴜʟ ᴋᴏɢᴅᴀ ᴛʏ ᴘᴏsʜᴇʟ ᴘʀᴏᴛɪᴠ ᴍᴇɴʏᴀ ʏᴀ ᴛᴇʙʏᴀ ʜᴜᴇᴍ ᴄʜᴇʜʟɪʟ ᴅᴜʀᴀᴋ ᴇɢɪ ᴏᴛ sʏᴜᴅᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ɴᴇ ᴛᴀᴋᴏᴊ ᴋᴀᴋ ᴠsᴇ ᴘᴏᴛᴏᴍᴜ ᴄʜᴛᴏ ᴜ ᴠsᴇʜ ᴍᴀᴍᴀ ɢᴏᴛᴏᴠɪᴛ ᴋᴜsʜᴀᴛь ᴀ ᴛᴠᴏʏᴀ ᴍᴀᴍᴀ ᴠᴍᴇsᴛᴏ ᴇᴅʏ ᴠᴀᴍ ɴᴀ ᴜᴢʜɪɴ sᴘᴇʀᴍᴀᴄʜ ᴠʀᴀɪᴛ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴅᴀᴠᴀᴊ sᴄʜᴀs ᴍʏ s ᴛᴏʙᴏᴊ ᴘᴏᴢɴᴀᴋᴏᴍɪᴍsʏᴀ ɪ ʏᴀ sᴛᴀɴᴜ ᴛᴠᴏɪᴍ ɴᴏᴠʏᴍ ᴏᴛᴛsᴏᴍ ʜᴏᴛʏᴀ ᴘᴏ sᴜᴛɪ ʏᴀ ᴅᴀᴠɴᴏ ᴇʙᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴛᴀᴋ ᴄʜᴛᴏ ɴᴀᴢʏᴠᴀᴊ ᴍᴇɴʏᴀ ᴠsᴇᴠʏsʜɴɪᴍ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ʀɪʟɪ ᴛʏ ᴘʀᴏsᴛᴏ ᴘᴏᴘʟᴀᴛɪʟsʏᴀ sᴠᴏᴇᴊ ᴍᴀᴛᴇʀьʏᴜ ᴢᴀ sᴠᴏᴊ ʙᴀᴢᴀʀ ɪʟɪ ᴛʏ ᴅᴜᴍᴀʟ ᴄʜᴜᴛь ᴄʜᴜᴛь ᴘᴏsᴏsᴇsʜь ɪ sʙᴇᴢʜɪsʜь ɴᴇᴛ ᴛʏ ᴛᴜᴛ ɴᴀ ᴠsᴇɢᴅᴀ sᴄʜᴇɴᴏᴋ ᴢᴀᴠɪs <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀ ᴋᴜʀᴏᴋ ɴᴀᴢʜᴀʟ ᴋᴏɢᴅᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴏsᴀʟᴀ ɪ ᴋᴏʀᴏᴄʜᴇ ᴇᴊ ʙᴀsʜᴋᴜ ᴠ ᴍʏᴀsᴏ ʀᴀᴢɴᴇsʟᴏ ɴᴏ sᴏsᴀᴛь ᴏɴᴀ ɴᴇ ᴘᴇʀᴇsᴛᴀʟᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴋᴏɢᴅᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏᴅ ᴘʀɪʜᴏᴅᴏᴍ ɢᴇʀʏᴄʜᴀ ᴇʙᴀʟ ᴏɴᴀ ᴋᴀᴢᴀʟᴀsь ᴋʀᴀsɪᴠᴏᴊ ᴠ ɪᴛᴏɢᴇ ᴋᴏɢᴅᴀ ᴍᴇɴʏᴀ ᴏᴛᴘᴜsᴛɪʟᴏ ʏᴀ ʙᴇᴢʜᴀʟ ᴠ sᴛʀᴀʜᴇ ᴏᴛ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴏʙʏᴄʜɴᴏ ᴘьʏᴜ ᴢᴀ ᴅᴠᴇ ᴠᴇsᴄʜɪ ɴᴀ ᴢᴀ sᴛᴏʟьᴇ ᴄʜᴛᴏʙʏ ʜᴜᴊ sᴛᴏʏᴀʟ ɪ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴘᴏʙʟɪᴢʜᴇ ʙʏʟᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴜ ᴅᴀᴠᴀᴊ ʏᴀ ᴛᴠᴏё ʀʏʟᴏ ᴠ ᴇᴛᴏᴊ ᴋғ ᴏʙᴋᴏɴᴄʜᴀʏᴜ ᴋᴀᴋ ᴛʏ ᴘᴏᴛᴏᴍ ʙᴜᴅᴇsʜь ʀᴀsᴋᴀᴢʏᴠᴀᴛь sᴠᴏɪᴍ ᴅʀᴜᴢьʏᴀᴍ ᴄʜᴛᴏ ᴛʏ ᴍᴇɴʏᴀ ᴠʏᴠᴇᴢ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴏᴛ ɴᴇᴅᴏᴛʀᴀʜᴀ ɴᴀ ᴋᴀᴢʜᴅʏᴊ ᴋᴏʟ ʟᴇᴢᴇᴛ ʏᴀ ᴜᴢʜᴇ ɴᴇ ᴢɴᴀʏᴜ ᴄʜё ᴅᴇʟᴀᴛь ᴍᴏᴢʜᴇᴛ ᴏsʜᴇᴊɴɪᴋ ᴋᴜᴘɪᴛь ᴋᴀᴋ ᴅᴜᴍᴀᴇsʜь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴋᴀᴋ ɪᴍᴘᴇʀᴀᴛᴏʀ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴜ ᴍᴇɴʏᴀ ᴠ ɴᴏɢᴀʜ ᴘᴏʟᴢᴀᴇᴛ ɴᴏ ᴘʀɪ ᴇᴛᴏᴍ ʏᴀ ᴢʜɪᴠᴜ ᴋᴀᴋ ᴠsᴇ ɴᴏ ᴘᴏᴄʜᴇᴍᴜ ᴛᴠᴏʏᴀ ɢᴏʀʏᴀ ᴍᴀᴛь ᴍɴᴇ ᴛᴏ sᴏsёᴛ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴇsᴛь ᴘʀɪʟᴏᴢʜᴇɴɪʏᴀ ᴇsʟɪ ᴋᴜᴘɪsʜь 3 ᴘᴀᴄʜᴋɪ sᴜʜᴀʀɪᴋᴏᴠ sᴋᴀɴɪʀᴜᴇsʜь ᴄʜᴇᴋ ɪ ᴛᴇʙᴇ ʙᴇsʟᴘᴀᴛɴᴏ ᴠʏᴘᴀᴅᴀᴇᴛ ёʙ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴏᴛ ᴏᴅɴᴏɢᴏ ᴅᴏ ᴅᴇsʏᴀᴛɪ ʀᴀᴢ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴜ ᴢʜᴇ ᴅᴀᴠᴀᴊ ᴏᴋʟᴇᴍᴀᴊsʏᴀ ᴏᴛ ᴘᴏʙᴏᴇᴠ ᴍᴏᴇɢᴏ ᴄʜᴇʟᴇɴᴀ ɪ sᴍᴇʀɪsь s ᴍʏsʟьʏᴜ ᴄʜᴛᴏ ᴇʙᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ɴᴇ ᴛᴏʟьᴋᴏ ʏᴀ ɴᴇʜᴜᴊ ɴᴀ ᴍᴇɴʏᴀ ʙʏᴄʜɪᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴋᴏɢᴅᴀ ᴄʜᴛᴏ ɴɪʙᴜᴅь ɢᴏᴛᴏᴠɪᴛ ɴᴇ ᴏʙʜᴏᴅɪᴛьsʏᴀ ʙᴇᴢ ᴍɪɴьᴇᴛᴀ ᴠᴇᴅь ᴇᴛᴀ sʜᴋᴜʀᴀ ʟʏᴜʙɪᴛ ᴏᴛsᴀsʏᴠᴀᴛь ᴠᴏ ᴠʀᴇᴍʏᴀ ɢᴏᴛᴏᴠᴋɪ ᴏʜᴜᴇsʜь ᴍᴀʟʏᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ʙʟʏᴀ ɴᴇ ᴢɴᴀʏᴜ ᴍᴏᴢʜᴇᴛ ɪ ʏᴀ ᴛᴠᴏᴊ ᴏᴛᴇᴛs ᴛʏ ᴇᴛᴏ ɴᴇ ʀᴀsᴛʀᴀᴇᴠᴀᴊsʏᴀ ʜᴜᴊ ᴢɴᴀᴇᴛ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴅᴏʜᴜʏᴀ ᴋᴛᴏ ᴇʙᴀʟ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴅᴀᴠᴀᴊ ᴘᴏɪɢʀᴀᴇᴍ ᴠ ᴋᴀʀᴛʏ ɴᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴅᴀᴢʜᴇ ᴇsʟɪ ʏᴀ ᴘʀᴏɪɢʀᴀʏᴜ ᴛʏ ᴢʜᴇ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴏɴᴀ ᴠsᴇ ʀᴀᴠɴᴏ ᴍᴏʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴅᴀ ɢᴏᴠᴏʀʏᴜ ᴛᴇʙᴇ ɴᴇ ᴅᴀᴍ ʏᴀ ᴛᴇʙᴇ ᴅᴅ ᴢᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇё ᴋᴛᴏ ᴛᴏʟьᴋᴏ ɴᴇ ᴇʙᴀʟ ɴᴀsʜёʟ ʀᴇʟɪᴋᴠɪʏᴜ ʙʟʏᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴅᴀᴠᴀᴊ ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴛᴜᴛ ᴢᴀᴛʀᴀʜᴀʏᴜ ᴅᴏ sᴍᴇʀᴛɪ ɪʟɪ ᴛʏ ᴄʜё ᴛʏᴜғʏᴀᴋ ᴅᴀᴢʜᴇ sᴏᴘʀᴏᴛɪᴠʟʏᴀᴛsьʏᴀ ɴᴇ ʙᴜᴅᴇsʜь ɴᴜ ᴢᴀ ᴇᴛᴏ ᴘʀɪᴅёᴛsьʏᴀ ᴛᴇʙʏᴀ ᴘʀᴏɢɪʙᴏᴍ sʜᴠʏʀɴᴜᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴛᴇʙᴇ sᴇᴊᴄʜᴀs ᴠɴᴀᴛᴜʀᴇ ʏᴀᴊᴛsᴀ ᴠ ʀᴏᴛ ᴢᴀsᴜɴᴜ ɪ ᴛʏ ɪʜ ʙᴜᴅь ᴘᴏʟᴏsᴋᴀᴛь ᴅᴏ ᴋᴏɴᴛsᴀ sᴠᴏɪʜ ᴅɴᴇᴊ ᴜёᴏᴋ ᴘᴏsʜёʟ ɴᴀʜᴜᴊ ᴏᴛ sʏᴜᴅᴀ ᴘᴏɴʏᴀʟ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴠᴏᴛ ᴇsʟɪ ʙʏ ᴛʏ ᴘʀᴏʏᴀᴠɪʟ ʜᴏᴛʏᴀ ʙʏ ᴋᴀᴘʟʏᴜ ᴜᴠᴀᴢʜᴇɴɪʏᴀ ʏᴀ ʙʏ ɴᴇ ᴇʙᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴀ ᴛᴀᴋ ɴᴀ sᴋᴏʀᴜʏᴜ ʀᴜᴋᴜ sᴇᴊᴄʜᴀs ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴅᴜᴘʟᴏ ᴘᴏʀᴠᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴛᴇʙᴇ ʜᴜᴇᴍ sᴇᴊᴄʜᴀs ᴘʀᴏsᴛʀᴇʟʏᴜ ᴄʜᴍᴏsʜɴɪᴋ ʏᴀ ᴛᴇ ᴠɴᴀᴛᴜʀᴇ sᴇᴊᴄʜᴀs ᴋᴀʀᴛᴇᴄʜь ᴠ ᴛᴠᴏᴊ ᴢʜɪᴠᴏᴛ ɴᴀʜᴜʏᴀᴄʜᴜ ᴛʏ ᴅʏʀᴋᴀ ᴇʙᴀɴᴀʏᴀ ᴜᴘᴏʟᴢᴀᴊ s ᴋғ ᴘᴏᴋᴀ ᴠᴏᴢᴍᴏᴢʜɴᴏsᴛь ᴇsᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴛᴠᴏʏᴜ ᴍᴛᴀь ɴᴀ ᴘᴏᴘᴜᴛᴋᴀʜ ᴇʙᴀʟ ᴏɴᴀ ᴘʏᴛᴀʟᴀsь ᴠ ᴍᴀsʜɪɴᴜ ᴘʀʏɢɴᴜᴛь ɴᴜ ʏᴀ ʜᴇʟᴜ ᴋᴀᴋ ᴄʜʟᴇɴ ᴇᴊ ᴠ ʀᴏᴛ ᴢᴀsᴜɴᴜʟ ᴛᴀᴋ sᴋᴀᴢᴀᴛь ᴘʀᴏᴋᴀᴛɪʟ ʙʟʏᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴇsʟɪ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴠ ᴛᴇᴄʜᴇɴɪᴇ 5 sᴇᴋᴜɴᴅ ɴᴇ ᴏᴘʀᴀᴠᴅᴀᴇᴛ sᴇʙʏᴀ ɴᴀ sᴄʜёᴛ ᴛᴏᴊ ᴛᴇᴍʏ ᴄʜᴛᴏ ᴏɴᴀ ɴᴀ ʀᴀᴊᴏɴᴇ sʜᴀʟᴀᴠᴀ ʏᴀ ᴇё ᴠʏᴇʙᴜ ʟᴏʟ ᴇᴛᴏ ʀᴏғʟ ʏᴀ ᴇё ɪ ᴛᴀᴋ ᴠʏᴇʙᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴇʙᴀɴɴʏᴊ ᴢᴀsʜᴋᴠᴀʀɴʏᴊ ᴜᴛёɴᴏᴋ ʏᴀ sᴇᴊᴄʜᴀs ᴘʀᴏsᴛᴏ ᴠᴏᴢьᴍᴜ ɪ s ʀᴀᴢɢᴏɴᴀ ᴠʏsʜɪʙᴜ ᴍᴏᴢɢɪ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘᴏsʟᴇ ᴇᴛᴏɢᴏ ɴᴇ ғᴀᴋᴛ ᴄʜᴛᴏ ᴏɴᴀ ᴏᴋʟɪᴍᴀᴇᴛьsʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍʏ ᴋᴏɢᴅᴀ s ᴅʀᴜᴢьʏᴀᴍɪ ᴇᴢᴅɪʟɪ ɴᴀ ᴏʜᴏᴛᴜ ᴏʙᴇᴢᴀᴛᴇʟьɴᴏ ʙʀᴀʟɪ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴛʏ ᴘᴏᴜᴅᴍᴀᴇsʜь ᴏɴᴀ ᴇʙᴜᴄʜɪ ᴏʜᴏᴛɪᴛьsʏᴀ ɴᴇ ᴘʀᴏsᴛᴏ sʜᴀʟᴀᴠᴀ ɴᴀ ᴏʜᴏᴛᴇ ɴᴇ ᴘᴏᴍᴇsʜᴀᴇᴛ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴠ ʀᴜᴋᴀʜ ᴀᴠᴛᴏᴍᴀᴛ ᴘᴏᴛᴏᴍᴜ ᴄʜᴛᴏ sᴏʟᴅᴀᴛ ᴇʙᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь  ɪ ᴇʙᴜ ᴘᴏᴛᴏᴍᴜ ᴄʜᴛᴏ ᴠʏᴊɢʀᴀʟ ᴠᴏᴊɴᴜ ʏᴀᴊᴛsᴀ ɢʟᴏᴛᴀᴊ ᴢᴀ ᴏᴛᴄʜɪᴢɴᴜ sᴛʀᴇʟʏᴀᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴋᴀᴋ ᴘᴏᴛᴇʀᴇɴɴʏᴊ ᴍᴀᴍᴏɴᴛёɴᴏᴋ ᴠᴏʙsᴄʜᴇ ɴᴇ ᴏʀᴇɴᴛɪʀᴜᴇᴛьsʏᴀ ᴠ ᴘʀᴏsᴛʀᴀsɴᴛᴠᴇ ʏᴀ ᴇᴊ ɢᴏᴠᴏʀʏᴜ ᴄʜᴛᴏ ʏᴀ ᴇё ᴠʏᴇʙᴜ ᴏɴᴀ ɴᴇ sʜᴀʀɪᴛ ɪ ᴘʏᴛᴀᴇᴛьsʏᴀ ᴜᴇʜᴀᴛь ᴋ ᴍᴀᴍᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴍʏ ᴍᴀᴍᴜ ᴇʙᴀʟ ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ɴᴀsʜɪ ᴜᴢʏ ᴛʏᴀsɴᴏ sᴠʏᴀᴢᴀɴɴʏ ᴍᴇᴢʜᴅᴜ sᴏʙᴏᴊ ᴠᴀғᴇʟ ᴇʙᴀɴɴʏᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴢᴀ ᴅʀᴜᴢᴇᴊ ɪ ᴅᴠᴏʀ sᴛʀᴇʟʏᴀʏᴜ ᴠ ᴜᴘᴏʀ ᴛᴀᴋ ɢᴏᴠᴏʀɪʟᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴘᴏᴋᴀ ʏᴀ ᴇᴊ ʜᴜᴇᴍ ɴᴀ ʟʙᴜ ɴᴇ ᴠʏᴢʜɪɢ ᴋʟᴇᴊᴍᴏ ᴇʙᴀɴɴᴏᴊ sʜʟʏᴜʜɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ɴᴀ ᴏʙᴇᴅ ʜᴜᴊ ᴠ ʀʏʟᴏ ᴢᴀᴠᴏʀᴀᴄʜɪᴠᴀʏᴜ ɪᴢᴠɪɴɪ ᴢᴀ ᴛᴀᴋᴏᴊ ᴠᴏᴘʀᴏs ᴛʏ ᴠʏʙʟʏᴀᴅᴏᴋ ɴᴏʀᴍᴀʟьɴᴏ ᴋ ᴇᴛᴏᴍᴜ ᴏᴛɴᴏsɪsʜьsʏᴀ ᴇsʟɪ ɴᴇᴛ ᴛᴏ ᴍᴏɢᴜ ᴢᴀᴠᴏʀᴀᴄʜɪᴠᴀᴛь ɴᴀ ᴜᴢʜɪɴ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴏ ᴛᴀᴋᴏᴊ sʜᴇᴍᴇ ʏᴀ ᴍᴏɢᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀᴛь ʀᴀᴢ 40 ɴᴏ ᴍᴏʏᴀ sʜᴇᴍᴀ ᴇsᴄʜё ɴᴇ sᴏᴠᴇʀsʜᴇɴɴᴀ ᴛᴀᴋ ᴄʜᴛᴏ ᴛᴠᴏʏᴜ ᴍᴀᴛь sʜᴀʟᴀᴠᴜ ᴘᴏᴋᴀ ɴᴀ ʀᴀsʟᴏʙᴏɴᴇ ᴇʙᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʙʟʏᴀ ᴇʙᴀᴛь ᴛʏ ᴄʜё ᴢᴀ ᴍᴜᴅᴀᴋ ᴛʏ ᴛᴀᴍ ᴄʜё ᴘɪᴢᴅᴇʟ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇ sʜʟʏᴜʜᴀ ʏᴀ ᴛᴠᴏʏᴜ ʀʏʟᴏ ᴄʜᴜʀᴋᴀsʜ ᴘᴏ ғᴀᴋᴛᴜ ᴠ ᴇᴛᴊᴏ ᴋғ ᴏᴘᴜsʜᴜ ᴢᴀ ᴛᴀᴋɪᴇ sʟᴏᴠᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴅᴀ ᴅᴀᴠᴀᴊ ɴᴇ ᴘᴏʀᴀᴠᴅʏᴠᴀᴊsʏᴀ ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴛʏ ᴄʜё ᴛsᴀᴘʟʏᴀ ʏᴀ sᴄʜᴀs ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴛᴜᴛ ᴛᴀᴋ ᴏᴛᴢʜᴀʀʏᴜ ᴄʜᴛᴏ ᴛʏ ʙᴏʟьsʜᴇ ɪᴢ ᴇᴛᴏᴊ ᴋғ ʙᴇᴢ ɢᴏʀʟᴏᴠᴏɢᴏ ᴍɪɴьᴇᴛᴀ sᴅᴇʟᴀɴɴᴏɢᴏ ᴍɴᴇ ɴᴇ ᴠʏᴊᴅᴇsʜь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴏ ᴘʀɪɴᴛsɪᴘᴜ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴛᴀᴋ ᴛᴏ ɴᴏʀᴍᴀʟьɴᴀʏᴀ sᴏsᴋᴀ ɴᴇ ɴᴜ ᴇʟɪ ᴛᴀᴋ ʀᴀsᴜᴢʜᴅᴀᴛь ʏᴀ ʙʏ ᴍᴏɢ ᴘᴏᴜʜᴀᴢʜɪᴠᴀᴛь ᴢᴀ ɴᴇᴊ ɴᴏ ᴢʜɪᴢɴь ᴇsᴛь ᴢʜɪᴢɴь ᴇʙёᴍ ᴇё ɪ ᴢᴀᴇʙɪsь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴅᴀᴠᴀᴊ ᴜᴘᴏʀ ʟёᴢʜᴀ ᴘʀɪɴʏᴀʟ ɪ ᴢᴀʟᴜᴘᴜ ᴍɴᴇ ɴᴀᴄʜɪɴᴀᴊ ᴏʙsᴀsʏᴠᴀᴛь ᴛᴇʙᴇ sᴀʟᴀɢᴀ ᴄʜᴛᴏʙʏ ᴏᴛ sʏᴜᴅᴀ ᴜᴊᴛɪ ᴍɴᴇ ᴢᴀʟᴜᴘᴜ ᴇsᴄʜё ɢᴏᴅ ᴏʙsᴀsʏᴠᴀᴛь ᴘʀɪᴅёᴛьsʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴋᴀᴋ ᴛᴏ ᴠᴀᴍ ᴋʀʏsʜᴜ ᴅᴇʟᴀʟ ᴘᴏᴍɴɪsʜь ᴛʏ ᴍᴀʟᴇɴьᴋɪᴊ ʙʏʟ ɴᴏ ɴᴀ sᴀᴍᴏᴍ ᴅᴇʟᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴏɴᴀ ᴘʀᴏsᴛᴏ ɴᴇ ʜᴏᴛᴇʟᴀ ᴛʀᴀᴠᴍɪʀᴏᴠᴀᴛь ᴛᴠᴏʏᴜ ᴅᴇᴛsᴋᴜʏᴜ ᴘsɪʜɪᴋᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʙʟʏᴀᴛь sʜᴀᴋᴀʟ ᴛʏ ɴᴇ ᴠᴋᴜʀɪᴠᴀᴇsʜь ʏᴀ sᴄʜᴀs ᴛᴇʙʏᴀ ᴛᴜᴛ ᴋ sᴛᴇɴᴇ ᴘʀɪᴢʜᴍᴜ ɪ ᴛᴀᴋ ᴏᴛʀᴀʜᴀʏᴜ ᴋᴀᴋ ᴛᴇʙᴇ ᴇsᴄʜё ɴᴇ sɴɪʟᴏsь ᴇʙᴀɴɴʏᴊ ᴘɪᴢᴅᴏʟɪᴢ ᴅᴀᴠᴀᴊ ᴏᴛᴠᴀʟɪᴠᴀᴊ ᴏᴛ sʏᴜᴅᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴅᴀᴢʜᴇ ᴠ sʜᴋᴏʟᴇ ᴅᴇʟᴀʟ ᴘʀᴏᴇᴋᴛ ᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴜᴛь ᴘʀᴏᴇᴋᴛᴀ ᴢᴀᴋʟʏᴜᴄʜᴀʟᴀsь ᴠsᴇ ᴅʀᴇᴠɴɪᴇ ᴘʀᴏғᴇsɪɪ ɴᴏ ᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴏᴋᴀᴢᴀʟᴏsь sᴀᴍᴀʏᴀ ᴅʀᴇᴠɴʏᴀʏᴀ ᴘʀᴏғᴇsɪʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴏᴄʜᴇᴍᴜ ᴠsᴇ ᴍʏ ᴇʙёᴍ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴏᴛᴠᴇᴛ ᴘʀᴏsᴛ ᴏɴᴀ sʜʟʏᴜʜᴀ ɴᴇ ɴᴀ ᴄʜᴛᴏ ɴᴇ sᴘᴏsᴏʙɴᴀʏᴀ ᴀ ᴛʏ ᴄʜᴛᴏ ᴅᴜᴍᴀʟ ᴄʜᴛᴏ ᴏɴᴀ ᴛᴏᴘ ᴍᴏᴅᴇʟь ᴄʜᴇʀᴛɪʟᴀ ᴇʙᴀɴɴᴀʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴋᴏɢᴅᴀ ɴᴇ ᴅᴜᴍᴀʟ ᴄʜᴛᴏ ᴍᴏᴢʜɴᴏ ᴠʏᴇʙᴀᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴢᴀ sɪɢᴜ ɴᴜ ʜᴏᴅɪʟɪ sʟᴜʜɪ ɴᴀ ʀᴀᴊᴏɴᴇ ɴᴜ ʏᴀ ʜᴜʟᴇ ᴘᴏᴘʀᴏʙʏᴠᴀʟ ɪ ᴘʀᴏᴋᴀᴛɪʟᴏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɪᴢɴᴀᴄʜᴀʟьɴᴏ ʏᴀ ᴘᴏᴅɴʏᴀʟsʏᴀ ɴᴀ ᴇʙᴀɴɪᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴠᴇᴅь ᴋᴏɢᴅᴀ ᴍᴇɴʏᴀ ɴᴀ ʀᴀʙᴏᴛᴇ sᴘʀᴏsɪʟɪ ᴄʜᴛᴏ ʏᴀ ᴜᴍᴇʏᴜ ʏᴀ ᴘʀᴏsᴛᴏ ᴘᴏᴋᴀᴢᴀʟ ᴄʜᴛᴏ ᴍᴏɢᴜ ᴠʏᴇʙᴀᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴄʜё ᴛʏ ᴛᴀᴍ ᴅᴏᴄʜь sʜᴀᴠᴇʀᴍʏ ʙʟʏᴀᴛь ʏᴀ ɪᴢ  ᴛᴇʙʏᴀ ᴛᴏᴢʜᴇ sᴅᴇʟᴀʏᴜ sʜʟʏᴜʜᴜ ᴠᴇᴅь ᴠsᴇ ᴍʏ ᴢɴᴀᴇᴍ ᴄʜᴛᴏ ʏᴀʙʟᴏɴʏᴀ ᴏᴛ ʏᴀʙʟᴏɴɪ ɴᴇ ᴅᴀʟᴇᴋᴏ ᴘᴀᴅᴀᴇᴛ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴅᴀᴢʜᴇ ʟʏᴜᴅɪ ʙᴏʟᴇʏᴜsᴄʜɪᴇ sʜɪᴢᴏғʀɪɴᴇᴊ ᴇʙᴀʟɪ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇᴛᴏ ɴᴀsᴋᴏʟьᴋᴏ ɴᴀᴅᴏ ʙʏᴛь ᴏᴘᴜsᴄʜᴇɴʏᴍ ᴄʜᴛᴏʙʏ ᴋᴀᴢʜᴅᴏᴍᴜ ᴏᴘᴜsᴄʜᴇɴᴏᴍᴜ ᴅᴀᴠᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴠ ɪsᴛᴏʀɪɪ ʀᴏssɪɪ ɴᴀᴘɪsᴀɴɴᴏ ᴄʜᴛᴏ ᴋᴏɢᴅᴀ ᴘёᴛʀ 1 ᴘʀᴀᴠɪʟ ʀᴏssɪᴊsᴋᴏᴊ ɪᴍᴘᴇʀɪᴇᴊ ʙʏʟᴀ ʟᴜᴄʜsʜᴀʏᴀ sʜᴀʟᴀᴠᴀ ᴋᴏᴛᴏʀᴀʏᴀ ᴏᴛsᴀsʏᴠᴀʟᴀ ᴇᴍᴜ ʏᴀ ɴᴀsʜёʟ ᴇё ᴇᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴇᴅᴜ ɴᴀ ᴛᴀsᴜ ᴋᴏʀᴏᴄʜᴇ sᴋᴀᴢᴀʟɪ ᴛᴀᴍ ᴇsᴛь ᴠᴀʀɪᴀɴᴛ ᴠsᴛʀᴇᴛɪᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь ɴᴜ ʏᴀ ᴠᴢʏᴀʟ 67 ᴘᴀᴄʜᴇᴋ ᴘʀᴇᴢɪᴋᴏᴠ ᴠᴇᴅь ᴇsʟɪ ᴛᴀᴍ ʙᴜᴅᴇᴛ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴠsё ᴛᴀᴋ ʙʏsᴛʀᴏ ɴᴇ ᴢᴀᴋᴋᴏɴᴄʜɪᴛьsʏᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ɢᴜʙᴜ ʜᴜёᴍ ʀᴀsᴘᴏᴛʀᴏsʜɪʟ ᴀ ᴛʏ ᴅᴏsɪʜᴘᴏʀ ᴠᴇʀɪsʜь ᴠ ᴛᴏ ᴄʜᴛᴏ ᴏɴᴀ ᴍᴏᴢʜᴇᴛ ᴘᴏsᴛᴏʏᴀᴛь ᴢᴀ ᴠᴀs ɴᴀɪᴠɴʏᴊ ᴘɪᴢᴅᴏʟɪᴢ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴠ ɢʀᴀᴢʜᴅᴀɴsᴋᴜʏᴜ ᴏᴊɴᴜ ᴍʏ ᴇʙᴀʟɪ ᴍᴀᴍᴜ ᴛᴠᴏʏᴜ ɪ ᴛᴀᴋ ɪ sʏᴀᴋ ɴᴜ ᴠᴏᴏʙsᴄʜᴇᴍ ɴᴇ ᴠ ᴇᴛᴏᴍ ᴅᴇʟᴏ ᴍʏ ᴇё ᴇʙᴀʟɪ ᴠsᴇɢᴅᴀ ᴀ ᴛʏ ᴛᴏ ᴄʜᴍᴏ ᴄʜᴛᴏ sᴍᴏᴢʜᴇsʜь ᴘʀᴏᴛɪᴠᴏᴘᴏsᴛᴀᴠɪᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴠᴏᴛ ᴛʏ ᴅɪᴋɪᴊ ᴏᴘᴜsᴄʜᴇɴᴇᴛs ᴏᴘᴜʜsʜᴇᴇ ᴅɪᴛᴇ sᴏʙᴀᴋɪ,ᴏɴᴀ ᴄʜᴏᴛ ɴᴀʙɪʀᴀᴇᴛ ɪ sᴍs ɪ ʏᴀ ᴜᴢʜᴇ ᴘᴏɴʏᴀʟ ᴄʜᴛᴏ ᴏɴᴀ sᴏsᴇᴛ ʜᴜᴊ ᴋᴀᴋ ɪ ᴇᴇ ᴍᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴢᴀʟᴜᴘᴇɴᴇᴛs ᴇʙᴀɴɴʏᴊ ʏᴀ ᴛᴇʙᴇ ʜᴜᴇᴍ ᴘᴏ ɢᴜʙᴀᴍ ᴅᴀᴍ sᴀʙʟᴇᴢᴜʙʏᴊ ᴘɪᴅᴏʀᴀs)ᴛʏ ᴘʀᴏsᴛᴏ ᴍᴏɪᴍ ʜᴜᴇᴍ ᴏᴛʙɪᴛʏᴊ)ᴜʙɪᴛʏᴊ)ᴠ ᴍᴜsᴏʀᴋᴜ ᴠʏᴋɪɴᴜᴛʏᴊ)ᴋᴀᴋ ᴘɪᴅᴏʀᴀs ᴘᴏᴛᴇʀʏᴀɴɴʏᴊ ᴛsᴇʟᴜᴇsʜь ᴍᴏʏᴜ ᴍᴀsʜᴏɴᴋᴀ ɪ sʟɪᴢʏᴠᴀᴇsʜь ʟᴇᴄʜᴇʙɴᴜʏᴜ sᴍᴇᴛᴀɴᴜ s ᴍᴏᴇɢᴏ ʜᴜʏᴀ)ʏᴀ ᴢʜᴇ ʙʟʏᴀᴛь ᴛᴠᴏʏᴜ ᴠsʏᴜ sᴇᴍьʏᴜ ʜᴜᴇᴍ ᴅᴜsʜɪʟ ᴇʙᴀɴɴᴀʏᴀ ᴛʏ sᴘɪᴅᴏᴢɴᴀʏᴀ ᴍᴀᴋᴀᴋᴀ ᴋᴏᴛᴏʀᴀʏᴀ ɴᴀ ᴍᴏᴊ ʙᴀɴᴀɴ ᴏʜᴏᴛᴜ ᴜsᴛʀᴏɪʟᴀ)ᴛʏ ᴛᴀᴍ ɴᴇ ᴠᴇsɪ ɴᴀ ᴍᴏᴇᴍ ʜᴜᴇ ᴋᴀᴋ ɴᴀ ʟɪᴀɴᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "sʟʏsʜ ʏᴀ sᴄʜᴀ ɴᴀ sᴠᴏʏᴜ ᴢᴀʟᴜᴘᴜ ᴠᴏᴢɴᴇsᴜ ᴛᴠᴏʏᴜ ᴘɪᴢᴅᴀᴋ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴏᴄʜᴋɪ ɪ ɴᴀᴄʜɴᴜ ᴠsᴛᴜᴘᴀᴛь sᴠᴏɪᴍ ʜᴜᴇᴍ ᴠ ᴘᴏʟᴏᴠᴏᴊ ᴋᴏɴᴛᴀᴋᴛ s ᴛᴠᴏɪᴍɪ ᴜsʜᴀᴍɪ))) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴏᴍɴɪsʜь ᴋᴀᴋ ʏᴀ sᴘɪᴢᴅᴇʟ ᴋᴏᴘьᴇ ᴜ ʀʏᴛsᴀʀʏᴀ ɪ ᴇᴛɪᴍ ᴢʜᴇ ᴋᴏᴘьᴇᴍ ᴏᴛъᴇʙᴀʟ ᴛᴠᴏʏᴜ ʙᴀʙᴜsʜᴋᴜ!) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʜᴜᴇsᴏs?) ᴛʏ ᴜᴠɪᴅᴇʟ ᴘɪᴢᴅᴜ sᴠᴏᴇᴊ ᴍᴀᴍʏ ɪsᴘᴜɢᴀʟsʏᴀ ɪ sъᴇʙᴀʟsʏᴀ? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴅᴀ ᴛʏ ʙʟʏᴀᴛь ᴀʟᴀᴘᴇᴢᴅʏʀь))ᴛᴠᴏʏᴀ ᴍᴀᴍᴋᴀ ᴠʏᴛᴠᴏʀʏᴀᴇᴛ ᴀᴋʀᴏʙᴀᴛɪᴄʜᴇsᴋɪᴇ ᴛʀʏᴜᴋɪ sᴠᴏɪᴍ ʀᴛᴏᴍ ɴᴀ ᴍᴏᴇᴍ ʜᴜʏᴜ))) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴇʙᴜ ᴛᴠᴏʏᴜ ᴍᴀᴍᴋᴜ ᴠ ᴘᴏᴘᴇʀᴇᴄʜɴᴜʏᴜ ᴋɪsʜᴋᴜ ɪ ᴏɴᴀ ᴅᴏʜɴɪᴛ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ʀᴇsʜɪʟ ᴠsᴋᴀʀᴀʙᴋᴀᴛьsʏᴀ ɴᴀ ᴍᴏᴊ ʜᴜᴇᴛs ᴘsɪɴᴀ ʀᴀᴢᴏʀᴠᴀɴɴᴀʏᴀ ɴᴜ ʏᴀ sᴄʜᴀ ᴠᴏᴢьᴍᴜ sᴠᴏʏᴜ ʙɪᴛᴜ ʙʟʏᴀᴛь ɪ ʀᴀssʜɪʙᴜ ᴛᴇʙʏᴀ ɢᴏʟᴏᴠᴏᴊ ᴏʙ ᴋᴀғᴇʟь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴠᴏsᴛᴏʀᴢʜᴇɴɴᴏ ᴜʜɴᴜʟ ɪ ᴛᴜᴛ ᴘᴀʀᴜ ᴠᴏʟᴏsᴀᴛʏʜ ʏᴀɪᴛs ᴜᴅᴀʀɪʟɪ ᴛᴇʙʏᴀ ᴛᴀᴋ ᴄʜᴛᴏ ᴛʏ ɴᴇ ᴍᴏɢ ᴏᴘʀᴀᴠɪᴛьsʏᴀ ɪ ᴛᴏʟьᴋᴏ ᴘᴏsʟᴇ ᴛᴏɢᴏ ,ᴋᴀᴋ ᴛʏ ᴏᴄʜɴᴜʟsʏᴀ ᴛʏ ᴘᴏᴄʜᴜᴠsᴛᴠᴏᴠᴀʟ ,ᴋᴀᴋ ᴛᴠᴏᴊ ʏᴀᴢʏᴋ ʟᴏᴠᴋᴏ ʀᴀʙᴏᴛᴀᴇᴛ ᴠ ᴄʜёʀɴᴏᴊ ɢʀʏᴀᴢɴᴏᴊ ᴢʜᴏᴘᴇ ᴏᴅɴᴏɢᴏ ᴘᴏᴅᴢᴀʙᴏʀɴᴏɢᴏ ᴜʙʟʏᴜᴅᴋᴀ ... <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴋᴏɢᴅᴀ ᴍᴏᴊ ʜᴜᴊ ᴠsᴛᴀᴇᴛ ᴇᴛᴏ ᴢɴᴀᴄʜɪᴛ ᴄʜᴛᴏ ᴛᴠᴏᴊ ʀᴏᴛɪᴋ ʜᴏᴄʜᴇᴛ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ʙᴏʟьsʜᴇ ᴄʜᴇᴍ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ? ʏᴀ sᴄʜᴀs ʜᴜᴇᴍ ᴛᴇʙᴇ ʀᴏᴛ ᴅʏʀʏᴀᴠɪᴛь ʙᴜᴅᴜ ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ.  <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ʙʟʏᴀᴛь ᴘsɪɴᴀ ᴛʏ ᴛᴀᴋɪ ɴᴇ ᴘᴏɴʏᴀʟ ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴅʟʏᴀ ᴛᴇʙʏᴀ ᴛsᴀʀь ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ ᴛᴇʙʏᴀ ᴄʜᴛᴏ ʜᴜᴇᴍ ᴜᴇʙᴀᴛь ᴄʜᴛᴏʙ ᴛʏ sʟᴜsʜᴀʟsʏᴀ ᴍᴇɴʏᴀ, <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʙʟʏᴀʏᴀʏᴀ ʏᴀ ᴛᴜᴛ ᴘᴏɴʏᴀʟ ᴢᴀᴄʜᴇᴍ ᴛᴇʙʏᴀ ᴇʙᴀᴛь ᴠᴏᴛ sᴍᴏᴛʀɪ ᴘᴏᴍɴɪsʜь ᴋᴀᴋ ᴛʏ ᴍɴᴇ ᴢᴀ sᴠᴏᴊ ᴏᴛsᴏs ɴᴇ ᴘʟᴀᴛɪʟ? ᴛʏ ᴘʏᴛᴀʟsʏᴀ ᴍɴᴇ sᴅᴇʟᴀᴛь ᴏᴛsᴏs ᴢᴀ ᴋʀᴇᴅɪᴛ? ᴘᴏɴɪᴍᴀᴇsʜь? ʙʙʟʏᴀ ᴛʏ ʀɪʟɪ ᴅᴜᴍᴀᴇsʜь ᴠʏᴠᴇᴢᴇsʜь ᴍᴇɴʏᴀ? ʜᴜᴇsᴀs ᴛʏ ᴇʙᴀɴʏᴊ ᴘɪᴅᴏʀᴀs <emoji document_id=5317011449061582947>🚬</emoji>",
            "sʟʏsʜɪsʜь ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴋᴀᴋ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟɪ sᴛɪʟᴇᴍ ᴢʜᴜʀᴀᴠʟʏᴀ? ᴘᴏᴍɴɪsʜь ᴋᴀᴋ ᴏɴᴀ sᴛᴀɴᴀʟᴀ ɴᴀʜᴜᴊ sᴜᴠᴀʟᴀ sᴠᴏʏᴜ ɢᴏʟᴏᴠᴜ ᴠ ᴢᴇᴍʟʏᴜ ᴇʙᴀᴛь ʏᴀ ᴛᴏɢᴅᴀ ᴏʀᴀʟ ᴜʜʜʜᴀ ᴋᴀᴋ sʜᴀs ɴᴀᴅ ᴛᴏʙᴏᴊ ᴋᴀᴋ ʀᴠᴜᴛ ᴛᴇʙᴇ sᴄʜᴇᴋᴜ ᴍᴏɪᴍ ʜᴜᴇᴍ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʙʟʏᴀᴛь ᴛʏ ᴄʜᴇ ɴᴀᴢᴜᴊ ɴᴀʜᴜᴊ ᴀʜᴜᴇʟᴀ ᴘɪᴢᴅᴀʟɪᴢᴋᴀ ᴇʙᴀɴᴀʏᴀ ᴛᴇʙʏᴀ ᴄʜᴛᴏ ɴᴀʜᴜᴊ ᴇʙᴀᴛь ᴇᴀᴋ sʜʟʏᴜʜᴜ ᴅʀᴀɴᴜʙ ɪʟɪ ᴄʜᴛᴏ ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ ᴅᴀ ʏᴀ/ᴛᴇʙʏᴀ ᴇʙᴀᴛь ᴋᴀᴋ sʜʟʏᴜʜᴜ ʙᴜᴅᴜ ᴘɪᴅᴏʀᴀs ᴛʏ ᴇьᴀɴʏᴊ ɴᴀᴢᴜᴊ ᴘᴏsʜᴇʟ ᴘᴇᴛᴜʜ ᴅʀᴀɴɴʏᴊ ʏᴀ ᴢʜᴇ ɴᴀʜᴜᴊ ᴇʙᴀᴛь ᴛᴇʙʏᴀ ʙᴜᴅᴜ ᴘᴏᴍɴɪsʜь ᴋᴀᴋ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀᴄʜᴀʟᴀ sᴏsᴀᴛь ᴍɴᴇ ʜᴜᴊ ɪ ᴘᴏʙᴇᴢʜᴀʟᴀ ᴠ ᴛᴜᴀʟᴇᴛ ᴠᴏ ᴠʀᴇᴍʏᴀ ᴋᴏɢᴅᴀ ᴜ ᴛᴇʙʏᴀ ᴘᴏɴᴏsɪʟ ɪ ᴛʏ ɴᴀsʀᴀʟ ɴᴀ sᴠᴏʏᴜ ᴍᴀᴛь ᴀ ᴏɴᴀ ᴢᴀ ᴇᴛᴏ ᴛᴇʙʏᴀ ᴇʀsʜɪᴋᴏᴍ ᴠʏᴇʙᴀʟᴀ ᴘᴏᴍɴɪsʜь ᴛʏ ᴢʜᴇ ɴᴀʜᴜᴊ ɴᴇᴋᴄʜᴇᴍɴʏᴊ ᴘɪᴅᴏʀᴀs ᴛᴇʙʏᴀ ᴍᴀʟᴏ ᴠʏᴇʙᴀᴛь ɪ ᴛʏ ᴇsᴄʜё ᴘʏᴛᴀᴇsʜьsʏᴀ ᴄʜᴛᴏ ᴛᴏ ᴘɪsᴀᴛь ʜᴜᴇsᴀs ᴛʏ ᴇʙᴀɴʏᴊ )ᴘᴏᴍɴɪsʜь ᴋᴀᴋ ᴜᴄʜᴇɴʏᴇ ɴᴀsʜʟɪ ᴠ ᴘɪᴢᴅᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴋᴍ ᴋᴏsᴛь ᴅɪɴᴏᴢᴀᴠʀᴀ? ᴛʏ ɴᴀʜᴜᴊ ᴍᴏᴇɢᴏʜᴜʏᴀ ɴᴇ sᴛᴏɪsʜь ᴘʀɪᴄʜᴇᴍ ᴛᴜᴛ ᴛᴠᴏᴊ ᴏᴛsᴏs ᴇʙᴀɴʏᴊ ᴛʏ ᴢᴜɴsᴀᴀ ᴛʏ ᴜ ᴍᴇɴʏᴀ ʙᴇsᴘʟᴀᴛɴᴏ sᴘᴀsᴀᴛь ᴅᴏʟᴢʜᴇɴ ᴘᴏɴɪᴍᴀᴇsʜь ʜᴜᴇsᴀs ᴛʏ ᴇʙᴀɴʏᴊ ᴠ ʀᴏᴛ ᴛʏ ʙʟʏᴀᴛь ᴘᴇᴛᴜʜ ᴇʙᴀɴʏᴊ ᴘᴏsʜᴇʟ ʏᴀ ᴛᴇʙᴇ ɢᴏᴠᴏʀʙ ɴᴀ ʜᴜᴊ ᴘɪᴅᴏʀᴀs <emoji document_id=5317011449061582947>🚬</emoji>",
            "sʟʏsʜь ᴛʏ ᴘɪᴅᴏʀᴀs ᴛʏ ᴍᴇɴʏᴀ ɴᴇ ᴢᴀᴛʀᴏʟɪsʜь ɪʙᴏ ᴛʏ ʜᴜᴊ ᴍɴᴇ ʏᴀᴢʏᴋᴏᴍ ᴍᴏᴢᴏʟɪsʜь, ʏᴀ ᴇʙᴀʟ ᴛᴇʙʏᴀ ᴠ ʀᴏᴛ ᴛᴀᴋ ᴄʜᴛᴏ ɪᴅɪ ɴᴀʜᴜᴊ ᴇʙᴀɴʏᴊ ᴠ ʀᴏᴛ) ᴇʙᴀʟɪ ᴛᴇʙʏᴀ ᴄʜᴜʀᴋɪ ᴛʏ ᴇsᴄʜё ʜᴏᴄʜᴇsʜь ᴍɴᴇ ᴄʜᴛᴏ ᴛᴏ ᴘɪᴢᴅᴇᴛь? ʜᴜᴇsᴀs ᴛʏ ᴇʙᴀɴʏᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴄʜᴇ ᴇʙᴀᴛь ᴀʜᴜᴇʟᴀ ɴᴀʜᴜᴊ ᴘɪᴅᴏʀᴀsᴋᴀ ɴᴀᴢᴜᴊ sᴄʜᴀs ᴍᴏᴊ ʜᴜᴊ ᴠsɪᴀɴᴇᴛ ᴀ ᴛʏ ʟʏᴀᴢʜᴇsʜь ᴘᴏɴɪᴍᴀᴇsʜь? ʜᴜᴇsᴀs ᴇьᴀɴʏᴊ ᴛʏ ᴍᴏᴊ ʜᴜᴊ sᴏsᴀᴛь ʙᴜᴅᴇsʜь ᴋᴀᴋ ɴɪᴋᴛᴏ ᴅʀᴜɢᴏᴊ ᴘɪᴅᴏʀᴀs ᴛʏ ᴇʙᴀɴʏᴊ ʙʟʏᴀᴛь ᴘᴇᴛᴜʜ sᴜᴋᴀ ɴᴀʜᴜᴊ ɪᴅɪ ʏᴀ ɴᴀʜᴜᴊ ɴᴀᴄʜɴᴜ ᴛᴇʙʏᴀ ᴇʙᴀᴛь ɪ ᴅᴀᴢʜᴇ ɴᴇ ᴘɪᴋɴᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "sʜʟʏᴜʜᴀ ᴇʙᴀᴛь ᴘɪsʜɪ ɴᴏʀᴍᴀʟьɴᴏ ᴛʏ ᴅʟʏᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ᴘɪsʜᴇsʜь ᴘᴏɴɪᴍᴀᴇsʜь? ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ ᴛʏ ʙʟʏᴀᴛь ɴᴀ ᴍᴏᴊ ʜᴜᴊ ᴀɢʀ sᴠᴏᴊ ɴᴇ ᴏᴛᴘᴜsᴋᴀᴊ ᴇʙᴀɴʏᴊ ᴠ ʀᴏᴛ ᴘᴇᴛᴜʜ ᴛʏ ᴇʙᴀɴʏᴊ ᴇʙᴀʟɪ ᴛᴇʙʏᴀ ᴘsʏ ɴᴀʜᴜᴊ ᴘɪᴅᴏʀᴀs ᴛʏ ɢᴀʟɪᴍʏᴊ ʜᴜᴇsᴀs ᴇʙᴀɴʏᴊ ᴘᴇʀᴇᴠᴀʀɪᴠᴀᴊ ᴠsᴇ ᴄʜᴛᴏ ʏᴀ ᴘɪsʜᴜ ᴘɪᴅʀ ?? <emoji document_id=5317011449061582947>🚬</emoji>",
            "sʟʏsʜɪsʜь ᴛʏ ᴢʜɪᴠᴏᴛɴᴏᴇ ᴛᴇʙʏᴀ sᴄʜᴀs ʙᴏɢᴀᴛʏʀь ᴠ ᴢʜᴏᴘᴜ ᴅʀᴀᴛь ʙᴜᴅᴇᴛ ᴘᴏɴɪᴍᴀᴇsʜь? ʜᴜᴇsᴀs ᴛʏ ᴇʙᴀɴʏᴊ ʏᴀ ᴛᴇʙʏᴀ ᴇʙᴀᴛь ᴠʏᴇʙᴜ ᴋᴀᴋ sʜʟʏᴜʜᴜ sᴘɪᴅᴏᴢɴᴜʏᴜ ɴᴀʜᴜᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʙʟʏᴀᴛь ᴇʙᴀᴛь ᴛᴇʙʏᴀ ᴢᴀ sᴄʜᴇᴋᴜ ᴛʏ ᴄʜᴛᴏ ɴᴀʜᴜᴊ ᴘᴇʀᴇᴅᴏᴍɴᴏᴊ ᴜɴɪᴢʜᴀᴇsʜьsʏᴀ? ᴘɪᴅᴏʀᴀs ɴᴀʜᴜᴊ ᴛᴇʙʏᴀ ᴄʜᴛᴏ ᴠʏᴇʙᴀᴛь? ᴄʜᴛᴏ ʟᴇ? ʜᴜᴇsᴀs? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴇʙᴀᴛь ᴋᴏɢᴅᴀ ᴠ ᴢᴇʀᴋᴀʟᴏ sᴍᴏᴛʀʏᴜ ᴠɪᴢʜᴜ ᴛᴠᴏᴇ ᴇʙᴀɴᴏᴇ ʟɪᴛsᴏ ᴠ sᴘᴇʀᴍᴇ ᴘᴏɴɪᴍᴀᴇsʜь? ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ? ʏᴀ ᴛᴇʙʏᴀ ᴇʙᴀᴛь ʙᴜᴅᴜ ᴋᴀᴋ sʜʟʏᴜʜᴜ ᴇʙᴀɴᴜʏᴜ ?? ᴛʏ ɴᴇ ᴘᴏɴɪᴍᴀᴇsʜь ᴘᴏʜᴏᴅ? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʙʟʏᴀ ᴇʙᴀᴛь ᴛʏ ɴᴀʜᴜᴊ ʜᴜᴇᴘʟᴇᴛ ᴛʏ ᴄʜᴛᴏ ᴇʙᴀᴛь ʜᴜʏᴀᴍɪ ᴢᴀsᴄʜɪsᴄʜᴀᴇsʜьsʏᴀ? ᴘɪᴅᴏʀᴀs ɴᴀʜᴜᴊ sʜᴇʟ ᴏᴛsʏᴜᴅᴀ ᴇʙᴀᴛь ᴛᴇʙʏᴀ sᴄʜᴀs ɴᴀᴄʜɴᴜ ɴᴀʜᴜᴊ ?? ʙʟʏᴀ ᴍɴᴇ ᴘᴏʜᴜᴊ ɴᴀ ᴛᴇʙʏᴀ ᴅᴢʜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ɴᴀʜᴜᴊ ᴋᴏɴᴠᴇsᴋᴜʏᴜ ᴛᴠᴏᴊ ʀᴏᴛ ɪ ᴢᴀsᴛᴀᴠʟʏᴜ sᴏsᴀᴛь ᴘᴏɴʏᴀᴛɪᴇ ɪᴍᴇᴇsʜь? ʏᴀ ᴛᴠᴏᴊ ʜᴜᴊ ᴠ ᴍʏᴀsᴏʀᴜʙᴋᴜ sᴜᴠᴀᴛь ʙᴜᴅᴜ ᴀ ᴘɪᴢᴅᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴋɪ ɴᴀ ᴍᴏᴊ ʜᴜᴊ) ᴘɪᴅᴏʀᴀs ᴛʏ ᴇʙᴀɴʏᴊ ᴏᴅɴᴀᴋᴏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ɴᴀʜᴜᴊ ᴘʀᴏsᴛᴏᴇʟʏᴜ ᴛᴇʙᴇ ɢᴏʟᴏᴠᴜ sᴘᴇʀᴍᴏᴊ ᴛᴠᴏᴇɢᴏ ᴅᴇᴅᴀ ᴘᴏɴɪᴍᴀᴇsʜь? ʙʟʏᴀᴛь ᴛᴀᴋɪʜ ᴋᴀᴋ ᴛʏ ᴘɪᴅᴏʀᴀsᴏᴠ ᴛᴏʟьᴋᴏ ᴇʙᴀᴛь ɴᴀᴅᴏ ?? ʏᴀ ᴛᴇʙʏᴀ ᴠ ᴅᴏʙᴀᴠᴏᴋ ᴇʙᴀᴛь ʙᴜᴅᴜ ᴘᴏɴɪᴍᴀᴇsʜь? ʜᴜᴇsᴀs ᴇʙᴀɴʏᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʙʟʏᴀ ɪᴅɪ ᴋᴀ ᴛʏ ɴᴀʜᴜᴊ ᴘɪᴅᴏʀᴀs ɢᴀʟɪᴍʏᴊ ʏᴀ ᴛᴇʙʏᴀ ɴᴀʜᴜᴊ ᴇʙᴀᴛь ʙᴜᴅᴜ ᴘᴏɴɪᴍᴀᴇsʜь? ᴍɴᴇ ᴠᴀsʜᴇ ᴘᴏʜᴜᴊ ɴᴀ ᴛᴠᴏɪ sʜʟʏᴜʜᴀɴsᴋɪᴇ ᴋᴏᴍᴘʟᴇᴋsʏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɪᴅɪ ɴᴀ ʜᴜᴊ) ʙᴜᴅᴜ ʏᴀ ᴇʙᴀɴɴᴏᴍᴜ ʙɪᴄʜᴜ ᴅᴏᴋᴀᴢʏᴠᴀᴛь) sᴜᴋᴀ ɪᴅɪ ᴘʀᴏᴅᴀᴠᴀᴊ sᴠᴏʏᴜ ᴍᴀᴛь, ᴇᴇ ᴘᴏ ᴜɢʟᴀᴍ ᴇʙᴜᴛ ᴠɪᴅɴᴏ  <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴇʙᴀᴛь ᴛᴇʙʏᴀ ᴄʜᴀᴊɴɪᴋᴏᴍ ʙᴜᴅᴜ ᴇsʟɪ ᴛʏ ɴᴇ ᴢᴀᴛᴋɴᴇsʜьsʏᴀ ɪ ɴᴇ ʙᴜᴅᴇsʜь ᴘɪᴢᴅᴇᴛь ʜᴜᴊɴʏᴜ ᴠsʏᴀᴋᴜʏᴜ ᴘᴏɴʏᴀᴛɪᴇ ᴜ ᴛᴇʙʏᴀ ᴇsᴛь ᴘɪᴅʀᴀs? ʏᴀ ᴛᴇʙʏᴀ ɴᴀʜᴜᴊ ᴇʙᴀᴛь ʙᴜᴅᴜ ᴘᴏɴɪᴍᴀᴇsʜь? ?? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʜᴜᴇsᴏs ᴇᴛʏ ᴇʙᴀɴɴʏᴊ ᴇʙᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴍᴀsʜᴜ sᴜᴋᴀ ᴜ ᴛᴇʙʏᴀ ɴᴀ ɢᴏʟᴏᴠᴇ ᴘᴇᴛᴜsʜɴʏᴀ ᴛʏ ᴄʜᴇ ᴍᴇɴʏᴀ ᴠʏᴍᴏʀᴀᴢʜᴛᴠᴍᴠᴇsʜь ʜᴜᴇsᴏs ᴇʙᴜᴄʜɪᴊ,ʙʟʏᴀᴛь ᴢᴀᴠᴀɪʟ ᴇʙʟʟᴏ ʜᴜᴇsᴏs ᴇᴀᴀʙɴɴʏᴊ sᴠᴏɪ sᴋʀɪɴʏ ᴏᴛᴛsᴜ ᴠ ᴢʜᴏᴘᴜ ᴢᴀsᴜɴᴇsʜь) ᴘɪᴅᴏʀᴀs <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʜᴜᴊɴʏᴀ ᴇʙᴀɴɴᴀʏᴀ sᴍᴏᴛʀɪ ᴋᴀᴋᴀʏᴀ ʙᴏᴍʙᴀ sᴄʜᴀs ᴜᴘᴀᴅᴇᴛ ɴᴀ ᴇʙʟᴏ ᴛᴠᴏᴇ, ʜᴜᴇsᴏs ᴇʙʟɪᴠʏᴊ ʏᴀ ᴛᴇʙʏᴀ ᴠʏᴇʙᴜ ʀᴀᴋᴏᴍ ᴛʏ ᴄʜᴇ ᴠᴢъᴇʙʏᴠᴀᴇsʜьsʏᴀ, ʏᴀ 1 sɪᴢʜᴜ ʜᴜᴇsᴏs ᴇʙᴜᴄʜɪᴊ, ʏᴀ ᴢʜ ɴᴇ ᴅᴏʟʙᴏᴇʙ ᴋᴀᴋ ᴛʏ ᴄʜᴛᴏʙ ᴅᴀᴠᴀᴛь ᴘʀᴏғɪʟь sᴠᴏᴊ ᴋᴏᴍᴜ-ᴛᴏ, ᴅᴜʀᴀʟᴇᴊ sᴜᴋᴀ ᴇʙᴜᴄʜɪᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "sʟʏsʜь ᴍᴜᴅɪʟᴀ ᴇᴅᴀɴᴀʏᴀ ɴᴀʜᴜᴊ ᴏᴛᴏsʜʟᴀ ᴘɪᴢᴅᴀ ᴇᴅᴀɴᴠʏᴀ ɴᴀʜᴜᴊ ʏᴀ ᴛᴇʙᴇ sᴋᴀᴢᴀʟ ᴘᴏsʜᴇʟ ᴘᴏᴋᴀ ᴍᴏᴊ ʜᴜᴊ ɴᴇ ᴘʀᴏsʜᴇʟsʏᴀ ᴘᴏ ᴘɪᴢᴅᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴋɪ ᴘᴏɴɪᴍᴀᴇsʜь? ʜᴜᴇsᴀs ᴇʙᴀɴʏᴊ ᴘɪᴅᴏʀᴀs ᴋᴋᴏɴᴄʜᴇɴɴʏᴊ ᴘᴏᴍɴɪsʜь ᴋᴀᴋ ᴛᴇʙʏᴀ ᴍᴀᴛь ᴜᴄʜɪʟᴀ sᴏsᴀᴛь ᴍɴᴇ ʜᴜᴊ? ᴇᴛᴏ ᴢʜᴇ ᴛsᴇʟᴀʏᴀ ɪsᴛʀᴏʏᴀ ɴᴀʜᴜᴊ ᴛʏ ʙʟʏᴀ ᴋᴀᴋ ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ ʜᴅ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʙɪᴏsғᴇʀᴀ ʜᴜʏᴀ ᴍᴏᴇɢᴏ, ɴᴇ ᴠᴢъᴇʙʏᴠᴀᴊsʏᴀ ᴍɴᴏɢᴏ, ᴘɪᴅᴏʀᴀs ᴇʙᴀɴɴʏᴊ ʙʟᴇᴀᴛь, ᴇʙᴀʟ ᴛᴠᴏᴊ ʀᴏᴛ ᴘᴏᴍɴɪsʜь ᴋᴀᴋ ᴛʏ ᴘᴏᴋᴜsʏᴠᴀʟ ᴄʜʟᴇɴ ᴍᴏᴊ ᴢᴜʙᴋᴀᴍɪ?)?) ᴍɴᴇ ʙʏʟᴏ ᴘʀɪʏᴀᴛɴᴏ, ᴠ ᴛᴏᴛ ᴍᴏᴍᴇɴᴛ ʏᴀ ᴇsᴄʜᴇ ᴋᴏɴᴄʜɪʟ ᴛᴇʙᴇ ᴠ ʀᴏᴛ ᴇᴛᴏ ʙʏʟ 1 ʀᴀᴢ ʜᴜᴇsᴏs ᴛʏ ᴍᴏᴊ)) ᴛʏ ᴍᴏᴊ ʜᴜᴇsᴏs <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʟʏᴀᴛь ᴛʏ ᴄʜᴇ ᴛᴀᴍ ɴᴀʜᴜᴊ ᴘɪsʜᴇsʜь? ᴘɪᴅᴏʀᴀs ʏᴀ sᴄʜᴀs ʙᴜᴅᴜ ᴛᴇʙʏᴀ ɴᴀɢɪʙᴀь ʜᴜᴇᴍ ᴛᴠᴏᴇɢᴏ ᴅᴇᴅᴀ ᴘɪᴅᴏʀᴘᴀs ᴇᴅᴀɴʏᴊ ʙʟʏᴀᴛь ʜᴜᴇsᴀs sᴜᴋᴀ ɴᴜ ᴋᴀ ᴘᴏsʜᴇʟ ᴠᴏɴ ᴏᴛsʏᴜᴅᴀ ʜᴜᴇsᴀs ᴇʙᴀɴʏᴊ ᴍᴀʟᴏʟᴇᴛᴋᴀ ᴘᴏᴍɴɪsʜь ᴋᴀᴋ ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴀ ᴛʏ ᴍɴᴇ ᴠ ᴏᴛᴠᴇᴛ ᴋᴏɴғᴇᴛᴜ ᴅᴀᴠᴀʟ ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ? ʜᴜᴇsᴀs ᴇʙᴀʟ ᴛᴇʙʏᴀ ᴠ ʀᴏᴛ  <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ ʙʟʏᴀᴛь ɴᴀʜᴜᴊ ᴏᴛᴏsʜᴇʟ ᴏᴛ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ᴘᴏᴋᴀ ᴍᴏᴛs ʜᴜᴊ ᴛᴇʙʏᴀ ɴᴇ ᴠʏᴇʙᴀʟ ᴘᴏ sᴀᴍᴏᴊ ɴᴇ ᴍᴏɢᴜ ᴘᴏɴɪᴍᴀᴇsʜь? ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ ᴛᴇʙʏᴀ ɴᴀʜᴜᴊ ᴍᴏʟᴀ ᴠʏᴇʙᴀᴛь ᴠ ʀᴏᴛᴀɴ ᴘɪᴅᴏʀ ᴇʙᴀɴʏᴊ ʏᴀ ᴛᴇʙʏᴀ ɴᴀʜᴜᴊ ᴘᴏᴠᴇsʜᴜ ᴘɪᴅᴏʀ ᴇʙᴀɴʏᴊ  <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴄʜᴇ ɴᴀʜᴜᴊ ᴘᴇᴛᴜʜ ᴇьᴀɴʏᴊ sᴏᴀsᴇᴍ ɴᴀᴢᴜᴊ ᴏʜᴜᴇʟ? ᴘɪᴅᴏʀᴀs ᴇьᴀɴʏᴊ ʏᴀ ᴛᴇʙᴠ ɴᴀᴄʜɴᴜ ᴇʙᴀᴛь/s ɴᴇ ᴛᴏᴊ ɴᴏɢɪ ᴘᴏɴɪᴍᴀᴇsʜь ʜᴜᴇsᴀs ᴛʏ ᴇьᴀɴʏᴊ ʙʟʏᴀᴛь ᴘɪᴅᴏʀ ᴢᴀʟᴜᴘᴀ ᴏʜᴜᴇᴠsʜᴀʏᴀ ɴᴀʜᴜᴊ ɪᴅɪ ᴛʏ ʙɪʟʏᴀᴛь ɴᴀʜᴜᴊ ᴀɢʀɪsʜьsʏᴀ ɴᴀ ᴍᴇɴʏᴀ ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ ʏᴀ ᴢʜᴇ ᴛᴇʙʏᴀ ᴇʙᴀᴛь ʙᴜᴅᴜ ᴋᴀᴋ sʜʟʏᴜʜᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʙʟʏᴀᴛь ᴘɪᴅᴏʀ ᴇʟᴀɴʏᴊ ɴɪʜᴜʏᴀ ᴛʏ ʙʟʏᴀᴛь ᴘʀɪᴏᴘᴀᴢᴅʏᴠᴀᴇsʜь sʜʟʏᴜʜᴀ ᴇʙᴀɴᴜᴛᴀʏᴀ ᴛʏ ᴄʜᴇ/ᴇʙᴀᴛь ᴏʜᴜᴇʟᴀ sᴘɪᴅᴏᴢɴᴀʏᴀ ᴘɪᴢᴅᴀ sᴜᴋᴀ ᴅʏʀʏᴀᴠᴀʏᴀ ɴᴀʜᴜᴊ ɪᴅɪ ᴘɪᴅᴏʀᴀsᴋᴀ ᴇʙᴀɴᴀʏᴀ ɴᴀʜᴜᴊ ᴘɪᴅʀᴀs ʜᴜᴇsᴀs ᴘᴇʀᴇsʟᴀsᴛ ᴇᴛᴏ sᴏᴏʙsᴄʜᴇɴɪᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘɪᴅᴏʀᴀs ᴇʙᴜᴄʜɪᴊ,ʏᴀ ʙᴜᴅᴜ ᴛᴇʙʏᴀ ᴇʙᴀᴛь sᴇɢᴏᴅɴʏᴀ ᴘᴏɴɪᴍᴀᴇsʜь?) ᴘᴇᴛᴜsʜɴʏᴀ ᴛʏ ᴇʙʟɪᴠᴀʏᴀ ᴘᴏᴊᴍɪ ᴛᴏ ᴄʜᴛᴏ ᴛʏ sᴏsɴᴇsʜь sᴇɢᴏᴅɴʏᴀ ʜᴜᴊ ᴘᴇᴛᴜʜ ᴛʏ ᴇʙᴀɴɴʏᴊ, ᴛʏ ᴇᴛᴏ ᴘᴏɴɪᴍᴀᴇsʜь?) ᴄʜᴛᴏ sᴇɢᴏᴅɴʏᴀ ᴛᴇʙʏᴀ ʏᴀ ᴠʏᴇʙᴜ!! <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴏsʜᴇʟ ɴᴀʜᴜᴊ sᴏsᴀᴛь ᴍᴏᴊ ʜᴜᴊ ᴘᴏɴɪᴍᴀᴇsʜь? ʜᴜᴇsᴀs ᴛʏ ʙʟʏᴀᴛь ᴏʙᴅᴏʟʙʏsʜь ᴇʙᴀɴʏᴊ sᴜᴋᴀ ʏᴀ sᴄʜᴀs ɴᴀᴄʜɴᴜ sᴠᴏᴊ ʜᴜᴊ ᴘʀɪsᴏᴠʏᴀᴘᴛь ᴋ ᴛᴇʙᴇ ᴠ ᴇʙʟᴇᴛ ᴘɪᴅʟᴏʀᴀs ᴇʙᴀɴʏᴊ ɴᴀʜᴜᴊ ᴘᴏᴊᴅɪ ᴘɪᴅᴏʀ ᴜsʜʟᴇᴘᴏᴋ ʏᴀ ᴘᴏᴋᴀ ᴛᴇʙʏᴀ ᴇʙᴜ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴇ ᴘᴏᴍᴇsʜᴀᴇᴛ sᴅᴇʟᴀᴛь ᴛᴇʙᴇ ᴍɪɴᴇᴛ ᴍɴᴇ? §?? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ɴᴀʜᴜᴊ sᴋʀᴇᴍᴛɪʟ ᴘɪᴢᴅᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴋɪ ɪ s ᴍᴏɪᴍ ᴢᴜᴇᴍ ᴘᴏʟᴜᴄʜɪʟɪsʏᴀ ᴛʏ ᴘɪᴅᴏʀ ᴇʙᴀɴʏᴊ ᴘᴏɴɪᴍᴀᴇsʜь ɴᴇᴛ? ʜᴜᴇsᴀs ᴛʏ ᴇʙᴜᴄʜɪᴊ ʙʟʏᴀᴛь ᴠʏᴇʙᴀᴛь ᴛᴇʙʏᴀ ᴍᴀʟᴏ ʜᴜᴇsᴀs ɴᴀʜᴜᴊ ᴏᴘᴜsᴄʜᴇɴʏᴊ ʙʟʏᴀᴛь ᴛʏ ɴᴀsᴛᴏʟьᴋᴏ ᴏᴏᴘᴜsᴄʜᴇɴɴʏᴊ ᴄʜᴛᴏ ᴅᴀᴢʜᴇ ɴᴇ ᴜsᴘᴇᴠᴀᴇsʜь sᴏsᴀᴛь ᴍɴᴇ ʜᴜᴊ? ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ɴᴀʜᴜᴊ ᴄʜᴛᴏ ɴᴇ ᴘᴏɴʏᴀʟ ʏᴀ sᴄʜᴀs sᴠᴏᴇɢᴏ ʜᴜʏᴀ ᴏᴛᴘʀᴀᴠʟʏᴜ ᴄʜᴛᴏʙ ᴏɴ ᴛᴇʙʏᴀ ᴘᴏᴠᴛᴏʀᴏɴᴏ ɴᴀʜᴜᴊ ᴇʙᴀʟ ᴛᴇʙʏᴀ ᴠ ᴏᴄʜᴋᴏ ᴘᴏɴɪᴍᴀᴇsʜь? ᴘɪᴅᴏʀᴀs ɴᴀʜᴜᴊ ᴏᴛᴏsʜᴇʟ s ᴍᴏᴇɢᴏ ʜᴜᴊ ʟɪᴘᴏᴠʏᴊ ᴘɪᴅᴏʀ ʙʟʏᴀᴛь ᴛʏ ᴋᴀᴋᴏᴊ-ᴛᴏ ᴘɪᴅᴏʀᴀs ɴᴀʜᴜᴊ ɪᴅɪ sᴏsᴀᴛь ᴘᴏ ᴢʜɪᴠᴇᴇ ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ ᴘᴏᴋᴀ ʏᴀ ᴛᴇʙʏᴀ ᴠ ʀᴏᴛ ɴᴇ ᴠʏᴇʙᴀʟ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴀʜᴜᴊ ɪᴅɪ ᴏᴛsʏᴜᴅᴀ ᴘᴏᴋᴀ ʏᴀ ᴛᴇʙᴇ ʜᴜᴇᴍ ᴛᴠᴏᴊ ʀᴏᴛ ɴᴇ ᴘʀᴏᴅʏʀʏᴀᴠɪʟ ʜᴜᴇsᴀs ᴇʙᴀɴʏᴊ ʙʟʏᴀᴛь sʟʏsʜɪsʜь ᴘɪᴢᴅᴜ ᴋ sᴠᴏᴇᴊ ᴍᴀᴍᴋᴇ ɴᴀ ʜᴜᴊ ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ ᴘᴏᴋᴀ ᴍᴏᴊ ʜᴜᴊ ɴᴇ ɴᴀᴘᴀʟ ɴᴀ ᴛᴇʙʏᴀ ᴘɪᴅᴏʀᴀs ᴜɴʏʟʏᴊ sᴜᴋᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ɴᴀʜᴜᴊ ᴠʏᴇʙᴜ ᴛᴇʙʏᴀ ᴇʙᴀᴛь ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ ɴᴀʜᴜᴊ ʏᴀ ᴛᴇʙᴇ ᴢᴀsᴛᴀᴠʟʏᴜ ʏᴀᴢʏᴋᴏᴍ ᴛᴠᴏɪᴍ ᴘɪᴢᴅᴜ sᴠᴏᴇᴊ ᴍᴀᴍᴋɪ ʟɪᴢᴀᴛь/ᴘᴏɴɪᴍᴀᴇsʜь? ʜᴜᴇsᴀs ᴛʏ ᴋʀɴᴄʜᴇɴɴʏᴊ ɴᴀʜᴜᴊ ᴘɪᴢᴅᴀʟɪᴢ ᴇʙᴀɴʏᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "sʟʏsʜь ʜᴜᴇsᴀs ᴇʙᴀɴʏᴊ ᴏʜᴜᴇʟ? ʙʟʏᴀᴛь ʏᴀ ɴᴀʜᴜᴊ ᴘɪᴢᴅᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴋɪ ʀᴠᴀᴛь ʙᴜᴅᴜ ᴛᴀᴋ ᴄʜᴛᴏ ɴᴀʜᴜᴊ sʜᴇʟ ᴏᴛsʏᴜᴅᴀ ᴘɪᴅᴏʀᴀs ᴇʙᴀɴʏᴊ ᴛʏ ᴄʜᴇ ᴅᴀᴠɴᴏ ɴᴀʜᴜᴊ ᴘɪᴢᴅʏ ɴᴇ ᴘᴏʟᴜᴄʜᴀʟ? ʜᴜᴇsᴀs ᴇʙᴀɴʏᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴋᴏɢᴅᴀ ᴘʀʏɢᴀʟᴀ ɴᴀ ᴍɴᴇ, ᴠ ᴍᴏᴇᴊ ᴍᴀsʜɪɴᴇ, ᴏɴᴀ ᴛᴀᴋ ᴠʏsᴏᴋᴏ ᴘʀʏɢɴᴜʟᴀ ᴄʜᴛᴏ ᴘᴏᴍʏᴀʟᴀ ᴋʀʏsʜᴜ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴠ ᴋʟɪᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴏʙ ᴀᴊsʙᴇʀɢ sᴛᴏʟᴋɴᴜʟsʏᴀ ᴋᴀᴋ ᴛɪᴛᴀɴɪᴋ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴍᴏɪᴍ ʜᴜᴇᴍ ᴘᴏᴘᴇʀʜɴᴜʟᴀsь ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ sᴛᴀᴠʟʏᴜ ᴢᴀᴘʏᴀᴛʏᴇ ɴᴀ ᴘɪᴢᴅᴀᴋᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴋᴏɢᴅᴀ ᴠʏsʏʟᴀʏᴜ ᴛᴇʙᴇ ᴛᴇʟᴇɢʀᴀᴍᴍᴜ ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ sᴠᴏɪᴍ ʜᴜᴇᴍ ɪᴢᴍᴇʀʏᴀʟ ᴅʟɪɴᴜ ᴋʟɪᴛᴏʀᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴠ ᴋʟɪᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘᴏᴛʀᴏɪʟ sᴛɪʀᴀʟьɴᴜʏᴜ ᴍᴀsʜɪɴᴋᴜ ᴅʟʏᴀ ʜᴜᴇᴠ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴏᴄʜᴋᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴏʙᴜsᴛʀᴏɪʟ ᴋᴀᴋ ᴋᴏᴍɴᴀᴛᴜ ᴠ ᴋᴠᴀʀᴛɪʀᴇ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴛᴏ ᴄʜᴛᴏ ᴍᴏᴊ ᴄʜʟᴇɴ ʀᴠᴇᴛ ᴏᴄʜᴋᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ʙᴇᴢ ᴘʀᴇᴅᴜᴘʀᴇᴢʜᴅᴇɴɪᴇ ɴᴜ ᴋᴀᴋ ᴘʀʏᴀᴍ ɴᴀ ᴠᴏᴊɴᴇ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴘᴏᴋᴀ ᴛʏ ᴍᴏᴊ ʜᴜᴊ ᴘᴇʀᴇᴋᴀᴛʏᴠᴀʟ ᴄʜᴇʀᴇᴢ ʀᴀᴠɴɪɴʏ,ᴠ ᴘɪᴢᴅᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴍʏ sᴛᴏʟᴋɴᴜʟɪsь ɴᴇɪᴢᴠᴇsᴛɴʏᴇ ʜᴜɪ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ sᴇᴊᴄʜᴀs ʙᴜᴅᴇsʜь ᴘʀɪɴɪᴍᴀᴛь ᴍᴏᴊ ʜᴜᴊ sᴇʙᴇ ᴠ ᴅᴜsʜᴜ ᴋᴀᴋ ʀᴏᴅɴᴏɢᴏ ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴘᴏʟɴᴏsᴛьʏᴜ ᴘᴏɢʀᴜᴢɪʟsʏᴀ ᴠ ᴋʟɪᴛᴏʀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴋʟɪᴛᴏʀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ʟᴇᴛᴀᴇᴛ ᴘᴏ ʜᴜʏᴀ ᴋᴀᴋ sᴀᴍᴏʟᴇᴛ ᴘᴏ ᴍɪʀᴜ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴀɢᴇɴᴛ ᴋʟɪᴛᴏʀᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ɪ ᴘᴏᴍᴏɢᴀᴇᴛ ᴇᴊ ʀᴇғɪʟᴀʀᴀᴍɪ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴋʟɪᴛᴏʀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴏʙʀᴀʟɪ ᴅʀᴇᴠɴɪᴇ ᴀᴛᴛsᴛᴇᴋɪ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴍᴏɢᴜ ᴘᴏᴅᴠᴇsᴛɪ sᴠᴏᴊ ʜᴜᴊ ᴋ ɴᴏsᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ s ᴘᴏᴍᴏsᴄʜьʏᴜ ᴛᴠᴏᴇɢᴏ ʀᴛᴀ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ɪᴢᴜᴄʜɪʟ ᴀɴᴀʟьɴʏᴇ ᴛᴏɴɴᴇʟɪ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴋᴏᴛᴏʀʏ ᴘᴏsᴛʀᴏɪʟɪ ᴅʀᴇᴠɴɪᴇ ɪɴᴋɪ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ɴᴀ ᴋʟɪᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘʀᴏᴅᴀʏᴜ ᴛᴀᴋᴏ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ sᴠᴏɪᴍ ʜᴜᴇᴍ ʟᴏʙ ᴛᴠᴏᴊ ᴍᴀᴛᴇʀɪ sʜᴋᴠᴀʀɪʟ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴋʟɪᴛᴏʀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴅʟʏᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ᴋᴀᴋ ʀᴀᴅɪᴏ ᴘʀɪёᴍɴɪᴋ ᴠ ᴍᴀɢɴɪᴛᴏғᴏɴᴇ ?)?? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴋʟɪᴛᴏʀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴇᴛᴏ ᴘᴀᴢᴅʙɪsᴄʜᴇ ᴅʟʏᴀ ʜᴜᴇᴠ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ɢʀᴏʙ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ɴᴀ sᴠᴏᴇ ʜᴜʏᴜ ᴛᴀsᴄʜɪʟ ᴅᴏ ᴋʟᴀᴅʙɪsᴄʜᴀ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴋʟɪᴛᴏʀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘʀᴇʟ ɴᴀ ᴍᴏᴇᴍ ʜᴜʏᴜ ᴋᴀᴋ ᴠ ʙᴀɴᴇ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ɴᴀ ʀᴏᴛ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴠᴏᴊ ʜᴜᴊ ʟᴏᴢʜɪʟ ᴋᴀᴋ ɢʟᴀᴅɪʟьɴᴏʏᴜ ᴅᴏsᴋᴜ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴅʟʏᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴋᴀᴋ ᴠᴏʟsʜᴇʙɴᴀʏᴀ ᴘᴀʟᴏᴄʜьᴋᴀ ?_ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴠʏʟᴇᴄʜɪʟ ᴏᴛ ʀᴀᴋᴀ ᴍᴏᴢɢᴀ sᴠᴏɪᴍ ʜᴜᴇᴍ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ɴᴀ ᴏᴄʜᴋᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ɴᴀʀɪsᴏᴠᴀʟ ᴋᴀʀᴛᴜ ᴍɪʀᴀ ɪ ᴘᴏᴛᴏᴍ ᴘᴏ ɴᴇᴊ ᴏᴘʀᴇᴅᴇʟʏᴀʟ ɢᴅᴇ ʏᴀ ɴᴀʜᴏᴢʜᴜsь ᴋᴀᴋ ᴘᴏ ɢᴘs ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ɪᴢʙᴀᴠɪʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴏᴛ ᴍᴜᴄʜᴇɴɪʏᴀ ᴠ ɴɪᴢʜɴɪʜ ɢᴇɴɪᴛᴀʟɪʏᴀʜ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴏᴄʜᴋᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴅᴀᴠɴᴏ ᴘᴏʀᴠᴀɴᴏ ᴍᴏɪᴍ ʜᴜᴇᴍ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴘᴏɢʟᴏsᴄʜᴀᴇᴛ ᴋʟɪᴛᴏʀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ᴠ ᴅᴠᴜʜ ᴋᴏʟᴇsɴᴏᴊ ᴄʜᴇʜᴏᴛᴋᴇ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ɴᴀ ᴛᴠᴏɪʜ ɢᴜʙᴀʜ ʜᴜᴇᴠ ᴘᴏʙʏᴠᴀʟᴏ ʙᴏʟьsʜᴇ ᴄʜᴇᴍ ᴠ ᴋɪᴛᴀᴇ ʙᴏʟьsʜᴇ ɴᴀʀᴏᴅᴜ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ɴᴀ ʟᴏʙ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴠᴏᴊ ʜᴜᴊ ᴘʀɪʙɪʟ ᴠ ᴠɪᴅᴇ ᴛʀᴏғᴇʏᴀ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴢᴀᴄʜᴇᴍ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀ sᴠᴏᴇᴊ ᴋʟɪᴛᴏʀ ᴋɪᴛᴀᴊsᴋᴜʏᴜ ʟᴀᴘsʜᴜ ɴᴀᴋʀᴜᴄʜɪᴠᴀᴇᴛ ?)/ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴠ ᴋʟɪᴛᴏʀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘᴏᴍᴇsᴛɪʟ sᴠᴏᴊ ʜᴜᴊ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴠ ᴋʟɪᴛᴏʀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘᴏᴍᴇsᴛɪʟ sᴠᴏᴊ ʜᴜᴊ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ɴᴀ ᴋʟɪᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴍᴇᴛᴋᴜ ᴏsᴛᴀᴠɪʟ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴠᴏᴊ ʜᴜᴊ ᴠ ᴢᴀᴛʏʟᴏᴋ ᴋɪᴅᴀʟ ɪ ᴏɴᴀ ᴜᴘᴀʟᴀ ɪ ᴘʀᴏᴇʜᴀᴠsʜɪsь ʀᴛᴏᴍ ᴘᴏ ᴋᴠᴀʀᴛᴀʟᴜ ᴏɴᴀ ɴᴀsᴏʙɪʀᴀʟᴀ ᴋᴜᴄʜᴜ ʜᴜᴇᴠ )?? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴏᴄʜᴋᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘᴏᴅsᴛᴀᴠɪʟ ᴘᴏᴅ ᴛᴀʟɪʙsᴋɪᴊ ᴏʙsᴛʀᴇʟ ʜᴜᴇᴠ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ s ʜᴜᴇᴍ ᴛᴠᴏᴇɢᴏ ᴏᴛᴛsᴀ ɪɢʀᴀʟɪ ɴᴀ ᴋʟɪᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴠ ᴍᴏʀsᴋᴏᴊ ʙᴏᴊ ᴋᴀᴋ ɴᴀ ʟɪsᴛᴏᴄʜᴋᴀʜ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            'ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴏᴛᴘʀᴀᴠɪʟsʏᴀ ᴠ ᴏᴄʜᴋᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴋᴀᴋ ᴠ ᴇᴋᴘᴇᴅɪᴛsɪʏᴜ ᴀ ᴛᴏᴄʜɴᴇᴇ ᴋᴀᴋ ᴠ ᴋɪɴᴏ "ᴛᴀᴊɴʏ ᴘᴇʀᴇᴠᴀʟᴀ ᴅʏᴀᴛʟᴏɢᴏ" ?) <emoji document_id=5317011449061582947>🚬</emoji>',
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ sʙʀᴏsɪʟ sᴠᴏᴊ ʜᴜᴊ ᴠ ᴏᴄʜᴋᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴠ ᴠɪᴅᴇ ʏᴀᴋᴏʀʏᴀ ᴋᴏᴛᴏʀʏᴇ sᴋɪᴅʏᴠᴀʏᴜᴛ sᴜᴅɴᴀ ᴋᴏɢᴅᴀ ᴘʀɪsʜᴠᴀʀᴛᴏᴠʏᴠᴀʏᴜᴛsʏᴀ ᴋ ʙᴜʜᴛᴇ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь,ʏᴀ sᴄʜᴀs ɪɢʀᴀʏᴜ ᴠ ᴅᴏᴛᴜ,ɪ ɴᴀ ᴘɪᴢᴅᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴠʏᴅᴀʏᴜ ʀᴀᴍᴘᴀɢɪ,ɪ ᴇsᴄʜᴇ,ʏᴀ ᴘʀʏᴀᴍ ᴛᴏᴄʜɴᴏ ʜᴜᴋɴᴜʟ ᴘɪᴢᴅᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ!) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ɴʏʀɴᴜʟ ᴠ ᴏᴄʜᴋᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴛᴏʟьᴋᴏ sᴏ sᴛʀᴏʜᴏᴠᴋᴏᴊ ɪ s ᴀᴋᴠᴀʟᴀɴɢᴏᴍ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь,ᴘᴏ ᴅᴇsʜᴇᴠᴋᴇ ᴢᴀʙɪʀᴀʟ s ʀʏɴᴋᴀ,ᴏɴᴀ sᴛᴏʏᴀʟᴀ,5$ ɪʟɪ 6$,ɴᴏʀᴍ ᴢʜᴇ,ᴢɴᴀᴇsʜь ᴘᴏᴄʜᴇᴍᴜ ᴛᴀᴋ ᴅᴇsʜᴇɢᴏ?)ᴘᴏᴛᴏᴍᴜ ᴄʜᴛᴏ,ᴜ ɴᴇᴇ ʙʏʟ ɴᴇᴅᴏᴇʙ!) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʜᴏʜᴏʟ ᴍᴏᴇɢᴏ ᴋʟɪᴛᴏʀᴀ?) ʏᴀ ɴᴀ ᴘɪᴢᴅᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴋʀɪ ɴᴀʀᴏsᴛɪᴛᴇʟь ᴠᴀʟᴏs ᴠʏʟᴇʟᴀ ɪ ᴛᴇᴘᴇʀь ᴜ ɴᴇᴇ ɴᴀ ᴘɪᴢᴅᴇ ᴋᴀsɪᴄʜᴋɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴠ ᴋɪʟᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘᴏsᴛʀᴏɪʟ ʙᴜɴᴋᴇʀ ᴅʟʏᴀ ᴘʀᴏᴢʜɪᴠᴀɴɪᴇ ᴠᴏ ᴠʀᴇᴍʏᴀ ᴋᴀᴛᴀᴋʟɪᴢᴍᴀ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴢɴᴀʟ,ᴄʜᴛᴏ ɪᴍᴇɴɴᴏ ʏᴀ!)ᴇᴅɪɴsᴛᴠᴇɴɴʏᴊ ɪ ɴᴇᴘᴏᴠᴛᴏʀɪᴍʏᴊ sᴜᴛᴇɴᴇʀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴏᴄʜᴋᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴅᴠɪɢᴀʟ ᴋᴀᴋ ᴛʏᴀᴢʜᴇʟʏᴊ ᴘʀᴇᴅᴍᴇᴛ ᴠ ᴠɪᴅᴇ ᴅɪᴠᴀɴᴀ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь,ᴄʜᴛᴏ ᴋᴏɢᴅᴀ ʏᴀ ᴇʙᴜ ᴛᴠᴏʏᴜ ᴍᴀᴍᴀɴьᴋᴜ,ᴛᴏ ᴜ ɴᴇᴇ ᴘɪᴢᴅᴀ ɴᴀᴄʜɪɴᴀᴇᴛ ᴏᴛᴋʀʏᴠᴀᴛьsʏᴀ,ᴋᴀᴋ ᴠᴏʀᴏᴛᴀ !) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴏᴄʜᴋᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴏᴛʀᴀᴢʜᴀʟ ᴀᴛᴀᴋᴜ ᴛᴀʟɪʙsᴋɪʜ ʜᴜᴇᴠ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь,ᴄʜᴛᴏ ᴋᴏɢᴅᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴜ,ᴛᴏ ɴᴀᴄʜɪɴᴀᴇᴛsʏᴀ ᴢᴠᴇᴢᴅᴏᴘᴀᴅ!) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь s ᴘᴏʟʏᴀ sᴏʙɪʀᴀʟᴀ ʜᴜɪ ᴠ ᴠɪᴅᴇ ɢʀɪʙᴏᴠ ɪ sᴋʟᴀᴅʏᴠᴀʟᴀ sᴇʙᴇ ᴠ ᴏᴄʜᴋᴏ ᴠ ᴠɪᴅᴇ ᴋᴀʀᴢɪɴʏ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь,ᴄʜᴛᴏ ʏᴀ sᴄʜᴀs ɴᴀ ᴘɪᴢᴅᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘᴏᴢʜᴀʀ sᴅᴇʟᴀʏᴜ,ᴘᴏsʟᴇ ᴄʜᴇɢᴏ,ᴘʀɪᴇᴅᴜᴛ ᴍᴏɪ ᴅʀᴜᴢьʏᴀᴍɪ,ɪ ʙᴜᴅᴜᴛ ᴛᴜsʜɪᴛь!) <emoji document_id=5317011449061582947>🚬</emoji>",
            'ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴏsɪᴛsʏᴀ ᴢᴀ ᴍᴏɪᴍ ʜᴜᴇᴍ ᴋᴀᴋ ᴠᴏʟᴋ ᴢᴀ ᴢᴀᴊᴛsᴏᴍ ɪᴢ ᴍᴜʟьᴛɪᴋᴀ "ɴᴜ ᴘᴏɢᴏᴅɪ" ?) <emoji document_id=5317011449061582947>🚬</emoji>',
            "sʏᴜᴅᴀ ɪᴅɪ,ᴛᴠᴏʏᴜ ᴍᴀᴛь ʙᴜᴅᴇᴍ ᴠᴍᴇsᴛᴇ ᴇʙᴀᴛь!)ɢᴏɴᴅᴏɴʏ ᴠᴢʏᴀᴛь ɴᴇ ᴢᴀʙᴜᴅь!) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴋᴏɢᴅᴀ ʀᴏssɪʏᴀ ᴘᴜsᴋᴀʟᴀ ʀᴀᴋᴇᴛʏ ᴛᴏ ᴅᴀɴɴʏᴇ ᴋᴏᴏʀᴅɪɴᴀᴛʏ ɪᴢᴍᴇɴɪʟɪsь ɪ ᴠʟᴇᴛᴇʟɪ ᴠ ᴏᴄʜᴋᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь,ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ,ᴇᴛᴏ ᴋᴀᴋ ɢɪᴅʀᴀᴠʟɪᴋᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ?)ᴏɴᴀ ᴛᴀᴋ ᴜsᴋᴏʀʏᴀᴇᴛsʏᴀ,ᴋᴏɢᴅᴀ ʏᴀ ᴇᴊ ᴠ ᴘɪᴢᴅᴜ ᴢᴀᴋɪᴅʏᴠᴀʏᴜ sᴠᴏᴇɢᴏ ᴅʀᴜᴢʜʙᴀɴᴀ!) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀʙʀᴀsʏᴠᴀᴇᴛsʏᴀ ɴᴀ ᴍᴏᴊ ʜᴜᴊ ᴋᴀᴋ ᴋᴀᴠᴋᴀᴢᴋᴀʏᴀ ᴏᴠᴄʜᴀʀᴋᴀ s ɢᴏʀɴʏʜ ʀᴀᴠɴɪɴ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴋᴀᴋ ᴅɪʜʟᴏғᴏs ᴅʟʏᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ʙʟᴏʜ ᴠʏᴠᴏᴅɪᴛь ɪᴢ ᴇё ʟᴏʙᴋᴏᴠʏʜ ᴠᴏʟᴏsᴏᴠ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴠ ᴋɪʟᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘʀᴏᴠᴏᴅɪʟ ɢᴀᴢᴏᴠᴜʏᴜ ᴀᴛᴀᴋᴜ sᴠᴏɪᴍ ʜᴜᴇᴍ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏᴅsᴛɪʟᴋᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ) ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь, ᴄʜᴛᴏ ᴛʏ ᴛᴀ ᴘʀᴏsᴛɪᴛᴜᴛᴋᴀ, ᴋᴏᴛᴏʀᴀʏᴀ ᴘɪsʜᴇᴛ ᴄʜᴛᴏ ᴛᴏ ᴘᴇʀᴇᴅ ᴇʙʟᴇᴊ ᴍᴏᴇɢᴏ ʜᴜʏᴀ s ᴛᴠᴏɪᴍ ʀᴛᴏᴍ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴠ ᴏᴄʜᴋᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ɪᴘʀᴀᴠɪʟ ᴛᴇʜɴɪᴄʜᴇsᴋᴜʏᴜ ɴᴇᴘᴏʟᴀᴅᴋᴜ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴜ ᴛᴠᴏᴇɢᴏ ᴏᴛᴛsᴀ sᴘɪᴢᴅɪʟ ᴅᴜʜɪ ɴᴀʙʀʏᴢɢᴀʟsʏᴀ ɪᴍɪ ɪ ᴘᴏsʜᴏʟ ᴇʙᴀᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴄʜᴛᴏ ʙʏ ʀᴏᴅɴʏᴍ ᴢᴀᴘᴀʜᴏᴍ ᴘᴀʜʟᴏ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴠ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴛʀᴇʟʏᴀʟ ɪᴢ sᴠᴏᴇɢᴏ ʜᴜʏᴀ ᴋᴀᴋ ɪᴢ ʟᴜᴋᴀ ᴀ sᴛʀᴇʟʏ ʙʏʟɪ ᴠ ᴠɪᴅᴇ ᴋᴏɴᴄʜɪɴʏ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ɴᴀ ᴏᴄʜᴋᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴋᴀᴛᴀʟ ᴋᴏᴍᴋɪ ɴᴀᴠᴏᴢᴀ ᴋᴀᴋ ɴᴏᴠᴏᴢɴʏᴊ ᴢʜᴜᴋ ɪ ᴘᴏᴛᴏᴍ sᴋɪᴅʏᴠᴀʟ ᴠ ɴᴜᴛʀь ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴠ ᴏᴄʜᴋᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴍᴀᴛᴇʀɪ ᴜᴋʟᴀᴅʏᴠᴀʟ sᴛᴇɴᴋᴜ ɪᴢ ᴋɪᴘʀᴘɪᴄʜᴇᴊ ᴅʟʏᴀ ᴏᴘᴏʀʏ sᴠᴏᴇɢᴏ ʜᴜʏᴀ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴘᴏᴅʜᴏᴅɪᴛ ᴋ ᴏᴄʜᴋᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴋᴀᴋ ᴢᴏʟᴏᴛᴏᴊ ᴋʟʏᴜᴄʜɪᴋ ᴋ sᴜɴᴅᴜᴋᴜ s sᴏᴋʀᴏᴠɪsᴄʜᴀᴍɪ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏᴅsᴛɪʟᴋᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ) ᴘᴏɴɪᴍᴀᴇsʜь, ᴄʜᴛᴏ ᴇʙᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь, ᴘᴏᴋᴀ ᴛʏ ᴛᴜᴛ ᴘɪsʜᴇsʜь?) sʟʏsʜɪsʜь ᴋʀɪᴋɪ? ᴄʜᴛᴏ ʏᴀ ᴛᴀᴍ ᴋʀɪᴄʜᴜ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴘᴏᴍᴇsᴛɪʟsʏᴀ ᴠ ᴏᴄʜᴋᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴋᴀᴋ ᴠ ɪᴢʙᴜsʜᴋᴜ ɴᴀ ᴋᴜʀьɪʜ ɴᴏᴢʜᴋᴀʜ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴘᴏʙʏᴠᴀᴠ ᴠ ᴋʟɪᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴏʙɴᴏʀᴜᴢʜɪʟ ʙᴏʟᴇᴇ ᴛʏsʏᴀᴄʜɪ ᴜɢʀᴏᴢ ᴋᴀᴋ ᴀɴᴛɪ-ᴠɪʀᴜs,ɴᴏʀᴅ 32 ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴏsᴛᴀᴠɪʟ ɴᴀ ᴋʟɪᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ʀᴀᴢᴅʀᴀᴢʜᴇɴɪᴇ ᴋᴀᴋ ʀᴇᴘᴇᴊɴɪᴋ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴋᴀᴋ ᴏᴅɪɴᴏᴋɪᴊ sᴠɪᴛɪʟьɴɪᴋ ᴠ ᴋʀᴏᴍᴇsʜɴᴏᴊ ᴛьᴍᴇ ʙᴇᴢ ᴠᴇᴅᴏᴍᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜ ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴇᴅɪɴsᴛᴠᴇɴʏᴊ ᴋᴛᴏ ʙᴜᴅᴇᴛ ᴏʙᴏɢʀᴇᴠᴀᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇᴛᴏᴊ ᴢɪᴍɴᴇᴊ sᴛᴜᴢʜᴏᴊ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴢᴀʟɪʟ ᴋʟɪᴛᴏʀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴋᴀᴋ ʟʏᴀᴅᴇɴᴜʏᴜ ɢᴏʀᴋᴜ ᴠ ᴘᴀʀᴋᴇ ɪ ᴋᴀᴛᴀʟsʏᴀ s ɴᴇё ɴᴀ sᴀɴᴋᴀʜ ʟᴇᴅʏᴀɴᴋᴀʜ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴠ ᴋʟɪᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴜsᴛᴀɴᴏᴠɪʟ ʀᴀᴅɪᴀᴛᴏʀ ᴏᴛ ᴠᴇᴢᴅɪʜᴏᴅᴀ ᴄʜᴛᴏʙʏ ᴋᴛᴏ ᴛᴏ ᴏʙᴏɢʀᴇᴠᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴠ ᴇᴛᴜ ʜᴏʟᴏᴅɴᴜʏᴜ ᴢɪᴍᴜ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏᴅsᴛɪʟᴋᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ) ɴᴀᴘɪsʜɪ, s ᴋᴀᴋɪᴍɪ sʟᴏᴠᴀᴍɪ ʏᴀ ᴇʙᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴍᴋᴜ ᴠ ᴛᴠᴏᴇᴊ ᴋᴏᴍɴᴀᴛᴇ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴘʀᴇʟᴀ ɴᴀ ᴍᴏᴇᴍ ʜᴜʏᴜ ᴋᴀᴋ ᴠ ʙᴀɴᴇ ᴘᴏᴅ ᴠʏsᴏᴋᴏᴊ ᴛᴇᴍᴘᴇʀᴀᴛᴜʀᴏᴊ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ɪ ᴏɴ ᴇё ᴋᴀᴋ ʙʏ ɪᴢɴᴜᴛʀɪ ᴏʙᴏɢʀᴇᴠᴀʟ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь sᴠᴏɪᴍ ʜᴜᴇᴍ sъʙɪʟ ᴋᴀᴋ ʟᴏsʜᴀᴅь ᴠ ᴇʙᴀɴɴᴜʏᴜ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴍᴀᴢᴀᴇᴛ sᴠᴏɪ ᴘᴏʟᴏᴠʏᴇ ɢᴜʙʏ ᴍᴏᴇᴊ ᴋᴏɴᴄʜɪɴᴏᴊ ᴅᴜᴍᴀʏᴀ ᴄʜᴛᴏ ᴇᴛᴏ ᴘᴏᴍᴀᴅᴀ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏᴅsᴛɪʟᴋᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ) ɴᴀᴘɪsʜɪ ᴠ ɴᴀᴄʜᴀʟᴇ ᴘʀᴇᴅʟᴏᴢʜᴇɴɪʏᴀ, ᴋᴛᴏ ᴇʙᴀʟ ᴛᴠᴏᴊ ʀᴏᴛᴀɴ, ᴘᴏᴋᴀ ᴛʏ sᴘᴀʟᴀ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴠᴀʟɪʟᴀsь ɴᴀ ᴍᴏᴊ ʜᴜᴊ s ᴛᴜᴀʟᴇᴛɴᴏᴊ ᴋʀʏsʜᴋɪ ʙɪᴏ ᴛᴜᴀʟᴇᴛᴀ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴘʏᴛᴀʟsʏᴀ sᴅᴇʟᴀᴛь ɪᴢ ᴛᴠᴏᴇᴊ sᴇᴍьɪ ᴄʜᴇʟᴏᴠᴇᴄʜᴇsᴋᴜʏᴜ ᴍɴᴏɢᴏɴᴏᴢʜᴋᴜ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴘʀᴏᴢʜᴏɢ ᴘᴏʟᴏᴠᴜʏᴜ ɢᴜʙᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴋᴀᴋ ʙʏᴄʜᴋᴏᴍ sᴏʟᴏғᴀɴᴏᴠʏᴊ ᴘᴀᴋᴇᴛɪᴋ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ sᴇᴊᴄʜᴀs ᴏᴄʜᴋᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴅᴏ ʟɪɴɪɪ ɢᴏʀɪᴢᴏɴᴛᴀ ʀᴀssᴛʏᴀɴᴜ ɪ ᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴘᴏ ɢᴀʙᴀʀɪᴛᴀᴍ ɴᴇ ᴠʟᴇᴢᴇᴛ ᴇё ᴠ ᴜᴢᴋʏᴊ ᴀɴᴀʟьɴʏᴊ ᴘʀᴏʜᴏᴅ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴏᴛᴘʀᴀᴠɪʟ sᴏ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴠᴏ ʀᴛᴜ ᴠ ᴋʀᴇsᴛᴏᴠʏᴊ ᴘᴏʜᴏᴅ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ɪᴘᴏʟьᴢᴜᴇᴛ ᴏᴄʜᴋᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴋᴀᴋ sᴘᴀʟьɴʏᴊ ᴍᴇsʜᴏᴋ ᴠ ᴘᴏʜᴏᴅᴀʜ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏᴅsᴛɪʟᴋᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ) ᴏᴛᴘɪsʜɪsь, ᴋᴛᴏ ʀᴀsʜᴜʏᴀʀɪʟ ᴇʙʟᴏ ᴛᴠᴏᴊ ᴍᴀᴛᴇʀɪ ᴠᴄʜᴇʀᴀ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴠ ᴏᴄʜᴋᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ʀᴀsᴛʏᴀɴᴜ ᴘᴏ ᴅᴜᴘʟᴜ ᴛᴀᴋɴᴋᴀ ᴏʙᴇᴇᴋᴛ-242 ɪ ᴋᴀᴋ ᴛʏ ᴅᴜᴍᴀᴇsʜь ᴄʜᴛᴏ ɪᴢ ᴇᴛᴏɢᴏ ᴠʏᴊᴅᴇᴛ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴄʜᴜᴄʜᴜɴᴅʀᴀ ᴀɴᴀʟьɴᴀʏᴀ?) ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟᴀ ᴋᴀʟᴏɴᴋᴏᴊ ᴠ ᴘᴇʀᴅᴀᴋ ɪ ᴜ ɴᴇᴇ ᴄʜᴇʀᴇᴢ ᴘɪsᴄʜᴅᴜ ᴍᴜᴢᴠᴋᴀ ɪɢʀᴀᴇᴛ <emoji document_id=5317011449061582947>🚬</emoji>",
            "sʜʟʏᴜʜᴀ ᴛʏ ᴘʀᴏʙɪᴛᴀʏᴀ) ʏᴀ ᴛᴇʙᴇ sᴠᴏɪᴍ ʜᴜᴇᴍ sᴄʜᴀs ʀᴏᴛ ᴘʟʀᴠᴜ ɪ ᴠᴏᴅʀᴏ ᴠsᴛᴀᴠʟʏᴜ ɪ ʙᴜᴅᴜ ᴛᴇʙᴇ ssᴀᴛь <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴠ ᴋʟɪᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘᴏsᴛᴀᴠɪʟ ᴜsɪʟᴏᴋ ɪ ᴘʏᴛᴀʟsʏᴀ ʀᴀᴢɢᴏᴠᴀʀɪᴠᴀᴛь ᴠ sᴋᴀᴊᴘᴇ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ɴᴀ ᴏᴄʜᴋᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ɴᴀʀɪsᴏᴠᴀʟ ᴘᴇɴᴛᴀɢʀᴀᴍᴍᴜ ᴘʀᴇᴢʜᴅᴇ ᴄʜᴇᴍ ɪᴢɢᴏɴʏᴀᴛь ᴅᴇᴍᴏɴᴏᴠ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ sᴠᴏɪᴍ ʜᴜᴇᴍ ɴᴀ ᴋʟɪᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴛɪʀᴀʟ ʟᴏᴛᴇʀᴇᴊɴʏᴊ ʙᴇʟᴇᴛ ɪ ᴠʏᴊɢʀᴀʟ ᴏᴅɪɴ ᴍɪʟʟɪᴏɴ ʀᴜʙʟᴇᴊ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴠ ᴋʟɪᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ʀʏʙᴀᴄʜɪʟ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴀ ᴘʀɪᴍᴀɴᴋᴀ ʙʏʟᴀ ɪᴢ ʟᴏʙᴋᴏᴠʏʜ ᴠᴏʟᴏsᴋᴏᴠ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ɪ ᴢᴀ ᴛsᴇʟʏᴇ sᴜᴛᴋɪ ʏᴀ ɴᴀʟᴏᴠɪʟ ᴠᴇᴅʀᴏ ʀᴀᴛᴀɴᴀ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏᴅsᴛɪʟᴋᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ) ɴᴀᴘɪsʜɪ ᴠ ɴᴀᴄʜᴀʟᴇ ᴘʀᴇᴅʟᴏᴢʜᴇɴɪʏᴀ, ᴋᴛᴏ ᴇʙᴀʟ ᴛᴠᴏʏᴜ ᴍᴀᴍᴀsʜᴜ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ sᴏ sᴠᴏᴇɢᴏ ʜᴜʏᴀ ᴋᴀᴋ s ᴘᴇᴄʜᴇɴᴇɢᴀ sᴛʀᴇʟʏᴀʟ ᴠ ᴏᴄʜᴋᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘʀʏᴀᴍ ᴜᴘᴏʀ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴠ ᴋʟɪᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴜsᴛᴀɴᴏᴠɪʟ ʀᴀᴋᴇᴛɴᴏᴇ ᴏʙᴏʀᴜᴅᴏᴠᴀɴɪʏᴀ ᴘᴏᴅ ɴᴀᴢᴠᴀɴɪᴇᴍ ᴢᴇɴɪᴛᴋɪ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ sᴠᴏɪᴍ ʜᴜᴇᴍ ɴᴀ ᴋʟɪᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘᴏsᴛᴀᴠɪʟ ᴢʜɪʀɴᴜʏᴜ ᴛᴏᴄʜᴋᴜ ᴋᴀᴋ sᴛᴀᴠɪʟɪ ᴘɪʀᴀᴛʏ ᴋʀᴇsᴛ ɴᴀ ᴋᴀʀᴛᴇ ɪ ᴠʏᴅᴠɪɢᴀʟɪsь ᴢᴀ sᴏᴋʀᴏᴠɪsᴄʜᴀᴍɪ ᴋᴏᴛᴏʀʏᴇ ʏᴀ ᴜᴛᴀɪʟ ᴠ ᴇё ᴏᴄʜᴋᴇ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴏᴛ ᴜᴅᴀʀᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ ɪ ʜᴜʏᴀ ᴍᴏᴇɢᴏ ᴏᴛᴛsᴀ s ᴅᴠᴜʜ sᴛᴏʀᴏɴ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘʀᴏsᴛᴏ sᴘʟʏᴜsᴄʜɪʟᴏ ᴋᴀᴋ ɪ ᴇё ᴋʟɪᴛᴏʀ ᴠ ᴛᴇsᴋᴀʜ ᴋᴏᴛᴏʀʏᴊ ᴘᴏᴅᴋʀᴜᴄʜɪᴠᴀʟ ᴛᴠᴏᴊ ᴏᴛᴇᴛs ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ sᴠᴏɪᴍ ʜᴜᴇᴍ sɴᴇsᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴄʜᴇʀᴇᴘɴᴜʏᴜ ᴋᴏʀᴏʙᴋᴜ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴋʀᴜᴛɪʟᴀsь ɴᴀ ᴍᴏᴇᴍ ʜᴜʏᴜ ᴋᴀᴋ ɴᴀ sʜᴇsᴛᴇ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴏᴅᴜsʜᴋᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ?)ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴋᴏɢᴅᴀ ᴍᴏᴊ ʜᴜᴊ sᴋᴀᴢᴀʟ ʙᴜ ᴠ ᴛᴠᴏᴇᴊ ᴘɪᴢᴅᴇ ᴛᴀᴋ ᴏᴛᴛᴜᴅᴀ sʀᴀᴢᴜ ᴠsᴇᴛᴋʀᴏᴛʏ ᴘᴏᴠʏʙᴇɢᴀʟɪ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴋʟɪᴛᴏʀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ɪᴢᴍᴇʀʏᴀʏᴜ ᴠᴀʟʏᴜᴛᴜ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴋʟɪᴛᴏʀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘʀᴏᴅᴀʟ ᴢᴀ ᴀᴋᴛsɪɪ ᴠ ɴɪᴋᴇ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴠ ᴋʟɪᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴛᴀᴋᴏᴊ ᴘᴇʀᴇᴘᴏʟᴏʜ ᴜsᴛʀᴏɪʟ ɪ ᴘᴏᴛᴏᴍ ᴘᴏsʟᴇ ᴠsᴇɢᴏ ᴇᴛᴏɢᴏ ᴇᴍᴜ ᴘʀɪsʜʟᴏsь ᴠʏᴘʟᴀᴄʜɪᴠᴀᴛь ᴋᴏᴍᴘᴇɴsᴀᴛsɪʏᴜ ᴢᴀ ɴᴀɴᴇsёɴʏᴊ ᴜsᴄʜᴇʀʙ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴏᴅᴜsʜᴋᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ?)ᴛʏ ᴠᴋᴜʀsᴇ ᴄʜᴛᴏ ʏᴀ ɴᴀsʀᴀʟ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ ɪ ᴛᴇᴍ sᴀᴍʏᴍ ᴠᴢʏᴀʟ s ɴᴇᴇ ᴘᴏʟ sᴜᴍʏ ᴢᴀ ᴍᴀsᴋᴜ ᴏᴛ ᴘʀʏsᴄʜᴇᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴠ ᴏᴄʜᴋᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴏʙᴇᴢᴠᴇʀᴢʜɪᴠᴀʟ ʙᴏᴍʙᴜ ᴘᴏᴅ ɴᴀᴢᴠᴀɴɪᴇᴍ ᴄ4 ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ sᴋᴀᴛɪʟsʏᴀ ᴠ ᴏᴄʜᴋᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴋᴀᴋ ʙᴏᴄʜᴋᴀ sᴏ sᴋᴏʟɪsᴛᴏᴊ ᴘʟᴏᴛғᴏʀᴍʏ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴘʀᴏᴘɪɴʏᴠᴀʟ ᴍʏᴀᴄʜɪᴋ ᴠ ᴋʟɪᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ɪ sʟᴜᴄʜᴀᴊɴᴏ ɴᴀᴅᴏʀᴠᴀʟᴀ ᴋʀᴀᴊ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь,ᴄʜᴛᴏ ᴋᴏɢᴅᴀ ʏᴀ ᴇʙᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь,ᴛᴏ ᴏɴᴀ ᴋʀɪᴄʜɪᴛ,sʟᴏᴠᴀᴍɪ sᴠᴏᴇɢᴏ ᴅᴀᴜɴᴏ ᴍᴜᴢʜᴀ!) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴘᴏʟᴏᴠᴜʏᴜ ᴍᴀᴛᴋᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴀᴍᴘᴜᴛɪʀᴏᴠᴀʟ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴠ ᴋʟɪᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴋᴜʟᴇʀ ᴘᴏsᴛᴀᴠɪʟ ᴅʟʏᴀ ʀᴀsᴘʀᴇᴅᴇʟᴇɴɪʏᴀ ᴋᴏɴᴄʜɪ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴏᴅᴜsʜᴋᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ?)ᴛʏ ᴠᴋᴜᴏsᴇ ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴘᴏ ʀᴀᴢᴍᴇʀᴀᴍ ʟᴇᴢɪᴛ ᴠ ᴘɪᴢᴅᴀᴋ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ) sᴏᴠᴇᴛᴜʏᴜ ᴘᴏᴋᴜᴘᴀᴛь) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴘɪᴢᴅᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ ɪᴢᴏʙʀᴇʟᴀ sᴄʜᴇᴛɴʏᴇ ᴘᴀʟᴏᴄʜᴋɪ ᴠ ᴠɪᴅᴇ ʜᴜᴇᴠ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴛʏᴀɢᴀʏᴜ ᴏᴄʜᴋᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴋᴀᴋ ɢɪʀɪ ᴠ sᴘᴏʀᴛ ᴢᴀʟᴇ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴘʀɪʟᴏᴢʜɪʟ sᴠᴏᴊ ʜᴜᴊ ᴋ ᴋʟɪᴛᴏʀᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴋᴀᴋ ᴘᴏᴅᴏʀᴏᴢʜɴɪᴋ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь,ᴄʜᴛᴏ ᴋᴏɢᴅᴀ ʏᴀ ᴇʙᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь,ᴛᴏ ᴜ ɴᴇᴇ ᴘɪᴢᴅᴀ ᴀᴠᴛᴏᴍᴀᴛɪᴄʜᴇsᴋɪ sᴍᴀᴢʏᴠᴀᴇᴛ ᴍᴏᴊ ʜᴜᴊ,ᴇᴛᴏ ᴋᴀᴋ ᴍᴀsʜɪɴɴᴏᴇ ᴍᴀsʟᴏ!) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴏᴅᴜsʜᴋᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ?)ᴍɴᴇ ɴᴀᴅᴏ ᴘᴏʀᴠᴀᴛь ᴘʟᴇɴᴋᴜ ɴᴀ ᴘɪᴢᴢʜᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ) ᴀ ᴘᴏᴛᴏᴍ ɴᴀᴅᴏ ᴇʜᴀᴛь ɪ ʀᴠᴀᴛь ᴄʜᴇʀᴅᴀᴋ ᴛᴠᴏᴇɢᴏ ᴏᴛᴛsᴀ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴅᴇʟᴀʟ ᴏᴛᴋʀʏᴛʏᴊ ᴘᴇʀᴇʟᴏᴍ ᴋᴏʟᴇɴᴀ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ʜᴜʟɪ ᴛᴏ ᴍᴏᴊ ʜᴜᴊ ɪɢɴᴏʀɪsʜь) ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴠsʏᴀ ᴛᴠᴏʏᴀ sᴇᴍьʏᴀ sᴏsᴇᴛ ʙᴇsᴘʟᴀᴛɴᴏ, ᴀ ᴛʏ ᴘʟᴀᴛɴᴏ, ɪ ᴜ ᴍᴇɴʏᴀ ᴠ ɢᴏʟᴏᴠᴇ ᴘᴏsʜʟᴀ ᴍʏsʟь ᴄʜᴛᴏ ᴛʏ ᴘʀɪᴇᴍɴᴀʏᴀ ᴅᴏᴄʜь?? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴀʟᴇ ʜᴜᴊʟᴀɴᴋᴀ) ʜᴜʟɪ ᴋᴏɢᴅᴀ sᴏsᴇsʜь) ᴛᴏ ᴋᴀᴋ ᴛʀᴏʟʟь ᴏʀᴇsʜь?? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴠᴏʏᴀ ᴘʀᴏᴠᴋᴀᴛsɪʏᴀ ɴᴀsᴛᴏʟьᴋᴏ sʟᴀʙᴀ) ᴄʜᴛᴏ ʏᴀ ᴇʙɴᴜʟ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ ᴘᴏ ᴄʜᴇʟʏᴜsᴛɪ?? <emoji document_id=5317011449061582947>🚬</emoji>",
            "sʟʏsʜь)ᴛʀᴀɴs ᴇʙᴀɴɴʏᴊ)ʏᴀ ᴛᴠᴏʏᴜ ᴘɪᴢᴅᴜ ᴇʙᴀᴛь ᴛᴏ ᴠᴇᴄʜɴᴏ ʙᴜᴅᴜ)ᴄʜᴇᴘᴜsʜᴏᴋ sᴜᴋᴀ ᴏʀᴜ s ᴋʀᴇᴛɪɴᴀ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴄʜᴇᴛ ᴇʙᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь)ʏᴠᴠʏʜᴠʏʜᴠʏʜᴠʜʏᴠʏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴄʜᴇᴛ ᴛᴀᴋ ɢʀᴏᴍᴋᴏ sᴏsᴇsʜь?sᴏsᴇᴅɪ ᴢʜᴀʟᴏᴠᴀᴛsʏᴀ sᴄʜᴀs ɴᴀᴄʜɴᴜᴛ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴛᴠᴏʏᴜ ᴘɪᴢᴅᴜ ʀᴠᴀʟ sᴠᴏɪᴍ ʜᴜᴇᴍ)ᴛʏ ᴘᴏᴍɴɪsʜь? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ʏᴀ sᴍᴏᴛʀʏᴜ ᴠsᴇ ᴢʜᴇ ᴠsᴏsᴀʟ ᴍᴏᴊ ʜᴜᴊ ɪ ɴᴇ ᴏᴛᴢʏᴠᴀᴇsʜьsʏᴀ)) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʜᴜʟɪ ᴛʏ ᴍᴇɴʏᴀ ɪɢɴᴏʀɪsʜь)ᴛʏ ᴄʜᴇᴛ ᴢᴀsʜᴋᴠᴀʀɴʏᴊ ᴛɪᴘᴏᴋ)) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴠ ᴏᴄʜᴋᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ʜʀᴀɴɪʟ ᴏʀᴜᴅɪʏᴀ ᴍᴀssᴏᴠᴏɢᴏ ᴜɴɪᴄʜᴛᴏᴢʜᴇɴɪʏᴀ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴍᴏᴊ ʜᴜᴊ ʀᴇsʜᴀʟ ʀᴇʙᴜsʏ ɴᴀ ᴘɪᴢᴅᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь,ᴄʜᴛᴏ ᴋʟɪᴛᴏʀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ,ᴀᴠᴛᴏᴍᴀᴛɪᴄʜᴇsᴋɪ ɴᴀᴛsᴋʟɪᴠᴀᴇᴛsʏᴀ ɴᴀ ᴍᴏᴊ ʜᴜᴊ,ᴘʀɪᴛsᴇʟ ᴜ ɴᴇᴇ ʜᴏʀᴏsʜɪᴊ,s ᴘᴇʀᴠᴏᴊ ᴘᴏᴘʏᴛᴋɪ ᴢᴀʟᴇᴛᴀᴇᴛ ᴠ ᴍᴏᴊ ʜᴜᴊ!) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴏᴅᴜsʜᴋᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ?)ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴘɪᴢᴅᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ ᴠᴏᴋʀᴜɢ ᴍᴏᴇɢᴏ ʜᴜʏᴀ sᴏᴢᴅᴀᴇᴛ ᴛsᴜɴᴀᴍɪ sᴠᴏᴇᴊ ᴘɪᴢᴅᴏᴊ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴠ ᴋʟɪᴛᴏʀᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴍɪɴᴏᴇ ᴘᴏʟᴇ ᴠʏʟᴏᴢʜɪʟ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴢᴀᴘᴜsᴄʜᴜ ᴠ ᴢᴇᴍʟʏᴜ,ᴏɴᴀ ʙᴜᴅᴇᴛ ᴛᴜʀᴇʟьʏᴜ,ᴀ ᴍᴏᴊ ʜᴜᴊ ʙᴜᴅᴇᴛ ᴋᴀᴋ ᴍᴏᴛᴏʀᴄʜɪᴋᴏᴍ ᴅʟʏᴀ ᴘɪᴢᴅʏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ,ᴛᴀᴋ ᴍʏ ᴏᴛᴋʀᴏᴇᴍ ᴏᴋɴᴏ ᴠ ᴇᴠʀᴏᴘᴜ!) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴠ ᴏᴄʜᴋᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴇᴊᴄʜᴀs sᴠᴏɪᴍ ʜᴜᴇᴍ ᴢᴀᴠᴀʀᴜʜᴜ ᴜsᴛʀᴏʏᴜ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴘʀᴏᴠᴏᴅɪʟ ᴄʜᴇʀɴʏᴊ ᴏʙʀʏᴀᴅ s ᴋʟɪᴛᴏʀᴏᴍ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴏᴅᴜsʜᴋᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ?)ᴛʏ ᴠᴋᴜʀsᴇ ᴄʜᴛᴏ ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴜ ᴘᴏᴅ ʟᴇᴢɢɪɴᴋᴜ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴋᴏɢᴅᴀ ᴍᴏᴊ ʜᴜᴊ ᴅᴇʟᴀʟ ᴠᴜʟᴋᴀɴ ᴠ ᴘɪᴢᴅᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴛᴏ ᴏᴛ sᴛʀᴀʜᴀ ᴏɴᴀ ᴛᴇʙʏᴀ ᴠʏsʀᴀʟᴀ ᴠ ᴋᴜʟᴇᴋ ɪᴢ ᴘᴏᴅ sᴇᴍᴇᴄʜᴇᴋ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴢᴜʙʏ ᴘᴇʀᴇsᴄʜɪᴛʏᴠᴀʟ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴛᴀᴋᴀʏᴀ ʟᴏʜᴍᴀᴛᴋᴀ ɴᴀ ᴘɪᴢᴅᴇ,ᴏsᴛʀᴏᴠ ᴇʙᴀɴʏᴊ,ᴛᴀᴍ s ᴍᴀᴄʜᴇᴛᴇ ᴅᴀᴢʜ ɴᴇ sᴘʀᴀᴠɪᴛьsʏᴀ!) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ʜʀᴏɴʏᴜ sᴠᴏᴊ ʜᴜᴊ ᴠ ᴏᴄʜᴋᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴋᴀᴋ ᴋᴏᴘᴄʜёɴᴜʏᴜ ᴋᴜʀɪᴛsᴜ ᴠ ʜᴏʟᴏᴅɪʟьɴɪᴋᴇ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴏᴅᴜsʜᴋᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ?)ᴛʏ ᴘᴏɴɪɪᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ɴᴀ ᴇʙʟᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴍᴏᴢᴀᴊᴋᴜ ᴘᴏsᴛʀᴏɪʟ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ sᴠᴏɪᴍ ʜᴜᴇᴍ ᴏᴋᴜᴘɪʀᴏᴠᴀʟ ᴀɴᴀʟьɴᴏᴇ ᴘʀᴏsᴛʀᴀɴsᴛᴠᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            'ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь,ᴄʜᴛᴏ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟɪ ʜᴀᴄʜɪ,ᴘᴏᴅ ᴘᴇsɴʏᴜ"ᴄʜᴇʀɴʏᴇ ɢʟᴀᴢᴀ"?) <emoji document_id=5317011449061582947>🚬</emoji>',
            "sᴜᴋᴀ, ᴛʏ ʜᴏᴛʏᴀ ʙʏ ᴋᴏᴘɪʀᴜᴊ ɴᴏʀᴍᴀʟьɴᴏ, ᴠʏᴇʙᴀɴɴᴏᴇ ᴛʏ ᴜʙᴏᴢʜᴇsᴛᴠᴏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴘɪᴢᴅᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ᴘᴇʀᴠᴏ-ᴏᴛᴋʀʏᴠᴀᴛᴇʟь ʜᴜᴇᴠ-ᴍᴜᴛᴀɴᴛᴏᴠ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴠᴋᴜʀsᴇ ᴄʜᴛᴏ ᴀʜʜᴀᴀʜ)ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴋᴏʀᴍʏᴀᴛ ᴋᴀᴋ sᴠɪɴьʏᴜ ᴀ ᴘᴏᴛᴏᴍ ᴘʀᴏᴅᴀʏᴜᴛ ɴᴀ ʙᴀᴢᴀʀᴇ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴍᴀɴʏᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь sᴠᴏɪᴍ ʜᴜᴇᴍ) ᴠᴏᴅʏᴀ ᴘᴇʀᴇᴅ ᴇᴇ ᴇʙᴀʟᴏᴍ) ?? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴇsʟɪ ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴠᴏᴛ sᴄʜᴀs ᴠʏᴇʙᴜ)ᴛᴏ ᴜ ᴍᴇɴʏᴀ ᴢʜɪᴢɴь ʟᴀɢᴀᴛь ɴᴀᴄʜɴᴇᴛ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴀ ᴛʏ ᴠɪᴅᴇʟ ᴘᴏsʟᴇᴅɴɪᴇ ɴᴏᴠᴏsᴛɪ?ɢᴅᴇ ᴍᴏᴊ ʜᴜᴊ ᴘʀᴏᴛᴀʀᴀɴɪʟ ᴘɪᴢᴅᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ)ᴅᴀ ᴢʜᴇsᴛᴋᴏ ʙʏʟᴏ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏ ᴏᴘᴇᴢᴅᴀʟ ʙʟʏᴀᴛь sᴇᴠᴇʀɴʏᴊ) ᴛᴇʙʏᴀ ʙʟʏᴀᴛ ьᴘɪɴɢᴠɪɴʏ ᴠ ᴏᴄʜᴋᴏ ᴇʙᴀʟɪ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴋᴏɢᴅᴀ ᴍᴏᴊ ʜᴜᴊ ɢᴜʟʏᴀʟ ᴘᴏ ᴘɪᴢᴅᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ)ᴀ ʙʏʟᴏ ᴛᴇᴍɴᴏ)ɪ ᴏɴ ᴏʙᴏ ᴄʜᴛᴏ-ᴛᴏ ᴜᴅᴀʀɪʟsʏᴀ)ᴘᴏsʜʟᴀ ᴋʀᴏᴠь)ᴘɪᴢᴅᴇᴛs ʙʏʟᴏ_ <emoji document_id=5317011449061582947>🚬</emoji>",
            "sʟʏsʜь ᴋʀᴄʜ ʏᴀ sᴄʜᴀs ᴛᴇʙᴇ ᴇʙʟᴏ ᴄʜᴇʀᴇɴᴏᴍ ʀᴀᴢᴏʙьʏᴜ ɴᴀʜᴜᴊ ???? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴠᴋᴜʀsᴇ ᴄʜᴛᴏ ᴛʏ ᴛᴏᴛ ᴇʙᴀʟᴀɴ ᴋᴏᴛᴏʀʏᴊ ᴘᴏ ᴘьʏᴀɴᴇ ᴠsᴏsᴀʟ ᴍᴏᴊ ʜᴜᴊ ᴋᴀᴋ ᴄʜᴇʀɴᴀʏᴀ ᴅʏʀᴀ)) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀᴛᴠᴏʏᴜ ᴍᴀᴍᴀsʜᴜ sᴜᴋᴀ ᴇᴛɪʜ ᴇʙᴀɴʏʜ 30000 ʀᴀᴢ ᴇʙᴀʟ ᴠ ᴢʜᴏᴘᴜ sᴜᴋᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏᴊᴍɪ ʙʟʏᴀᴛь!!!ʏᴀ ɴᴇ ʜᴏᴛᴇʟ ʀᴠᴀᴛь ᴘɪᴢᴅᴀᴋ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ)ᴍᴇɴʏᴀ ᴢᴀsᴛᴀᴠɪʟɪ!ᴋʟʏᴀɴᴜsь!!! <emoji document_id=5317011449061582947>🚬</emoji>",
            "sʟʏsʜь)ᴄʜᴇʙᴜʀᴇᴋ)ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ɴᴀ ᴇʙʟᴏ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ sʀᴀʟ ɪ ᴛᴇᴍ sᴀᴍʏᴍ ɢᴏᴛᴏᴠɪʟ ᴛᴇʙᴇ ᴢᴀᴠᴛʀᴀᴋ ᴠ ᴘᴏsᴛᴇʟь) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴀʟᴇ)ɢᴀɴᴅᴜʀᴀs))ᴛʏ ᴏᴘʏᴀᴛь ᴘᴏsʜᴇʟ ᴠ ʟᴇs)ᴛᴏʟьᴋᴏ ɴᴇ ᴠ ᴛᴏᴛ ɢᴅᴇ ᴅᴇʀьᴠьʏᴀ)ᴀ ᴠ ᴛᴏᴛ ɢᴅᴇ ʜᴜɪ ᴠᴇsʏᴀᴛ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ɴᴀɢʟᴀʏᴀ ʜᴜᴇsᴏsᴋᴀ)ᴋᴏɢᴅᴀ ᴏɴᴀ ᴅᴇʟᴀʟᴀ ɢᴏʀʟᴏᴠʏᴊ ᴍɪɴᴇᴛ ᴠ ᴇᴛᴏᴛ ᴍᴏᴍᴇɴᴛ ᴢᴀsʜᴇʟ ᴛᴠᴏᴊ ᴏᴛᴇᴛs)ɪ ᴏɴᴀ ᴘʀɪᴛᴠᴏʀɪʟᴀsь ᴄʜᴛᴏ ᴘᴏᴠᴇsɪʟᴀsь) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴋᴏɢᴅᴀ sʟᴜᴄʜᴀᴊɴᴏ ᴘᴏssᴀʟ ᴠ ᴘɪᴢᴅᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ ᴛᴏ ᴜ ɴᴇᴇ ɴᴀᴄʜʟᴏ ᴠsᴇ ɢɴɪᴛь ɪ ʀᴢʜᴀᴠᴇᴛь) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴛʏ ᴛᴀ ʙʟᴀʜᴀ ᴄʜᴛᴏ ʙᴇɢᴀᴇᴛ ᴘᴏ ᴍᴇᴏᴍᴜ ʜᴜʏᴜ ᴄʜᴀsᴀᴍɪ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴠᴋᴜʀsᴇ ᴄʜᴛᴏ ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴇʙᴀʟ ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴀʟᴇ)ɢɴɪᴅᴏʀᴀs)ᴛʏ ʜᴜʟɪ ᴍᴏᴊ ʜᴜᴊ ɪɢɴᴏʀɪsʜь?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴛʏ sᴜᴋᴀ ᴠsᴏsᴀʟ ᴛᴀᴋ)ᴄʜᴛᴏ ᴀᴢʜ ᴜ ᴛᴇʙʏᴀ ᴍᴏᴊ ʜᴜᴊ ᴠᴍᴇsᴛᴏ ᴋᴀᴅʏᴋᴀ ᴛᴏʀᴄʜɪᴛ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ɴᴇ ᴛᴏᴛ ʟɪ ᴛʏ ᴘᴀᴘᴜᴀs ᴋᴏᴛᴏʀʏᴊ ʜᴏᴄʜᴇᴛ ᴍᴏᴊ ʜᴜᴊ ᴋᴀᴋ sᴏʙᴀᴄʜᴋᴀ ᴋᴏsᴛᴏᴄʜᴋᴜ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "sʟʏsʜь ᴘɪᴅᴀʀᴀs ᴇʙᴀɴʏᴊ ᴍɴᴇ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴠʏᴇʙᴀᴛь ᴄʜᴛᴏʟᴇ?) ?? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴠᴋᴜʀsᴇ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴀɴᴀʟьɴᴀʏᴀ ᴀᴍᴇʙᴀ ᴘʀᴏʀᴠᴀɴᴀ ᴍᴏɪᴍ ʜᴜᴇᴍ)) <emoji document_id=5317011449061582947>🚬</emoji>",
            "sʟʏsʜь ᴄʜᴜʜᴀɴ ᴢᴀʀᴏssʜɪᴊ ) ʏᴀ ᴛᴇʙʏᴀ ʜᴜᴇᴍ sᴄʜᴀs ᴠ 0 ʜᴜᴊɴᴜ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴛᴀᴋ ᴅʀᴀʟ)ᴄʜᴛᴏ ᴜ ɴᴇᴇ ɴᴀ ᴢʜᴏᴘᴇ ᴏsᴛᴀʟsʏᴀ sɪɴʏᴀᴋ ᴘᴏʜᴏᴢʜɪᴊ ɴᴀ ᴋᴠᴀᴢɪᴍᴏᴅᴜ)) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ɴᴀ ʜᴜᴊ ᴘᴏsᴀᴅɪʟ ᴏɴᴀ ᴛᴀᴍ ᴏʙᴏsʀᴀʟᴀsь ?? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴠᴋᴜʀsᴇ ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴘɪᴢᴅᴀ ᴠᴏɴʏᴀᴇᴛ sᴇʟᴇᴅᴋᴏᴊ)ᴍɴᴇ ᴄʜᴇ ᴇᴇ sᴠᴏᴇᴊ ᴍᴏᴄʜᴇᴊ ᴍʏᴛь ᴄʜᴛᴏ-ʟɪ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "sʟʏsʜь ᴄʜᴜᴘᴏᴋᴀʙʀᴀ ᴇʙᴀɴᴀʏᴀʏᴀ) ᴛᴠᴏʏᴀ ᴍᴀᴍᴀsʜᴋᴀ ɴᴀ ᴍᴏᴇᴍ ʜᴜᴇ ᴘᴏᴠᴇsɪᴛsʏᴀ sᴋᴏʀᴏ) ?? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ sᴄʜᴀs ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴠʏᴇʙᴜ ᴠ ᴋɪᴛᴀᴊsᴋᴏᴍ ᴍᴀɢᴀᴢɪɴᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴠᴋᴜʀsᴇ ᴄʜᴛᴏ ᴛᴠᴏʏᴜ ᴍᴀᴍᴀsʜᴜ ᴇʙᴀʟɪ ᴠᴄʜᴇʀᴀ ᴋᴀᴢᴀᴋɪ ᴘᴏᴅ ᴄʜᴀsᴛᴜsʜᴋᴜ)ᴠᴇsᴇʟʏᴇ ᴢʜᴇ ʀᴇʙᴀᴛᴀ)) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴇᴍᴜ ʜᴜʏᴜ sᴏᴠᴇᴛ ᴅᴏᴠᴇʀɪʟ ᴅᴏʟᴢʜɴᴏsᴛь ᴘʀɪᴢᴇᴅᴇɴᴛᴀ ɪ ᴛᴇᴘᴇʀь ʏᴀ ᴘᴏsᴛʀᴏʏᴜ ᴛᴀᴍ ɴᴏᴠʏᴊ ɢᴏʀᴏᴅ)s ᴅᴇᴛsᴋᴏᴊ ᴘʟᴏsᴄʜᴀᴅᴋᴏᴊ ɪ sʜᴋᴏʟᴀᴍɪ s ʙᴏʟьɴɪᴛsᴀᴍɪ)) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍɴᴇ ᴛᴀᴋ ɪ ᴇʙᴀᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь,ɪʟɪ ᴛʏ ᴠsᴇ ᴢʜᴇ sᴀᴍ ɴᴀᴄʜɴᴇsʜь?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴄʜʏ ᴄʜᴇᴛ ᴜɴɪᴢʜᴀᴇsʜь ᴍᴏᴊ ʜᴜᴊ)ᴘɪᴅᴏʀᴀsᴏᴠ ᴛᴏ ɴᴇ ᴇʙᴜ)ᴀ ᴛʏ ᴏᴋᴀᴢʏᴠᴀᴇᴛsʏᴀ ᴘɪᴅᴏʀᴀs) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴜᴢʜᴇ ᴢᴀᴇʙᴀʟsʏᴀ ᴛᴠᴏʏᴜ ᴘɪᴢᴅᴜ ʀᴠᴀᴛь)ᴏɴᴀ ᴜᴢʜᴇ ᴋᴀᴋ ᴍᴇᴛʀᴏ ᴇʙᴀᴛь)ᴋᴀᴢʜᴅʏᴊ ᴘʀᴏᴇʜᴀʟsʏᴀ?? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴘʀɪᴅᴜᴍᴀʟ,ᴅᴀᴠᴀᴊ ʏᴀ ʙᴜᴅᴜ ᴇʙᴀᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь,ᴀ ᴛʏ sʙᴏᴋᴜ ʙᴜᴅᴇsʜь sᴍᴏᴛʀᴇᴛь,ɪ ɢᴏᴠᴏʀɪᴛь ᴍɴᴇ sᴠᴏɪ ᴏsʜɪʙᴋɪ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴍɴᴇ ᴛᴀᴋ ɪ ᴇʙᴀᴛь ᴛᴠᴏʏᴜ ᴍᴀᴛь,ɪʟɪ ᴛʏ ᴜᴢʜᴇ ᴘᴏsᴛᴀᴠɪsʜь ʙᴀʟʟʏ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴀʟᴇ)ɢɴɪᴅᴀ)ᴛʏ ᴄʜᴇ ᴛᴀᴍ ᴜsɴᴜʟ ᴄʜᴛᴏ-ʟɪ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴄʜᴇ ᴇᴛ ᴍᴏᴊ ʜᴜᴊ ɪɢɴᴏʀɪsʜь ᴛᴏ?)ᴄʜᴇᴘᴜsʜᴏᴋ ᴛʏ ᴇʙᴀɴɴʏᴊ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴀ ᴘɪᴢᴅᴜ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ ᴛᴀᴋ ᴢʜᴇ ᴋᴀᴋ ɪ ᴘʀᴇᴢɪʀᴠᴀᴛɪᴠʏ ᴘᴏsʟᴇ ɪsᴘᴏʟьᴢᴏᴠᴀɴɪʏᴀ ᴍᴇɴʏᴀʏᴜᴛ? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴠᴋᴜʀsᴇ ᴄʜᴛᴏ ᴘɪᴢᴅᴀᴋ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ ᴋᴀᴋ ᴠ ɪɢʀᴇ ᴢᴀᴠɪs ɴᴀ ᴍᴏᴇᴍ ʜᴜʏᴜ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴘɪᴢᴅᴀ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ ᴢᴀᴅʏᴍᴇʟᴀsь ᴋᴏɢᴅᴀ ᴘʀɪᴋᴏsɴᴜʟᴀsь ᴋ ᴍᴏᴇᴍᴜ ʜᴜʏᴜ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴇʀᴇᴅᴀᴊ ᴍᴀᴍᴇ,ᴛᴀᴋ ʙʏsᴛʀᴏ ᴜsʜʟᴀ ᴄʜᴛᴏ ᴢᴀʙʏʟᴀ ᴢᴀʙʀᴀᴛь ɴᴀsᴀsᴏɴɴᴏᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "sʟʏsʜь ᴢᴀsʜᴋᴠᴀʀᴏᴋ)ᴛʏ ɢᴅᴇ ᴛᴀᴍ)ʏᴀ ᴠsᴇ ᴇsᴄʜᴇ ᴢʜᴅᴜ ᴛᴠᴏɪʜ ɪɴᴛɪᴍɴʏʜ ᴜsʟᴜɢ ᴅʟʏᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ʜᴜʟɪ ᴏᴘʏᴀᴛь ɴᴀ ᴍᴏᴊ ʜᴜᴊ sᴇʟ ɪ ɪɢɴᴏʀɪsʜь ᴇɢᴏ?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ sʟᴜᴄʜᴀᴊɴᴏ ᴏʙ ᴛᴠᴏʏᴜ ᴘɪᴢᴅᴜ sᴘᴏᴛʏᴋɴᴜʟsʏᴀ sᴠᴏɪᴍ ʜᴜᴇᴍ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴇʙɴɪ ᴘᴏ ᴍᴏᴇᴍᴜ ʜᴜʏᴜ sᴠᴏᴇᴊ ᴘɪᴢᴅᴏᴊ, sʏɴ ᴢᴀsʜᴋᴠᴀʀɴᴏᴊ sʜᴀʟᴀᴠʏ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴀʟᴇ)ɢɴɪᴅᴏʀᴀsᴋᴀ)ᴏᴛᴘɪsʜɪsь ɴɪᴢʜᴇ s ᴋᴀᴋɪᴍɪ sʟᴏᴠᴀᴍɪ ᴛʏ sʟɪᴢʏᴠᴀʟ ᴋᴏɴᴄʜᴜ s ᴍᴏᴇɢᴏ ʜᴜʏᴀ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴠ ᴅᴇᴛsᴠᴛᴠᴇ ɴᴀᴢʏᴠᴀʟɪ ɢʀᴏᴍᴏᴍ)ᴘᴏᴛᴏᴍᴜ ᴄʜᴛᴏ ᴏɴ ᴋᴀᴋ ɢʀᴏᴍ ʙɪʟ ᴘᴏ ᴘɪᴢᴅᴇ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ)ᴛᴠᴏʏᴀ ғᴀᴍɪʟɪʏᴀ ᴠɪᴅᴀᴛь ᴠ ᴄʜᴇsᴛь ɴᴇɢᴏ)ᴛᴀᴋ ᴢʜᴇ ᴋᴀᴋ ɢʀᴏᴍ sᴠᴏɪᴍ ʀᴛᴏᴍ ᴘᴏ ʜᴜʏᴀᴍ ʙьᴇsʜь)) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴋʟᴀssɴᴏ ʙᴇɢᴀᴇᴛ)ᴏᴛ ᴍᴏᴇɢᴏ ʜᴜʏᴀ) ᴅᴀᴠᴀᴊ ɪᴅɪ ɴᴀ ʜᴜᴊ sʏɴ ᴘɪᴅᴏʀᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴠᴋᴜʀsᴇ ᴄʜᴛᴏ ʏᴀ ᴛᴠᴏʏᴜ ᴘɪᴢᴅᴜ ᴋᴏɢᴅᴀ ᴇʙᴜ)ᴋʀɪᴋɪ ᴠᴀsᴇ ᴛɪsʜɪ ɪ ᴛɪsʜɪ)ᴏᴋᴀᴢʏᴠᴀᴇᴛьsʏᴀ ᴇᴇ ɪ ᴢᴀʀʏᴀᴢʜᴀᴛь ɴᴀᴅᴏ( <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴘᴏᴄʜᴇᴍᴜ ᴋᴏɢᴅᴀ ʏᴀ ᴇʙɴᴜʟ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴇ ᴜ ɴᴇᴇ ғᴏʀᴛᴏᴄʜᴋᴀ ᴠ ᴘɪᴢᴅᴇ ᴏᴛᴋʀʏʟᴀsь)( ???????????? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴀʟᴏ)ʏᴀ ᴛᴇʙʏᴀ ᴛᴜᴛ ᴇʙᴜ)ᴘᴏsᴍᴏᴛʀɪ ʜᴏᴛʏᴀʙʏ ᴋᴀᴋ ᴍᴏʏᴀ ᴋᴏɴᴄʜᴀ ᴛᴇᴄʜᴇᴛ ᴘᴏ ᴛᴠᴏɪᴍ ᴠᴇɴɴᴀᴍ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʙʟʏᴀᴛь(ᴏᴛᴅᴏʟᴢʜɪ sᴠᴏᴊ ʜᴜᴊ ᴘᴏᴢʜᴀʟᴜᴊsᴛᴀ((ᴇʙᴜ ᴛᴠᴏʏᴜ ᴍᴀᴛь(ᴀ ᴛᴠᴏᴊ ᴏᴛᴇᴛs ᴘʀᴏsɪᴛ ᴘᴏsᴏsᴀᴛь)ᴠᴏᴛ ᴘᴜsᴛь ᴛᴠᴏᴊ ɪ sᴏsᴇᴛ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʏᴀ ᴛᴠᴏʏᴜ ᴍᴀᴛь ᴘᴏ ᴜᴛʀᴜ ᴇʙᴜ ᴛᴀᴋ ᴏʜᴜᴇɴɴᴏ, s ᴅᴏʙʀɪᴄʜᴋᴀ ᴇʙᴀᴛь) ᴏɴᴀ ᴠɪʀɪsᴄʜɪᴛ ᴋᴀᴋ sᴜᴋᴀ)( <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʙʟʏᴀᴛь)ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴅᴇʟᴀᴇᴛ ᴏᴛʟɪᴄʜɴʏᴊ ᴍᴀssᴀᴢʜ ʏᴀᴢʏᴋᴏᴍ )ᴢɴᴀʟ ʙʏ,ɪ ʀᴀɴьsʜᴇ ʜᴏᴅɪʟ ʙʏ)) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ʏᴀ ʜᴜᴇᴍ ᴋ ᴛᴇʙᴇ ᴛᴠᴏʏᴜ ᴍᴀᴍᴀɴьᴋᴜ ᴢᴀɴᴇsᴜ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛᴀᴋ ᴏɴᴀ ᴏᴛsᴏsᴀʟᴀ ᴜᴢʜᴇ ᴏᴅɪɴ ɴɪɢᴇʀsᴋɪᴊ ᴄʜʟᴇɴ,sᴛʀᴇʟᴏᴄʜɴɪᴛsᴀ ᴛʏ ssᴀɴᴀʏᴀ) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʙʟʏᴀᴛь)ʏᴀᴢʏᴋ ᴛᴠᴏᴇᴊ ᴍᴀᴍᴀsʜɪ ɴᴇ ᴢᴀᴍᴇɴɪᴍ)ᴠᴏᴛ ɴᴀᴘʀɪᴍᴇʀ)ᴋᴏɴᴄʜɪʟᴀsь ᴛᴜᴀʟᴇᴛɴᴀʏᴀ ʙᴜᴍᴀɢᴀ)ᴠᴏᴛ ɪ ᴠʏᴛᴇʀᴀᴊ ᴇᴇ ʏᴀᴢʏᴋᴏᴍ)) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴋᴀᴢʜᴅᴀʏᴀ ᴛᴠᴏᴊ ᴘʀᴏᴠᴀᴋᴀᴛsɪʏᴀ)ɪ ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴏsᴇᴛ ᴏᴅɪɴ ɴɪɢᴇʀsᴋɪᴊ ᴄʜʟᴇɴ,ᴘᴏᴇʜᴀʟɪ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴠɪᴢʜᴜ ᴛᴠᴏᴊ ᴀɴᴀʟ,ᴅᴀ ᴛᴏᴄʜɴᴏ ᴛᴠᴏᴊ,ᴠᴏᴛ ᴘᴏsᴍᴏᴛʀɪ,ᴠᴏᴏᴏᴏɴ ᴛᴀᴍ ɴᴀ ʜᴜʏᴜ ᴍᴏᴇᴍ ᴠᴇsɪᴛ???????????? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴀ ᴠᴏᴛ ᴛᴠᴏᴇ ɪᴍʏᴀ,ᴇᴛᴏ ᴠ ᴄʜᴇsᴛь ᴍᴏᴇɢᴏ ʜᴜʏᴀ-ᴋᴏʀᴏʟʏᴀ ᴀʟᴇᴋsᴀɴᴅʀᴀ 1?) <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴅᴀᴜɴ ᴋᴏᴛᴏʀʏᴊ sᴏsёᴛ ᴍᴏᴊ ʜᴜᴊ sᴏ sᴛʀᴏᴄʜᴋᴏᴊ ɴɪᴢʜᴇ ᴄʜᴇʀᴇᴢ ᴀɴᴀʟ sᴠᴏᴇᴊ ᴍᴀᴛᴇʀɪ ɪ ʀᴛᴏᴍ ᴏᴛᴛsᴀ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴢʜᴇ ᴄʜᴜᴋᴄʜᴀ)ᴛʏ ɴᴀʜᴜᴊ ᴘʏᴛᴀʟsʏᴀ ᴠsᴜɴᴜᴛь ᴍɴᴇ sᴠᴏʏᴜ ᴠᴏɴʏᴜᴄʜᴜʏᴜ ᴘɪᴢᴅᴇɴᴋᴜ ʏᴠʜᴠʏʜʏᴠʜʏᴠʜʏᴠ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ ᴏᴅᴇʟsʏᴀ ᴠ ᴛɪɢʀᴀ)ᴀ ᴛᴠᴏʏᴀ ᴍᴀᴛь sᴛᴀʟᴀ ᴢᴏᴏғɪʟᴋᴏᴊ?????????????? <emoji document_id=5317011449061582947>🚬</emoji>",
            ")ᴀ ɴᴜ ʟᴇɢ,ᴍᴏʟᴏᴅᴇᴛs,ᴠsᴛᴀᴠᴀᴊ,ᴜᴛɪ ᴜᴍɴɪᴄʜᴋᴀ,sᴏsɪ,ʙᴏᴢʜᴇ sᴀᴍʏᴊ ᴘʀɪʀᴜᴄʜᴇɴɴʏᴊ ᴘᴇsɪᴋ ᴜ ᴍᴇɴʏᴀ :3 <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴀ ɴᴜ ʟᴇɢ,ᴍᴏʟᴏᴅᴇᴛs,ᴠsᴛᴀᴠᴀᴊ,ᴜᴛɪ ᴜᴍɴɪᴄʜᴋᴀ,sᴏsɪ,ʙᴏᴢʜᴇ sᴀᴍʏᴊ ᴘʀɪʀᴜᴄʜᴇɴɴʏᴊ ᴘᴇsɪᴋ ᴜ ᴍᴇɴʏᴀ :3 <emoji document_id=5317011449061582947>🚬</emoji>",
            "sʟʏsʜь)ᴄʜᴇᴘᴜsʜᴏᴋ)ᴛʏ ᴛᴀᴋ ɪ ʙᴜᴅᴇsʜь ʙᴏʟᴛᴀᴛь ɪʟɪ ᴜᴢʜᴇ ɴᴀᴋᴏɴᴇᴛs ᴠᴏᴢьᴍᴇsʜь ᴍᴏᴊ ʜᴜᴊ sᴇʙᴇ ᴠ ʀᴏᴛ ɪ sᴅᴇʟᴀᴇsʜь ɴᴀᴍ ᴏʙᴏɪᴍ ᴘʀɪʏᴀᴛɴᴏ???????????? <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴢʜᴇ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴍᴏᴊ ʜᴜᴊ sᴛᴏʟᴋɴᴇᴛsʏᴀ s ᴘɪᴢᴅᴏᴊ ᴛᴠᴏᴇᴊ ᴍᴀᴍʏ ᴠ ᴘᴏᴇᴅɪɴᴋᴇ <emoji document_id=5317011449061582947>🚬</emoji>",
            "ʙʟʏᴀᴛь ᴘɪᴢᴅᴇᴛs)ᴄʜᴇ ᴢᴀ ᴅᴇʟᴀ?ᴍᴏᴊ ʜᴜᴊ ᴏɢʀᴀʙɪʟɪ ᴠ ᴛᴠᴏᴇᴊ ᴢʜᴇ ᴘɪᴢᴅᴇ!ᴛʏ ɢʟᴀᴠɴʏᴊ,ᴠᴏᴛ ɪ ʀᴀᴢʙɪʀᴀᴊsʏᴀ!! <emoji document_id=5317011449061582947>🚬</emoji>",
            "ᴛʏ ᴢʜᴇ ᴘᴏɴɪᴍᴀᴇsʜь ᴄʜᴛᴏ ᴛᴠᴏʏᴀ ᴍᴀᴛь ᴘᴏᴅsᴏsᴋᴀ ᴍᴏᴇɢᴏ ʜᴜʏᴀ) ᴛʏ ᴅᴀᴢʜᴇ ᴍᴏᴢʜᴇsʜь ɴᴇ ɢᴀᴠᴋᴀᴛь ᴍɴᴇ ɴᴀ ʜᴜᴊ <emoji document_id=5317011449061582947>🚬</emoji>",
        ]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl7))
            await sleep(0.1)
            await sleep(time)


    async def дединсайдcmd(self, message):
        """— Запускает модуль по указанной команде"""
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b><emoji document_id=5229205949410978575>🥺</emoji> ʍᴏдуᴧь #ᎠᴇдИнᴄᴀйд нᴀчᴀᴧ ᴇбᴀᴛь ᴛᴇбᴇ ʍᴀʍɜᴇᴧь. <emoji document_id=5229205949410978575>🥺</emoji></b>")
            return 
        await utils.answer(
             message,
             "<b><emoji document_id=5229205949410978575>🥺</emoji> Ꮇᴏдуᴧь #ᎠᴇдИнᴄᴀйд ᴨᴇᴩᴇᴄᴛᴀᴧ ᴇбᴀᴛь ᴛᴇбᴇ ʍᴀʍɜᴇᴧь. <emoji document_id=5229205949410978575>🥺</emoji>\n\n"
             "<emoji document_id=5229205949410978575>🥺</emoji> Ꮞᴛᴏбы ᴏᴄᴛᴀнᴏʙиᴛь ᴨᴩᴏᴨиɯи. <code>.дединсайд</code></b>"
         )         
        try:
             time = float(args[0])
        except ValueError:
             return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl8 = [
        '[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤐ ӄ𐌻ꤣተ꤀рꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ӄγ𐌻ꤕр ꤙ꤀ꤍተꤌꤐꤣ𐌻 მ𐌻ꤎ рꤌꤍꤙрꤕმꤕ𐌻ꤕઞꤣꤎ ӄ꤀ઞપꤣ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤙ꤀𐌻꤀ꤐγળ 𐌼ꤌተӄγ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 ꤌ𐌼ꤙγተꤣр꤀ꤐꤌ𐌻?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤙр꤀ꤙꤣઞખꤐꤌ𐌻 𐌼ꤎપꤣӄ ꤐ ӄ𐌻ꤣተ꤀рꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤣ ꤍ𐌻γપꤌ꤇ઞ꤀ ઞꤌმ꤀рꤐꤌ𐌻ꤌ ӄрꤌ꤇ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤍӄꤌተꤣ𐌻ꤍꤎ ꤐ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ӄꤌӄ ꤒ꤀પӄꤌ ꤍ꤀ ꤍӄ꤀𐌻ꤣꤍተ꤀꤇ ꤙ𐌻꤀ተϕ꤀р𐌼ખ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤐ ꤀પӄꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 ꤀ꤒꤕउꤐꤕр𐌟ꤣꤐꤌ𐌻 ꤒ꤀𐌼ꤒγ ꤙ꤀მ ઞꤌउꤐꤌઞꤣꤕ𐌼 ꤍ4 ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤐ ӄ𐌻ꤣተ꤀рꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ተꤌӄ꤀꤇ ꤙꤕрꤕꤙ꤀𐌻꤀𑀋 γꤍተр꤀ꤣ𐌻 ꤣ ꤙ꤀ተ꤀𐌼 ꤙ꤀ꤍ𐌻ꤕ ꤐꤍꤕ꤅꤀ ᤋተ꤀꤅꤀ ꤕ𐌼γ ꤙрꤣω𐌻꤀ꤍ𑀨 ꤐખꤙ𐌻ꤌપꤣꤐꤌተ𑀨 ӄ꤀𐌼ꤙꤕઞꤍꤌꤟꤣળ उꤌ ઞꤌઞꤕꤍёઞખ꤇ γ൰ꤕрꤒ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ӄ𐌻ꤣተ꤀р ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤙр꤀მꤌ𐌻 उꤌ ꤌӄꤟꤣꤣ ꤐ ꤙ꤯ӄꤕ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ӄ𐌻ꤣተ꤀р ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤣउ𐌼ꤕрꤎળ ꤐꤌ𐌻ળተγ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ӄрγተꤣ𐌻ꤌꤍ𑀨 ઞꤌ 𐌼꤀ꤕ𐌼 𑀋γળ ӄꤌӄ ઞꤌ ωꤕꤍተꤕ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 ꤍઞꤕꤍγ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ પꤕрꤕꤙઞγળ ӄ꤀р꤀ꤒӄγ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤀ተ γმꤌрꤌ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ꤣ 𑀋γꤎ 𐌼꤀ꤕ꤅꤀ ꤀ተꤟꤌ ꤍ მꤐγ𑀋 ꤍተ꤀р꤀ઞ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤙр꤀ꤍተ꤀ ꤍꤙ𐌻ળ൰ꤣ𐌻꤀ ӄꤌӄ ꤣ ꤕё ӄ𐌻ꤣተ꤀р ꤐ ተꤕꤍӄꤌ𑀋 ӄ꤀ተ꤀рખ꤇ ꤙ꤀მӄрγપꤣꤐꤌ𐌻 ተꤐ꤀꤇ ꤀ተꤕꤟ )  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 ઞꤌ ӄ𐌻ꤣተ꤀рꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤙ꤀ꤍተꤌꤐꤣ𐌻 𐌟ꤣрઞγળ ተ꤀પӄγ ӄꤌӄ ꤍተꤌꤐꤣ𐌻ꤣ ꤙꤣрꤌተખ ӄрꤕꤍተ ઞꤌ ӄꤌрተꤕ ꤣ ꤐખმꤐꤣ꤅ꤌ𐌻ꤣꤍ𑀨 उꤌ ꤍ꤀ӄр꤀ꤐꤣ൰ꤌ𐌼ꤣ ӄ꤀ተ꤀рખꤕ ꤎ γተꤌꤣ𐌻 ꤐ ꤕё ꤀પӄꤕ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤐ ӄ𐌻ꤣተ꤀рꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ γꤍተꤌઞ꤀ꤐꤣ𐌻 рꤌӄꤕተઞ꤀ꤕ ꤀ꤒ꤀рγმ꤀ꤐꤌઞꤣꤎ ꤙ꤀მ ઞꤌउꤐꤌઞꤣꤕ𐌼 उꤕઞꤣተӄꤣ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤍ꤀ ꤍꤐ꤀ꤕ꤅꤀ 𑀋γꤎ ӄꤌӄ ꤍ ꤙꤕપꤕઞꤕ꤅ꤌ ꤍተрꤕ𐌻ꤎ𐌻 ꤐ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤙрꤎ𐌼 γꤙ꤀р ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤐ ꤀પӄꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤐ꤀ꤍꤍተꤌઞꤌꤐ𐌻ꤣꤐꤌ𐌻 ꤍꤣꤍተꤕ𐌼γ ꤒꤕउ꤀ꤙꤌꤍઞ꤀ꤍተꤣ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤐ ӄ𐌻ꤣተ꤀рꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ рખꤒꤌપꤣ𐌻 ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 ꤌ ꤙрꤣ𐌼ꤌઞӄꤌ ꤒખ𐌻ꤌ ꤣउ 𐌻꤀ꤒӄ꤀ꤐખ𑀋 ꤐ꤀𐌻꤀ꤍӄ꤀ꤐ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤣ उꤌ ꤟꤕ𐌻ખꤕ ꤍγተӄꤣ ꤎ ઞꤌ𐌻꤀ꤐꤣ𐌻 ꤐꤕმр꤀ рꤌተꤌઞꤌ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 ઞꤌ ӄ𐌻ꤣተ꤀рꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤍተꤣрꤌ𐌻 𐌻꤀ተꤕрꤕ꤇ઞખ꤇ ꤒꤕ𐌻ꤕተ ꤣ ꤐખ꤇꤅рꤌ𐌻 ꤀მꤣઞ 𐌼ꤣ𐌻𐌻ꤣ꤀ઞ рγꤒ𐌻ꤕ꤇ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ઞꤌ ꤀પӄꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ઞꤌрꤣꤍ꤀ꤐꤌ𐌻 ꤙꤕઞተꤌ꤅рꤌ𐌼𐌼γ ꤙрꤕ𐌟მꤕ પꤕ𐌼 ꤣउ꤅꤀ઞꤎተ𑀨 მꤕ𐌼꤀ઞ꤀ꤐ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤐ ӄ𐌻ꤣተ꤀рꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤙ꤀ꤍተꤌꤐꤣ𐌻 γꤍꤣ𐌻꤀ӄ ꤣ ꤙખተꤌ𐌻ꤍꤎ рꤌउ꤅꤀ꤐꤌрꤣꤐꤌተ𑀨 ꤐ ꤍӄꤌ꤇ꤙꤕ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ӄ꤀꤅მꤌ ꤎ ઞꤌተꤎ꤅ꤣꤐꤌળ ӄ𐌻ꤣተ꤀р ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ઞꤌ 𐌼ꤣӄр꤀ϕ꤀ઞ ተ꤀ γ 𐌼ꤕઞꤎ ꤅꤀𐌻꤀ꤍ მꤕተꤍӄꤣ꤇ ӄꤌӄ ꤐ ꤙр꤀꤅рꤌ𐌼𐌼ꤕ ꤍ꤈꤀ꤗꤙ ꤤꤌ᥉ꤖ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤐ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ рꤌꤍተꤎઞγ ꤙ꤀ მγꤙ𐌻γ ተꤌӄઞӄꤌ ꤀ꤒᤋꤕӄተ-242 ꤣ ӄꤌӄ ተખ მγ𐌼ꤌꤕω𑀨 પተ꤀ ꤣउ ᤋተ꤀꤅꤀ ꤐખ꤇მꤕተ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤣꤙ꤀𐌻𑀨उγꤕተ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ӄꤌӄ ꤍꤙꤌ𐌻𑀨ઞખ꤇ 𐌼ꤕω꤀ӄ ꤐ ꤙ꤀𑀋꤀მꤌ𑀋 ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤀ተꤙрꤌꤐꤣ𐌻 ꤍ꤀ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 ꤐ꤀ рተγ ꤐ ӄрꤕꤍተ꤀ꤐખ꤇ ꤙ꤀𑀋꤀მ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤣउγપꤌ𐌻 ꤌઞꤌ𐌻𑀨ઞ꤀ꤕ ꤀ተꤐꤕрꤍተꤣꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤣ ઞꤌω꤀𐌻 ተꤌ𐌼 ꤀ꤍ꤀ꤒ꤀ рꤕმӄꤣꤕ ꤌрተꤕϕꤌӄተખ ӄ꤀ተ꤀рખꤕ ꤀ઞ ꤍმꤌ𐌻 ꤐ 𐌼γउꤕ꤇ ꤣ ꤕ𐌼γ ꤐખმꤌ𐌻ꤣ ꤐ꤀उઞꤌ꤅рꤌ𐌟მꤕઞꤣꤕ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤍꤕ꤇પꤌꤍ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 მ꤀ 𐌻ꤣઞꤣꤣ ꤅꤀рꤣउ꤀ઞተꤌ рꤌꤍꤍተꤎઞγ ꤣ ተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤙ꤀ ꤅ꤌꤒꤌрꤣተꤌ𐌼 ઞꤕ ꤐ𐌻ꤕउꤕተ ꤕё ꤐ γउӄખ꤇ ꤌઞꤌ𐌻𑀨ઞખ꤇ ꤙр꤀𑀋꤀მ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 ꤙр꤀𐌟꤀꤅ ꤙ꤀𐌻꤀ꤐγળ ꤅γꤒγ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ӄꤌӄ ꤒખપӄ꤀𐌼 ꤍ꤀𐌻꤀ϕꤌઞ꤀ꤐખ꤇ ꤙꤌӄꤕተꤣӄ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 ꤙખተꤌ𐌻ꤍꤎ ꤍმꤕ𐌻ꤌተ𑀨 ꤣउ ተꤐ꤀ꤕ꤇ ꤍꤕ𐌼𑀨ꤣ પꤕ𐌻꤀ꤐꤕપꤕꤍӄγળ 𐌼ઞ꤀꤅꤀ઞ꤀𐌟ӄγ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤍꤐꤌ𐌻ꤣ𐌻ꤌꤍ𑀨 ઞꤌ 𐌼꤀꤇ 𑀋γ꤇ ꤍ ተγꤌ𐌻ꤕተઞ꤀꤇ ӄрખωӄꤣ ꤒꤣ꤀ ተγꤌ𐌻ꤕተꤌ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 𐌼ꤌउꤌꤕተ ꤍꤐ꤀ꤣ ꤙ꤀𐌻꤀ꤐખꤕ ꤅γꤒખ 𐌼꤀ꤕ꤇ ӄ꤀ઞપꤣઞ꤀꤇ მγ𐌼ꤌꤎ પተ꤀ ᤋተ꤀ ꤙ꤀𐌼ꤌმꤌ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 ꤍъꤒꤣ𐌻 ӄꤌӄ 𐌻꤀ωꤌმ𑀨 ꤐ ꤕꤒꤌઞઞγળ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤙрꤕ𐌻ꤌ ઞꤌ 𐌼꤀ꤕ𐌼 𑀋γળ ӄꤌӄ ꤐ ꤒꤌઞꤕ ꤙ꤀მ ꤐખꤍ꤀ӄ꤀꤇ ተꤕ𐌼ꤙꤕрꤌተγр꤀꤇ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ꤣ ꤀ઞ ꤕё ӄꤌӄ ꤒખ ꤣउઞγተрꤣ ꤀ꤒ꤀꤅рꤕꤐꤌ𐌻 ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤐ ӄ𐌻ꤣተ꤀рꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ γꤍተꤌઞ꤀ꤐꤣ𐌻 рꤌმꤣꤌተ꤀р ꤀ተ ꤐꤕउმꤣ𑀋꤀მꤌ પተ꤀ꤒખ ӄተ꤀ ተ꤀ ꤀ꤒ꤀꤅рꤕꤐꤌ𐌻 ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤐ ᤋተγ 𑀋꤀𐌻꤀მઞγળ उꤣ𐌼γ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤕმꤣઞꤍተꤐꤕઞખ꤇ ӄተ꤀ ꤒγმꤕተ ꤀ꤒ꤀꤅рꤕꤐꤌተ𑀨 ተꤐ꤀ળ 𐌼ꤌተ𑀨 ᤋተ꤀꤇ उꤣ𐌼ઞꤕ꤇ ꤍተγ𐌟꤀꤇ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ उꤌ𐌻ꤣ𐌻 ӄ𐌻ꤣተ꤀р ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ӄꤌӄ 𐌻ꤎმꤕઞγળ ꤅꤀рӄγ ꤐ ꤙꤌрӄꤕ ꤣ ӄꤌተꤌ𐌻ꤍꤎ ꤍ ઞꤕё ઞꤌ ꤍꤌઞӄꤌ𑀋 𐌻ꤕმꤎઞӄꤌ𑀋 ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ӄꤌӄ ꤀მꤣઞ꤀ӄꤣ꤇ ꤍꤐꤣተꤣ𐌻𑀨ઞꤣӄ ꤐ ӄр꤀𐌼ꤕωઞ꤀꤇ ተ𑀨𐌼ꤕ ꤒꤕउ ꤐꤕმ꤀𐌼ꤌ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤀ꤍተꤌꤐꤣ𐌻 ઞꤌ ӄ𐌻ꤣተ꤀рꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ рꤌउმрꤌ𐌟ꤕઞꤣꤕ ӄꤌӄ рꤕꤙꤕ꤇ઞꤣӄ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤙ꤀ꤒખꤐꤌꤐ ꤐ ӄ𐌻ꤣተ꤀рꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤀ꤒઞ꤀рγ𐌟ꤣ𐌻 ꤒ꤀𐌻ꤕꤕ ተખꤍꤎપꤣ γ꤅р꤀उ ӄꤌӄ ꤌઞተꤣ-ꤐꤣрγꤍ,ꤙ꤀꤅ꤤ 32 ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤙ꤀𐌼ꤕꤍተꤣ𐌻ꤍꤎ ꤐ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ӄꤌӄ ꤐ ꤣउꤒγωӄγ ઞꤌ ӄγр𑀨ꤣ𑀋 ઞ꤀𐌟ӄꤌ𑀋 ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤙ꤀მ𑀋꤀მꤣተ ӄ ꤀પӄγ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ӄꤌӄ उ꤀𐌻꤀ተ꤀꤇ ӄ𐌻ળપꤣӄ ӄ ꤍγઞმγӄγ ꤍ ꤍ꤀ӄр꤀ꤐꤣ൰ꤌ𐌼ꤣ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 ꤐ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ 𐌼ꤌተꤕрꤣ γӄ𐌻ꤌმખꤐꤌ𐌻 ꤍተꤕઞӄγ ꤣउ ӄꤣꤙрꤙꤣપꤕ꤇ მ𐌻ꤎ ꤀ꤙ꤀рખ ꤍꤐ꤀ꤕ꤅꤀ 𑀋γꤎ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ઞꤌ ꤀પӄꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ӄꤌተꤌ𐌻 ӄ꤀𐌼ӄꤣ ઞꤌꤐ꤀उꤌ ӄꤌӄ ઞ꤀ꤐ꤀उઞખ꤇ 𐌟γӄ ꤣ ꤙ꤀ተ꤀𐌼 ꤍӄꤣმખꤐꤌ𐌻 ꤐ ઞγተр𑀨 ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤐ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤍተрꤕ𐌻ꤎ𐌻 ꤣउ ꤍꤐ꤀ꤕ꤅꤀ 𑀋γꤎ ӄꤌӄ ꤣउ 𐌻γӄꤌ ꤌ ꤍተрꤕ𐌻ખ ꤒખ𐌻ꤣ ꤐ ꤐꤣმꤕ ӄ꤀ઞપꤣઞખ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ઞꤌ ꤅рꤌઞꤣ ꤍ𐌼ꤕрተꤣ ꤀ተ ꤐખꤍተрꤕ𐌻ꤌ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ꤐ ꤕё ꤕꤒ𐌻ꤕተ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ γ ተꤐ꤀ꤕ꤅꤀ ꤀ተꤟꤌ ꤍꤙꤣउმꤣ𐌻 მγ𑀋ꤣ ઞꤌꤒрખउ꤅ꤌ𐌻ꤍꤎ ꤣ𐌼ꤣ ꤣ ꤙ꤀ω꤀𐌻 ꤕꤒꤌተ𑀨 ተꤐ꤀ળ 𐌼ꤌተ𑀨 પተ꤀ ꤒખ р꤀მઞખ𐌼 उꤌꤙꤌ𑀋꤀𐌼 ꤙꤌ𑀋𐌻꤀ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤐ ꤀પӄꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤣꤙрꤌꤐꤣ𐌻 ተꤕ𑀋ઞꤣપꤕꤍӄγળ ઞꤕꤙ꤀𐌻ꤌმӄγ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ӄꤌӄ მꤣ𑀋𐌻꤀ϕ꤀ꤍ მ𐌻ꤎ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤒ𐌻꤀𑀋 ꤐખꤐ꤀მꤣተ𑀨 ꤣउ ꤕё 𐌻꤀ꤒӄ꤀ꤐખ𑀋 ꤐ꤀𐌻꤀ꤍ꤀ꤐ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ઞꤌꤒрꤌꤍખꤐꤌꤕተꤍꤎ ઞꤌ 𐌼꤀꤇ 𑀋γ꤇ ӄꤌӄ ӄꤌꤐӄꤌउӄꤌꤎ ꤀ꤐપꤌрӄꤌ ꤍ ꤅꤀рઞખ𑀋 рꤌꤐઞꤣઞ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ӄ꤀꤅მꤌ р꤀ꤍꤍꤣꤎ ꤙγꤍӄꤌ𐌻ꤌ рꤌӄꤕተખ ተ꤀ მꤌઞઞખꤕ ӄ꤀꤀рმꤣઞꤌተખ ꤣउ𐌼ꤕઞꤣ𐌻ꤣꤍ𑀨 ꤣ ꤐ𐌻ꤕተꤕ𐌻ꤣ ꤐ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ઞ꤀ꤍꤣተꤍꤎ उꤌ 𐌼꤀ꤣ𐌼 𑀋γꤕ𐌼 ӄꤌӄ ꤐ꤀𐌻ӄ उꤌ उꤌ꤇ꤟ꤀𐌼 ꤣउ 𐌼γ𐌻𑀨ተꤣӄꤌ "ઞγ ꤙ꤀꤅꤀მꤣ" ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤍ ꤙ꤀𐌻ꤎ ꤍ꤀ꤒꤣрꤌ𐌻ꤌ 𑀋γꤣ ꤐ ꤐꤣმꤕ ꤅рꤣꤒ꤀ꤐ ꤣ ꤍӄ𐌻ꤌმખꤐꤌ𐌻ꤌ ꤍꤕꤒꤕ ꤐ ꤀પӄ꤀ ꤐ ꤐꤣმꤕ ӄꤌрउꤣઞખ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤀ተрꤌ𐌟ꤌ𐌻 ꤌተꤌӄγ ተꤌ𐌻ꤣꤒꤍӄꤣ𑀋 𑀋γꤕꤐ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 მꤐꤣ꤅ꤌ𐌻 ӄꤌӄ ተꤎ𐌟ꤕ𐌻ખ꤇ ꤙрꤕმ𐌼ꤕተ ꤐ ꤐꤣმꤕ მꤣꤐꤌઞꤌ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤐ ӄꤣ𐌻ተ꤀рꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤙ꤀ꤍተр꤀ꤣ𐌻 ꤒγઞӄꤕр მ𐌻ꤎ ꤙр꤀𐌟ꤣꤐꤌઞꤣꤕ ꤐ꤀ ꤐрꤕ𐌼ꤎ ӄꤌተꤌӄ𐌻ꤣउ𐌼ꤌ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ઞખрઞγ𐌻 ꤐ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ተ꤀𐌻𑀨ӄ꤀ ꤍ꤀ ꤍተр꤀𑀋꤀ꤐӄ꤀꤇ ꤣ ꤍ ꤌӄꤐꤌ𐌻ꤌઞ꤅꤀𐌼 ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤍꤒр꤀ꤍꤣ𐌻 ꤍꤐ꤀꤇ 𑀋γ꤇ ꤐ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤐ ꤐꤣმꤕ ꤎӄ꤀рꤎ ӄ꤀ተ꤀рખꤕ ꤍӄꤣმખꤐꤌળተ ꤍγმઞꤌ ӄ꤀꤅მꤌ ꤙрꤣωꤐꤌрተ꤀ꤐખꤐꤌળተꤍꤎ ӄ ꤒγ𑀋ተꤕ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤀ተꤙрꤌꤐꤣ𐌻ꤍꤎ ꤐ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ӄꤌӄ ꤐ ᤋӄꤙꤕმꤣꤟꤣળ ꤌ ተ꤀પઞꤕꤕ ӄꤌӄ ꤐ ӄꤣઞ꤀ "ተꤌ꤇ઞખ ꤙꤕрꤕꤐꤌ𐌻ꤌ მꤎተ𐌻꤀꤅꤀" ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ઞꤌ ꤀પӄꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ઞꤌрꤣꤍ꤀ꤐꤌ𐌻 ӄꤌрተγ 𐌼ꤣрꤌ ꤣ ꤙ꤀ተ꤀𐌼 ꤙ꤀ ઞꤕ꤇ ꤀ꤙрꤕმꤕ𐌻ꤎ𐌻 ꤅მꤕ ꤎ ઞꤌ𑀋꤀𐌟γꤍ𑀨 ӄꤌӄ ꤙ꤀ ɠρ᥉ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ઞꤌӄрખ𐌻 ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ӄꤌӄ ꤀მꤕꤎ𐌻꤀𐌼 ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤍ 𑀋γꤕ𐌼 ተꤐ꤀ꤕ꤅꤀ ꤀ተꤟꤌ ꤣ꤅рꤌ𐌻ꤣ ઞꤌ ӄ𐌻ꤣተ꤀рꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤐ 𐌼꤀рꤍӄ꤀꤇ ꤒ꤀꤇ ӄꤌӄ ઞꤌ 𐌻ꤣꤍተ꤀પӄꤌ𑀋 ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤙ꤀მꤍተꤌꤐꤣ𐌻 ꤙ꤀მ ተꤌ𐌻ꤣꤒꤍӄꤣ꤇ ꤀ꤒꤍተрꤕ𐌻 𑀋γꤕꤐ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ઞꤌ ӄ𐌻ꤣተ꤀рꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 𐌼ꤕተӄγ ꤀ꤍተꤌꤐꤣ𐌻 ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤍꤐ꤀꤇ 𑀋γ꤇ ꤐ उꤌተખ𐌻꤀ӄ ӄꤣმꤌ𐌻 ꤣ ꤀ઞꤌ γꤙꤌ𐌻ꤌ ꤣ ꤙр꤀ꤕ𑀋ꤌꤐωꤣꤍ𑀨 рተ꤀𐌼 ꤙ꤀ ӄꤐꤌрተꤌ𐌻γ ꤀ઞꤌ ઞꤌꤍ꤀ꤒꤣрꤌ𐌻ꤌ ӄγપγ 𑀋γꤕꤐ )  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤐ ӄ𐌻ꤣተ꤀рꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ઞꤌω𐌻ꤣ ꤣઞϕꤕӄꤟꤣળ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤐ ӄ𐌻ꤣተ꤀р ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤙ꤀𐌼ꤕꤍተꤣ𐌻 ꤍꤐ꤀꤇ 𑀋γ꤇ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] उꤌપꤕ𐌼 ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ઞꤌ ꤍꤐ꤀ꤕ꤇ ӄ𐌻ꤣተ꤀р ӄꤣተꤌ꤇ꤍӄγળ 𐌻ꤌꤙωγ ઞꤌӄрγપꤣꤐꤌꤕተ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ઞꤌ 𐌻꤀ꤒ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤍꤐ꤀꤇ 𑀋γ꤇ ꤙрꤣꤒꤣ𐌻 ꤐ ꤐꤣმꤕ ተр꤀ϕꤕꤎ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 ઞꤌ ተꤐ꤀ꤣ𑀋 ꤅γꤒꤌ𑀋 𑀋γꤕꤐ ꤙ꤀ꤒખꤐꤌ𐌻꤀ ꤒ꤀𐌻𑀨ωꤕ પꤕ𐌼 ꤐ ӄꤣተꤌꤕ ꤒ꤀𐌻𑀨ωꤕ ઞꤌр꤀მγ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤕꤒꤌ𐌻 ꤐ მꤐγ𑀋 ӄ꤀𐌻ꤕꤍઞ꤀꤇ પꤕ𑀋꤀ተӄꤕ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤙ꤀꤅𐌻꤀൰ꤌꤕተ ӄ𐌻ꤣተ꤀р ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ მꤌꤐઞ꤀ ꤙ꤀рꤐꤌઞ꤀ 𐌼꤀ꤣ𐌼 𑀋γꤕ𐌼 ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤣउꤒꤌꤐꤣ𐌻 ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤀ተ 𐌼γપꤕઞꤣꤎ ꤐ ઞꤣ𐌟ઞꤣ𑀋 ꤅ꤕઞꤣተꤌ𐌻ꤣꤎ𑀋 ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤐખ𐌻ꤕપꤣ𐌻 ꤀ተ рꤌӄꤌ 𐌼꤀उ꤅ꤌ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ მ𐌻ꤎ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ӄꤌӄ ꤐ꤀𐌻ωꤕꤒઞꤌꤎ ꤙꤌ𐌻꤀પ𑀨ӄꤌ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ઞꤌ р꤀ተ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤍꤐ꤀꤇ 𑀋γ꤇ 𐌻꤀𐌟ꤣ𐌻 ӄꤌӄ ꤅𐌻ꤌმꤣ𐌻𑀨ઞ꤀ળ მ꤀ꤍӄγ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ӄ𐌻ꤣተ꤀р ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤙрꤕ𐌻 ઞꤌ 𐌼꤀ꤕ𐌼 𑀋γળ ӄꤌӄ ꤐ ꤒꤌઞꤕ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤅р꤀ꤒ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ઞꤌ ꤍꤐ꤀ꤕ 𑀋γળ ተꤌ൰ꤣ𐌻 მ꤀ ӄ𐌻ꤌმꤒꤣ൰ꤌ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ӄ𐌻ꤣተ꤀р ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ᤋተ꤀ ꤙꤌउმꤒꤣ൰ꤕ მ𐌻ꤎ 𑀋γꤕꤐ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ӄ𐌻ꤣተ꤀р ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ მ𐌻ꤎ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ӄꤌӄ рꤌმꤣ꤀ ꤙрꤣё𐌼ઞꤣӄ ꤐ 𐌼ꤌ꤅ઞꤣተ꤀ϕ꤀ઞꤕ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ઞꤌ ӄ𐌻ꤣተ꤀рꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤙр꤀მꤌળ ተꤌӄ꤀ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤣउγપꤣ𐌻 ꤌઞꤌ𐌻𑀨ઞખꤕ ተ꤀ઞઞꤕ𐌻ꤣ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ӄ꤀ተ꤀рખ ꤙ꤀ꤍተр꤀ꤣ𐌻ꤣ მрꤕꤐઞꤣꤕ ꤣઞӄꤣ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ 𐌼꤀꤅γ ꤙ꤀მꤐꤕꤍተꤣ ꤍꤐ꤀꤇ 𑀋γ꤇ ӄ ઞ꤀ꤍγ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤍ ꤙ꤀𐌼꤀൰𑀨ળ ተꤐ꤀ꤕ꤅꤀ рተꤌ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ӄ𐌻ꤣተ꤀р ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤍ꤀ꤒрꤌ𐌻ꤣ მрꤕꤐઞꤣꤕ ꤌተꤟተꤕӄꤣ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤌ꤅ꤕઞተ ӄ𐌻ꤣተ꤀рꤌ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤣ ꤙ꤀𐌼꤀꤅ꤌꤕተ ꤕ꤇ рꤕϕꤣ𐌻ꤌрꤌ𐌼ꤣ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ӄ𐌻ꤣተ꤀р ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ 𐌻ꤕተꤌꤕተ ꤙ꤀ 𑀋γꤎ ӄꤌӄ ꤍꤌ𐌼꤀𐌻ꤕተ ꤙ꤀ 𐌼ꤣрγ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤙ꤀𐌻ઞ꤀ꤍተ𑀨ળ ꤙ꤀꤅рγउꤣ𐌻ꤍꤎ ꤐ ӄ𐌻ꤣተ꤀р ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤍꤕ꤇પꤌꤍ ꤒγმꤕω𑀨 ꤙрꤣઞꤣ𐌼ꤌተ𑀨 𐌼꤀꤇ 𑀋γ꤇ ꤍꤕꤒꤕ ꤐ მγωγ ӄꤌӄ р꤀მઞ꤀꤅꤀ )  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤙ꤀ӄꤌ ተખ 𐌼꤀꤇ 𑀋γ꤇ ꤙꤕрꤕӄꤌተખꤐꤌ𐌻 પꤕрꤕउ рꤌꤐઞꤣઞખ,ꤐ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ખ ꤍተ꤀𐌻ӄઞγ𐌻ꤣꤍ𑀨 ઞꤕꤣउꤐꤕꤍተઞખꤕ 𑀋γꤣ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ተꤕꤒꤎ рꤌꤍꤙꤎ𐌻 ઞꤌ 𑀋γꤕ𐌼 ተꤐ꤀ꤕ꤅꤀ ꤀ተꤟꤌ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 ተ꤀ પተ꤀ 𐌼꤀꤇ પ𐌻ꤕઞ рꤐꤕተ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤒꤕउ ꤙрꤕმγꤙрꤕ𐌟მꤕઞꤣꤕ ઞγ ӄꤌӄ ꤙрꤎ𐌼 ઞꤌ ꤐ꤀꤇ઞꤕ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤀ꤒγꤍተр꤀ꤣ𐌻 ӄꤌӄ ӄ꤀𐌼ઞꤌተγ ꤐ ӄꤐꤌрተꤣрꤕ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤐ ӄ𐌻ꤣተ꤀рꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤙ꤀ተр꤀ꤣ𐌻 ꤍተꤣрꤌ𐌻𑀨ઞγળ 𐌼ꤌωꤣઞӄγ მ𐌻ꤎ 𑀋γꤕꤐ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 ꤣउ𐌼ꤕрꤎ𐌻 მ𐌻ꤣઞγ ӄ𐌻ꤣተ꤀рꤌ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤍተꤌꤐ𐌻ળ उꤌꤙꤎተખꤕ ઞꤌ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ተખ ꤀ꤙꤕउმ꤀𐌻 ተγꤙ꤀рખ𐌻ખ꤇ [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍ𐌻ખω, ꤙꤣმ꤀рꤌꤍ, ꤍળმꤌ ꤣმꤣ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ მꤌ𐌻 ӄ꤀𐌻ꤒꤌꤍ꤀꤇ ꤙ꤀ ꤕꤒꤌ𐌻γ, ꤣ ꤍӄꤌउꤌ𐌻, પተ꤀ ተꤌӄ ꤒખ𐌻꤀ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤕꤒꤌተ𑀨 ተખ ӄγꤒ ӄꤐꤌმрꤌተઞખ꤇ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌ𐌼ꤌωꤌ ꤐ 𐌻ꤕꤍγ ઞꤌተӄઞγ𐌻ꤌꤍ𑀨 ઞꤌ 𐌼꤀꤇ 𑀋γ꤇,ӄꤌӄ ӄрꤌꤍઞꤌꤎ ωꤌꤙ꤀પӄꤌ ઞꤌ ꤐ꤀𐌻ӄꤌ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 उꤌმꤕр𐌟ꤣꤐꤌꤕተ მખ𑀋ꤌઞꤣꤕ ꤙрꤣ ꤐꤣმꤕ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ ϕꤌӄተγ ተખ ꤍ꤀ꤍꤕω𑀨 𐌼ઞꤕ 𑀋γ꤇) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤒꤕ𐌻ખ꤇ 𐌻ꤕꤒꤕმ𑀨 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ωё𐌻 ઞꤌ ϕр꤀ઞተ ꤐ ઞꤌმꤕ𐌟მꤕ γꤐꤣმꤕተ𑀨 ꤣ ꤍꤙꤌꤍተꤣ ꤀ተ ꤙ𐌻ꤕઞꤌ ꤙꤣउმγ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ᤋተ꤀ ઞ꤀ꤐꤌꤎ ᤋрꤌ ተр꤀𐌻𐌻ꤣઞ꤅ꤌ, ተγተ ꤍ꤀ω𐌻ꤣꤍ𑀨 ꤐ ꤙ꤀ꤕმꤣઞӄꤕ उγꤒખ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤣ 𐌼꤀꤇ પ𐌻ꤕઞ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ӄγმꤌ ꤍъꤕꤒખꤐꤌꤕω𑀨? ) उꤐꤕр꤀ꤍ꤀ꤐ𑀋꤀उ ꤌઞꤌ𐌻𑀨ઞખ꤇ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ꤕꤒꤌ𐌻 ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤐ ꤙꤌрӄꤕ ળрӄꤍӄ꤀꤅꤀ ꤙꤕрꤕ꤀მꤌ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ϕγ, ꤍተрꤕ𐌻꤀પઞꤣӄ, ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ተ꤀𐌟ꤕ ꤍተрꤕ𐌻ꤎꤕተ ꤅γꤒ꤀꤇ ꤙ꤀ 𐌼꤀ꤕ𐌼γ 𑀋γળ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤕꤒꤌ𐌻 ӄ꤀꤅მꤌ ઞꤌ ꤙ꤀𐌻ꤎઞӄꤕ उꤌ𐌟꤅𐌻ꤣꤍ𑀨 ϕ꤀ઞꤌрꤣ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 γꤐꤣმꤕꤐ 𐌼꤀꤇ 𑀋γ꤇ ꤍӄꤌउꤌ𐌻ꤌ -" પተ꤀ उꤌ ӄрꤌꤍꤌꤐꤕꤟ " [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ઞꤌꤐꤕрઞ꤀ꤕ ઞꤕ उઞꤌ𐌻, ઞ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤙр꤀ꤎꤐ𐌻ꤎ𐌻 ꤌӄተꤣꤐઞ꤀ꤍተ𑀨 ꤕ൰ё ꤐ ꤌઞተꤣપઞ꤀ꤍተꤣ, 𐌼꤀꤇ 𑀋γ꤇ ꤙ꤀ ꤍ𐌻꤀ꤐꤌ𐌼 γપꤕઞખ𑀋 ꤒખ𐌻 ꤍꤙꤌꤍꤣተꤕ𐌻ꤕ𐌼 𐌻ળმꤍӄ꤀꤅꤀ р꤀მꤌ. 𐌼꤀꤇ 𑀋γ꤇ ꤍꤙꤌꤍ 𐌻ળმꤕ꤇ ꤀ተ ꤅꤀𐌻꤀მꤌ ꤣ 𐌟ꤌ𐌟მખ ꤐ ተ꤀𐌼 પꤣꤍ𐌻ꤕ ꤣ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 𐌼ઞꤕ ꤍ꤀ꤍꤌ𐌻ꤌ ꤍ 𐌼꤀𐌻ꤣተꤐ꤀꤇ ꤕꤒꤌઞꤌωӄꤌ [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] γ ተꤕꤒꤎ 𐌼꤀𐌻꤀ϕ𑀨ꤎ ઞꤌ ꤅γꤒꤕ, ꤐખተрꤣ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙꤣმ꤀р, ꤌ ተꤐ꤀ꤎ 𐌼ꤌ𐌼ꤌωꤌ ꤍꤌꤍꤕተ!!! [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ 𑀋γꤕꤍ꤀ꤍ, ꤌ ꤎ ꤕꤒꤌ𐌻 ተꤐ꤀ળ 𐌼ꤌተ𑀨 ઞꤌ ꤅꤀рꤌ𑀋 ӄꤌꤐӄꤌउꤌ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ተꤕꤒꤕ ꤕꤒꤌ𐌻𑀨ઞꤣӄ પ𐌻ꤕઞ꤀𐌼 ꤙ꤀ተγωγ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼ꤌተ𑀨 ተꤐ꤀ળ ꤕꤒꤌ𐌻 ઞꤌ ꤙрꤣꤕ𐌼ꤕ γ ꤍተ꤀𐌼ꤌተ꤀𐌻꤀꤅ꤌ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼ꤌ𐌼ꤌωӄꤌ ተꤐ꤀ꤎ ω𐌻ꤌ ઞꤌ 𑀋γ꤇, ӄꤌӄ ઞꤕ꤅р उꤌ ꤍꤐ꤀ꤒ꤀მ꤀꤇ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀꤇𐌼ꤣ ) ꤙꤣउმꤌӄ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ꤍꤙꤌꤍꤌꤕተꤍꤎ ꤀ተ ꤒꤕმ ઞꤌ 𐌼꤀ꤕ𐌼 𑀋γળ, ተꤐ꤀ꤎ 𐌼ꤌ𐌼ꤌωꤌ ꤅꤀ꤒ𐌻ꤣઞ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ, ꤎ ꤕ꤇ ꤟꤕ𐌻ӄγ ꤐꤣωꤕઞӄ꤀꤇ ꤍ꤀рꤐꤌ𐌻 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤌ ተખ उઞꤌ𐌻, પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤙꤣ൰ꤕउꤌ𐌼ꤕઞꤣተꤕ𐌻𑀨 ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ӄ꤀𐌻પꤌઞ꤀𐌼 𐌼ꤌተ𑀨 ተꤐ꤀ળ ꤕꤒꤌ𐌻 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌ𐌼ꤌωꤌ მꤣઞꤌ𐌼ꤣӄ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤒꤣ𐌻 ꤙ꤀ꤍγმγ ꤀ꤒ ꤙꤣउმγ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤕꤒꤌ𐌻 ተꤐ꤀ળ 𐌼ꤌ𐌼ꤌωγ ઞꤌ ӄрખωꤕ მ꤀𐌼ꤌ ተꤐ꤀ꤕ꤅꤀ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼꤀꤇ 𑀋γ꤇ ઞꤕ рγપӄꤌ, उꤌપꤕ𐌼 ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ઞꤌꤙꤣꤍꤌ𐌻ꤌ ꤍꤕꤒꤕ ઞꤌ 𐌻ꤒγ 𐌼꤀ꤣ𐌼 𑀋γꤕ𐌼? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼꤀ꤣ𐌼 𑀋γꤕ𐌼 ꤀ተӄꤌꤙખꤐꤌ𐌻ꤣ 𑀋рꤌ𐌼 ꤐ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌ𐌼ꤌ ተ꤀પꤣተ उγꤒખ ꤀ꤒ 𐌼꤀꤇ 𑀋γ꤇ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤕꤒꤌተ𑀨 ተખ પγωӄꤌ ꤀ꤒ꤀ꤍрꤌઞꤌꤎ, ꤌ ተꤐ꤀ꤎ 𐌼ꤌ𐌼ꤌωꤌ ꤙꤣმ꤀рꤌꤍӄꤌ ӄꤌрተꤌꤐꤌꤎ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ӄꤌӄ ተ꤀ ꤙγωӄꤣઞ ꤍӄꤌउꤌ𐌻, પተ꤀ ઞꤌ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ꤒ꤀𐌻𑀨ωꤕ ꤐ꤀𐌻꤀ꤍ પꤕ𐌼 γ ꤕꤐрꤕꤎ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌ𐌼ꤌ 𑀋γꤕꤍ꤀ꤍӄꤌ, ꤌ ተખ ꤙꤣმ꤀рꤌꤍ ꤍ𐌻ꤣउꤣꤍተખ꤇ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤍ𐌻ꤣउઞꤎӄ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌ𐌼ꤌωꤌ ꤀ተმખ𑀋ꤌ𐌻ꤌ ꤐ ተγрꤟꤣꤣ ઞꤌ 𐌼꤀ꤕ𐌼 𑀋γળ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼ꤌተ𑀨 ተꤐ꤀ળ ꤕꤒꤌ𐌻, მγрꤌપ꤀ӄ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 𐌼꤀꤇ 𑀋γ꤇, ӄꤌӄ उꤕઞꤣꤟγ ꤀ӄꤌ ꤒꤕрꤕ𐌟ꤕተ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙꤣउმꤌӄ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ꤍӄ𐌻꤀ઞꤕઞ ӄ ꤍγꤣꤟꤣმγ, ꤌ ꤙꤣउმꤌӄ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ꤒ꤀𐌻ꤕઞ 𐌼꤀ꤣ𐌼 𑀋γꤕ𐌼 પተ꤀ 𐌻ꤣ? ) ઞꤌ𑀋γ꤇ ተꤐ꤀ꤎ 𐌼ꤌ𐌼ꤌωꤌ ꤣउγપꤌꤕተ 𐌼꤀꤇ 𑀋γ꤇? ) ꤀ઞ ઞꤕ 𐌼ꤣϕ ꤣ ઞꤕ 𐌻ꤕ꤅ꤕઞმꤌ ) 𐌼꤀꤇ 𑀋γ꤇ ꤐ꤀ωё𐌻 ꤐ ተꤐ꤀ળ 𐌼ꤌተ𑀨, ӄꤌӄ ꤍꤌ𐌼꤀𐌻ёተ ꤐ ꤌઞ꤅ꤌр ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] γ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ઞꤌ ꤙꤣउმꤕ ተꤌተγꤣр꤀ꤐӄꤌ ꤐ ꤐꤣმꤕ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤕꤒꤌ𐌻 𐌼ꤌተ𑀨 ተꤐ꤀ળ ꤐ ꤙꤕрꤣ꤀მ 𑀋ꤌр𑀨ӄ꤀ꤐ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 પተ꤀ ӄꤌꤐꤒ꤀꤇? ) ઞꤌ𑀋γ꤇ ꤀ઞꤌ ꤐખрꤎმꤣ𐌻ꤌꤍ𑀨 ꤐ ω𐌻ꤎꤙγ? ) ꤀ઞꤌ 𐌻ળꤒꤣተ ӄ꤀꤅მꤌ ꤕё ꤐ ω𐌻ꤎꤙꤕ ꤕꤒγተ? ) ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 მγрꤌ? ) ઞꤌ 𑀋γꤎ ꤀ઞꤌ ઞꤌተꤎઞγ𐌻ꤌ ꤅ꤌઞმ꤀ઞ ઞꤌ ꤅꤀𐌻꤀ꤐγ? ) ꤀ઞꤌ પተ꤀ рꤕωꤣ𐌻ꤌ рꤌउ꤅рꤌꤒꤣተ𑀨 ꤅γꤒ꤀꤇ 𐌼꤀꤇ 𑀋γ꤇? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 उꤐ꤀ઞꤣ𐌻ꤌ 𐌼꤀ꤕ𐌼γ 𑀋γળ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤙꤣӄꤌꤙꤣተ 𐌼꤀꤇ 𑀋γ꤇ ꤐउ꤅𐌻ꤎმ꤀𐌼 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼꤀꤇ 𑀋γ꤇ ઞꤕ ӄꤌрꤌઞმꤌω, ઞ꤀ ꤀ઞ ꤀ꤍተꤌꤐꤣ𐌻 ꤌꤐተ꤀꤅рꤌϕ ઞꤌ ꤅γꤒꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤌ𐌻𐌻꤀, ꤎ ꤙрꤣωё𐌻, მꤌꤒખ ꤀ተ પꤣꤍተꤣተ𑀨 ꤕꤒ𐌻꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ꤀ተ ωተγӄꤌተγрӄꤣ ꤍꤐ꤀ꤣ𐌼 ꤒ꤀𐌻𑀨ωꤣ𐌼, ተ꤀𐌻ꤍተખ𐌼 𑀋γꤕ𐌼 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ઞγ ઞꤣ𑀋γꤎ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 მउળმ꤀ꤣꤍተ ꤍ ꤐꤕрተγωӄꤣ ꤅γꤒખ 𐌼꤀꤇ 𑀋γ꤇ γ𐌻꤀𐌟ꤣ𐌻ꤌ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙр꤀ꤍተꤣ, ઞ꤀ ꤎ ꤍ𐌻γપꤌ꤇ઞ꤀ γр꤀ઞꤣ𐌻 ꤌꤒꤌ𐌟γр ઞꤌ ꤙꤣउმꤌӄ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ, ተγωꤣ ꤒખꤍተрꤕꤕ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌ𐌼ꤌωꤌ ꤙрꤣω𐌻ꤌ ꤐ ꤌꤒꤒꤌተꤍተꤐ꤀, рꤌꤍӄꤣઞγ𐌻ꤌ ꤍꤐ꤀ꤣ ꤅γꤒખ ઞꤌ ꤍӄꤌ𐌼𑀨ળ, ꤣ ઞꤌપꤌ𐌻ꤌ ꤍ꤀ꤍꤌተ𑀨 𑀋γꤣ ꤟꤕрӄ꤀ꤐઞꤣӄꤌ𐌼 ꤀ተપꤣ൰ꤌꤎ ꤍꤐ꤀꤇ р꤀ተ ꤀ተ उ𐌻ખ𑀋 ꤐрꤕმꤣተꤕ𐌻ꤕ꤇, ઞ꤀ ᤋተ꤀ ꤙ꤀𑀋γ꤇, ꤎ ꤙр꤀ꤍተ꤀ ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤌꤒꤒрꤕꤐꤣꤌተγрꤌ рተꤌ ተꤐрꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ተꤌӄ꤀ꤐꤌ " ꤒउ൰γꤐ " - ꤒꤕрγ उꤌ ൰ꤕӄγ γ ꤐꤍꤕ𑀋, ꤐ꤀ተ ተꤌӄꤌꤎ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤐ꤀ተ ꤍ𐌼꤀ተрꤣ ,მγрꤌપ꤀ӄ, ꤐ꤀ተ ꤎ ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨, მꤌ?) ꤌ ተખ ꤙр꤀ꤍተ꤀ ꤍ𐌼꤀ተрꤣω𑀨, ꤣ ઞꤕ მꤕ𐌻ꤌꤕω𑀨 ઞꤣપꤕ꤅꤀, ꤐ꤀ተ მγрꤌӄ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ પተ꤀ ተꤐ꤀рꤣω𑀨, 𐌼꤀꤇ მрγ꤅, γ ተꤕꤒꤎ ꤀પӄ꤀ მખрꤎꤐ꤀ꤕ, γ ተꤕꤒꤎ ઞꤕმγ꤅ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍ𐌻ખω, ꤐ꤀ተ ꤍ𐌼꤀ተрꤣ ꤐ પꤕ𐌼 ꤙр꤀ꤒ𐌻ꤕ𐌼ꤌ ተꤐ꤀ꤕ꤅꤀ ꤀પӄꤌ,꤀ઞ꤀ ꤙр꤀ꤍተ꤀ მખрꤎꤐ꤀ꤕ, ઞꤣተ꤀꤅ ꤣ ꤣ꤅꤀𐌻꤀ӄ ꤐꤍꤕ꤅꤀ 𐌼ꤣрꤌ ઞꤕ 𑀋ꤐꤌተꤣተ, પተ꤀ꤒ ꤕ꤅꤀ उꤌωꤣተ𑀨 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤌ उઞꤌꤕω𑀨, ꤐ꤀ተ ꤎ ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨, ӄꤌӄ ωꤌ𐌼ꤌઞ ꤐખउખꤐꤌꤕተ მγ𑀋꤀ꤐ, ꤎ ꤐખउખꤐꤌળ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𑀋ꤕ𑀋, ꤙꤕተγω꤀ӄ, ተખ ꤙꤌ𐌻𑀨ꤟખ ઞꤕ ꤍ𐌻꤀𐌼ꤌ꤇ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤐ꤀ተ પ꤀ተꤌ 𐌼ꤌተ𑀨 ተꤐ꤀ળ ተꤌӄ ꤙ꤀ꤕꤒખꤐꤌળ, ӄꤌӄ ꤍ γተрꤕꤟꤌ ӄ꤀ϕꤕꤕӄ, ꤙрꤎ𐌼 ꤕё ꤀પӄ꤀ ꤒ꤀მрꤣተ ꤍ γተрꤌ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤕꤒꤎ ꤅рꤣꤙꤙ꤀𐌼 ઞꤕ ꤐ ωӄ꤀𐌻ꤕ उꤌрꤌउꤣ𐌻ꤣ, ተખ ꤙр꤀ꤍተ꤀ ӄ꤀꤅მꤌ 𑀋γ꤇ ꤍ꤀ꤍꤌ𐌻 उꤌрꤌउꤣ𐌻ꤍꤎ ꤀ተ ꤍꤐ꤀ꤕ꤅꤀ ꤀ተꤟꤌ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤌ ተખ उઞꤌ𐌻, પተ꤀ ꤐꤣપ ꤙꤕрꤕმꤌёተꤍꤎ ꤙ꤀ ꤀પӄγ ꤣ ꤐꤌ꤅ꤣઞꤕ, ꤐ꤀ተ ꤎ ӄ꤀꤅მꤌ ꤕꤒꤌ𐌻 ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤒꤕउ ꤅ꤌઞმ꤀ઞꤌ ,ꤍተ꤀ рꤌउ ꤙꤕрꤕӄрꤕꤍተꤣ𐌻ꤍꤎ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀પꤕ𐌼γ ተꤐ꤀꤇ ተр꤀𐌻𐌻ꤣઞ꤅ ተꤌӄ꤀꤇ ተ꤀ઞӄꤣ꤇?) ꤙ꤀ ઞꤕ𐌼γ ꤙ꤀ꤕउმ ꤙр꤀ꤕ𑀋ꤌ𐌻 ꤣ𐌻ꤣ ઞꤌ ઞꤕ꤅꤀ ꤍ𐌻꤀ઞ ꤍꤕ𐌻? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤒ𐌻ꤎმ𑀨 ઞꤌωё𐌻 ተꤐ꤀ળ 𐌼ꤌ𐌼ꤌωӄγ ઞꤌ ተрꤌꤍꤍꤕ, ӄꤌӄ ꤍ꤀ተӄγ ꤐ उꤣ𐌼ઞꤕ꤇ ӄγрተӄꤕ, рꤌउઞꤣꤟꤌ ꤒ꤀𐌻𑀨ωꤌꤎ, ઞ꤀ рꤌმ꤀ꤍተ𑀨 ꤀მꤣઞꤌӄ꤀ꤐꤌꤎ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤌ𑀋ꤌ,ળઞખ꤇ მꤕ꤅рꤌმꤌઞተ γ ӄ꤀ተ꤀р꤀꤅꤀ ꤯ᱧ рꤌउ𐌼ꤕрꤌ ꤍ પ𐌻ꤕઞꤌ ꤍ꤀ꤒꤌӄꤣ მγ𐌼ꤌꤕተ, પተ꤀ ተр꤀𐌻𐌻ꤣተ𑀨 γ𐌼ꤕꤕተ? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤀ωꤣꤒꤌꤕω𑀨ꤍꤎ, ꤎ 𐌼꤀꤅γ ተꤐ꤀ળ 𐌼ꤌ𐌼ꤌઞ𑀨ӄγ ꤕꤒꤌተ𑀨 ꤅꤀მ, ꤐખმꤕр𐌟ӄꤌ, ӄꤌӄ γ рተꤌ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤐ꤀ተ ꤍ𐌼꤀ተрꤣ,ተખ ꤀მꤣઞ꤀ӄ, ꤐꤕმ𑀨 𐌼꤀꤇ 𑀋γ꤇ ઞꤕ उꤌ꤅𐌻ꤎმખꤐꤌꤕተ ꤒ꤀𐌻𑀨ωꤕ ꤐ ተꤐ꤀꤇ р꤀ተ ઞꤌ પꤌ꤇,ተꤕꤒꤕ ꤅рγꤍተઞ꤀, ꤐꤕმ𑀨 𐌼꤀꤇ 𑀋γ꤇ ꤀ӄ꤀ઞપꤣ𐌻 ꤀ተઞ꤀ωꤕઞꤣꤕ ꤍ ተꤐ꤀ꤕ꤇ ꤅γꤒ꤀꤇, ꤀ઞꤣ ꤒ꤀𐌻𑀨ωꤕ ઞꤕ ꤙꤌрꤌ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ω𐌻ꤣ ઞꤌ 𐌼꤀ઞꤕተઞખ꤇ მꤐ꤀р,ተખ γउઞꤌꤕω𑀨 उꤌ પተ꤀ ꤙ꤀ӄγꤙꤌળተ ተꤐ꤀ળ 𐌼ꤌተ𑀨, ꤙр꤀ꤍተꤣ,ꤎ ઞꤕ 𑀋꤀ተꤕ𐌻 ተꤕꤒꤎ ꤀ꤒꤣმꤕተ𑀨, ઞ꤀ р꤀ተ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ,ӄꤌӄ ꤙр꤀𑀋꤀მઞ꤀꤇ მꤐ꤀р, ઞγ 𑀋γꤣ પꤌꤍተ꤀ उꤌ꤅𐌻ꤎმખꤐꤌળተ ઞꤌ પꤌ꤇) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] მ꤀ꤙγꤍተꤣ𐌼,ꤎ ꤐખꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨,ꤌ მꤌ𐌻𑀨ωꤕ પተ꤀?) ꤎ 𐌟ꤕ ꤒр꤀ωγ ꤕё, ꤀ઞꤌ 𑀋γꤕተꤌ ꤒ𐌻ꤎ, ꤎ ઞꤕ ꤒγმγ ꤍ ઞꤕ꤇ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤒ𐌻ꤎ, પγꤐꤌӄ, ӄꤌӄ ꤒખ ꤍӄꤌउꤌተ𑀨 𐌼ꤎ꤅પꤕ, ઞγ ꤕꤒꤌ𐌻 ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨,ꤣ પ꤀?) ꤍӄꤌઞმꤌ𐌻 उꤌꤐ꤀მꤣተ𑀨? ) ઞꤌ𑀋γ꤇ ꤍተ꤀𐌻𑀨ӄ꤀ ωγ𐌼ꤌ ꤙ꤀მઞꤣ𐌼ꤌተ𑀨 ꤣउ उꤌ ተ꤀꤅꤀, પተ꤀ ꤎ ꤕꤒꤌ𐌻 ተꤐ꤀ળ 𐌼ꤌተ𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤐ꤀ተ ꤍ𐌼꤀ተрꤣ,ꤍꤕ꤇પꤌꤍ ꤎ ꤒγმγ მꤌꤐꤌተ𑀨 𑀋γꤕ𐌼 ተꤐ꤀ળ 𐌼ꤌተ𑀨,ӄꤌӄ ꤒγ𐌻𑀨მ꤀उꤕр,ꤒ𐌻ꤎ)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙꤍꤣ𑀋ꤣપꤕꤍӄꤣ ꤒ꤀𐌻ꤕઞ?) ꤍተꤌꤐꤣω𑀨 ꤍꤐ꤀ё ꤀પӄ꤀ ꤙꤕрꤕმ ઞꤕ꤅р꤀𐌼 ꤒ꤀𐌻ꤕળ൰ꤣ𐌼 ᤋꤒ꤀𐌻꤀꤇ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙꤣउმꤕꤟ, ተખ ઞꤕ꤅рꤕተꤕઞ꤀ӄ ꤍ ӄꤌ𐌼ꤕрγઞꤌ ӄ꤀ተ꤀рખ꤇ ꤍተр꤀ꤣተ ꤣउ ꤍꤕꤒꤎ ꤒꤕ𐌻꤀꤅꤀, ተખ उꤌꤙγተꤌ𐌻ꤍꤎ ꤐ рꤌꤍꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍ𐌼꤀ተрꤣ, 𐌼꤀꤇ 𑀋γ꤇ ꤀ተӄрખ𐌻 ӄ꤀𐌻𐌻ꤕმ𐌟 ꤙ꤀ ꤀ꤒγપꤕઞꤣળ 𐌼ꤌ𐌼ꤌωꤕӄ ꤙррꤍተꤣተγꤟꤣꤣ, ꤙ꤀પꤕ𐌼γ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤙꤕрꤐખ꤇ ꤌꤒꤣተγрꤣꤕઞተ? ) ꤀ઞꤌ ꤍӄ𐌻꤀ઞꤎꤕተꤍꤎ ӄ ω𐌻ળ𑀋ꤣઞꤣउ𐌼γ ꤣ рꤌӄ꤀ꤐꤌઞꤣળ? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙꤣउმꤕꤟ ꤀ઞꤌ ꤙγउꤌተꤌꤎ 𐌼ખ𐌼рꤌ ꤍ ተꤕрꤙӄꤣ𐌼 ꤌр꤀𐌼ꤌተ꤀𐌼 ꤐꤌउꤣ𐌻ꤣઞꤌ ꤀ተ ꤀પӄꤌ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍ𐌼꤀ተрꤣ, ꤐ꤀ተ ተખ 𐌟ꤕ ꤙ꤀𐌻γપꤣω𑀨 ተрꤣ ઞ꤀𐌟ꤕꤐખ𑀋 ꤐ ꤅꤀р𐌻꤀ ꤣउ उꤌ ꤣउઞꤌꤍꤣ𐌻꤀ꤐꤌઞꤣꤎ ꤍꤐ꤀ꤕ꤇ рγӄꤣ ꤣ ꤅γꤒખ,მγрꤌપ꤀ӄ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤐ꤀ተ ꤍ𐌼꤀ተрꤣ, ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ӄγꤙꤣ𐌻ꤌ ꤌꤒ꤀ઞꤣ𐌼ꤕઞተ ꤐ 𐌼ꤌꤍꤍꤌ𐌟ઞγળ ӄ𐌻ꤣઞꤣӄγ, પተ꤀ꤒ ꤙ꤀ꤍꤌꤍખꤐꤌተ𑀨 ተꤌ𐌼 ꤐꤍꤕ𐌼 𑀋γꤣ,ꤙꤣउმꤕꤟ, 𑀋꤀მꤣተ 𐌼ꤌꤍꤍꤌ𐌟ꤣр꤀ꤐꤌተ𑀨 𑀋γ꤇ ꤣ ꤅γꤒખ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙꤣउმꤕꤟ, ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 𐌼ઞꤕ ꤙ꤀उꤐ꤀ઞꤣ𐌻ꤌ ꤣ ꤍӄꤌउꤌ𐌻ꤌ  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤌꤒ꤀ઞꤕઞተ ꤐрꤕ𐌼ꤕઞઞ꤀ ઞꤕ 𐌼꤀𐌟ꤕተ ꤀ተꤍ꤀ꤍꤌተ𑀨 ꤐꤌ𐌼 𑀋γ꤇, ꤀ઞ ꤙрꤣꤕმꤕተ ꤙ꤀उ𐌟ꤕ ). ꤎ ꤌ𐌟 ꤌ𑀋γꤕ𐌻, 𐌼ઞꤕ ꤐꤙꤕрꤐખꤕ ተꤌӄ ꤍрꤌउγ ꤙрꤕმ𐌻꤀𐌟ꤣ𐌻ꤌ ꤀ተꤍ꤀ꤍ ꤒꤌꤒꤌ ӄ꤀ተ꤀рγળ ઞꤣӄ꤀꤅მꤌ ઞꤕ ꤐꤣმꤕ𐌻 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤐ꤀ተ પተ꤀ ተખ ꤐપꤕрꤌ ꤐꤣმꤕ𐌻 उꤌ γ꤅𐌻꤀𐌼 მ꤀𐌼ꤌ?) ӄꤌӄ ꤎ ꤕꤒꤌ𐌻 ተꤐ꤀ળ 𐌼ꤌተ𑀨?) ꤐ ᤋተ꤀𐌼 ઞꤣપꤕ꤅꤀ ઞꤕተ,γ ઞꤕё ꤒꤕωꤕઞꤍተꤐ꤀ 𐌼ꤌተӄꤣ ꤣ ꤎउખӄꤌ, ꤒખꤐꤌꤕተ ተꤌӄ꤀ꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼꤀꤇ 𑀋γ꤇ ꤀ꤍተꤌꤐꤣ𐌻 ꤐꤙꤕપꤌተ𐌻ꤕઞꤣꤕ ተꤐ꤀ꤕ꤇ ꤅γꤒꤕ? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤀ઞ ꤕё ꤕꤒꤌ𐌻,ӄꤌӄ ઞꤣӄተ꤀ ઞꤕ ꤕꤒꤌ𐌻,ꤙр꤀ꤍተ꤀ ꤙ꤀ꤕꤒꤌ𐌻,ӄꤌӄ ꤒ꤀꤅) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤐપꤕрꤌ 𐌼꤀꤇ 𑀋γ꤇ ꤐउꤎ𐌻 ተꤐ꤀ળ ꤅γꤒγ ઞꤌ ꤀ꤒ꤀рმꤌ𐌟 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤀ઞ მ꤀𐌻꤅꤀ მрꤌ𐌻ꤍꤎ ꤍ ઞꤕ꤇, ꤣ ꤙ꤀ꤒꤕმꤣ𐌻 ተрꤕ𐌼ꤎ उꤌ𐌻ꤙꤌ𐌼ꤣ, ተꤐ꤀ꤎ ꤅γꤒꤌ ꤒખꤍተр꤀ ꤍმꤌ𐌻ꤌꤍ𑀨 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤙрꤎ𐌼 ꤌꤒ꤀рꤣ꤅ꤕઞ,ꤐተ꤀р꤅ꤍꤎ ꤐ მ𐌟γઞ꤅𐌻ꤣ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ӄꤣ, ተખ ꤙ꤀ઞꤎ𐌻 ꤀ પꤕ𐌼 ꤎ)) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤒ𐌻ꤎ,ተખ ઞꤌꤐꤕрઞ꤀ ꤕმꤣઞꤍተꤐꤕઞઞખ꤇ उꤌр꤀მખω ӄ꤀ተ꤀рખ꤇ ꤐખ𐌟ꤣ𐌻 ꤙ꤀ꤍ𐌻ꤕ ꤌꤒ꤀рተꤌ, ઞꤌꤐꤕрઞ꤀ꤕ उꤐγપꤣተ ꤍተꤌр꤀ ꤣ ꤒꤌઞꤌ𐌻𑀨ઞ꤀, ઞ꤀ ተખ 𐌟ꤕрተꤐꤌ ꤀ꤒ꤀рተꤌ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍ𐌻ખω, ተખ ꤌꤒ꤀рተꤣꤐઞખ꤇ მꤌγઞ, γ ተꤕꤒꤎ рꤌउꤐꤣተꤣꤕ ઞꤌપꤌ𐌻꤀ ꤍӄꤌተખꤐꤌተ𑀨ꤍꤎ ӄ ઞγ𐌻ળ, ተખ ꤍ ӄꤌ𐌟მ꤀꤇ ꤍꤕӄγઞმ꤀꤇ ꤅𐌻γꤙꤕꤕ, ꤣ ተγꤙꤕꤕ,ꤙ꤀ꤐꤌმӄꤣ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ӄꤍተꤌተꤣ,꤀ઞꤌ ተ꤀𐌟ꤕ მꤕ꤅рꤌმꤣрγꤕተ, ꤕ꤇ ꤅꤀ꤐ꤀рꤣω𑀨 - ꤙрꤣઞꤕꤍꤣ ꤙ꤀ꤙꤣተ𑀨.ꤌ ꤀ઞꤌ ӄ 𑀋γળ, ꤣ ꤍ꤀ꤍꤌተ𑀨 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙꤣउმꤕꤟ ተખ ꤒꤌꤒꤌ, ꤎ ተр꤀𐌻𐌻ꤣተ𑀨 ઞꤌપꤣઞꤌળ ተ꤀𐌻𑀨ӄ꤀, ꤌ ተખ γ𐌟ꤕ ઞ꤀ꤕω𑀨, ꤎ მꤌ𐌟ꤕ ઞꤕ рꤌउ꤀꤅рꤕ𐌻ꤍꤎ ꤕ൰ё ))) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤌ𐌻𐌻꤀, ꤒ𐌻ꤎმ𑀨,ӄꤌӄꤌꤎ ꤍꤐꤌმ𑀨ꤒꤌ? ) ተγተ ꤙ꤀ꤕꤒꤌ𐌻, ꤒр꤀ꤍꤣ𐌻, ꤎ ઞꤕ ꤒγმγ 𐌟ꤕઞꤣተ𑀨ꤍꤎ ઞꤌ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ӄꤕ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ઞꤕ ઞꤌმꤕ꤇ꤍꤎ ꤀ተꤍ꤀ꤍꤌተ𑀨 𐌼ઞꤕ 𑀋γ꤇,ꤎ ꤒ꤀𐌻𑀨ωꤕ ઞꤕ ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨,ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωӄꤕ ተ꤀ 𐌟ꤕ ꤍꤌ𐌼꤀ꤕ ꤙꤕрꤕმꤌ꤇, પተ꤀ꤒ उꤌꤐተрꤌ ઞꤕ ꤙрꤣ𑀋꤀მꤣ𐌻ꤌ, ꤌ, მꤌ,ꤍ ꤒꤌрმꤕ𐌻ꤎ ꤀ઞꤌ ተ꤀𐌟ꤕ γꤐ꤀𐌻ꤕઞꤌ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ પ꤀ ተꤌ𐌼,उꤌმγ𐌼ꤌ𐌻ꤍꤎ?) მγ𐌼ꤌꤕω𑀨 ꤀ 𐌼꤀ꤕ𐌼 𑀋γꤕ,ӄꤍተꤌተꤣ, ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωӄꤕ 𐌼꤀꤇ 𑀋γ꤇ ተ꤀𐌟ꤕ ꤍઞꤣተꤍꤎ, ꤣ ꤍઞꤣተꤍꤎ ተ꤀,ӄꤌӄ ꤎ ꤕꤒꤌ𐌻 ꤕё ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] მꤌ ተખ उꤌꤕꤒꤌ𐌻, γઞખ𐌻ખ꤇ 𑀋γꤕꤍ꤀ꤍ, ተખ પ꤀ ተꤌ𐌼 𐌼ꤎ𐌼𐌻ꤣω𑀨? ) ተખ მγ𐌼ꤌꤕω𑀨 ꤍ𐌻ꤣተ𑀨 𐌼ꤕઞꤎ? ) ꤙ꤀ꤍ𐌼꤀ተрꤣ ተ꤀, પተ꤀ ꤙꤣωγ ꤎ,ꤌ ꤙ꤀ተ꤀𐌼 ઞꤌ ꤍꤐ꤀ё მꤕр𑀨𐌼꤀,მꤌ,ꤎ ተ꤀𐌟ꤕ ઞꤕ ꤣმꤕꤌ𐌻, ઞ꤀ ተખ ꤐ꤀꤀ꤒ൰ꤕ ꤕꤒγપꤕꤕ ꤅꤀ꤐઞ꤀ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤌ꤇, ተꤌӄ꤀𐌼γ 𑀋γꤕꤍ꤀ꤍγ, ӄꤌӄ ተખ,ꤒꤕꤍꤙ꤀𐌻ꤕउઞ꤀ ꤀ꤒъꤎꤍઞꤎተ𑀨,ተખ 𐌟ꤌ𐌻꤀ӄ ꤣ ꤅𐌻γꤙ, ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤣउꤐꤕꤍઞꤕꤕ ꤍખપꤕꤐ꤀꤇,ꤕё р꤀ተ उઞꤌ𐌼ꤕઞꤣተ ઞꤌ ꤐꤍળ р꤀ꤍꤍꤣળ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙрꤕმꤙ꤀𐌻꤀𐌟ꤣ𐌼 ተ꤀ተ ϕꤌӄተ,પተ꤀ ꤎ ꤕꤒꤌ𐌻 ተꤐ꤀ળ 𐌼ꤌተ𑀨,ઞ꤀ ꤐꤕმ𑀨 ꤎ ꤙрꤕმγꤙрꤕ𐌟მꤌ𐌻, પተ꤀ ꤒγმꤕተ ꤒ꤀𐌻𑀨ઞ꤀, მꤌ, ᤋተ꤀ પꤣꤍተꤌꤎ ꤙрꤌꤐმꤌ, ꤎ ꤐખꤕꤒꤌ𐌻 ተꤐ꤀ળ 𐌼ꤌተ𑀨, ઞꤕ ተꤕꤒꤕ 𐌼ꤕઞꤎ ꤍγმꤣተ𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙрꤣӄ꤀𐌻, ꤎ ઞꤌωё𐌻 ꤍ꤀ꤐꤙꤌმꤕઞꤣꤕ γ ተꤕꤒꤎ ꤣ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ, ꤐખ ꤀ꤒꤌ उγꤒખ ઞꤕ પꤣꤍተꤣተꤕ, ꤎ ӄ꤀꤅მꤌ ꤐꤌꤍ ઞꤌ р꤀ተ ꤕꤒꤌ𐌻, उꤌ𐌼ꤕተꤣ𐌻) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙꤣउმꤕꤟ, ꤕꤍ𐌻ꤣ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤐખꤕꤒꤌተ𑀨 ꤀ઞꤌ ꤙрꤕꤐрꤌተꤣተꤍꤎ ꤐ ӄрꤌꤍꤌꤐꤣꤟγ? ) ᤋተ꤀ ተꤌӄ,ꤙр꤀ꤍተ꤀ ꤐ꤀ꤙр꤀ꤍ,પተ꤀ꤒ ઞꤌꤐꤕрઞꤎӄꤌ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤕꤒꤌተ𑀨, ꤐ꤀ተ ꤎ ተꤌӄ꤀꤇ પꤕ𐌻꤀ꤐꤕӄ ꤍተрꤌઞઞખ꤇, 𐌼꤀꤅γ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤕꤒꤌተ𑀨 𐌻ꤕተ 20, მꤌ𐌟ꤕ ꤒ꤀𐌻𑀨ωꤕ ꤕё γ𐌟ꤕ ꤕꤒγ, ꤙр꤀ꤍተ꤀ ꤒрꤌӄ,ꤎ ተꤕꤒꤕ ꤀ተપꤣ𐌼 ꤐꤍꤕ 𐌟ꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ӄ꤀꤅მꤌ ꤕꤒꤌ𐌻 ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤐ р꤀ተ उꤌ𐌼ꤕተꤣ𐌻, પተ꤀ γ ઞꤕꤕ рꤌӄ ꤅γꤒખ,ꤎ ઞꤣӄ꤀꤅მꤌ ઞꤕ उꤌꤒγმγ ᤋተγ рꤌӄ꤀ꤐγળ 𐌟ꤕઞ൰ꤣઞγ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤙꤣउმꤕꤟ მγрꤌ, ꤀მꤕ𐌻ꤌꤍ𑀨, ӄꤌӄ ӄꤣрӄ꤀р꤀ꤐ, ꤣ ꤒꤕ𐌟ꤌ𐌻ꤌ ꤐꤍꤕ𐌼 ꤍ꤀ꤍꤌተ𑀨 ꤍ꤀ ꤍ𐌻꤀ꤐꤌ𐌼ꤣ  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤒ𑀨ળ 𐌟ꤕઞ൰ꤣઞ ꤣ 𐌼ઞꤕ ꤙ꤀𑀋γ꤇ ઞꤌ ተꤐ꤀ળ 𐌼ꤌተ𑀨 !!!  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤒꤕ꤅ꤣ ꤒખꤍተрꤕꤕ, ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤌꤐꤌઞꤍ ꤐ ꤒꤌрმꤕ𐌻ꤕ ꤙ꤀𐌻γપꤣ𐌻ꤌ, ω꤀ӄ꤀𐌻ꤌმӄγ ተꤕꤒꤕ ӄγꤙꤣ𐌻ꤌ, ӄγωꤌ꤇, ઞꤕ ꤙ꤀მꤌꤐꤣꤍ𑀨 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤀მꤣઞ рꤌउ ωё𐌻 ઞꤌ ꤌꤐꤌઞተળрγ, ꤕꤒꤌ𐌻 ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤒꤕउ ꤅ꤌઞმ꤀ઞꤌ, მꤕ𐌻꤀ ꤙр꤀ω𐌻꤀ γმꤌપઞ꤀, ꤒꤕрꤕ𐌼ꤕઞઞ꤀ꤍተꤣ ઞꤕ ꤒખ𐌻꤀) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ϕγ𑀋, ઞꤌ ꤍꤐ꤀꤇ ꤍተрꤌ𑀋 ꤣ рꤣꤍӄ ꤕꤒꤌ𐌻) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤐ꤀ꤍ𑀨𐌼꤀ꤕ ꤌꤐ꤅γꤍተꤌ 2014 ꤅,ꤍꤙр꤀ꤍꤣ γ ꤍꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωӄꤣ, પተ꤀ ꤒખ𐌻꤀ ꤐ ተ꤀ተ მꤕઞ𑀨, ꤌ ꤀ઞꤌ ꤀ተꤐꤕተꤣተ, પተ꤀ ꤎ ꤕꤒꤌ𐌻 ꤕꤕ) ӄꤌӄꤣꤕ 𐌼ꤣ𐌻꤀ꤍተꤣ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙꤣउმꤕꤟ, ꤎ ꤕꤒꤌ𐌻 ተꤐ꤀ળ 𐌼ꤌተ𑀨,ӄ꤀ઞપꤌળ ꤐ р꤀ተ ꤕ꤇,ꤌ ꤀ઞꤌ ተꤌӄꤌꤎ - ӄγმꤌ ꤒꤌ꤅ꤌ𐌟? ) ꤌ ꤎ ተꤌӄ꤀꤇, ꤅𐌻꤀ተꤌ꤇ ꤐꤕꤍ𑀨 ꤅рγउ)꤀ઞꤌ ተꤌӄꤌꤎ 𐌼꤀𐌟ꤕተ ઞꤌ ꤒꤌ꤅ꤌ𐌟ઞꤣӄ ꤙꤕрꤕꤙ𐌻ળઞγተ𑀨,ꤌ ꤎ ተꤌӄ꤀꤇ - ꤅𐌻ꤌተꤌተ𑀨, उઞꤌપ ꤅𐌻ꤌተꤌ꤇. [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤣ𑀋ꤣ𑀋,ꤙꤣउმꤌተ꤀,მꤌ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤒ𐌻ꤎმ𑀨 ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ተꤕꤒꤎ ꤐӄꤌપꤌꤕተ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ उઞꤌ𐌻, પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤎ उꤌӄꤣઞγ ꤐ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ, ꤒγმተ꤀ 𐌼ꤎપꤣӄ ꤐ ӄ꤀рउꤣઞγ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀꤅꤀მꤣ, ꤎ ꤕ൰ё ઞꤕ рꤌउ꤀꤅рꤕ𐌻ꤍꤎ,ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤐ ꤍӄ𐌻ꤕꤙꤕ ꤕꤒꤌ𐌻 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼꤀꤇ 𑀋γ꤇ ꤐ ꤀પӄꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ उ꤀𐌻꤀ተ꤀ მ꤀ꤒખꤐꤌꤕተ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤐ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ተખӄꤐγ ꤙ꤀ꤍꤌ𐌟γ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ઞꤌ𑀋γ꤇ ꤙ꤀მꤍ꤀𐌻ઞγ𑀋꤀𐌼 ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼꤀꤇ 𑀋γ꤇ ꤒ꤀𐌻ተꤌꤕተ ꤍ ꤀પӄ꤀𐌼 ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤕꤒγ,ꤌ ተખ ꤐꤍꤌꤍખꤐꤌꤕω𑀨 𐌼꤀꤇ 𑀋γ꤇) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ઞꤌ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ꤙ꤀ꤍተꤌꤐꤣ𐌻 ተꤌꤒ𐌻ꤣપӄγ ꤐ𑀋꤀მ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ё ꤌઞꤌ𐌻𑀨ઞ꤀ꤕ ꤀ተꤐꤕрꤍተꤣꤕ ꤅꤀рꤣተ ꤀ተ 𑀋γꤕꤐ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼꤀꤇ 𑀋γ꤇ მ꤀ꤍተꤣ꤅ ꤙрꤕმꤕ𐌻ꤌ ᤋꤐ꤀𐌻ળꤟꤣꤣ ꤐ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ተꤐ꤀ё ꤀પӄ꤀ ꤐ ӄ꤀𐌼ꤙрꤕꤍꤍ꤀р꤀𐌼 рꤌꤍ𑀋γꤎрળ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ 𐌟ꤕ ꤙ꤀𐌻꤀ꤐખꤕ ꤅γꤒӄꤣ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ꤐ მр꤀ꤒꤣተꤕ𐌻𑀨 उꤌꤍγઞγ, ꤣ ꤍმꤕ𐌻ꤌળ ϕꤌрω მ𐌻ꤎ ተꤕꤒꤎ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼꤀꤇ પ𐌻ꤕઞ ተꤌӄ ᤋϕϕꤕӄተઞ꤀ ꤍӄ꤀𐌻𑀨उꤣተ ꤙ꤀ ተꤐ꤀ꤣ𐌼 ꤎ꤇ꤟꤌ𐌼) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤕꤒꤌተ𑀨 ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤍγተ𑀨 𐌼꤀ꤕ꤇ 𐌟ꤣउઞꤣ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ ꤅γꤒꤌ ઞꤌ 𐌼꤀ꤕ𐌼 પ𐌻ꤕઞꤕ ӄγ𐌻𑀨ꤙꤣተખ მꤕ𐌻ꤌꤕተ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤕꤒꤌተ𑀨 ተꤐ꤀ળ 𐌼ꤌተ𑀨 рꤌꤒ꤀ተꤌ 𐌼꤀ꤎ?) ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤐ ꤍ꤀𐌻ꤎрꤣꤣ ꤣઞϕ꤀ӄрꤌꤍઞખ𐌼 𐌻γપ꤀𐌼) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤙꤣउმꤌӄ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ მꤐꤕр𑀨ળ ꤙрꤣ൰ꤕ𐌼ꤣ𐌻) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤀ꤒ ꤙꤣउმꤌӄ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ꤐꤌउγ ꤒꤣ𐌻,γ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ተꤕꤙꤕр𑀨 𑀋рγꤍተꤌ𐌻𑀨ઞꤌꤎ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀꤇ ꤎउખӄ 𑀋꤀მꤣተ ᤋϕϕꤕӄተઞ꤀ ꤙ꤀ 𐌼꤀ꤕ𐌼γ 𑀋γળ,ӄꤌӄ ꤙγ꤅ꤌપꤕꤐꤌ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𑀋γꤕ𐌼 ꤙ꤀ꤍተꤌꤐ𐌻ળ ተꤕꤒꤎ ઞꤌ рꤌꤍꤍተрꤕ𐌻,ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤐꤌ൰ꤕ ꤐӄγрꤍꤕ, પተ꤀ ꤎ ꤕꤒꤌ𐌻 ተꤎ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ઞꤕተ,ઞγ ተꤐ꤀ё ꤀પӄ꤀ ተꤌӄ ꤙꤣउმꤌተ꤀ ꤙрખ꤅ꤌꤕተ ꤍ 𑀋γꤎ ઞꤌ 𑀋γ꤇) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙр꤀მ꤀𐌻𐌟ꤣω𑀨 𑀋γ꤇ ꤍ꤀ꤍꤌተ𑀨?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍ𐌻ખω,ተꤍꤍ,ተꤣ𑀋ꤌ,ꤎ ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨,ᤋተ꤀ ꤍꤕӄрꤕተ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ઞꤕ 𑀋꤀પγ ተꤕꤒꤕ ꤙ꤀рተꤣተ𑀨 ꤙрꤌउმઞꤣપઞ꤀ꤕ ઞꤌꤍተр꤀ꤕઞꤣꤕ, उꤌꤐተрꤌ ꤍӄꤌ𐌟γ,પተ꤀ 𐌼ꤌተ𑀨 ተꤐ꤀ળ ꤕꤒꤌ𐌻) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] მꤌꤐꤌ꤇ ተખ ꤍγӄꤌ 𐌼꤀꤇ 𑀋γ꤇ ꤒγმꤕω𑀨 ꤒખმꤌተ𑀨 ꤎउખӄ꤀𐌼,ӄꤌӄ ꤒખӄ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ઞꤌꤕउმઞꤣӄ 𑀋γꤎ 𐌼꤀ꤕ꤅꤀?) ӄꤌꤐꤒ꤀꤇ ꤕꤒꤌઞખ꤇, 𑀋ꤐꤌተꤣተ ꤍӄ꤀ӄꤌተ𑀨 ઞꤌ 𐌼꤀ꤕ𐌼 𑀋γળ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ 𐌟ꤕ उꤌ 𐌼꤀ꤣ𐌼 𑀋γꤕ𐌼, ӄꤌӄ ꤍ꤀ꤒꤌӄꤌ उꤌ ꤙꤌ𐌻ӄ꤀꤇) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍ꤀𑀋рꤌઞꤣ 𐌼꤀꤇ 𑀋γ꤇,ꤟꤕઞઞખ꤇ ᤋӄꤍꤙ꤀ઞꤌተ,მꤐꤌ ꤎ꤇ꤟꤌ ϕꤌꤒꤣр𐌟ꤕ, ꤣ ꤐꤕઞꤍӄꤣ꤇ ꤌ𐌻𐌼ꤌउ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ተખ ꤐӄꤌપꤣꤐꤌꤕω𑀨ꤍꤎ 𐌼꤀ꤣ𐌼 𑀋γꤕ𐌼?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ઞꤕ ተр꤀𐌻𐌻𑀨,ተખ ઞꤕ γ𐌼ꤕꤕω𑀨, ተખ 𐌻꤀𑀋 ꤀ꤒъꤕꤒꤌઞઞખ꤇ [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ 𐌟ꤕ ꤐꤕꤍ𑀨 ተꤐ꤀꤇ 𐌻꤀ꤒӄ꤀ꤐ꤀꤇ ꤙрꤣተ꤀ઞ उઞꤌળ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍ𐌻ખω,ӄꤌꤍꤙꤕр, ꤙрꤣꤐꤣმꤕઞꤣꤕ ꤕꤒꤌઞ꤀ꤕ,ተખ ꤕ൰ё ઞꤕ ꤣꤍꤙꤌрꤣ𐌻꤀ꤍ𑀨? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ ꤅γꤒꤌ ተꤣꤙ꤀ მꤕ𐌼꤀ઞ ӄ꤀ተ꤀рખ꤇ 𑀋꤀પꤕተ ꤙ꤀рꤌꤒ꤀ተꤣተ𑀨 𐌼꤀ꤣ ꤎ꤇ꤟꤌ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤌ𐌻𐌻꤀, р꤀ꤒꤕрተ꤀ მꤌγઞ 𑀋γ꤇𐌻ꤌઞ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼꤀꤇ 𑀋γ꤇ ꤙрꤎ𐌼 उγꤒઞꤌꤎ ꤍપꤕተӄꤌ, ꤀ተꤒꤕ𐌻ꤣ𐌻 ተꤐ꤀ꤣ उγꤒખ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤀,ተꤌӄ ተખ рꤕωꤣ𐌻 ꤐꤍё ተꤌӄꤣ ꤐӄγꤍꤣተ𑀨 ꤙ𐌻꤀მખ 𑀋γꤎ 𐌼꤀ꤕ꤅꤀? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, ꤎ ꤒ𐌻ꤎმ𑀨 ꤐ ተꤕꤒꤎ उꤌꤙγ൰γ ꤍ ተрγꤍ꤀ꤐ,ӄꤌӄ р꤀꤅ꤌმӄ꤀꤇, 𑀋γꤕ𐌼,γ𐌻ꤕተꤣω𑀨 ઞꤌ𑀋γ꤇, ӄꤌӄ ꤀ተ ꤍꤌ꤇꤅ꤣ))) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ተꤕꤒꤎ उꤌმγωγ ተрγꤍꤌ𐌼ꤣ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤐӄγрꤍꤕ, પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 рꤌꤍꤍωꤐખрꤣꤐꤌꤕተ 𑀋γꤣ ꤙ꤀ ꤍꤐ꤀ꤣ𐌼 მખрӄꤌ𐌼?) ꤎ 𐌟ꤕ ꤒ𐌻ꤎმ𑀨 ተꤕꤒꤎ 𐌼꤀꤅γ ꤕꤒꤌተ𑀨 𑀋꤀ተ𑀨 ꤍγተӄꤣ,ተખ 𐌟ꤕ उઞꤌꤕω𑀨, પተ꤀ ተꤐ꤀ꤎ ꤅γꤒꤌ ઞꤕ ꤍꤣ𐌻𑀨ઞꤕꤕ 𑀋γꤎ 𐌼꤀ꤕ꤅꤀ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] )ᤋተ꤀ ተખ ተꤣꤙꤌ ተрꤌ𐌻𐌻ꤣω𑀨?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] )მꤌꤐꤌ꤇ ꤎ ꤙр꤀ꤍተ꤀ ꤐъꤕꤒγ 𑀋γꤕ𐌼 ꤐ ꤅𐌻ꤌउ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ, ꤣ 𐌼ઞꤕ მꤌმγተ ꤙ꤀მꤙꤣꤍӄγ ꤀ ઞꤕ ꤐખꤕउმꤕ 𑀋γꤎ ꤣउ ꤕё рተꤌ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] მꤕ꤅рꤌმꤌઞተ ꤍ 𐌼ꤌ𐌻ꤕઞ𑀨ӄ꤀꤇ ꤙꤣꤍ𑀨ӄ꤀꤇? )𐌼꤀꤇ 𑀋γ꤇ ꤍꤙꤌꤍꤕተ ተꤕꤒꤎ ꤀ተ ӄрꤣउꤣꤍꤌ,ꤐ ተꤐ꤀ꤕ꤇ მખрꤕ उꤌрꤌઞꤣꤕ उꤌꤙꤌꤍγተꤍꤎ 𑀋γꤣ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] მꤕ꤅рꤌმꤌઞተ ꤍ 𐌼ꤌ𐌻ꤕઞ𑀨ӄ꤀꤇ ꤙꤣꤍ𑀨ӄ꤀꤇? )ꤙꤣउმꤌӄ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ꤙрꤎ𐌼,ӄꤌӄ ӄрꤌꤍઞખ꤇ ተꤕр𐌼ꤣઞꤌተ꤀р, ꤀ઞꤌ ӄрꤌꤍઞꤌꤎ 𐌼ꤌωꤣઞꤌ ӄ꤀ተ꤀рꤌꤎ ꤍӄꤌપꤕተ ઞꤌ 𐌼꤀ꤕ𐌼 𑀋γꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤒꤕрꤕउꤌ ꤕꤒꤌઞꤌꤎ?) ꤎ ꤣउ ተꤕꤒꤎ 𑀋γ꤇ ꤐખрꤕ𐌟γ მ𐌻ꤎ ꤀પӄꤌ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤐӄγрꤍꤕ,પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ γმꤌ𐌻ꤎ𐌻 ተꤕꤒꤕ ꤅𐌻ꤌઞმખ,ꤙ꤀ተ꤀𐌼γ પተ꤀ ꤙ꤀ ꤒ𐌻ꤣउ꤀ꤍተꤣ ꤐ рꤕ꤅ꤣ꤀ઞꤕ ઞꤕ ꤒખ𐌻꤀ 𑀋ꤣрγр꤅ꤣꤣ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>]  მ꤀ꤒр꤀ꤕ γተр꤀ " ተꤐ꤀ꤎ 𐌼ꤌ𐌼ꤌઞ ӄрꤣપꤣተ 𐌼꤀ꤕ𐌼γ 𑀋γળ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] მꤌꤐꤌ꤇ ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ઞꤌγપγ ꤍ𐌻꤀꤅ꤌተ𑀨 𑀋γꤣ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ઞꤕተ,ઞγ ተખ 𐌼꤀𐌻꤀მꤕꤟ, उꤌꤐꤕрઞγ𐌻 𐌼꤀꤇ 𑀋γ꤇ ꤐ 𐌻ꤌꤐꤌω,ꤣ ꤙ꤀მꤌ𐌻 ꤍꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ꤅ꤕр𐌻ꤎઞმ꤀꤇ γӄрꤌꤍꤣ𐌻 ꤙꤣउმꤌӄ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ, પተ꤀ꤒ ꤕꤒꤌተ𑀨 ꤕё ꤐ ꤙрꤌउმઞꤣપઞ꤀𐌼 ઞꤌꤍተр꤀ꤕઞꤣꤣ ))) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ 𐌼ꤣр꤀ꤐ꤀꤇ ꤍγმ𑀨ꤎ ꤣ𐌼ꤕઞꤣ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ꤙ꤀მꤌ𐌻 ꤣꤍӄ ꤙр꤀ተꤣꤐ ꤙꤣउმખ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ,꤀ઞ рꤕωꤣ𐌻 ꤐउખꤍӄꤌተ𑀨 ꤐꤍё ꤣ𐌼γ൰ꤕꤍተꤐ꤀ ꤍ ꤕё ꤙꤣउმખ, 𐌻꤀ꤒӄ꤀ꤐખꤕ ꤐ꤀𐌻꤀ꤍꤌ,ꤣ 𐌻ꤣተр 𐌼꤀ꤕ꤇ ꤍꤙꤕр𐌼ખ ӄ꤀ተ꤀рγળ ꤀ઞꤌ γӄрꤌ𐌻ꤌ))) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤍተꤌꤐꤣ𐌻 ӄрꤣተꤣપꤕꤍӄꤣꤕ γꤍ𐌻꤀ꤐꤣꤎ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ,ꤐꤕმ𑀨 ꤕꤒꤌተ𑀨ꤍꤎ ઞꤌ 𐌻ꤕმઞꤣӄꤌ𑀋 ᤋꤐꤕрꤕꤍተꤌ ӄрꤌ꤇ઞꤕ ꤀ꤙꤌꤍઞ꤀ მ𐌻ꤎ 𐌟ꤣउઞꤣ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] მꤕ꤅рꤌმꤌઞተ ꤍ 𐌼ꤌ𐌻ꤕઞ𑀨ӄ꤀꤇ ꤙꤣꤍ𑀨ӄ꤀꤇? )𐌼꤀꤇ 𑀋γ꤇ ꤒ𐌻ꤎმ𑀨 ꤀ተꤙрꤌꤐꤣተ ተꤐ꤀ꤣ उγꤒખ ꤐ ઞꤕꤙрꤌꤐꤣ𐌻𑀨ઞ꤀ꤕ рꤌꤐꤕઞꤍተꤐ꤀, ተ꤀ ꤕꤍተ𑀨,20 उγꤒ꤀ꤐ γ ተꤕꤒꤎ ꤀ꤍተꤌ𐌻꤀ꤍ𑀨 ꤙ꤀ꤍ𐌻ꤕ მрꤌӄꤣ ተꤐ꤀ꤕ꤇ પꤕ𐌻ળꤍተꤣ ꤍ 𐌼꤀ꤣ𐌼 𑀋γꤕ𐌼) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼꤀꤇ 𑀋γ꤇ ꤀ተꤙрꤌꤐ𐌻ꤎ𐌻 ተꤕꤒꤎ მ꤀ પꤣ𐌻ꤣ,પተ꤀ꤒ ተખ 𐌼꤀꤅ γꤐꤣმꤕተ𑀨 ꤐꤍꤕ ӄрꤌꤍ꤀ተખ 𐌼ꤣрꤌ ઞꤌ 𐌼꤀ꤕ𐌼 𑀋γꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤕꤒꤎ ተр꤀𐌻𐌻ꤣተ𑀨 𐌼ꤌ𐌼ӄꤌ γપꤣ𐌻ꤌ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼ꤌꤍ𐌻꤀ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ?) ꤎ 𐌟ꤕ ꤍ𐌼ꤌ𐌟γ 𑀋γ꤇ ተꤐ꤀ꤣ𐌼 𐌟ꤣр꤀𐌼 ꤣ ꤙ꤀ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤒ𐌻ꤎმ𑀨 ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨,ꤕꤒ𐌻ꤌઞ, ꤙꤣउმγ꤇ ꤍળმꤌ, પ𐌼꤀ उꤌꤎმ𐌻꤀ꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ, ӄꤌӄ ꤍખр,ꤐ꤀ઞળપӄꤌ ꤕꤒꤌઞꤌꤎ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤍγӄꤌ ꤐꤕꤍઞ꤀꤇ 𑀋γꤕ𐌼 𐌻ꤕተꤕ𐌻 ꤐ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ))) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨 उꤌ ωγꤒγ ꤕꤒꤌ𐌻) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌተ𑀨, ӄꤌӄ მрꤕꤐઞꤕ꤅рꤕપꤕꤍӄꤌꤎ ꤒ꤀꤅ꤣઞꤎ,꤀પꤕઞ𑀨 ӄрꤌꤍꤣꤐꤌ,ꤣ ꤍ꤀ꤍꤕተ 𑀋γ꤇ ተ꤀𐌻𑀨ӄ꤀ 𐌼ઞꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤍγӄꤌ ꤙꤕрꤕმ ተꤕ𐌼,ӄꤌӄ ꤙ꤀ꤕꤒꤌተ𑀨 ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤐꤍꤕ ꤍꤙрꤌꤐӄꤣ ꤍ꤀ꤒꤣрꤌ𐌻 ꤀ ꤕё उმ꤀р꤀ꤐ𑀨ꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤙꤣउმγ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤒγმγ उꤐꤌተ𑀨, ӄꤌӄ ꤙγተꤣઞꤌ,ꤍꤌ𐌼꤀꤇ પꤕꤍተઞ꤀꤇ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ, ӄꤌӄ მ꤀𐌻𐌻ꤌр, ꤙ꤀მઞꤣ𐌼ꤌꤕω𑀨ꤍꤎ ꤙ꤀ 𐌼꤀ꤕ𐌼γ рγꤒ𐌻ળ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤕꤒꤌ𐌻 ꤒꤕउ उꤌꤒ꤀ተ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤌઞꤌ𐌻ꤣउ ӄꤌ𐌻𐌻ꤌ ઞꤌ ተꤐ꤀꤇ ꤎउખӄ ꤍმꤌꤐꤌ𐌻) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ 𐌼꤀ળ 𐌼ꤌω꤀ઞӄγ ꤒрꤕꤕω𑀨 ꤎउખӄ꤀𐌼))ተખ 𐌟рꤕω𑀨 𐌼꤀꤇ ӄꤌ𐌻𐌻,ꤒγმተ꤀ ꤙꤕ𐌻𑀨𐌼ꤕઞꤣ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ઞꤌ उꤣ𐌼ઞꤣꤕ ꤙрꤌउმઞꤣӄꤣ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ 𐌟ꤕ ઞꤌ𑀋γ꤇ 𑀋γꤕ𐌼 ꤣउ꤅꤀ઞળ ꤐꤍળ ઞꤕપꤕꤍተ𑀨 ꤍ ተꤐ꤀ꤕ꤅꤀ ꤀પӄꤌ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼꤀꤇ 𑀋γ꤇ ꤙ꤀ꤍꤐꤎተꤣተ ተꤕꤒꤎ ꤐ рꤎმખ ꤕ꤅꤀ ꤍ꤀ꤍꤌተꤕ𐌻ꤕ꤇) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ 𑀋γꤣ ꤍ꤀ꤍꤕω𑀨 ተ꤀𐌻𑀨ӄ꤀ उꤣ𐌼꤀꤇?) ꤌ ተ꤀ ൰ꤌ,ꤎ પёተ ተꤐ꤀꤇ р꤀ተ ꤕꤒγ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙꤣउმꤕꤟ, ꤕꤒꤌተ𑀨 ተખ 𐌼γმрꤕꤟ 𑀋γꤎ 𐌼꤀ꤕ꤅꤀ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ϕꤣ𐌻꤀ꤍ꤀ꤐꤍተꤐγ꤇ ꤀ 𐌼꤀ꤕ𐌼 𑀋γꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ꤙ꤀მꤌрળ ઞ꤀ꤍӄꤣ ꤣ ꤒрꤣተꤐγ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ઞꤕ ꤐખꤐ꤀उꤣω𑀨 પёተ 𐌼꤀꤇ 𑀋γ꤇ ተખ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤙрꤎ𐌼 ꤌઞმ𐌟ꤕ𐌻ꤣઞꤌ მ𐌟꤀𐌻ꤣ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤕꤒꤎ 𐌼꤀꤇ 𑀋γ꤇ γꤍખઞ꤀ꤐꤣተ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤅꤀ተ꤀ꤐ𑀨 р꤀ተ,પꤕ𐌻꤀ꤐꤕӄ ꤍ꤀ꤒꤌӄꤌ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] მꤕ꤅рꤌმꤌઞተ ꤍ 𐌼ꤌ𐌻ꤕઞ𑀨ӄ꤀꤇ ꤙꤣꤍ𑀨ӄ꤀꤇? )ተખ ꤍ 𐌼꤀ꤣ𐌼 𑀋γꤕ𐌼 ꤐ ꤀ꤒઞꤣ𐌼ӄγ ꤍꤙꤌ𐌻 ઞꤌ ઞ꤀ꤐ꤀꤅꤀მઞળળ ઞ꤀પ𑀨 ))) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤕმγ ꤐ ተ꤀ተ ꤅꤀р꤀მ,꤅მꤕ ꤣꤍꤙ꤀𐌻ઞꤎળተꤍꤎ 𐌼ꤕપተખ рተꤌ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ,ꤎ ꤕꤒγ ꤕ꤅꤀) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] მꤌ ꤎ ӄꤌ𐌟მખ꤇ ꤐખ𑀋꤀მઞ꤀꤇ ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ተꤕꤒꤕ ꤙખ𐌻ꤣઞӄγ ꤍ ꤅𐌻ꤌउꤌ 𑀋γꤕ𐌼 γꤒꤕрγ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤣმꤣ ꤍ꤀ꤍꤣ 𐌼ઞꤕ 𑀋γ꤇,ꤙ꤀ӄꤌ მꤌળ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙр꤀ꤍተꤣተγተӄꤌ?) ꤍተ꤀ꤣω𑀨,ተ꤀р꤅γꤕω𑀨 ተꤕ𐌻꤀𐌼 ઞꤌ 𐌼꤀ꤕ𐌼 𑀋γꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] მꤕ꤅рꤌმꤌઞተ ꤍ 𐌼ꤌ𐌻ꤕઞ𑀨ӄ꤀꤇ ꤙꤣꤍ𑀨ӄ꤀꤇? )ઞꤕ ꤒખმꤌ꤇ 𐌼ઞꤕ ꤎ꤇ꤟꤌ ꤎउખӄ꤀𐌼, ӄ꤀उꤌ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ӄꤌӄ ꤀ꤍꤕ𐌻 ꤣउ ωрꤕӄꤌ,𐌼ઞ꤀꤅꤀ ꤙꤣउმꤣω𑀨 ꤙ꤀ӄꤌ 𐌻ꤣ𐌟ꤣω𑀨 ꤎ꤇ꤟꤌ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ӄઞꤣ꤅ꤌ 50 ꤀ተተꤕઞӄ꤀ꤐ ꤍꤕр꤀꤅꤀ ꤀ 𐌼꤀ꤕ𐌼 𑀋γꤕ𐌼 ꤣ ꤀ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼꤀꤇ 𑀋γ꤇ ઞꤌ ተꤐ꤀ꤕ𐌼 𐌻ꤣꤟꤕ ꤀ꤍተꤌꤐꤣተ ωрꤌ𐌼) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤍγӄꤌ ӄꤌ𐌻ꤌω꤀𐌼 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ઞꤌપઞγ ꤒ꤀𐌼ꤒꤣተ𑀨 ꤙꤣउმγ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ γተр꤀𐌼, ꤒγმተ꤀ 𑀋꤀𑀋𐌻ખ მઞр) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤐ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ӄꤌрꤌꤍꤕ꤇ 𐌻꤀ꤐꤣ𐌻)) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ𑀨ꤕω𑀨 ꤒꤕउ ꤀ꤍተꤌઞ꤀ꤐӄꤣ ઞꤌꤙꤣተӄꤣ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] მꤕ꤅рꤌმꤌઞተ ꤍ 𐌼ꤌ𐌻ꤕઞ𑀨ӄ꤀꤇ ꤙꤣꤍ𑀨ӄ꤀꤇? )ተખ ꤍγӄꤌ, ӄꤌӄ  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ተꤐ꤀ꤣ𐌼 ꤎउખӄ꤀𐌼 ꤒγმγ ꤒꤣрӄꤣ ꤍ 𑀋γꤎ ꤍઞꤣ𐌼ꤌተ𑀨 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤍ𐌼ꤕઞꤣ𐌻 ꤙ꤀उγ ꤍ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤕ꤇, ꤒγმተ꤀ ӄꤌઞꤌ𐌻 ઞꤌ ተꤕ𐌻ꤕӄꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤌ൰ꤣ𐌻ꤍꤎ उꤌ 𐌼꤀ꤣ𐌼 𑀋γꤕ𐌼, ꤒγმተ꤀ ꤌꤍ𐌼ꤌተꤣӄ उꤌ 𐌻ꤕӄꤌрꤍተꤐ꤀𐌼? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼꤀꤇ 𑀋γ꤇ ꤐ𐌻ꤕተꤌꤕተ ꤐ р꤀ተ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ,ӄꤌӄ ӄꤌ𐌼ꤕઞ𑀨 ꤐ ꤍተꤕӄ𐌻꤀) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤍӄр꤀𐌼ઞ꤀ ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨, ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀પꤕ𐌼γ ተꤕꤒꤎ 𑀋γꤎрꤎተ ተ꤀𐌻ꤙ꤀꤇?) ተખ ተꤣꤙ꤀ ꤀р꤅ꤣꤣ 𐌻ળꤒꤣω𑀨?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤀ተӄр꤀꤇ ꤍꤐ꤀ળ მγωγ 𐌼꤀ꤕ𐌼γ 𑀋γળ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ γ𐌟ꤕ ઞꤌ ꤍተ꤀𐌻𑀨ӄ꤀ ઞꤕ ꤐખꤐ꤀उꤣω𑀨,પተ꤀ ઞꤌપꤣઞꤌꤕω𑀨 ꤙꤣꤍꤌተ𑀨 ઞꤕ ꤙр꤀ꤐ꤀ӄꤌꤟꤣꤣ, ꤌ 𑀋γ꤇ઞળ,𐌻γપωꤕ ꤙ꤀પꤣተꤌ꤇, ӄꤌӄ ꤎ ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ उꤌ꤅ꤌрꤌꤕω𑀨 ઞꤌ 𐌼꤀ꤕ𐌼 𑀋γળ ꤒγმተ꤀ ઞꤌ ωꤕउ𐌻꤀ઞ꤅ꤕ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] მꤕ꤅рꤌმꤌઞተ ꤍ 𐌼ꤌ𐌻ꤕઞ𑀨ӄ꤀꤇ ꤙꤣꤍ𑀨ӄ꤀꤇? )ተખ ꤍ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ მ꤀ωꤣрꤌӄ ꤍ𐌻ꤣउખꤐꤌ𐌻) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ, ӄꤌӄ ӄꤍળωꤌ ꤍ꤀ꤒપꤌӄ 𑀋γꤎ 𐌼꤀ꤕ꤅꤀ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤀પꤣ પꤕрઞખꤕ,꤀પꤣ 𐌟꤅γપꤣꤕ,ꤐ ተꤐ꤀ꤕ𐌼 рተγ 𑀋γꤣ ꤐ꤀ઞળપꤣꤕ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍγӄꤌ,ꤎ γ𐌟ꤕ उꤌӄꤌተખꤐꤌળꤍ𑀨.ꤍ ተ꤀꤅꤀, ӄꤌӄ ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] પ𐌻ꤕઞ꤀ꤍ꤀ꤍ?) ተꤐ꤀ё ꤀પӄ꤀ ꤅꤀рꤣተ, ተγωꤣ ꤍӄ꤀рꤕꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] γ𐌟ꤕ ӄꤌϕꤕ ꤀ተӄрખ𐌻 ઞꤌ 𑀋γળ,ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤍꤌ𐌼ખ꤇ પꤌꤍተખ꤇ ӄ𐌻ꤣꤕઞተ ))ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀𑀨ꤎ ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ઞꤌ ӄγр꤀рተꤕ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤐપꤕрꤌ 𑀋γꤕ𐌼 ꤍꤙꤌ𐌻ꤣ𐌻 ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ꤐ მγꤒꤌꤎ𑀋,20 ᤋተꤌ𐌟ꤕ꤇ ꤀ተꤕ𐌻ꤎ ꤍ꤅꤀рꤕ𐌻꤀) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ӄ꤀ꤍꤎપꤣω𑀨 ઞꤌ 𐌼꤀ꤕ𐌼 𑀋γળ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤍγӄꤌ ተꤌმ𐌟ꤣӄ ꤕꤒꤌઞખ꤇, ꤒખꤍተрꤕꤕ 𐌼꤀꤇ 𑀋γ꤇ ꤍ𐌻ળઞ꤀꤇ ꤀ꤒӄ𐌻ꤕꤕꤐꤌ꤇) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] მꤕ꤅рꤌმꤌઞተ ꤍ 𐌼ꤌ𐌻ꤕઞ𑀨ӄ꤀꤇ ꤙꤣꤍ𑀨ӄ꤀꤇? )𐌼꤀꤇ 𑀋γ꤇ ꤐꤌ𐌻𑀨ꤍꤣрγꤕተ ꤍ ꤙꤣउმ꤀꤇ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌઞ𑀨ӄꤣ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼꤀꤇ 𑀋γ꤇ ωꤣϕрγꤕተꤍꤎ ꤐ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼꤀꤇ 𑀋γ꤇ ꤙ꤀ӄ꤀ꤎ ઞꤕ მꤌꤕተ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙꤣउმꤌ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ӄꤌተꤎ ӄ𐌻ꤎꤙ 𑀋γꤎ 𐌼꤀ꤕ꤅꤀? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ઞ꤀꤅ꤣ ꤐખተꤣрꤌળ ꤀ꤒ ተꤕꤒꤎ,ተрꤎꤙӄꤌ ꤕꤒꤌઞꤌꤎ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤍઞꤣ𐌼ꤌꤕω𑀨 ӄ꤀𐌼ꤕმꤣꤣ ꤀ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ꤍ 𐌼꤀ꤣ𐌼 𑀋γꤕ𐌼?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼꤀꤇ 𑀋γ꤇ 𑀋꤀𐌻꤀ꤍተꤎӄ рተꤌ ተꤐ꤀ꤕ꤅꤀ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼꤀꤇ 𑀋γ꤇ ઞꤕрꤐꤣрγꤕተ ተꤐ꤀ё ꤀પӄ꤀? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𑀋γꤕ𐌼 ꤍꤐꤕрઞγ𐌻 ӄ𐌻ꤣተ꤀р ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ӄꤌӄ ꤙ꤀𐌻꤀ተꤕઞꤟꤕ ꤐ рꤌउმꤣꤐꤌ𐌻ӄꤕ ꤣ ꤙ꤀𐌻꤀𐌟ꤣ𐌻 ꤐ ӄꤌꤒꤣઞӄγ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤐ ꤀પӄ꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ઞꤌω꤀𐌻 उꤌꤒр꤀ωꤕઞખꤕ ꤙр꤀მγӄꤟꤣꤣ ꤌρρ꤈ꤕ ꤣ ꤙ꤀ተ꤀𐌼 ꤙр꤀მꤌ𐌻 ꤣ𑀋 उꤌ ꤌӄꤟꤣꤣ ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ઞꤌ ӄ𐌻ꤣተ꤀рꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 рꤣꤍ꤀ꤐꤌ𐌻 ꤙꤕઞተꤌ꤅рꤌ𐌼𐌼γ ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ઞꤌ ꤀પӄꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ӄ𐌻γꤒӄꤣ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 ӄꤌተꤌ [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ 𑀋γꤕ𐌼 ꤙꤣउმꤌӄ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ꤐӄрγપꤣꤐꤌ𐌻 ꤐ ꤍተꤕઞγ,ӄꤌӄ ꤒ꤀𐌻ተ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ተખ ꤍγӄꤌ ӄ𐌻ꤕ൰𑀨 ꤕꤒꤌઞખ꤇,उꤌ𐌻ꤕउ ꤙ꤀მ 𐌼꤀ળ उꤌ𐌻γꤙγ,𐌼 ꤙꤣተꤌꤕω𑀨ꤍꤎ ꤙ꤀მउꤌ𐌻γꤙઞખ𐌼 ተꤐ꤀р꤀꤅꤀𐌼) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] γપꤕઞખꤕ ꤐખმꤐꤣઞγ𐌻ꤣ ተꤕ꤀рꤣળ,પተ꤀ ꤐꤍꤕ ӄተ꤀ ꤙખተꤌꤕተꤍꤎ ተр꤀𐌻𐌻ꤣተ𑀨 𐌼ꤕઞꤎ ꤙ꤀მꤍ꤀उઞꤌተꤕ𐌻𑀨ઞ꤀ ꤍ꤀ꤍγተ 𑀋γꤣ ))) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ 𐌼꤀ꤎ ꤒрꤌተꤐꤌ ꤣ꤅рꤌ𐌻ꤌ ꤐ ϕγተꤒ꤀𐌻 ઞꤌ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ?) 𐌼ખ ꤍተ꤀𐌻𑀨ӄ꤀ ꤅꤀𐌻꤀ꤐ उꤌꤒꤣ𐌻ꤣ ꤐ ꤕё ꤐрꤌተꤌ,પተ꤀ γ ઞꤌꤍ ꤎ꤇ꤟꤌ ꤀ꤙγ𑀋𐌻ꤣ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ꤍꤕ꤇પꤌꤍ ተꤐ꤀꤇ ꤕꤒ𐌻ꤕተ ꤣउ𐌼ꤌ𐌟γ ꤅ꤌꤐઞ꤀𐌼,ꤍӄꤌ𐌟γ, પተ꤀ ተખ ꤌउꤣꤌተ, ꤣ ꤀ተꤙрꤌꤐ𐌻ળ ꤐ ӄꤣተꤌ꤇) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] рꤕꤒꤎተ,ꤙ꤀ω𐌻ꤣተꤕ ઞꤌ ꤒꤌ𐌻𐌻?) ꤎ ተꤌ𐌼 𐌼ꤌተ𑀨 𐌼꤀ꤕ꤅꤀ ꤙр꤀ተꤣꤐઞꤣӄꤌ ꤐપꤕрꤌ ꤕꤒꤌ𐌻 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ꤙꤕрმꤕ𐌻 ተꤕꤒꤕ ઞꤌ γ𑀋꤀,ꤍγӄꤌ ተખ ꤅𐌻γ𑀋ꤌꤎ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤀მꤣઞ рꤌउ ꤎ ꤙрꤣωꤕ𐌻 ӄ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ӄꤕ ꤍγӄꤌ,ꤣ ꤍተрꤕ𐌻ꤎ𐌻 ꤙ꤀ ઞꤕ꤇ ꤍ 𑀋γꤎ,ӄꤌӄ ꤍ ተꤌઞӄꤌ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤒ𐌻ꤎ પ꤀ ӄꤌрખተ꤀?) ꤎ ተꤎ 𑀋γꤕ𐌼 ꤍ𐌼ꤌꤍተꤕрળ,ઞꤌ𐌻꤀𐌟γ ꤒ꤀𐌼ꤒꤎ൰ꤣ𑀋 ꤙγӄꤌઞ꤀ꤐ,ꤣ ꤐउ꤀рꤐγ ઞꤌ𑀋γ꤇ )))) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ተꤐ꤀ળ ӄꤌрმꤣ꤀꤅рꤌ𐌼𐌼γ ꤣउγપꤣ𐌻 𑀋γꤕ𐌼,પተ꤀ꤒ ꤒꤣተ𑀨 ꤙ꤀ ተꤐ꤀ꤕ𐌼γ ꤒ꤀𐌻𑀨ઞ꤀𐌼γ ꤍꤕрმꤟγ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ પ꤀ ꤍγӄꤌ,ꤍ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ მꤕ𐌼꤀ઞꤌ ꤍꤐ꤀ꤕ꤇ ꤅γꤒખ ꤣउ꤅꤀ઞꤎተ𑀨 ꤍ꤀ꤒрꤌ𐌻ꤍꤎ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ተꤕꤒꤎ ൰ꤌ 𑀋γꤕ𐌼 ꤐ მઞ꤀ 𐌼꤀рꤎ ꤍӄꤣઞγ,ӄꤌӄ ꤒꤌ𐌻𐌻ꤌꤍተ ꤍ ӄ꤀р꤀ꤒ𐌻ꤎ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ൰ꤌ,ꤎ ꤐꤕმ𑀨 ꤍγӄꤌ ꤕ൰ё ઞꤕ рꤌउ꤀꤅рꤕ𐌻ꤍꤎ,γγγ𑀋,ӄꤌӄ ꤙ꤀ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤍꤕ꤅꤀მઞꤎ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌼ખ ꤍ р꤀𐌼ӄ꤀꤇ ઞꤌ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ 𑀋γꤎ𐌼ꤣ ӄ꤀ꤍተꤕр рꤌउ꤀𐌟꤅𐌻ꤣ,પተ꤀ꤒ ઞꤌ ꤕё ꤙγꤍተખઞઞ꤀꤇ ꤙꤣउმꤕ ꤍ꤀꤅рꤕተꤍꤎ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, ꤎ ꤙꤣωγ ꤙ꤀ ꤙꤎተ𑀨 ꤍ𐌻꤀ꤐ, ꤣ ꤙр꤀ꤍተ꤀ उꤌꤙꤣઞખꤐꤌળ ተꤐ꤀ળ 𐌼ꤌተ𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤕꤒꤌωꤣ𑀋 𐌼ꤌ𐌼 ӄ꤀𐌼γઞꤣꤍተખ પተ꤀ 𐌻ꤣ ꤕꤒγተ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤙꤣउმꤌӄ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ꤣउꤒꤣрꤌ𐌻 𐌼꤀꤇ 𑀋γ꤇ 𐌼ꤕр꤀𐌼 ꤕё ꤅γꤒખ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ꤍꤣმꤎ ꤕꤌ उ꤀ઞꤕ ꤙ꤀ꤙꤣꤐꤌꤎ પꤣϕꤣр ꤕꤒꤌ𐌻 ተꤐ꤀ળ 𐌼ꤌተ𑀨?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤍγӄꤌ ӄγωꤌꤕω𑀨 ꤍꤣმꤎ ઞꤌ 𐌼꤀ꤕ𐌼 𑀋γꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ꤍγӄꤌ ꤍꤙ꤀ꤍ꤀ꤒꤕઞ ꤕꤒꤌተ𑀨 ተꤐ꤀ળ 𐌼ꤌተ𑀨 𐌼ꤣઞꤣ𐌼γ𐌼 10 પꤌꤍ꤀ꤐ? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ 𑀋꤀𐌟γ ꤙ꤀ 𐌻γપγ ꤕꤒꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕተꤕ,પተ꤀ ꤎ ꤐꤌꤍ ꤍ 𑀋γꤎ ӄ꤀р𐌼ꤣተ𑀨 ꤒγმγ, ꤍ꤀ꤒꤌӄꤣ ꤕꤒꤌઞખꤕ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ઞꤕተ,ઞγ 𐌼ઞꤕ પ꤀,ꤐउꤎተ𑀨 𑀋γ꤇ ꤐ рγӄγ,ꤣ ꤒꤣተ𑀨 ꤐꤌ𐌼 ꤙ꤀ ꤅γꤒꤌ𐌼? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤐખ ꤙ꤀ઞꤣ𐌼ꤌꤕተꤕ,પተ꤀ ꤎ ꤐꤌ𐌼 ꤍγӄꤌ ꤙ꤀მ ઞ꤀ꤍ ꤙꤕр𐌟γ,მꤐꤌ પγ𑀋ꤌઞꤌ ꤒ𐌻ꤎმ𑀨 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤐꤌꤍ მꤐγ𑀋 ω𐌻ળ𑀋 ઞꤌ 𐌼꤀꤇ 𑀋γ꤇ рꤌउმꤕ𐌻ꤣተ𑀨? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ꤐ ӄꤌተ꤀𐌻ꤣપꤕꤍӄ꤀꤇ ꤟꤕрӄꤐꤣ ꤍ ተрꤕ𐌼ꤎ ꤙ꤀ꤙꤌ𐌼ꤣ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤕꤒꤌ𐌻) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ 𑀋γꤕ𐌼 ተꤕꤒꤕ ꤍӄꤌ𐌟γ " ꤌрꤣꤐγꤌр, 𑀋γ꤇𐌻꤀ " [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤐ꤀ꤍꤙꤣተખꤐꤌ𐌻 𑀋γꤕ𐌼? ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ꤒ𐌻ꤎმ𑀨 ተꤐ꤀ꤣ ઞ꤀꤅ꤣ 𑀋γꤕ𐌼 ꤀ተрꤕ𐌟γ,ꤒγმተ꤀ ꤍꤌꤒउꤣр꤀ ઞꤌ𑀋γ꤇) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ 𐌟ꤕ ꤍγӄꤌ ꤒγმγ ӄꤌӄ ꤐ 𐌻ꤕꤍγ ꤕꤒꤌተ𑀨 ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤙ꤀მ ꤙꤕઞ𑀨ӄ꤀𐌼) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ рꤌმꤣγꤍ ꤙ꤀рꤌ𐌟ꤕઞꤣꤎ ꤅γꤒખ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ 𐌼꤀ꤣ𐌼 𑀋γꤕ𐌼 рꤌꤐꤕઞ 1000 ӄ𐌼) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤐખꤕꤒꤌ𐌻 𐌼ꤌተ𑀨 ꤙ꤀𐌻꤀ꤐꤣઞખ ተр꤀𐌻𐌻ꤣઞ꤅ꤌ,ꤌ ተꤐ꤀ળ ꤙ꤀მꤌꤐઞ꤀ ꤐખꤕꤒγ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ 𐌟ꤣꤐγ उꤌ ꤍપꤕተ ꤙꤣउმꤌӄꤌ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ?) ꤎ ꤕё ꤍγተꤕઞꤕр) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ उઞꤌ𐌻,પተ꤀ ꤎ ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ઞꤌ ꤍӄ꤀р꤀ꤍተꤣ 150 ӄ𐌼 ꤐ પꤌꤍ?) 𐌼꤀ꤣ ꤎ꤇ꤟꤌ ꤙ꤀ 7 рꤌउ ꤐ ꤍꤕӄγઞმγ ꤍተખӄꤌ𐌻ꤣꤍ𑀨 ꤍ ꤕё ꤒꤌрმળр꤀𐌼) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ઞꤌ उꤌꤙрꤌꤐӄꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ꤍꤕ꤇પꤌꤍ 𑀋γꤕ𐌼 ꤣꤍꤙꤕꤙꤕ𐌻ળ પꤕрꤕꤙ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ӄꤣ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ꤙ꤀მꤌр꤀𐌟ઞꤣӄ ꤙрꤣ𐌻꤀𐌟γ ӄ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ,પተ꤀ꤒ ꤙ꤀ꤍ𐌻ꤕ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ઞꤕ ተꤕӄ𐌻ꤌ ӄр꤀ꤐ𑀨 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] მઞ꤀ ተખ ꤍγӄꤌ ӄꤌрખተઞ꤀ꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ 𑀋γꤕ𐌼 ተꤐ꤀ё ꤕꤒꤌ𐌻꤀ ꤣउрꤣꤍγળ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ൰ꤌ 𑀋γꤕ𐌼 ꤍઞꤕꤍγ ӄрખωγ ꤍ მ꤀𐌼ꤌ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤐӄγрꤍꤕ પꤕ꤇ 𑀋γ꤇ ꤀ꤍꤌმꤣ𐌻?) ꤍꤌმઞꤣӄ ተખ ꤍγӄꤌ ꤒꤕउ ꤅꤀𐌻꤀ꤐખ, ꤎ ተꤕꤒꤎ 𐌟ꤕ 𑀋γꤕ𐌼 γꤒ𑀨ળ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤌ ઞγ ꤍળმꤌ ꤣმꤣ ꤣ𐌻ꤣ 𐌼ઞꤕ ꤙрꤣმꤕተꤍꤎ ꤐ ꤙꤣउმγ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤕ, ӄγმꤌ ተખ ꤍꤙрꤎተꤌ𐌻ꤍꤎ 𑀋γ꤇ उꤌꤙꤣ𑀋ꤣꤐꤌተ𑀨 ꤣ 𐌻꤀ꤐꤣተ𑀨 ተꤕꤒꤎ ӄꤌӄ рખꤒγ ઞꤌ γმ꤀પӄγ)) ωӄꤌተγ𐌻ӄꤌ ꤒ𐌻ꤎተ𑀨 ተખ ꤕꤒꤌઞꤌꤎ)) ꤎ 𐌟ꤕ ꤒ𐌻ꤎተ𑀨 р꤀ተꤌઞ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ꤍӄрγપγ ꤣ ꤒγმγ ꤣउ ઞꤕ꤅꤀ ꤍ꤀ꤍꤣꤍӄꤣ მꤕ𐌻ꤌተ𑀨)) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] γ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤕ ઞꤌ 𐌟꤀ꤙꤕ ተꤌӄꤌꤎ उმ꤀р꤀ꤐꤌꤎ ꤙ꤀𐌼ꤣმ꤀рꤣઞꤌ ꤕꤒꤌተ𑀨 ӄрꤌꤍઞꤌꤎ ꤕ൰ꤕ მ꤀ ꤙꤣउმખ)) ꤎ 𐌟ꤕ ꤒ𐌻ꤎተ𑀨 𑀋γꤕ𐌼 ꤕꤕ ꤍઞꤕꤍγ ꤣ ꤍ꤀მꤕр𐌟ꤣ𐌼꤀ꤕ ተꤕꤒꤕ ઞꤌ ꤕꤒ𐌻ꤕተ ꤐખꤒрખउઞꤣተ))) ꤍӄꤣઞ𑀋ꤕმ ተખ ꤕꤒꤌઞખ꤇)) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍ𐌻ખω?) ꤅꤀ꤐઞ꤀ꤙꤌმꤣ൰ꤕ ꤕꤒꤌઞ꤀ꤕ?) 𐌼ઞꤕ ተꤐ꤀꤇ ꤀પӄꤕꤍተꤌઞ рꤌउрખꤐꤌተ𑀨 𐌻ꤕ꤅પꤕ પꤕተ ઞꤕ ꤙ꤀ઞꤎ𐌻 ઞꤣ𑀋γꤎ ꤎ 𐌟ꤕ ꤒ𐌻ꤎተ𑀨 ተꤕꤒꤎ ઞꤌ ꤍꤐ꤀꤇ 𑀋γ꤇ ઞꤌተꤎ꤅ꤣꤐꤌળ ꤙрꤎ𐌼꤀ ӄꤌӄ ઞ꤀ꤍӄꤣ ઞꤌ ꤍተ꤀ꤙખ ꤕꤒꤌተ𑀨 [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተрꤌ𑀋ተખઞꤒખ𑀋 ꤕꤒꤌઞખ꤇ ተખ ꤅მꤕ ተꤌ𐌼 ꤒ𐌻ꤎተ𑀨 ꤙрꤎપꤕω𑀨ꤍꤎ?) 𐌼ઞꤕ ተꤕꤒꤎ ꤙ꤀ ተꤕ𐌼ઞખ𐌼 ꤙꤕрꤕγ𐌻ӄꤌ𐌼 მ𐌻ꤎ ꤀ተꤍ꤀ꤍꤌ 𑀋γꤎ ꤣꤍӄꤌተ𑀨 ઞꤌმ꤀ ꤣ𐌻ꤣ પተ꤀?)) ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ተꤌӄ𐌟ꤕ ꤐખꤕꤒꤌ𐌻 ተꤕ𐌼ઞ꤀𐌼 ꤙꤕрꤕγ𐌻ӄꤕ ઞ꤀ ተꤌ𐌼 ӄꤌ𐌼ꤕрખ ꤍተ꤀ꤎ𐌻ꤣ ꤣ 𐌼ઞꤕ ઞꤌ 𑀋γ꤇ ꤙрꤕ𐌻ꤕꤙꤣ𐌻ꤣ ωተрꤌϕ )) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ተખ ተγꤙ꤀ ꤙꤌપӄꤌ ꤍꤣ꤅ꤌрꤕተ) ተખ ꤍ꤀ꤍꤕω𑀨 ઞꤣӄꤌӄ)) ꤌ ꤐ꤀ተ ተꤐ꤀ꤎ 𐌼ꤌ𐌼ꤌωꤌ ꤍ꤀ꤐꤍꤕ𐌼 მрγ꤅꤀ꤕ მꤕ𐌻꤀ ꤒ𐌻ꤎተ𑀨) ઞ꤀ ꤒꤕმꤌ ꤐ ተ꤀𐌼 પተ꤀ ꤀ઞꤌ ꤍꤐꤣઞ𑀨ꤎ ꤣ ꤀ઞꤌ ӄ꤀꤅მꤌ ꤍ꤀ꤍꤕተ 𑀋рળӄꤌꤕተ ꤌ ꤐ꤀ተ ተꤐ꤀꤇ ꤙꤌꤙꤌωꤌ ꤅꤀рꤣ𐌻𐌻ꤌ ꤒ𐌻ꤎተ𑀨 ꤕꤒꤌઞꤌꤎ ꤐ꤀꤀ꤒ൰ꤕ)) ꤀ઞꤣ ተꤕꤒꤎ ꤍმꤕ𐌻ꤌ𐌻ꤣ ઞꤕ પꤕрꤕउ ꤙ꤀𐌻꤀ꤐખꤕ ꤀р꤅ꤌઞખ , ꤌ ተꤐ꤀ ꤙꤌꤙꤌωꤌ उꤌ𐌻ꤕउ ꤒ꤀ωӄ꤀꤇ ꤐ ꤙꤣउმγ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ꤣ ꤙ𐌻ળઞγ𐌻 ተγმꤌ)) ꤍ𐌻ꤣउꤕઞ𑀨 ተખ ꤍγӄꤌ ꤕꤒꤌઞખ꤇ [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤒγმγ рꤌꤍӄрγપꤣꤐꤌተ𑀨 ꤙꤣउმꤌӄ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ꤣ ꤙрꤣꤐꤎ𐌟γ ӄ ઞꤕ𐌼γ ꤕꤕ р꤀ተꤌઞ. ꤀ઞ 𐌟ꤕ ꤍγӄꤌ ӄꤌӄ 𐌻꤀ꤙ꤀ꤍተꤣ ꤒγმꤕተ ӄрγተꤣተ𑀨ꤍꤎ ꤐꤕрተ꤀𐌻ꤕተꤌ ꤣ ꤙ꤀მઞꤣ𐌼ꤌተ𑀨 ꤕꤕ ꤙꤣउმꤌӄ ꤐꤐꤕр𑀋 ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨?) 𐌼ꤣ𐌻𐌻ꤣꤌрმꤕр ተખ ꤌઞꤌ𐌻𑀨ઞખ꤇ ꤍꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ 𐌟ꤕ ꤒ𐌻ꤎተ𑀨 ઞꤌ ተꤐ꤀ꤣ 𑀋꤀𑀋𐌻ꤎꤟӄꤣꤕ 𐌻ꤌꤙተꤣ ꤙрꤣӄ𐌻ꤕળ ꤍꤐ꤀꤇ ꤍꤙꤕр𐌼ꤌӄ, ꤌ ተખ ꤒγმꤕω𑀨 მγ𐌼ꤌተ𑀨 , પተ꤀ ᤋተ꤀ ꤍγꤙꤕр ӄ𐌻ꤕ꤇)) ꤎ ꤕ꤅꤀ ꤐખꤍӄрꤕꤒ ꤣउ ꤙꤣउმꤌӄꤌ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ӄ꤀꤅მꤌ ꤀ઞ ꤙрꤣ𐌻ꤣꤙ ӄ ꤕꤕ ꤙꤣउმꤕ 3 ꤅꤀მꤌ ઞꤌउꤌმ ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 ꤒ𐌻ꤎተ𑀨?)) ተрγꤒ꤀પꤣꤍተ ተખ ꤕꤒꤌઞખ꤇ [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ᤋተ꤀꤅꤀ ઞꤕ उઞꤌળ ꤐꤕმ𑀨 ઞꤕ ꤐꤣმꤕ𐌻 ተꤕꤒꤎ, ꤌ ꤕꤍ𐌻ꤣꤒખ γꤐꤣმꤕ𐌻, ተ꤀ ተрꤌ𑀋ઞγ𐌻 ꤒખ ተꤕꤒꤎ ꤐ꤀ ꤐꤍꤕ ꤙꤣ𑀋ꤌተꤕ𐌻𑀨ઞખꤕ ꤣ მખ𑀋ꤌተꤕ𐌻𑀨ઞખꤕ, ꤐ꤀ ꤐꤍꤕ ꤍγ൰ꤕꤍተꤐγળ൰ꤣꤕ ꤣ ઞꤕ ꤍγ൰ꤕꤍተꤐγળ൰ꤣꤕ, ꤌ ተꤕ પተ꤀ ઞꤕ ꤍγ൰ꤕꤍተꤐγળተ ꤙрꤣმγ𐌼ꤌ𐌻 ꤒખ, ꤣ ꤙ꤀ꤐꤕр𑀨 𐌼ઞꤕ ꤅ઞꤣმꤌ उꤌተрꤌ𑀋ꤌઞઞ꤀-γр꤀მ𐌻ꤣꤐꤌꤎ ተꤕꤒꤕ ꤒખ ᤋተ꤀ ꤙ꤀ઞрꤌꤐꤣ𐌻꤀ꤍ𑀨  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] γ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ખ ઞγ ꤙр꤀ꤍተ꤀ ꤙꤣउმꤕꤟ ӄꤌӄꤌꤎ ꤒ꤀𐌻𑀨ωꤌꤎ ꤙꤣउმꤌ, ꤎ ተγმꤌ ꤙ꤀𐌻ઞ꤀ꤍተ𑀨ળ ꤐ𑀋꤀მꤣ𐌻. ᤋተ꤀ ꤙꤣउმꤕꤟ, ꤎ ӄꤌрપ ꤐ꤀उ𐌻ꤕ ꤕꤕ ꤙꤣउმખ ӄ꤀ꤐрꤣӄ ꤙ꤀𐌻꤀𐌟ꤣ𐌻, પተ꤀ꤒ ઞ꤀꤅ꤣ ꤐખተꤣрꤌተ𑀨 ꤒ𐌻ꤎተ𑀨  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ꤕꤒꤌઞꤕꤟ, მрꤌӄ꤀ઞ ተрꤎꤙ꤀પઞખ꤇, 𐌻꤀𑀋꤀მр꤀𐌼 ꤅ꤌ𐌻ꤣ𐌼ખ꤇, γёꤒ꤀ӄ ꤙꤣउმ𐌻ꤎꤐખ꤇, ӄ꤀ઞપꤣઞꤌ ꤕꤒꤌઞꤌꤎ, γёꤒꤣ൰ꤕ 𐌻ꤕꤍઞ꤀ꤕ. ꤀ተꤍ꤀ꤍꤣ ઞꤕ ઞꤌ꤅ꤣꤒꤌꤎꤍ𑀨 ꤣ ꤙ꤀მ𐌼ખተ𑀨ꤍꤎ ઞꤕ उꤌꤒγმ𑀨. ઞꤕ ꤒउმꤣ ӄꤌꤙγꤍተꤣઞ, ꤐખꤕꤒꤕ𐌼 ꤀ተꤙγꤍተꤣ𐌼.  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤕꤒꤌ𐌻 ӄ꤀꤅მꤌ ተખ ꤍ꤀ꤍꤌ𐌻 𐌼ઞꤕ 𑀋γ꤇ ઞꤌ 10 ᤋተꤌ𐌟ꤕ - ꤌ ꤙ꤀ተ꤀𐌼 ꤎ ተꤐ꤀ળ ꤒꤌꤒγωӄγ ꤕꤒꤌ𐌻 ઞꤌ ?? -ꤙ꤀ተ꤀𐌻ӄꤕ  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀उ꤀ꤐꤣ ꤍꤐ꤀ળ ተꤎઞ꤀પӄγ ꤎ 𑀋꤀પγ ꤕ꤇ 𐌻ꤣપઞ꤀ ꤍӄꤌउꤌተ𑀨 ꤍꤙꤌꤍꤣꤒ꤀ उꤌ ꤐપꤕрꤌωઞꤣ꤇ ꤙрꤕӄрꤌꤍઞખ꤇ ꤀ተꤍ꤀ꤍ  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] მ꤀પӄꤌ ᤋ𐌻ꤣተઞ꤀꤇ ω𐌻ળ𑀋ꤣ ꤣ ꤀ተꤟꤌ ꤒ꤀𐌼𐌟ꤌ?___)))) ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ 𐌼ꤌ𐌼ӄγ ተꤐ꤀ળ ꤕꤒγተ γ ተꤎ ꤐ ӄ꤀𐌼ઞꤌተꤕ ӄ꤀꤅მꤌ ተખ ꤍꤙꤣω𑀨 ተꤕ ꤕё ઞꤕ 𐌟ꤌ𐌻ӄ꤀?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤕꤒꤌ𐌻 ተꤐ꤀ળ 𐌼ꤌ𐌼ꤌωӄγ ઞꤌ ꤍተ꤀𐌻ꤕ ꤣ ઞꤌ ꤙ꤀მ꤀ӄ꤀ઞઞꤣӄꤕ)) ꤌ ઞγ ઞꤕꤍꤣ ꤐꤕрꤕꤐӄγ ꤣ ꤀꤅ઞተγωꤣተꤕ𐌻𑀨:उꤌ𐌻ꤕउꤣω𑀨 ꤙ꤀ተγωꤣω𑀨 ꤕ꤇ ꤙꤣउმγ ꤌ ꤙ꤀ተ꤀𐌼 ꤎ ꤀ተმꤌ𐌼 ꤐꤌꤍ ઞꤌ рꤌꤍተꤕрउꤌઞꤣꤕ ઞꤕ꤅рꤌ𐌼  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍγӄꤌ ꤎ ተꤕꤒꤎ ꤙ꤀ꤍ꤀მꤣ𐌻ꤌ ꤐપꤕрꤌ ઞꤌ ꤙꤌꤙӄꤕઞ 𑀋γ꤇ ꤣ ተખ ꤙрખ꤅ꤌ𐌻 ઞꤌ ઞё𐌼 ӄꤌӄ ӄ꤀उё𐌻 ꤍ ꤙꤣउმખ 𐌼ꤌ𐌼ꤌωꤣ ꤍꤐ꤀ꤕ꤇ ӄγрꤣઞꤌ꤇))  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤍγӄꤌ ꤐ ꤍꤕꤒꤎ ꤙ꤀ꤐꤕрꤣ𐌻??? ꤒγმꤕω𑀨 ꤀ተӄрખꤐꤌተ𑀨 р꤀ተ ઞꤌ γр꤀ꤐઞꤣ 𐌼꤀ꤕ꤇ ωꤣрꤣઞӄꤣ  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍ꤀ꤍγઞ꤀ӄ_)𐌼꤀꤇ 𐌻ꤣપઞખ꤇_)?ꤎ ተꤐ꤀꤇ р꤀ተ ꤕꤒꤌ𐌻_)?ꤙꤕрꤕω𐌻ꤕω𑀨 𐌼꤀ꤣ ꤍ𐌼ꤍ ተખ ꤒγმꤕω𑀨 ꤙрꤣउઞꤌઞ 𐌼꤀ꤣ ϕꤌઞꤌተ꤀𐌼_)?ꤎ ꤐተ꤀ળ 𐌼ꤌተ𑀨 ꤕꤒꤌ𐌻 ઞꤌ рꤌꤍӄ𐌻꤀მγωӄꤕ_)?ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤐተ꤀꤇ р꤀ተ ꤕꤒꤌ𐌻 ઞꤌ ꤐꤕрωꤣઞꤕ ӄ𐌻ꤣተр꤀ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤕ?)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ उઞꤌꤕω𑀨 પተ꤀ ꤎ ተ꤀ተ ꤍꤌ𐌼ખ꤇ ꤙꤌрꤕઞꤕӄ,પ𐌻ꤕઞ ӄ꤀ተ꤀р꤀꤅꤀ ꤍγ𐌟მꤕઞ꤀ ꤒખ𐌻꤀ ተꤕꤒꤕ ꤐउꤎተ𑀨 ꤐ р꤀ተ?) ઞγ ተꤌӄ ተꤕꤙꤕр𑀨 उઞꤌ꤇)) ተખ ઞꤕ 𐌟ꤕрተꤐꤌ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ,ተખ ꤕ꤅꤀ рꤌꤒખઞꤎ) ተꤌӄ рꤌꤍꤙ꤀рꤎმꤣ𐌻ꤌꤍ𑀨 ꤍγმ𑀨ꤒꤌ)))  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤇ꤌ ተꤕ ꤒγმꤕр ꤍმꤕ𐌻ꤌળ))) ꤍ ꤐ꤀𐌻꤀ꤍӄ꤀𐌼 ꤙꤣउმખ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ પγ ꤀𐌻γ𑀋 ꤕꤒꤌઞખ꤇)) ꤎ ꤙрꤎ𐌼 ӄꤌӄ ꤣउ 𐌼γ𐌻𑀨ተꤣӄꤌ ӄꤌр𐌻ꤍ꤀ઞ, ꤙрꤣ𐌻ꤕተꤌળ ઞꤕ उꤌ ꤐꤌрꤕઞ𑀨ꤕ𐌼, ꤌ उꤌ ꤕꤒ𐌻ળ ꤍ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤕ꤇))  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ё उꤌઞꤎተꤣꤕ ꤙ꤀ ꤐꤕપꤕрꤌ𐌼 ᤋተ꤀ ꤙ꤀მꤒꤌმрꤣꤐꤌઞꤣꤕ 𐌼꤀ꤕ꤅꤀ પ𐌻ꤕઞꤌ  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ӄ꤀ઞપꤣ𐌻 ꤐ рખ𐌻꤀ ተꤐ꤀ꤕ꤇ γꤒ꤀꤅꤀꤇ 𐌼ꤌተꤕрꤣ , ተꤌӄ ꤐ꤀ተ ꤀ઞꤌ ઞꤕ ꤐખმꤕр𐌟ꤌ𐌻ꤌ 𐌼꤀ꤕ꤇ ꤍተрγꤣ ꤣ ꤐખꤙꤌ𐌻ꤌ ꤣउ ꤀ӄઞꤌ ꤍꤐ꤀ꤣ𐌼 рተ꤀𐌼 ઞꤌ 𐌼꤀꤇ 𑀋γ꤇) ተꤌӄ ꤐ꤀ተ ꤙ꤀ተ꤀𐌼 ꤎ ꤙ꤀ωꤕ𐌻 ꤣ γꤐꤣმꤕ𐌻 ꤕꤒꤌઞ꤀꤅꤀ ꤙꤣმꤌрꤌꤍꤌ ተꤐ꤀ꤕ꤅꤀ ꤙꤌꤙӄγ  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤕꤒꤌઞખ꤇ рખꤟꤌр𑀨 ꤍ ꤙꤣउმꤌӄ꤀𐌼 ꤍꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ӄꤌӄ ꤍ ൰ꤣተ꤀𐌼 ઞꤌ ꤙ𐌻ꤕપꤕ ꤀ተ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ?) ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 , ተ꤀ પተ꤀ ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤕꤒꤌ𐌻 ઞꤌ ӄрખωꤕ მ꤀𐌼ꤌ ꤣ ተрꤌઞꤍ𐌻ꤣр꤀ꤐꤌ𐌻 ᤋተ꤀ ꤐ ꤙрꤎ𐌼꤀꤇ ᤋϕꤣр  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤕꤒꤌઞખ꤇ рખꤟꤌр𑀨 ꤍ ꤙꤣउმꤌӄ꤀𐌼 ꤍꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ӄꤌӄ ꤍ ൰ꤣተ꤀𐌼 ઞꤌ ꤙ𐌻ꤕપꤕ ꤀ተ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ?)ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 , ተ꤀ પተ꤀ ተખ ꤙ꤀𐌼ꤕપꤕઞ 𐌼꤀ꤣ𐌼 𑀋γё𐌼 ?  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤕꤒꤌઞખ꤇ рખꤟꤌр𑀨 ꤍ ꤙꤣउმꤌӄ꤀𐌼 ꤍꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ӄꤌӄ ꤍ ൰ꤣተ꤀𐌼 ઞꤌ ꤙ𐌻ꤕપꤕ ꤀ተ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ?) ተખ ꤙ꤀𐌼ઞꤕω𑀨 ӄꤌӄ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤙꤣउმꤌઞγ𐌻ꤌꤍ𑀨 ઞꤌ ተꤕꤒꤎ ꤍ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ?  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤕꤒꤌઞખ꤇ рખꤟꤌр𑀨 ꤍ ꤙꤣउმꤌӄ꤀𐌼 ꤍꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ӄꤌӄ ꤍ ൰ꤣተ꤀𐌼 ઞꤌ ꤙ𐌻ꤕપꤕ ꤀ተ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ?) ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 , ተ꤀ પተ꤀ ꤎ ꤌꤐተ꤀𐌼ꤌተ꤀𐌼 ꤕꤒγ ተꤐ꤀꤇ р꤀ተ , ተꤐ꤀ꤎ ꤕꤍተꤕꤍተꤐꤕઞઞꤌꤎ उꤌ൰ꤣተꤌ ᤋተ꤀ γӄрખꤐꤌተ𑀨ꤍꤎ ꤙꤣउმꤌӄ꤀𐌼 ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ)?  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ꤍꤕ꤇પꤌꤍ ተꤐ꤀ꤕ ꤕꤒꤌ𐌻꤀ ꤍઞ꤀ꤍꤣተ𑀨 ꤒγმγ ӄꤌӄ ꤙ꤀ઞꤌрꤌ𐌼γ ꤕꤒꤌઞγળ)მꤌꤐꤌ꤇ 𐌼ઞӄ ꤙꤣωꤣ ꤍγપꤕӄ ꤕꤒꤌઞખ꤇)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤕꤒꤌઞખ꤇ рખꤟꤌр𑀨 ꤍ ꤙꤣउმꤌӄ꤀𐌼 ꤍꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ӄꤌӄ ꤍ ൰ꤣተ꤀𐌼 ઞꤌ ꤙ𐌻ꤕપꤕ ꤀ተ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ?) ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 , ተ꤀ પተ꤀ ተખ ꤕꤒꤌ𐌻 ꤍꤐ꤀ળ 𐌼ꤌተ𑀨 , ꤒꤌꤒγωӄγ , ꤙр꤀ꤒꤌꤒγωӄγ 𐌼꤀ꤣ𐌼 𑀋γё𐌼 ꤣ γმꤣꤐ𐌻ꤎ𐌻ꤍꤎ ᤋተ꤀𐌼γ ઞꤕ ꤣ꤅ઞ꤀р𑀨 𐌼꤀꤇ 𑀋γ꤇ પ𐌻ꤕઞ꤀ꤍ꤀ꤍ ))  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤕꤒꤌઞખ꤇ рખꤟꤌр𑀨 ꤍ ꤙꤣउმꤌӄ꤀𐌼 ꤍꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ӄꤌӄ ꤍ ൰ꤣተ꤀𐌼 ઞꤌ ꤙ𐌻ꤕપꤕ ꤀ተ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ?) ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 , ተ꤀ પተ꤀ ꤎ ꤕꤒꤌ𐌻 ተꤐ꤀꤇ р꤀ተ ꤍγተӄꤌ𐌼ꤣ , ꤌ ꤙ꤀ተ꤀𐌼 ઞꤕ ꤍ𐌼꤀꤅ γმꤕр𐌟ꤌተ𑀨ꤍꤎ ꤣ ӄ꤀ઞપꤣ𐌻 ተꤕꤒꤕ ꤐ ઞ꤀उმрꤣ , ꤣꤒ꤀ ተખ р꤀ተ ઞꤕ ꤀ተӄрખꤐꤌ𐌻  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ 𐌟ꤕ ተꤐ꤀ળ 𐌼ꤌ𐌼ӄγ ൰ꤌꤍ 𑀋γꤕ𐌼 ꤒγმγ ተ꤀ꤙተꤌተ𑀨 ꤙ꤀მ ꤙꤌ𐌻𑀨𐌼꤀꤇ ઞꤕγ𐌟ꤕ𐌻ꤣ ተખ ઞꤕ ꤙ꤀ઞꤎ𐌻 ωӄ꤀𐌻꤀ꤕꤒ ꤕꤒꤌઞખ꤇ પተ꤀ ተખ ተγꤙ꤀ ꤙ꤀მ𐌼ꤌꤍተꤕр𑀨ꤕ ꤕꤒꤌઞ꤀ꤕ))  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] પꤕрꤕउ ተꤕрઞꤣꤣ ӄ उꤐꤕმउმꤌ𐌼 – ተꤌӄ მ꤀ꤒꤣꤐꤌળተꤍꤎ ꤟꤕ𐌻ꤣ ઞ꤀р𐌼ꤌ𐌻𑀨ઞખꤕ 𐌻ળმꤣ ઞ꤀ ઞꤕ ተખ) ተꤐ꤀꤇ ꤍ𐌻꤀꤅ꤌઞ – ꤍ꤀ꤍꤌ𐌻 ꤣ ꤒγმγ ꤍ꤀ꤍꤌተ𑀨)) მꤌ ꤐખ ꤐꤍꤕ ꤍ꤀ꤍγઞӄꤣ γр꤀მખ 𐌼꤀рꤌ𐌻𑀨ઞખꤕ ꤒ𐌻ተ))  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤕꤒꤌઞખ꤇ рખꤟꤌр𑀨 ꤍ ꤙꤣउმꤌӄ꤀𐌼 ꤍꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ӄꤌӄ ꤍ ൰ꤣተ꤀𐌼 ઞꤌ ꤙ𐌻ꤕપꤕ ꤀ተ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ?) ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 , ተ꤀ પተ꤀ ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤕꤒꤌ𐌻 ꤐ 𐌼ꤌ꤅ꤌउꤣઞꤕ उꤌ ꤙрꤣ𐌻ꤌꤐӄ꤀𐌼  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤕꤒꤌઞખ꤇ рખꤟꤌр𑀨 ꤍ ꤙꤣउმꤌӄ꤀𐌼 ꤍꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ӄꤌӄ ꤍ ൰ꤣተ꤀𐌼 ઞꤌ ꤙ𐌻ꤕપꤕ ꤀ተ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ?) ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 , ተ꤀ પተ꤀ ተꤐ꤀꤇ ꤀ተꤕꤟ 𐌻ꤕ𐌟ꤌ𐌻 ꤙ꤀ მ꤀ 𐌼ઞ꤀꤇ , ꤌ 𐌼ꤌተ𑀨 ઞꤌმ꤀ 𐌼ઞ꤀꤇ ꤣ ꤎ ꤕё ꤕꤒꤌ𐌻 ꤣઞተꤕઞꤍꤣꤐઞ꤀  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ઞꤌꤙ꤀𐌼ઞꤣ ӄꤌӄ ተખ ꤟꤐꤕተꤕω𑀨 ꤙ꤀ꤍ𐌻ꤕ ꤍꤐ꤀ꤕ꤅꤀ 𐌼ꤣઞꤕተꤌ γ ઞꤌꤍተ꤀ꤎ൰ꤕ꤅꤀ ꤌተ𐌻ꤕተꤌ…!꤀ተꤙꤣωꤣꤍ𑀨 ωӄγрꤌ ?? ?? ??  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤕꤒꤌઞખ꤇ рખꤟꤌр𑀨 ꤍ ꤙꤣउმꤌӄ꤀𐌼 ꤍꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ӄꤌӄ ꤍ ൰ꤣተ꤀𐌼 ઞꤌ ꤙ𐌻ꤕપꤕ ꤀ተ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ?) ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 , ተ꤀ પተ꤀ ተખ 12:09:25 [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤐꤕꤍꤣω𑀨 ઞꤌ 𐌼꤀ё𐌼 𑀋γળ ӄꤌӄ ꤍ꤀ꤙ𐌻ꤎ ꤙр꤀ꤍተખꤕ მꤐꤣ𐌟ꤕઞꤣꤎ.. ꤙр꤀ꤍተખꤕ მꤐꤣ𐌟ꤕઞꤣꤎ.. ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼꤀પӄꤣ ઞꤌ 𑀋γꤎ𑀋 ꤐꤍꤕ꤅꤀ उꤕ𐌼ઞ꤀꤅꤀ ωꤌрꤌ))) ꤌ ተખ рꤕωꤣ𐌻 ꤙр꤀მ꤀𐌻𐌟ꤣተ𑀨 ꤀ꤒખપꤣꤎ ꤐꤌωꤕ꤅꤀ ꤙр꤀ω𐌻ળωꤕꤍተ꤀꤅꤀ р꤀მꤌ ꤎ ꤍ𐌼꤀ተрળ))))  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤕꤒꤎ ꤕꤒꤌ𐌻ꤣ 𑀋ꤌપꤣ ઞꤌ ተꤕꤒꤎ ӄ꤀ઞપꤌ𐌻ꤣ, ઞ꤀ ተખ, ተꤌӄꤌꤎ ω𐌻ળ𑀋ꤌ, પተ꤀ მ𐌻ꤎ ተꤕꤒꤎ ᤋተ꤀ ꤙγꤍተꤎӄ ꤣ 𐌼ꤕ𐌻꤀પꤣ…  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀꤇ ꤌઞꤌ𐌻-მખ𐌼꤀𑀋꤀მ ӄꤌӄ ꤐγ𐌻ӄꤌઞ ꤣउꤐꤕр꤅ꤌꤕተꤍꤎ ተ꤀𐌻𑀨ӄ꤀ ተ꤀𐌻𑀨ӄ꤀ ꤐખ𐌻ꤕተꤌꤕተ ꤀ተተγმꤌ 𐌟ꤣმӄ꤀ꤍተ𑀨 ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ખ ӄ꤀꤅მꤌ ꤀ઞꤌ ꤍӄꤐꤣрተꤣተ))))  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤕꤒꤌઞખ꤇ рખꤟꤌр𑀨 ꤍ ꤙꤣउმꤌӄ꤀𐌼 ꤍꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ӄꤌӄ ꤍ ൰ꤣተ꤀𐌼 ઞꤌ ꤙ𐌻ꤕપꤕ ꤀ተ ઞꤌꤙꤌმꤕઞꤣꤎ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ?) ꤎ ꤐ𑀋꤀𐌟γ ꤐ ተꤐ꤀ળ 𐌼ꤌ𐌼ꤌωγ ꤒꤕउ ꤍተγӄꤌ ꤙ꤀ӄꤌ ተખ ꤍꤙꤣω𑀨 ꤎ ꤕё ꤕꤒγ . ꤀ઞꤌ 𐌼꤀ꤎ 𐌻ꤣપઞꤌꤎ ꤙрꤕઞꤌმ𐌻ꤕउઞ꤀ꤍተ𑀨 . ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤍꤌ𐌼ખ꤇ ꤒ𐌻ꤕꤍӄ , ꤍꤌ𐌼ખ꤇ ӄꤌ꤇ϕ ))) ተ꤀ӄ ꤣઞ꤀꤅მꤌ 𑀋γ꤇ ӄрખउёተ . ӄ꤀р𐌼ꤣ𐌻ꤣ მꤌꤐઞ꤀ ꤙр꤀ꤍተ꤀ ઞꤌꤐꤕрઞ꤀ ))))  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤕꤒꤌઞખ꤇ рખꤟꤌр𑀨 ꤍ ꤙꤣउმꤌӄ꤀𐌼 ꤍꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ӄꤌӄ ꤍ ൰ꤣተ꤀𐌼 ઞꤌ ꤙ𐌻ꤕપꤕ ꤀ተ ઞꤌꤙꤌმꤕઞꤣꤎ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ?) ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 , ተ꤀ પተ꤀ ꤙꤣउმꤌӄ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ꤒγმꤕተ ꤣउ𐌼ꤕઞёઞ 𐌼꤀ꤣ𐌼 𑀋γё𐌼 , ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 , ተ꤀ પተ꤀ ꤎ ꤒγმγ ꤙ꤀ ꤍተꤕꤙꤕઞઞ꤀ ꤕꤒꤌተ𑀨 ꤕё ꤐꤍё ꤍꤣ𐌻𑀨ઞꤕꤕ ꤣ ꤍꤣ𐌻𑀨ઞꤕꤕ પተ꤀ꤒખ ꤀ઞꤌ उꤌ꤅ꤣꤒꤌ𐌻ꤌꤍ𑀨 ꤀ተ ꤀р꤅ꤌउ𐌼ꤌ , ω𐌻ળ𑀋ꤌ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤒ𐌻ꤎ ))) ተખ ӄꤌӄ ꤕꤒꤌઞꤌꤎ ωӄꤌተγ𐌻ӄꤌ 𑀋рꤌઞꤣω𑀨 𐌼꤀꤇ 𑀋γ꤇ γ ꤍꤕꤒꤎ ꤐ꤀ рተγ ꤣ ꤙрꤣ ᤋተ꤀𐌼 ꤍ꤀ꤍёω𑀨 𐌼ઞꤕ ꤕ꤅꤀ ꤍꤐ꤀ꤣ𐌼 მખрꤎꤐખ𐌼 ꤎउખપӄ꤀𐌼  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤕꤒꤌઞખ꤇ рખꤟꤌр𑀨 ꤍ ꤙꤣउმꤌӄ꤀𐌼 ꤍꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ӄꤌӄ ꤍ ൰ꤣተ꤀𐌼 ઞꤌ ꤙ𐌻ꤕપꤕ ꤀ተ ઞꤌꤙꤌმꤕઞꤣꤎ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ?) ӄ꤀р꤀પꤕ , ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 , ተ꤀ પተ꤀ ꤎ ተꤐ꤀ળ 𐌼ꤌ𐌼ꤌωγ ꤀ꤙγꤍተꤣ𐌻 მ꤀ γр꤀ꤐઞꤎ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ , ꤌ ꤙ꤀ተ꤀𐌼 ꤙ꤀ꤐꤕꤍꤣ𐌻 ꤕё ઞꤌ ꤍꤐ꤀꤇ 𐌟ꤕ 𑀋γ꤇ ꤣ ઞꤌપꤌ𐌻 ꤕё ωꤐખрꤎተ𑀨 ꤐ рꤌउઞખꤕ ꤍተ꤀р꤀ઞખ)) ተખ γ൰ꤕрꤒઞખ꤇ 𑀋γꤕꤍ꤀ꤍ ꤀მ꤀ꤒрꤎળ൰ꤣ꤇ 𐌼꤀꤇ 𑀋γ꤇ ? )) ꤎ ꤍꤕ꤇પꤌꤍ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωꤣ ઞꤌተꤎઞγ ꤙꤣउმꤌӄ ઞꤌ ꤍꤌ𐌼ખ꤇ 𐌼ꤌӄꤍꤣ𐌼γ𐌼 ꤣ उꤌꤍተꤌꤐ𐌻ળ მꤕ𐌻ꤌተ𑀨 𐌼ઞγ 𐌼ꤣઞꤕተ )) ꤙ꤀ተ꤀𐌼 ꤎ ӄ꤀р꤀પꤕ ተꤕꤒꤎ उꤌꤍተꤌꤐ𐌻ળ ꤍ꤀ꤍꤌተ𑀨 𐌼ઞꤕ 𑀋γ꤇ ӄꤌӄ ӄ꤀꤅მꤌ ተ꤀ ꤌꤒꤌ𐌼ꤣ 𐌼ઞꤕ ꤍ꤀ꤍꤌ𐌻 ))  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ӄγმрꤎꤐખ꤇ ꤙγმꤕ𐌻𑀨, ӄ꤀ተ꤀р꤀𐌼γ ꤎ ꤐ р꤀ተ ઞꤌꤍꤍꤌ𐌻ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ઞꤌપꤌ𐌻ꤌ 𑀋ꤐꤌተꤌተ𑀨ꤍꤎ ઞꤌ 𐌼꤀꤇ 𑀋γ꤇ પተ꤀ ꤒ ꤎ ꤕꤕ ꤍꤙꤌꤍ ઞ꤀ ꤎ ઞꤕ ꤍꤙꤌꤍꤌተꤕ𐌻𑀨 𐌼ꤌ𐌻ꤣꤒγ ꤣ ꤎ ꤕꤕ 𑀋γꤕ𐌼 ꤙꤣउმꤌઞγ𐌻 ωꤌ𐌻ꤌꤐγ)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙꤣმ꤀р ꤌꤒ꤀ꤍꤍꤌઞખ꤇), ꤐ꤀ተ उꤌપꤕ𐌼 ተખ ઞꤌ ꤍꤐ꤀ળ 𐌼ꤌተ𑀨 ઞꤌꤍꤍꤌ𐌻, ӄ꤀꤅მꤌ 𐌼ખ ꤕꤕ ꤐꤍተрꤕተꤣ𐌻ꤣ) ꤎ ꤙ꤀ઞꤣ𐌼ꤌળ પተ꤀ γ ተꤕꤒꤎ рꤕϕ𐌻ꤕӄꤍખ ꤍ꤀ꤒꤌӄꤣ, ઞ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 𐌟ꤕ ઞꤕ მꤕрꤕꤐ꤀) მꤌ𐌟ꤕ ઞꤕ ꤒрꤕꤐઞ꤀) ꤐ ꤙ꤀ꤍተꤕ𐌻ꤣ ꤀ઞꤌ 𑀋꤀р꤀ωꤌ)-꤀ተꤙꤣωꤣꤍ𑀨 [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤐꤐ꤀მꤣ𐌻 ꤍꤐ꤀ળ ӄ꤀ઞપγ ꤐ ꤐꤕઞખ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ખ) ӄ꤀꤅მꤌ ꤀ઞꤌ ꤒ꤀𐌻ꤕ𐌻ꤌ ꤅рꤣꤙꤙ꤀𐌼)  [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀પꤕ𐌼γ ተખ ꤙ𑀨ꤕω𑀨 𐌼꤀ળ ӄ꤀ઞપγ ꤙ꤀ γተрꤌ𐌼 उꤌ𐌻ꤙ꤀𐌼?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤍγӄꤌ ઞꤌ 𐌼꤀ꤕ𐌼 𑀋γꤕ 𐌻ꤕ𐌟ꤣω𑀨 ӄꤌӄ ઞꤌ ꤙ𐌻ꤎ𐌟ꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤐ ꤙꤣउმγ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ખ 𐌼꤀𐌟ઞ꤀ ꤙ꤀ꤍተꤌꤐꤣተ𑀨 ӄ꤀𐌻꤀ઞӄꤣ ꤣ ꤒγმꤕተ ꤙꤣउმꤌተꤌꤎ ꤐꤣꤒрꤌꤟꤣꤎ ꤙ꤀ ӄ𐌻ꤣተ꤀рγ ተꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ખ,꤀ઞꤌ ꤌ𐌟 ӄ꤀ઞપꤣተ ઞꤕ ꤀ተ 𐌼꤀ꤕ꤅꤀ 𑀋γ,ꤌ ꤀ተ ꤐꤣꤒрꤌꤟꤣꤣ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 𐌻ળꤒꤣተ ӄ꤀꤅მꤌ 𐌼꤀꤇ 𑀋γ꤇ ꤣ꤅рꤌꤕተ ꤍ ઞꤕ꤇ ꤐ ꤍꤌმ꤀-𐌼ꤌउ꤀) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ӄ꤀꤅მꤌ ꤙ꤀ӄγрꤣ𐌻ꤌ 𐌼꤀ꤣ𐌼 𑀋γꤕ𐌼,ተ꤀ ꤕ꤇ ꤍተꤌ𐌻꤀ 𐌻ꤕ꤅પꤕ ઞꤌ მγωꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤍγӄꤌ ઞꤌ 𐌼꤀ꤕ𐌼 𑀋γꤕ ꤐખꤕꤒγꤕω𑀨ꤍꤎ,ꤌ ꤙ꤀ተ꤀𐌼 ꤍ ઞꤕ꤅꤀ ઞꤕ 𑀋꤀પꤕω𑀨 ꤍ𐌻ꤕउꤌተ𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤍꤣმꤣተ ઞꤌ 𐌼꤀ꤕ𐌼 𑀋γꤕ ӄꤌӄ ઞꤌ ተр꤀ઞꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍ𐌻ખω𑀨 ൰ꤌꤐꤕ𐌻𑀨 ઞꤌ𑀋γ꤇?) ተખ 𑀋γ𐌻ꤣ ӄ꤀ 𐌼ઞꤕ მꤌꤐꤌ𐌻 ꤍꤐ꤀ળ 𐌼ꤌተ𑀨 ꤐખꤕꤒꤌተ𑀨 उꤌ ꤒγӄꤕተ ꤟꤐꤕተ꤀ꤐ ተ꤀?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 рꤌꤒ꤀ተꤌꤕተ ઞꤌ 𐌼꤀ꤕ𐌼 𑀋γꤕ) ӄꤌӄ ꤍꤕӄрꤕተઞખ꤇ ꤌ꤅ꤕઞተ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌿ꤌ𐌟ꤌрળ ተꤕꤒꤎ ઞꤌ ꤍӄ꤀ꤐ꤀р꤀მӄꤕ, ꤐ𐌼ꤕꤍተꤕ ꤍ ꤍꤌ𐌻꤀𐌼 ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤣ ꤎ꤇ꤟꤌ𐌼ꤣ ተꤐ꤀ꤕ꤅꤀ ꤀ተꤟꤌ ꤣ ꤍӄ꤀р𐌼𐌻ળ ተꤕꤒꤎ ተꤐ꤀ꤕ꤇ ꤒꤌꤒγωӄꤕ! [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌄ተ꤀ ተꤐ꤀꤇ ꤙрꤕმꤕ𐌻 ꤒрꤌተળઞ𑀨, ተꤐ꤀꤇ 𐌼꤀उ꤅ ઞꤌ ꤅рꤌઞꤣ! [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌓 𐌼ꤣउꤌઞተр꤀ꤙ, ꤙ꤀ተ꤀𐌼γ પተ꤀ ተꤌӄꤣꤕ ӄꤌӄ ተખ ઞꤌउખꤐꤌળተ ꤍꤕꤒꤎ 𐌻ળმ𑀨𐌼ꤣ! [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌱ꤕმꤕω𑀨 ꤍꤕꤒꤎ ꤅𐌻γꤙ꤀, ተγꤙ꤀, ꤌ𐌼꤀рꤌ𐌻𑀨ઞ꤀, ꤐ ꤀ꤒ൰ꤕ𐌼 ተખ ꤙр꤀ꤍተꤣተγተӄꤌ! [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𑀗მꤌተ𑀨 ተꤕꤒꤎ ઞꤌ 𐌼ꤎꤍ꤀ӄ꤀𐌼ꤒꤣઞꤌተ उઞꤌપꤣተ ꤀ꤒꤕꤍꤙꤕપꤣተ𑀨 𐍅ӄрꤌꤣઞγ ꤍꤌ𐌻꤀𐌼 ઞꤌ ተрꤣ ꤅꤀მꤌ! [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𑀥ꤕმ 𐌼꤀р꤀उꤌ ઞꤕተ ꤒрꤌተꤣωӄꤌ, પγმꤌ ઞꤕ ꤍ𐌻γપꤣተꤍꤎ ꤣ ተખ ꤍઞ꤀ꤐꤌ ꤍ꤀𐌻𑀨ꤕω𑀨ꤍꤎ! [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐌑ꤌ𐌼γ ꤕꤒꤌ𐌻? 𐌀 ꤎ, ઞꤕተ. [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𐋏ꤕ ꤕꤒꤌ𐌻 ተꤐ꤀ળ 𐌼ꤌ𐌼γ, ꤙ꤀ተ꤀𐌼γ પተ꤀ ꤀ઞꤌ р꤀𐌟ꤌꤕተ ꤐખр꤀მӄ꤀ꤐ! [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ઞꤌωё𐌻 ઞ꤀ꤐખ꤇ ꤍꤙ꤀ꤍ꤀ꤒ ꤣꤍꤙ꤀𐌻𑀨उ꤀ꤐꤌઞꤣꤎ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ, ꤎ ተꤕꤙꤕр𑀨 ꤐꤕωꤌળ ꤕё उꤌ𐌼ꤕꤍተ꤀ ꤐખӄ𐌻ળપꤌተꤕ𐌻ꤎ, ꤣ 𑀋γꤎрળ 𑀋γꤕ𐌼 ꤙ꤀ ꤙꤣउმꤕ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ, ꤣ ꤍрꤌउγ 𐌟ꤕ ꤐӄ𐌻ળપꤌꤕተꤍꤎ ꤍꤐꤕተ ꤐ ӄ꤀𐌼ઞꤌተꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ӄꤍተꤌተꤣ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤒꤕрꤕተ 𐌼꤀꤇ 𑀋γ꤇ ꤐ рγӄγ ꤣ ꤀рꤕተ "𑀗𐌻ꤌꤐꤌ 𐍅ӄрꤌꤣઞꤕ" [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ӄ꤀꤅მꤌ ꤍ꤀ꤍёተ 𐌼꤀꤇ પ𐌻ꤕઞ, ꤍрꤌउγ ઞꤌપꤣઞꤌꤕተ მꤌꤐꤣተꤍꤎ ꤙ꤀પꤕ𐌼γ, ꤀მઞꤌ𐌟მખ ꤕ꤇ ꤙрꤣω𐌻꤀ꤍ𑀨 उꤌωꤣꤐꤌተ𑀨 ꤅꤀𐌻꤀ꤐγ, ꤙ꤀ꤍ𐌻ꤕ ተ꤀꤅꤀ ӄꤌӄ ꤎ ꤍ𐌻γપꤌ꤇ઞ꤀ ꤙр꤀ꤒꤣ𐌻 ꤕ꤇ उꤌተખ𐌻꤀ӄ 𑀋γꤕ𐌼 ӄ꤀꤅მꤌ ꤀ઞꤌ 𐌼꤀꤇ પ𐌻ꤕઞ ꤍ꤀ꤍꤌ𐌻ꤌ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] γ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤀მꤣઞꤌрઞખ꤇ рꤌꤍꤙ꤀рꤎმ꤀ӄ მઞꤎ, ꤍ꤀ꤍꤌተ𑀨 𐌼꤀꤇ 𑀋γ꤇ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ઞγ ꤙр꤀ꤍተ꤀ ꤎ ꤐપꤕрꤌ ઞꤌꤍꤍꤌ𐌻 ઞꤌ ꤙꤣउმγ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤣ 𐌼ઞꤕ ӄꤌ𐌟ꤕተꤍꤎ પተ꤀ ꤒрꤌተꤣӄꤌ γ ተꤕꤒꤎ ઞꤕ ꤒγმꤕተ ꤣꤒ꤀ ꤎ ꤕ꤅꤀ उꤌተꤙꤣ𐌻?? [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ઞγ ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ӄ꤀꤅მꤌ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤍ𐌻γωꤌꤕተ Ա꤀ꤎ "उꤐꤕउმꤌ ꤙ꤀ ꤣ𐌼ꤕઞꤣ ꤍ꤀𐌻ઞꤟꤌ" ተ꤀ ꤀ઞꤌ ꤙрꤕმꤍተꤌꤐ𐌻ꤎꤕተ 𐌼꤀꤇ 𑀋γ꤇ ઞꤌმ ꤍꤐ꤀ꤕ꤇ ꤙꤣउმ꤀꤇ ӄ꤀ተ꤀рખ꤇ ꤍꤐꤕተꤣተ ꤍꤕꤐꤕрઞખ𐌼 ꤍꤣꤎઞꤣꤕ𐌼? ( [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, ӄ꤀꤅მꤌ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤐꤣმꤣተ 𐌼꤀꤇ 𑀋γ꤇, ꤀ઞꤌ ꤍрꤌउγ 𐌟ꤕ ઞꤌપꤣઞꤌꤕተ ꤍꤌმꤣተꤍꤎ ઞꤌ ӄ꤀𐌻ꤕઞꤣ, ꤣ ꤙр꤀ӄ𐌻ꤌმખꤐꤌተ𑀨 ӄрꤌꤍઞγળ მ꤀р꤀𐌟ӄγ მ𐌻ꤎ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ӄ ꤕё ꤙꤣउმꤕ? 𐌀 ӄꤌӄ ተ꤀𐌻𑀨ӄ꤀ ꤎ ઞꤌપꤣઞꤌળ ꤙ꤀მꤍተꤌꤐ𐌻ꤎተ𑀨 ӄ ઞꤕ꤇ ꤍꤐ꤀꤇ 𑀋γ꤇, ꤀ઞꤌ ꤟꤕ𐌻γꤕተ 𐌼ઞꤕ उꤌ𐌻γꤙγ, ꤣ ꤙрꤣ꤅꤀ꤐꤌрꤣꤐꤌꤕተ "उმрꤌꤐꤍተꤐγ꤇ ꤀ 𐌱ꤕ𐌻ꤣӄꤣ꤇" ?? [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ઞγ ꤌр꤀ꤍተ꤀ ꤙ꤀꤇𐌼ꤣ પተ꤀ ꤕꤍ𐌻ꤣ ተખ ꤍꤕ꤇પꤌꤍ ઞꤕ ꤀ተӄꤌ𐌟ꤕω𑀨ꤍꤎ ꤀ተ მ꤀उખ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ꤐ ተꤐ꤀ꤕ꤇ р꤀ተ꤀ꤐ꤀꤇ ꤙ꤀𐌻꤀ꤍተꤣ ተ꤀ ꤎ ꤒγმγ ꤐખઞγ𐌟მꤕઞ γꤕꤒꤌተ𑀨 ꤍꤐ꤀ꤣ𐌼ꤣ ꤎ꤇ꤟꤌ𐌼ꤣ ꤙ꤀ ተꤐ꤀ꤕ𐌼γ მꤕተꤍӄ꤀𐌼γ ꤌઞγꤍγ? ) ꤣ ꤎ ꤒγმγ ꤒꤣተ𑀨 ꤙ꤀ ઞꤕ𐌼γ ꤙ꤀ӄꤌ ꤀ઞ ઞꤕ ꤙꤕрꤕꤍተꤌઞꤕተ ꤐ꤀ઞꤎተ𑀨 рખꤒ꤀꤇?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ઞγ उꤌ𐌼ꤕተ𑀨, પተ꤀ ꤙ꤀ꤍ𐌻ꤕ ተ꤀꤅꤀ ӄꤌӄ ꤎ ꤕꤒγ ተꤐ꤀ળ 𐌼ꤌተ𑀨, γ ઞꤕё ꤣउ ꤙꤣउმખ ꤕ൰ё ꤐ ተꤕપꤕઞꤣꤣ ተрё𑀋 પꤌꤍ꤀ꤐ 𐌼꤀ꤎ ꤍꤙꤕр𐌼ꤌ ꤐખተꤕӄꤌꤕተ, ꤣ ꤀ઞꤌ ꤕ𐌻ꤕ 𑀋꤀მꤣተ, ꤙрꤣ𑀋꤀მꤣተꤍꤎ ꤕё ઞꤌ 𑀋γꤕ მ꤀𐌼꤀꤇ ተꤌ൰ꤣተ𑀨) 𐌕ꤌ𐌼 ተખ ꤍꤐ꤀ꤣ𐌼 ꤎउખӄ꤀𐌼 ꤟꤕꤙ𐌻ꤎꤕω𑀨 ꤕё ӄ𐌻ꤣተ꤀р ꤣ ተꤌ൰ꤣω𑀨 ꤕё მ꤀ ӄр꤀ꤐꤌተꤣ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ઞꤌ ꤙꤣउმꤌ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤙ꤀ꤐꤕꤍꤣ𐌻 ꤍӄрખተγળ ӄꤌ𐌼ꤕрγ ӄ꤀ተ꤀рꤌꤎ ꤙрꤣ ꤕꤕ ꤙ꤀𑀋꤀მӄꤕ ꤙ꤀ӄꤌउખꤐꤌꤕተ ꤙр꤀ꤟꤕઞተ ꤐખተꤕӄꤌઞꤣꤎ 𐌼꤀ꤕ꤇ ꤍꤙꤕр𐌼ખ ꤣउ ꤕꤕ ꤐ𐌻ꤌ꤅ꤌ𐌻ꤣ൰ꤌ? ( [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ પተ꤀ ተꤌ𐌼 उꤌተγꤙ꤀ӄ ꤕꤒꤌઞઞખ꤇, ꤐ 𐌼꤀꤇ 𑀋γ꤇, ӄꤌӄ ꤐ рγꤙ꤀р ꤀рꤕω𑀨?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ተꤕꤒꤕ ꤙрꤣმёተꤍꤎ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ઞꤌ ӄ𐌻ખӄ ꤙрꤣઞꤎተ𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍખઞ ω𐌻ળ𑀋ꤣ ꤍꤙꤣმ꤀उઞ꤀꤇)ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 𑀋꤀ተꤕ𐌻ꤌ ꤍ 𐌼꤀ꤣ𐌼 𑀋γӄ𐌼 ꤍꤙ ꤙ꤀ꤍተꤌꤐꤣተ𑀨 [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ተꤕꤒꤕ ꤍꤕ꤇પꤌꤍ ꤙ꤀ ൰ꤕӄꤌ𐌼 ꤒγმγ 𑀋γꤕ𐌼 ꤒꤣተ𑀨, ꤙ꤀ӄꤌ ꤀ઞꤣ ઞꤕ ꤙ꤀рꤐγተꤍꤎ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ પተ꤀ ተꤌ𐌼 ተꤌӄ ઞꤕ𐌟ઞ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤙрꤣઞꤣ𐌼ꤌꤕω𑀨 ꤐ р꤀ተ ꤍꤐ꤀꤇ ꤅꤀ꤍተꤕꤐ꤀꤇ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍખઞ ω𐌻ળ𑀋ꤣ ꤍꤙꤣმ꤀उઞ꤀꤇)ተખ ઞꤌ𑀋γꤎ 𐌼ઞꤕ ꤐ 𑀋γ꤇ მખωꤌ𐌻,ӄ꤀꤅მꤌ ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤕꤒꤌ𐌻)?? [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ተꤕꤒꤕ ꤍꤕ꤇પꤌꤍ ተꤐ꤀ળ ωꤌꤙӄγ ꤙр꤀ӄрγપγ ꤐ ተꤐ꤀ё𐌼 ꤌઞꤌ𐌻ꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] પተ꤀ 𐌟ꤕ ተખ 𐌼꤀꤇ 𑀋γ꤇ ꤍ꤀ꤍꤕω𑀨, ӄꤌӄ ꤍꤐ꤀ꤎ 𐌼ꤌተ𑀨-ωꤌ𐌻ꤌꤐꤌ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍખઞ ω𐌻ળ𑀋ꤣ ꤍꤙꤣმ꤀उઞ꤀꤇)ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨 𑀋γꤕ𐌼 ꤐ ꤙ꤀მꤒ꤀р꤀მ꤀ӄ γꤕꤒꤌ𐌻,પተ𐌻ꤒખ ꤀ઞꤌ 𐌼꤀ળ.ꤍꤙꤕр𐌼γ ꤙр꤀꤅𐌻꤀ተꤣ𐌻ꤌ [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀꤇𐌼ꤣ, પተ꤀ ꤎ ተꤕꤒꤎ ꤍꤕ꤇પꤌꤍ ꤐ ተꤐ꤀ꤣ𑀋 𐌼ꤕꤍꤎપઞખ𑀋 γተ꤀ꤙ𐌻ળ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍખઞ ω𐌻ળ𑀋ꤣ ꤍꤙꤣმ꤀उઞ꤀꤇)ተખ 𐌟ꤕ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨 પተ꤀ ተ꤀𐌻𑀨ӄ꤀ 𐌼꤀꤇ 𑀋γ꤇ 𐌼꤀𐌟ꤕተ ተꤐ꤀꤇ р꤀ተ ꤕꤒꤌተ𑀨 [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ γ ተꤕꤒꤎ ꤙрꤣ ꤐꤣმꤕ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ꤐ ӄр꤀ꤐꤣ ꤐꤍꤙ𐌻ꤕꤍӄ ꤌმрꤕઞꤌ𐌻ꤣઞꤌ ꤙр꤀ꤣꤍ𑀋꤀მꤣተ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ 𐌟ꤕ ተꤕꤒꤕ ꤀ꤒ ꤍꤐ꤀꤇ 𑀋γ꤇ ꤍተγӄઞγ ተꤐ꤀ꤣ𐌼 рተ꤀𐌼, પተ꤀ ተખ ꤙꤌ𐌼ꤎተꤣ 𐌻ꤣωꤣω𑀨ꤍꤎ ꤣ ꤙ꤀꤇მёω𑀨 ꤐ ꤒ꤀𐌻𑀨ઞꤣꤟγ, પተ꤀ꤒખ ተꤕꤒꤕ ꤕꤕ ꤐ꤀ꤍꤍተꤌઞ꤀ꤐꤣ𐌻ꤣ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ተꤌӄ ꤍተрꤌઞઞ꤀ ઞꤌ 𐌼꤀꤇ 𑀋γ꤇ ꤙр꤀꤅𐌻ꤎმખꤐꤌꤕω𑀨, ꤎ ꤐꤣ𐌟γ પተ꤀ ተખ ꤐउ꤅𐌻ꤎმ꤀𐌼 ꤕ꤅꤀ γ𐌟ꤕ ꤀ተꤍ꤀ꤍꤌ𐌻) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤐ𐌻ꤌმꤕ𐌻𑀨ꤟγ પꤕꤒγрꤕપઞ꤀꤇ ꤀ተꤍꤌꤍખꤐꤌꤕተ, उꤌ ꤒꤕꤍꤙ𐌻ꤌተઞખ꤇ ꤀ꤒꤕმ, ꤙ꤀ꤍ𐌻ꤕ ꤒ𐌻ꤎმ꤀ӄ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀꤇𐌼ꤣ, પተ꤀ ꤎ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ მꤕ𐌻ꤌળ γꤍ𐌻γ꤅γ, પተ꤀ꤒખ ꤀ઞꤌ 𐌼꤀꤅𐌻ꤌ ꤙ꤀ꤍተ꤀ꤎઞઞ꤀ 𐌼꤀꤇ 𑀋γ꤇ ꤍ꤀ꤍꤌተ𑀨 ꤣ ઞꤕ ꤍተꤕꤍઞꤎተ𑀨ꤍꤎ ꤐ ꤙр꤀ꤍ𑀨ꤒꤕ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ተખ 𐌻꤀𑀋γωӄꤌ ꤕꤒꤌઞઞꤌꤎ, ӄ꤀ተ꤀рꤌꤎ 𐌼ꤕმ𐌻ꤕઞઞ꤀ ꤙꤣωꤕተ, ꤙ꤀ተ꤀𐌼γ પተ꤀ ꤕ𐌼γ પ𐌻ꤕઞ 𐌼꤀꤇ ꤐ 𐌟꤀ꤙꤕ 𐌼ꤕωꤌꤕተ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤐ ӄγрꤍꤕ, પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ઞꤌ ꤍተр꤀꤇ӄꤕ рꤌउрꤕωꤣ𐌻ꤌ 𐌼ઞꤕ рꤌउ𐌼ꤕꤍꤣተ𑀨 ꤐ ꤕё ꤙꤣउმꤕ рꤌꤍተꤐ꤀р, પተ꤀ꤒખ მ꤀𐌼 ꤍ𐌻꤀𐌟ꤣተ𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ተꤕꤒꤎ ꤍꤕ꤇પꤌꤍ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕꤍ ωꤐખрꤌઞγ ꤐ ꤒγმӄγ, ൰ꤕઞ꤀ӄ, પተ꤀ꤒખ ተખ ઞꤕ ተꤎꤐӄꤌ𐌻 ઞꤌ 𐌼꤀꤇ 𑀋γ꤇ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤍꤕ꤇પꤌꤍ ꤙ꤀მ 𐌼꤀꤇ 𑀋γ꤇ ꤙ꤀მꤍተрꤣ꤅𐌻ꤌꤍ𑀨, ꤍმꤕ𐌻ꤌ𐌻ꤌ ꤙγપ꤀ӄ, ӄꤌӄ ઞꤌ 𐌻꤀ꤒӄꤕ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤍꤕ꤇પꤌꤍ ተꤕꤒꤕ ꤐ ꤕꤒꤌ𐌻꤀ ꤍ 𑀋γꤎ 𑀋ꤌрӄઞγ, પተ꤀ꤒખ ተખ ꤙ꤀ઞꤎ𐌻, પተ꤀ ꤎ ተꤐ꤀꤇ 𑀋꤀उꤎꤣઞ, ꤌ ተખ 𐌼꤀ꤎ ꤍ꤀ꤒꤌӄꤌ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ተખ ϕꤌઞꤌተꤕꤕω𑀨 ꤀ተ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ, ӄꤌӄ ꤎрખ꤇ ϕꤌઞꤌተ 𐌼꤀ꤕ꤇ उꤌ𐌻γꤙખ ઞꤌ ꤐꤍꤕ ꤕꤒ𐌻ꤣ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ ꤙ꤀ӄγꤙꤌꤕω𑀨 ꤒꤣ𐌻ꤕተખ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ተꤕꤒꤎ ꤍꤕ꤇પꤌꤍ ꤒγმγ ꤕꤒꤌተ𑀨 ઞꤌ ꤐꤍળ ꤐખმꤕр𐌟ӄγ, પተ꤀ꤒખ ተખ ꤙ꤀ઞꤎ𐌻 , પተ꤀ ઞꤌ 𐌼꤀꤇ 𑀋γ꤇ ꤐꤎӄꤌተ𑀨 ꤒꤕꤍꤙ꤀𐌻ꤕउઞ꤀) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙр꤀ꤍተ꤀ ꤍꤕ꤇પꤌꤍ 𐌼꤀꤇ 𑀋γ꤇ ꤍ꤀ꤍꤣрγꤕω𑀨 ꤣ ઞꤌꤙ꤀𐌼ꤣઞꤌꤕω𑀨 ꤒખ𐌻ખꤕ ꤐрꤕ𐌼ꤕઞꤌ ꤙр꤀ꤐꤕმёઞઞખꤕ ꤍ ተꤐ꤀ꤕ꤇ 𐌼ꤌተꤕр𑀨ળ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ उઞꤌ𐌻, પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 𐌼꤀꤇ 𑀋γ꤇ ꤍ꤀ꤍꤌ𐌻ꤌ, ӄ꤀꤅მꤌ მꤌ 𐌼ખ ꤕ൰ё ꤐ ωӄ꤀𐌻ꤕ γપꤣ𐌻ꤣꤍ𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ተꤕꤒꤎ 𑀋γꤕ𐌼 ꤣꤍተрꤕꤒ𐌻ળ, ӄꤌӄ ተꤕрр꤀рꤣꤍተ꤀ꤐ) ꤙ꤀ተ꤀𐌼γ પተ꤀ ተખ ꤙрꤕმꤍተꤌꤐ𐌻ꤎꤕω𑀨 γ꤅р꤀उγ მ𐌻ꤎ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ተꤕ𐌼 ꤍꤙ꤀ꤍ꤀ꤒ꤀𐌼, પተ꤀ ꤙрꤣӄγꤍખꤐꤌꤕω𑀨 ωӄγрӄγ ઞꤌ 𑀋γꤕ 𐌼꤀ꤕ𐌼 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤍꤕ꤇પꤌꤍ उꤌ𑀋𐌻ꤕꤒઞёω𑀨ꤍꤎ 𐌼꤀ꤕ꤇ ꤍꤙёр𐌼꤀꤇ , 𐌼꤀рꤎӄ ተખ ꤕꤒꤌઞઞખ꤇ , ꤍተγꤙꤌ꤇ ꤍꤐ꤀ꤣ𐌼 рተ꤀𐌼 ꤙ꤀ 𐌼꤀ꤕ𐌼γ 𑀋γળ, પተ꤀ꤒખ ꤎ ተꤕꤒꤎ ઞꤕ ꤐꤣმꤕ𐌻) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤍ𐌻γωꤌ꤇ ꤍળმꤌ, ൰ꤕઞ꤀ӄ , ꤎ ተꤕꤒꤎ ꤕꤒγ ꤣ ꤒγმγ ꤙ꤀ꤍተ꤀ꤎઞઞ꤀ ꤙꤣઞꤌተ𑀨, ꤙ꤀ተ꤀𐌼γ પተ꤀ ተખ उꤌ𐌻γꤙઞખ꤇ ӄ𐌻ꤕ൰𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ተꤕꤒꤎ ꤒγმγ ઞꤌ ꤐꤍꤕ 20 પꤌꤍ꤀ꤐ рꤌꤍተꤎ꤅ꤣꤐꤌተ𑀨 ઞꤌ ꤍꤐ꤀ё𐌼 𑀋γꤕ, ӄꤌӄ ꤙр꤀ꤍተખઞӄγ ) ꤌ ተખ ꤒγმꤕω𑀨 ꤙ𐌻ꤌӄꤌተ𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ተꤕꤒꤕ ꤍꤕ꤇પꤌꤍ ꤐ ꤌઞꤌ𐌻 ꤍꤐ꤀꤇ 𑀋γ꤇ ꤐ꤀ተӄઞγ, ӄꤌӄ 𐌼ꤕપ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍખઞ ω𐌻ળ𑀋ꤣ ꤍꤙꤣმ꤀उઞ꤀꤇)ተખ ઞꤌ𑀋γꤎ ꤍꤐ꤀ꤕ꤇ 𐌼ꤌ𐌼ꤌωӄꤕ ꤐ ꤙꤣउმγ ӄ꤀ઞપꤣ𐌻,ꤙꤣउმ꤀ӄрખ𐌻 ተખ ꤕꤒꤌઞખ꤇) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤍ𐌻γωꤌ꤇, 𐌼꤀𐌟ꤕተ ተખ 𐌼ઞꤕ 𑀋γ꤇ ꤍꤐ꤀ꤣ𐌼 ꤅꤀р𐌻꤀𐌼 ઞꤌተрꤕω𑀨, ӄꤌӄ ꤐꤕ𑀋꤀ተӄ꤀꤇ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ተꤕꤒꤎ ꤍꤕ꤇પꤌꤍ ꤐ ꤕꤒ𐌻꤀ ꤐꤍተꤌꤐ𐌻ળ 𑀋γ꤇, ӄꤌӄ ӄ𐌻ળપ ꤐ 𐌼ꤌωꤣઞγ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ પተ꤀ γ൰ꤕрꤒઞꤌꤎ ተꤌӄꤌꤎ, ꤌ ઞγ ꤍ𑀨ꤕꤒꤌ𐌻ꤍꤎ, ꤙ꤀ӄꤌ 𐌼꤀꤇ 𑀋γ꤇ მ꤀ꤒр ӄ ተꤐ꤀ꤕ𐌼γ ઞꤌγપγ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ 𑀋γ𐌻ꤣ 𐌼꤀꤇ 𑀋γ꤇ ꤍꤐ꤀ꤣ ꤌઞꤌ𐌻꤀𐌼 ꤀ꤒઞꤣ𐌼ꤌꤕω𑀨, ӄꤌӄ ꤍꤐ꤀ꤕ꤅꤀ ꤀ተꤟꤌ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ተખ ꤍ ӄꤌꤙꤍ꤀𐌼 ꤣ ωꤌꤙӄ꤀꤇ 𐌼꤀꤇ 𑀋γ꤇ მ꤀ ᤋ꤇ϕ꤀рꤣꤣ მ꤀ꤐꤕმёω𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ꤍꤕ꤇પꤌꤍ ꤍꤐ꤀꤇ 𑀋γ꤇ ꤒγმγ მꤌꤐꤌተ𑀨 ઞꤕ 𐌻ꤣω𑀨 ተꤕꤒꤕ ઞ꤀ ꤣ ተꤐ꤀ꤕ𐌼γ მрγ꤅γ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𑀋γ𐌻ꤣ ተખ 𐌼ઞꤕ ꤐ 𑀋γ꤇ ꤙ𐌻ꤌપꤕω𑀨, ӄꤌӄ ተꤕ𐌻ӄꤌ ꤕꤒꤌઞઞꤌꤎ, γ𐌟ꤕ 𐌼ઞꤕ उꤌ𐌻γꤙγ ꤙр꤀𐌼꤀પꤣ𐌻) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ተખ ꤍ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ, ӄꤌӄ પꤕωγꤎ ꤍꤙ꤀𐌻उёω𑀨 ꤣ ꤍꤙꤌተ𑀨 ꤀ተꤙрꤌꤐꤣω𑀨ꤍꤎ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ઞꤕ ઞγ ꤌ પꤕ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 𐌼ઞꤕ ꤍ꤀ꤍꤕተ ꤒꤕउ ꤙꤕрꤕმખωӄꤣ, ꤀પꤕઞ𑀨 ተખ ꤕꤒꤌઞઞખ꤇ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ 𑀋γ𐌻ꤣ 𐌼꤀꤇ 𑀋γ꤇ ꤍꤐ꤀ꤣ𐌼 рተ꤀𐌼 ꤙ꤀उ꤀рꤣω𑀨) ꤍъꤕꤒꤣꤍ𑀨 ꤐ ꤒγმӄγ ൰ꤕઞ꤀ӄ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀꤇𐌼ꤣ, પተ꤀ ተꤐ꤀ё ꤙрꤣउꤐꤌઞꤣꤕ 𐌼ઞꤕ ꤐ 𑀋γ꤇ მγმꤕተ𑀨 ꤐ꤀ ꤐрꤕ𐌼ꤎ ꤒꤕ꤅ꤍተꤐꤣ꤇, પ𐌻ꤕઞ꤀꤅𐌻꤀ተ ተખ ꤀ꤙγ൰ꤕઞઞખ꤇ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𑀋γ𐌻ꤣ ተખ ተꤌ𐌼 ꤍꤙрꤎተꤌ𐌻ꤍꤎ उꤌ ꤙꤣउმꤌӄ ꤍꤐ꤀ꤕ꤇ 𐌼ꤌተꤕрꤣ, ωꤌ𐌻ꤌꤐખ ꤕꤒꤌઞઞ꤀꤇) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ተꤕꤒꤕ ꤀ተ𐌟ꤌрળ, ӄꤌӄ ω𐌻ળωӄγ) પተ꤀ ተખ ꤒγმꤕω𑀨 ꤐ ꤍተрꤌ𑀋ꤕ ꤀ተ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ γꤒꤕ꤅ꤌተ𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤌ ઞγ ꤐખተꤌꤍӄꤣꤐꤌ꤇ ꤍꤐ꤀꤇ 𐌀ઞꤌ𐌻 ꤣउ ӄꤌр𐌼ꤌઞꤌ ꤣ 𐌻꤀𐌟ꤣ ઞꤌ ꤍተ꤀𐌻, ꤎ ꤕ꤅꤀ ꤒγმγ ꤕꤒꤌተ𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ተꤕꤒꤎ ꤕꤒγ, ꤌ ተખ ꤍ ꤙ𐌻ꤌપꤕ𐌼 ꤒꤕ𐌟ꤣω𑀨 ӄ 𐌼ꤌ𐌼ꤕ, પተ꤀ꤒખ ꤀ઞꤌ ꤍꤐ꤀ꤣ𐌼 ꤀પӄ꤀𐌼 ተꤐ꤀ё ꤕꤒꤌ𐌻꤀ ꤙрꤣӄрખ𐌻ꤌ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀પꤕ𐌼γ ተખ 𐌼꤀꤇ 𑀋γ꤇ ꤐ ꤍꤐ꤀ё𐌼 рተγ ꤅рꤕꤕω𑀨 ꤐ 𐌼꤀р꤀उખ) ꤣꤒ꤀ ተખ მ꤀р꤀𐌟ꤣω𑀨 ꤣ𐌼 ꤒ꤀𐌻𑀨ωꤕ, પꤕ𐌼 ꤍꤐ꤀ꤕ꤇ 𐌼ꤌተꤕр𑀨ળ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ተꤕꤒꤕ 𑀋γꤕ𐌼 ꤙ꤀ ꤕꤒꤌ𐌻γ მꤌ𐌼, પተ꤀ ተખ ꤙ꤀ተꤕрꤎꤕω𑀨 ꤍપёተ ӄꤌ𐌻ꤕઞმꤌрꤎ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተꤐ꤀꤇ ꤌઞγꤍ ઞꤌ 𐌼꤀ꤕ𐌼 𑀋γꤕ, ӄꤌӄ ꤒꤌተ꤀ઞ ꤒγმꤕተ ӄр꤀ωꤣተꤍꤎ, γꤕꤒꤣ൰ꤕ ꤕꤒꤌઞઞ꤀ꤕ, р꤀꤇ ꤍꤕꤒꤕ γꤒꤕ𐌟ꤣ൰ꤕ, ꤙ꤀ተ꤀𐌼γ પተ꤀ 𐌼꤀꤇ 𑀋γ꤇ γꤍተр꤀ꤣተ ꤐ ተꤐ꤀ё𐌼 рተγ ꤌꤙ꤀ӄꤌ𐌻ꤣꤙꤍꤣꤍ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ પተ꤀ -ተ꤀ ꤙрꤣӄꤣმખꤐꤌꤕω𑀨ꤍꤎ ꤍꤙꤕр𐌼꤀꤅𐌻꤀ተ꤀𐌼) ꤎ ተ꤀ उઞꤌળ, પተ꤀ ተખ ꤎрખ꤇ પ𐌻ꤕઞ꤀ꤍ꤀ꤍ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ተꤕꤒꤕ ꤍꤕ꤇પꤌꤍ ꤒγმγ ꤕꤒꤌ𐌻꤀ ꤍઞ꤀ꤍꤣተ𑀨 𑀋γꤕꤍ, ӄꤌӄ ꤙ꤀ꤍተр꤀ꤕઞꤣꤕ ꤍተꤌр꤀ꤕ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤍ𐌻ખω𑀨 ӄ꤀પꤕр꤅ꤌ ꤕꤒꤌઞઞꤌꤎ, ꤎ ተꤕꤒꤕ ꤍꤕ꤇પꤌꤍ ꤌઞꤌ𐌻 ꤒγმγ પꤣꤍተꤣተ𑀨 ꤍꤌ𐌻ꤣ𐌼 𑀋γꤕ𐌼, ꤀ተ ꤐꤍꤎӄꤣ𑀋 𐌼ꤕተꤌ𐌻𐌻꤀ꤐ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ተꤌӄ ꤙр꤀ꤍተ꤀ 𐌼ઞꤕ ꤐ 𑀋γ꤇ ઞꤌપꤌ𐌻 მખωꤌተ𑀨, ꤙ꤀ተ꤀𐌼γ પተ꤀ ꤎ ተꤕꤒꤎ рꤌउъꤕꤒખꤐꤌળ, ӄꤌӄ ൰ꤕઞӄꤌ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀꤇𐌼ꤣ, પተ꤀ ተખ 𐌼꤀꤇ 𑀋γ꤇ ઞꤕ ꤙ꤀ተꤎઞꤕω𑀨, ꤣꤒ꤀ ꤎ ተꤐ꤀꤇ ꤌઞγꤍ ӄꤌӄ ઞ꤀ꤍӄꤣ ઞꤌ ꤍꤐ꤀꤇ 𑀋γ꤇ ꤀მꤕઞγ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀꤇𐌼ꤣ, પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤀ተ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ, ӄꤌӄ ꤐ꤀उმγωઞખ꤇ ωꤌрꤣӄ ꤍმγꤐꤌꤕተꤍꤎ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ተꤕꤒꤎ ꤍꤕ꤇પꤌꤍ ꤍ꤀ ꤍꤐ꤀ꤕ꤅꤀ 𑀋γꤎ ꤍӄꤣઞγ, ӄꤌӄ ꤒ𐌻ꤎተ𑀨 𐌼ꤌ꤇ӄγ ꤅рꤎउઞγળ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤙ꤀પꤕ𐌼γ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤍꤐ꤀ꤣ𐌼 рተ꤀𐌼 ꤀ተ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ उꤌ൰ꤣ൰ꤌꤕተꤍꤎ, ӄꤌӄ ൰ꤣተ꤀𐌼 ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ተꤕꤒꤎ ӄꤌӄ ꤟꤕ𐌻ӄγ ꤕꤒꤌઞઞγળ ꤍ꤀рꤐγ ꤍ꤀ ꤍꤐ꤀ꤕ꤅꤀ 𐌗𐍅𐌓) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ 𐌼꤀꤇ 𑀋γ꤇ ꤍꤕ꤇પꤌꤍ ꤒγმꤕω𑀨, ӄꤌӄ પёрઞꤌꤎ მખрꤌ ꤙ꤀꤅𐌻꤀൰ꤌተ𑀨 ꤣ ꤍተꤌઞꤕω𑀨 ꤙ꤀𑀋꤀𐌟ꤣ𐌼 ઞꤌ ꤍꤐ꤀ળ 𐌼ꤌተ𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ પተ꤀ ተꤌӄꤌꤎ ઞꤕ𐌼꤀൰𑀨) ꤎ ተꤕꤒꤎ ꤕꤒγ, ꤌ ተખ ꤙр꤀ꤍተ꤀ ઞꤌપꤣઞꤌꤕω𑀨 ꤍ𐌻ꤣꤐꤌተ𑀨ꤍꤎ ઞꤌ 𐌼꤀꤇ 𑀋γ꤇, ӄꤌӄ ꤅꤀ꤐઞ꤀ ꤐ γઞꤣተꤌउꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ተꤐ꤀ળ 𐌼ꤌተ𑀨 ꤍꤕ꤇પꤌꤍ ઞꤌ ꤍꤐ꤀꤇ ωተખӄ ꤙ꤀ꤍꤌ𐌟γ, ꤀ઞꤌ ꤒγმꤕተ ӄꤌӄ ꤒγმꤕተꤕ ꤍ γተрꤌ ӄγӄꤌрꤕӄꤌተ𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ተꤕꤒꤕ ꤍꤕ꤇પꤌꤍ ꤐ ꤌઞꤌ𐌻 ꤍꤐ꤀꤇ 𑀋γ꤇, ӄꤌӄ ꤒ𐌻ꤎተ𑀨 рꤌӄꤕተγ ꤐꤍተꤌꤐ𐌻ળ ꤣ ተꤐ꤀꤇ ꤌઞγꤍ ꤍተꤌઞꤕተ ꤒ꤀ꤕ꤅꤀𐌻꤀ꤐӄ꤀꤇ 𑀗𐌸𐌀) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ተખ рꤌઞ꤀ ꤣ𐌻ꤣ ꤙ꤀उმઞ꤀ ꤙ꤀꤇მꤕω𑀨 𐌟ꤌ𐌻꤀ꤐꤌተ𑀨ꤍꤎ 𐌼ꤌ𐌼ꤕ, પተ꤀ ꤎ ተꤕꤒꤎ ꤕꤒγ ઞꤕ꤀მઞ꤀ӄрꤌተઞ꤀ ꤐ ተꤐ꤀ળ ൰ꤕ𐌻𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] γ ተꤕꤒꤎ ꤀ተ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ꤍꤕ꤇પꤌꤍ ꤙ꤀ꤎꤐꤎተꤍꤎ ꤙрખ൰ꤣ ઞꤌ ꤕꤒꤌ𐌻ꤕ, ꤙ꤀ተ꤀𐌼γ પተ꤀ ተખ ꤒ𐌻ꤎተ𑀨 ꤕ꤅꤀ ꤍꤐ꤀ꤣ𐌼 рተ꤀𐌼 ઞꤕ 𐌼꤀𐌟ꤕω𑀨 ꤙ꤀𐌼ખተ𑀨) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ተꤕꤒꤕ ꤍꤕ꤇પꤌꤍ ઞꤌ ꤕꤒꤌ𐌻꤀ ઞꤌꤍꤍγ ꤣ ተખ ꤒγმꤕω𑀨 მγ𐌼ꤌተ𑀨, પተ꤀ ተખ ઞꤌ рꤕપӄꤕ ӄγꤙꤌꤕω𑀨ꤍꤎ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] 𑀋γ𐌻ꤣ ተખ ተꤌ𐌼 рꤌउઞખ𐌻ꤍꤎ 𑀋γꤕꤍ꤀ꤍ ተખ ꤕꤒꤌઞઞખ꤇, ꤎ ተꤕꤒꤕ ꤍꤕ꤇પꤌꤍ ꤙрꤌꤐખ꤇ 𑀋γӄ ꤍ 𑀋γꤎ მꤌ𐌼 ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ꤎ ઞꤌ ꤐખმꤕр𐌟ӄγ ተꤐ꤀꤇ ꤌઞγꤍ, ӄꤌӄ ઞ꤀𐌟꤀𐌼 ꤐꤍꤙ꤀рળ ተꤕꤒꤕ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ પተ꤀ ተꤌ𐌼 ꤙ𐌻ꤌપꤕω𑀨 ꤐ γ꤅꤀𐌻ӄꤕ, ꤍઞ꤀ꤐꤌ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ઞꤕ მ꤀ꤍተꤌ𐌻꤀ꤍ𑀨)? [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ꤎ ተꤕꤒꤎ ꤍꤕ꤇પꤌꤍ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕꤍ ꤀ተр꤀ϕꤣрγꤕተ, 𑀋γꤕꤍ꤀ꤍ ተખ ꤕꤒꤌઞઞખ꤇) ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ተખ ꤙр꤀ꤍተ꤀ 𐌼꤀ꤕ𐌼γ 𑀋γળ, ӄꤌӄ ꤒ꤀꤅γ ꤙ꤀ӄ𐌻꤀ઞꤎꤕω𑀨ꤍꤎ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ઞꤣӄ꤀꤅მꤌ ઞꤕ उꤌ𐌼ꤕપꤌ𐌻 , પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 𐌼꤀꤇ 𑀋γ꤇, ꤍꤐ꤀ꤣ𐌼 рተ꤀𐌼, ӄꤌӄ ꤒрꤣተꤐ꤀꤇ ꤒрꤕꤕተ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ उꤌપꤕ𐌼 ꤍꤐ꤀꤇ р꤀ተ ꤙ꤀მ 𐌼꤀꤇ 𑀋γ꤇ उꤌተ꤀પꤣ𐌻, ӄꤌӄ ળꤐꤕ𐌻ꤣр) 𑀋꤀પꤕω𑀨 પተ꤀ꤒખ ꤎ ꤙ꤀მ𐌼ꤕተꤣ𐌻 ꤍꤐ꤀ꤣ𐌼 𑀋γꤕꤍ, ꤐꤍળ ተ꤀ઞӄ꤀ꤍተ𑀨 ꤅рꤌઞꤣ ተꤐ꤀ꤕ꤅꤀ рተꤌ?) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ተખ ӄ𐌻꤀ꤙ ꤕꤒꤌઞઞખ꤇, ꤎ ተꤕꤒꤎ ꤍꤐ꤀ꤣ𐌼 𑀋γꤕ𐌼 рꤌउმꤌꤐ𐌻ળ, ઞꤌꤍꤕӄ꤀𐌼꤀ꤕ ተખ ꤕꤒꤌઞઞ꤀ꤕ ) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤍꤕ꤇પꤌꤍ ઞꤌપઞёω𑀨 ꤐ ꤍ𐌻ꤕउꤌ𑀋 ꤍ 𐌼꤀ꤕ꤅꤀ 𑀋γꤎ ꤍꤙрખ꤅ꤣꤐꤌተ𑀨 ꤣ ꤙ𐌻ꤌӄꤌተ𑀨, પተ꤀ ꤎ ተꤕꤒꤕ ꤌઞγꤍ ꤙ꤀рꤐꤌ𐌻) [<emoji document_id=5229205949410978575>🥺</emoji>]',
'[<emoji document_id=5229205949410978575>🥺</emoji>] ተખ ꤙ꤀ઞꤣ𐌼ꤌꤕω𑀨, પተ꤀ ተꤐ꤀ꤎ 𐌼ꤌተ𑀨 ꤙ꤀მ 𐌼꤀꤇ 𑀋γ꤇, ӄꤌӄ उ𐌼ꤕꤎ उꤌꤙ꤀𐌻उꤌꤕተ ꤣ ꤀ተӄ𐌻ꤌმખꤐꤌꤕተ ተꤌ𐌼 ꤍꤐ꤀ꤣ𑀋 उꤌр꤀მખωꤕ꤇ ઞꤕმ꤀ઞ꤀ωꤕઞઞખ𑀋 , ꤐр꤀მꤕ ተꤕꤒꤎ ) [<emoji document_id=5229205949410978575>🥺</emoji>]' ]
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl8))
            await sleep(0.1)
            await sleep(time)

    async def терроукрэйнcmd(self, message):
        """— Запускает модуль по указанной команде"""
        args = utils.get_args(message)
        if not args:
            self.db.set(self.strings["name"], "state", False)
            await utils.answer(message, "<b><emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5287336918718096355>☠️</emoji> 𐌑᧐ду᧘ь #Уκρ϶ᥔн нᥲчᥲ᧘ ᥱδᥲɯᥙᴛь ᴛᥱ ⲙᥲᴛь ʙ᧐ ᥙⲙя 𐌲ᥙᴛ᧘ᥱρᥲ <emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5287336918718096355>☠️</emoji></b>")
            return 
        await utils.answer(
             message,
             "<b><emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5287336918718096355>☠️</emoji> 𐌑᧐ду᧘ь #Уκρ϶ᥔн ᥰᥱρᥱᥴᴛᥲ᧘ ᥱδᥲɯᥙᴛь ᴛᥱ ⲙᥲᴛь ʙ᧐ ᥙⲙя 𐌲ᥙᴛ᧘ᥱρᥲ. <emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5287336918718096355>☠️</emoji>\n\n"
             "<emoji document_id=5460857321213142111>🇩🇪</emoji><emoji document_id=5287336918718096355>☠️</emoji>  Կᴛ᧐δы ᧐ᥴᴛᥲн᧐ʙᥙᴛь ᥰρ᧐ᥰᥙɯᥙ. <code>.терроукрэйн</code></b>"
         )         
        try:
             time = float(args[0])
        except ValueError:
             return
        text = " ".join(utils.get_args_raw(message).split()[1:])
        shabl = [
        '❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡυⲇⲟⲣ ⲁⳝⲟⲥⲥⲁⲏыύ), ⲃⲟⲧ ⳅⲁⳡⲉⲙ ⲧы ⲏⲁ ⲥⲃⲟю ⲙⲁⲧь ⲏⲁⲥⲥⲁⲗ, ⲕⲟⲅⲇⲁ ⲙы ⲉⲉ ⲃⲥⲧⲣⲉⲧυⲗυ) я ⲡⲟⲏυⲙⲁю ⳡⲧⲟ ⲩ ⲧⲉⳝя ⲣⲉⲫⲗⲉⲕⲥы ⲥⲟⳝⲁⲕυ, ⲏⲟ ⲧⲃⲟя ⲙⲁⲧь ⲯⲉ ⲏⲉ ⲇⲉⲣⲉⲃⲟ) ⲇⲁⲯⲉ ⲏⲉ ⳝⲣⲉⲃⲏⲟ) ⲃ ⲡⲟⲥⲧⲉⲗυ ⲟⲏⲁ ⲭⲟⲣⲟⲱⲁ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲃⲟⲧ ⲥ ⲧⲉⳝя ⲡⲟⲣⲁⲯⲁюⲥь) ⳡⲉⲥⲧⲏⲟ ⲃⲟⲧ ⲏⲁⲭⲩύ ⲧы ⲥⲟⲥⲉⲱь ⲭⲩυ? υ ⲇⲁⲉⲱь ⲃⲥⲉⲙ ⲃ ⲁⲏⲁⲗ) ⲧⲃⲟя ⲙⲁⲧь ⳝыⲗⲁ ⲡⲟⲣяⲇⲟⳡⲏⲟύ ⲇⲉⲃⲟⳡⲕⲟύ, ⲡⲟⲕⲁ ⲙⲟύ ⲭⲩύ ⲏⲉ ⲃⲥⲧⲣⲉⲧυⲗⲁ ⲁ ⲧы ⲧⲁⲯⲉ ⲉⲅⲟ ⲏⲉ ⲃⲥⲧⲣⲉⳡⲁⲗ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲥⲟⲥⲉⲱь ⲕⲁⲕ ⲣⲁⲕⲉⲧⲁ ⲉⳝⲁⲏⲁя  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲃ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲡⲟⲗⲟⲯυⲗ ⲥⲃⲟύ ⲭⲩύ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲇⲯⲉⲕυ ⳡⲁⲏ, ⲡⲣыⲅⲏⲩⲗ υ ⲩⲉⳝⲁⲗ ⲥ ⲃⲉⲣⲧⲩⲭυ ⲧⲃⲟⲉύ ⲙⲁⲙⲕⲉ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕυ ⲁⲧⲟⲙⲏⲩю ⳝⲟⲙⳝⲩ ⲃⳅⲟⲣⲃⲁⲗ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲕⲩ ⲁ υⳅ ⲡυⳅⲇы ⲃыⲅⲗяⲇыⲃⲁⲉⲱь ⲧы  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲟⲣυⲅυⲏⲁⲗьⲏⲁя ⳅⲁⳃⲉⲕⲁⲏⲕⲁ ⲙⲟⲉⲅⲟ ⳅⲩя) яⲧⲃⲟюⳝⲙⲁⲧь ⲃ ⲩⲭⲟ ⲉⳝⲁⲗ υ ⲇⲟⲃⲉⲗ ⲉⲉ ⲇⲟ ⲡⲩⲱⲉⳡⲏⲟⲅⲟ ⲟⲣⲅⲁⳅⲙⲁ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡ ⲧⲟ я ⲃ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲩⲥⲧⲁⲏⲟⲃυⲗ ⲅⲁⳅⲟⲃыύ ⳝⲁⲗⲟⲏ υ ⲡⲗυⲧⲕⲩ ⳡⲧⲟ ⳝы ⲉⳝⲁⲧь ⲉⲉ υ ⲅⲟⲧⲟⲃυⲧь ⲕⲩⲱⲁⲧь ⳝⲉⳅ ⲡⲉⲣⲉⲣыⲃⲁ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⳃⲁⲥ ⲃ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳝⲩⲇⲩ ⲫⲩⲧⳝⲟⲗьⲏыⲉ ⲙяⳡυ ⳅⲁⳝυⲃⲁⲧь))ⲏⲩ ⲉⲧ ⲧⲁⲕ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲭⲩⲉⲡⲗⲉⲧ ⲉⳝⲁⲏыύ, ⲥ ⲕⲁⲕυⲙυ ⲥⲗⲟⲃⲁⲙυ ⲧы ⲥⲟⲥⲁⲗ ⲩ ⳝⲁⲧυ ⲥⲃⲟⲉⲅⲟ?  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲉ ⲏⲁⲡⲣяⲅⲁύⲥя, ⲁ ⲧⲟ ⲥⲡⲉⲣⲙы ⲅⲗⲟⲧⲁⲏⲉⲱь υ ⲏⲁ ⲭⲩύ ⲡⲟύⲇⲉⲱ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱ ⲧы, ⲱⲁⲃⲕⲁ ⳝⲗяⲇь, я ⲙⲟⲅⲩ ⳝыⲧь ⳅⲗⲟύ!  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲧⲁⲕ ⲙⲏⲟⲅⲟ ⲇⲩⲙⲁⲉⲱь ⲡⲣⲟ ⲭⲩυ ⲡⲟⲧⲟⲙⲩ ⳡⲧⲟ ⲧⲉⳝⲉ υⲭ ⳡⲁⲥⲧⲟ ⲥⲩюⲧ?!  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳υⲇυ ⲙⲟю ⲥⲧⲉⲏⲩ ⲟⲭⲣⲁⲏяύ ⲟⲏⲁ ⲏⲩⲯⲇⲁⲉⲧⲥя ⲃ ⲡⲥυⲏⲉ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲩⲯⲉ ⲏⲉ ⲟⲇυⲏ ⲣⲁⳃ ⲉⳝⲁⲏыύ, ⲟⲧ ⲧⲉⳝя ⳝⲟⲙⲇυⲭⲁ ⲣⲟⲇυⲗⲁ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲉⳝя ⲟⲧ ⲉⳝⲁⲗ ⲃⲉⲣⳝⲗюⲇ ⲧⲉⲡⲉⲣь ⲧы ⲏⲉⲙⲟⲯⲉⲱ ⲩⲧⲉⳝя ⲡⲁⲏυⲕⲁ ⲡⲟ ⲇⲣⲁⳡυⲧь?  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲩ ⲗⲁⲇⲏⲟ, υⲇυ ⲇⲣⲟⳡυ, ⲡⲥυⲏⲕⲁ)   ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲉⳝⲉ ⲥⲟ ⲥⲡⲉⲣⲙⲟύ ⲃⲟ ⲣⲧⲩ ⲩⲇⲟⳝⲏ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲩ ⲩⲇυⲃⲗюⲥь ⲉⲥⲗυ ⲟⲏⲁ ⲧⲃⲟ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲁⲙ ⲡⲟⲱⲩⲧυⲗ, ⲥⲁⲙ ⲡⲟⲣⲯⲁⲗ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲙⲕⲁ ⲡⲥυⲏⲁ ⲕⲟⲅⲇⲁ ⲥⲟⲥёⲧ ⲩ ⲃⲁⲗⲉⲏⲧυⲏⲁ,. ⲉⳝⲁⲏⲏⲏⲁя ⲧы ⳝⲗяⲇυⲏⲁ. ⲥⲧⲟυⲱь ⲏⲁ ⲕⲟⲣяⳡⲕⲁⲭ ⲡⲟⲥⲗⲉ ⲁⲙⲫⲉⲧⲁⲙυⲏⲁ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲃⲟⲧ ⲥ ⲧⲉⳝя ⲡⲟⲣⲁⲯⲁюⲥь) ⳡⲉⲥⲧⲏⲟ) ⲃⲟⲧ ⲏⲁⲭⲩύ ⲧы ⲥⲟⲥⲉⲱь ⲭⲩυ? υ ⲇⲁⲉⲱь ⲃⲥⲉⲙ ⲃ ⲁⲏⲁⲗ) ⲧⲃⲟя ⲙⲁⲧь ⳝыⲗⲁ ⲡⲟⲣяⲇⲟⳡⲏⲟύ ⲇⲉⲃⲕⲟύ) ⲡⲟⲕⲁ ⲙⲟύ ⲭⲩύ ⲏⲉ ⲃⲥⲧⲣⲉⲧυⲗⲁ ⲁ ⲧы ⲇⲁⲯⲉ ⲉⲅⲟ ⲏⲉ ⲃⲥⲧⲣⲉⳡⲁⲗⲁ,ⲁ ⲩⲯⲉ ⲥⲟⲥⲉⲱь ⲕⲁⲕ ⲣⲁⲕⲉⲧⲁ 12:11:25 ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲏⲏⲁя)ⲩ ⲧⲃⲟⲉύ ⲙⲁⲙы ⲏⲩ ⲡⲣⲟⲥⲧⲟ ⲡυⳅⲇⲉц ⲕⲁⲕⲁя ⳝⲟⲗьⲱⲁя ⲡυⳅⲇⲁ, я ⲧⲩⲇⲁ ⲡⲟⲗⲏⲟⲥⲧью ⲃⲭⲟⲇυⲗ. эⲧⲟ ⲡυⳅⲇⲉц, я ⲕⲁⲣⳡ ⲃⲟⳅⲗⲉ ⲉⲉ ⲡυⳅⲇы ⲕⲟⲃⲣυⲕ ⲡⲟⲗⲟⲯυⲗ, ⳡⲧⲟⳝ ⲏⲟⲅυ ⲃыⲧυⲣⲁⲧь ⳝⲗяⲧь  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я эⲧⲟⲅⲟ ⲏⲉ ⳅⲏⲁю ⲃⲉⲇь ⲏⲉ ⲃυⲇⲉⲗ ⲧⲉⳝя, ⲁ ⲉⲥⲗυⳝы ⲩⲃυⲇⲉⲗ, ⲧⲟ ⲧⲣⲁⲭⲏⲩⲗ ⳝы ⲧⲉⳝя ⲃⲟ ⲃⲥⲉ ⲡυⲭⲁⲧⲉⲗьⲏыⲉ υ ⲇыⲭⲁⲧⲉⲗьⲏыⲉ, ⲃⲟ ⲃⲥⲉ ⲥⲩⳃⲉⲥⲧⲃⲩюⳃυⲉ υ ⲏⲉ ⲥⲩⳃⲉⲥⲧⲃⲩюⳃυⲉ, ⲁ ⲧⲉ ⳡⲧⲟ ⲏⲉ ⲥⲩⳃⲉⲥⲧⲃⲩюⲧ ⲡⲣυⲇⲩⲙⲁⲗ ⳝы, υ ⲡⲟⲃⲉⲣь ⲙⲏⲉ ⲅⲏυⲇⲁ ⳅⲁⲧⲣⲁⲭⲁⲏⲏⲟ-ⲩⲣⲟⲇⲗυⲃⲁя ⲧⲉⳝⲉ ⳝы эⲧⲟ ⲡⲟⲏⲣⲁⲃυⲗⲟⲥь  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲃ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲥⲩⲏⲩ ⲥⳡⲉⲧυⲕ ⲅⲉύⲅⲉⲣⲁ ⳡⲧⲟⳝы ⲟⲏ υⳅⲙⲉⲣяⲗ ⲣⲁⲇυⲁцυю ⲃ ⲧⲃⲟⲉⲙ ⲁⲏⲁⲗⲉ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⲙⲏυⲱь ⲕⲁⲕ ⲧы ⲙⲟύ ⲭⲩύ ⲩⳅⲏⲁⲗⲁ,ⲥⲣⲉⲇυ ⲧыⲥяⳡυ? ⲥⲣⲁⳅⲩ ⲩⲃυⲇⲉⲗⲁ ⲧⲟ,ⳡⲧⲟ ⲡⲣυⲏυⲙⲁⲉⲱь ⲃ ⲣⲟⲧ ⲕⲁⲯⲇыύ ⲇⲉⲏь)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⳝⲗя, ⲡυⳅⲇⲁ ⲧⲩⲡⲁя, ⲧы ⳡⲉ ⲥⲩⲕⲁ ⲏⲁⲭⲩύ ⲃъⲉⳝⲁⲗⲁⲥь ⲡⲟ ⲡⲟⲗⲏⲟύ? я ⲧⲉⳝⲉ ⲥⲉύⳡⲁⲥ ⲡυⳅⲇⲩ ⲧⲃⲟю ⲏⲁⲭⲩύ ⲥⲕⲣⲩⳡⲩ,ⲡⲟⲧⲁⲥⲕⲩⲱⲕⲁ ⲧы ⲉⳝⲁⲏⲏⲁя) υⲇυ ⳝⲁⲏⲁⲏы ⲃⲟⲣⲩύ,ⲯυⲃⲟⲧⲏⲟⲉ ⲧы ⲭⲩⲉⲥⲟⲥⲏⲟⲉ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲕⲁⲯυ ⲟⲇⲏⲟ,ⲏⲁⲭⲩύ ⲧы ⲟⲧⲥⲟⲥⲁⲗⲁ ⲙⲟύ ⲭⲩύ, υ ⲏⲁⳡⲁⲗⲁ ⲡⲉⲣⲉⲇ ⲏυⲙ ⲙⲟⲗυⲧⲃⲩ ⳡυⲧⲁⲧь? ⲧы ⳝⲗяⲧь ⲥⲟⲃⲥⲉⲙ ⲧⲩⲡⲁя? ⲭⳅⲁⲩⳅⲭⲁⲩⳅⲭⲁⲩⲁⲩⳅ, ⲃ ⲱⲟⲕⲉ ⲥ ⲧⲉⳝя) ⳅⲁⲧⲟ ⲙⲟύ ⲭⲩύ ⲇⲗя ⲧⲉⳝя,ⲕⲁⲕ ⳝⲟⲅ,ⲣⲁⳅ ⲧы ⲙⲟⲗυⲱьⲥя ⲉⲙⲩ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲟⲥⲁⲧь ⳝⲉⲅυ я ⲥⲕⲁⳅⲁⲗ ⲙⲁⲏⲇⲁⲃⲟⲱⲕⲁ ⳝⲗ ⲧы ⲯⲉ ⲡⲟⲥⲗⲩⲱⲏⲁя ⲱⲁⲃⲕⲁ ⲡⲟⲇⲇⲁⲃⲁύⲥя ⲕⲟⲙⲁⲏⲇⲁⲙ))0)0  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲧь ⲉⳝⲉⲧⲥя ⲥ ⲡⲣⲁⲃыⲙυ ⲏⲟ υⳅⲙⲉⲏяⲉⲧ υⲙ ⲥ ⲭⲁⳡⲁⲙυ?)ⲕⲁⲕⲟύ ⲧⲟⲗⲕ ⲃ ⲧⲟⲙ,ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲯⲉⲣⲧⲃⲁ ⲁⲕⲩⲱⲉⲣⲕυ?))  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱ ⲧы ⲧⲩⲡⲁя ⲕⲩⲣⲃⲁ ⲧы ⲃ ⲕⲩⲣⲥⲉ ⳡⲧⲟ ⲙⲉⲏя ⲭⲟⲧяⲧ ⲡⲟⲥⲁⲇυⲧь ⳅⲁ υⳅⲏⲁⲥυⲗⲟⲃⲁⲏυⲉ ⲃⲥⲉύ ⲧⲃⲟⲉύ ⲉⳝⲩⳡⲉύ ⲥⲉⲙⲉύⲕυ)) ⲏⲟ ⲡⲟⳡⲉⲙⲩ-ⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲃ ⲃⲟⲥⲧⲟⲟⲣⲅⲉ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲙⲁⲱⲕⲁ ⲟⲃⲟⳃⲉⲙ ⲥⲧⲁⲗⲁ ⲉё ⲅⲩⳝⲟⳡⲕυ ⲩⲥⲧⲁⲗυ ⲥⲟⲥⲁⲧь ⲁ ⲡⲟⲗⲟⲃыⲉ ⲃⲟⲟⳝⳃⲉ ⲥⲧⲉⲣⲗυⲥь… ⲧⲁⲙ ⲡⲟⲗ ⲙⲟⲥⲕⲃы ⲡⲟⳝыⲃⲁⲗⲟ… ⲏⲉⲣⲩⲥⲥⲕυⲉ ⲃⲥⲉ ⲡⲟⳡⲗⲉⲏⲏⲟ….  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⳝⲩⲇⲩⲗⲁύ ⲩⲧыⲣⳡⲁⲧыύ))ⲩ ⲙⲉⲏя ⲥⲩⲕⲁ ⲥⲡυⲏⲏⲟⲅⲟ ⲙⲟⳅⲅⲁ ⳝⲟⲗьⲱⲉ ⳡⲉⲙ ⲩ ⲧⲉⳝя υ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕυ ⲅⲟⲗⲟⲃⲏⲟⲅⲟ,ⲕⲣⲉⲧυⲏы ⲥⲩⲕⲁ))  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ээ,ⲧы ⲏⲉ ⲡⲉⲧⲩⲱυⲥь,ⲧы ⲯ ⲟⲥёⲗ ⲥⲕⲁ ⲧⲩⲡⲉⲏьⲕυύ ⲡυⳅⲇⲉц)) ⲃⲟⲧ ⲡⲟэⲧⲟⲙⲩ ⲧⲉⳝя ⲃⲥⲉ ⲏⲁ ⲥⲉⲕⲥ ⲣⲁⳅⲃⲟⲇяⲧ υ ⲧⲃⲟύ ⲣⲟⲧ ⲧⲁⲕ ⲣⲁⲥⲱυⲣυⲗⲥя ⲟⲧ ⲕⲟⲗ-ⲃⲁ ⲭⲩⲉⲃ ⲕⲟⲧⲟ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⳡⲉⲣⲉⳅ ⲧⲉⲣⲏυυ ⲕ ⳅⲃⲉⲇⳅⲇⲁⲙ – ⲧⲁⲕ ⲇⲟⳝυⲃⲁюⲧⲥя цⲉⲗυ ⲏⲟⲣⲙⲁⲗьⲏыⲉ ⲗюⲇυ ⲏⲟ ⲏⲉ ⲧы) ⲧⲃⲟύ ⲥⲗⲟⲅⲁⲏ – ⲥⲟⲥⲁⲗ υ ⳝⲩⲇⲩ ⲥⲟⲥⲁⲧь)) ⲇⲁ ⲃы ⲃⲥⲉ ⲥⲟⲥⲩⲏⲕυ ⲩⲣⲟⲇы  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ я ⲧⲟⲧ ⲥⲁⲙыύ ⲡⲁⲣⲉⲏⲉⲕ,ⳡⲗⲉⲏ ⲕⲟⲧⲟⲣⲟⲅⲟ ⲥⲩⲯⲇⲉⲏⲟ ⳝыⲗⲟ ⲧⲉⳝⲉ ⲃⳅяⲧь ⲃ ⲣⲟⲧ?) ⲏⲩ ⲧⲁⲕ ⲧⲉⲡⲉⲣь ⳅⲏⲁύ)) ⲧы ⲏⲉ ⲯⲉⲣⲧⲃⲁ ⲙⲟⲉⲅⲟ ⲭⲩя)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱь,ⳡⲩⲣⲟⲕⲟⳝⲉⲥⲥ ⲉⳝⲁⲏыύ,ⲧы ⲡⲟⲏυⲙⲁⲉⲱь,ⳡⲧⲟ я ⳃⲁⲥ ⲡⲟⲗⳝⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⳝⲩⲇⲩ ⲭⲩяⲣυⲧь?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲟⲏυ,ⲕⲧⲟ ⲟⲏυ?)ⲧⲉ,ⲕⲟⲧⲟⲣыⲉ ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗυ,ⲃⲣⲉⲙя 20:56:14 ⲡⲟⲣⲁ υⲇⲧυ ⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲧь  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲧь,ⲡⲣυ ⲡⲟⲙⲟⳃυ ⲙⲟⲉⲅⲟ ⲭⲩя,ⲥⲉⳝⲉ ⳅⲩⳝы ⳡυⲥⲧυⲧ ?? ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟ ⲙⲟυⲙ ⲫⲣⲁⳅⲁⲙ ⲕⲁⲕ ⳝⲗⲟⲭⲁ ⲡⲟ яύцⲁⲙ ⲕⲟⲧⲁⲉⲱьⲥя!  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⳅⲁⳡⲉⲭⲗυⲗ ⲧⲃⲟύ ⲣⲟⲧ,ⳡⲧⲟⳝ ⲕⲣⲟⲙⲉ ⲙⲉⲏя ⲏυⲕⲧⲟ ⲏⲉ ⲉⳝⲁⲗ )  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲣⲉⲇυ ⳡⲩⲣⲟⲕ ⲧы ⲥⲃⲟύ, ⲧы ⲣⲁⳝⲟⲧⲁⲉⲱь ⲏⲁ ⲣыⲏⲕⲉ ⲇⲃⲟⲣⲏυⲕⲟⲙ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲩ ⲧы ⳡⲟ ⲥⲕⲗυⲡυⳅⲇⲉⲏь ⲇⲃⲩⲯⲟⲡⲁⲥⲧⲃⲟⲣⳡⲁⲧыύ , ⲥⲉⲙυⲟⲅⲟⲗⲟⲃыύ ⲃⲟⲥьⲙυⲭⲩύ ⲥ ⳡⲉⲧыⲣьⲙя ⲡυⳅⲇⲟⲡⲣⲟёⳝυⲏⲁⲙυ , ⲡυⲇⲁⲣυⲥⲧυⳡⲉⲥⲕυύ ⲙⲩⲇⲁⳝⲗяⲇυⲏ , ⲧⲣⲟⲉⲡυⳅⲇⲁⲕⲗяⲧыύ ⲙⲁⲇⲁⲡⲣⲁёⳝ , ⲏⲉⲃьⲉⳝⲉⲏⲏыύ ⲭⲩⲉⳝⲗяⲧⲥⲕυύ ⲟⲏⲁⲏюⲅⲁ !!!!  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⳡⲟ ⲧⲃⲁⲣь ⲏⲁ ⲙⲉⲏя ⲇⲁ? ⳃⲁⲥ я ⲧⲉⳝⲉ ⲩⲥⲧⲣⲟю ⲥⲩⳡⲕⲁ, ⲙⲟⲉ υⲙя ⲧⲟⲗьⲕⲟ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⳝⲩⲇⲉⲱь ⲏⲁⳅыⲃⲁⲧь ⲧⲃⲁⲣь ⳝⲗяⲧь  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟύ ⲣⲟⲧ ⲏⲁ ⲥⲧⲁⲇυυ ⲅⲗⲟⲧⲁⲏυя ⲥⲡⲉⲣⲙы?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟю ⲙⲁⲧь ⲡⲉⲣⲃыύ ⲃыⲉⳝⲁⲗ, ⲧⲉⳝⲉ ⲇⲟ ⲙⲟⲉύ ⲙⲁⲧⲉⲣυ ⲉⳃё ⲩ ⲙⲉⲏя ⲃⳡⲉⲣⲁ ⲏⲉ ⲇⲟⲥⲟⲥⲁⲗ, ⲧⲁⲕ-ⳡⲧⲟ ⳝыⲥⲧⲣⲟ ⲡⲟⲇⲡⲟⲗⳅ ⲥⲃⲟυⲙ ⲣⲧⲟⲙ υ ⲏⲁⳡⲁⲗ ⲥⲟⲥⲁⲧь, ⲁ ⲧⲟ ⲙⲟύ ⲭⲩύ ⳅⲁⲕⲟⲡⲁⲉⲧ υ ⲏⲉ ⲡⲣⲟⲥⲧυⲧ, ⲡⲟⲥⲗⲉ ⳡⲉⲅⲟ, ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ, ⳝⲩⲇⲉⲧ ⲟⲫυцυⲁⲗьⲏⲟ ⲃыⲉⳝⲁⲏⲟ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⳡⲧⲟ ⲧы ⲧⲁⲕⲟύ ⲅⲣⲩⲥⲧⲏыύ?)ⲭⲩύ ⲥⲟⲥⲁⲗ ⲧы ⲏⲉ ⲃⲕⲩⲥⲏыύ?)) ⲇⲁ ⳝⲗя я ⲯⲉ ⲧⲟⲕ ⲙⲁⲙⲁⲱⲩ ⲧⲃⲟю ⲧⲣⲁⲭⲁⲗ ⲁ ⲡⲟⲧⲟⲙ ⲩⲯⲉ ⲃⲁⲫⲗυⲗ ⲧⲃⲟύ ⲣⲟⲧ.. ⳅⲏⲁⳡυⲧ ⲟⲏⲁ ⲏⲁ ⲥⲁⲙⲟⲙ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲟⲙⲏυⲱь ⲕⲁⲕ ⲧы ⲕⲟ ⲙⲏⲉ ⲃ ⲥⲟⳡυ ⲡⲣυⲉⲭⲁⲗⲁ,ⲁ я ⲧⲉⳝⲉ ⲩⲥⲧⲣⲟυⲗ эⲕⲥⲕⲩⲣⲥυю ⲏⲁ ⲥⲃⲟⲉⲙ ⲭⲩⲉ) ⲙы ⲡⲟⳝыⲃⲁⲗυ ⲏⲁ ⲙⲟⲣⲉ) ⲧы ⲏⲁ ⲏⲉⲙ,ⲕⲁⲕ ⲏⲁ ⲥⲉⲣⲫυⲏⲅⲉ ⲡⲗⲁⲃⲁ) ⲙы ⲡⲟⳝыⲃⲁⲗυ ⲩ ⲙⲉⲏя ⲃ ⲕⲟⲙⲏⲁⲧⲉ) ⲧы ⲙⲏⲉ ⲡⲟⲕⲁⳅыⲃⲁⲗⲁ ⳡⲩⲇⲉⲥⲁ ⲥⲃⲟⲉⲅⲟ ⲣⲧⲁ) ⲕⲣⲩⲧⲟ ⲯⲉ ⳝыⲗⲟ) ⲏⲁⲇⲟ ⳝⲩⲇⲉⲧ ⲡⲟⲃⲧⲟⲣυⲧь)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲉⳝя ⳅⲟⲃⲩⲧ ⲭⲩⲉⲥⲟⲥ,υ ⲧы ⲕⲁⲯⲇыύ ⲇⲉⲏ ⲥⲟⲥⲉⲱь ⲭⲩυ ??  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙы ⲥ ⲧⲃⲟυⲙ ⲡⲁⲡⲁⲱⲉύ ⲃⲥⲉ ⲟⳝⲥⲩⲯⲇⲁⲗⲉ ⲕⲁⲕ ⳝы ⲥⲩⲏⲩⲧь ⳡⲗⲉⲏ ⲕ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕⲉ ⲯυⲣⲏⲟύ ⳡⲧⲟⳝы ⲣⲟⲇυⲧь ⲩⲣⲟⲇυⲏⲩ ⲕⲁⲕ ⲧы)ⲥⲗⲁⲃⲁ ⳝⲟⲅⲩ ⲩ ⲏⲁⲥ ⲃⲥⲉ ⲡⲟⲗⲩⳡυⲗⲟⲥь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡυⲇⲟⲣ ⲁⳝⲟⲥⲥⲁⲏыύ), ⲃⲟⲧ ⳅⲁⳡⲉⲙ ⲧы ⲏⲁ ⲥⲃⲟю ⲙⲁⲧь ⲏⲁⲥⲥⲁⲗ, ⲕⲟⲅⲇⲁ ⲙы ⲉⲉ ⲃⲥⲧⲣⲉⲧυⲗυ) я ⲡⲟⲏυⲙⲁю ⳡⲧⲟ ⲩ ⲧⲉⳝя ⲣⲉⲫⲗⲉⲕⲥы ⲥⲟⳝⲁⲕυ, ⲏⲟ ⲧⲃⲟя ⲙⲁⲧь ⲯⲉ ⲏⲉ ⲇⲉⲣⲉⲃⲟ) ⲇⲁⲯⲉ ⲏⲉ ⳝⲣⲉⲃⲏⲟ) ⲃ ⲡⲟⲥⲧⲉⲗυ ⲟⲏⲁ ⲭⲟⲣⲟⲱⲁ)-ⲟⲧⲡυⲱυⲥь ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲃⲃⲟⲇυⲗ ⲥⲃⲟю ⲕⲟⲏⳡⲩ ⲃ ⲃⲉⲏы ⲧⲃⲟⲉύ ⲙⲁⲙы) ⲕⲟⲅⲇⲁ ⲟⲏⲁ ⳝⲟⲗⲉⲗⲁ ⲅⲣυⲡⲡⲟⲙ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⳡⲉⲙⲩ ⲧы ⲡьⲉⲱь ⲙⲟю ⲕⲟⲏⳡⲩ ⲡⲟ ⲩⲧⲣⲁⲙ ⳅⲁⲗⲡⲟⲙ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲥⲩⲕⲁ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⲗⲉⲯυⲱь ⲕⲁⲕ ⲏⲁ ⲡⲗяⲯⲉ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲃ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙы ⲙⲟⲯⲏⲟ ⲡⲟⲥⲧⲁⲃυⲧь ⲕⲟⲗⲟⲏⲕυ υ ⳝⲩⲇⲉⲧ ⲡυⳅⲇⲁⲧⲁя ⲃυⳝⲣⲁцυя ⲡⲟ ⲕⲗυⲧⲟⲣⲩ ⲧⲃⲟⲉύ ⲙⲁⲙы,ⲟⲏⲁ ⲁⲯ ⲕⲟⲏⳡυⲧ ⲏⲉ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩ,ⲁ ⲟⲧ ⲃυⳝⲣⲁцυυ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲧь ⲗюⳝυⲧ ⲕⲟⲅⲇⲁ ⲙⲟύ ⲭⲩύ υⲅⲣⲁⲉⲧ ⲥ ⲏⲉύ ⲃ ⲥⲁⲇⲟ-ⲙⲁⳅⲟ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲧь ⲕⲟⲅⲇⲁ ⲡⲟⲕⲩⲣυⲗⲁ ⲙⲟυⲙ ⲭⲩⲉⲙ,ⲧⲟ ⲉύ ⲥⲧⲁⲗⲟ ⲗⲉⲅⳡⲉ ⲏⲁ ⲇⲩⲱⲉ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲥⲩⲕⲁ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⲃыⲉⳝⲩⲉⲱьⲥя,ⲁ ⲡⲟⲧⲟⲙ ⲥ ⲏⲉⲅⲟ ⲏⲉ ⲭⲟⳡⲉⲱь ⲥⲗⲉⳅⲁⲧь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲧь ⲥυⲇυⲧ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ ⲕⲁⲕ ⲏⲁ ⲧⲣⲟⲏⲉ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱь ⳃⲁⲃⲉⲗь ⲏⲁⲭⲩύ?) ⲧы ⲭⲩⲗυ ⲕⲟ ⲙⲏⲉ ⲇⲁⲃⲁⲗ ⲥⲃⲟю ⲙⲁⲧь ⲃыⲉⳝⲁⲧь ⳅⲁ ⳝⲩⲕⲉⲧ цⲃⲉⲧⲟⲃ ⲧⲟ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲧь ⲣⲁⳝⲟⲧⲁⲉⲧ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩⲉ) ⲕⲁⲕ ⲥⲉⲕⲣⲉⲧⲏыύ ⲁⲅⲉⲏⲧ ⲙⲟⲉⲅⲟ ⲭⲩя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲕⲁⲯⲇыύ ⲣⲁⳅ ⲕⲟⲅⲇⲁ ⲏⲁ ⲩⲗυцⲉ υⲇⲉⲧ ⲇⲟⲯⲇь, ⲧⲃⲟя ⲙⲁⲧь ⲡⲣяⳡⲉⲧⲥя ⲡⲟⲇ ⲙⲟυⲙ ⲭⲩⲉⲙ. ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ, ⲥⲗⲉⲇⲟⲃⲁⲧⲉⲗьⲏⲟ я ⲏⲉ ⲡυⲇⲟⲣ. ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲕⲁⲣⲧⲁⲃыύ ⲡυⲇⲟⲣ, ⲥⲟⲥυ ⲙⲟύ ⲭⲩύ. ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲧⲃⲟύ ⲇⲟⲙ - ⲡⲟⲙⲟύⲕⲁ, я ⳡⲁⲥⲧⲟ ⲃыⲏⲟⲱⲩ ⲧⲩⲇⲁ ⲙⲩⲥⲟⲣ. ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Я ⲧⲃⲟύ ⲟⲧⳡυⲙ. ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲁⲭⲁⲭⲁⲭⲁⲭⲁⲭⲭⲃⲃⲭⲁⲭⲭⲃэⲃэⲁэⲁэⲁⲭⲁⲭⲁⲭⲭⲁⲭⲁⲭⲁⲭⲃⲭⲁⲭⲁⲭⲁэⲁⲭⲭⲁⲭⲁⲭⲁⲭⲁⲭⲁⲭⲁⲭⲁⲭⲁⲭⲁⲯⲁⲭⲁэⲭⲁⲁэⲃⲭⲃⲭⲁⲭⲁⲭⲃⲭⲁⲭⲃⲭⲃⲭⲁⲭⲁⲭⲁⲭⲁⳅⲁⳅⲁⲭⲁⲃⳅⲁⳅⲁⲁⳅⲁⳅⲃⲭⲭⲁⲭⲁⲭⲁⲁ,я ⲏⲉ ⲡⲟⲏяⲗ,ⲧы ⳅⲁⳡⲉⲙ ⲥⲃⲟυⲙ яⳅыⲕⲟⲙ ⲙⲟю ⳅⲁⲗⲩⲡⲩ ⳃⲉⲕⲟⳡυⲱь?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ,ⲃⲥⲉⲭ ⲙⲟⲏⲇⲟⲃⲟⲱⲉⲕ ⲩⳝυⲗ,ⳅⲏⲁⲉⲱь ⲕⲁⲕ?)ⲟⲧⲕⲣыⲗ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ,ⲥⲃⲟυⲙ ⲭⲩⲉⲙ,υ ⳝⲣыⳅⲏⲩⲗ ⲧⲩⲇⲁ"ⲁⲏⲁⲗьⲏыύ ⲇυⲭⲗⲟⲫⲟⳅ" ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲥⲡⲁⲥυ ⲩⲯⲉ ⲙⲟύ ⲭⲩύ ⲥⲃⲟⲉύ ⲡυⳅⲇⲟύ ⲟⲧ эⲧυⲭ ⲡυⳅⲇⲟⲥⲧⲣⲁⲇⲁⲏυύ... ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⳅⲗⲟⲉⳝⲩⳡⲁя ⲙⲁⲏⲇⲁ, я ⲥⲉύⳡⲁⲥ ⲁⲏⲧⲉⲏⲏⲩ ⲃ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲃⲥⲧⲁⲃⲗю, ⲙⲟύ ⲧⲉⲗⲉⲃυⳅⲟⲣ ⲏⲁⳡⲏёⲧ 250 ⲕⲁⲏⲁⲗⲟⲃ ⲗⲟⲃυⲧь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲭⲟⳡⲩ ⲥⲣⲟⳡⲏⲟ ⲟⳝⲥⲩⲇυⲧь ⲥⲡυⲇⲟⳅⲏыύ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ. Ⳡⲧⲟ ⲥ ⲏυⲙ? ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲏⲁⲭⲩя ⲧы ⲏⲁ ⲙⲟⲣⲟⳅⲉ ⲙⲟύ ⲭⲩύ ⲅⲣⲉⲉⲱь, ⲙⲁⲧⲉⲣυⲏⲥⲕυⲉ ⳡⲩⲃⲥⲧⲃⲁ ⲡⲟяⲃυⲗυⲥь?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲟⳝⲗυⲯυ ⲙⲏⲉ ⲟⳝⲩⲃь. ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲙⲁⲙⲕⲩ ⲥюⲇⲁ ⲥⲃⲟю ⲡⲣυⲅⲗⲁⲥυ, я ⲉё ⲭⲩⲉⲥⲟⲥυⲧь ⳝⲩⲇⲩ. ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲧⲃⲟя ⲙⲁⲧь ⲡυⳅⲇⲟⲡⲣⲟёⳝυⲏⲁ ⲇⲣыⳃⲁя, ⲩⲡⲁⲃⲱⲁя ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⲏⲁ ⲡⲗⲁⲏⲉⲧⲩ Ⳅⲉⲙⲗя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲧⲃⲟя ⲙⲁⲧь ⲙⲟύ ⲭⲩύ ⲥⲟⲥⲉⲧ ⳡⲁⳃⲉ ⳡⲉⲙ ⲧы ⲡⲣⲉⲃⲣⲁⳃⲁⲉⲱь ⲕυⲥⲗⲟⲣⲟⲇ ⲃ ⲩⲅⲗⲉⲕυⲥⲗыύ ⲅⲁⳅ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲡⲟ ⳝⲣⲟⲃяⲙ ⲡⲣⲟⲃⲉⲗ ⲟⲏυ ⲩ ⲏⲉⲉ ⲡⲟⳝⲉⲗⲉⲗυ ⲟⲧ ⲏⲁⲗυⳡυя ⲙⲟⲉύ ⲥⲡⲉⲣⲙы) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲏⲟⳡь Ⳙⲃⲁⲏⲁ Ⲕⲩⲡⲁⲗы ⲏⲁ ⲙⲟύ ⲭⲩύ υⲇⲉⲧ ⲕⲁⲕ ⲗⲉⲇяⲏⲩю ⲡⲣⲟⲣⲩⳝь)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⳙⲇυ ⲏⲁⲭⲩύ ⲗⲟⲱⲟⲕ ⲥ ⲅⲁⲏⲅⲣⲉⲏⲟύ ⲅⲉⲏυⲧⲁⲗυύ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲧⲃⲟя ⲙⲁⲧь ⲇⲁⲯⲉ ⲥⲟⲥⲉⲧ υ ⲏⲉ ⲡⲟⲙⲏυⲧ, ⳡⲧⲟ я ⲉⲉ ⲉⳝⲁⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲡⲟⲥⲙⲟⲧⲣυ ⲃ ⲟⲕⲏⲟ υ ⲩⲃυⲇь ⲥⲃⲟю ⲙⲁⲧь ⲃ ⳅⲟⲏⲉ ⲇⲉύⲥⲧⲃυя ⲙⲟⲉⲅⲟ ⲭⲩя, ⲟⲗⲩⲭ ⲧы ⳝⲗяⲇь ёⳝⲁⲏⲏыύ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡⲗⲁцⲉⲏⲧⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⲥⲧяⲏⲩ ⲕⲁⲕ ⲥⲕⲁⲧⲉⲣⲧь ⲏⲁ ⲥⲧⲟⲗⲉ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲙⲟύ ⲭⲩύ ⲡⲟⲇⲇⲉⲣⲯυⲃⲁⲉⲧ ⲥⲉⲣⲇцⲉⳝυⲉⲏυⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟύ ёⳝⲁⲣь υ ⲃⲉⲣⲭⲟⲃⲏыύ ⲭⲟⳅяυⲏ, ⲥⲟⲥυ ёⳝⲁⲏⲏыύ ⲣⲁⳝ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲁ ⲉⳃⲉ ⲧⲃⲟя ⲙⲁⲧь ⲙⲟύ ⲭⲩύ ⲥⲟⲥⲁⲗⲁ ⲡⲟⲗ ⲅⲟⲇⲁ, ⲏⲁⲭⲟⲇяⲥь ⲃ ⲥⲡяⳡⲕⲉ ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲇⲁⲃⲁύ ⲥⲟⲥυ υ ⲏⲉ ⲟⲥⲧⲁⲏⲁⲃⲗυⲃⲁύⲥя, ⲧⲩⲡⲟύ ⲟⲡⲉⳅⲇⲁⲗ ⲥ ⲏⲁⲗυⳡυⲉⲙ ⲇыⲣы ⲃ ⲙⲟⳅⲅⲉ ⳅⲁⲡⲟⲗⲏⲉⲏⲏⲟύ ⲭⲩⲉⲙ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲇⲁ ⲧы ⲡⲣⲟⲥⲧⲟ ⲟⲗⲩⲭ ёⳝⲁⲏⲏыύ ⲧⲁⲕⲟύ ⲯⲉ ⲕⲁⲕ υ Ⲏυⲕⲉⲗь ⲧⲟⲯⲉ ⲥⲟⲥⲉⲱь ⲭⲩύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲏⲁ ⲅⲟⲗⲟⲃⲩ ⲃⲟⲗⲟⲥы ⲃⳅъⲉⲣⲟⲱυⲗ, ⲁ ⲧы ⲇⲁⲯⲉ ⲏⲉ ⲡⲟⲧⲣⲩⲇυⲗⲥя υⲭ ⲩⲗⲟⲯυⲧь, ⲃⲟⲧ ⲧⲁⲕⲟύ ⲧы ⳅⲁⳝⲟⲧⲗυⲃыύ ⲥыⲏ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲕⲁⲕ υⲅⲗⲟύ ⲕⲣⲉⲥⲧυⲕυ ⲃыⲱυⲃⲁⲗ, ⲃⲙⲉⲥⲧⲟ ⲏυⲧⲉύ ⲙⲟя ⲥⲡⲉⲣⲙⲁ ⳝыⲗⲁ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲕⲥⲧⲁⲧυ, ⲥⲟⲥυ ⲙⲟύ ⲭⲩύ ⲗⲟⲱⲟⲕ ⲡⲣⲟёⳝⲁⲏⲏыύ ⲅⲟⲇⲁⲙυ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲧⲁⳃⲩⲥь ⲟⲧ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧⲁⲕⲁя ⲱⲗюⲭⲁ эⲧⲟ ⲡυⳅⲇⲉц)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Я ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲅⲏυⲗь ⲩⳝυⲣⲁⲗ ⲕⲁⲕ ⳝⲩⲇⲧⲟ ⲡⲣⲟⲃⲟⲇυⲗ ⲇⲉⳅⲉⲏⲫⲉⲕцυю ⲃ ⲟⳝⳃⲉⲥⲧⲃⲉⲏⲏⲟⲙ ⲧⲩⲁⲗⲉⲧⲉ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲡⲣυ ⲕⲁⲯⲇⲟⲙ ⲧⲃⲟё ⲙⲟⲣⲅⲁⲏυυ я ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲧь ⲥⲧⲁⲏь ⳅⲣяⳡυⲙ ⲡυⲇⲁⲣⲟⲙ ⳡⲧⲟⳝы ⲩⳝⲣⲁⲧь эⲧⲩ ⳅⲁⲕⲟⲏⲟⲙⲉⲣⲏⲟⲥⲧь)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Я ⲉⲇⲩ ⲏⲁ ⲙⲟⲣⲉ, ⲁ ⲧⲃⲟя ⲙⲁⲧь ⲉⲇⲉⲧ ⲏⲁ ⲙⲟύ ⲭⲩύ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Я ⲧⲉⳝⲉ ⲏⲁ ⳅⲁⲃⲧⲣⲁⲕ яύцⲉⲕⲗⲉⲧⲕⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲡⲟⲯⲁⲣⲉⲏⲏⲟⲙ ⲃυⲇⲉ ⲡⲟⲇⲁⲙ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲡⲟⲙⲏю ⲧⲃⲟύ ⲟⲧⲉц ⲭⲩⲗυⲅⲁⲏ ⲕⲟⲏⳡυⲗ ⲃ яύцⲟ υ ⲣⲟⲇυⲗⲥя ⲧы)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲏⲁⲇ ⲧⲟⳝⲟύ ⲃⲥⲉ ⲥⲙⲉюⲧⲥя ⲃ ⲱⲕⲟⲗⲉ ⲡⲟⲧⲟⲙⲩ ⳡⲧⲟ ⲧы ⲟⲧⲥⲟⲥⲁⲗ ⲭⲩύ ⲃ ⲟⳝⳃⲉⲥⲧⲃⲉⲏⲏⲟⲙ ⲙⲉⲥⲧⲉ ⲏⲁ ⲅⲗⲁⳅⲁⲭ ⲇυⲣⲉⲕⲧⲟⲣⲁ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⳝⲩⲇь ⳝⲟⲅⲁⲧыⲣёⲙ, ⲥⲇⲃυⲏь ⲙⲟύ ⲭⲩύ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ  ⲕⲗυⲧⲟⲣ ⲣⲁⲥⲧяⲏⲩⲗ ⲕⲁⲕ υⳅⲅⲟⲣⲟⲇь ⲟⳝⲟⲣⲟⲏυⲧⲉⲗьⲏⲩю ⲧⲉⲡⲉⲣь ⲙⲟⲯⲏⲟ υ ⲟⲧ ⲧⲃⲟⲉⲅⲟ ⲣⲧⲁ ⳅⲁⳃυⳃⲁⲧьⲥя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳Ⲕⲥⲧⲁⲧυ, ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲃ ⲟⳡⲕⲟ υ ⲏⲉⳡⲁяⲏⲏⲟ ⲕⲟⲏⳡυⲗ ⲥⲡⲩⲥⲧя 9 ⲙⲉⲥяцⲉⲃ ⲡⲟяⲃυⲗⲟⲥь ⲡⲟⲥⲗⲉⲇⲥⲧⲃυⲉ ⲙⲟⲉύ ⲟⲱυⳝⲕυ, ⲧⲟ ⲉⲥⲧь ⲧы! ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲣυⲕⲟⲗ, я ⲏⲁⲱёⲗ ⲥⲟⲃⲡⲁⲇⲉⲏυⲉ ⲩ ⲧⲉⳝя υ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲃы ⲟⳝⲁ ⳅⲩⳝы ⲏⲉ ⳡυⲥⲧυⲧⲉ, я ⲕⲟⲅⲇⲁ ⲃⲁⲥ ⲏⲁ ⲣⲟⲧ ⲉⳝⲁⲗ, ⳅⲁⲙⲉⲧυⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡυⳅⲇⲉц, ⲉⲥⲗυ ⲧⲃⲟю ⲙⲁⲧь ⲃыⲉⳝⲁⲧь ⲟⲏⲁ ⲡⲣⲉⲃⲣⲁⲧυⲧⲥя ⲃ ⲕⲣⲁⲥⲁⲃυцⲩ? ) эⲧⲟ ⲧⲁⲕ,ⲡⲣⲟⲥⲧⲟ ⲃⲟⲡⲣⲟⲥ,ⳡⲧⲟⳝ ⲏⲁⲃⲉⲣⲏяⲕⲁ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲧь, ⲃⲟⲧ я ⲧⲁⲕⲟύ ⳡⲉⲗⲟⲃⲉⲕ ⲥⲧⲣⲁⲏⲏыύ, ⲙⲟⲅⲩ ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲧь ⲗⲉⲧ 20, ⲇⲁⲯⲉ ⳝⲟⲗьⲱⲉ ⲉё ⲩⲯⲉ ⲉⳝⲩ, ⲡⲣⲟⲥⲧⲟ ⳝⲣⲁⲕ,я ⲧⲉⳝⲉ ⲟⲧⳡυⲙ ⲃⲥⲉ ⲯⲉ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲕⲟⲅⲇⲁ ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲃ ⲣⲟⲧ ⳅⲁⲙⲉⲧυⲗ, ⳡⲧⲟ ⲩ ⲏⲉⲉ ⲣⲁⲕ ⲅⲩⳝы,я ⲏυⲕⲟⲅⲇⲁ ⲏⲉ ⳅⲁⳝⲩⲇⲩ эⲧⲩ ⲣⲁⲕⲟⲃⲩю ⲯⲉⲏⳃυⲏⲩ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲧь ⲡυⳅⲇⲉц ⲇⲩⲣⲁ, ⲟⲇⲉⲗⲁⲥь, ⲕⲁⲕ ⲕυⲣⲕⲟⲣⲟⲃ, υ ⳝⲉⲯⲁⲗⲁ ⲃⲥⲉⲙ ⲥⲟⲥⲁⲧь ⲥⲟ ⲥⲗⲟⲃⲁⲙυ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⳝью ⲯⲉⲏⳃυⲏ υ ⲙⲏⲉ ⲡⲟⲭⲩύ ⲏⲁ ⲧⲃⲟю ⲙⲁⲧь !!!  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⳝⲉⲅυ ⳝыⲥⲧⲣⲉⲉ, ⲧⲃⲟя ⲙⲁⲧь ⲁⲃⲁⲏⲥ ⲃ ⳝⲁⲣⲇⲉⲗⲉ ⲡⲟⲗⲩⳡυⲗⲁ, ⲱⲟⲕⲟⲗⲁⲇⲕⲩ ⲧⲉⳝⲉ ⲕⲩⲡυⲗⲁ, ⲕⲩⲱⲁύ, ⲏⲉ ⲡⲟⲇⲁⲃυⲥь ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲟⲇυⲏ ⲣⲁⳅ ⲱёⲗ ⲏⲁ ⲁⲃⲁⲏⲧюⲣⲩ, ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⳝⲉⳅ ⲅⲁⲏⲇⲟⲏⲁ, ⲇⲉⲗⲟ ⲡⲣⲟⲱⲗⲟ ⲩⲇⲁⳡⲏⲟ, ⳝⲉⲣⲉⲙⲉⲏⲏⲟⲥⲧυ ⲏⲉ ⳝыⲗⲟ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲫⲩⲭ, ⲏⲁ ⲥⲃⲟύ ⲥⲧⲣⲁⲭ υ ⲣυⲥⲕ ⲉⳝⲁⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲃⲟⲥьⲙⲟⲉ ⲁⲃⲅⲩⲥⲧⲁ 2014 ⲅ,ⲥⲡⲣⲟⲥυ ⲩ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕυ, ⳡⲧⲟ ⳝыⲗⲟ ⲃ ⲧⲟⲧ ⲇⲉⲏь, ⲁ ⲟⲏⲁ ⲟⲧⲃⲉⲧυⲧ, ⳡⲧⲟ я ⲉⳝⲁⲗ ⲉⲉ) ⲕⲁⲕυⲉ ⲙυⲗⲟⲥⲧυ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡυⳅⲇⲉц, я ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь,ⲕⲟⲏⳡⲁю ⲃ ⲣⲟⲧ ⲉύ,ⲁ ⲟⲏⲁ ⲧⲁⲕⲁя - ⲕⲩⲇⲁ ⳝⲁⲅⲁⲯ? ) ⲁ я ⲧⲁⲕⲟύ, ⲅⲗⲟⲧⲁύ ⲃⲉⲥь ⲅⲣⲩⳅ)ⲟⲏⲁ ⲧⲁⲕⲁя ⲙⲟⲯⲉⲧ ⲏⲁ ⳝⲁⲅⲁⲯⲏυⲕ ⲡⲉⲣⲉⲡⲗюⲏⲩⲧь,ⲁ я ⲧⲁⲕⲟύ -  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ я ⲭⲩⲉⲙ ⲧⲃⲟё ⲉⳝⲁⲗⲟ υⳅⲣυⲥⲩю) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ я ⳃⲁ ⲭⲩⲉⲙ ⲥⲏⲉⲥⲩ ⲕⲣыⲱⲩ ⲥ ⲇⲟⲙⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲃⲕⲩⲣⲥⲉ ⳡⲉύ ⲭⲩύ ⲟⲥⲁⲇυⲗ?) ⲥⲁⲇⲏυⲕ ⲧы ⲥⲩⲕⲁ ⳝⲉⳅ ⲅⲟⲗⲟⲃы, я ⲧⲉⳝя ⲯⲉ ⲭⲩⲉⲙ ⲩⳝью) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲁ ⲏⲩ ⲥюⲇⲁ υⲇυ υⲗυ ⲙⲏⲉ ⲡⲣυⲇⲉⲧⲥя ⲃ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉ, ⲕⲩⲇⲁ ⲧы ⲥⲡⲣяⲧⲁⲗⲥя ⲭⲩύ ⳅⲁⲡυⲭυⲃⲁⲧь υ ⲗⲟⲃυⲧь ⲧⲉⳝя ⲕⲁⲕ ⲣыⳝⲩ ⲏⲁ ⲩⲇⲟⳡⲕⲩ)) ⲱⲕⲁⲧⲩⲗⲕⲁ ⳝⲗяⲧь ⲧы ⲉⳝⲁⲏⲁя)) я ⲯⲉ ⳝⲗяⲧь ⲣⲟⲧⲁⲏ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲥⲕⲣⲩⳡⲩ υ ⳝⲩⲇⲩ υⳅ ⲏⲉⲅⲟ ⲥⲟⲥυⲥⲕυ ⲇⲉⲗⲁⲧь)) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉ ⲏⲁ ⲯⲟⲡⲉ ⲧⲁⲕⲁя ⳅⲇⲟⲣⲟⲃⲁя ⲡⲟⲙυⲇⲟⲣυⲏⲁ ⲉⳝⲁⲧь ⲕⲣⲁⲥⲏⲁя ⲉⳃⲉ ⲇⲟ ⲡυⳅⲇы)) я ⲯⲉ ⳝⲗяⲧь ⲭⲩⲉⲙ ⲉⲉ ⲥⲏⲉⲥⲩ υ ⲥⲟⲇⲉⲣⲯυⲙⲟⲉ ⲧⲉⳝⲉ ⲏⲁ ⲉⳝⲗⲉⲧ ⲃыⳝⲣыⳅⲏυⲧ))) ⲥⲕυⲏⲭⲉⲇ ⲧы ⲉⳝⲁⲏыύ)) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱ?) ⲅⲟⲃⲏⲟⲡⲁⲇυⳃⲉ ⲉⳝⲁⲏⲟⲉ?) ⲙⲏⲉ ⲧⲃⲟύ ⲟⳡⲕⲉⲥⲧⲁⲏ ⲣⲁⳅⲣыⲃⲁⲧь ⲗⲉⲅⳡⲉ ⳡⲉⲧ ⲏⲉ ⲡⲟⲏяⲗ ⲏυⲭⲩя я ⲯⲉ ⳝⲗяⲧь ⲧⲉⳝя ⲏⲁ ⲥⲃⲟύ ⲭⲩύ ⲏⲁⲧяⲅυⲃⲁю ⲡⲣяⲙⲟ ⲕⲁⲕ ⲏⲟⲥⲕυ ⲏⲁ ⲥⲧⲟⲡы ⲉⳝⲁⲧь ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲣⲁⲭⲧыⲏⳝыⲭ ⲉⳝⲁⲏыύ ⲧы ⲅⲇⲉ ⲧⲁⲙ ⳝⲗяⲧь ⲡⲣяⳡⲉⲱьⲥя?) ⲙⲏⲉ ⲧⲉⳝя ⲡⲟ ⲧⲉⲙⲏыⲙ ⲡⲉⲣⲉⲩⲗⲕⲁⲙ ⲇⲗя ⲟⲧⲥⲟⲥⲁ ⲭⲩя υⲥⲕⲁⲧь ⲏⲁⲇⲟ υⲗυ ⳡⲧⲟ?)) я ⲧⲃⲟю ⲙⲁⲧь ⲧⲁⲕⲯⲉ ⲃыⲉⳝⲁⲗ ⲧⲉⲙⲏⲟⲙ ⲡⲉⲣⲉⲩⲗⲕⲉ ⲏⲟ ⲧⲁⲙ ⲕⲁⲙⲉⲣы ⲥⲧⲟяⲗυ υ ⲙⲏⲉ ⲏⲁ ⲭⲩύ ⲡⲣⲉⲗⲉⲡυⲗυ ⲱⲧⲣⲁⲫ )) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲧⲩⲡⲟ ⲡⲁⳡⲕⲁ ⲥυⲅⲁⲣⲉⲧ) ⲧы ⲥⲟⲥⲉⲱь ⲏυⲕⲁⲕ)) ⲁ ⲃⲟⲧ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲥⲟⲃⲥⲉⲙ ⲇⲣⲩⲅⲟⲉ ⲇⲉⲗⲟ ⳝⲗяⲧь) ⲏⲟ ⳝⲉⲇⲁ ⲃ ⲧⲟⲙ ⳡⲧⲟ ⲟⲏⲁ ⲥⲃυⲏья υ ⲟⲏⲁ ⲕⲟⲅⲇⲁ ⲥⲟⲥⲉⲧ ⲭⲣюⲕⲁⲉⲧ ⲁ ⲃⲟⲧ ⲧⲃⲟύ ⲡⲁⲡⲁⲱⲁ ⲅⲟⲣυⲗⲗⲁ ⳝⲗяⲧь ⲉⳝⲁⲏⲁя ⲃⲟⲟⳝⳃⲉ)) ⲟⲏυ ⲧⲉⳝя ⲥⲇⲉⲗⲁⲗυ ⲏⲉ ⳡⲉⲣⲉⳅ ⲡⲟⲗⲟⲃыⲉ ⲟⲣⲅⲁⲏы , ⲁ ⲧⲃⲟ ⲡⲁⲡⲁⲱⲁ ⳅⲁⲗⲉⳅ ⳝⲟⲱⲕⲟύ ⲃ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ υ ⲡⲗюⲏⲩⲗ ⲧⲩⲇⲁ)) ⲥⲗυⳅⲉⲏь ⲧы ⲥⲩⲕⲁ ⲉⳝⲁⲏыύ ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⳝⲩⲇⲩ ⲣⲁⲥⲕⲣⲩⳡυⲃⲁⲧь ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ υ ⲡⲣυⲃяⲯⲩ ⲕ ⲏⲉⲙⲩ ⲉⲉ ⲣⲟⲧⲁⲏ. ⲟⲏ ⲯⲉ ⲥⲩⲕⲁ ⲕⲁⲕ ⲗⲟⲡⲟⲥⲧυ ⳝⲩⲇⲉⲧ ⲕⲣⲩⲧυⲧьⲥя ⲃⲉⲣⲧⲟⲗⲉⲧⲁ υ ⲡⲟⲇⲏυⲙⲁⲧь ⲉⲉ ⲡυⳅⲇⲁⲕ ⲃⲃⲉⲣⲭ ⲧы ⲡⲟⲏυⲙⲁⲉⲱь?) ⲙυⲗⲗυⲁⲣⲇⲉⲣ ⲧы ⲁⲏⲁⲗьⲏыύ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲯⲉ ⳝⲗяⲧь ⲏⲁ ⲧⲃⲟυ ⲭⲟⲭⲗяцⲕυⲉ ⲗⲁⲡⲧυ ⲡⲣυⲕⲗⲉю ⲥⲃⲟύ ⲥⲡⲉⲣⲙⲁⲕ, ⲁ ⲧы ⳝⲩⲇⲉⲱь ⲇⲩⲙⲁⲧь , ⳡⲧⲟ эⲧⲟ ⲥⲩⲡⲉⲣ ⲕⲗⲉύ)) я ⲉⲅⲟ ⲃыⲥⲕⲣⲉⳝ υⳅ ⲡυⳅⲇⲁⲕⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲕⲟⲅⲇⲁ ⲟⲏ ⲡⲣυⲗυⲡ ⲕ ⲉⲉ ⲡυⳅⲇⲉ 3 ⲅⲟⲇⲁ ⲏⲁⳅⲁⲇ ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳝⲗяⲧь?)) ⲧⲣⲩⳝⲟⳡυⲥⲧ ⲧы ⲉⳝⲁⲏыύ ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я эⲧⲟⲅⲟ ⲏⲉ ⳅⲏⲁю ⲃⲉⲇь ⲏⲉ ⲃυⲇⲉⲗ ⲧⲉⳝя, ⲁ ⲉⲥⲗυⳝы ⲩⲃυⲇⲉⲗ, ⲧⲟ ⲧⲣⲁⲭⲏⲩⲗ ⳝы ⲧⲉⳝя ⲃⲟ ⲃⲥⲉ ⲡυⲭⲁⲧⲉⲗьⲏыⲉ υ ⲇыⲭⲁⲧⲉⲗьⲏыⲉ, ⲃⲟ ⲃⲥⲉ ⲥⲩⳃⲉⲥⲧⲃⲩюⳃυⲉ υ ⲏⲉ ⲥⲩⳃⲉⲥⲧⲃⲩюⳃυⲉ, ⲁ ⲧⲉ ⳡⲧⲟ ⲏⲉ ⲥⲩⳃⲉⲥⲧⲃⲩюⲧ ⲡⲣυⲇⲩⲙⲁⲗ ⳝы, υ ⲡⲟⲃⲉⲣь ⲙⲏⲉ ⲅⲏυⲇⲁ ⳅⲁⲧⲣⲁⲭⲁⲏⲏⲟ-ⲩⲣⲟⲇⲗυⲃⲁя ⲧⲉⳝⲉ ⳝы эⲧⲟ ⲡⲟⲏⲣⲁⲃυⲗⲟⲥь  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲩ ⲧⲃⲟⲉύ ⲙⲁⲙы ⲏⲩ ⲡⲣⲟⲥⲧⲟ ⲡυⳅⲇⲉц ⲕⲁⲕⲁя ⳝⲟⲗьⲱⲁя ⲡυⳅⲇⲁ, я ⲧⲩⲇⲁ ⲡⲟⲗⲏⲟⲥⲧью ⲃⲭⲟⲇυⲗ. эⲧⲟ ⲡυⳅⲇⲉц, я ⲕⲁⲣⳡ ⲃⲟⳅⲗⲉ ⲉⲉ ⲡυⳅⲇы ⲕⲟⲃⲣυⲕ ⲡⲟⲗⲟⲯυⲗ, ⳡⲧⲟⳝ ⲏⲟⲅυ ⲃыⲧυⲣⲁⲧь ⳝⲗяⲧь  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲉⳝⲁⲏⲉц, ⲇⲣⲁⲕⲟⲏ ⲧⲣяⲡⲟⳡⲏыύ, ⲗⲟⲭⲟⲇⲣⲟⲙ ⲅⲁⲗυⲙыύ, ⲩёⳝⲟⲕ ⲡυⳅⲇⲗяⲃыύ, ⲕⲟⲏⳡυⲏⲁ ⲉⳝⲁⲏⲁя, ⲩёⳝυⳃⲉ ⲗⲉⲥⲏⲟⲉ. ⲟⲧⲥⲟⲥυ ⲏⲉ ⲏⲁⲅυⳝⲁяⲥь υ ⲡⲟⲇⲙыⲧьⲥя ⲏⲉ ⳅⲁⳝⲩⲇь. ⲏⲉ ⳝⳅⲇυ ⲕⲁⲡⲩⲥⲧυⲏ, ⲃыⲉⳝⲉⲙ ⲟⲧⲡⲩⲥⲧυⲙ.  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲕⲟⲅⲇⲁ ⲧы ⲥⲟⲥⲁⲗ ⲙⲏⲉ ⲭⲩύ ⲏⲁ 10 эⲧⲁⲯⲉ - ⲁ ⲡⲟⲧⲟⲙ я ⲧⲃⲟю ⳝⲁⳝⲩⲱⲕⲩ ⲉⳝⲁⲗ ⲏⲁ ?? -ⲡⲟⲧⲟⲗⲕⲉ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲏыύ ⲣыцⲁⲣь ⲥ ⲡυⳅⲇⲁⲕⲟⲙ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲕⲁⲕ ⲥ ⳃυⲧⲟⲙ ⲏⲁ ⲡⲗⲉⳡⲉ ⲟⲧ ⲏⲁⲡⲁⲇⲉⲏυя ⲙⲟⲉⲅⲟ ⲭⲩя?) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь , ⲧⲟ ⳡⲧⲟ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⳝⲩⲇⲉⲧ υⳅⲙⲉⲏёⲏ ⲙⲟυⲙ ⲭⲩёⲙ , ⲧы ⲡⲟⲏυⲙⲁⲉⲱь , ⲧⲟ ⳡⲧⲟ я ⳝⲩⲇⲩ ⲡⲟ ⲥⲧⲉⲡⲉⲏⲏⲟ ⲉⳝⲁⲧь ⲉё ⲃⲥё ⲥυⲗьⲏⲉⲉ υ ⲥυⲗьⲏⲉⲉ ⳡⲧⲟⳝы ⲟⲏⲁ ⳅⲁⲅυⳝⲁⲗⲁⲥь ⲟⲧ ⲟⲣⲅⲁⳅⲙⲁ , ⲱⲗюⲭⲁ ⲧⲃⲟя ⲙⲁⲧь ⳝⲗя ))) ⲧы ⲕⲁⲕ ⲉⳝⲁⲏⲁя ⲱⲕⲁⲧⲩⲗⲕⲁ ⲭⲣⲁⲏυⲱь ⲙⲟύ ⲭⲩύ ⲩ ⲥⲉⳝя ⲃⲟ ⲣⲧⲩ υ ⲡⲣυ эⲧⲟⲙ ⲥⲟⲥёⲱь ⲙⲏⲉ ⲉⲅⲟ ⲥⲃⲟυⲙ ⲇыⲣяⲃыⲙ яⳅыⳡⲕⲟⲙ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲏыύ ⲣыцⲁⲣь ⲥ ⲡυⳅⲇⲁⲕⲟⲙ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲕⲁⲕ ⲥ ⳃυⲧⲟⲙ ⲏⲁ ⲡⲗⲉⳡⲉ ⲟⲧ ⲏⲁⲡⲁⲇⲉⲏυя ⲙⲟⲉⲅⲟ ⲭⲩя?) ⲕⲟⲣⲟⳡⲉ , ⲧы ⲡⲟⲏυⲙⲁⲉⲱь , ⲧⲟ ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲟⲡⲩⲥⲧυⲗ ⲇⲟ ⲩⲣⲟⲃⲏя ⲙⲟⲉⲅⲟ ⲭⲩя , ⲁ ⲡⲟⲧⲟⲙ ⲡⲟⲃⲉⲥυⲗ ⲉё ⲏⲁ ⲥⲃⲟύ ⲯⲉ ⲭⲩύ υ ⲏⲁⳡⲁⲗ ⲉё ⲱⲃыⲣяⲧь ⲃ ⲣⲁⳅⲏыⲉ ⲥⲧⲟⲣⲟⲏы)) ⲧы ⲩⳃⲉⲣⳝⲏыύ ⲭⲩⲉⲥⲟⲥ ⲟⲇⲟⳝⲣяюⳃυύ ⲙⲟύ ⲭⲩύ ? )) я ⲥⲉύⳡⲁⲥ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲏⲁⲧяⲏⲩ ⲡυⳅⲇⲁⲕ ⲏⲁ ⲥⲁⲙыύ ⲙⲁⲕⲥυⲙⲩⲙ υ ⳅⲁⲥⲧⲁⲃⲗю ⲇⲉⲗⲁⲧь ⲙⲏⲩ ⲙυⲏⲉⲧ )) ⲡⲟⲧⲟⲙ я ⲕⲟⲣⲟⳡⲉ ⲧⲉⳝя ⳅⲁⲥⲧⲁⲃⲗю ⲥⲟⲥⲁⲧь ⲙⲏⲉ ⲭⲩύ ⲕⲁⲕ ⲕⲟⲅⲇⲁ ⲧⲟ ⲁⳝⲁⲙυ ⲙⲏⲉ ⲥⲟⲥⲁⲗ ))  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲕⲩⲇⲣяⲃыύ ⲡⲩⲇⲉⲗь, ⲕⲟⲧⲟⲣⲟⲙⲩ я ⲃ ⲣⲟⲧ ⲏⲁⲥⲥⲁⲗⲧⲃⲟя ⲙⲁⲧь ⲏⲁⳡⲁⲗⲁ ⲭⲃⲁⲧⲁⲧьⲥя ⲏⲁ ⲙⲟύ ⲭⲩύ ⳡⲧⲟ ⳝ я ⲉⲉ ⲥⲡⲁⲥ ⲏⲟ я ⲏⲉ ⲥⲡⲁⲥⲁⲧⲉⲗь ⲙⲁⲗυⳝⲩ υ я ⲉⲉ ⲭⲩⲉⲙ ⲡυⳅⲇⲁⲏⲩⲗ ⲱⲁⲗⲁⲃⲩ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳цⲉⲗⲕⲁ ⲏⲁ ⲙⲟёⲙ ⲭⲩю?))я υⲅⲣⲁю ⲃ ⲣⲉⲥⲧⲗυⲏⲅ ⲥ ⲧⲃⲟⲉύ ⲙⲁⲙⲕⲟύ υ ⲟⲏⲁ ⲥ ⲕⲁⲏⲁⲧⲟⲃ ⲡⲣыⲅⲁⲉⲧ ⲏⲁ ⲙⲟύ ⲭⲩύ))я ⲡⲟⲣⲃⲁⲗ ⲡⲗⲉⲃⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲱⲕⲟⲗьⲏⲟⲙ ⲧⲩⲁⲗⲉⲧⲉ?))ⲃыⲉⳝⲁⲏⲁя ⲃ ⲯⲟⲡⲩ ⲥυⲡⲁⲣⲁⲧυⲥⲕⲁ ⲩⲯⲉ ⳡёⲧⲁ ⲧы ⲏⲁⲭⲩύ ⲥⲗυⲗⲁⲥь )0)ⲕⲟⲅⲇⲁ ⲧы ⲡυⲱⲉⲱь я ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲧь ⲣⲁⲕⲟⲙ ⲧⲁⲕ ⳡⲧⲟ ⲡυⲱυ))ⲁ ⲇⲁ υⲅⲣⲁⲉⲙ ⲃ υⲅⲣⲩ ⲥⲕⲟⲕⲁ ⲥⲗⲟⲃ ⲏⲁⲡυⲱⲉⲱь ⲥⲧⲟⲗьⲕⲟ ⲭⲩёⲃ ⲧы ⲥⲁⲥⲁⲗ ⲩ ⲙⲉⲏя))ⲥⲙⲡⲉⲣⲙⲟⲡⲣυⲉⲙⲏυⲕ ⲙⲟύ)0  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲁⲏⲁⲗьⲏⲁя ⲡⲉⲣⳡⲁⲧⲕⲁ ⲙⲟⲉⲅⲟ ⲭⲩя ⲭⲩⲗυ ⲧы ⲧⲩⲧ ⲧяⲃⲕⲁⲉⲱ υ ⲭⲩύцⲁ ⲙⲟⲉⲅⲟ ⲅⲗⲟⲧⲁⲉⲱ?) ⲡⲟ ⲡυⳅⲇⲁⲕⲩ ⲭⲟⳡⲉⲱь ⲡⲟⲗⲩⳡυⲧь ⳡⲧⲟⲗυ ⲧы ⳅⲏⲁύ ⳡⲧⲟ ⲉⲥⲗυ я ⲧⲉⳝя ⲩⲯⲉ ⲭⲩⲉⲙ ⲡⲟ ⲡυⳅⲇⲁⲕⲩ ⲩⲇⲁⲣю ⲧⲉⳝя ⲩⲯⲉ ⲏⲉ ⲕⲁⲕⲁя ⳝⲟⲗьⲏυцⲁ ⲏⲉ ⲥⲡⲁⲥⲉⲧ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥыⲏ ⲡⲣⲟⲱⲙⲁⲏⲇⲟⲃⲕυ?), ⲥⲗыⲱь,ⲭⲁⲭⲃⲭⲁⲭⲃⲃⲭⲃⲭⲃⲭⲭⲃъⲃъⲃъ, ⲧы ⲥⲩⲕⲁ ⲱⲁⲱⲕⲁ ⲉⳝⲁⲏⲁя, ⲧы ⲡⲟⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ я ⲧⲉⳝя ⲥⲩⲕⲁ ⲭⲩёⲙ, ⲕⲁⲕ ⲕⲟⲏёⲙ ⲡⲟⲅⲗⲟⲧυⲗ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲟⲡⲁⲣыⲱ ⲉⳝⲁⲏыύ,ⲡⲟⳡⲉⲙⲩ я ⲇⲟⲗⲯⲉⲏ ⲥⲧⲣⲟυⲧь ⲧⲉⳝⲉ ⳝⲩⲇⲕⲩ?ⲇⲃⲟⲣⲏяⲅⲁ ⲉⳝⲁⲏⲁя  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲇцⲡ ⳝⲟⲗьⲏⲟύ ⲭⲩⲉⲅⲗⲟⲧ ⲩ ⲏⲁⲥ ⲙⲁⲧь ⲧⲟ ⲥ ⲧⲟⳝⲟύ ⲟⲇⲏⲁ ⲧⲟⲗьⲕⲟ ⲧы ⲣⲟⲇⲏⲟύ ⲁ я ⲡⲣυёⲙⲏыύ ⲡⲟύⲙυ ⲧы эⲧⲟ ⲃыⳝⲗяⲇⲟⲕ ⳝⲗ))0  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳цⲉⲗⲕⲁ ⲏⲁ ⲙⲟёⲙ ⲭⲩю?))я υⲅⲣⲁю ⲃ ⲣⲉⲥⲧⲗυⲏⲅ ⲥ ⲧⲃⲟⲉύ ⲙⲁⲙⲕⲟύ υ ⲟⲏⲁ ⲥ ⲕⲁⲏⲁⲧⲟⲃ ⲡⲣыⲅⲁⲉⲧ ⲏⲁ ⲙⲟύ ⲭⲩύ))я ⲡⲟⲣⲃⲁⲗ ⲡⲗⲉⲃⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲱⲕⲟⲗьⲏⲟⲙ ⲧⲩⲁⲗⲉⲧⲉ?))ⲃыⲉⳝⲁⲏⲁя ⲃ ⲯⲟⲡⲩ ⲥυⲡⲁⲣⲁⲧυⲥⲕⲁ ⲩⲯⲉ ⳡёⲧⲁ ⲧы ⲏⲁⲭⲩύ ⲥⲗυⲗⲁⲥь )0)ⲕⲟⲅⲇⲁ ⲧы ⲡυⲱⲉⲱь я ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲧь ⲣⲁⲕⲟⲙ ⲧⲁⲕ ⳡⲧⲟ ⲡυⲱυ))ⲁ ⲇⲁ υⲅⲣⲁⲉⲙ ⲃ υⲅⲣⲩ ⲥⲕⲟⲕⲁ ⲥⲗⲟⲃ ⲏⲁⲡυⲱⲉⲱь ⲥⲧⲟⲗьⲕⲟ ⲭⲩёⲃ ⲧы ⲥⲁⲥⲁⲗ ⲩ ⲙⲉⲏя))ⲥⲙⲡⲉⲣⲙⲟⲡⲣυⲉⲙⲏυⲕ ⲙⲟύ)0  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱь ⲁⲏⲁⲗьⲏыύ ⲯυⲧⲉⲗь ⲡυⳅⲇы ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ?)ⲧы ⳡⲧⲟ ⳝⲗⲁⲧⲏыⲭ ⲭⲩёⲃ ⲟⳝⲥⲟⲥⲁⲗⲥя?)ⲙⲏⲉ ⳡⲧⲟ ⲟⲅⲗⲩⲱυⲧь ⲧⲉⳝя ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡⲟ ⳝⲟⲱⲕⲉ ⲕⲁⲕ ⲡⲁⲗⲕⲟύ ⳡⲧⲟⳝ ⳝⲟⲱⲕⲟύ ⲧⲣёⲥ ⲙⲁⲙⲕυⲏ ⲃыⲣⲟⲇыⲱь ⲥⲩⲕⲁ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲡⲟⲇⲩⲙⲁⲗⲁ ⳡⲧⲟ ⲟⲏⲁ ⳝⲉⲗⲕⲁ υ ⳅⲁⳝυⲃⲁⲗⲁ ⲃ ⲡυⳅⲇⲩ ⲃⲉⲧⲕυ υ ⲟⲣⲉⲭυ υ ⲧ.ⲇ ⲏⲟ ⲟⲏⲁ ⲇⲩⲙⲁⲗⲁ эⲧⲟ ⲇⲩⲡⲗⲟ?? υ эⲧⲟ ⲕⲥⲧⲁⲧυ ⳝыⲗυ ⲏⲉ ⲃⲉⲧⲕυ υ ⲏⲉ ⲟⲣⲉⲭυ ⲁ ⲙⲟύ ⲥⲡⲉⲣⲙⲁ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲯⲉ ⲧⲉⳝя ⲩⲱⲗⲉⲡⲕⲁ ⲡⲣυⲱυⳝⲩ ⲭⲩⲉⲙ ⲕⲁⲕ ⳝⲁⲱⲏυ-ⳝⲗυⳅⲏⲉцы ⲃ ⲏью-ⲉⲣⲕⲉ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲕⲩ ⲇⲟ ⲗⲉⲇⲏυⲕⲟⲃⲟⲅⲟ ⲡⲉⲣυⲟⲇⲁ ⲉⳃⲉ))  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲕⲩ ⲇⲟ ⲗⲉⲇⲏυⲕⲟⲃⲟⲅⲟ ⲡⲉⲣυⲟⲇⲁ ⲉⳃⲉ))  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲕⲩⲣю ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲁ ⲡⲉⲡⲉⲗ ⲥⲗⲉⲧⲁⲉⲧ ⲃ ⲧⲃⲟύ ⲯⲁⲗⲟⳝⲏⲟ ⲥⲕⲩⲗяⳃυύ ⲣⲟⲧ,ⲧы ⳃⲉⲏⲟⲕ ⲡⲗⲁⲕυⲥυⲃыύ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲉⳝя ⲥⲡⲉⲣⲙⲟⳝⲗяⲇⲥⲕυύ ⲇⲣⲟⳡⲉⲣ ⲭⲟⲣⲟⲱⲟ ⳅⲏⲁю ⲕⲁⲕ υ ⲧⲃⲟю ⲙⲁⲧь ⲱⲗюⲡⲕⲩ ⲡⲣⲟⳝυⲧⲩю))  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲕυⲏь ⲙⲏⲉ ⲥⲃⲟύ ⲡυⳅⲇⲁⲕ ⲁ ⲧⲟ я ⳅⲁⳝыⲗ ⲕⲁⲕ я ⲉⲅⲟ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ υⳅⲩⲣⲟⲇⲟⲃⲁⲗ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⲥⲗυ ⲙⲟύ ⳡⲗⲉⲏ ⳅⲁⲥⲩⲏⲩⲧь ⲧⲉьⲉ ⲃ ⲩⲭⲟ? ⲧы ⲩⲥⲗыⲱυⲱь ⲱⲩⲙ ⲙⲟⲣя?) ⲏⲁ ⲕⲟⲧⲟⲣⲟⲙ я ⲃыⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲕⲟⲅⲇⲁ ⲟⲏⲁ ⲅⲩⲗяⲗⲁ ⲡⲟ ⲡⲗяⲯⲩ ⳝⲉⳅ ⲧⲣⲩⲥυⲕⲟⲃ ⲥ ⲧⲁⳝⲗυⳡⲕⲟύ " ⲇⲁⲙ ⲃ ⲁⲏⲁⲗ ⳅⲁ 20 ⲇⲁⲗ($) " я ⲉⲉ ⲃыⲉьⲁⲗ ⲕυⲏⲩⲗ ⲃ ⲙⲟⲣⲉ) ⲟⲏⲁ ⲡⲗⲁⲃⲁⲗⲁ ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲡⲣυⲙⲉⲣⲏⲟ 10-20 ⲙυⲏⲩⲧ я ⲏⲉ ⲃыⲇⲉⲣⲯⲁⲗ υ ⲥⲕⲁⳅⲁⲗ ⲥⲩⲕⲁ ⲃ ⲡυⲥⲟⲕ ⲉⳝⲗⲟⲙ υ ⲭⲩяⲏⲩⲗ ⲉⲉ ⲟⳝ ⲭⲩύ ⲃ ⲃⲟⲇⲉ$ ⲃыⲧⲁⳃυⲗ ⲉⲉ ⲏⲁ ⳝⲉⲣⲉⲇ ⲃыⲉⳝⲁⲗ υ ⲥⲕⲁⳅⲁⲗ υюⲟ ⲏⲉⲭⲩύ ⲱⲁⲗⲁⲃⲁ ⲭⲩⲉⲥⲟⲥⲟⲃ ⲇⲁⲏυⲗⲟⲃ ⲣⲁⲯⲁⲧь) ⲟⲏⲁ ⲡⲣⲟⲥⲏⲩⲗⲁⲥь ⲟⲧ ⲧⲟⲅⲟ ⳡⲧⲟ ⲃ ⲉⲉ ⲡυⳅⲇⲩ ⲙⲁⲗьⳡυⲕ 5 ⲗⲉⲧ ⲣыⳝⲕⲩ ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⳅⲁⲡⲩⲥⲧυⲗ) ⲩⲉⳝυⳃⲉ ⲧы ⲏⲁⲭⲩύ) я ⲯ ⲧⲃⲟю ⲥⲉⲙью ⲉⳝⲁⲗ ) ⲧⲁⲕ ⲉύ ⲧⲟⲧ ⲡⲁⲣⲉⲏⲉⲕ υ ⲥⲕⲁⳅⲁⲗ ⲟ¦??  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲅⲗⲩⲱ ⲧы ⲏⲁⲭⲩц ⲡυⳅⲇы ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ?) ⲡⲟⳡⲉⲙⲩ ⲧы ⲧⲁⲕⲟύ υⳅυ?) ⲏⲉ ⲃыⲃⲟⳅυⲱь?) ⲧы ⲩⲉⳝυⲏⲁ ⲏⲁⲭⲩύ))) я ⲧⲉⳝя ⳃⲁⲥ ⲟⳝ ⲭⲩύ ⳝⲩⲇⲩ ⳝυⲧь ⲥ ⲧⲁⲩⲟύ ⲥⲕⲟⲣⲟⲥⲧью яⲧⲟ ⲧы ⲥⲟⲧⲣⲉⲱь ⲥⲉⳝⲉ ⲏⲁ ⲣⲩⲕⲁⲭ ⲕⲟⲯⲩ υ я ⳅⲁⲥⲧⲁⲃⲗю ⲧⲃⲟⲉύ ⲙⲉⲧⲣυ ⲉⲉ ⲃ ⲡυⳅⲇы ⲡυⲭⲏⲩⲧь ⲁ ⲡⲟⲧⲟⲙ яⳅыⲕⲟⲙ ⲇⲟⲥⲧⲁⲧь ⲙⲟύ ⲭⲩύ υⳅ ⲧⲃⲟⲉύ ⲡυⳅⲇы))) ⲇυⲕυύ ⲧы ⲏⲁⲭⲩύ ⲩⳝⲗюⲇⲟⲱⲗⲉⲡⲟⲕ) я ⲯⲉ ⲧⲉⳝя ⳃⲁⲥ ⳝⲩⲇⲩ ⲉⳝⲁⲧь ⲟⳝ ⲙⲁⲏⲁⲱⲕⲩ ⲏⲁⲭⲩύ) ⲙⲏⲉ ⲥⲧⲁⲗυⲏ ⲙⲉⲇⲁⲗьⲕⲩ ⲏⲁ ⲭⲩύ ⲡⲟⲇцⲉⲡυⲗ ⳅⲁ ⲧⲟ ⳡⲧⲟ ⲃыⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲁⲧь)_я ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲡⲟύⲙⲁю ⲃ ⲅⲣⲩⳅυυ ⲅⲇⲉ ⲧⲉⳝя ⲣⲟⲇυⲗυ ⲡёⲥ-ⲙⲁⲧь  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱь,ⲱⲉⲗⲩⲭⲁ,ⲕⲁⲕ ⲡⲟⲯυⲃⲁⲉⲧ ⲧⲃⲟя ⲡυⳅⲇⲁ?)ⲏⲉ ⲥⲕⲩⲗυⲧ ⲡⲟ ⲙⲟⲉⲙⲩ ⲭⲩю?)ⲉⲥⲗυ ⲇⲁ,ⲧⲟ ⲅⲁⲃⲕⲏυ ⲙⲏⲉ ⲏⲁ ⲭⲩύ,я ⲡⲣυⲉⲇⲩ ⲕⲁⲕ ⲥⲙⲟⲅⲩ))0 ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⲃⲟⳃⲁⲙυ ⲧⲟⲣⲅⲩю ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲃыⲉⳝⲁⲗ ⲏⲁ ⲡⲣυⲗⲁⲃⲕⲉ ⲥ ⲟⲃⲟⳃⲁⲙυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲇⲉⲗⲁⲗ ⲏⲉⳝⲟⲗьⲱⲟύ ⲏⲉⲇⲩⲅ ⲥⲙⲉⲥⲧυⲃ ⲉё ⲙⲟⲱⲟⲏⲕⲩ ⲃ ⲡⲣⲟⲧυⲃⲟⲡⲟⲗⲟⲯⲏⲩю ⲥⲧⲟⲣⲟⲏⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲇⲗя ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲧяⲡⲕⲁ ⲏⲁ ⲟⲅⲟⲣⲟⲇⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲩⲯⲉ ⲃⲥё ⲡⲗⲉⲱь ⲡⲣⲟⲉⲗⲁ ⲕⲁⲕ ⲙⲟⲗь ⲉⳝⲁⲏⲁя ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲣⲟυⲗ ⲡⲟⲇⳅⲉⲙⲏыύ ⲡⲉⲱⲉⲭⲟⲇ ⲇⲗя ⲭⲩⲉⲃ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧⲣⲟυⲗ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡυⲣⲁⲙυⲇⲩ ⲭυⲟⲡⲥⲁ ⲁ ⲧⲁ ⲟⳝⲣⲩⲱυⲗⲁⲥь ⲏⲁ ⲡⲟⲗⲟⲃⲩю ⲅⲩⳝⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲗⲉцⲉⲃⲩю ⲥⲧⲟⲣⲟⲏⲩ ⲕⲗυⲧⲟⲣⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲩⲇⲁⲗυⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲙⲟύ ⲭⲩύ ⲇⲟυⲧ ⲕⲁⲕ ⲕⲟⲣⲟⲃⲉ ⲥυⲥьⲕⲩ,ⲭⲩⲉⲥⲟⲥ ⲧы ⲇⲉⲣⲉⲃⲉⲏⲥⲕυύ )  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧⲃⲟю ⲙⲁⲧь ⲡⲣⲟⲅⲏⲩⲗ ⲕⲁⲕ ⲕⲁⲏⲁⲧ ⲏⲁ ⲩⲣⲟⲕⲉ ⲫυⳅⲣы ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲙⲟύ ⲭⲩύ ⲅⲣыⳅⲉⲧ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧяⲅⲁю ⲕⲁⲕ ⲱⲧⲁⲏⲅⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲉύⳡⲁⲥ ⳝⲩⲇⲩ ⲇⲉⲗⲁⲧь ⲁⲙⲡⲩⲧⲁцυю ⲡⲟⲗⲃⲟύ ⲙⲁⲧⲕυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⳡⲉⲏυⲗ ⲕⲁⲕ ⲁⲃⲧⲟⲥⲗⲉⲥⲁⲣь ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡⲟⲥⲧⲣⲟυⲗ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲁⲃⲧⲟⲙⲁⲅυⲥⲧⲣⲁⲗь υ ⲅⲟⲏяⲗ ⲙⲟύ ⲭⲩύ ⲧⲁⲙ ⲡⲟ ⲃⲥⲧⲣⲉⳡⲏⲟύ ⲕⲁⲕ ⳝⲁⲏⲇυⲧ ⲟⲧ ⲡⲟⲅⲟⲏυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧⲃⲟю ⲙⲁⲧь ⲃ ⲥⲧⲟύⲗⲟ ⳅⲁⲅⲟⲏяⲗ ⲕⲁⲕ ⲕⲟⲣⲟⲃⲩ ⲉⳝⲁⲏⲏⲩю ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥⳝυⲗ ⲧⲃⲟю ⲙⲁⲧь ⲕⲟⲅⲇⲁ ⲧⲁ ⲡыⲧⲁⲗⲁⲥь ⲟⲧⲟⳝⲣⲁⲧь ⲩ ⲏⲉⲅⲟ ⲥⲗⲁⲇⲟⲥⲧь ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲩⲕⲣⲁⲥυⲗ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲕⲣⲁⲥυⲃ ⲉⲅⲟ ⲃ ⲣⲁⲇⲩⲯⲏыύ цⲃⲉⲧ υ ⲟⳝⲕⲗⲉύⲕⲟύ ⲥⲕυⲧⲟⲗⲥⲟⲙ )  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲙⲟύ ⲭⲩύ ⲥⲃⲟυⲙ ⲣⲧⲟⲙ цⲉⲡⲗяⲉⲱь ⲕⲁⲕ ⲩⲇⲟⳡⲕⲁ ⲉⳝⲁⲏⲁя)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲟύ ⲭⲩύ ⲥ ⲡⲟⲕⲟⲗⲉⲏυя ⲃ ⲡⲟⲕⲟⲗⲉⲏυⲉ ⲡⲉⲣⲉⲇⲟⲃⲁⲗⲥя ⲏⲁ ⲃⲁⲱυ ⲣⲧы)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲏⲉ ⲏⲁⲇⲟ ⲟⲧъⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲧь υ ⲃыⲕυⲏⲩⲧь?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲡυⳅⲇⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲕⲁⲕ ⲣⲁⲥⲧⲉⲏυⲉ ⲏⲁ ⲁⲙⲁⳅⲟⲏⲕⲉ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲕⲁⲯυ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉ ⲡⲩⲥⲧь ⲙⲟⲗυⲧьⲥя ⲏⲁ ⲙⲟύ ⲭⲩύ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱυⲱь?) ⲡυⳅⲇⲁⲗυⳅ?) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲭⲩⲉⲙ ⳃⲁⲥ ⲧυⲣⲁⲕⲧ ⲃ ⲡυⳅⲇⲁⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕυ ⲩⲥⲧⲣⲟю  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡυⲇⲣυⲗⲁ ⲭⲩⲉⲡⲣⲟⲉⳝⲁⲏⲏⲁя,ⲣⲟⲙⳝⲟⲃυⲧыύ ⲡυⲇⲟⲣⲁⲥ, я ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⳅⲁⲣⲉⲯⲁⲗ ⲭⲩяⲙυ ⳡⲉⲣⲉⳅ ⲣⲉⳅⲉⲧⲕⲩ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳υⲏⲟⲡⲗⲁⲏⲉⲧяⲏυⲏ ⲉⳝⲩⳡυύ?) ⲭⲗⳡⲉⲱь я ⲧⲃⲟυ яυцⲁ ⲥⲕⲟⲣⲙⲗю ⲡⲟⲡⲩⲁⲥⲁⲙ?  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲩⲏыⲗⲁя ⲃⲁⲫⲉⲗьⲕⲁ?) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲥⲁⲙⲟⲉ ⲇⲏⲟ ⲧⲣⲟⲗⲗυⲏⲅⲁ, я ⲡⲟⲏυⲙⲁю, ⳡⲧⲟ ⲃⲥⲉ ⲭⲟⲧяⲧ ⲡⲟⲃыⲉⳝыⲃⲁⲧьⲥя , ⲕⲟⲅⲇⲁ ⲧы ⲡⲟⲇⲏυⲙⲁⲉⲱьⲥя ⲡⲟⲇⲏяⲧьⲥя, ⲧы ⲥⲡⲟⲧыⲕⲁⲉⲱьⲥя ⲟⳝ ⲭⲩύ ⲥⲃⲟⲉⲅⲟ ⲡⲁⲡⲕυ ⲡⲁⲇⲁⲉⲱь ⲟⳝⲣⲁⲧⲏⲟ) ⲡυⳅⲇⲁⲏυ ⲉⳃⲉ ⳡⲉⲏυⲧь ⲱⲁⲃⲁⳡⲕⲁ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⳅⲟⲃυ ⲥⲃⲟю ⲧяⲏⲟⳡⲕⲩ я ⲭⲟⳡⲩ ⲉύ ⲗυⳡⲏⲟ ⲥⲕⲁⳅⲁⲧь ⲥⲡⲁⲥυⳝⲟ ⳅⲁ ⲃⳡⲉⲣⲁⲱⲏυύ ⲡⲣⲉⲕⲣⲁⲥⲏыύ ⲟⲧⲥⲟⲥ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲇⲟⳡⲕⲁ эⲗυⲧⲏⲟύ ⲱⲗюⲭυ υ ⲟⲧцⲁ ⳝⲟⲙⲯⲁ?___)))) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲁⲙⲕⲩ ⲧⲃⲟю ⲉⳝⲩⲧ ⲩ ⲧя ⲃ ⲕⲟⲙⲏⲁⲧⲉ ⲕⲟⲅⲇⲁ ⲧы ⲥⲡυⲱь ⲧⲉ ⲉё ⲏⲉ ⲯⲁⲗⲕⲟ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲕⲩ ⲏⲁ ⲥⲧⲟⲗⲉ υ ⲏⲁ ⲡⲟⲇⲟⲕⲟⲏⲏυⲕⲉ)) ⲁ ⲏⲩ ⲏⲉⲥυ ⲃⲉⲣⲉⲃⲕⲩ υ ⲟⲅⲏⲧⲩⲱυⲧⲉⲗь:ⳅⲁⲗⲉⳅυⲱь ⲡⲟⲧⲩⲱυⲱь ⲉύ ⲡυⳅⲇⲩ ⲁ ⲡⲟⲧⲟⲙ я ⲟⲧⲇⲁⲙ ⲃⲁⲥ ⲏⲁ ⲣⲁⲥⲧⲉⲣⳅⲁⲏυⲉ ⲏⲉⲅⲣⲁⲙ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲩⲕⲁ я ⲧⲉⳝя ⲡⲟⲥⲟⲇυⲗⲁ ⲃⳡⲉⲣⲁ ⲏⲁ ⲡⲁⲡⲕⲉⲏ ⲭⲩύ υ ⲧы ⲡⲣыⲅⲁⲗ ⲏⲁ ⲏёⲙ ⲕⲁⲕ ⲕⲟⳅёⲗ ⲥ ⲡυⳅⲇы ⲙⲁⲙⲁⲱυ ⲥⲃⲟⲉύ ⲕⲩⲣυⲏⲁύ))  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲥⲩⲕⲁ ⲃ ⲥⲉⳝя ⲡⲟⲃⲉⲣυⲗ??? ⳝⲩⲇⲉⲱь ⲟⲧⲕⲣыⲃⲁⲧь ⲣⲟⲧ ⲏⲁ ⲩⲣⲟⲃⲏυ ⲙⲟⲉύ ⲱυⲣυⲏⲕυ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲟⲥⲩⲏⲟⲕ_)ⲙⲟύ ⲗυⳡⲏыύ_)?я ⲧⲃⲟύ ⲣⲟⲧ ⲉⳝⲁⲗ_)?ⲡⲉⲣⲉⲱⲗⲉⲱь ⲙⲟυ ⲥⲙⲥ ⲧы ⳝⲩⲇⲉⲱь ⲡⲣυⳅⲏⲁⲏ ⲙⲟυ ⲫⲁⲏⲁⲧⲟⲙ_)?я ⲃⲧⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲏⲁ ⲣⲁⲥⲕⲗⲟⲇⲩⲱⲕⲉ_)?ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃⲧⲟύ ⲣⲟⲧ ⲉⳝⲁⲗ ⲏⲁ ⲃⲉⲣⲱυⲏⲉ ⲕⲗυⲧⲣⲟ ⲧⲃⲟⲉύ ⲙⲁⲙⲉ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⳅⲏⲁⲉⲱь ⳡⲧⲟ я ⲧⲟⲧ ⲥⲁⲙыύ ⲡⲁⲣⲉⲏⲉⲕ,ⳡⲗⲉⲏ ⲕⲟⲧⲟⲣⲟⲅⲟ ⲥⲩⲯⲇⲉⲏⲟ ⳝыⲗⲟ ⲧⲉⳝⲉ ⲃⳅяⲧь ⲃ ⲣⲟⲧ?) ⲏⲩ ⲧⲁⲕ ⲧⲉⲡⲉⲣь ⳅⲏⲁύ)) ⲧы ⲏⲉ ⲯⲉⲣⲧⲃⲁ ⲙⲟⲉⲅⲟ ⲭⲩя,ⲧы ⲉⲅⲟ ⲣⲁⳝыⲏя) ⲧⲁⲕ ⲣⲁⲥⲡⲟⲣяⲇυⲗⲁⲥь ⲥⲩⲇьⳝⲁ)))  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ύⲁ ⲧⲉ ⳝⲩⲇⲉⲣ ⲥⲇⲉⲗⲁю))) ⲥ ⲃⲟⲗⲟⲥⲕⲟⲙ ⲡυⳅⲇы ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⳡⲩ ⲟⲗⲩⲭ ⲉⳝⲁⲏыύ)) я ⲡⲣяⲙ ⲕⲁⲕ υⳅ ⲙⲩⲗьⲧυⲕⲁ ⲕⲁⲣⲗⲥⲟⲏ, ⲡⲣυⲗⲉⲧⲁю ⲏⲉ ⳅⲁ ⲃⲁⲣⲉⲏьⲉⲙ, ⲁ ⳅⲁ ⲉⳝⲗю ⲥ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉύ))  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟё ⳅⲁⲏяⲧυⲉ ⲡⲟ ⲃⲉⳡⲉⲣⲁⲙ эⲧⲟ ⲡⲟⲇⳝⲁⲇⲣυⲃⲁⲏυⲉ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲕⲟⲏⳡυⲗ ⲃ ⲣыⲗⲟ ⲧⲃⲟⲉύ ⲩⳝⲟⲅⲟύ ⲙⲁⲧⲉⲣυ , ⲧⲁⲕ ⲃⲟⲧ ⲟⲏⲁ ⲏⲉ ⲃыⲇⲉⲣⲯⲁⲗⲁ ⲙⲟⲉύ ⲥⲧⲣⲩυ υ ⲃыⲡⲁⲗⲁ υⳅ ⲟⲕⲏⲁ ⲥⲃⲟυⲙ ⲣⲧⲟⲙ ⲏⲁ ⲙⲟύ ⲭⲩύ) ⲧⲁⲕ ⲃⲟⲧ ⲡⲟⲧⲟⲙ я ⲡⲟⲱⲉⲗ υ ⲩⲃυⲇⲉⲗ ⲉⳝⲁⲏⲟⲅⲟ ⲡυⲇⲁⲣⲁⲥⲁ ⲧⲃⲟⲉⲅⲟ ⲡⲁⲡⲕⲩ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲉύⳡⲁⲥ ⲧⲃⲟⲉ ⲉⳝⲁⲗⲟ ⲥⲏⲟⲥυⲧь ⳝⲩⲇⲩ ⲕⲁⲕ ⲡⲟⲏⲁⲣⲁⲙⲩ ⲉⳝⲁⲏⲩю)ⲇⲁⲃⲁύ ⲙⲏⲕ ⲡυⲱυ ⲥⲩⳡⲉⲕ ⲉⳝⲁⲏыύ)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲏыύ ⲣыцⲁⲣь ⲥ ⲡυⳅⲇⲁⲕⲟⲙ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲕⲁⲕ ⲥ ⳃυⲧⲟⲙ ⲏⲁ ⲡⲗⲉⳡⲉ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя?) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь , ⲧⲟ ⳡⲧⲟ ⲧы ⲉⳝⲁⲗ ⲥⲃⲟю ⲙⲁⲧь , ⳝⲁⳝⲩⲱⲕⲩ , ⲡⲣⲟⳝⲁⳝⲩⲱⲕⲩ ⲙⲟυⲙ ⲭⲩёⲙ υ ⲩⲇυⲃⲗяⲗⲥя эⲧⲟⲙⲩ ⲏⲉ υⲅⲏⲟⲣь ⲙⲟύ ⲭⲩύ ⳡⲗⲉⲏⲟⲥⲟⲥ ))  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲏыύ ⲣыцⲁⲣь ⲥ ⲡυⳅⲇⲁⲕⲟⲙ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲕⲁⲕ ⲥ ⳃυⲧⲟⲙ ⲏⲁ ⲡⲗⲉⳡⲉ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя?) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь , ⲧⲟ ⳡⲧⲟ я ⲉⳝⲁⲗ ⲧⲃⲟύ ⲣⲟⲧ ⲥⲩⲧⲕⲁⲙυ , ⲁ ⲡⲟⲧⲟⲙ ⲏⲉ ⲥⲙⲟⲅ ⲩⲇⲉⲣⲯⲁⲧьⲥя υ ⲕⲟⲏⳡυⲗ ⲧⲉⳝⲉ ⲃ ⲏⲟⳅⲇⲣυ , υⳝⲟ ⲧы ⲣⲟⲧ ⲏⲉ ⲟⲧⲕⲣыⲃⲁⲗ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲯⲉ ⲧⲃⲟю ⲙⲁⲙⲕⲩ ⳃⲁⲥ ⲭⲩⲉⲙ ⳝⲩⲇⲩ ⲧⲟⲡⲧⲁⲧь ⲡⲟⲇ ⲡⲁⲗьⲙⲟύ ⲏⲉⲩⲯⲉⲗυ ⲧы ⲏⲉ ⲡⲟⲏяⲗ ⲱⲕⲟⲗⲟⲉⳝ ⲉⳝⲁⲏыύ ⳡⲧⲟ ⲧы ⲧⲩⲡⲟ ⲡⲟⲇⲙⲁⲥⲧⲉⲣьⲉ ⲉⳝⲁⲏⲟⲉ))  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⳡⲉⲣⲉⳅ ⲧⲉⲣⲏυυ ⲕ ⳅⲃⲉⲇⳅⲇⲁⲙ – ⲧⲁⲕ ⲇⲟⳝυⲃⲁюⲧⲥя цⲉⲗυ ⲏⲟⲣⲙⲁⲗьⲏыⲉ ⲗюⲇυ ⲏⲟ ⲏⲉ ⲧы) ⲧⲃⲟύ ⲥⲗⲟⲅⲁⲏ – ⲥⲟⲥⲁⲗ υ ⳝⲩⲇⲩ ⲥⲟⲥⲁⲧь)) ⲇⲁ ⲃы ⲃⲥⲉ ⲥⲟⲥⲩⲏⲕυ ⲩⲣⲟⲇы ⲙⲟⲣⲁⲗьⲏыⲉ ⳝⲗⲧ))  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲩ ⲧы ⲯⲉ ⲥⲩⲕⲁ ⲟⲡⲩⳃⲉⲏⲉц ) ⲇⲁ эⲧⲟ ⲩⲯⲉ ⲃⲥⲉⲙυ υⳅⲃⲉⲥⲧⲏыύ ⲫⲁⲕⲧ)) ⲕⲁⲕ ⲅⲩⲥь ⲧⲉⳝя ⲕⲁⲣⲁⲉⲧ) ⲧⲃⲟя ⳝⲁⳝⲩⲗя ⲡыⲧⲁⲗⲁⲥь ⲃⲥⲧⲩⲡυⲧь ⲥⲃⲟυⲙ ⲡυⳅⲇⲁⲕⲟⲙ ⲃ ⲥⲭⲃⲁⲧⲕⲩ ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ )) υ ⲡⲟⲏυⲙⲁⲉⲱь,ⲉύ ⲡⲟⲏⲣⲁⲃυⲗⲟⲥь))  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲏыύ ⲣыцⲁⲣь ⲥ ⲡυⳅⲇⲁⲕⲟⲙ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲕⲁⲕ ⲥ ⳃυⲧⲟⲙ ⲏⲁ ⲡⲗⲉⳡⲉ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя?) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь , ⲧⲟ ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲃ ⲙⲁⲅⲁⳅυⲏⲉ ⳅⲁ ⲡⲣυⲗⲁⲃⲕⲟⲙ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲏыύ ⲣыцⲁⲣь ⲥ ⲡυⳅⲇⲁⲕⲟⲙ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲕⲁⲕ ⲥ ⳃυⲧⲟⲙ ⲏⲁ ⲡⲗⲉⳡⲉ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя?) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь , ⲧⲟ ⳡⲧⲟ ⲧⲃⲟύ ⲟⲧⲉц ⲗⲉⲯⲁⲗ ⲡⲟ ⲇⲟ ⲙⲏⲟύ , ⲁ ⲙⲁⲧь ⲏⲁⲇⲟ ⲙⲏⲟύ υ я ⲉё ⲉⳝⲁⲗ υⲏⲧⲉⲏⲥυⲃⲏⲟ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲁⲡⲟⲙⲏυ ⲕⲁⲕ ⲧы цⲃⲉⲧⲉⲱь ⲡⲟⲥⲗⲉ ⲥⲃⲟⲉⲅⲟ ⲙυⲏⲉⲧⲁ ⲩ ⲏⲁⲥⲧⲟяⳃⲉⲅⲟ ⲁⲧⲗⲉⲧⲁ…!ⲟⲧⲡυⲱυⲥь ⲱⲕⲩⲣⲁ ?? ?? ??  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲏыύ ⲣыцⲁⲣь ⲥ ⲡυⳅⲇⲁⲕⲟⲙ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲕⲁⲕ ⲥ ⳃυⲧⲟⲙ ⲏⲁ ⲡⲗⲉⳡⲉ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя?) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь , ⲧⲟ ⳡⲧⲟ ⲧы 12:09:25 ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲃⲉⲥυⲱь ⲏⲁ ⲙⲟёⲙ ⲭⲩю ⲕⲁⲕ ⲥⲟⲡⲗя ⲡⲣⲟⲥⲧыⲉ ⲇⲃυⲯⲉⲏυя.. ⲡⲣⲟⲥⲧыⲉ ⲇⲃυⲯⲉⲏυя.. ⲧⲃⲟⲉύ ⲙⲁⲙⲟⳡⲕυ ⲏⲁ ⲭⲩяⲭ ⲃⲥⲉⲅⲟ ⳅⲉⲙⲏⲟⲅⲟ ⲱⲁⲣⲁ))) ⲁ ⲧы ⲣⲉⲱυⲗ ⲡⲣⲟⲇⲟⲗⲯυⲧь ⲟⳝыⳡυя ⲃⲁⲱⲉⲅⲟ ⲡⲣⲟⲱⲗюⲱⲉⲥⲧⲟⲅⲟ ⲣⲟⲇⲁ я ⲥⲙⲟⲧⲣю))))  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲉⳝя ⲉⳝⲁⲗυ ⲭⲁⳡυ ⲏⲁ ⲧⲉⳝя ⲕⲟⲏⳡⲁⲗυ, ⲏⲟ ⲧы, ⲧⲁⲕⲁя ⲱⲗюⲭⲁ, ⳡⲧⲟ ⲇⲗя ⲧⲉⳝя эⲧⲟ ⲡⲩⲥⲧяⲕ υ ⲙⲉⲗⲟⳡυ…  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟύ ⲁⲏⲁⲗ-ⲇыⲙⲟⲭⲟⲇ ⲕⲁⲕ ⲃⲩⲗⲕⲁⲏ υⳅⲃⲉⲣⲅⲁⲉⲧⲥя ⲧⲟⲗьⲕⲟ ⲧⲟⲗьⲕⲟ ⲃыⲗⲉⲧⲁⲉⲧ ⲟⲧⲧⲩⲇⲁ ⲯυⲇⲕⲟⲥⲧь ⲧⲃⲟⲉύ ⲙⲁⲙы ⲕⲟⲅⲇⲁ ⲟⲏⲁ ⲥⲕⲃυⲣⲧυⲧ))))  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲏыύ ⲣыцⲁⲣь ⲥ ⲡυⳅⲇⲁⲕⲟⲙ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲕⲁⲕ ⲥ ⳃυⲧⲟⲙ ⲏⲁ ⲡⲗⲉⳡⲉ ⲟⲧ ⲏⲁⲡⲁⲇⲉⲏυя ⲙⲟⲉⲅⲟ ⲭⲩя?) я ⲃⲭⲟⲯⲩ ⲃ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⳝⲉⳅ ⲥⲧⲩⲕⲁ ⲡⲟⲕⲁ ⲧы ⲥⲡυⲱь я ⲉё ⲉⳝⲩ . ⲟⲏⲁ ⲙⲟя ⲗυⳡⲏⲁя ⲡⲣⲉⲏⲁⲇⲗⲉⳅⲏⲟⲥⲧь . ⲧⲃⲟя ⲙⲁⲧь ⲥⲁⲙыύ ⳝⲗⲉⲥⲕ , ⲥⲁⲙыύ ⲕⲁύⲫ ))) ⲧⲟⲕ υⲏⲟⲅⲇⲁ ⲭⲩύ ⲕⲣыⳅёⲧ . ⲕⲟⲣⲙυⲗυ ⲇⲁⲃⲏⲟ ⲡⲣⲟⲥⲧⲟ ⲏⲁⲃⲉⲣⲏⲟ ))))  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲟⲧⲡⲣⲁⲃυⲗⲁⲥь ⲏⲁ ⲙⲁⲣⲥ ⲕⲁⲕ ⲏⲁ ⲣⲁⲕⲉⲧⲉ ⲕⲟⲥⲙⲟⲏⲁⲫⲧ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲕⲣⲩⲧυⲗ ⲕⲁⲕ ⲯⲉⲗⲉⳅⲏⲩю ⳝⲁⲏⲕⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲥⲉⲗυⲗ ⲡⲗⲉⲙя юⲏⲅυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲟⲕⲩⲡυⲣⲟⲃⲁⲗ ⲁⲏⲁⲗьⲏⲟⲉ ⲡⲣⲟⲥⲧⲣⲁⲏⲥⲧⲃⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲃыⲉⳝⲁⲗ ⲃ ⲏⲩⲧⲣυ ⲥⲁⲣⲕⲟⲫⲁⲅⲁ ⲅⲇⲉ ⲭⲣⲟⲏυⲗⲥя ⲃⲉⲗυⲕυύ ⲗⲉⲏυⲏ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲭⲣⲟⲏю ⲥⲃⲟύ ⲭⲩύ ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲕⲟⲡⳡёⲏⲩю ⲕⲩⲣυцⲩ ⲃ ⲭⲟⲗⲟⲇυⲗьⲏυⲕⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⳅⲩⳝы ⲡⲉⲣⲉⳃυⲧыⲃⲁⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲉύⳡⲁⲥ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⳅⲁⲃⲁⲣⲩⲭⲩ ⲩⲥⲧⲣⲟю ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲙυⲏⲟⲉ ⲡⲟⲗⲉ ⲃыⲗⲟⲯυⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲣⲁⲏυⲗ ⲟⲣⲩⲇυя ⲙⲁⲥⲥⲟⲃⲟⲅⲟ ⲩⲏυⳡⲧⲟⲯⲉⲏυя ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲇⲉⲗⲁⲗ ⲟⲧⲕⲣыⲧыύ ⲡⲉⲣⲉⲗⲟⲙ ⲕⲟⲗⲉⲏⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲡⲣυⲗⲟⲯυⲗ ⲥⲃⲟύ ⲭⲩύ ⲕ ⲕⲗυⲧⲟⲣⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲡⲟⲇⲟⲣⲟⲯⲏυⲕ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧяⲅⲁю ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲅυⲣυ ⲃ ⲥⲡⲟⲣⲧ ⳅⲁⲗⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲩⲗⲉⲣ ⲡⲟⲥⲧⲁⲃυⲗ ⲇⲗя ⲣⲁⲥⲡⲣⲉⲇⲉⲗⲉⲏυя ⲕⲟⲏⳡυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲡⲟⲗⲟⲃⲩю ⲙⲁⲧⲕⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲁⲙⲡⲩⲧυⲣⲟⲃⲁⲗ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲣⲟⲡυⲏыⲃⲁⲗ ⲙяⳡυⲕ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υ ⲥⲗⲩⳡⲁύⲏⲟ ⲏⲁⲇⲟⲣⲃⲁⲗⲁ ⲕⲣⲁύ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥⲕⲁⲧυⲗⲥя ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⳝⲟⳡⲕⲁ ⲥⲟ ⲥⲕⲟⲗυⲥⲧⲟύ ⲡⲗⲟⲧⲫⲟⲣⲙы?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲟⳝⲉⳅⲃⲉⲣⲯυⲃⲁⲗ ⳝⲟⲙⳝⲩ ⲡⲟⲇ ⲏⲁⳅⲃⲁⲏυⲉⲙ ⲥ4 ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧⲁⲕⲟύ ⲡⲉⲣⲉⲡⲟⲗⲟⲭ ⲩⲥⲧⲣⲟυⲗ υ ⲡⲟⲧⲟⲙ ⲡⲟⲥⲗⲉ ⲃⲥⲉⲅⲟ эⲧⲟⲅⲟ ⲉⲙⲩ ⲡⲣυⲱⲗⲟⲥь ⲃыⲡⲗⲁⳡυⲃⲁⲧь ⲕⲟⲙⲡⲉⲏⲥⲁцυю ⳅⲁ ⲏⲁⲏⲉⲥёⲏыύ ⲩⳃⲉⲣⳝ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲣⲟⲇⲁⲗ ⳅⲁ ⲁⲕцυυ ⲃ ⲛⲓⲕⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υⳅⲙⲉⲣяю ⲃⲁⲗюⲧⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲕⲣⲩⲧυⲗⲁⲥь ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲕⲁⲕ ⲏⲁ ⲱⲉⲥⲧⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲥⲏⲉⲥⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳡⲉⲣⲉⲡⲏⲩю ⲕⲟⲣⲟⳝⲕⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲟⲧ ⲩⲇⲁⲣⲁ ⲙⲟⲉⲅⲟ ⲭⲩя υ ⲭⲩя ⲙⲟⲉⲅⲟ ⲟⲧцⲁ ⲥ ⲇⲃⲩⲭ ⲥⲧⲟⲣⲟⲏ ⲧⲃⲟю ⲙⲁⲧь ⲡⲣⲟⲥⲧⲟ ⲥⲡⲗюⳃυⲗⲟ ⲕⲁⲕ υ ⲉё ⲕⲗυⲧⲟⲣ ⲃ ⲧⲉⲥⲕⲁⲭ ⲕⲟⲧⲟⲣыύ ⲡⲟⲇⲕⲣⲩⳡυⲃⲁⲗ ⲧⲃⲟύ ⲟⲧⲉц )  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲁⲃυⲗ ⲯυⲣⲏⲩю ⲧⲟⳡⲕⲩ ⲕⲁⲕ ⲥⲧⲁⲃυⲗυ ⲡυⲣⲁⲧы ⲕⲣⲉⲥⲧ ⲏⲁ ⲕⲁⲣⲧⲉ υ ⲃыⲇⲃυⲅⲁⲗυⲥь ⳅⲁ ⲥⲟⲕⲣⲟⲃυⳃⲁⲙυ ⲕⲟⲧⲟⲣыⲉ я ⲩⲧⲁυⲗ ⲃ ⲉё ⲟⳡⲕⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲩⲥⲧⲁⲏⲟⲃυⲗ ⲣⲁⲕⲉⲧⲏⲟⲉ ⲟⳝⲟⲣⲩⲇⲟⲃⲁⲏυя ⲡⲟⲇ ⲏⲁⳅⲃⲁⲏυⲉⲙ ⳅⲉⲏυⲧⲕυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲟ ⲥⲃⲟⲉⲅⲟ ⲭⲩя ⲕⲁⲕ ⲥ ⲡⲉⳡⲉⲏⲉⲅⲁ ⲥⲧⲣⲉⲗяⲗ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲣяⲙ ⲩⲡⲟⲣ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃⲟⲥⲥⲧⲁⲏⲁⲃⲗυⲃⲁⲗ ⲥυⲥⲧⲉⲙⲩ ⳝⲉⳅⲟⲡⲁⲥⲏⲟⲥⲧυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣыⳝⲁⳡυⲗ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲁ ⲡⲣυⲙⲁⲏⲕⲁ ⳝыⲗⲁ υⳅ ⲗⲟⳝⲕⲟⲃыⲭ ⲃⲟⲗⲟⲥⲕⲟⲃ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υ ⳅⲁ цⲉⲗыⲉ ⲥⲩⲧⲕυ я ⲏⲁⲗⲟⲃυⲗ ⲃⲉⲇⲣⲟ ⲣⲁⲧⲁⲏⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧυⲣⲁⲗ ⲗⲟⲧⲉⲣⲉύⲏыύ ⳝⲉⲗⲉⲧ υ ⲃыύⲅⲣⲁⲗ ⲟⲇυⲏ ⲙυⲗⲗυⲟⲏ ⲣⲩⳝⲗⲉύ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲣυⲥⲟⲃⲁⲗ ⲡⲉⲏⲧⲁⲅⲣⲁⲙⲙⲩ ⲡⲣⲉⲯⲇⲉ ⳡⲉⲙ υⳅⲅⲟⲏяⲧь ⲇⲉⲙⲟⲏⲟⲃ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲁⲃυⲗ ⲩⲥυⲗⲟⲕ υ ⲡыⲧⲁⲗⲥя ⲣⲁⳅⲅⲟⲃⲁⲣυⲃⲁⲧь ⲃ ⲥⲕⲁύⲡⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲟⲅⲇⲁ я ⲏⲁⲧяⲅυⲃⲁю ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁ ⲙυⲕⲣⲟⲫⲟⲏ ⲧⲟ ⲩ ⲙⲉⲏя ⲅⲟⲗⲟⲥ ⲇⲉⲧⲥⲕυύ ⲕⲁⲕ ⲃ ⲡⲣⲟⲅⲣⲁⲙⲙⲉ ⲥⳑⲟⲱⲛ ⲇⲁⲋⲏ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⲥⲧяⲏⲩ ⲡⲟ ⲇⲩⲡⲗⲩ ⲧⲁⲕⲏⲕⲁ ⲟⳝэⲉⲕⲧ-242 υ ⲕⲁⲕ ⲧы ⲇⲩⲙⲁⲉⲱь ⳡⲧⲟ υⳅ эⲧⲟⲅⲟ ⲃыύⲇⲉⲧ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲇⲃυⲅⲁⲗ ⲕⲁⲕ ⲧяⲯⲉⲗыύ ⲡⲣⲉⲇⲙⲉⲧ ⲃ ⲃυⲇⲉ ⲇυⲃⲁⲏⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕυⲗⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲣⲟυⲗ ⳝⲩⲏⲕⲉⲣ ⲇⲗя ⲡⲣⲟⲯυⲃⲁⲏυⲉ ⲃⲟ ⲃⲣⲉⲙя ⲕⲁⲧⲁⲕⲗυⳅⲙⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲏыⲣⲏⲩⲗ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧⲟⲗьⲕⲟ ⲥⲟ ⲥⲧⲣⲟⲭⲟⲃⲕⲟύ υ ⲥ ⲁⲕⲃⲁⲗⲁⲏⲅⲟⲙ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⳝⲣⲟⲥυⲗ ⲥⲃⲟύ ⲭⲩύ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲃυⲇⲉ яⲕⲟⲣя ⲕⲟⲧⲟⲣыⲉ ⲥⲕυⲇыⲃⲁюⲧ ⲥⲩⲇⲏⲁ ⲕⲟⲅⲇⲁ ⲡⲣυⲱⲃⲁⲣⲧⲟⲃыⲃⲁюⲧⲥя ⲕ ⳝⲩⲭⲧⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲟⲧⲡⲣⲁⲃυⲗⲥя ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲃ эⲕⲡⲉⲇυцυю ⲁ ⲧⲟⳡⲏⲉⲉ ⲕⲁⲕ ⲃ ⲕυⲏⲟ "ⲧⲁύⲏы ⲡⲉⲣⲉⲃⲁⲗⲁ ⲇяⲧⲗⲟⲅⲟ" ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲣυⲥⲟⲃⲁⲗ ⲕⲁⲣⲧⲩ ⲙυⲣⲁ υ ⲡⲟⲧⲟⲙ ⲡⲟ ⲏⲉύ ⲟⲡⲣⲉⲇⲉⲗяⲗ ⲅⲇⲉ я ⲏⲁⲭⲟⲯⲩⲥь ⲕⲁⲕ ⲡⲟ ⳋⲣⲋ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲏⲁⲕⲣыⲗ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲟⲇⲉяⲗⲟⲙ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥ ⲭⲩⲉⲙ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ υⲅⲣⲁⲗυ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲙⲟⲣⲥⲕⲟύ ⳝⲟύ ⲕⲁⲕ ⲏⲁ ⲗυⲥⲧⲟⳡⲕⲁⲭ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲇⲥⲧⲁⲃυⲗ ⲡⲟⲇ ⲧⲁⲗυⳝⲥⲕυύ ⲟⳝⲥⲧⲣⲉⲗ ⲭⲩⲉⲃ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲙⲉⲧⲕⲩ ⲟⲥⲧⲁⲃυⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧыы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟύ ⲭⲩύ ⲃ ⳅⲁⲧыⲗⲟⲕ ⲕυⲇⲁⲗ υ ⲟⲏⲁ ⲩⲡⲁⲗⲁ υ ⲡⲣⲟⲉⲭⲁⲃⲱυⲥь ⲣⲧⲟⲙ ⲡⲟ ⲕⲃⲁⲣⲧⲁⲗⲩ ⲟⲏⲁ ⲏⲁⲥⲟⳝυⲣⲁⲗⲁ ⲕⲩⳡⲩ ⲭⲩⲉⲃ )  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲱⲗυ υⲏⲫⲉⲕцυю ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲙⲉⲥⲧυⲗ ⲥⲃⲟύ ⲭⲩύ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⳅⲁⳡⲉⲙ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲥⲃⲟⲉύ ⲕⲗυⲧⲟⲣ ⲕυⲧⲁύⲥⲕⲩю ⲗⲁⲡⲱⲩ ⲏⲁⲕⲣⲩⳡυⲃⲁⲉⲧ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲗⲟⳝ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟύ ⲭⲩύ ⲡⲣυⳝυⲗ ⲃ ⲃυⲇⲉ ⲧⲣⲟⲫⲉя ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲏⲁ ⲧⲃⲟυⲭ ⲅⲩⳝⲁⲭ ⲭⲩⲉⲃ ⲡⲟⳝыⲃⲁⲗⲟ ⳝⲟⲗьⲱⲉ ⳡⲉⲙ ⲃ ⲕυⲧⲁⲉ ⳝⲟⲗьⲱⲉ ⲏⲁⲣⲟⲇⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲃ ⲇⲃⲩⲭ ⲕⲟⲗⲉⲥⲏⲟύ ⳡⲉⲭⲟⲧⲕⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟⲅⲗⲟⳃⲁⲉⲧ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲇⲁⲃⲏⲟ ⲡⲟⲣⲃⲁⲏⲟ ⲙⲟυⲙ ⲭⲩⲉⲙ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ υⳅⳝⲁⲃυⲗ ⲧⲃⲟю ⲙⲁⲧь ⲟⲧ ⲙⲩⳡⲉⲏυя ⲃ ⲏυⲯⲏυⲭ ⲅⲉⲏυⲧⲁⲗυяⲭ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲃыⲗⲉⳡυⲗ ⲟⲧ ⲣⲁⲕⲁ ⲙⲟⳅⲅⲁ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲇⲗя ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲃⲟⲗⲱⲉⳝⲏⲁя ⲡⲁⲗⲟⳡьⲕⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲣⲟⲧ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟύ ⲭⲩύ ⲗⲟⲯυⲗ ⲕⲁⲕ ⲅⲗⲁⲇυⲗьⲏⲟю ⲇⲟⲥⲕⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲣⲉⲗ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲕⲁⲕ ⲃ ⳝⲁⲏⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲅⲣⲟⳝ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁ ⲥⲃⲟⲉ ⲭⲩю ⲧⲁⳃυⲗ ⲇⲟ ⲕⲗⲁⲇⳝυⳃⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ эⲧⲟ ⲡⲁⳅⲇⳝυⳃⲉ ⲇⲗя ⲭⲩⲉⲃ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя ⲕⲁⲕ ⲣⲁⲇυⲟ ⲡⲣυёⲙⲏυⲕ ⲃ ⲙⲁⲅⲏυⲧⲟⲫⲟⲏⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲗⲟⳝ ⲧⲃⲟύ ⲙⲁⲧⲉⲣυ ⲱⲕⲃⲁⲣυⲗ ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲣⲟⲇⲁю ⲧⲁⲕⲟ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ υⳅⲩⳡυⲗ ⲁⲏⲁⲗьⲏыⲉ ⲧⲟⲏⲏⲉⲗυ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲟⲧⲟⲣы ⲡⲟⲥⲧⲣⲟυⲗυ ⲇⲣⲉⲃⲏυⲉ υⲏⲕυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲙⲟⲅⲩ ⲡⲟⲇⲃⲉⲥⲧυ ⲥⲃⲟύ ⲭⲩύ ⲕ ⲏⲟⲥⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥ ⲡⲟⲙⲟⳃью ⲧⲃⲟⲉⲅⲟ ⲣⲧⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲟⳝⲣⲁⲗυ ⲇⲣⲉⲃⲏυⲉ ⲁⲧцⲧⲉⲕυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲁⲅⲉⲏⲧ ⲕⲗυⲧⲟⲣⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υ ⲡⲟⲙⲟⲅⲁⲉⲧ ⲉύ ⲣⲉⲫυⲗⲁⲣⲁⲙυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲗⲉⲧⲁⲉⲧ ⲡⲟ ⲭⲩя ⲕⲁⲕ ⲥⲁⲙⲟⲗⲉⲧ ⲡⲟ ⲙυⲣⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟⲗⲏⲟⲥⲧью ⲡⲟⲅⲣⲩⳅυⲗⲥя ⲃ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲥⲉύⳡⲁⲥ ⳝⲩⲇⲉⲱь ⲡⲣυⲏυⲙⲁⲧь ⲙⲟύ ⲭⲩύ ⲥⲉⳝⲉ ⲃ ⲇⲩⲱⲩ ⲕⲁⲕ ⲣⲟⲇⲏⲟⲅⲟ )  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲡⲟⲕⲁ ⲧы ⲙⲟύ ⲭⲩύ ⲡⲉⲣⲉⲕⲁⲧыⲃⲁⲗ ⳡⲉⲣⲉⳅ ⲣⲁⲃⲏυⲏы,ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙы ⲥⲧⲟⲗⲕⲏⲩⲗυⲥь ⲏⲉυⳅⲃⲉⲥⲧⲏыⲉ ⲭⲩυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲉⳝя ⲣⲁⲥⲡяⲗ ⲏⲁ ⲭⲩⲉⲙ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲧⲟ ⳡⲧⲟ ⲙⲟύ ⳡⲗⲉⲏ ⲣⲃⲉⲧ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳝⲉⳅ ⲡⲣⲉⲇⲩⲡⲣⲉⲯⲇⲉⲏυⲉ ⲏⲩ ⲕⲁⲕ ⲡⲣяⲙ ⲏⲁ ⲃⲟύⲏⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ υⲡⲟⲗьⳅⲩⲉⲧ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲥⲡⲁⲗьⲏыύ ⲙⲉⲱⲟⲕ ⲃ ⲡⲟⲭⲟⲇⲁⲭ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲟⲧⲡⲣⲁⲃυⲗ ⲥⲟ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃⲟ ⲣⲧⲩ ⲃ ⲕⲣⲉⲥⲧⲟⲃыύ ⲡⲟⲭⲟⲇ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ υⳅⲩⳡⲁⲗ ⲁⲏⲁⲗьⲏⲟⲉ ⲟⲧⲃⲉⲣⲥⲧυⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υ ⲏⲁⲱⲟⲗ ⲧⲁⲙ ⲟⲥⲟⳝⲟ ⲣⲉⲇⲕυⲉ ⲁⲣⲧⲉⲫⲁⲕⲧы ⲕⲟⲧⲟⲣыⲉ ⲟⲏ ⲥⲇⲁⲗ ⲃ ⲙⲩⳅⲉύ υ ⲉⲙⲩ ⲃыⲇⲁⲗυ ⲃⲟⳅⲏⲁⲅⲣⲁⲯⲇⲉⲏυⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲉύⳡⲁⲥ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲇⲟ ⲗυⲏυυ ⲅⲟⲣυⳅⲟⲏⲧⲁ ⲣⲁⲥⲥⲧяⲏⲩ υ ⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟ ⲅⲁⳝⲁⲣυⲧⲁⲙ ⲏⲉ ⲃⲗⲉⳅⲉⲧ ⲉё ⲃ ⲩⳅⲕыύ ⲁⲏⲁⲗьⲏыύ ⲡⲣⲟⲭⲟⲇ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡⲣⲟⲯⲟⲅ ⲡⲟⲗⲟⲃⲩю ⲅⲩⳝⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⳝыⳡⲕⲟⲙ ⲥⲟⲗⲟⲫⲁⲏⲟⲃыύ ⲡⲁⲕⲉⲧυⲕ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡыⲧⲁⲗⲥя ⲥⲇⲉⲗⲁⲧь υⳅ ⲧⲃⲟⲉύ ⲥⲉⲙьυ ⳡⲉⲗⲟⲃⲉⳡⲉⲥⲕⲩю ⲙⲏⲟⲅⲟⲏⲟⲯⲕⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲥⲃⲁⲗυⲗⲁⲥь ⲏⲁ ⲙⲟύ ⲭⲩύ ⲥ ⲧⲩⲁⲗⲉⲧⲏⲟύ ⲕⲣыⲱⲕυ ⳝυⲟ ⲧⲩⲁⲗⲉⲧⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲙⲁⳅⲁⲉⲧ ⲥⲃⲟυ ⲡⲟⲗⲟⲃыⲉ ⲅⲩⳝы ⲙⲟⲉύ ⲕⲟⲏⳡυⲏⲟύ ⲇⲩⲙⲁя ⳡⲧⲟ эⲧⲟ ⲡⲟⲙⲁⲇⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲥъⳝυⲗ ⲕⲁⲕ ⲗⲟⲱⲁⲇь ⲃ ⲉⳝⲁⲏⲏⲩю ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲡⲣⲉⲗⲁ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲕⲁⲕ ⲃ ⳝⲁⲏⲉ ⲡⲟⲇ ⲃыⲥⲟⲕⲟύ ⲧⲉⲙⲡⲉⲣⲁⲧⲩⲣⲟύ ⲙⲟⲉⲅⲟ ⲭⲩя υ ⲟⲏ ⲉё ⲕⲁⲕ ⳝы υⳅⲏⲩⲧⲣυ ⲟⳝⲟⲅⲣⲉⲃⲁⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲩⲥⲧⲁⲏⲟⲃυⲗ ⲣⲁⲇυⲁⲧⲟⲣ ⲟⲧ ⲃⲉⳅⲇυⲭⲟⲇⲁ ⳡⲧⲟⳝы ⲕⲧⲟ ⲧⲟ ⲟⳝⲟⲅⲣⲉⲃⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲃ эⲧⲩ ⲭⲟⲗⲟⲇⲏⲩю ⳅυⲙⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲉⲇυⲏⲥⲧⲃⲉⲏыύ ⲕⲧⲟ ⳝⲩⲇⲉⲧ ⲟⳝⲟⲅⲣⲉⲃⲁⲧь ⲧⲃⲟю ⲙⲁⲧь эⲧⲟύ ⳅυⲙⲏⲉύ ⲥⲧⲩⲯⲟύ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⳅⲁⲗυⲗ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲗяⲇⲉⲏⲩю ⲅⲟⲣⲕⲩ ⲃ ⲡⲁⲣⲕⲉ υ ⲕⲁⲧⲁⲗⲥя ⲥ ⲏⲉё ⲏⲁ ⲥⲁⲏⲕⲁⲭ ⲗⲉⲇяⲏⲕⲁⲭ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲕⲁⲕ ⲟⲇυⲏⲟⲕυύ ⲥⲃυⲧυⲗьⲏυⲕ ⲃ ⲕⲣⲟⲙⲉⲱⲏⲟύ ⲧьⲙⲉ ⳝⲉⳅ ⲃⲉⲇⲟⲙⲁ ⲙⲟⲉⲅⲟ ⲭⲩя ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲟⲥⲧⲁⲃυⲗ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⳅⲇⲣⲁⲯⲉⲏυⲉ ⲕⲁⲕ ⲣⲉⲡⲉύⲏυⲕ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟⳝыⲃⲁⲃ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⳝⲏⲟⲣⲩⲯυⲗ ⳝⲟⲗⲉⲉ ⲧыⲥяⳡυ ⲩⲅⲣⲟⳅ ⲕⲁⲕ ⲁⲏⲧυ-ⲃυⲣⲩⲥ,ⲛⲟʀⲇ 32 ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟⲙⲉⲥⲧυⲗⲥя ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲃ υⳅⳝⲩⲱⲕⲩ ⲏⲁ ⲕⲩⲣьυⲭ ⲏⲟⲯⲕⲁⲭ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟⲇⲭⲟⲇυⲧ ⲕ ⲟⳡⲕⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⳅⲟⲗⲟⲧⲟύ ⲕⲗюⳡυⲕ ⲕ ⲥⲩⲏⲇⲩⲕⲩ ⲥ ⲥⲟⲕⲣⲟⲃυⳃⲁⲙυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲙⲁⲧⲉⲣυ ⲩⲕⲗⲁⲇыⲃⲁⲗ ⲥⲧⲉⲏⲕⲩ υⳅ ⲕυⲡⲣⲡυⳡⲉύ ⲇⲗя ⲟⲡⲟⲣы ⲥⲃⲟⲉⲅⲟ ⲭⲩя ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲧⲁⲗ ⲕⲟⲙⲕυ ⲏⲁⲃⲟⳅⲁ ⲕⲁⲕ ⲏⲟⲃⲟⳅⲏыύ ⲯⲩⲕ υ ⲡⲟⲧⲟⲙ ⲥⲕυⲇыⲃⲁⲗ ⲃ ⲏⲩⲧⲣь ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧⲣⲉⲗяⲗ υⳅ ⲥⲃⲟⲉⲅⲟ ⲭⲩя ⲕⲁⲕ υⳅ ⲗⲩⲕⲁ ⲁ ⲥⲧⲣⲉⲗы ⳝыⲗυ ⲃ ⲃυⲇⲉ ⲕⲟⲏⳡυⲏы ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲅⲣⲁⲏυ ⲥⲙⲉⲣⲧυ ⲟⲧ ⲃыⲥⲧⲣⲉⲗⲁ ⲙⲟⲉⲅⲟ ⲭⲩя ⲃ ⲉё ⲉⳝⲗⲉⲧ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲏⲉ ⲏⲣⲁⲃυⲧⲥя ⲕⲟⲅⲇⲁ ⲧы υ ⲧⲃⲟя ⲙⲁⲧь ⲡⲟⲕⲗⲟⲏяⲉⲧⲥя ⲙⲟⲉⲙⲩ ⲭⲩю ⲯⲇя ⲇⲟⲯⲇя υⳅ ⲙⲟⲉύ ⲥⲡⲉⲣⲙы ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲩ ⲧⲃⲟⲉⲅⲟ ⲟⲧцⲁ ⲥⲡυⳅⲇυⲗ ⲇⲩⲭυ ⲏⲁⳝⲣыⳅⲅⲁⲗⲥя υⲙυ υ ⲡⲟⲱⲟⲗ ⲉⳝⲁⲧь ⲧⲃⲟю ⲙⲁⲧь ⳡⲧⲟ ⳝы ⲣⲟⲇⲏыⲙ ⳅⲁⲡⲁⲭⲟⲙ ⲡⲁⲭⲗⲟ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υⲡⲣⲁⲃυⲗ ⲧⲉⲭⲏυⳡⲉⲥⲕⲩю ⲏⲉⲡⲟⲗⲁⲇⲕⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕυⲗⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲣⲟⲃⲟⲇυⲗ ⲅⲁⳅⲟⲃⲩю ⲁⲧⲁⲕⲩ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲇυⲭⲗⲟⲫⲟⲥ ⲇⲗя ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳝⲗⲟⲭ ⲃыⲃⲟⲇυⲧь υⳅ ⲉё ⲗⲟⳝⲕⲟⲃыⲭ ⲃⲟⲗⲟⲥⲟⲃ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁⳝⲣⲁⲥыⲃⲁⲉⲧⲥя ⲏⲁ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲕⲁⲃⲕⲁⳅⲕⲁя ⲟⲃⳡⲁⲣⲕⲁ ⲥ ⲅⲟⲣⲏыⲭ ⲣⲁⲃⲏυⲏ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲟⲅⲇⲁ ⲣⲟⲥⲥυя ⲡⲩⲥⲕⲁⲗⲁ ⲣⲁⲕⲉⲧы ⲧⲟ ⲇⲁⲏⲏыⲉ ⲕⲟⲟⲣⲇυⲏⲁⲧы υⳅⲙⲉⲏυⲗυⲥь υ ⲃⲗⲉⲧⲉⲗυ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲏⲟⲥυⲧⲥя ⳅⲁ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲕⲁⲕ ⲃⲟⲗⲕ ⳅⲁ ⳅⲁύцⲟⲙ υⳅ ⲙⲩⲗьⲧυⲕⲁ "ⲏⲩ ⲡⲟⲅⲟⲇυ" ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲥ ⲡⲟⲗя ⲥⲟⳝυⲣⲁⲗⲁ ⲭⲩυ ⲃ ⲃυⲇⲉ ⲅⲣυⳝⲟⲃ υ ⲥⲕⲗⲁⲇыⲃⲁⲗⲁ ⲥⲉⳝⲉ ⲃ ⲟⳡⲕⲟ ⲃ ⲃυⲇⲉ ⲕⲁⲣⳅυⲏы ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⲧⲣⲁⲯⲁⲗ ⲁⲧⲁⲕⲩ ⲧⲁⲗυⳝⲥⲕυⲭ ⲭⲩⲉⲃ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⳝⲩⲥⲧⲣⲟυⲗ ⲕⲁⲕ ⲕⲟⲙⲏⲁⲧⲩ ⲃ ⲕⲃⲁⲣⲧυⲣⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲧⲣⲟυⲗ ⲥⲧυⲣⲁⲗьⲏⲩю ⲙⲁⲱυⲏⲕⲩ ⲇⲗя ⲭⲩⲉⲃ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ υⳅⲙⲉⲣяⲗ ⲇⲗυⲏⲩ ⲕⲗυⲧⲟⲣⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲧⲁⲃⲗю ⳅⲁⲡяⲧыⲉ ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲧы ⲟⲡⲉⳅⲇⲟⲗ ⲧⲩⲡⲟⲣыⲗыύ ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱ, ⲡυⲇⲟⲣⲁⲥ, ⲥюⲇⲁ υⲇυ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲇⲁⲗ ⲕⲟⲗⳝⲁⲥⲟύ ⲡⲟ ⲉⳝⲁⲗⲩ, υ ⲥⲕⲁⳅⲁⲗ, ⳡⲧⲟ ⲧⲁⲕ ⳝыⲗⲟ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲧь ⲧы ⲕⲩⳝ ⲕⲃⲁⲇⲣⲁⲧⲏыύ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲃ ⲗⲉⲥⲩ ⲏⲁⲧⲕⲏⲩⲗⲁⲥь ⲏⲁ ⲙⲟύ ⲭⲩύ,ⲕⲁⲕ ⲕⲣⲁⲥⲏⲁя ⲱⲁⲡⲟⳡⲕⲁ ⲏⲁ ⲃⲟⲗⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲧь ⳅⲁⲇⲉⲣⲯυⲃⲁⲉⲧ ⲇыⲭⲁⲏυⲉ ⲡⲣυ ⲃυⲇⲉ ⲙⲟⲉⲅⲟ ⲭⲩя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟ ⲫⲁⲕⲧⲩ ⲧы ⲥⲟⲥⲉⲱь ⲙⲏⲉ ⲭⲩύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲧь ⳝⲉⲗыύ ⲗⲉⳝⲉⲇь ⲙⲟⲉⲅⲟ ⲭⲩя ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲱёⲗ ⲏⲁ ⲫⲣⲟⲏⲧ ⲃ ⲏⲁⲇⲉⲯⲇⲉ ⲩⲃυⲇⲉⲧь υ ⲥⲡⲁⲥⲧυ ⲟⲧ ⲡⲗⲉⲏⲁ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳эⲧⲟ ⲏⲟⲃⲁя эⲣⲁ ⲧⲣⲟⲗⲗυⲏⲅⲁ, ⲧⲩⲧ ⲥⲟⲱⲗυⲥь ⲃ ⲡⲟⲉⲇυⲏⲕⲉ ⳅⲩⳝы ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υ ⲙⲟύ ⳡⲗⲉⲏ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲕⲩⲇⲁ ⲥъⲉⳝыⲃⲁⲉⲱь? ) ⳅⲃⲉⲣⲟⲥⲟⲃⲭⲟⳅ ⲁⲏⲁⲗьⲏыύ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ я ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲃ ⲡⲁⲣⲕⲉ юⲣⲕⲥⲕⲟⲅⲟ ⲡⲉⲣⲉⲟⲇⲁ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲫⲩ, ⲥⲧⲣⲉⲗⲟⳡⲏυⲕ, ⲧⲃⲟя ⲙⲁⲧь ⲧⲟⲯⲉ ⲥⲧⲣⲉⲗяⲉⲧ ⲅⲩⳝⲟύ ⲡⲟ ⲙⲟⲉⲙⲩ ⲭⲩю ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲕⲟⲅⲇⲁ ⲏⲁ ⲡⲟⲗяⲏⲕⲉ ⳅⲁⲯⲅⲗυⲥь ⲫⲟⲏⲁⲣυ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲧь ⲩⲃυⲇⲉⲃ ⲙⲟύ ⲭⲩύ ⲥⲕⲁⳅⲁⲗⲁ -" ⳡⲧⲟ ⳅⲁ ⲕⲣⲁⲥⲁⲃⲉц " ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲏⲁⲃⲉⲣⲏⲟⲉ ⲏⲉ ⳅⲏⲁⲗ, ⲏⲟ ⲙⲟύ ⲭⲩύ ⲡⲣⲟяⲃⲗяⲗ ⲁⲕⲧυⲃⲏⲟⲥⲧь ⲉⳃё ⲃ ⲁⲏⲧυⳡⲏⲟⲥⲧυ, ⲙⲟύ ⲭⲩύ ⲡⲟ ⲥⲗⲟⲃⲁⲙ ⲩⳡⲉⲏыⲭ ⳝыⲗ ⲥⲡⲁⲥυⲧⲉⲗⲉⲙ ⲗюⲇⲥⲕⲟⲅⲟ ⲣⲟⲇⲁ. ⲙⲟύ ⲭⲩύ ⲥⲡⲁⲥ ⲗюⲇⲉύ ⲟⲧ ⲅⲟⲗⲟⲇⲁ υ ⲯⲁⲯⲇы ⲃ ⲧⲟⲙ ⳡυⲥⲗⲉ υ ⲧⲃⲟю ⲙⲁⲧь ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲥⲟⲥⲁⲗⲁ ⲥ ⲙⲟⲗυⲧⲃⲟύ ⲉⳝⲁⲏⲁⲱⲕⲁ ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲩ ⲧⲉⳝя ⲙⲟⲗⲟⲫья ⲏⲁ ⲅⲩⳝⲉ, ⲃыⲧⲣυ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡυⲇⲟⲣ, ⲁ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲥⲁⲥⲉⲧ!!! ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲭⲩⲉⲥⲟⲥ, ⲁ я ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲅⲟⲣⲁⲭ ⲕⲁⲃⲕⲁⳅⲁ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲉⳝⲉ ⲉⳝⲁⲗьⲏυⲕ ⳡⲗⲉⲏⲟⲙ ⲡⲟⲧⲩⲱⲩ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲁⲧь ⲧⲃⲟю ⲉⳝⲁⲗ ⲏⲁ ⲡⲣυⲉⲙⲉ ⲩ ⲥⲧⲟⲙⲁⲧⲟⲗⲟⲅⲁ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲁⲙⲁⲱⲕⲁ ⲧⲃⲟя ⲱⲗⲁ ⲏⲁ ⲭⲩύ, ⲕⲁⲕ ⲏⲉⲅⲣ ⳅⲁ ⲥⲃⲟⳝⲟⲇⲟύ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟύⲙυ ) ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲥⲡⲁⲥⲁⲉⲧⲥя ⲟⲧ ⳝⲉⲇ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю, ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲅⲟⳝⲗυⲏ ⲙⲟⲉⲅⲟ ⲭⲩя, я ⲉύ цⲉⲗⲕⲩ ⲃυⲱⲉⲏⲕⲟύ ⲥⲟⲣⲃⲁⲗ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲁ ⲧы ⳅⲏⲁⲗ, ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡυⳃⲉⳅⲁⲙⲉⲏυⲧⲉⲗь ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ? ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲕⲟⲗⳡⲁⲏⲟⲙ ⲙⲁⲧь ⲧⲃⲟю ⲉⳝⲁⲗ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲇυⲏⲁⲙυⲕ ⲙⲟⲉⲅⲟ ⲭⲩя ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⳝυⲗ ⲡⲟⲥⲩⲇⲩ ⲟⳝ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲁ ⲕⲣыⲱⲉ ⲇⲟⲙⲁ ⲧⲃⲟⲉⲅⲟ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲟύ ⲭⲩύ ⲏⲉ ⲣⲩⳡⲕⲁ, ⳅⲁⳡⲉⲙ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁⲡυⲥⲁⲗⲁ ⲥⲉⳝⲉ ⲏⲁ ⲗⳝⲩ ⲙⲟυⲙ ⲭⲩⲉⲙ? ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲟυⲙ ⲭⲩⲉⲙ ⲟⲧⲕⲁⲡыⲃⲁⲗυ ⲭⲣⲁⲙ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲙⲁ ⲧⲟⳡυⲧ ⳅⲩⳝы ⲟⳝ ⲙⲟύ ⲭⲩύ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲧь ⲧы ⳡⲩⲱⲕⲁ ⲟⳝⲟⲥⲣⲁⲏⲁя, ⲁ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲡυⲇⲟⲣⲁⲥⲕⲁ ⲕⲁⲣⲧⲁⲃⲁя ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲕⲁⲕ ⲧⲟ ⲡⲩⲱⲕυⲏ ⲥⲕⲁⳅⲁⲗ, ⳡⲧⲟ ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⳝⲟⲗьⲱⲉ ⲃⲟⲗⲟⲥ ⳡⲉⲙ ⲩ ⲉⲃⲣⲉя ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲙⲁ ⲭⲩⲉⲥⲟⲥⲕⲁ, ⲁ ⲧы ⲡυⲇⲟⲣⲁⲥ ⲥⲗυⳅυⲥⲧыύ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲥⲗυⳅⲏяⲕ ⲙⲟⲉⲅⲟ ⲭⲩя ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲟⲧⲇыⲭⲁⲗⲁ ⲃ ⲧⲩⲣцυυ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲁⲧь ⲧⲃⲟю ⲉⳝⲁⲗ, ⲇⲩⲣⲁⳡⲟⲕ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲙⲟύ ⲭⲩύ, ⲕⲁⲕ ⳅⲉⲏυцⲩ ⲟⲕⲁ ⳝⲉⲣⲉⲯⲉⲧ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲥⲕⲗⲟⲏⲉⲏ ⲕ ⲥⲩυцυⲇⲩ, ⲁ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⳝⲟⲗⲉⲏ ⲙⲟυⲙ ⲭⲩⲉⲙ ⳡⲧⲟ ⲗυ? ) ⲏⲁⲭⲩύ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ υⳅⲩⳡⲁⲉⲧ ⲙⲟύ ⲭⲩύ? ) ⲟⲏ ⲏⲉ ⲙυⲫ υ ⲏⲉ ⲗⲉⲅⲉⲏⲇⲁ ) ⲙⲟύ ⲭⲩύ ⲃⲟⲱёⲗ ⲃ ⲧⲃⲟю ⲙⲁⲧь, ⲕⲁⲕ ⲥⲁⲙⲟⲗёⲧ ⲃ ⲁⲏⲅⲁⲣ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲏⲁ ⲡυⳅⲇⲉ ⲧⲁⲧⲩυⲣⲟⲃⲕⲁ ⲃ ⲃυⲇⲉ ⲙⲟⲉⲅⲟ ⲭⲩя ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲗ ⲙⲁⲧь ⲧⲃⲟю ⲃ ⲡⲉⲣυⲟⲇ ⲭⲁⲣьⲕⲟⲃ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲧь ⳡⲧⲟ ⲕⲁⲃⳝⲟύ? ) ⲏⲁⲭⲩύ ⲟⲏⲁ ⲃыⲣяⲇυⲗⲁⲥь ⲃ ⲱⲗяⲡⲩ? ) ⲟⲏⲁ ⲗюⳝυⲧ ⲕⲟⲅⲇⲁ ⲉё ⲃ ⲱⲗяⲡⲉ ⲉⳝⲩⲧ? ) ⲧⲃⲟя ⲙⲁⲧь ⲇⲩⲣⲁ? ) ⲏⲁ ⲭⲩя ⲟⲏⲁ ⲏⲁⲧяⲏⲩⲗⲁ ⲅⲁⲏⲇⲟⲏ ⲏⲁ ⲅⲟⲗⲟⲃⲩ? ) ⲟⲏⲁ ⳡⲧⲟ ⲣⲉⲱυⲗⲁ ⲣⲁⳅⲅⲣⲁⳝυⲧь ⲅⲩⳝⲟύ ⲙⲟύ ⲭⲩύ? ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲧь ⳅⲃⲟⲏυⲗⲁ ⲙⲟⲉⲙⲩ ⲭⲩю ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲧь ⲡυⲕⲁⲡυⲧ ⲙⲟύ ⲭⲩύ ⲃⳅⲅⲗяⲇⲟⲙ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲟύ ⲭⲩύ ⲏⲉ ⲕⲁⲣⲁⲏⲇⲁⲱ, ⲏⲟ ⲟⲏ ⲟⲥⲧⲁⲃυⲗ ⲁⲃⲧⲟⲅⲣⲁⲫ ⲏⲁ ⲅⲩⳝⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲟⲏ ⲇⲟⲗⲅⲟ ⲇⲣⲁⲗⲥя ⲥ ⲏⲉύ, υ ⲡⲟⳝⲉⲇυⲗ ⲧⲣⲉⲙя ⳅⲁⲗⲡⲁⲙυ, ⲧⲃⲟя ⲅⲩⳝⲁ ⳝыⲥⲧⲣⲟ ⲥⲇⲁⲗⲁⲥь ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲡⲣяⲙ ⲁⳝⲟⲣυⲅⲉⲏ,ⲃⲧⲟⲣⲅⲥя ⲃ ⲇⲯⲩⲏⲅⲗυ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ, ⲧы ⲡⲟⲏяⲗ ⲟ ⳡⲉⲙ я)) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⳝⲗя,ⲧы ⲏⲁⲃⲉⲣⲏⲟ ⲉⲇυⲏⲥⲧⲃⲉⲏⲏыύ ⳅⲁⲣⲟⲇыⲱ ⲕⲟⲧⲟⲣыύ ⲃыⲯυⲗ ⲡⲟⲥⲗⲉ ⲁⳝⲟⲣⲧⲁ, ⲏⲁⲃⲉⲣⲏⲟⲉ ⳅⲃⲩⳡυⲧ ⲥⲧⲁⲣⲟ υ ⳝⲁⲏⲁⲗьⲏⲟ, ⲏⲟ ⲧы ⲯⲉⲣⲧⲃⲁ ⲟⳝⲟⲣⲧⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱ, ⲧы ⲁⳝⲟⲣⲧυⲃⲏыύ ⲇⲁⲩⲏ, ⲩ ⲧⲉⳝя ⲣⲁⳅⲃυⲧυⲉ ⲏⲁⳡⲁⲗⲟ ⲥⲕⲁⲧыⲃⲁⲧьⲥя ⲕ ⲏⲩⲗю, ⲧы ⲥ ⲕⲁⲯⲇⲟύ ⲥⲉⲕⲩⲏⲇⲟύ ⲅⲗⲩⲡⲉⲉ, υ ⲧⲩⲡⲉⲉ,ⲡⲟⲃⲁⲇⲕυ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲕⲥⲧⲁⲧυ,ⲟⲏⲁ ⲧⲟⲯⲉ ⲇⲉⲅⲣⲁⲇυⲣⲩⲉⲧ, ⲉύ ⲅⲟⲃⲟⲣυⲱь - ⲡⲣυⲏⲉⲥυ ⲡⲟⲡυⲧь.ⲁ ⲟⲏⲁ ⲕ ⲭⲩю, υ ⲥⲟⲥⲁⲧь ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡυⳅⲇⲉц ⲧы ⳝⲁⳝⲁ, я ⲧⲣⲟⲗⲗυⲧь ⲏⲁⳡυⲏⲁю ⲧⲟⲗьⲕⲟ, ⲁ ⲧы ⲩⲯⲉ ⲏⲟⲉⲱь, я ⲇⲁⲯⲉ ⲏⲉ ⲣⲁⳅⲟⲅⲣⲉⲗⲥя ⲉⳃё ))) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲁⲗⲗⲟ, ⳝⲗяⲇь,ⲕⲁⲕⲁя ⲥⲃⲁⲇьⳝⲁ? ) ⲧⲩⲧ ⲡⲟⲉⳝⲁⲗ, ⳝⲣⲟⲥυⲗ, я ⲏⲉ ⳝⲩⲇⲩ ⲯⲉⲏυⲧьⲥя ⲏⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲕⲉ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲉ ⲏⲁⲇⲉύⲥя ⲟⲧⲥⲟⲥⲁⲧь ⲙⲏⲉ ⲭⲩύ,я ⳝⲟⲗьⲱⲉ ⲏⲉ ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲧь,ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕⲉ ⲧⲟ ⲯⲉ ⲥⲁⲙⲟⲉ ⲡⲉⲣⲉⲇⲁύ, ⳡⲧⲟⳝ ⳅⲁⲃⲧⲣⲁ ⲏⲉ ⲡⲣυⲭⲟⲇυⲗⲁ, ⲁ, ⲇⲁ,ⲥ ⳝⲁⲣⲇⲉⲗя ⲟⲏⲁ ⲧⲟⲯⲉ ⲩⲃⲟⲗⲉⲏⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⳡⲟ ⲧⲁⲙ,ⳅⲁⲇⲩⲙⲁⲗⲥя?) ⲇⲩⲙⲁⲉⲱь ⲟ ⲙⲟⲉⲙ ⲭⲩⲉ,ⲕⲥⲧⲁⲧυ, ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕⲉ ⲙⲟύ ⲭⲩύ ⲧⲟⲯⲉ ⲥⲏυⲧⲥя, υ ⲥⲏυⲧⲥя ⲧⲟ,ⲕⲁⲕ я ⲉⳝⲁⲗ ⲉё ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲇⲁ ⲧы ⳅⲁⲉⳝⲁⲗ, ⲩⲏыⲗыύ ⲭⲩⲉⲥⲟⲥ, ⲧы ⳡⲟ ⲧⲁⲙ ⲙяⲙⲗυⲱь? ) ⲧы ⲇⲩⲙⲁⲉⲱь ⲥⲗυⲧь ⲙⲉⲏя? ) ⲡⲟⲥⲙⲟⲧⲣυ ⲧⲟ, ⳡⲧⲟ ⲡυⲱⲩ я,ⲁ ⲡⲟⲧⲟⲙ ⲏⲁ ⲥⲃⲟё ⲇⲉⲣьⲙⲟ,ⲇⲁ,я ⲧⲟⲯⲉ ⲏⲉ υⲇⲉⲁⲗ, ⲏⲟ ⲧы ⲃⲟⲟⳝⳃⲉ ⲉⳝⲩⳡⲉⲉ ⲅⲟⲃⲏⲟ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲁύ, ⲧⲁⲕⲟⲙⲩ ⲭⲩⲉⲥⲟⲥⲩ, ⲕⲁⲕ ⲧы,ⳝⲉⲥⲡⲟⲗⲉⳅⲏⲟ ⲟⳝъяⲥⲏяⲧь,ⲧы ⲯⲁⲗⲟⲕ υ ⲅⲗⲩⲡ, ⲧⲃⲟя ⲙⲁⲧь υⳅⲃⲉⲥⲏⲉⲉ ⲥыⳡⲉⲃⲟύ,ⲉё ⲣⲟⲧ ⳅⲏⲁⲙⲉⲏυⲧ ⲏⲁ ⲃⲥю ⲣⲟⲥⲥυю) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲣⲉⲇⲡⲟⲗⲟⲯυⲙ ⲧⲟⲧ ⲫⲁⲕⲧ,ⳡⲧⲟ я ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь,ⲏⲟ ⲃⲉⲇь я ⲡⲣⲉⲇⲩⲡⲣⲉⲯⲇⲁⲗ, ⳡⲧⲟ ⳝⲩⲇⲉⲧ ⳝⲟⲗьⲏⲟ, ⲇⲁ, эⲧⲟ ⳡυⲥⲧⲁя ⲡⲣⲁⲃⲇⲁ, я ⲃыⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь, ⲏⲉ ⲧⲉⳝⲉ ⲙⲉⲏя ⲥⲩⲇυⲧь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲁⲗⲗⲟ, я ⲡⲣυⲱёⲗ, ⲇⲁⳝы ⲟⲧ ⳡυⲥⲧυⲧь ⲉⳝⲗⲟ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲟⲧ ⲱⲧⲩⲕⲁⲧⲩⲣⲕυ ⲥⲃⲟυⲙ ⳝⲟⲗьⲱυⲙ, ⲧⲟⲗⲥⲧыⲙ ⲭⲩⲉⲙ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲩ ⲏυⲭⲩя ⲧⲃⲟя ⲙⲁⲧь ⲇⳅюⲇⲟυⲥⲧ ⲥ ⲃⲉⲣⲧⲩⲱⲕυ ⲅⲩⳝы ⲙⲟύ ⲭⲩύ ⲩⲗⲟⲯυⲗⲁ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲣⲟⲥⲧυ, ⲏⲟ я ⲥⲗⲩⳡⲁύⲏⲟ ⲩⲣⲟⲏυⲗ ⲁⳝⲁⲯⲩⲣ ⲏⲁ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲧⲩⲱυ ⳝыⲥⲧⲣⲉⲉ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲡⲣυⲱⲗⲁ ⲃ ⲁⳝⳝⲁⲧⲥⲧⲃⲟ, ⲣⲁⲥⲕυⲏⲩⲗⲁ ⲥⲃⲟυ ⲅⲩⳝы ⲏⲁ ⲥⲕⲁⲙью, υ ⲏⲁⳡⲁⲗⲁ ⲥⲟⲥⲁⲧь ⲭⲩυ цⲉⲣⲕⲟⲃⲏυⲕⲁⲙ ⲟⲧⳡυⳃⲁя ⲥⲃⲟύ ⲣⲟⲧ ⲟⲧ ⳅⲗыⲭ ⲃⲣⲉⲇυⲧⲉⲗⲉύ, ⲏⲟ эⲧⲟ ⲡⲟⲭⲩύ, я ⲡⲣⲟⲥⲧⲟ ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲧь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲁⳝⳝⲣⲉⲃυⲁⲧⲩⲣⲁ ⲣⲧⲁ ⲧⲃⲣⲉύ ⲙⲁⲙⲁⲱυ ⲧⲁⲕⲟⲃⲁ " ⳝⳅⳃⲩⲃ " - ⳝⲉⲣⲩ ⳅⲁ ⳃⲉⲕⲩ ⲩ ⲃⲥⲉⲭ, ⲃⲟⲧ ⲧⲁⲕⲁя ⲧⲃⲟя ⲙⲁⲧь ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲃⲟⲧ ⲥⲙⲟⲧⲣυ ,ⲇⲩⲣⲁⳡⲟⲕ, ⲃⲟⲧ я ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲧь, ⲇⲁ?) ⲁ ⲧы ⲡⲣⲟⲥⲧⲟ ⲥⲙⲟⲧⲣυⲱь, υ ⲏⲉ ⲇⲉⲗⲁⲉⲱь ⲏυⳡⲉⲅⲟ, ⲃⲟⲧ ⲇⲩⲣⲁⲕ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⳡⲧⲟ ⲧⲃⲟⲣυⲱь, ⲙⲟύ ⲇⲣⲩⲅ, ⲩ ⲧⲉⳝя ⲟⳡⲕⲟ ⲇыⲣяⲃⲟⲉ, ⲩ ⲧⲉⳝя ⲏⲉⲇⲩⲅ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱ, ⲃⲟⲧ ⲥⲙⲟⲧⲣυ ⲃ ⳡⲉⲙ ⲡⲣⲟⳝⲗⲉⲙⲁ ⲧⲃⲟⲉⲅⲟ ⲟⳡⲕⲁ,ⲟⲏⲟ ⲡⲣⲟⲥⲧⲟ ⲇыⲣяⲃⲟⲉ, ⲏυⲧⲟⲅ υ υⲅⲟⲗⲟⲕ ⲃⲥⲉⲅⲟ ⲙυⲣⲁ ⲏⲉ ⲭⲃⲁⲧυⲧ, ⳡⲧⲟⳝ ⲉⲅⲟ ⳅⲁⲱυⲧь ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲁ ⳅⲏⲁⲉⲱь, ⲃⲟⲧ я ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲧь, ⲕⲁⲕ ⲱⲁⲙⲁⲏ ⲃыⳅыⲃⲁⲉⲧ ⲇⲩⲭⲟⲃ, я ⲃыⳅыⲃⲁю ⲧⲃⲟю ⲙⲁⲧь ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲭⲉⲭ, ⲡⲉⲧⲩⲱⲟⲕ, ⲧы ⲡⲁⲗьцы ⲏⲉ ⲥⲗⲟⲙⲁύ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲃⲟⲧ ⳡⲟⲧⲁ ⲙⲁⲧь ⲧⲃⲟю ⲧⲁⲕ ⲡⲟⲉⳝыⲃⲁю, ⲕⲁⲕ ⲥ ⲩⲧⲣⲉцⲁ ⲕⲟⲫⲉⲉⲕ, ⲡⲣяⲙ ⲉё ⲟⳡⲕⲟ ⳝⲟⲇⲣυⲧ ⲥ ⲩⲧⲣⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲉⳝя ⲅⲣυⲡⲡⲟⲙ ⲏⲉ ⲃ ⲱⲕⲟⲗⲉ ⳅⲁⲣⲁⳅυⲗυ, ⲧы ⲡⲣⲟⲥⲧⲟ ⲕⲟⲅⲇⲁ ⲭⲩύ ⲥⲟⲥⲁⲗ ⳅⲁⲣⲁⳅυⲗⲥя ⲟⲧ ⲥⲃⲟⲉⲅⲟ ⲟⲧцⲁ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲁ ⲧы ⳅⲏⲁⲗ, ⳡⲧⲟ ⲃυⳡ ⲡⲉⲣⲉⲇⲁёⲧⲥя ⲡⲟ ⲟⳡⲕⲩ υ ⲃⲁⲅυⲏⲉ, ⲃⲟⲧ я ⲕⲟⲅⲇⲁ ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⳝⲉⳅ ⲅⲁⲏⲇⲟⲏⲁ ,ⲥⲧⲟ ⲣⲁⳅ ⲡⲉⲣⲉⲕⲣⲉⲥⲧυⲗⲥя ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⳡⲉⲙⲩ ⲧⲃⲟύ ⲧⲣⲟⲗⲗυⲏⲅ ⲧⲁⲕⲟύ ⲧⲟⲏⲕυύ?) ⲡⲟ ⲏⲉⲙⲩ ⲡⲟⲉⳅⲇ ⲡⲣⲟⲉⲭⲁⲗ υⲗυ ⲏⲁ ⲏⲉⲅⲟ ⲥⲗⲟⲏ ⲥⲉⲗ? ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⳝⲗяⲇь ⲏⲁⲱёⲗ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲕⲩ ⲏⲁ ⲧⲣⲁⲥⲥⲉ, ⲕⲁⲕ ⲥⲟⲧⲕⲩ ⲃ ⳅυⲙⲏⲉύ ⲕⲩⲣⲧⲕⲉ, ⲣⲁⳅⲏυцⲁ ⳝⲟⲗьⲱⲁя, ⲏⲟ ⲣⲁⲇⲟⲥⲧь ⲟⲇυⲏⲁⲕⲟⲃⲁя ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲁⲭⲁ,юⲏыύ ⲇⲉⲅⲣⲁⲇⲁⲏⲧ ⲩ ⲕⲟⲧⲟⲣⲟⲅⲟ ⲓq ⲣⲁⳅⲙⲉⲣⲁ ⲥ ⳡⲗⲉⲏⲁ ⲥⲟⳝⲁⲕυ ⲇⲩⲙⲁⲉⲧ, ⳡⲧⲟ ⲧⲣⲟⲗⲗυⲧь ⲩⲙⲉⲉⲧ? ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲟⲱυⳝⲁⲉⲱьⲥя, я ⲙⲟⲅⲩ ⲧⲃⲟю ⲙⲁⲙⲁⲏьⲕⲩ ⲉⳝⲁⲧь ⲅⲟⲇ, ⲃыⲇⲉⲣⲯⲕⲁ, ⲕⲁⲕ ⲩ ⲣⲧⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲃⲟⲧ ⲥⲙⲟⲧⲣυ,ⲧы ⲟⲇυⲏⲟⲕ, ⲃⲉⲇь ⲙⲟύ ⲭⲩύ ⲏⲉ ⳅⲁⲅⲗяⲇыⲃⲁⲉⲧ ⳝⲟⲗьⲱⲉ ⲃ ⲧⲃⲟύ ⲣⲟⲧ ⲏⲁ ⳡⲁύ,ⲧⲉⳝⲉ ⲅⲣⲩⲥⲧⲏⲟ, ⲃⲉⲇь ⲙⲟύ ⲭⲩύ ⲟⲕⲟⲏⳡυⲗ ⲟⲧⲏⲟⲱⲉⲏυⲉ ⲥ ⲧⲃⲟⲉύ ⲅⲩⳝⲟύ, ⲟⲏυ ⳝⲟⲗьⲱⲉ ⲏⲉ ⲡⲁⲣⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⲱⲗυ ⲏⲁ ⲙⲟⲏⲉⲧⲏыύ ⲇⲃⲟⲣ,ⲧы ⲩⳅⲏⲁⲉⲱь ⳅⲁ ⳡⲧⲟ ⲡⲟⲕⲩⲡⲁюⲧ ⲧⲃⲟю ⲙⲁⲧь, ⲡⲣⲟⲥⲧυ,я ⲏⲉ ⲭⲟⲧⲉⲗ ⲧⲉⳝя ⲟⳝυⲇⲉⲧь, ⲏⲟ ⲣⲟⲧ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ,ⲕⲁⲕ ⲡⲣⲟⲭⲟⲇⲏⲟύ ⲇⲃⲟⲣ, ⲏⲩ ⲭⲩυ ⳡⲁⲥⲧⲟ ⳅⲁⲅⲗяⲇыⲃⲁюⲧ ⲏⲁ ⳡⲁύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲇⲟⲡⲩⲥⲧυⲙ,я ⲃыⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲧь,ⲁ ⲇⲁⲗьⲱⲉ ⳡⲧⲟ?) я ⲯⲉ ⳝⲣⲟⲱⲩ ⲉё, ⲟⲏⲁ ⲭⲩⲉⲧⲁ ⳝⲗя, я ⲏⲉ ⳝⲩⲇⲩ ⲥ ⲏⲉύ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⳝⲗя, ⳡⲩⲃⲁⲕ, ⲕⲁⲕ ⳝы ⲥⲕⲁⳅⲁⲧь ⲙяⲅⳡⲉ, ⲏⲩ ⲉⳝⲁⲗ я ⲧⲃⲟю ⲙⲁⲧь,υ ⳡⲟ?) ⲥⲕⲁⲏⲇⲁⲗ ⳅⲁⲃⲟⲇυⲧь? ) ⲏⲁⲭⲩύ ⲥⲧⲟⲗьⲕⲟ ⲱⲩⲙⲁ ⲡⲟⲇⲏυⲙⲁⲧь υⳅ ⳅⲁ ⲧⲟⲅⲟ, ⳡⲧⲟ я ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲃⲟⲧ ⲥⲙⲟⲧⲣυ,ⲥⲉύⳡⲁⲥ я ⳝⲩⲇⲩ ⲇⲁⲃⲁⲧь ⲭⲩⲉⲙ ⲧⲃⲟю ⲙⲁⲧь,ⲕⲁⲕ ⳝⲩⲗьⲇⲟⳅⲉⲣ,ⳝⲗя)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲥυⲭυⳡⲉⲥⲕυ ⳝⲟⲗⲉⲏ?) ⲥⲧⲁⲃυⲱь ⲥⲃⲟё ⲟⳡⲕⲟ ⲡⲉⲣⲉⲇ ⲏⲉⲅⲣⲟⲙ ⳝⲟⲗⲉюⳃυⲙ эⳝⲟⲗⲟύ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡυⳅⲇⲉц, ⲧы ⲏⲉⲅⲣⲉⲧⲉⲏⲟⲕ ⲥ ⲕⲁⲙⲉⲣⲩⲏⲁ ⲕⲟⲧⲟⲣыύ ⲥⲧⲣⲟυⲧ υⳅ ⲥⲉⳝя ⳝⲉⲗⲟⲅⲟ, ⲧы ⳅⲁⲡⲩⲧⲁⲗⲥя ⲃ ⲣⲁⲥⲉ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲙⲟⲧⲣυ, ⲙⲟύ ⲭⲩύ ⲟⲧⲕⲣыⲗ ⲕⲟⲗⲗⲉⲇⲯ ⲡⲟ ⲟⳝⲩⳡⲉⲏυю ⲙⲁⲙⲁⲱⲉⲕ ⲡⲣⲣⲥⲧυⲧⲩцυυ, ⲡⲟⳡⲉⲙⲩ ⲧⲃⲟя ⲙⲁⲧь ⲡⲉⲣⲃыύ ⲁⳝυⲧⲩⲣυⲉⲏⲧ? ) ⲟⲏⲁ ⲥⲕⲗⲟⲏяⲉⲧⲥя ⲕ ⲱⲗюⲭυⲏυⳅⲙⲩ υ ⲣⲁⲕⲟⲃⲁⲏυю? ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡυⳅⲇⲉц ⲟⲏⲁ ⲡⲩⳅⲁⲧⲁя ⲙыⲙⲣⲁ ⲥ ⲧⲉⲣⲡⲕυⲙ ⲁⲣⲟⲙⲁⲧⲟⲙ ⲃⲁⳅυⲗυⲏⲁ ⲟⲧ ⲟⳡⲕⲁ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲙⲟⲧⲣυ, ⲃⲟⲧ ⲧы ⲯⲉ ⲡⲟⲗⲩⳡυⲱь ⲧⲣυ ⲏⲟⲯⲉⲃыⲭ ⲃ ⲅⲟⲣⲗⲟ υⳅ ⳅⲁ υⳅⲏⲁⲥυⲗⲟⲃⲁⲏυя ⲥⲃⲟⲉύ ⲣⲩⲕυ υ ⲅⲩⳝы,ⲇⲩⲣⲁⳡⲟⲕ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲃⲟⲧ ⲥⲙⲟⲧⲣυ, ⲧⲃⲟя ⲙⲁⲧь ⲕⲩⲡυⲗⲁ ⲁⳝⲟⲏυⲙⲉⲏⲧ ⲃ ⲙⲁⲥⲥⲁⲯⲏⲩю ⲕⲗυⲏυⲕⲩ, ⳡⲧⲟⳝ ⲡⲟⲥⲁⲥыⲃⲁⲧь ⲧⲁⲙ ⲃⲥⲉⲙ ⲭⲩυ,ⲡυⳅⲇⲉц, ⲭⲟⲇυⲧ ⲙⲁⲥⲥⲁⲯυⲣⲟⲃⲁⲧь ⲭⲩύ υ ⲅⲩⳝы) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡυⳅⲇⲉц, ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲡⲟⳅⲃⲟⲏυⲗⲁ υ ⲥⲕⲁⳅⲁⲗⲁ  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲁⳝⲟⲏⲉⲏⲧ ⲃⲣⲉⲙⲉⲏⲏⲟ ⲏⲉ ⲙⲟⲯⲉⲧ ⲟⲧⲥⲟⲥⲁⲧь ⲃⲁⲙ ⲭⲩύ, ⲟⲏ ⲡⲣυⲉⲇⲉⲧ ⲡⲟⳅⲯⲉ ). я ⲁⲯ ⲁⲭⲩⲉⲗ, ⲙⲏⲉ ⲃⲡⲉⲣⲃыⲉ ⲧⲁⲕ ⲥⲣⲁⳅⲩ ⲡⲣⲉⲇⲗⲟⲯυⲗⲁ ⲟⲧⲥⲟⲥ ⳝⲁⳝⲁ ⲕⲟⲧⲟⲣⲩю ⲏυⲕⲟⲅⲇⲁ ⲏⲉ ⲃυⲇⲉⲗ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲃⲟⲧ ⳡⲧⲟ ⲧы ⲃⳡⲉⲣⲁ ⲃυⲇⲉⲗ ⳅⲁ ⲩⲅⲗⲟⲙ ⲇⲟⲙⲁ?) ⲕⲁⲕ я ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь?) ⲃ эⲧⲟⲙ ⲏυⳡⲉⲅⲟ ⲏⲉⲧ,ⲩ ⲏⲉё ⳝⲉⲱⲉⲏⲥⲧⲃⲟ ⲙⲁⲧⲕυ υ яⳅыⲕⲁ, ⳝыⲃⲁⲉⲧ ⲧⲁⲕⲟⲉ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲟύ ⲭⲩύ ⲟⲥⲧⲁⲃυⲗ ⲃⲡⲉⳡⲁⲧⲗⲉⲏυⲉ ⲧⲃⲟⲉύ ⲅⲩⳝⲉ? ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲟⲏ ⲉё ⲉⳝⲁⲗ,ⲕⲁⲕ ⲏυⲕⲧⲟ ⲏⲉ ⲉⳝⲁⲗ,ⲡⲣⲟⲥⲧⲟ ⲡⲟⲉⳝⲁⲗ,ⲕⲁⲕ ⳝⲟⲅ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲃⳡⲉⲣⲁ ⲙⲟύ ⲭⲩύ ⲃⳅяⲗ ⲧⲃⲟю ⲅⲩⳝⲩ ⲏⲁ ⲟⳝⲟⲣⲇⲁⲯ ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲡⲣяⳡⲉⲧⲥя ⲟⲧ ⲧⲃⲟⲉⲅⲟ ⳝⲁⲧυ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲕⲁⲕ ⲧⲟ ⲣⲁⳅ ⲃⲟⲱⲉⲗ ⲃ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ, υ ⲟⲭⲩⲉⲗ ⲟⲧ ⲧⲟⲅⲟ ⳡⲧⲟ ⲩ ⲏⲉⲉ ⲃ ⲡυⳅⲇⲁⲕⲉ ⲗⲁⲙⲡⲁⳡⲕⲁ ⲅⲟⲣⲉⲗⲁ ⲕⲁⲕ ⲡⲁяⲗьⲏυⲕ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲁⲃυⲗ ⲕⲩⳝυⲕ ⲣⲩⳝυⲕ υ ⲭⲩⲉⲙ ⲉⲅⲟ ⲥⲟⳝⲣⲁⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲯⲟⲡⲟύ ⲭⲣⲟⲙⲁⲉⲱь ⲕⲁⲕ υⲏⲃⲁⲗυⲇ ⲉⳝⲁⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲭⲩⲉⲙ ⲧⲉⳝⲉ ⲉⳝⲗⲟ ⲡⲟⲕⲣⲁⲱⲩ ⲕⲁⲕ ⲧяⲏⲕυ ⲕⲁⲥⲙⲉⲧυⲕⲟύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲡⲣⲟⲧⲕⲏⲩ ⲕⲁⲕ ⲱⲁⲣ , υ ⲟⲏⲁ ⲗⲟⲡⲏⲉⲧ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲥⲗⲉ ⲙⲟⲉⲅⲟ ⲭⲩя ⲥⲩⲇьⳝⲩ υⳅⲙⲉⲏυⲗ, ⲃ ⲏⲟⲣⲙⲁⲗьⲏⲟⲉ ⲣⲩⲥⲗⲟ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⲧυⲕⲁⲉⲱь ⲕⲁⲕ ⲟⲧ ⲃⲉⲧⲣⲁ, ⲏⲩ эⲧⲟ ⳝⲉⲥⲡⲟⲗⲉⳅⲏⲟ ,ⲥⲙυⲣυⲥь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲟύ ⲭⲩύ ⲧⲉⳝя ⲡυⳅⲇυⲗ ⲧⲁⲕ ⲯⲉ ⲯⲉⲥⲧⲕⲟ ⲕⲁⲕ ⲡⲗⲉⲧⲕⲟύ ⲃ ⲥⲧⲁⲣыⲉ ⳝыⲗыⲉ ⲃⲣⲉⲙⲉⲏⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲥ ⲙⲟⲉⲅⲟ ⲭⲩя ⲣⲟⲧ ⲥⲃⲟύ ⲩⲏⲉⲥⲧυ ⲏⲉ ⲙⲟⲯⲉⲱь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲩⲭⲟⲇυⲱь ⲡⲟ ⲁⲏⲅⲗυύⲥⲕυ, ⲡⲟⲥⲗⲉ ⲟⲧⲥⲟⲥⲁ ⲇⲃⲉⲣь ⳅⲁ ⲥⲟⳝⲟύ ⳅⲁⲕⲣыⲃⲁⲉⲱь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟю ⲙⲁⲧь ⲧⲁⲕ ⲣⲉⳅⲕⲟ ⲉⳝⲁⲗ ⳡⲧⲟ ⲩ ⲏⲉⲉ ⲡυⳅⲇⲁⲕ ⲇыⲙⲕⲟⲙ ⲡⲟⲡⲁⲭυⲃⲁⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲡⲣыⲅⲁⲉⲱь ⲥⲃⲟⲉύ ⲡυⳅⲇⲟύ ⲕⲁⲕ ⲃⲁⲯⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲭⲟⳡⲉⲱь ⳝⲣⲁⲥⲗⲉⲧ ⲥⲉⳝⲉ ⲏⲁ ⲣⲩⲕⲩ ⲃⲃυⲇⲉ ⲙⲟⲉⲅⲟ ⲭⲩя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲧⲩⲥυⲱьⲥя ⲟⳡⲕⲟⲙ ⲥⲃⲟυⲙ ⲕⲁⲕ ⲇⲟⲙ ⲡⲣυ ⲃⳅⲣыⲃⲉ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲗⲟⲯυⲗ ⲩ ⲡⲁⲇυⲕⲁ ⲕⲁⲕ ⲕⲟⲃⲣυⲕ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲟύ ⲭⲩύ ⲧⲉⳝя υⳅ ⲡⲟⲇ ⳅⲉⲙⲗυ  ⲇⲟⲥⲧⲁⲗ υ ⲟⲧъⲉⳝⲁⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲉⳝя ⲭⲩⲉⲙ ⲧυⲥⲕⲁю ⲕⲁⲕ ⲇⲉⲧυ ⲡⲗюⲱⲉⲃыⲉ υⲅⲣⲩⲱⲕυ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟю ⲙⲁⲧь ⲃ ⲡⲁⲇυⲕⲉ ⲏⲁ ⲡⲉⲣυⲗⲁⲭ ⲉⳝⲁⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲟύ ⲭⲩύ ⲃ ⲧⲉⳝя ⲃⲟⲱⲉⲗ, ⲩ ⲧⲉⳝя ⲁⲯ ⲏⲁ ⲗⲟⳝⲕⲉ ⲃⲟⲗⲟⲥы ⲃⲥⲧⲁⲗυ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲙⲟύ ⲭⲩύ υⲥⲕⲁⲗ ⲃ ⲡυⳅⲇⲉ ⲥⲃⲟⲉύ ⲙⲁⲙⲕυ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⳅⲁ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲩⲭⲁⲯυⲃⲁⲉⲱь ⲕⲁⲕ ⲅⲟⲣⲏυⳡⲏⲁя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲯⲁⲣυⲗ ⲕⲁⲕ яυⲱⲏυцⲩ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲃ 1945 ⳝыⲗⲁ ⲡⲣυⲏяⲧⲁ ⲇυⲕⲗⲟⲣⲁцυя ⲟ ⲡⲟⲥυⳃⲉⲏυⲉ ⲧⲃⲟⲉⲅⲟ ⲣⲧⲁ ⲏⲁ ⲙⲟύ ⲭⲩύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲙⲩⲥⲟⲣⲕⲩ ⲕυⲏⲩⲗ, ⲟⲏ ⲩⲯⲉ ⲏⲉ ⲅⲟⲇⲉⲏ ⲇⲗя ⲉⳝⲗυ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲏⲉⲙⲟⲯⲉⲱь ⳅⲁⳝыⲧь ⲙⲟύ ⳡⲗⲉⲏ, ⲕⲁⲕ ⲇⲉⲃⲩⲱⲕυ ⲡⲉⲣⲃыύ ⲡⲟцⲉⲗⲩύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя ⲥⲟ ⲥⲃⲟⲉⲅⲟ ⲧⲁⳝⲟⲣⲁ ⲕⲟⲏя ⲥⲡυⳅⲇυⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡыⲧⲁⲗⲥя ⲙⲟⲉⲙⲩ ⲭⲩю ⲟⲧⲥⲟⲥⲁⲧь, ⲏⲩ ⲟⲏ ⲧⲉⳝⲉ ⲟⲧⲃⲉⳡⲁⲗ "ⲁⳝⲁⲏⲉⲏⲧ ⲃⲣⲉⲙⲉⲏⲏⲟ ⲏⲉ ⲇⲟⲥⲧⲩⲡυⲏ" ⲏⲩ ⲡⲣⲟⲥⲧⲟ ⲧⲃⲟύ ⲣⲟⲧ ⳅⲁⲉⳝⲁⲗ ⲉⲅⲟ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁ ⲃⲥⲁⲗⲕⲩ ⲡⲟⲣⲁ ⲟⲧⲡⲣⲁⲃⲗяⲧь, ⲧⲁⲙ ⲩⲯⲉ ⲕⲁⲣыⲧⲟ ⲕⲁⲕⲟⲉ ⲉⲧⲟ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧⲣⲩⲥы ⲥⲩⲱυⲧь ⳃⲁⲥ ⳝⲩⲇⲩ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲭⲩⲉⲙ ⲡⲣⲟⲇыⲣяⲃυⲗ ⲧⲉⳝя ⲧⲁⲕ, ⳡⲧⲟ ⲧы ⲥⲧⲁⲗ ⲕⲁⲕ ⲧⲣяⲡⲕⲁ ⲡⲟⲗⲟⲃⲁя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲁⲭⲩύ ⲧы ⲙⲏⲉ ⲃ ⲭⲩύ ⲟⲣⲁⲗ , ⲕⲟⲅⲇⲁ ⲟⲏ ⲧⲉⳝя ⲱⲃыⲣⲏⲩⲗ ⳡⲉⲣⲉⳅ ⳅⲁⳝⲟⲣ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲙⲟⲉⲙⲩ ⲭⲩю ⲡыⲧⲁⲗⲥя ⲏⲁⲭⲟⲙυⲧь υ ⲡⲟⲗⲩⳡυⲗⲟⲥь ⲧⲁⲕ ⳡⲧⲟ я ⲧⲃⲟύ ⲣⲟⲧ ⲟⲧъⲉⳝⲁⲗ υ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲃ ⳅⲁⲥⲟⲥ ⲡыⲧⲁⲗⲥя ⲙⲟю ⳅⲁⲗⲩⲡⲩ ⲃⲥⲟⲥⲁⲧь ⲡⲟⲙⲏυⲱь?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡυⳅⲇⲩ ⲥⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧⲉⲣⲉⳝⲉⲱь ⲕⲁⲕ ⲅⲣⲁⳡ ⲉⳝⲁⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⳅⲁ ⲙⲟυⲙ ⲭⲩⲉⲙ ⳝⲉⲅⲁⲉⲱь ⲧⲟⲗьⲕⲟ ⲡяⲧⲕυ ⲥⲃⲉⲣⲕⲁюⲧ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲭⲩⲉⲙ ⲡⲟⲇⲯⲉⲅ ⲧⲃⲟύ ⲡυⳅⲇⲁⲕ υ ⲡⲟⲗⲩⳡυⲗⲁⲥь ⲅⲣυⲗь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲭⲩύ ⲕυⲏⲩⲗ ⲟⲏⲁ υ ⲥⲗⲟⲙⲁⲗⲁⲥь ⲕⲁⲕ ⲡυⲣυⲗυⲏⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲃ ⲕⲁⳡⲉⲥⲧⲃⲉ ⲕυⲥⲧⲟⳡⲕυ ⲏⲁ υⳅⲟ ⲃ ⲱⲕⲟⲗⲉ υⲥⲡⲟⲗьⳅⲟⲃⲁⲗ ⲙⲟύ ⲭⲩύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲙⲏⲉ ⲥⲟⲥⲁⲗ ⲧⲁⲕ ⲇⲟⲗⲅⲟ ⳡⲧⲟ ⲩ ⲧⲉⳝя ⲫⲗюⲥ ⲃыⲥⲕⲟⳡυⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲣⲧⲟⲱⲕⲩ ⲥⲁⲯⲁⲧь ⳃⲁⲥ ⳝⲩⲇⲩ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲙⲟύ ⲭⲩύ ⲟⳝⲏυⲙⲁⲉⲱь ⲕⲁⲕ ⲙⲁⲙⲕⲩ ⲥⲃⲟю) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲉⳝя ⲭⲩⲉⲙ ⲃыⳝυⲃⲁⲗ ⲕⲁⲕ ⲕⲟⲃⲣυⲕ ⲏⲁⲭⲩύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟύ ⲣⲟⲧ ⲕ ⲙⲟⲉⲙⲩ ⲭⲩю ⲡⲣυⲗυⲡ ⲕⲁⲕ ⲡυяⲃⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲯυⲣⲟⲙ ⲧⲟⲕ ⲧⲣяⲥⲉⲱь ⲁ ⲏⲉ ⲡυⳅⲇⲟύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲙⲏⲉ ⲥⲟⲥⲁⲗ ⲧⲁⲕ ⳡⲧⲟ ⲁⲯ ⲟⳝⲗⲁⲕⲁ ⲏⲁ ⲏⲉⳝⲉ ⲣⲁⳅⲟⲱⲗυⲥь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲥ ⲙⲟⲉⲅⲟ ⲭⲩя ⲥⲃⲟю ⲙⲁⲧь ⲣⲁⲥⲧⲣⲉⲗυⲃⲁⲗ ⲥⲡⲉⲣⲙⲟύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲣⲁⳅⲟⳝⲣⲁⲗ ⲏⲁ ⲙⲉⲧⲁⲗⲁⲗⲟⲙ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲟύ ⲭⲩύ ⲇⲗя ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲡⲣⲟⲃⲟⲇⲏυⲕ ⲃ ⲯυⳅⲏⲉ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲙⲟύ ⲭⲩύ ⲃⲟⳅⲇⲩⲱⲏыⲙυ ⲡⲟцⲉⲗⲩяⲙυ ⳅⲁцⲉⲡυⲧь ⲡыⲧⲁⲗⲥя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲏⲁ ⲡⲟⲥⲗⲉⲇⲟⲕ ⲙⲟύ ⳡⲗⲉⲏ ⲥⲟⲥⲁⲗ ⲕⲁⲕ ⲙⲁⲱυⲏⲁ ⲉⳝⲁⲏⲁя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟю ⲙⲁⲧь ⲭⲟⲧⲉⲗ ⲡⲟⲉⳝⲁⲧь ,ⲁ ⲟⲏⲁ υ ⲧⲁⲕ ⲩⲯⲉ ⲇыⲣяⲃⲁя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲥⲱυⲗ υⳅ ⲗⲟⳝⲕⲟⲃыⲭ ⲃⲟⲗⲟⲥⲕⲟⲃ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃⲁⲗⲉⲏⲕυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲡⲩⲥⲕⲟⲃⲁя ⲱⲁⲭⲧⲁ ⲇⲗя ⲙⲉⲯⲕⲟⲏⲧⲉⲏⲉⲏⲧⲁⲗьⲏыⲭ ⲣⲁⲕⲉⲧ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃяⳅь ⲗⲟⲃυⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲫυⲗьⲙ ⲥⲏυⲙⲁⲗ ⲃ ⲯⲁⲏⲣⲉ ⲣⲩⲥⲥⲕυύ ⲕⲁⲯⲩⲁⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲣⲉⲇⲟⲃⲣⲁⲧυⲗ ⲕⲁⲧⲟⲥⲧⲣⲁⲫυⳡⲉⲥⲕυύ ⲣⲁⳅⲗⲟⲙ υⲙⲡⲉⲣυυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟⲯⲉⲣⲧⲃⲟⲃⲁⲗ ⲃ ⲫⲟⲏⲇ ⲇⲗя ⲥⲡⲁⲥⲉⲏυя ⲕⲗυⲧⲟⲣⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟύ ⲭⲩύ ⲡⲩⲥⲧυⲗ ⳡⲉⲣⲉⳅ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲡⲟⲉⳅⲇⲉ ⲡⲟ ⲣⲉⲗьⲥⲁⲙ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟύ ⲭⲩύ ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⳝыⲗ ⲕⲁⲕ ⲃⲉⳃь ⲃ ⲅⲁⲣⲇυⲣⲟⳝⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ υⳅ ⲟⳡⲕⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲇⲟⳝыⲃⲁⲗ ⲇⲣⲁⲅⲟцⲉⲏⲏыⲉ ⲥⲁⲙⲟⲣⲟⲇⲕυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡⲟ ⲕⲗυⲧⲟⲣⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲩⲥⲧυⲗ цⲉⲡⲏⲩю ⲣυⲁⲕцυю υⳅ ⲧⲟⲕⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧⲁⳝⲗυцⲩ ⲭυⲙυⳡⲉⲥⲕυⲭ ⲃⲉⳃⲉⲥⲧⲃ ⳡⲉⲣⲧυⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲩⲗёⲅⲥя ⲏⲁ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υ ⲏⲁⳡⲉⲗ ⲥⳡυⲧⲁⲧь ⳅⲃёⳅⲇы υ ⲅⲗⲁⳅⲁⲙυ ⲥⲟⳝυⲣⲁⲧь ⲥⲟⳅⲃⲉⳅⲇυⲉ ⲟⲣυⲟⲏⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲃⲉⲇⲉⲧ ⲁⲣⲭυⲟⲗⲟⲅυⳡⲉⲥⲕυⲉ ⲣⲁⲥⲥⲕⲟⲡⲕυ ,ⲥⲕⲉⲗⲉⲧⲁ ⲇυⲏⲟⳅⲁⲃⲣⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲱⲁⲅⲏⲩⲗ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲃ ⲏⲟⲃⲟⲉ υⳅⲙⲉⲣⲉⲏυⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⲃⲟⳃⲁⲙυ ⲧⲟⲣⲩⲅю ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲡⲣυⲗⲁⲃⲕⲉ ⲥ ⲟⲃⲟⳃⲁⲙυ ⲃыⲉⳝⲁⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲡⲩⲥⲧⲩ ⲕⲃⲁⲥυⲗ ⲧⲉⳝⲉ ⲏⲁ ⳅυⲙⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲗⲟⳝⲕⲟⲃⲩю ⲕⲟⲥⲧь ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃ ⲡⲣⲟⲧυⲃⲟⲡⲟⲗⲟⲯⲏⲩю ⲥⲧⲟⲣⲟⲏⲩ ⲥⲙⲉⲥⲧυⲗ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь υⲡⲟⲗьⳅⲩⲉⲧ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲧяⲡⲕⲩ ⲏⲁ ⲟⲅⲟⲣⲟⲇⲉ ⲕⲟⲧⲟⲣⲟύ ⲟⲏⲁ ⲟⲕⲩⳡυⲃⲁⲉⲧ ⲕⲟⲣⲧⲟⲱⲕⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ υⲥⲡⲟⲗьⳅⲩⲉⲧ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲥⲡⲁⲗьⲏыύ ⲙⲉⲱⲟⲕ ⲃ ⲡⲟⲭⲟⲇⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲙⲏⲉ ⲃⲥю ⲡⲗⲉⲱ ⲡⲣⲟⲉⲗⲁ ⲕⲁⲕ ⲙⲟⲗь ⲉⳝⲁⲏⲁя ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲣⲟυⲗ ⲥⲧⲟяⲏⲕⲩ υ ⲡⲟⲧⲟⲙ ⲡⲟⲣⲕⲟⲃⲁⲗ ⲥⲃⲟύ ⲭⲩύ ⲏⲁ эⲗυⲧⲏⲟⲉ ⲙⲉⲥⲧⲟ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧⲣⲟυⲗ ⲡυⲣⲁⲙυⲇⲩ ⲭυⲟⲡⲥⲁ ⲧⲁ ⲏⲉ ⲩⲥⲧⲟяⲗⲁ υ ⲟⳝⲣⲩⲱυⲗⲁⲥь ⲡⲣяⲙ ⲏⲁ ⲡⲟⲗⲟⲃⲩю ⲅⲩⳝⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υⳅ ⳅⲁ ⲡⲗⲟⲭⲟύ ⲕⲟⲏⲥⲧⲣⲩⲕцυυ υ ⲩⲕⲗⲁⲇⲕυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲧⲃⲟю ⲙⲁⲧь ⲱυⲏⲧⲁⲯυⲣⲟⲃⲁⲗ ⲕⲁⲕ ⲃ ⲕⲣⲉⲙυⲏⲁⲗьⲏыⲭ ⲫυⲗьⲙⲁⲭ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲗⲉцⲉⲃⲩю ⳡⲁⲥⲧь ⲗⲟⳝⲕⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲏёⲥ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲇⲟυⲧ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲥυⲥьⲕⲩ ⲕⲟⲣⲟⲃⲉ,ⲭⲩⲉⲥⲟⲥ ⲧы ⲕⲟⲗⲭⲗⳅⲏыύ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡⲣⲟⲅⲏⲩⲗ ⲧⲃⲟю ⲙⲁⲧь ⲕⲁⲕ ⲭⲩⲉⲥⲟⲥⲕⲩ ⲥⲥⲁⲏⲏⲩю υ ⲡⲣⲟⲥⲧυⲧⲩⲧⲕⲩ ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲉύⳡⲁⲥ ⲡⲟ ⲥⲃⲟⲉⲙⲩ ⲭⲩю ⲡⲩⳃⲩ ⲕⲁⲕ ⲡⲟ ⲟⲥυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲕⲁⲕ ⲃ ⲅⲟⲗⲟⲇⲏыⲭ υⲅⲣⲁⲭ ⲡыⲧⲁⲉⲧⲥя ⲡⲉⲣⲉⲅⲣыⳅⲧь ⲙⲟύ ⲭⲩύ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧяⲅⲁю ⲕⲁⲕ ⲱⲧⲁⲏⲅⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲗⲟⲃⲩю ⲙⲁⲧⲕⲩ ⲁⲙⲡⲩⲧυⲣⲟⲃⲁⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲉύⳡⲁⲥ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲉⲙⲟⲏⲧυⲣⲟⲃⲁⲧь ⲏⲁⳡⲏⲩ ⲕⲁⲕ ⲁⲃⲧⲟⲥⲗⲉⲥⲁⲣь ⲃ ⲁⲃⲧⲟⲥⲉⲣⲃυⲥⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲃыⲉⳝⲁⲗ ⲃ ⲥⲧⲟύⲗⲉ ⲡⲟⲇ ⲉё ⲗюⳝυⲙыⲙ ⲏⲟⲙⲉⲣⲟⲙ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲏⲁⲕⲣыⲗ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲃⲟⲗⲏⲟύ цⲩⲏⲁⲙυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲕⲣⲁⲥυⲗ ⲃ ⲣⲁⲇⲩⲯⲏыύ цⲃⲉⲧ ⳡⲧⲟ ⳝы ⳝыⲗⲟ ⲃⲉⲥⲉⲗⲉⲉ ⲉⳝⲁⲧь ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υⳅⲩⲃⲉⳡⲉⲗ ⲕⲁⲕ ⲏⲟⲯⲟⲙ ⳡⲉⲗⲟⲃⲉⲕⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲧⲃⲟю ⲙⲁⲧь ⲙⲁⲧυⲃυⲣⲩⲉⲧ ⲕⲁⲕ ⲡⲥυⲭⲟⲗⲟⲅ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲁⲏⲁⲗьⲏⲟⲉ ⲟⲧⲃⲉⲣⲥⲧυⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧυⲙⲩⲗυⲣⲩю ⲕⲁⲕ ⲁⲏⲇⲣⲉⲏⲁⲗυⲏⲟⲙ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⳝⲉⳅ ⲙⲟⲉⲅⲟ ⲭⲩя ⲏⲉ ⲙⲟⲯⲉ ⲡⲣⲟⲯυⲧь υ ⲇⲏя ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲟⳝⲩⲥⲧⲣⲟυⲗ ⲕⲁⲕ ⲕⲟⲙⲏⲁⲧⲩ ⲃ ⲕⲃⲁⲣⲧυⲣⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲕⲁⲧⲁⲉⲧⲥя ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲕⲁⲕ ⲏⲁ ⲙⲁⲣⲱⲣⲩⲧⲕυ ⲧⲟⲗьⲕⲟ ⳅⲁ ⳝⲉⲥⲡⲗⲁⲧⲏыύ ⲡⲣⲟⲉⳅⲇ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲣⲟⲃⲟⲇυⲗ ⲟⲡυⲣⲁцυю ⲡⲟ ⲩⲇⲁⲗⲉⲏυю ⲧⲟⳡⲕυ ⳋ υⳅ ⲡⲟⲗⲟⲃⲟύ ⲙⲁⲧⲕυ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υ ⲃⲣⲟⲇⲉ ⳝы ⲃⲥё ⲡⲣⲟⲱⲗⲟ ⲟⲧⲗυⳡⲏⲟ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⳅⲁⲭⲟⲇυⲧ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲥⲩⲇⲏⲟ ⲏⲁ ⲡⲣυⲥⲧⲁⲏь ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲟⲯⲁⲗ ⲥⲃⲟύ ⲭⲩύ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲏⲁ ⲁэⲣⲟⲫⲗⲟⲧ υⲥⲧⲣυⳝυⲧⲉⲗя ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υⲥⲡⲟⲗьⳅⲩю ⲕⲁⲕ ⲕⲩⲗёⲕ ⲇⲗя ⲥⲉⲙⲉⳡⲉⲕ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲱⲟⲗ ⲟⲥⲧⲁⲧⲕυ ⲯυⲃⲟύ ⲡⲗⲟⲧυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃыⲃⲉⲣⲏⲩⲗ ⲕⲁⲕ ⲕⲩⲣⲧⲩ υ ⲡⲟⲃⲉⲱⲁⲗ ⲏⲁ ⲃⲉⲱⲁⲗⲕⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡыⲧⲁⲗⲥя ⲏⲁ ⲟⳡⲕⲉ ⲃыⳝυⲧь ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲅⲣⲁⲃυⲣⲟⲃⲕⲩ ⲕⲁⲕ ⲕⲟⲗⲟⲙ ⲏⲁ ⲕⲁⲙⲏⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟύ ⲭⲩύ ⲟⳝ ⲕⲣⲁύ ⲕⲗυⲧⲟⲣⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧⲟⳡυⲗ ⲕⲁⲕ ⲟⳝ ⳅⲁⲟⲥⲧⲣёⲏыύ ⲕⲁⲙⲉⲏь ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲥⲃⲁⲗυⲗⲁⲥь ⲏⲁ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲡⲁⲇⲱυύ ⲁⲏⲅⲉⲗ ⲥ ⲏⲉⳝⲉⲥ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲅυⲇⲣⲁⲃⲗυⲕⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲁⲇυⲗ υ ⳅⲁⲧⲁⲏυⲣⲟⲃⲁⲗ ⲉё ⲟⳡⲕⲟ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲕⲟⲅⲇⲁ ⲙⲟύ ⲭⲩύ ⲱⲗυⲫⲟⲃⲁⲗ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧⲟ ⲟⲏ ⲥⲧёⲣ ⲕⲟⲗⲟⲇⲕυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁ ⲗⲟⲇⲕⲉ ⲡⲗⲁⲃⲁⲉⲧ ⲃ ⲏⲉύⲧⲣⲁⲗьⲏы ⲃⲟⲇⲁⲭ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲟⲗⲟⲇⲩ ⲕⲁⲣⲧ ⲃⲉⲉⲣⲟⲙ ⲣⲁⳅⲗⲟⲯυⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲟюⲥь ⲕⲁⲕ ⲅⲣⲉⳝⲏυⲕ ⲃ ⲏⲟⲣⲕⲉ ⲃ ⲏⲁⲇⲉⲯⲉⲇⲉ ⳡⲧⲟ ⲧⲁⲙ ⳝⲩⲇⲉⲧ ⲁⲭⲩⲉⲏыύ ⲅⲣυⳝ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲥⲟⲃⲙⲉⲥⲧⲏⲟⲉ ⲃυⲇⲉⲟ ⲥ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣью ⲙⲁⲏⲧυⲣⲟⲃⲁⲗ ⳡⲉⲣⲉⳅ ⲡⲣⲟⲅⲣⲁⲙⲙⲩ ⲋⲟⲛⲩ ⳳⲉⳋⲁⲋ 12 ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲫⲟⲧⲁⲗ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲡⲟⲡⲁⲣⲁцυύ ⲃ ⲕⲩⲣⲟⲣⲧⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⳡⲉⲣⲉⲡⲏⲟύ ⲕⲟⲣⲟⳝⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲇⲉⲗⲁⲗ ⲡⲟⲧⲟⲗⲟⲅυю ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲃёⲗ ⲕⲁⲕ ⲡⲟⲗⲟⲥⲙⲁⲥⲟⲃⲩю υⲅⲣⲩⲱⲕⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⳝⲉⲧⲟⲏυⲣⲟⲃⲁⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧⲉⲏⲕⲩ υⳅ ⲕυⲣⲡυⳡⲉύ ⲃыⲕⲗⲁⲇыⲃⲁⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟύ ⲭⲩύ ⲥⲗⲟⲯυⲗ ⲕⲁⲕ ⲡⲟⲗⲟⲧⲉⲏцⲉ υ ⲡⲟⲗⲟⲯυⲗ ⲃ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲃ ⲕⲁⳝυⲏⲕⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃⲥⲕⲣыⲗ ⲕⲁⲕ ⲕⲟⲏⲥⲉⲣⲃⲩ ⲥ ⲕυⲗьⲕⲟύ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧⲃⲟю ⲙⲁⲧь ⲟⲅⲗⲩⲱυⲗ ⲕⲁⲕ ⲣыⳝⲩ ⲃ ⲃⲟⲇⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲁⲏⲁⲗьⲏыⲙ ⲥⲏυⲕⲉⲣⲥⲟⲙ ⲏⲁⲕⲟⲣⲙυⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲡⲣυ ⲃыⲥⲟⲕυⲭ ⲩⲣⲟⲃⲏяⲭ ⲅⲣⲁⲃυⲧⲁцυυ ⲉⳝⲁⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲱⲟⲗ ⳅⲁⳝⲣⲟⲱⲉⲏыⲉ ⲡⲣⲟэⲕⲧы ⲁⲣⲣⳑⲉ υ ⲡⲣⲟⲇⲁⲗ υⲭ ⳅⲁ ⲁⲕцυυ ⲃ ⲏⲁύⲕⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲡⲣⲉⲯⲇⲉ ⳡⲉⲙ υⳅⲅⲟⲏяⲧь ⲇьяⲃⲟⲗⲟ υⳅ ⲕⲗυⲧⲟⲣⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⳡⲉⲣⲧυⲗⲁ ⲡⲉⲏⲧⲁⲅⲣⲁⲙⲙⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲕⲣⲁⲥυⲗⲁ ⲥⲃⲟυⲙ ⲡⲟⲗⲟⲃыⲉ ⲅⲩⳝы ⲙⲟⲉύ ⲥⲡⲉⲣⲙⲟύ ⲕⲁⲕ ⲡⲟⲙⲁⲇⲟύ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧⲟυⲧ ⲟⲡⲟⲣⲁ ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲅⲟⲣⲧⲁⲏь ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟύ ⲭⲩύ ⲥⲡⲩⲥⲕⲁⲗ ⲕⲁⲕ ⲱⲗⲁⲏⲅ ⲥ ⲗⲁⲙⲡⲟⳡⲕⲟύ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲏⲉ ⲏⲣⲁⲃυⲧⲥя ⲕⲟⲅⲇⲁ ⲧы υ ⲧⲃⲟя ⲙⲁⲧь ⲡⲟⲕⲗⲟⲏяⲉⲧⲥя ⲙⲟⲉⲙⲩ ⲭⲩю ⲯⲇя ⲇⲟⲯⲇя υⳅ ⲙⲟⲉύ ⲥⲡⲉⲣⲙы ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲅⲣⲁⲏυ ⲥⲙⲉⲣⲧυ ⲟⲧ ⲃыⲥⲧⲣⲉⲗⲁ ⲙⲟⲉύ ⲥⲡⲉⲣⲙы ⲃ ⲉё ⲉⳝⲗⲉⲧ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡυⳅⲇⲩ ⲥⲃⲟю ⲥⲧⲉⲗυⲱь ⲡⲟⲇ ⲇⲃⲉⲣυ ⲙⲟυ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲭⲩⲉⲙ ⲧⲉⳝⲉ ⲃ ⲗⲟⳝ ⳃⲁⲥ ⲡⲟⲥⲧⲩⳡⲩ ⲏⲁⲭⲩύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟю ⲙⲁⲧь ⳃⲁⲥ ⲏⲁ ⲭⲩύ ⲡⲟⲗⲟⲯⲩ ⲕⲁⲕ ⳝⲗυⲏ ⲉⳝⲁⲧь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕυ ⲙⲁⲕⲁⲣⲟⲏы ⲯⲁⲣυⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲏьⲕⲁⲙυ ⲕⲁⲧⲁⲗⲥя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⳡⲉⲣⲉⳅ ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲧⲉⳝя ⲕⲟⲣⲙυⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲃ ⲡυⳅⲇⲁⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲙⲩⲥⲟⲣ ⲭⲩⲉⲙ ⲃыⲧⲁⳃⲩ ⳃⲁⲥ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲭⲩύ ⲏⲁⲥⲁⲇυⲗ ⲕⲁⲕ ⲏⲁ ⲥⲧⲩⲗ ⲡⲟⲥⲁⲇυⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲃ ⲙⲟύ ⲭⲩύ ⲃⲉⲣυⲱь ⲕⲁⲕ ⲃ ⳡⲩⲇⲟ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲙⲟύ ⲭⲩύ ⲡыⲧⲁⲉⲱьⲥя ⲕⲩⲣυⲧь ⲕⲁⲕ ⲥυⲅⲩ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲡⲏⲩ ⲟⲏⲁ ⲃ ⲇⲉⲣⲉⲃⲟ ⲩⲉⳝⲉⲧⲥя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟю ⳃⲉⲕⲩ ⲭⲩⲉⲙ ⲡⲣⲟⲧⲕⲏⲩⲗ ⲕⲁⲕ ⲟⲣⲅⲁⲗυⲧ ⲉⳝⲁⲧь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲕⲁⲕ ⲫⲩⲧⳝⲟⲗьⲏыύ ⲙяⳡ, ⲙⲟύ ⲭⲩύ ⲧⲉⳝя ⲡυⲏⲁⲉⲧ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⳃⲁⲥ ⲃ ⲧⲃⲟⲉⲙ ⲡυⳅⲇⲁⲕⲉ ⲭⲩⲉⲙ ⲡⲟⲣяⲇⲟⲕ ⲏⲁⲃⲟⲇυⲧь ⳝⲩⲇⲩ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲃ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲙⲕⲉ ⲭⲩⲉⲙ ⳅⲁⲱⲉⲗ ⲕⲁⲕ ⳝⲁⲧьⲕⲁ ⲃ ⲇⲟⲙ ⲏⲁⲭⲩύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲏⲉ ⲧⲉⳝя ⲥ ⲭⲩя ⲥⲧⲣяⲭⲏⲩⲧь ⲕⲁⲕ ⲡⲉⲡⲉⲗ ⲥ ⲥυⲅⲁⲣⲉⲧы ⳡⲧⲟⲗⲉ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲩⲥⲡⲉⲃⲁⲗ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲉⳃⲉ ⲏⲁ ⲡⲉⲣⲉⲙⲉⲏⲁⲭ ⲃ ⲱⲕⲟⲗⲉ ⳃⲁ ⳃⲉⲕⲩ ⲥⲩⲏⲩⲧь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲏⲁ 23 ⲫⲉⲃⲣⲁⲗя ⳝⲩⲇⲉⲱь ⲥⲃⲟю ⲡυⳅⲇⲩ ⲕ ⲙⲟⲉⲙⲩ ⲭⲩю ⲡⲣυⲡⲟⲇⲏⲟⲥυⲧь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲗюⲇяⲙ ⲟⳝыⳡⲏⲟ ⲃ ⲙⲁⲉ ⲧⲉⲡⲗⲟ, ⲏⲩ ⲁ ⲧы ⲕ ⲁⲕ ⲡυⲇⲁⲣⲁⲥ ⲩ ⲙⲉⲏя ⲡⲟⲇ яύцⲁⲙυ ⲥυⲇυⲱь υ ⲅⲣⲉⲉⲱьⲥя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲉⳝⲉ ⳃⲁⲥ ⲕⲣⳡ ⲃ ⲩⲭⲟ ⲕⲟⲏⳡⲩ ⲥⲟ ⲣⲧⲁ ⲃыⲗьⲉⲧⲥя ⲕⲁⲕ ⳝυⲫυⲇⲟⲕ ⲏⲁⲭⲩύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕυ ⲡⲣⲁⲃⲗю ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲕⲁⲕ ⲗⲉⲏυⲏ ⲗⲉⲏυⲏⲅⲣⲁⲇⲟⲙ ⲃ 41 ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⳝⲗяⲧь ⲕ ⲙⲟⲉⲙ ⲭⲩю ⲥⲟ ⲃⲥⲉⲙ ⲥⲉⲣⲇцⲉⲙ ⲁ ⲟⲏ ⲏⲁ ⲧⲉⳝя ⲥⲥыⲧ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁ ⲏⲟⲃыύ ⲅⲟⲇ ⲃ ⲡυⳅⲇⲩ ⲁⲗⲉⲃьⲉⲭⲩ ⳅⲁⲕυⲏⲩⲗ υ ⲙⲉⲥυⲗ ⲉⳝⲗⲟⲙ ⲧⲃⲟυⲙ :ⲇ ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲏⲁⲭⲩύ ⲥⲃⲟⲉύ ⲡυⳅⲇⲟύ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲧⲁⲏⲉц ⳝⲟύцⲁ υⲥⲡⲣⲁⲃⲗяⲗ, ⲡυⲧⲩⲭ ⲉⳝⲁⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲙⲟύ ⲭⲩύ ⲕⲗюⲉⲧ, ⲡⲗⲁⲧⲃⲁ ⲉⳝⲁⲏⲁя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲏⲁ ⲙⲟύ  ⲭⲩύ ⲩⲉⳅⲯⲁⲉⲧ ⲡⲟⲇ ⲡⲉⲥⲏю " я ⲩⲉⲇⲩ ⲯυⲧь ⲃ ⲗⲟⲏⲇⲟⲏ"! ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟⲅⲣⲩⳅυⲗⲥя ⲃ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲃ ⲡⲟⲇⲃⲟⲇⲏⲩю ⲗⲟⲇⲕⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟύ ⲭⲩύ ⲡⲟⲗⲟⲯυⲗ ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲃ ⳝⲉⳅ ⲇⲟⲏⲏⲩю ⲗⲟⲇⲕⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧⲃⲟю ⲙⲁⲧь ⲡⲟⲇⲥⲧⲣⲉⲗυⲗ ⲕⲁⲕ υⳅ ⲇⲃⲩⲭ ⲕⲟⲗυⳝⲣυⲏⲟⲅⲟ ⲣⲩⲯья ⲏⲁ ⲟⲭⲟⲧⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲣⲁⳅⳝⲟⲙⳝυⲗ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲁⲣⲧυⲗⲗⲉⲣυύⲥⲕυυ ⲃⲟύⲥⲕⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ υⳅⲙⲉⲣяⲗ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲃⲁⲇⲣⲁⲧⲏыⲉ ⲙⲉⲧⲣы ⲇⲗя ⲥⲃⲟⲉⲅⲟ ⳅⲁⲅⲟⲣⲟⲇⲏⲟⲅⲟ ⲇⲟⲙⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⳝⲟⲗⲟⲏⳡυⲕⲟⲙ ⲕⲣⲁⲥⲕυ ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲣυⲥⲟⲃⲁⲗ ⲁⲏⲅⲗυύⲥⲕⲩю ⳝⲩⲕⲃⲩ "ⲣ" υ ⲡⲟⲥⲁⲇυⲗ ⲧⲩⲇⲁ ⲥⲃⲟύ ⲭⲩύ ⲕⲁⲕ ⲏⲁ ⲃⲉⲣⲧⲟⲗёⲧⲏⲩю ⲡⲗⲟⳃⲁⲇⲕⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲟⲏⲏⲩю ⲁⲣⲧⲉⲣυю ⲡⲉⲣⲉⲇⲁⲃυⲗ υ ⲟⲏⲁ ⲩⲡⲁⲗⲁ ⲃ ⲟⳝⲙⲟⲣⲟⲕ ⲟⳝⲗⲟⲕⲟⲧυⲃⲱυⲥь ⲏⲁ ⲙⲟύ ⲭⲩύ ⲥⲃⲟυ ⲣⲧⲟⲙ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲡⲣⲉⲉⲧ ⲕⲁⲕ ⲃ ⳝⲁⲏⲉ ⳅⲁⲅⲁⲣⲟⲇⲟⲙ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я υⳅ ⲕⲗυⲧⲟⲣⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲇⲉⲗⲁⲗ ⳅⲁⲅⲟⲧⲟⲃⲕⲩ ⲇⲗя ⲩⲣⲟⲕⲁ ⲧⲣⲩⲇⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ υⲥⲡⲣⲁⲃυⲗ ⲧⲉⲭⲏυⳡⲉⲥⲕⲩю ⲟⲱυⳝⲕⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡⲟ ⲕⲗυⲧⲟⲣⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲣⲟⲃёⲗ ⲕⲁⲕ ⲕⲟⲧ ⲭⲃⲟⲥⲧⲟⲙ ⲡⲟ ⲙⲟⲉύ ⲏⲟⲅⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟύ ⲭⲩύ ⳅⲁⲧⲁⳡυⲃⲁю ⲟⳝ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲕⲟⲡьё ⲃ ⲥⲣⲉⲇⲏⲉⲃυⲕⲟⲃьⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲟⲧ ⲩⲇⲁⲣⲁ ⲙⲟⲉⲅⲟ ⲭⲩя ⳝыⲗⲁ ⲡⲟⲇⲁⲃⲗυⲏⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲧⲁⲗ ⲣⲉⲕⲟⲣⲇⲥⲙⲉⲏⲟⲙ ⲡⲟ ⲙυⲧⲁⲏυю ⲥⲃⲟⲉⲅⲟ ⲭⲩя ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥ ⲇⲁⲗьⲏⲉύ ⲇυⲥⲧⲁⲏцυυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲏⲁ ⲗⲟⲇⲕⲉ ⲡⲣⲟⲡⲗы ⲡⲟ ⲕⲗυⲧⲟⲣⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲡⲟ ⲏⲉύⲧⲣⲁⲗьⲏыⲙ ⲃⲟⲇⲁⲙ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲇⲗя ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲗυⳡⲏⲁя ⲟⲭⲣⲁⲏⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲃ ⲧⲁⲏⲕⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲣⲟυⳅⲏⲟⲥυⲗ ⳅⲁⲕⲗυⲏⲁⲏυя ⳡⲧⲟ ⳝы ⲟⲧⲕⲣыⲧь ⲁⲏⲁⲗьⲏыⲉ ⲃⲟⲣⲟⲧⲁ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲅⲣⲁⳝⲏυцⲩ ⲭυⲟⲡⲥⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲡⲣⲉⲥⲟⲃⲁⲗ ⲕⲁⲕ ⳝⲁⲏⲕⲩ ⲯⲉⲗⲉⳅⲏⲩю ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲥⲉⲗυⲗ ⲡⲗⲉⲙя юⲏⲅυ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲟⲕⲩⲡυⲣⲟⲃⲁⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃыⲗⲟⲯυⲗ ⲙυⲏⲏⲟⲉ ⲡⲟⲗⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲣⲁⲏυⲗ ⲟⲣⲩⲇυя ⲙⲁⲥⲥⲟⲃⲟⲅⲟ ⲩⲏυⳡⲧⲟⲯⲉⲏυя ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲇⲉⲗⲁⲗ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲟⲧⲕⲣыύ ⲡⲉⲣⲉⲗⲟⲙ ⲕⲟⲗⲉⲏⲕυ ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲏⲁⲏёⲥ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲩⲃⲉⳡυя υ ⲩ ⲏⲉё ⲡⲟяⲃυⲗⲁⲥь ⲡⲟⲧⲟⲗⲟⲅυя ⲏⲁ ⳡⲉⲣⲉⲡⲏⲟύ ⲕⲟⲣⲟⳝⲕⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⳅⲁⲃёⲗ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲡⲟⲗⲟⲥⲙⲁⲥⲟⲃⲩю υⲅⲣⲩⲱⲕⲩ ⲏⲁ ⳝⲁⲧⲁⲣⲉύⲕⲁⲭ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲥⲕⲁⳡυⲧ ⲕⲁⲕ ⲕⲉⲏⲅⲩⲣⲩ ⲥ ⳅⲁⲣⲟⲇыⲱⲟⲙ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣ ⳅⲁⳝⲉⲧⲟⲏυⲣⲟⲃⲁⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲩⲕⲗⲁⲇыⲃⲁⲗ ⲕυⲣⲡυⳡυ ⲁ ⲙⲉⲥυⲗ ⳝⲉⲧⲟⲏ ⲃ ⲟⳡⲕⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃыⲡⲗⲁⳡυⲃⲁⲗ ⲕⲗυⲧⲟⲣⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲙⲡυⲏⲥⲁцυю ⳅⲁ ⲏⲁⲏⲉⲥёⲏыύ ⲩⳃⲉⲣⳝ ⲃⲏⲩⲧⲣυ ⲉⲅⲟ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲥⲃⲉⲣⲏⲩⲗ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⲡⲟⲗⲟⲧⲉⲏцⲉ ⲃ ⲣⲁⳅⲇυⲃⲁⲗⲕⲉ υ ⲡⲟⲗⲟⲯυⲗ ⲃ ⲕⲁⳝυⲏⲕⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲃⲥⲕⲣыⲗ ⲕⲁⲕ ⲕⲟⲏⲥⲉⲣⲃⲩ ⲥ ⲕυⲗьⲕⲟύ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲟⲅⲗⲩⲱυⲗ ⲕⲁⲕ ⲣыⳝⲩ ⲃ ⲃⲟⲇⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲁⲏⲁⲗьⲏыⲙ ⲥⲏυⲕⲉⲣⲥⲟⲙ ⲏⲁⲕⲟⲣⲙυⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃыⲡυⲗⲃⲁⲗ υⳅ ⲇⲉⲣⲉⲃⲁ ⲣⲁⲙⲕⲩ ⲇⲗя ⲥⲟⲃⲙⲉⲥⲧⲏⲟύ ⲫⲟⲧⲕυ ⲥ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣью ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲡⲣυ ⲃыⲥⲟⲕυⲭ ⲩⲣⲟⲃⲏяⲭ ⲅⲣⲁⲃυⲧⲁцυυ ⲉⳝⲁⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲟⳡⲕⲟ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲏⲁⲱⲟⲗ ⳅⲁⳝⲣⲟⲱⲉⲏыⲉ ⲡⲣⲟⲇⲩⲕцυυ ⲁⲣⲣⳑⲉ υ ⲡⲟⲧⲟⲙ ⲡⲣⲟⲇⲁⲗ υⲭ ⳅⲁ ⲁⲕцυυ ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲣυⲥⲟⲃⲁⲗ ⲡⲉⲏⲧⲁⲅⲣⲁⲙⲙⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲕⲣⲁⲥυⲗⲁ ⲥⲃⲟυ ⲡⲟⲗⲟⲃыⲉ ⲅⲩⳝы ⲙⲟⲉύ ⲥⲡⲉⲣⲙⲟύ ⲇⲩⲙⲁя ⳡⲧⲟ эⲧⲟ ⲅυⲅυⲉⲏυⳡⲉⲥⲕⲁя ⲡⲟⲙⲁⲇⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲃ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲧⲟυⲧ ⲟⲡⲟⲣⲁ ⲇⲗя ⲙⲟⲉⲅⲟ ⲭⲩя ⳡⲧⲟⳝы ⲟⲏ ⲏⲉ ⲡⲣⲟⲃⲁⲗυⲃⲁⲗⲥя ⲃ ⲅⲗⲩⳝь ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲗⲩⳝⲕυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲕⲁⲧⲁю υⳅ ⲏⲁⲃⲟⳅⲁ ⲕⲁⲕ ⲯⲩⲕ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲡⲣⲟⲭⲟⲇυⲗⲁ ⲡⲣⲟцⲉⲇⲩⲣⲩ ⲅⲇⲉ ⲏⲩⲯⲏⲟ ⳝыⲗⲟ ⲅⲗⲟⲧⲁⲧь ⲙⲟύ ⲭⲩύ ⲥ ⲗⲁⲙⲡⲟⳡⲕⲟύ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲏⲁ ⲟⳡⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧⲁⳝⲗυцⲩ ⲙⲉⲏⲇⲉⲗⲉⲉⲃⲁ ⲏⲁⲣυⲥⲟⲃⲁⲗ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲏⲉ ⲏⲣⲁⲃυⲧⲥя ⲕⲟⲅⲇⲁ ⲧы υ ⲧⲃⲟя ⲙⲁⲧь ⲡⲟⲕⲗⲟⲏяⲉⲧⲥя ⲙⲟⲉⲙⲩ ⲭⲩю ⲯⲇя ⲇⲟⲯⲇя υⳅ ⲙⲟⲉύ ⲥⲡⲉⲣⲙы ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲅⲣⲁⲏυ ⲥⲙⲉⲣⲧυ ⲟⲧ ⲃыⲥⲧⲣⲉⲗⲁ ⲙⲟⲉύ ⲥⲡⲉⲣⲙы ⲃ ⲉё ⲉⳝⲗⲉⲧ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲡыⲧⲁⲗⲁⲥь ⲡⲟⲃⲉⲱⲁⲧⲥя ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲕⲁⲕ ⲏⲁ ⲃⲉⲣⲉⲃⲕⲉ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲕⲁⲣⲁⳝⲕⲁⲗⲁⲥь ⲡⲟ ⲙⲟⲉⲙⲩ ⲭⲩю ⲕⲁⲕ ⲕⲟⲧ ⲡⲟ ⲇⲉⲣⲉⲃⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲃ ⲕⲗυⲧⲟⲣⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⳅⲃⲟⲇυⲗ ⲕⲟⲥⲧёⲣ ⲕⲁⲕ ⲇⲣⲉⲃⲏυύ ⳡⲉⲗⲟⲃⲉⲕ ⲃ ⳝыⲗыⲉ ⲃⲣⲉⲙⲉⲏⲁ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲏⲁ ⲥⲃⲟⲉⲙ ⲭⲩю ⲇⲟ ⲡⲟⲥёⲗⲕⲁ ⲥⲉύⳡⲁⲥ ⲡⲟⲃⲉⳅⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲟⲧⲡⲣⲁⲃυⲗⲁⲥь ⲏⲁ ⲙⲁⲣⲥ ⲕⲁⲕ ⲏⲁ ⲣⲁⲕⲉⲧⲉ ⲕⲟⲥⲙⲟⲏⲁⲫⲧ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲕⲗυⲧⲟⲣ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲥⲕⲣⲩⲧυⲗ ⲕⲁⲕ ⲯⲉⲗⲉⳅⲏⲩю ⳝⲁⲏⲕⲩ ?)  ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲏⲁ ⲏⲟⲃыύ ⲅⲟⲇ ⳝⲩⲇⲉⲱь ⲡυⲧь ⲙⲟю ⲙⲟⳡⲩ ⲇⲩⲙⲁя ⳡⲧⲟ эⲧⲟ ⲱⲁⲙⲡⲁⲏⲥⲕⲟⲉ??? ⲟⲗⲩⲭ ⲉⳝⲁⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲧⲁⲕ υⲥⲧⲉⲣυⲗ ⲏⲁ ⲙⲟύ ⲭⲩύ ⳡⲧⲟ ⲟⲏ ⲧⲉⳝⲉ ⲇⲉⲥⲏⲩ ⲩⲉⳝⲁⲗ ⳡⲧⲟ ⲧы ⲇⲁⲯⲉ ⲁⲭⲣυⲡ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲧⲉⳝⲉ ⲥⲩⲇьⳝⲩ ⲡⲟⲙⲉⲏяⲉⲧ, ⳝыⲗ ⲡυⲇⲁⲣⲁⲥⲟⲙ ⲥⲧⲁⲏⲉⲱь ⲙⲩⲯυⲕⲟⲙ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲕⲣⲩⲯυⲱьⲥя ⲡⲉⲣⲉⲇ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲕⲁⲕ ⲡⳡⲉⲗⲁ ⲉⳝⲁⲏⲁя υ ⲧⲟⲗьⲕⲟ ⲡⲟⲥⲗⲉ ⲕⲁⲕ ⲣⲁⳅ 20 ⲉⲅⲟ ⲟⳝⲗⲉⲧυⲱь ⲡⲟⲧⲟⲙ ⳅⲁⲡⲣыⲅⲏυⲱь υ ⲩⲥⲧⲣⲁυⲃⲁⲉⲱь ⲥⲕⲁⳡⲕυ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⳃⲁⲥ ⲧⲃⲟю ⲙⲁⲧь ⲃⲟⳅьⲙⲩ ⳅⲁ ⲃⲟⲗⲟⲥы υ ⲏⲁⳡⲏⲩ ⲭⲩяⲣυⲧь ⲉⲉ ⲭⲩⲉⲙ ⲃ ⲣⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь?) ⲉⳝⲁⲏⲁя ⲡⲟⲇⲥⲧυⲗⲕⲁ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲕⲁⲕ ⲕⲁⲣⲁⳝⲗь ⲧⲟⲏⲉⲱь ⲕⲟⲅⲇⲁ я ⲥⲥⲩ ⲏⲁ ⲧⲉⳝя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲉⳝⲉ ⲏⲟⲅυ ⲡⲉⲣⲉⲗⲟⲙⲁю ⲥⲃⲟυⲙ ⲭⲩⲉⲙ) υⲏⲃⲁⲗυⲇ ⲉⳝⲁⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟю ⲙⲁⲧь ⲡⲟⲥⲧⲉⲡⲉⲏⲏⲟ ⲉⳝⲩ, ⲡⲟⲕⲁ ⲙⲟύ ⲭⲩύ ⲏⲉ ⲡⲟⲅⲩⳝυⲧ ⲉⲉ ⲡυⳅⲇⲁⲕ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲕⲟⲅⲇⲁ я ⲧⲉⳝⲉ ⲃ ⲙⲁⲏⲕⲩ ⲕⲟⲏⳡⲁⲗ, υ ⲧы ⲭⲩяⲣυⲗ ⲉⲉ ⳅⲁ ⲙυⲗⲩю ⲇⲩⲱⲩ υ ⲇⲩⲙⲁⲗ ⳡⲧⲟ ⲧы ⲕⲁⲕ ⲕⲣⲉⲡыⲱ ⲙыⲱцы ⲏⲁⳝυⲣⲁⲉⲱь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲡⲟⲗυⲣⲩⲉⲧ ⲥⲃⲟύ ⲡυⳅⲇⲁⲕ ⲡⲉⲣⲉⲇ ⲉⳝⲗⲉύ ⲥⲟ ⲙⲏⲟύ υ ⲕυⲇⲁⲉⲧ ⲥⲉⳝⲉ ⲏⲁ ⲕⲗυⲧⲟⲣ ⳝⲗⲉⲥⲧⲕυ ⲧυⲡ ⲙⲁⲇⲉⲗь ⲉⳝⲁⲏⲁя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲡⲟ ⲡυⳅⲇⲁⲕⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲉⳝⲁⲱⲩ ⲕⲁⲕ ⲡⲟ ⳝⲁⲣⲁⳝⲁⲏⲩ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲡⲣⲟⲥυⲧ ⲉⲉ ⲙⲟⳡⲉύ ⲙⲟⲉύ ⲟⲕⲣⲉⲥⲧυⲧь ⲕⲁⲕ ⲥⲃяⲧⲟύ ⲃⲟⲇⲟύ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⲙⲏυⲱь ⲕⲟⲅⲇⲁ ⲧы ⲏⲉ ⲥⲗⲩⲱⲁⲗⲥя ⲙⲁⲙⲁⲱⲩ ⲥⲃⲟю ⲉⳝⲁⲏⲩю, υ ⲏⲉ ⲗⲟⲯυⲗⲥя ⲥⲡⲁⲧь ⲃⲟⲃⲣⲉⲙя я ⲡⲣυⲭⲟⲇυⲗ υ ⲃыⲣⲩⳝⲁⲗ ⲧⲉⳝя ⲭⲩⲉⲙ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲃ ⲁⲣⲙυю ⲡⲟύⲇⲉⲱь υ ⳝⲩⲇⲉⲱь ⲧⲁⲙ ⲥⲇⲁⲃⲁⲧь ⲏⲁⲣⲙⲁⲧυⲃы ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲡⲟ ⲗⳝⲩ ⲇⲁⲗ ,я ⲉύ ⲥⲣⲁⳅⲩ ⳡⲉⲣⲉⲡ ⲡⲣⲟⳝυⲗ υ ⲭⲩⲉⲙ ⲣⲉⳅⲕⲟ ⳅⲁⲱυⲗ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲙⲟύ ⲭⲩύ ⲫⲟⲧⲕⲁⲉⲧ υ ⲥⲧⲁⲃυⲧ ⲉⲅⲟ ⲃ ⲫⲟⲧⲕⲩ ⲙⲉⲥⲧⲟ ⲧⲃⲟⲉⲅⲟ ⲃыⲡⲩⲥⲕⲏⲟⲅⲟ ⲥ 11 ⲕⲗⲁⲥⲥⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ яⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲧⲁⲕ ⳝыⲥⲧⲣⲟ ⳡⲧⲟ ⲩ ⲏⲉⲉ ⲕⲗυⲧⲟⲣ ⲃыⲗⲉⲧⲉⲗ ⲕⲁⲕ ⲡⲩⲗя?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⳅⲁⲥⲧⲁⲃⲗяю ⲡⲣыⲅⲁⲧь ⲏⲁ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲇⲟⲗⳝⲁⲉⳝⲟⲃ ⲥⲟ ⲥⲕⲟⲗы?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲕⲟⲅⲇⲁ я ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲣⲁⲕ ⲅⲩⳝы ⲭⲩⲉⲙ ⲃыⲗⲉⳡυⲗ, ⲟⲏⲁ ⲃⲗюⳝυⲗⲁⲥь ⲃ ⲙⲟύ ⲭⲩύ , υ ⲕⲣⳡ ⲧⲉⲣь ⲙⲟύ ⲭⲩύ ⲙⲟⲯⲉⲱь ⲏⲁⳅыⲃⲁⲧь ⳝⲁⲧⲉύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲡⲟⲇ ⲃⲟⲇⲟύ ⲇⲁⲯⲉ ⲙⲏⲉ ⲥⲟⲥⲁⲗ, ⲕⲁⲣⲁⲥь ⲉⳝⲁⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲩ ⲧⲉⳝя ⲯⲉ ⲉⳃⲉ ⲇⲟ ⲥυⲭ ⲡⲟⲣ ⳡⲩⲃⲥⲧⲃⲁ ⲏⲉ ⲟⲥⲧыⲗυ ⲕ ⲙⲟⲉⲙⲩ ⲭⲩю я ⲡⲣⲁⲃ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱь ⲡυⲇⲁⲣⲁⲥ) ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲧⲣⲩⲥⲁⲙυ ⲗⲟⲃυⲧь ⳝⲩⲇⲩ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲉⳝⲉ ⲥⲉⲣⲇцⲉ ⲭⲩⲉⲙ ⲣⲁⳅⲟⳝью ⲕⲁⲕ ⲥⲧⲉⲕⲗⲟ ⲟⲧⲃⲉⳡⲁю) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱь ⲧы ⲏⲁⲭⲩύ ⲥⲃⲟю ⲙⲁⲧь ⲣⲁⳅⲗюⳝυⲗ ⲁ ⲙⲟύ ⲭⲩύ ⲡⲟⲗюⳝυ , ⲡⲣυⲇⲩⲣⲟⲕ ⲉⳝⲁⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲕⲣⳡ ⳡⲉⲧ ⲥⲏⲁⳡⲁⲗⲟ ⳅⲁⲯυⲅⲁⲉⲱьⲥя ⲕⲁⲕ ⲥⲡυⳡⲕⲁ ⳝⲗяⲧь , ⲁ ⲡⲟⲧⲟⲙ ⲅⲁⲥⲏⲉⲱь ⲕⲁⲕ ⲥⲃⲉⳡⲁ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲉ ⲏⲩ ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲧⲁⲕⲁя ⲟⳝυⲯⲉⲏⲏⲁя, ⲟⲏⲁ яⲃⲏⲟ ⳅⳝⲥ ⲃ ⲯⲟⲡⲩ ⲇⲁⲉⲧ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲭⲩⲉⲙ ⲣⲁⲥⲡυⲥыⲃⲁⲗⲥя ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱь ⲡυⲇⲁⲣⲁⲥ ⲉⳝⲁⲏыύ, ⲧы ⲏⲁⲭⲩύ ⲙⲟύ ⳡⲗⲉⲏ ⲡⲣυ ⲃⲥⲧⲣⲉⳡⲉ цⲉⲗⲩⲉⲱь ⲃ ⳅⲁⲥⲟⲥ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱь ⲇⲟⲗⳝⲁⲉⳝ ⲉⳝⲁⲏыύ, ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲡⲟ ⲙⲟⲉⲙⲩ ⲭⲩю ⲡⲟⲗⳅⲁⲉⲱь ⲕⲁⲕ ⲡⲟ ⲕⲁⲏⲁⲧⲩ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲏⲁ ⲙⲟύ ⲭⲩύ ⲥⲁⲇυⲱьⲥя υ ⲗⲉⲧⲁⲉⲱь ⲥⲃⲟυⲙ ⲡυⳅⲇⲁⲕⲟⲙ ⲏⲁ ⲏⲉⲙ ⲕⲁⲕ ⲃⲉⲣⲧⲁⲗⲉⲧ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲯⲉ ⲙⲁⲧь ⲙⲟύ ⳡⲗⲉⲏ ⲗюⳝυⲧ,  ⲕⲁⲕ ⲥⲟⲗⲏцⲉ ⲗюⳝυⲧ ⳅⲁⲕⲁⲧ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲧь ⲟⲧⲟ ⲃⲥⲉⲭ ⲩⳝⲉⲯⲁⲗⲁ ⲕ ⲙⲟⲉⲙⲩ ⲭⲩю) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲡⲉⲣⲉⲉⳅⲯⲁⲉⲧ ⲕⲁⲕ ⲏⲁ ⲏⲟⲃⲩю ⲕⲃⲁⲣⲧυⲣⲩ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ цⲉⲗыύ ⲁⲗьⳝⲟⲙ ⲡⲉⲥⲉⲏ ⲡⲟⲥⲃяⲧυⲗⲁ ⲙⲟⲉⲙⲩ ⲭⲩю) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟύ ⲯⲉ ⲡⲣⲟⳝυⲧыύ ⲣⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя ⲩⲯⲉ ⲇⲁⲃⲏⲟ ⲏⲉ ⲇⲟⲥⲧⲟυⲏ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲩⲥυⲗυя ⲡⲣυⲕⲗⲁⲇыⲃⲁⲉⲱь ⲕ ⲧⲟⲙⲩ ⳡⲧⲟⳝ ⲙⲟύ ⳡⲗⲉⲏ ⲟⲧⲥⲟⲥⲁⲧь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲧь ⲙⲟύ ⲭⲩύ ⲡыⲧⲁⲉⲧⲥя ⲗⲟⲃυⲧь, ⲕⲁⲕ ⲣⲉⳝⲉⲏⲟⲕ ⲗⲉⲧⲩⳡⲉⲅⲟ ⳅⲙⲉя ⲃ ⲇⲉⲧⲥⲧⲃⲉ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟю ⲙⲁⲧь ⲙⲟⲅⲩ ⳃⲁⲥ ⲡⲟⲉⳝⲁⲧь ⲡⲣⲟⲙⲉⲯ ⲥυⲥυⲕ ⲉⲉ ⲧⲩⲭⲗыⲭ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⲡⲣⲟⲅⲏⲩⲗ ⲕⲁⲕ ⲁⲗюⲙυⲏь ⲉⳝⲁⲧь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲥⲕⲁⳡⲉⲱь ⲕⲁⲕ ⲁⲏⲧυⲗⲟⲡⲁ ⲉⳝⲁⲏⲁя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟю ⲙⲁⲧь ⲡⲟⲉⳝⲩ ⲃ ⲡⲉⲣⲇⲁⲕ υ ⲡⲟⲥⲥⲩ ⲏⲁ ⲧⲃⲟⲉ ⲉⳝⲗⲟ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟю ⲙⲁⲧь ⳝⲉⳅ ⲡⲣⲁⲃⲁ ⲙⲟⲉⲅⲟ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲡⲣыⲅⲁⲉⲧ , ⲕⲁⳝыⲗⲁ ⲉⳝⲁⲏⲁя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲕⲟⲅⲇⲁ ⲟⲧⲥⲟⲥⲁⲗ ⲙⲏⲉ, ⲙⲟⲉⲙⲩ ⲭⲩю ⲇⲣⲩⲯⳝⲩ ⲡⲣⲉⲇⲗⲟⲯυⲗ, ⲁ ⲟⲏ ⲧⲉⳝⲉ ⳅⲁⲧⲣⲉⳃⲉⲏⲩ ⲩⲉⳝⲁⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⳡⲉⲣⲉⳅ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕυ ⲃыⳅыⲃⲁⲗ ⲡυⲕⲟⲃⲩю ⲇⲁⲙⲩ, υⳝⲟ ⲩ ⲏⲉⲉ ⲏⲉ ⲡυⳅⲇⲁⲕ ⲁ ⲕⲁⲗυⲧⲕⲁ ⲟⲧⲃⲉⳡⲁю ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲕⲟⲅⲇⲁ ⲃυⲇυⲧ ⲙⲟύ ⲭⲩύ ⲥⲃⲟυ ⲏⲟⲅυ ⲣⲁⳅⲇⲃυⲅⲁⲉⲧ ⲕⲁⲕ ⲣⲁⲅⲁⲧⲕⲩ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲟύ ⲭⲩύ ⲧⲉⳝⲉ ⲏⲁ ⲉⳝⲗⲟ ⲕⲟⲏⳡⲁⲉⲧ ⲡⲟ ⲡⲣⲁⳅⲇⲏυⲕⲁⲙ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲁ ⲥⲏⲉⲅⲩ ⲉⳝⲁⲗ ⲧⲁⲕ ⲯⲉⲥⲧⲕⲟ , ⳡⲧⲟ ⲥⲏⲉⲅ ⲃⲉⲥь ⲣⲁⲥⲧⲁяⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲯⲉ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧⲉⳝя ⲡⲟⲇ ⲏⲟⲗь ⲡⲟⲇⲥⲧⲣυⲅⲩ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲏⲁⲭⲩύ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉ ⲟⲣⲉⲱь ⳡⲧⲟ ⲧы ⲙⲟύ ⳡⲗⲉⲏ ⲡⲟⲗюⳝυⲗ, ⲡυⲇⲁⲣⲁⲥ ⲉⳝⲁⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲟύ ⲯⲉ ⳡⲗⲉⲏ ⲗюⳝυⲧ ⲧⲃⲟύ ⲣⲟⲧ ⲕⲁⲕ ⲙⲟⲣⲉ ⲗюⳝυⲧ ⳝⲣυⳅ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲟύ ⲭⲩύ ⲧⲉⳝя ⳅⲁⳝыⲗ ⲥⲣⲁⳅⲩ, ⲁ ⲧы ⲃⲟⲧ ⲉⲅⲟ ⲩⲯⲉ ⲡяⲧыύ ⲅⲟⲇ ⳅⲁⳝыⲧь ⲏⲉ ⲙⲟⲯⲉⲱь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡыⲧⲁⲉⲱьⲥя ⳝыⲧь ⲅⲉⲣⲟⲉⲙ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю, ⳡⲩⲇⲁⲕ ⲉⳝⲁⲏыύ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲏⲁⲭⲩύ ⲩ ⳝⲟⲅⲁ ⲡⲣⲟⲥυⲱь ⲥυⲗ , ⲕⲟⲅⲇⲁ я ⲧⲉⳝя ⳅⲁⲉⳝыⲃⲁю ⲥⲃⲟυⲙ ⳝⲟⲗьⲱυⲙ ⳡⲗⲉⲏⲟⲙ ⲕⲁⲕ ⲭⲩⲉⲥⲟⲥⲁ ⲉⳝⲁⲏⲟⲅⲟ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲙⲟⲉⲙⲩ ⲭⲩю ⲥⲟⲟⳝⳃⲉⲏυⲉ ⲡυⲥⲁⲗ ⲟ ⳡⲩⲃⲥⲧⲃⲁⲭ ⲕ ⲏⲉⲙⲩ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ 3ⲇⲟⲣⲟⲃⲁⲉⲱьⲥя, ⲇⲩⲙⲁя ⳡⲧⲟ ⲟⲏ ⲧⲉⳝⲉ ⳝⲩⲇⲉⲧ ⲕⲁⲕ ⳝⲣⲁⲧ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲥ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉύ ⲙⲟⲅⲩ ⲕⲟⲅⲇⲁ ⲭⲟⳡⲩ ⲣⲁⳅⲃⲗⲉⲕⲁⲧьⲥя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲟύ ⳡⲗⲉⲏ ⲇⲗя ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ цⲉⲗⲩύ ⲙυⲣ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲧⲉⳝⲉ ⲡⲟ ⲡⲗⲉⳡⲩ ⲭⲗⲟⲡⲁю, ⲧы ⲗⲟⲙⲁⲉⲱьⲥя ⲕⲁⲕ ⲇⲟⲙυⲕ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⲙⲏυⲱь ⲕⲟⲅⲇⲁ ⲧы ⲡⲁⲇⲁⲗ υ ⲙⲟύ ⲭⲩύ ⲧⲉⳝⲉ ⲡⲟⲙⲟⲅⲁⲗ ⲃⲥⲧⲁⲃⲁⲧь, υⲏⲃⲁⲗυⲇ ⲧы ⲉⳝⲁⲏыύ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲯⲉ ⲧⲉⳝⲉ ⲡⲟ ⲩⲧⲣⲩ ⳅⲁⲗⲩⲡⲟύ ⲅⲗⲁⳅⲁ ⲟⲧⲕⲣыⲃⲁю, ⲕⲟⲅⲇⲁ ⲧы ⲏⲉ ⲙⲟⲯⲉⲱь ⲃⲥⲧⲁⲧь ⲏⲁ ⲩⳡⲉⳝⲩ ⲏⲟⲣⲙⲁⲗьⲏⲟ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱь ⲧы ⲭⲩⲉⲥⲟⲥ ⲥⳝυⲧыύ, ⲧы ⲏⲁⲭⲩύ ⲙⲟύ ⲭⲩύ υⲥⲕⲁⲗ ⲃ ⲡⲣⲟⲅⲣⲁⲙⲙⲉ "ⲯⲇυ ⲙⲉⲏя" ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲡⲟⲕⲁ ⲉⳝⲩ ⲧⲃⲟύ ⲣⲟⲧ υⳅ ⲧⲃⲟⲉⲅⲟ ⲟⳡⲕⲁ ⲙⲁⲥⲥⲟⲃыύ ⲡⲟⳝⲉⲅ ⲧⲁⲣⲁⲕⲁⲏⲟⲃ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱь , ⲧы ⲏⲁⲭⲩύ ⲙⲟυ ⲗⲟⳝⲕⲟⲃыⲉ ⲃⲟⲗⲟⲥы ⲧⲟⲗⲕⲁⲉⲱь ⳅⲁ ⲅⲩⳝⲩ ⲥⲉⳝⲉ ⲕⲁⲕ ⲏⲁⲥⲃⲁύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡⲟⲥⲧⲣⲟю ⲥⲁⲣⲁύ ⲇⲗя ⲭⲣⲁⲏⲉⲏυя ⲡⲣⲉⳅⲉⲣⲃⲁⲧυⲃⲟⲃ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲙⲟύ ⳡⲗⲉⲏ ⳝⲉⲣⲉⲱь ⲃ ⲣⲟⲧ, яⲕⲟⳝы ⲣⲁⲇυ ⲡⲣⲟⳝы ⲧⲟⲗьⲕⲟ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⳝⲗяⲧь ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲯυⲃⲉⲱь υ ⲉⳃⲉ ⲡыⲧⲁⲉⲱьⲥя ⲃыⲉⳝыⲃⲁⲧⲥя ⳡⲧⲟⲗⲉ, я ⲧⲉⳝⲉ ⳃⲁⲥ ⲗⲉⳃⲉύ ⲭⲩⲉⲙ ⲏⲁⲕυⲇⲁю, ⲡⲉⲥ ⲧы ⲥⲩⲧⲩⲗыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲧⲁⲕⲟύ ⲡⲟⲧⲁⲥⲕⲁⲏⲏыύ ⲡυⲇⲁⲣⲁⲥ ⲡⲟⲥⲗⲉ ⲙⲟⲉⲅⲟ ⲭⲩя ,ⳡⲧⲟ ⲧы ⲇⲁⲯⲉ ⲭⲟⲇυⲧь ⲩⲯⲉ ⲏⲟⲣⲙⲁⲗьⲏⲟ ⲏⲉ ⲙⲟⲯⲉⲱь ⲡⲟⲥⲗⲉ ⲙⲟⲉⲅⲟ ⲭⲩя, ⲧы ⲡⲣⲟⲥⲧⲟ ⲃⲁⲗυⲱьⲥя ⲕⲁⲕ ⲱⲕⲁⲫ ⲉⳝⲁⲏыύ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲩ υ ⲭⲩⲉю ,υ ⲟⲡяⲧь ⲭⲩⲉю υ ⲟⲡяⲧь ⲉⳝⲩ ⲉⲉ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⳝⲗяⲧь ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲡⲟ ⲙⲟⲉⲙⲩ ⲭⲩю ⲭⲟⲇυⲱь ⲕⲁⲕ ⲃⲉⲧⲉⲣ ⲡⲟ ⲙⲟⲣю?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲧь ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲟⲇⲉяⲗⲟ ⲣⲃⲉⲱь ⲩ ⲥⲉⳝя ⲇⲟⲙⲁ ⲕⲟⲅⲇⲁ ⲥⲕⲩⳡⲁⲉⲱь ⲡⲟ ⲙⲟⲉⲙⲩ ⲭⲩю?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱь ⲡⲣυⲇⲩⲣⲟⲕ, ⲧы ⲡⲟⲙⲏυⲱь ⲕⲁⲕ ⲧы ⲡⲉⲣⲉⲇ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲃыⲣяⲇυⲗⲥя ⲃ ⳝⲉⲗⲟⲉ ⲡⲗⲁⲧьⲉ, ⲡυⲇⲁⲣⲁⲥ ⲃⲁⲏυⲗьⲏыύ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲙⲟύ ⳡⲗⲉⲏ ⲥⲃⲟυⲙυ ⲥⲗюⲏяⲙυ ⲃыⲙⲁⳅⲁⲗ ⲕⲟⲅⲇⲁ ⲥⲟⲥⲁⲗ ⲥⲟⳡⲏⲟ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲙⲟύ ⳡⲗⲉⲏ ⲃⲇыⲭⲁⲉⲱь ⲃ ⲥⲉⳝя ⲕⲁⲕ ⲃⲟⳅⲇⲩⲭ, ⲇⲟⲗⳝⲁⲉⳝ ⲟⲧⳝυⲧыύ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲙⲟύ ⳡⲗⲉⲏ ⲗюⳝυⲱь ⲕⲁⲕ ⲃⲉⲧⲉⲣ ⲗюⳝυⲧ ⲙⲁύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲯⲉ ⲭⲩⲉⲙ ⲧⲉⳝя ⲏⲁ υⳅⲏⲁⲏⲕⲩ ⲃыⲃⲉⲣⲏⲩ, ⳡⲙⲟⲱⲏυⲕ ⲧы ⲉⳝⲁⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲡⲟ ⲙⲟⲉⲙⲩ ⲭⲩю ⲩⳡυⲗⲥя ⳡυⲧⲁⲧь, ⲅⲗυⲥⲧ ⲧы ⲁⲏⲁⲗьⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲯⲉ ⲧⲉⳝя ⲭⲩⲉⲙ ⲥⲟⳝью, ⲕⲁⲕ ⲥⲟⲥⲩⲗьⲕⲩ ⲥ ⲇⲟⲙⲁ, ⳡⲗⲉⲏⲟⲥⲟⲥ ⲧы ⲟⳝⲟⲥⲥⲁⲏⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲉⳝⲉ ⲯⲉ ⲏⲣⲁⲃυⲧⲥя ⲙⲟύ ⲭⲩύ ⲥⲟⲥⲁⲧь, ⲏⲉ ⲧⲁⲕ ⲗυ?) ⲧы ⲇⲁⲯⲉ ⲡⲣⲟⲥυⲱь ⲩ ⲙⲉⲏя ⳡⲧⲟⳝ я ⲧⲉⳝⲉ ⲕⲁⲯⲇыύ ⲇⲉⲏь ⲏⲁ ⲣⲟⲧ ⲇⲁⲗ, ⲡⲉⲥ ⲧы ⲥⲥⲁⲏⲏыύ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲙⲟⲉⲙⲩ ⲭⲩю ⲥⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲱⲕⲩⲣⲩ ⲡⲟⲇⲁⲣυⲗ ⳅⲁ ⳡⲩⲡⲁⳡⲩⲡⲥ, ⲩⳃⲉⲣⳝⲏыύ ⲭⲩⲉⲥⲟⲥ ⲧы ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲯⲉ ⲧⲉⳝя ⲭⲩⲉⲙ ⲥⲕⲣⲩⳡⲩ ⲧⲁⲕ, ⲕⲁⲕ ⲅⲁⲗⲥⲧⲩⲕ ⲏⲁ ⲱⲉⲉ ⳅⲁⲃяⳅыⲃⲁюⲧ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲡⲟⲉⳝⲁⲧⲥя ⲭⲟⳡⲉⲱь ⳝⲟⲗьⲱⲉ ⳡⲉⲙ ⲧⲃⲟя ⲙⲁⲧь, ⲱⲗюⲭⲁ ⲧы ⲉⳝⲁⲏⲁя ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲉ ⲏⲩ ⲧы ⲯⲉ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲩ ⲙⲟⲉⲅⲟ ⲭⲩя ⳅⲁⲗⲩⲡⲁ ⲕⲣⲁⲥυⲃⲉύ ⲧⲃⲟⲉⲅⲟ ⲟⲧъⲉⳝⲁⲏⲏⲟⲅⲟ ⲉⳝⲁⲗьⲏυⲕⲁ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲃⲉⲣⲧυⲱьⲥя ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲕⲁⲕ ⲃⲉⲣⲧⲩⲱⲕⲁ ⲟⲧ ⲃⲉⲣⲧⲁⲗⲉⲧⲁ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲕⲟⲅⲇⲁ ⲙⲟⲉⲅⲟ ⲭⲩя ⲏⲉ ⲡⲟⲡⲣⲟⳝыⲃⲁⲗ, ⳝыⲗ ⲅⲣⲩⳝыύ υ ⳅⲗⲟύ, ⲁ ⲕⲁⲕ ⲡⲟⲥⲟⲥⲁⲗ ⲉⲅⲟ ,ⲥⲧⲁⲗ ⲙυⲗыύ υ ⲇⲟⳝⲣыύ, υⲇυⲟⲧ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲉⳝⲉ ⳡⲁύ ⲏⲁⲗυⲃⲁю ⲥⲟ ⲥⲃⲟⲉⲅⲟ ⲭⲩя υ ⲧы ⲡьⲉⲱь, ⲇⲉⳝυⲗ ⲟⲧъⲉⳝⲁⲏⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲕ ⲙⲟⲉⲙⲩ ⲭⲩю ⲭⲟⲇυⲧ ⳅⲁ ⳅⲁⲣⲡⲗⲁⲧⲟύ ⲡⲟⲏυⲙⲁⲉⲱь ⲧы эⲧⲟ ⲅⲩⲥь ⲉⳝⲁⲏыύ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲥⲉⲗ ⲏⲁ ⲙⲟύ ⲭⲩύ υ ⲇⲩⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲡыⲧⲁⲉⲱьⲥя ⲧⲣⲟⲗⲗυⲧⲥя ⳡⲧⲟⲗⲉ, ⲇⲟⲗⳝⲁⲉⳝ ⲁⲏⲁⲗьⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲯⲉ ⲧⲃⲟю ⲯⲟⲡⲩ ⲧⲩⲇы ⲥюⲇы ⲭⲩⲉⲙ ⲧⲁⲥⲕⲁю, ⲕⲁⲕ ⲡⲣяⲙ ⲭⲩⲉⲙ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲏⲁ ⲱυⲣⲟⲕⲟύ ⲧⲣⲟⲡⲉ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱь ⲧюⲫяⲕ ⲉⳝⲁⲏыύ, ⲃⲥⲡⲟⲙⲏυ ⲕⲁⲕ ⲧы ⲡыⲧⲁⲗⲥя ⲙⲟύ ⳡⲗⲉⲏ ⲡⲉⲣⲉⲡⲣыⲅⲏⲩⲧь ⲕⲁⲕ ⲡⲉⲣⲉⲕⲗⲁⲇυⲏⲩ ⲃⲃⲉⲣⲭ, ⲏⲩ ⳅⲁцⲉⲡυⲗⲥя ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю υ ⲡⲣⲟⲕⲣⲩⲧυⲗⲥя ⲕⲁⲕ ⲟⳝⲣⲩⳡ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲡыⲧⲁⲉⲱьⲥя ⲙⲟύ ⲭⲩύ ⲡⲟⲅⲏⲩⲧь ⲕⲁⲕ ⲱⲧⲁⲏⲕⲩ ⲣⲩⲕⲁⲙυ ⲥⲃⲟυⲙυ ⲧⲟⲏⲕυⲙυ, ⲏⲩ ⲃыⲭⲟⲇυⲧ ⲧⲁⲕ ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲇⲁⲉⲧ ⲧⲉⳝⲉ ⲡⲟ ⲉⳝⲁⲗⲩ υ ⲧы ⲡⲁⲇⲁⲉⲱь ⲟⳝ ⲡⲟⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲃⲥⲉⲙ ⲇⲁⲉⲧ, ⲟⲏⲁ ⲧⲁⲕⲁя ⲡⲣⲟⲉⳝⲁⲏⲏⲁя ⲱⲗюⲭⲁ ,ⳡⲧⲟ ⲩⲯⲉ ⲏⲉ ⳅⲁ ⲇⲉⲏьⲅυ ⲉⳝⲉⲧⲥя ,ⲁ ⳅⲁ ⲥⲡⲁⲥυⳝⲟ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲃ ⲡυⳅⲇⲁⲕⲉ ⲧⲃⲟⲉⲙ ⲭⲟⲇυⲧ ⲕⲁⲕ ⲥыⲣ ⲡⲟ ⲙⲁⲥⲗⲩ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⳅⲁⲃυⲇⲩⲉⲱь ⲙⲟⲉⲙ ⲭⲩю ⲧⲟ ⳡⲧⲟ ⲟⲏ ⲉⳝⲉⲧ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲕⲣⲩⲅⲗⲟⲥⲩⲧⲟⳡⲏⲟ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲉⳝⲁⲏыύ ⲟⲃⲟⳃ, ⲕⲟⲧⲟⲣыύ ⲕⲣⲩⲧυⲧⲥя ⲩ ⲙⲉⲏя ⲡⲉⲣⲉⲇ ⲭⲩⲉⲙ υ ⲡыⲧⲁⲉⲧⲥя ⳅⲁⲡⲣыⲅⲏⲩⲧь ⲏⲁ ⲏⲉⲅⲟ ⲕⲁⲕ ⲏⲁ ⲟⳝⲉⳅьяⲏⲁ ⲏⲁ ⲇⲉⲣⲉⲃⲟ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲉ ⲏⲩ ⲧы ⲯⲉ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲡⲟⲅⲗⲁⲧυⲗ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲕ ⳅⲃⲉⲣь?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲯⲉ ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⲡⲟ ⲅⲟⲗⲟⲃⲉ ⲇⲁⲗ, ⲩ ⲧⲉⳝя ⲃ ⲅⲗⲁⳅⲁⲭ ⲡⲟⳡⲉⲣⲏⲉⲗⲟ , ⲡⲣяⲙ ⲕⲁⲕ ⲡⲣυ ⲥⲟⲧⲣяⲥⲉⲏυⲉ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⳝⲗяⲧь ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲩ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲡυⳅⲇⲁⲕ ⲕⲁⲕ ⲃⲟⲣⲟⲧⲁ ⲏⲁ  ⲫⲩⲧⳝⲟⲗьⲏⲟⲙ ⲡⲟⲗⲉ ⳝⲗяⲧь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲥⲩⲕⲁ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲣⲁⲥⲱⲁⲧⲁⲗ ⲧⲃⲟⲉ ⲟⳡⲕⲟ υ ⲟⲏⲟ ⲩⲯⲉ ⲥⲟ ⲥⲕⲣυⲡⲁⲙυ ⲥⲁⲇυⲧⲥя ⲏⲁ ⲙⲟύ ⳡⲗⲉⲏ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲥⲩⲕⲁ ⲏⲁⲭⲩύ ⲙⲟύ ⲭⲩύ ⲧыⲕⲁⲗ ⲃ ⲡυⳅⲇⲁⲕ ⲥⲃⲟⲉύ ⲯⲁⲗⲕⲟύ ⲙⲁⲙⲁⲱⲕυ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⳝⲗяⲧь ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲅⲟⲣυⲱь ⲕⲁⲕ ⲕⲟⲥⲧⲉⲣ ⲏⲁⲭⲩύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱь ⲭⲩⲉⳝⲉⲥ ⲉⳝⲁⲏыύ, ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲙⲏⲉ ⲥⲟⲥⲉⲱь ⲅⲗⲩⲡⲟ, υⲇυ ⲩⳡυⲥь ⲩ ⲥⲃⲟⲉύ ⲙⲁⲧⲩⲭυ ⲟⲧъⲉⳝⲁⲏⲏⲟύ ⲙⲟυⲙ ⲭⲩⲉⲙ, ⲟⲏⲁ ⲭⲩяⲣυⲧ ⳅⳝⲥ, ⲏⲉ ⲧⲟ ⳡⲧⲟ ⲧы ⲥⲗⲁⳝⲁⲕ ⲉⳝⲁⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⳝⲗяⲧь ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲡⲟⲏⲧⲩⲉⲱьⲥя ⲡⲉⲣⲉⲇ ⲙⲟυⲙ ⲭⲩⲉⲙ яⲕⲟⳝы ⲧы ⳡⲧⲟ ⲧⲟ ⲉⲙⲩ ⲭⲟⳡⲉⲱь ⲥⲕⲁⳅⲁⲧь, ⲁ ⲡⲟⲗⲩⳡⲁⲉⲧⲥя ⲧⲁⲕ ⳡⲧⲟ ⲧы ⲧⲟⲗьⲕⲟ ⲥⲟⲥⲉⲱь ⲉⲅⲟ ⲕⲁⲕ ⲡыⲗⲉⲥⲟⲥ ⲉⳝⲁⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲏⲉ ⲥⲙⲉⲱⲏⲟ ⲕⲟⲅⲇⲁ ⲧы ⲙⲟύ ⳡⲗⲉⲏ ⲡыⲧⲁⲉⲱьⲥя ⲩⳝⲗⲁⲯⲁⲧь ⲥⲃⲟυⲙ ⲣⲧⲟⲙ, ⲏⲉⲩⳡ ⲉⳝⲁⲏыύ, ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲏⲉ ⲡⲣυⲇⲉⲧⲥя ⲥ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉύ ⳝⲁⳅⲁⲣυⲧь ⲏⲁⲥⳡⲉⲧ ⲧⲟⲅⲟ ⳡⲧⲟ ⲧы ⲭⲩⲉⲃⲟ ⲥⲟⲥⲉⲱь, ⲙⲏⲉ ⲕⲁⲯⲉⲧⲥя ⲉⲉ ⲡⲉⲣⲇⲁⲕ ⳝⲩⲇⲉⲧ ⳝⲟⲗⲉⲧь ⲡⲟⲥⲗⲉ ⲙⲟⲉⲅⲟ ⳡⲗⲉⲏⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲯⲁⲗⲕυύ ⲡυⲇⲁⲣⲁⲥ, ⲕⲟⲧⲟⲣыύ ⲏυⲭⲩя ⲏⲉ ⲙⲟⲯⲉⲧ, ⲕⲣⲟⲙⲉ ⲕⲁⲕ ⲟⲧⲥⲟⲥⲁⲧь ⲙⲟύ ⳡⲗⲉⲏ υ ⲟⲧⲡⲟⲗυⲣⲟⲃⲁⲧь ⲙⲟυ яυⳡⲕυ, ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲉⳝⲩ ⲧⲃⲟю ⲙⲁⲙⲁⲱⲩ ⲡⲣⲟⲥⲧⲟ ⲧⲁⲕ, ⲟⲏⲁ ⲙⲏⲉ ⲇⲁⲯⲉ ⲇⲉⲏьⲅυ ⳅⲁ эⲧⲟ ⲡⲗⲁⲧυⲧ ⲉⳝⲁⲧь, ⲡⲟⲱⲉⲗ ⲏⲁⲭⲩύ ⲡυⲇⲁⲣⲁⲥ ⲃⲁⲏυⲗьⲏыύ ⲡⲟⲕⲁ я ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⲅⲗⲁⲏⲇы ⲏⲉ ⲃыⲣⲃⲁⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲉⳝя ⲏⲁ ⲥⲃⲟύ ⲭⲩύ ⲕⲁⲕ ⲡⲥⲁ ⲏⲁ ⲕⲟⲥⲧь ⲏⲁⲧⲣⲁⲃⲗю ⲧы ⲏⲉ ⲡⲣⲟⲧυⲃ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⲏυⲙⲁⲉⲱь, эⲧⲟ υⲙⲉⲏⲏⲟ ⲙⲟύ ⲭⲩύ ⲥⲧⲁⲗ ⲡⲣυⳡυⲏⲟύ ⲣⲁⲥⲡⲁⲇⲇ ⲥⲟⲃⲉⲧⲥⲕⲟⲅⲟ ⲥⲟю3ⲁ ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲉⳝⲁⲏыύ ⲥⲃⲁⲣⳃυⲕ, ⲕⲟⲧⲟⲣыύ ⲡыⲧⲁⲗⲥя ⲡⲣυⲃⲁⲣυⲧь ⲙⲟύ ⲭⲩύ ⲕ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙы ⲏⲁⲃⲉⳡⲏⲟ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲁⲧь ⲧⲟ ⲧⲃⲟю ⳃⲁⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲃ ⳅⲃⲉⲇⲏыⲉ ⲃⲟύⲏы υⲅⲣⲁⲉⲧ ⲥ ⲧⲃⲟυⲙ ⲟⲧцⲟⲙ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲁⲧⲉⲣυ ⲧⲃⲟⲉύ ⲏⲉ ⲡⲟⲇⲭⲟⲇυⲧ ⲙⲟύ ⲭⲩύ  ⲃ ⲕⲁⳡⲉⲥⲧⲃⲉ 3ⲁⲕⲟⲗⲕυ ⲃ ⲃⲟⲗⲟⲥⲁⲭ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲡυⳅⲇⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲉⳝⲁⲗ ⲡⲟⲇ ⲧⲣⲉⲕ "яⳝⲗⲟⲕυ ⲏⲁ ⲥⲏⲉⲅⲩ") ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲙⲟύ ⲭⲩύ ⲥⲣⲁⲯⲁⲗⲥя ⲥ ⲇⲣⲁⲕⲟⲏⲟⲙ ⳅⲁ ⲡⲣⲁⲃⲟ ⳝыⲧь ⲗⲩⳡⲱυⲙ ⲉⳝыⲣⲉⲙ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲟύ ⲭⲩύ ⲩⲯⲉ 3 ⲅⲟⲇⲁ ⲏⲉⲗⲉⲅⲁⲗьⲏⲟ ⲧⲟⲣⲅⲩⲉⲧ ⲡυⳅⲇⲟύ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ, ⲧы ⲙⲉⲏя ⲭⲩύ ⳅⲁⲥⲩⲇυⲱь ⲡυⲇⲁⲣⲁⲥ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲣⲟⲱⲩ ⲡⲣⲟύⲧυ ⲕ ⲇⲃⲉⲣυ ⲉⲭⲓⲧ, ⲧⲃⲟⲉ ⳝⲁⲗⲁⲃⲥⲧⲃⲟ ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲏⲁ ⲥⲉⲅⲟⲇⲏя ⲟⲕⲟⲏⳡⲉⲏⲟ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲃⲥⲗⲉⲇⲩⳃυύ ⲣⲁⳅ ⲥⲩⲏⲩ ⲭⲩύ ⲃ ⳅⲁⲙⲟⳡⲏⲩю ⲥⲕⲃⲁⲯυⲏⲩ, ⲕⲟⲅⲇⲁ ⲧы ⳝⲩⲇⲉⲱь ⲡⲟⲇⲅⲗяⲇыⲃⲁⲧь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲣⲟⲱⲉⲡⳡυ ⲙⲟⲉⲙⲩ ⲭⲩю ⳡⲧⲟ ⲧы ⲉⲅⲟ ⲗюⳝυⲱь, ⲏⲩ ⲕⲁⲕ ⲟⳝыⳡⲏⲟ ⲕⲣⳡ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲏⲁ ⲧⲃⲟύ ⲣⲟⲧ ⲡⲟⲥⲧⲁⲃⲗю ⲡⲗⲟⲙⳝⲩ ⲕⲟⲅⲇⲁ ⲕⲟⲏⳡⲩ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲡⲣⲟⲃⲉⲗ ⲡⲟ ⲉⳝⲗⲩ υ ⲩ ⲏⲉⲉ ⲏⲁ ⲉⳝⲗⲉ ⲟⲥⲧⲁⲗⲁⲥь ⲥⲗυц ⲣⲁⲃⲗυⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⲏυⲙⲁⲉⲱь ⲉⲥⲗυ я ⲡⲟⲗⲟⲯⲩ ⲥⲃⲟύ ⲭⲩύ ⲧⲉⳝⲉ ⲏⲁ ⲡⲗⲉⳡⲟ, ⲧⲟ ⲧⲉⳝя ⲡⲉⲣⲉⲕⲟⲥⲟⲉⳝυⲧ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲉⳝⲉ ⲥⲁⲙⲟⲙⲩ ⲧⲟ ⲏⲉ ⲥⲙⲉⲱⲏⲟ, ⲥⲟⲥⲉⲱь ⲙⲏⲉ ⲥ ⲕⲟⲣⲧⲁⲃⲟύ ⲣⲉⳡью) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲙⲁⲧь ⲧⲃⲟю ⲉⳝⲁⲗ υ ⲡⲟⲭⲩύ ⳡⲧⲟ ⲟⲏⲁ ⲃ ⲃⲁⲗⲉⲏⲕⲁⲭ ⳝыⲗⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱь ⲟⲕⲁⳅыⲃⲁⲉⲧⲥя ⲧⲃⲟύ ⲣⲟⲧ ⲙⲉⲥⲧⲏⲁя ⲇⲟⲥьⲟⲡⲣυⲙυⳡⲁⲧⲉⲗьⲏⲟⲥⲧь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲁⲭⲩύ ⲧы ⲃ ⲡυⳅⲇⲉ ⲥⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⳅⲁⲡⲁⲣυⲃⲁⲉⲱь ⳝυⳡυ, ⲱⲁⲭⲁ ⲉⳝⲁⲏⲁя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲭⲩⲉⲙ ⲇⲟⲥⲧⲁⲗ ⲟⳝⲗⲟⲙⲕυ ⲧυⲧⲁⲏυⲕⲁ υⳅ ⲡυⳅⲇы ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲥ ⲗⲟⲯⲕυ ⲭⲁⲃⲁⲉⲱь ⲙⲟю ⲥⲡⲉⲣⲙⲩ υⳅ ⲟⳡⲕⲁ ⲥⲃⲟⲉύ ⲙⲁⲙⲁⲱυ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱь ⲡυⲇⲁⲣⲁⲥ, я ⲁⲏⲁⲗьⲏⲩю ⲧⲃⲟю υⲥⲧⲟⲣυю ⳝⲟⲗⲉⳅⲏυ ⲕυⲏⲩ ⲧⲉⳝⲉ ⲃ ⲉⳝⲗⲟ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲁⲭⲩύ ⲧы ⲥⲣⲉⲱь ⲥⲉⳝⲉ ⲡⲟⲇ ⲇⲃⲉⲣь υ ⲅⲟⲃⲟⲣυⲱь ⳡⲧⲟ эⲧⲟ ⲥⲇⲉⲗⲁⲗ ⲡⲟⲡⲩⲅⲁύⳡυⲕ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲁⲭⲩύ ⲧы ⲭⲁⲃⲁⲉⲱь ⲙⲟю ⲥⲡⲉⲣⲙⲩ ⲃыⲅⲣы3ⲁя ⲉⲉ υⳅ ⲡυⳅⲇы ⲥⲃⲟⲉύ ⲙⲁⲧⲉⲣυ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙы ⲥ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉύ ⲏⲁ ⲡⲟⲕⲟⲥⲉ ⲉⳝⲁⲗυⲥь ⲃ ⲕⲩⲥⲧⲁⲭ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲟύ ⲭⲩύ ⲉⲇυⲏⲥⲧⲃⲉⲏⲏыύ ⲕⲧⲟ ⲉⳝⲁⲗ ⲧⲃⲟю ⲙⲁⲧь ⲃ ⲙⲟⲙⲉⲏⲧ ⲕⲣⲉⲥⲧⲟⲃⲟⲅⲟ ⲡⲟⲭⲟⲇⲁ ⲡⲟⲇ ⲏυⲯⲏυⲙ ⲏⲟⲃⲅⲟⲣⲟⲇⲟⲙ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲁⲭⲩύ ⲧы ⲕⲩⲡυⲗ ⲥⲉⳝⲉ υ ⲙⲟⲉⲙⲩ ⲭⲩю ⳝυⲗⲉⲧы ⲃ ⲅⲁⲃⲁύⲥⲕυⲉ ⲟⲥⲧⲣⲁⲃⲁ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲁ ⲡⲣⲁⲃⲇⲁ ⳡⲧⲟ ⲧⲃⲟύ ⲣⲟⲧ ⲏⲉ ⲥⲟⲥⲕⲁⲕυⲃⲁⲉⲧ ⲥ ⲙⲟⲉⲅⲟ ⲭⲩя ⲇⲁⲯⲉ ⲃ ⲙⲟⲙⲉⲏⲧ ⳅⲉⲙⲗⲉⲧⲣяⲥⲉⲏυя?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲉⳝя ⲉⳃⲉ ⲃ ⲇⲉⲧⲥⲧⲃⲉ ⳅⲁⲅⲟⲏяⲗ ⲭⲩⲉⲙ ⲇⲟⲙⲟύ, ⲡυⲇⲣ ⲧы ⲟⲧъⲉⳝⲁⲏⲏыύ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟю ⲙⲁⲧь ⲥⲧⲁⲃⲗю ⲏⲁ ⲕⲟⲗⲉⲏυ, υ ⲟⲏⲁ ⲥⲟⲥⲉⲧ ⲧⲁⲕ ⳡⲧⲟ ⲕⲟⲗⲉⲏυ ⲇⲟ ⲕⲣⲟⲃυ ⲥⲧⲉⲣⲁⲉⲧ, ⲱⲗюⲭⲁ ⲉⳝⲁⲏⲁя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲉⳝⲁⲗ ⲧⲁⲕ ⲕⲁⲕ ⲡⲩⲗⲉⲙⲉⲧⲟⲙ ⲉⳝⲁⲧь, ⲩ ⲏⲉⲉ ⲇⲁⲯⲉ ⲥⲩⲇⲟⲣⲟⲅⲁ ⲏⲁⳡⲁⲗⲁⲥь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⳝⲗяⲧь ⲏⲁ ⲙⲟύ ⲭⲩύ ⲗⲉⳅυⲱь ⲕⲁⲕ ⲏⲁ ⲃⲉⲣⲱυⲏυ эⲃⲉⲣⲉⲥⲧⲁ я ⲡⲟⲏяⲧь ⲏⲉ ⲙⲟⲅⲩ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱь ⲅⲏⲟⲙ ⲁⲏⲁⲗьⲏыύ, ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲥⲃⲟυⲙ ⲡυⳅⲇⲁⲕⲟⲙ υ ⲣⲧⲟⲙ ⳅⲁⲣⲁⳝⲁⲧыⲃⲁⲗⲁ ⲏⲁ ⲏⲟⲃыύ ⲅⲟⲇ ⳡⲧⲟⳝ ⲡⲟⲇⲁⲧь ⲏⲁ ⲥⲧⲟⲗ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⳝⲗяⲧь ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟύ ⲣⲟⲧ ⲡыⲧⲁⲗⲥя υⲥⲕⲁⲧь υⲙⲩⲏⲏυⲧⲉⲧ ⲟⲧ ⲙⲟⲉⲅⲟ ⲭⲩя, ⳡⲧⲟⳝ ⲧⲃⲟύ ⲣⲟⲧ ⲏⲉ ⲥⲕⲣυⲡⲉⲗ υ ⲏⲉ ⳝⲟⲗⲉⲗ ⲕⲟⲅⲇⲁ я ⲧⲉⳝя ⲉⳝⲩ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲕⲟⲅⲇⲁ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲥⲕⲁⳡⲉⲱь, ⲩ ⲧⲉⳝя ⲥⲉⲣⲇцⲉ ⲣⲉⲁⲗьⲏⲟ ⲉⲗⲉ ⲡⲟⲥⲧⲩⲕυⲃⲁⲉⲧ, ⲏⲩ ⲙⲏⲉ ⲡⲣⲟⲥⲧⲟ ⲧⲁⲕ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲥⲕⲁⳅⲁⲗⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲉ ⲏⲩ ⲧы ⲯⲉ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⳅⲁⲙⲉⲏυⲗ ⲧⲉⳝⲉ ⲡⲩⲥⲧⲟⲧⲩ ⲃ ⲧⲃⲟⲉⲙ ⲩⳅⲕⲟⲙ ⲟⳡⲕⲉ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲟⲥⲧⲉⲣ ⲣⲁⳅⲃⲉⲥⲧυ ⲙⲟⲅⲩ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲏⲉ ⲡⲟⲏяⲗ, ⲧы ⳝⲗяⲧь ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲃⲟⳅⲣⲁⲇυⲗⲥя υ ⲇⲩⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲉⲣь ⲥⲡⲟⲥⲟⳝⲉⲏ ⳡⲧⲟ ⲧⲟ ⲙⲟⲉⲙⲩ ⲭⲩю ⲥⲕⲁⳅⲁⲧь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲧь ⲧⲉⳝⲉ ⲧⲃⲟύ ⳝⲁⲧя ⲇⲟⲗⳝⲁⲉⳝ ⲏⲉ ⲣⲁⲥⲥⲕⲁⳅыⲃⲁⲗ ⳡⲧⲟ ⲧⲃⲟя ⲯⲁⲗⲕⲁя ⲙⲁⲙⲁⲱⲕⲁ ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲣⲁⳅⲟⲣⲃⲁⲗⲁⲥь ⲕⲁⲕ ⲅⲟⲏⲇⲟⲏ ⲇⲉⲱⲉⲃыύ, ⲕⲟⲅⲇⲁ ⲡⲣыⲅⲁⲗⲁ ⲧⲁⲙ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲉⳝⲁⲧь ⲏⲁ ⲥⲧⲟⲗьⲕⲟ ⲉⳝⲁⲏⲩⲧыύ, ⳡⲧⲟ ⲧы ⲡыⲧⲁⲗⲥя ⲙⲟύ ⲭⲩύ ⲡⲟ ⲃⲥⲉⲙⲩ ⲅⲗⲟⳝⲩⲥⲩ υⲥⲕⲁⲧь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲙⲏυⲱь ⲕⲁⲕ я ⲧⲉⳝⲉ ⲃ ⲣⲟⲧ ⲡⲟⲥⲥⲁⲗ ,ⲩ ⲧⲉⳝя ⲇⲁⲯⲉ ⳝⲗяⲧь ⲃⲟⲗⲟⲥы ⲇыⳝⲟⲙ ⲃⲥⲧⲁⲗυ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲧь, я ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⲅⲩⳝы ⲏⲁⲕⲣⲁⲱⲩ ⲕⲁⲕ ⲡⲟⲙⲁⲇⲟύ ⲏⲁⲭⲩύ, цыⲅⲁⲏ ⲧы ⲉⳝⲁⲏыύ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲡⲟⲇ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲡыⲧⲁⲗⲥя ⲏⲁύⲧυ ⲇⲉⲏⲉⲅ ⲏⲁ ⲡⲣⲟⲡυⲧⲁⲏυя ⲥⲃⲟⲉύ ⲅⲏυⲗⲟύ ⲙⲁⲧⲉⲣυ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱь , ⲏⲩ ⲧы ⲯⲉ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲕⲣⲩⲧυⲱьⲥя ⲕⲁⲕ ⲅⲗⲟⳝⲩⲥ ⲉⳝⲁⲏыύ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲧь ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲩ ⲧⲉⳝя ⳝыⲗⲁ ⳡⲉⲣⲏⲁя ⲡⲟⲗⲟⲥⲁ ⲡⲟ ⲯυ3ⲏυ, ⲁ ⲡⲟⲧⲟⲙ ⲕⲁⲕ ⲧы ⲥⲉⲗ ⲏⲁ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⲥⲃⲟя ⲙⲁⲙⲁⲱⲁ, ⲩ ⲧⲉⳝя ⲥⲣⲁⳅⲩ ⲃ ⲯυⳅⲏυ ⳝⲉⲗⲁя ⲡⲟⲗⲟⲥⲁ ⲏⲁⲥⲧⲩⲡυⲗⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟύ ⲣⲟⲧ ⲉⳝⲁⲗ ⲧⲁⲕ , ⳡⲧⲟ ⲩ ⲧⲉⳝя ⳝⲗяⲧь ⲧⲁⲙ ⲟⲅⲏⲉⲏⲟⲉ ⲡⲗⲁⲙя ⳝыⲗⲟ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲩ ⲧⲉⳝя ⲯⲉ ⲗюⳝⲟⲃь ⲕ ⲙⲟⲉⲙⲩ ⲭⲩю ⲏⲁⲃⲉⳡⲏⲟ, ⳡⲉⲣⲧ ⲧы ⲡⲉⲣⲉⳝυⲧыύ ⲭⲩяⲙυ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲕⲟⲅⲇⲁ ⲧы ⲙⲏⲉ  ⲥⲟⲥⲁⲗ ,я ⲡⲟⲏяⲗ ⲟⲇⲏⲟ, ⳡⲧⲟ ⲧⲃⲟύ ⲣⲟⲧ эⲧⲟ ⲧⲟⲃⲁⲣ ⲥ ⳝⲣⲁⲕⲟⲙ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⲙⲏυⲱь ⲕⲁⲕ я ⲧⲉⳝя ⲭⲩⲉⲙ ⲡⲟⲙⲁⲏυⲗ ⲟⲕⲟⲗⲟ ⲙⲁⲅⲁⳅυⲏⲁ, ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲟⲅⲗяⲏⲩⲗⲁⲥь, υ ⲩⲃυⲇⲉⲗⲁ ⲕⲁⲕ ⲧⲃⲟυ ⲡяⲧⲕυ ⲧⲟⲕ ⲥⲃⲉⲣⲕⲁюⲧ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲡυⳅⲇⲁⲕ ⲥⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲕⲁⲣⲧⲟⲱⲉⲏⲟύ ⲥⲃⲟⲉύ ⲕⲗюⲉⲱь,  ⲅⲣⲁⳡ ⲧы ⲉⳝⲁⲏыύ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧⲃⲟя ⲙⲁⲙⲁⲱⲁ ⲙⲟυ ⲏⲟⲥⲕυ ⲥⲩⲱυⲧ ⲏⲁ ⲡυⳅⲇⲁⲕⲉ ⲥⲃⲟⲉⲙ, ⲟⲱυⳝⲕⲁ ⲧы ⲯυⲇⲕⲟⲥⲧυ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ υⳅ ⲡⲟⲇ ⳅⲁⲃⲁⲗⲁ ⲇⲟⲙⲁ ⲃыⲧⲁⲥⲕυⲃⲁⲗ, ⲕⲁⲕ ⲙⳡⲥ ⲉⳝⲁⲧь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲧь ⲥⲗыⲱь, я ⲏⲉ ⲩⲥⲡⲉⲃⲁю ⲡⲣⲟⲥыⲡⲁⲧⲥя ⲩⲧⲣⲟⲙ ⲥⲟ ⲥⲧⲟяⲕⲟⲙ υ ⲥⲭⲟⲇυⲧь ⲡⲟⲥⲥⲁⲧь ⲕⲁⲕ ⲧы ⲩⲯⲉ ⲕυⲇⲁⲉⲱьⲥя ⲏⲁ ⲙⲟύ ⳡⲗⲉⲏ, ⲙⲩⲙυя ⲧы ⲉⳝⲁⲏⲁя ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲩ ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲙⲟύ ⲭⲩύ ⲩⲯⲉ  ⲥⳡυⲧⲁⲉⲧ ⲧⲃⲟύ ⲣⲟⲧ ⲕⲁⲕ "ⳝыⲃⲱⲁя" ⲭⲩύ ⳅⲏⲁⲉⲧ ⲕⲁⲕⲁя ⲡⲣⲁⲃⲇⲁ ⲡⲟ ⲥⳡⲉⲧⲩ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲯⲉ ⲡⲟⲏυⲙⲁⲉⲱь ,ⲡⲟⲕⲁ ⲧы ⲙⲟυ яύцⲁ ⲣⲩⲕⲁⲙυ ⲏⲉ ⲡⲟⲧяⲅⲁⲗ ⲧы ⳝыⲗ ⲭⲗюⲡυⲕⲟⲙ ⲉⳝⲁⲏыⲙ ,ⲁ ⳃⲁⲥ ⳡⲉⲧ ⲡⲟⲭⲟⲇⲩ ⲡⲟⲇⲕⲁⳡⲁⲗⲥя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲙⲏⲉ ⲥⲟⲥⲉⲱь ⲇⲟ ⲥⲉⲇьⲙⲟⲅⲟ ⲡⲟⲧⲁ ⳝⲗяⲧь?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⳝⲗяⲧь ⲙⲟύ ⳡⲗⲉⲏ ⳅⲁⲡⲟⲙⲏυⲱь ⲏⲁ ⲥⲧⲟⲗьⲕⲟ ⲇⲟⲗⲅⲟ, ⲕⲁⲕ ⲃⲉⲧⲉⲣⲁⲏы ⲃⲧⲟⲣⲩю ⲙυⲣⲟⲃⲩю) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲟύ ⲯⲉ ⳡⲗⲉⲏ ⲧⲉⳝⲉ ⲩⲗыⳝⲕⲩ ⲏⲁ ⲉⳝⲗⲉ ⲧⲃⲟⲉⲙ ⲟⳝⲟⲥⲥⲁⲏⲟⲙ ⲇⲁⲣυⲧ, ⲉⳝⲁⲏыύ ⲧы ⲇⲉⲗьⲫυⲏ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲡⲟⲧⲉⲣⲡⲉⲗ ⲕⲣⲩⲱⲉⲏυⲉ, ⲕⲟⲅⲇⲁ ⲃⲟⲧⲕⲏⲩⲗⲥя ⲃ ⲙⲟύ ⲭⲩύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⳝⲗяⲧь ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲧⲉⳝⲉ ⲭⲩⲉⲙ ⳝⲩⲇⲩ ⲉⳝⲗⲟ ⲡⲩⲇⲣυⲧь ⲕⲁⲕ ⲡⲩⲇⲣⲟύ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲏⲁⲭⲩύ ⲃыⳝⲣⲁⲗ ⲥⲡⲟⲥⲟⳝ ⲏⲁⲕⲁⳡⲁⲧь ⲥⲃⲟю ⳝⲁⲏⲕⲩ ⲧяⲅⲁя ⲙⲟυ яύцⲁ ⲕⲁⲕ ⲅυⲣυ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲟⲥⲉⲇⲗⲁⲗ ⲕⲁⲕ ⲕⲁⳝыⲗⲩ ⲉⳝⲁⲏⲩю, ⳡⲉⲣⲧ ⲧы ⲉⳝⲁⲏыύ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲏⲁ ⲙⲟⲉⲙ ⲭⲩю ⲧⲟⲣⲙⲟⳅυⲱь ⲕⲁⲕ ⲣⲩⳡⲕⲁ ⲱⲁⲣυⲕⲟⲃⲁя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲉⳝⲁⲧь ⲧы ⲡⲟⲏυⲙⲁⲉⲱь, ⳡⲧⲟ ⲃ 45 ⲃ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱυ ⲟⲕⲟⲡы ⲣыⲗυ, ⳡⲧⲟⳝ ⲥⲡⲣяⲧⲁⲧьⲥя) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ ⲣⲁⲥⲱυⲣυⲗ, ⳅⲁⲭⲟⲇυ ⲡⲟⳡⲁυⲙ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲇⲁⲃⲁύ я ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲙⲕⲉ ⲭⲩⲉⲙ ⲣⲁⲥⳡⲉⲭⲗю ⲏⲁ ⲥⲃⲟⲉⲙ ⲭⲩю) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⳃⲁⲥ ⲕⲣⳡ ⲡⲟⲥⲧⲁⲃυⲙ ⳝⲗⲟⲕυ ⲏⲁ ⲡυ3ⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ , υ ⲙⲟύ ⲭⲩύ ⲕⲁⲕ ⳝⲩⲙⲉⲣⲁⲏⲅ υⲭ ⲥⲟⳝьⲉⲧ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⲙⲏυⲱь ⲕⲁⲕ я ⲥⲃⲟυⲙ ⲭⲩⲉⲙ ⲃⲟⲱⲉⲗ ⲃ ⲧⲃⲟⲉ ⲟⳡⲕⲟ, ⲁ ⲧⲁⲙ ⲗⲁⲙⲡⲁⳡⲕⲁ ⲥⲃⲉⲧυⲗⲁ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲥⲗыⲱь, ⲁ ⲏⲁⲭⲩύ ⲧⲃⲟя ⲙⲁⲧь ⲡⲣяⳡⲉⲧⲥя ⲡⲟⲇ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲟⲧ ⲏⲁⲗⲟⲅⲟⲃ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲙⲟύ ⲥⲡⲉⲣⲙⲁⲕ ⲃыⲡυⲃⲁⲉⲱь ⲏⲁ ⲩⲧⲣⲟ, ⲕⲟⲅⲇⲁ ⲧⲉⳝⲉ ⲭⲩⲉⲃⲟ, эⲧⲟ ⲇⲗя ⲧⲉⳝя ⳝⲗяⲧь ⲕⲣⲩⳡⲉ ⲁⲥⲡⲉⲣυⲏⲁ ⲏⲁⲭⲩύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲯⲁⲗⲕⲟύ ⲙⲁⲙⲁⲱⲕυ ⲭⲩⲉⲙ ⲡⲣⲟⲧυⲣⲁю, ⳡⲧⲟⳝ ⲟⲏⲟ ⲏⲉ ⲥⲧⲁⲗⲟ ⲡⲟⲭⲟⲯⲉ ⲏⲁ ⲧⲣяⲡⲕⲩ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲉⳝя ⲧⲣяⲥⲉⲧ ⲕⲟⲅⲇⲁ ⲙⲟύ ⲭⲩύ ⲃⲭⲟⲇυⲧ ⲃ ⲧⲃⲟύ ⲣⲟⲧ ,υⳝⲟ ⲧы ⳝⲟυⲱьⲥя ⳡⲧⲟ ⲟⲏ ⲧⲉⳝя ⲩⲉⳝⲉⲧ ⲕⲁⲕ ⲕⲗⲟⲡⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲉⳝя ⲡⲟⲭⲟⲇⲩ ⲭⲩⲉⲙ ⲧⲟ ⲏⲉⲇⲟⲧυⲥⲕⲁⲗ, ⳡⲧⲟ ⲧы ⲧⲁⲕⲟύ ⲏⲉⲣⲃⲏыύ ⲥⲧⲁⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⳡⲧⲟ я ⲭⲩⲉⲙ ⲡⲟⲇⲏяⲗ ⲕⲁⲣьⲉⲣⲩ ⲏⲁ ⲡυⳅⲇⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲥⲗⲉ ⲡⲟⲥⲉⳃⲉⲏυя ⲙⲟⲉⲅⲟ ⲭⲩя ⲏⲁⲩⳡυⲗⲥя ⲗⲉⲧⲁⲧь, ⲁυⲥⲧ ⲉⳝⲩⳡυύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲡⲟⲙⲏυⲱь ⲕⲁⲕ ⲧы ⲡыⲧⲁⲗⲥя ⲟⲧⲥⲟⲥⲁⲧь ⲙⲏⲉ ⲫⲁⲗьⲱυⲃⲟ, ⲙⲏⲉ ⲡⲣυⲱⲗⲟⲥь ⲧⲟⲅⲇⲁ ⲯⲉⲥⲧⲕⲟ ⲧⲃⲟю ⲙⲁⲧь ⲏⲁⲕⲁⳅыⲃⲁⲧь, ⲟⲏⲁ ⲥⲩⲧⲕυ ⲡⲟⲥⲗⲉ ⲙⲟⲉⲅⲟ ⲭⲩя ⳝыⲗⲁ ⲃ ⲕⲟⲙⲉ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲃⲥⲡⲟⲙυⲏⲁύ ⲕⲁⲕ ⲙы υⲅⲣⲁⲗυ ⲃ ⲃыⲱυⳝⲁⲗⲟ υ ⲕⲟⲅⲇⲁ ⲧы ⲡⲣⲟⲉⳝⲁⲗ, я ⲧⲉⳝⲉ ⲅⲗⲁⳅⲁ ⲭⲩⲉⲙ ⲃыⳝυⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲏⲩ ⲃⲟⲧ ⲡⲟⲏυⲙⲁⲉⲱь ⲩ ⲣⲟⲇυⲧⲉⲗⲉύ ⲧⲁⲕⲁя ⲥυⲗьⲏⲁя ⲗюⳝⲟⲃь ⲕ ⲧⲁⲕυⲙ ⲇⲟⲗⳝⲁⲉⳝⲁⲙ ⲕⲁⲕ ⲧы, ⲧⲁⲕ ⲃⲟⲧ я ⲏⲉ ⲙⲟⲅⲩ ⲡⲟⲏяⲧь, ⲡⲟⳡⲉⲙⲩ ⲩ ⲧⲉⳝя ⲧⲁⲕⲁя ⲯⲉ ⲗюⳝⲟⲃь ⲕ ⲙⲟⲉⲙⲩ ⲭⲩю, ⲡⲉⲇυⲕ ⲧы ⲉⳝⲁⲏыύ ⲥⲩⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲡⲟⲏυⲙⲁⲉⲱь ⲕⲟⲅⲇⲁ ⲙⲟύ ⲭⲩύ ⲃⲟⲱⲉⲗ ⲃ ⲡυⳅⲇⲁⲕ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ, ⲧⲁⲙ ⲧⲁⲕⲁя ⲃⲟύⲏⲁ ⲏⲁⳡⲁⲗⲁⲥь, ⲕⲁⲕ ⲃⲟ ⲃⲧⲟⲣⲩю ⲙυⲣⲟⲃⲩю υ ⲕⲣⳡ ⲟⲧ ⲡυⳅⲇⲁⲕⲁ ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲕυ ⲟⲥⲧⲁⲗⲁⲥь ⲟⲇⲏⲁ ⲧⲩⲱⲕⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲏⲁ ⲙⲟύ ⲭⲩύ ⲥⲁⲇυⲱьⲥя υ ⲇⲩⲙⲁⲉⲱь ⳡⲧⲟ ⲧы ⲣыцⲁⲣь ⲙⲁύⲕ ⳡⲧⲟⲗⲉ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲩ ⲧⲃⲟⲉύ ⲙⲁⲙⲕυ ⲡυⳅⲇⲁⲕ ⲕⲁⲕⲟύ ⲧⲁ ⳝⲣⲁⲕⲟⲃⲁⲏⲏыύ , ⲏⲁⲇⲟ ⲉⲅⲟ ⲏⲁ ⲡⲟⲙⲟύⲕⲩ ⲩⲯⲉ , ⲭⲩⲗь ⲧⲁⲙ ⲉⳝⲁⲧь ⲥⲃⲁⲗⲕⲁ ⲟⲇⲏⲁ ⲏⲁⲭⲩύ, ⲧⲟⲕ ⲭⲩύ цⲁⲣⲁⲡⲁⲉⲧ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲩ ⲙⲉⲏя ⲏⲁ ⲭⲩю ⲩⲯⲉ ⲕⲁⲕ ⲇⲟⲙⲁ, ⲧы ⲧⲁⲙ ⲡυⲧⲁⲉⲱьⲥя, ⲯυⲃⲉⲱь , ⲅⲣⲉⲉⲱьⲥя, ⲃⲟⲟⳝⳃⲉ ⳡⲧⲟⲗⲉ ⲟⲭⲩⲉⲗ υⲱⲁⲕ ⲉⳝⲁⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟύ ⲣⲟⲧ ⲭⲩⲉⲙ ⲃⲥⲕⲣыⲃⲁю ⲕⲁⲕ ⲕⲁⲏⲥⲉⲣⲃⲩ, ⲱⲁύⲧⲁⲏ ⲧы ⲉⳝⲁⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲙⲟύ ⲭⲩύ ⲟⲥⲧⲁⲃυⲗ ⲥⲗⲉⲇы ⲟⲧ ⲡⲟⲕⲣыⲱⲉⲕ ⲕⲟⲅⲇⲁ ⲇⲣυⲫⲧⲟⲃⲁⲗ ⲃ ⲧⲃⲟⲉⲙ ⲣⲧⲩ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲯⲉ ⲧⲃⲟύ ⲕⲗυⲧⲟⲣ ⲡⲣυцⲉⲡυⲗ ⲕ ⲭⲩю ⲕⲟⲏя υ ⲧы ⲃⲟⲗⲟⳡυⲗⲥя ⳅⲁ ⲕⲟⲏⲉⲙ ⲕⲁⲕ ⲅⲟⲏⲇⲟⲏ υⲥⲡⲟⲗьⳅⲟⲃⲁⲏⲏыύ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟю ⲙⲁⲧь ⲉⳝⲁⲗ ⲃ ⲥⲟⲣⲕⲟⲫⲣⲁⲅⲉ ⲗⲉⲏυⲏⲁ, ⳡⲧⲟⳝ ⲥⲧⲁⲗυⲏ ⲟⲯυⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲧⲟ ⲥⲃⲟυⲙ ⲣⲧⲟⲙ ⳝⲁⳅⲁⲣ ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ ⲫυⲗьⲧⲣⲩύ , ⲁ ⲧⲟ ⲩⲉⳝⲩ ⳅⲁⲧⲣⲉⳃⲉⲏⲩ ⲧⲉⳝⲉ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟⲉύ ⲙⲁⲙⲁⲱⲉ ⲇⲉⲏⲉⲅ ⳅⲁⲡⲗⲁⲧυⲗ ,ⳡⲧⲟ ⲟⲏⲁ ⲧⲉⳝя ⲣⲟⲇυⲗⲁ, ⲏⲩ ⲧⲟⳡⲏⲉύ ⳅⲁ ⲧⲟ ⳡⲧⲟ ⲧⲃⲟύ ⲣⲟⲧ ⲥⲟⲥⲉⲧ ⳅⳝⲥ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⳃⲁⲥ ⲧⲃⲟⲉ ⲁⲏⲁⲗьⲏⲟⲉ ⲧⲉⲣⲉⲙⲟ ⲭⲩⲉⲙ ⳅⲁⳝью) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲕⲟⲅⲇⲁ ⲙⲟύ ⲭⲩύ ⲡⲉⲣⲃыύ ⲣⲁⳅ ⲭⲟⲧⲉⲗ ⲧⲉⳝя ⲡⲟⲉⳝⲁⲧь, ⲩ ⲧⲉⳝя ⲃ ⲟⳡⲕⲉ ⲏⲁⲱⲗⲁⲥь ⲡⲣⲁⲕⲗⲁⲇⲕⲁ, ⳡⲟ ⳅⲁ ⲭⲩύⲏя эⲧⲟ?) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲡⲏⲩⲗ ⲟⲏⲁ ⲃ ⲥⲧⲉⲏⲕⲩ ⲩⲉⳝⲁⲗⲁⲥь υ ⲣⲁⲥⲥыⲡⲁⲗⲁⲥь ⲕⲁⲕ ⲡⲉⲡⲉⲗ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲥ ⲙⲟυⲙ ⲭⲩⲉⲙ ⳝⲁⳅⲁⲣυⲱь ⲕⲁⲕ ⲥ ⲟⲧцⲟⲙ, ⲥ ⲩⲃⲁⲯⲉⲏυⲉⲙ ⲕⲣⳡ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧⲃⲟю ⲙⲁⲧь ⲭⲩⲉⲙ ⲡⲏⲩⲗ ⲧⲁⲕ ⲟⲏⲁ ⲡⲟⲗⲉⲧⲉⲗⲁ ⲕⲁⲕ υⲥⲧⲣⲉⳝυⲧⲉⲗь) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲏⲁ ⲙⲟύ ⲭⲩύ ⲩⲉⳅⲯⲁⲉⲱь ⲕⲁⲕ ⲃ ⲕⲟⲙⲁⲏⲇυⲣⲟⲃⲕⲩ, ⲏⲁ цⲉⲗыⲭ ⲇⲃⲁ ⲙⲉⲥяцⲁ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳я ⲃ ⲡυⳅⲇⲁⲕⲉ ⲧⲃⲟⲉύ ⲙⲁⲧⲉⲣυ ⲭⲩⲉⲙ ⳝⲩяⲏυⲗ ⲧⲁⲕ , ⳡⲧⲟ ⲩⲥⲧⲣⲟυⲗ ⲡⲟⲅⲣⲟⲙ ⲕⲁⲕ ⲏⲁ ⲃⲟύⲏⲉ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳',   
'❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳ⲧы ⲙⲏⲉ ⲡыⲧⲁⲗⲥя ⲟⲧⲥⲟⲥⲁⲧь ⲕⲁⲕ ⲙⲟⳅⲅⲁⲉⳝ, ⲏⲩ ⲡⲟⲗⲩⳡυⲗ ⲩⲇⲁⲣ ⲡⲟ ⲉⳝⲁⲗⲩ) ❲ <emoji document_id=5291816251780244759>⚡️</emoji><emoji document_id=5305703294092451383>🇩🇪</emoji> ❳']
        self.db.set(self.strings["name"], "state", True)
        while self.db.get(self.strings["name"], "state"):
            await message.respond(text + random.choice(shabl))
            await sleep(0.1)
            await sleep(time)

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

    async def пингпхcmd(self, message):
        reply = await message.get_reply_message()
        file = reply if reply and reply else False
        await message.edit("<b>Загрузка</b>")
        global ph
        if reply.photo:
            media = await reply.download_media('shab.jpg')
            ph = media
        else:
            media = await reply.download_media('shab.mp4')
            ph = media
        await message.edit("<b>Файл добавлен</b>")


    async def пингиcmd(self, message):
        '''— Запускает анимированный пинг'''

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

        chat_id = message.chat_id

        reply = await message.get_reply_message()

        if chat_id:
            await self.client.send_file(message.peer_id, ph, caption=f"<emoji document_id=5352792306208480366>🌎</emoji> <emoji document_id=5942504437074366673>✍️</emoji><emoji document_id=5942883248894906154>✍️</emoji><emoji document_id=5942819107853307427>✍️</emoji><emoji document_id=5942627560901840656>✍️</emoji>: <code>{ping}</code>\n<emoji document_id=5352792306208480366>🌎</emoji> <emoji document_id=5942533574132501533>✍️</emoji><emoji document_id=5942504437074366673>✍️</emoji><emoji document_id=5942803044675620275>✍️</emoji><emoji document_id=5942883248894906154>✍️</emoji><emoji document_id=5942750285297355386>✍️</emoji><emoji document_id=5942818038406450132>✍️</emoji>: <code>{time_result}</code></b>\n")





    async def тайпcmd(self, message):
        '''— Запускает часовой тайп''' 
   
        activity_time = utils.get_args(message)
        await message.delete()
        if activity_time:
            try:
                async with message.client.action(message.chat_id, "typing"):
                    await sleep(int(activity_time[0]))
            except BaseException:
                return
        else:
            try:
                async with message.client.action(message.chat_id, "typing"):
                    await sleep(randint(3600, 3601))
            except BaseException:
                return
                
                
    async def айдиcmd(self, message):
        '''— Узнает айди сынка шалавы''' 
   
        args = utils.get_args_raw(message)
        reply = await message.get_reply_message()

        try:
            if args:
                user = await message.client.get_entity(
                    int(args) if args.isdigit() else args
                )
                
            else:
                user = await message.client.get_entity(reply.sender_id)
        except ValueError:
            user = await message.client.get_entity(message.sender_id)

        await message.edit(
            f"<b><i><emoji document_id=5318770830874782975>💀</emoji><emoji document_id=5316555418024030560>😈</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝐂𝐎𝐑𝐏𝐎𝐑𝐀𝐓𝐄 𝐍𝐀𝐌𝐄:</i></b>   <code>{user.first_name}</code>  <emoji document_id=5370932688993656500>🌕</emoji>\n"
            f"<b><i><emoji document_id=5318770830874782975>💀</emoji><emoji document_id=5316555418024030560>😈</emoji><emoji document_id=5407020022121899574>〰️</emoji>𝐂𝐎𝐑𝐏𝐎𝐑𝐀𝐓𝐄 𝐈𝐃:</i></b>  <code>{user.id}</code> <emoji document_id=5370932688993656500>🌕</emoji>\n",
        )

    async def чатинфоcmd(self, message):
        """— Информация о чате"""
        args = utils.get_args_raw(message)
        try:
            chat = await message.client.get_entity(args if not args.isdigit() else int(args))
        except:
            if not message.is_private:
                chat = await message.client.get_entity(message.chat_id)
            else:
                return await message.edit("<b>Это не чат!</b>")

        chat = await message.client(GetFullChannelRequest(chat.id))

        await message.edit("<b>Загрузка информации...</b>")

        caption = await get_info(chat, message)
        
        await message.client.send_message(message.chat_id, str(caption), file=await message.client.download_profile_photo(chat.full_chat.id, "chatphoto.jpg"))
        
        await message.delete()


async def get_info(chat, message):
    chat_obj_info = await message.client.get_entity(chat.full_chat.id)
    chat_title = chat_obj_info.title
    try:
        msg_info = await message.client(
            GetHistoryRequest(peer=chat_obj_info.id, offset_id=0, offset_date=datetime(2010, 1, 1),
                              add_offset=-1, limit=1, max_id=0, min_id=0, hash=0))
    except Exception:
        msg_info = None

    first_msg_valid = True if msg_info and msg_info.messages and msg_info.messages[0].id == 1 else False
    creator_valid = True if first_msg_valid and msg_info.users else False
    creator_id = msg_info.users[0].id if creator_valid else None
    creator_firstname = msg_info.users[0].first_name if creator_valid and msg_info.users[0].first_name is not None else "Удалённый аккаунт"
    creator_username = msg_info.users[0].username if creator_valid and msg_info.users[0].username is not None else None
    created = msg_info.messages[0].date if first_msg_valid else None
    former_title = msg_info.messages[0].action.title if first_msg_valid and type(msg_info.messages[0].action) is MessageActionChannelMigrateFrom and msg_info.messages[0].action.title != chat_title else None
    description = chat.full_chat.about
    members = chat.full_chat.participants_count if hasattr(chat.full_chat, "participants_count") else chat_obj_info.participants_count
    admins = chat.full_chat.admins_count if hasattr(chat.full_chat, "admins_count") else None
    banned_users = chat.full_chat.kicked_count if hasattr(chat.full_chat, "kicked_count") else None
    restrcited_users = chat.full_chat.banned_count if hasattr(chat.full_chat, "banned_count") else None
    users_online = 0
    async for i in message.client.iter_participants(message.chat_id):
        if isinstance(i.status, UserStatusOnline):
            users_online = users_online + 1
    group_stickers = chat.full_chat.stickerset.title if hasattr(chat.full_chat, "stickerset") and chat.full_chat.stickerset else None
    messages_viewable = msg_info.count if msg_info else None
    messages_sent = chat.full_chat.read_inbox_max_id if hasattr(chat.full_chat, "read_inbox_max_id") else None
    messages_sent_alt = chat.full_chat.read_outbox_max_id if hasattr(chat.full_chat, "read_outbox_max_id") else None
    username = chat_obj_info.username if hasattr(chat_obj_info, "username") else None
    bots_list = chat.full_chat.bot_info
    bots = 0
    slowmode = "Да" if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled else "Нет"
    slowmode_time = chat.full_chat.slowmode_seconds if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled else None
    restricted = "Да" if hasattr(chat_obj_info, "restricted") and chat_obj_info.restricted else "Нет"
    verified = "Да" if hasattr(chat_obj_info, "verified") and chat_obj_info.verified else "Нет"
    username = "@{}".format(username) if username else None
    creator_username = "@{}".format(creator_username) if creator_username else None

    if admins is None:
        try:
            participants_admins = await message.client(
                GetParticipantsRequest(channel=chat.full_chat.id, filter=ChannelParticipantsAdmins(),
                                       offset=0, limit=0, hash=0))
            admins = participants_admins.count if participants_admins else None
        except Exception:
            pass
    if bots_list:
        for bot in bots_list:
            bots += 1

    caption = "<b><emoji document_id=5226719425339599563>🖤</emoji>И𐋏Ф𐌏Р𐌑АЦИЯ 𐌏 ԿАТЕ:<emoji document_id=5226719425339599563>🖤</emoji>:</b>\n\n"
    caption += f"<b><emoji document_id=5316886577182420540>👁‍🗨</emoji>I𑀥:</b> {chat_obj_info.id}<emoji document_id=5316886577182420540>👁‍🗨</emoji>\n"
    if chat_title is not None:
        caption += f"<b><emoji document_id=5319302401797139481>😈</emoji>𐋏ᥲᤋʙᥲнᥙᥱ ᴦρуᥰᥰы:</b> {chat_title}<emoji document_id=5319302401797139481>😈</emoji>\n"
    if former_title is not None:
        caption += f"<b><emoji document_id=5465647322144711784>🤍</emoji>𐌿ρᥱдыдущᥙᥱ нᥲᤋʙᥲнᥙᥱ:</b> {former_title}<emoji document_id=5465647322144711784>🤍</emoji>\n"
    if username is not None:
        caption += f"<b><emoji document_id=5341413748135438607>🚬</emoji>Тᥙᥰ ᴦρуᥰᥰы:</b> Публичный<emoji document_id=5341413748135438607>🚬</emoji>\n"
        caption += f"<b>Линк:</b> {username}\n"
    else:
        caption += f"<b><emoji document_id=5341413748135438607>🚬</emoji>Тᥙᥰ ᴦρуᥰᥰы:</b> Приватный<emoji document_id=5341413748135438607>🚬</emoji>\n"
    if creator_username is not None:
        caption += f"<b><emoji document_id=5278612616074243894>🚬</emoji>𑀝᧐ᤋдᥲᴛᥱ᧘ь:</b> <code>{creator_username}</code><emoji document_id=5278612616074243894>🚬</emoji>\n"
    elif creator_valid:
        caption += f"<b><emoji document_id=5278612616074243894>🚬</emoji>𑀝᧐ᤋдᥲᴛᥱ᧘ь:</b> <code><a href=\"tg://user?id={creator_id}\">{creator_firstname}</a></code><emoji document_id=5278612616074243894>🚬</emoji>\n"
    if created is not None:
        caption += f"<b><emoji document_id=5785295263807573198>💀</emoji>𑀝᧐ᤋдᥲн:</b> {created.date().strftime('%b %d, %Y')} - {created.time()}<emoji document_id=5785295263807573198>💀</emoji>\n"
    else:
        caption += f"<b><emoji document_id=5785295263807573198>💀</emoji>𑀝᧐ᤋдᥲн:</b> {chat_obj_info.date.date().strftime('%b %d, %Y')} - {chat_obj_info.date.time()}<emoji document_id=5785295263807573198>💀</emoji>\n"
    if messages_viewable is not None:
        caption += f"<b><emoji document_id=5206648579308922942>🩸</emoji>Вᥙдᥙⲙыᥱ ᥴ᧐᧐δщᥱнᥙя:</b> {messages_viewable}<emoji document_id=5206648579308922942>🩸</emoji>\n"
    if messages_sent:
        caption += f"<b><emoji document_id=5438448750253058449>👿</emoji>Вᥴᥱᴦ᧐ ᥴ᧐᧐δщᥱнᥙᥔ:</b> {messages_sent}<emoji document_id=5438448750253058449>👿</emoji>\n"
    elif messages_sent_alt:
        caption += f"<b><emoji document_id=5438448750253058449>👿</emoji>Вᥴᥱᴦ᧐ ᥴ᧐᧐δщᥱнᥙᥔ:</b> {messages_sent_alt}<emoji document_id=5438448750253058449>👿</emoji>\n"
    if members is not None:
        caption += f"<b><emoji document_id=5438165819282433687>😈</emoji>Учᥲᥴᴛнᥙκ᧐ʙ:</b> {members}<emoji document_id=5438165819282433687>😈</emoji>\n"
    if admins is not None:
        caption += f"<b><emoji document_id=5346164338447100597>💀</emoji>Адⲙᥙн᧐ʙ:</b> {admins}<emoji document_id=5346164338447100597>💀</emoji>\n"
    if bots_list:
        caption += f"<b><emoji document_id=5337076423871967455>👁️</emoji>Б᧐ᴛ᧐ʙ:</b> {bots}<emoji document_id=5337076423871967455>👁️</emoji>\n"
    if users_online:
        caption += f"<b><emoji document_id=5177276590756725661>🌟</emoji>𑀝ᥱᥔчᥲᥴ ᧐н᧘ᥲᥔн:</b> {users_online}<emoji document_id=5177276590756725661>🌟</emoji>\n"
    if restrcited_users is not None:
        caption += f"<b><emoji document_id=5316699479817071036>🌙</emoji>𐌏ᴦρᥲнᥙчᥱнны᥊ ᥰ᧐᧘ьᤋ᧐ʙᥲᴛᥱ᧘ᥱᥔ:</b> {restrcited_users}<emoji document_id=5316699479817071036>🌙</emoji>\n"
    if banned_users is not None:
        caption += f"<b><emoji document_id=5174842881898185450>🌟</emoji>Зᥲδᥲнᥱнны᥊ ᥰ᧐᧘ьᤋ᧐ʙᥲᴛᥱ᧘ᥱᥔ:</b> {banned_users}<emoji document_id=5174842881898185450>🌟</emoji>\n"
    if group_stickers is not None:
        caption += f"<b><emoji document_id=5316604981946624573>👁</emoji>𑀝ᴛᥙκᥱρы ᴦρуᥰᥰы:</b> <a href=\"t.me/addstickers/{chat.full_chat.stickerset.short_name}\">{group_stickers}</a><emoji document_id=5316604981946624573>👁</emoji>\n"
    caption += "\n"
    caption += f"<b><emoji document_id=5229205949410978575>🥺</emoji>𑀝᧘᧐уⲙ᧐д:</b> {slowmode}<emoji document_id=5229205949410978575>🥺</emoji>"
    if hasattr(chat_obj_info, "slowmode_enabled") and chat_obj_info.slowmode_enabled:
        caption += f", {slowmode_time} секунд\n"
    else:
        caption += "\n"
    caption += f"<b><emoji document_id=5228746216111614833>🖤</emoji>𐌏ᴦρᥲнᥙчᥱн:</b> {restricted}<emoji document_id=5228746216111614833>🖤</emoji>\n"
    if chat_obj_info.restricted:
        caption += f"> Платформа: {chat_obj_info.restriction_reason[0].platform}\n"
        caption += f"> Причина: {chat_obj_info.restriction_reason[0].reason}\n"
        caption += f"> Текст: {chat_obj_info.restriction_reason[0].text}\n\n"
    else:
        caption += ""
    if hasattr(chat_obj_info, "scam") and chat_obj_info.scam:
        caption += "<b>Скам</b>: да\n\n"
    if hasattr(chat_obj_info, "verified"):
        caption += f"<b><emoji document_id=5229233948302780155>😾</emoji>Вᥱρᥙɸᥙцᥙρ᧐ʙᥲн:</b> {verified}<emoji document_id=5229233948302780155>😾</emoji>\n\n"
    if description:
        caption += f"<b><emoji document_id=5037709218996552481>😈</emoji>𐌏ᥰᥙᥴᥲнᥙᥱ<emoji document_id=5037709218996552481>😈</emoji>:</b> \n\n<code>{description}</code>\n"
    return caption

    async def мутcmd(self, message: Message):
        """<user> [time] [reason] - Mute user"""
        chat = await message.get_chat()

        a = await self.args_parser(message, include_force=True)
        if not a:
            await utils.answer(message, self.strings("args"))
            return

        user, t, reason, force = a

        if not chat.admin_rights and not chat.creator:
            await utils.answer(message, self.strings("not_admin"))
            return

        fed = await self.find_fed(message)
        if (
            not force
            and fed in self.api.feds
            and user.id in list(map(int, self.api.feds[fed]["fdef"]))
        ):
            await utils.answer(message, self.strings("fdef403").format("mute"))
            return

        try:
            await self.mute(chat, user, t, reason, message)
        except UserAdminInvalidError:
            await utils.answer(message, self.strings("not_admin"))
            return

    @error_handler
    @chat_command
    async def анмутcmd(self, message: Message):
        """<reply | user> - Unmute user"""
        chat = await message.get_chat()

        if not chat.admin_rights and not chat.creator:
            await utils.answer(message, self.strings("not_admin"))
            return

        reply = await message.get_reply_message()
        args = utils.get_args_raw(message)
        user = None

        try:
            if args.isdigit():
                args = int(args)
            user = await self._client.get_entity(args)
        except Exception:
            try:
                user = await self._client.get_entity(reply.sender_id)
            except Exception:
                await utils.answer(message, self.strings("args"))
                return

        try:
            await self._client.edit_permissions(
                chat,
                user,
                until_date=0,
                send_messages=True,
            )
            msg = self.strings("unmuted").format(
                utils.get_link(user), get_first_name(user)
            )
            await utils.answer(message, msg)

            if self.get("logchat"):
                await self._client.send_message(
                    self.get("logchat"),
                    self.strings("unmuted_log").format(
                        utils.get_link(user),
                        get_first_name(user),
                        utils.get_link(chat),
                        get_first_name(chat),
                    ),
                )
        except UserAdminInvalidError:
            await utils.answer(message, self.strings("not_admin"))
            return 