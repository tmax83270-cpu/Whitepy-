import telebot
import os

# Ton token BotFather
TOKEN = os.environ.get("8476960807:AAGLf9Fy05l3A390iBjdigCNOYwtWNnVC0k")  # ou remplace directement par ton token en texte

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Bonjour ! Ton bot fonctionne 😄")

bot.infinity_polling()
