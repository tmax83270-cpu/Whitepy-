from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")  # Ton token dans les variables d'environnement

def start(update: Update, context: CallbackContext):
    chat_id = update.effective_chat.id
    texte = "Salut ! Bienvenue sur mon bot 😃"
    boutons = [
        [InlineKeyboardButton("Info", callback_data='info')],
        [InlineKeyboardButton("Aide", callback_data='aide')]
    ]
    clavier = InlineKeyboardMarkup(boutons)
    context.bot.send_photo(chat_id=chat_id, photo=open("image.jpg","rb"), caption=texte, reply_markup=clavier)

def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    if query.data == 'info':
        query.edit_message_text(text="Voici les infos du bot !")
    elif query.data == 'aide':
        query.edit_message_text(text="Voici l'aide du bot !")

updater = Updater(TOKEN, use_context=True)
dispatcher = updater.dispatcher
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CallbackQueryHandler(button))
updater.start_polling()
updater.idle()
