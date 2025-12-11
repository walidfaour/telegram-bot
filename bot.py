from telethon import TelegramClient, events
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Password users must enter
SECRET_PASSWORD = "WhatstheHiddenMessage"

# Track which users are currently entering a password
awaiting_password = set()

@client.on(events.NewMessage(pattern='/start'))
async def start_handler(event):
    user = event.sender_id
    awaiting_password.add(user)
    await event.reply("🔐 Welcome! Please enter the password:")

@client.on(events.NewMessage)
async def password_checker(event):
    user = event.sender_id
    text = event.raw_text.strip()

    # If user is not in password mode, ignore
    if user not in awaiting_password:
        return

    # Check password
    if text == SECRET_PASSWORD:
        awaiting_password.remove(user)

        await event.reply(
            "✅ Correct!\n\n"
            "Use the UV light in the drawer on the back of the page that was inside your envelope.\n"
            "You'll see a hidden password.\n\n"
            "Then login using that password here:\n"
            "http://ezekielsecretsanta.com/secret-santa-login"
        )
    else:
        await event.reply("❌ Incorrect password. Try again.")

print("Bot is running...")
client.run_until_disconnected()
