import random
import asyncio
from pyrogram import filters
from FallenRobot import pbot as FallenRobot



"""
    |----╒════════════╕----|
          |  Kang with credits |
          |----- Coded by: ----|
          |       @CoderX      |
          |----(2142595466)----|
          |      on telegram   |
    |----╘════════════╛----|
"""

ROMANTIC_STRINGS = [
                     'Meri chahat dekhni hai? \nTo mere dil par apna dil rakhkar dekh\nteri dhadkan naa bhadjaye to meri mohabbat thukra dena...',
                     'Tere ishq me is tarah mai neelam ho jao\naakhri ho meri boli aur main tere naam ho jau...',
                     'Nhi pta ki wo kabhi meri thi bhi ya nhi\nmujhe ye pta hai bas ki mai to tha umr bas usi ka rha...',
                     'Tumne dekha kabhi chand se pani girte hue\nmaine dekha ye manzar tu me chehra dhote hue...',
                     'Tera pata nahi par mera dil kabhi taiyar nahi hoga\nmujhe tere alawa kabi kisi aur se pyaar nhi hoga...',
                     'Lga ke phool haathon se usne kaha chupke se\nagar yaha koi nahi hota to phool ki jagah tum hote...',
                   ]

"""
    Hello kangers, 
    How are you all??
    So if you want to add more shyari add it between '', example 'Yes I'm kanging your codes', 
    I hope it's clear to you!

    So if you're really kanging this atleast don't remove this line it takes a lot of time to code things.
    Coded by : @CoderX on telegram...
"""

@FallenRobot.on_message(filters.command("shayari"))
async def lel(bot, message):
    ran = random.choice(ROMANTIC_STRINGS)
    await bot.send_chat_action(message.chat.id, "typing")
    await asyncio.sleep(1.5)
    return await message.reply_text(text=ran)


__mod_name__ = "Sʜᴀʏᴀʀɪ"

__help__ = """

ᴍᴀᴋᴇs ᴀ sʜᴀʏᴀʀɪ ᴀɴᴅ sᴇɴᴅ ɪᴛ ᴛᴏ ʏᴏᴜ.

❍ /shayari *:* ᴍᴀᴋᴇs sʜᴀʏᴀʀɪ ɪғ ʏᴏᴜ sᴇɴᴅ ᴛʜɪs ᴄᴏᴍᴍᴀɴᴅ

 """
