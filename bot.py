from telethon import TelegramClient, events
import os

API_ID = int(os.environ.get("API_ID"))
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")
SECRET_PASSWORD = os.environ.get("SECRET_PASSWORD")

client = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)

# Commands that trigger the Phase 8 message
HELP_COMMANDS = {'/start', '/help', 'help', '?'}

@client.on(events.NewMessage)
async def message_handler(event):
    text = event.raw_text.strip()
    text_lower = text.lower()
    
    # Check if it's a help/start command
    if text_lower in HELP_COMMANDS:
        await event.reply(
            "📌 **Phase 8 Challenge:**\n\n"
            "Good reaching to phase 8.\n"
            "Enter the password to reveal the next challenge."
        )
    # Check if it's the correct password
    elif text == SECRET_PASSWORD:
        await event.reply(
            "📌 **Phase 9 Challenge:**\n\n"
            "Great job! The next step is to find a hidden message in the office? "
            "But how would you find it? The message or password is invisible and to be able to see it "
            "you have to use a UV light. To get a UV light, you can find it in one of the drawers in "
            "the first raw of desks where SOC sits right infront of you. It is a black & grey object that looks like a pen.\n\n"
            "To make sure, Lexibook and Spy Mission are written on it."
            "Try to find the hidden text on the paper that came in your secret santa envelope. "
            "Somewhere in the middle section of the paper maybe?"
            "The hidden text you find will be the password you should enter here: "
            "https://ezekielsecretsanta.com/secret-santa-login"
        )
    # Anything else is incorrect
    else:
        await event.reply("❌ Incorrect password. Try again.")

print("Bot is running...")

client.run_until_disconnected()


