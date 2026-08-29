from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8857588032:AAGBVfQsvhKhRcPoD1ys0rpkDRrVl0KdHl4"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 👋\n"
        "Добро пожаловать в моего бота! 💜\n\n"
        "Нажми кнопку «Кто я», чтобы начать! 🎮"
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
