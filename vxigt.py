import logging
import os
from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ChatJoinRequestHandler,
    ContextTypes
)

# ---------------- CONFIG ----------------
BOT_TOKEN = os.getenv("8951924190:AAGdEOeC_GQNcAVjPdQiRPP7xV2BUxgU70U")

WELCOME_MESSAGE = """🔥 Welcome to Auto Join System Bot! 🔥

🤖 Your bot is now ACTIVE
⚡ Auto join request approval enabled
🚀 Just add me as admin in your channel

👉 Join Updates:
https://t.me/Premium_Collection_bx

💎 Enjoy seamless automation 24/7
"""

# ---------------- LOGGING ----------------
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

# ---------------- AUTO APPROVE ----------------
async def auto_accept(update: Update,
                      context: ContextTypes.DEFAULT_TYPE):

    req = update.chat_join_request
    user = req.from_user
    chat = req.chat

    try:
        await context.bot.approve_chat_join_request(
            chat.id,
            user.id
        )

        try:
            await context.bot.send_message(
                user.id,
                f"Thanks for joining ({user.first_name}) 🎉"
            )
        except:
            pass

    except Exception as e:
        logging.error(e)


# ---------------- START ----------------
async def start(update: Update,
                context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(WELCOME_MESSAGE)


# ---------------- MAIN ----------------
def main():

    app = Application.builder()\
        .token(BOT_TOKEN)\
        .build()

    app.add_handler(ChatJoinRequestHandler(auto_accept))
    app.add_handler(CommandHandler("start", start))

    print("🤖 Bot Running...")
    app.run_polling()


if __name__ == "__main__":
    main()