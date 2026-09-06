import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

app = Flask(__name__)

@app.get("/")
def home():
    return "Playerlion bot is running"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلاً بك في Playerlion 🦁\nالبوت يعمل الآن.")

def run_web():
    port = int(os.environ.get("PORT", "10000"))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    threading.Thread(target=run_web, daemon=True).start()

    application = ApplicationBuilder().token(os.environ["BOT_TOKEN"]).build()
    application.add_handler(CommandHandler("start", start))
    application.run_polling()
