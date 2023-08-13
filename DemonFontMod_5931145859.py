#meta developer: @sheanova
import logging
from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class DemonFontMod(loader.Module):
    """шрифт наебашит"""
    strings = {"name": "DevilFont",
               "nety_teksta": "<b>Heту текста для изменения.</b>"}

    async def client_ready(self, client, db):
        self.client = client

    @loader.owner
    async def фcmd(self, soobshenie):
        """<любой текст или реплай>"""
            
        otvet = await soobshenie.get_reply_message()
        vvod = utils.get_args_raw(soobshenie)
        if not vvod:
            if not otvet or not otvet.text:
                await utils.answer(soobshenie, self.strings("nety_teksta", soobshenie))
                return
            else:
                tekst = otvet.raw_text
        else:
            tekst = vvod
        vyvod = ""
        for simvol in tekst:
            if simvol.lower() in bykvy:
                bykva = bykvy[simvol.lower()]
                if simvol.isupper():
                    bykva = bykva.upper()
            else:
                bykva = simvol
            vyvod += bykva
        await utils.answer(soobshenie, vyvod)
bykvy = {"а": "А", "б": "6", "в": "V", "г": "Г", "д": "D", "е": "3", "ё": "3", "ж": "J", "з": "Z", "и": "i", "й": "i", "к": "K", "л": "L", "м": "M", "н": "H", "о": "0", "п": "П", "р": "R", "с": "C", "т": "T", "у": "Y", "ф": "F", "х": "X", "ц": "Ц", "ч": "Ч", "ш": "III", "щ": "IIL", "ъ": "Ъ", "ы": "bI", "ь": "b", "э": "Э", "ю": "I-O'", "я": "Я"}