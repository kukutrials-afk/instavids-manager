import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters
)

TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Welcome to InstaVids Manager!\n\n"
        "/accounts - Manage accounts\n"
        "/newpost - Create post draft\n"
        "/help - Help"
    )

async def accounts(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Account manager is ready for setup."
    )

async def newpost(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Send your photo or video with caption."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "InstaVids Manager\n"
        "/start\n/accounts\n/newpost\n/help"
    )

def main():
    if not TOKEN:
        raise RuntimeError("BOT_TOKEN is missing")

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("accounts", accounts))
    app.add_handler(CommandHandler("newpost", newpost))
    app.add_handler(CommandHandler("help", help_command))

    app.run_polling()

if __name__ == "__main__":
    main()
