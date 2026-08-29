import os
import threading

from flask import Flask
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes


TOKEN = os.environ["BOT_TOKEN"]

# 🔗 СЮДА ВСТАВЬ АДРЕС СВОЕГО MINI APP
MINI_APP_URL = "https://muroda0031-lang.github.io/shodiyor-mini-app/shodiyor_mini_app.html"


web_app = Flask(__name__)


@web_app.route("/")
def home():
    return "Bot is running! 💜"


@web_app.route("/health")
def health():
    return "OK"


def run_web_server():
    port = int(os.environ.get("PORT", 10000))
    web_app.run(host="0.0.0.0", port=port)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "🎮 Кто я",
                web_app=WebAppInfo(url=MINI_APP_URL)
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Привет! 👋\n"
        "Добро пожаловать в NEXUS ONLINE! 💜\n\n"
        "Нажми кнопку «🎮 Кто я», чтобы начать игру!",
        reply_markup=reply_markup
    )


def run_bot():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()


if __name__ == "__main__":
    web_thread = threading.Thread(
        target=run_web_server,
        daemon=True
    )
    web_thread.start()

    run_bot()
