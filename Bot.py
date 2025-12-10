import os
from flask import Flask, request
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Récupère ton token depuis les Environment Variables Render
TOKEN = os.environ.get("TELEGRAM_TOKEN")

# Crée l'application Flask pour le serveur Render
app = Flask(__name__)
bot = Bot(token=TOKEN)

# Crée l'application Telegram pour gérer les commandes
application = ApplicationBuilder().token(TOKEN).build()

# Commande /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot actif !")

application.add_handler(CommandHandler("start", start))

# Route webhook
@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    update = Update.de_json(request.get_json(force=True), bot)
    application.update_queue.put(update)
    return "ok"

# Port fourni par Render
PORT = int(os.environ.get("PORT", 5000))

if __name__ == "__main__":
    # Configure le webhook avec ton URL Render
    bot.set_webhook(f"https://whitepy.onrender.com/{TOKEN}")
    app.run(host="0.0.0.0", port=PORT)
