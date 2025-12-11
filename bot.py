import os
from telegram.ext import ApplicationBuilder, CommandHandler
from telegram import Update
from telegram.ext import ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hello Walid! Bot is running on Railway 🚀")

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("pong")

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("ping", ping))

    app.run_polling()

if __name__ == "__main__":
    main()
