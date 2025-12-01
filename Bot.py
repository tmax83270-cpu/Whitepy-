from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Remplace par ton token BotFather
TOKEN = "8476960807:AAGLf9Fy05l3A390iBjdigCNOYwtWNnVC0k"

# Fonction appelée quand quelqu'un envoie /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bonjour ! Ton bot fonctionne 😄")

# Créer l'application du bot
app = ApplicationBuilder().token(TOKEN).build()

# Ajouter le handler pour la commande /start
app.add_handler(CommandHandler("start", start))

# Lancer le bot en continu
app.run_polling()
