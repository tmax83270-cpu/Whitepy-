import os
from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler

# Token depuis les secrets Render
TOKEN = os.environ.get("TELEGRAM_TOKEN")
bot = Bot(token=TOKEN)

# Créer l'application Flask
app = Flask(__name__)

# Créer le dispatcher
dispatcher = Dispatcher(bot, None, workers=0)

# Commande /start
def start(update: Update, context):
    update.message.reply_text("Bot actif !")

dispatcher.add_handler(CommandHandler("start", start))

# Route webhook
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    dispatcher.process_update(update)
    return "ok"

# Port fourni par Render
PORT = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    # Configurer le webhook avec ton URL publique
    bot.set_webhook(f"https://whitepy.onrender.com/{TOKEN}")
    app.run(host="0.0.0.0", port=PORT)
