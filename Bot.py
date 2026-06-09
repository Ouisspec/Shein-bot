import logging
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update

TOKEN = "8556419775:AAHcY3Q5GmmsWyc_F96_67qkdSKfm3WSpg0"
CODE = "CV8UF"
LINKTREE = "https://linktr.ee/Actusmode"

async def start(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"🛍️ Bienvenue sur Bons Plans SHEIN !\n\n"
        f"🏷️ Code promo : {CODE}\n\n"
        f"👇 Mes sélections : {LINKTREE}\n\n"
        f"Tape /aide pour voir toutes les commandes"
    )

async def code(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        f"💸 Ton code promo SHEIN :\n\n🏷️ {CODE}\n\n"
        f"1. Va sur shein.com\n2. Ajoute au panier\n"
        f"3. Entre {CODE} à la caisse 🎉\n\n"
        f"🔗 {LINKTREE}"
    )

async def lien(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"🔗 Mes sélections :\n\n👉 {LINKTREE}\n\nCode : {CODE} 💸")

async def aide(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start\n/code\n/lien\n/aide")

async def message_auto(update: Update, ctx: ContextTypes.DEFAULT_TYPE):
    texte = update.message.text.lower()
    if any(w in texte for w in ["code", "promo", "réduction"]):
        await code(update, ctx)
    else:
        await update.message.reply_text(f"👋 Tape /code pour le code promo !")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("code", code))
app.add_handler(CommandHandler("lien", lien))
app.add_handler(CommandHandler("aide", aide))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, message_auto))
print("Bot démarré ✅")
app.run_polling()
