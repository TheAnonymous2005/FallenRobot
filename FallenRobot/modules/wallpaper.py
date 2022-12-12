import random
import requests
from pyrogram import filters
from pyrogram.types import Message 

from FallenRobot import pbot, arq

@pbot.on_message(filters.command("wall"))
async def wall(_, m: Message):
    if len(m.command) < 2:
        return await m.reply_text("ɢɪᴠᴇ ᴍᴇ ᴀ ᴛᴇxᴛ !")
    search = m.text.split(None, 1)[1]
    x = await arq.wall(search)
    y = x.result
    await m.reply_photo(random.choice(y).url_image)
except Exception as e:
        await m.edit_text(
            f"`Wallpaper not found for : `{search}`",
        )
