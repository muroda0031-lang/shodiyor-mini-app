```python
import os
import threading

from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes


# Токен берём из переменной Render
TOKEN = os.environ["BOT_TOKEN"]


# Небольшой веб-сервер для Render
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


# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! 👋\n"
        "Добро пожаловать в моего бота! 💜\n\n"
        "Нажми кнопку «Кто я», чтобы начать! 🎮"
    )


def run_bot():
    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.run_polling()


if __name__ == "__main__":
    # Запускаем веб-сервер и Telegram-бота одновременно
    web_thread = threading.Thread(
        target=run_web_server,
        daemon=True
    )
    web_thread.start()

    run_bot()
```
