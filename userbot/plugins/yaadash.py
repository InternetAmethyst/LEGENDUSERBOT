import asyncio
from . import *


@bot.on(admin_cmd(pattern="yaadash"))
async def yaadash(ult):
	await ult.edit("***falled while walking***")
	await asyncio.sleep(3)
	await ult.edit("***2 Hours Later***")
	await asyncio.sleep(6)
	await ult.edit("who i am here ?") 
	await asyncio.sleep(1)
	await ult.edit("Where I Am?")
	await asyncio.sleep(1)
	await ult.edit("What I Am Using?")
	await asyncio.sleep(1)
	await ult.edit("What Is Phone?")
	await asyncio.sleep(1)
	await ult.edit("What Is Telegram?")
	await asyncio.sleep(1)
	await ult.edit("Why Life Exists?")
	await asyncio.sleep(1)
	await ult.edit("What is Language?")
	await asyncio.sleep(1)
	await ult.edit("Does Reborn Take Place?")
	await asyncio.sleep(1)
	await ult.edit("What Is Thinking?")
	await asyncio.sleep(1)
	await ult.edit("Does Superman Exists")
	await asyncio.sleep(3)
	await ult.edit("Oof I Guess I Should Die")



CmdHelp("yaadash").add_command(
'yaadash', None, 'Use and see'
).add()
