from telethon import TelegramClient, events
import os

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]

client = TelegramClient("session", api_id, api_hash)

@client.on(events.NewMessage)
async def handler(event):
    print("Message:", event.text)

client.start()
client.run_until_disconnected()
