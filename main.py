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

if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN environment variable not set!")

WELCOME_MESSAGE = """🔥 Welcome to Auto Join System Bot! 🔥

🤖 Your bot is ACTIVE
⚡ Auto join request approval enabled
🚀 Add me as admin in your channel

👉 Join Updates:
https://t.me/Premium_Collection_bx

💎 Enjoy seamless automation 24/7
"""

# ---------------- LOGGING ----------------
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

logger = logging.getLogger(__name__)


# ---------------- AUTO APPROVE ----------------
async def auto_accept(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:
        req = update.chat_join_request

        # Safety check (IMPORTANT FIX)
        if not req:
            logger.warning("No join request found in update")
            return

        user = req.from_user
        chat = req.chat

        await context.bot.approve_chat_join_request(
            chat.id,
            user.id
        )

        try:
            await context.bot.send_message(
                chat_id=user.id,
                text=f"Thanks for joining ({user.first_name}) 🎉"
            )
        except Exception as dm_error:
            logger.warning(f"DM failed: {dm_error}")

        logger.info(f"Approved user {user.id} in chat {chat.id}")

    except Exception as e:
        logger.error(f"Auto approve error: {e}")


# ---------------- START COMMAND ----------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    try:
        if update.message:
            await update.message.reply_text(WELCOME_MESSAGE)
    except Exception as e:
        logger.error(f"Start error: {e}")


# ---------------- MAIN ----------------
def main():

    app = Application.builder().token(BOT_TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(ChatJoinRequestHandler(auto_accept))

    logger.info("🤖 Bot is running...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
