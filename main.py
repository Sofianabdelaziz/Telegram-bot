from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from flask import Flask, request
import os

TOKEN = os.environ.get("8134728342:AAHrCWtuQjers6JY-87sh67Z7HPCSX8SR94")  # ضع التوكن في متغير بيئة على Render
app = Flask(__name__)

# واجهة البوت
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [["زر 1", "زر 2"], ["زر 3"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("مرحبا بك 👋", reply_markup=reply_markup)

application = ApplicationBuilder().token(TOKEN).build()
application.add_handler(CommandHandler("start", start))

# نقطة تشغيل الويبهوك
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), application.bot)
    application.update_queue.put(update)
    return "ok"

# نقطة اختبار
@app.route("/", methods=["GET"])
def index():
    return "Bot is running ✅"

if __name__ == "__main__":
    app