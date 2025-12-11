import os
from telethon import TelegramClient, events
import asyncio

API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

client = TelegramClient("bot_session", API_ID, API_HASH)

async def main():
    await client.start(bot_token=BOT_TOKEN)

    @client.on(events.NewMessage(pattern="/start"))
    async def handler(event):
        await event.reply("Bot is running successfully on Railway 🔥")

    print("Bot started!")
    await client.run_until_disconnected()

asyncio.run(main())
