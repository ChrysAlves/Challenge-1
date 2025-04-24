from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Respostas personalizadas
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔥 Bem-vindo ao FURIA CS Bot! Use os comandos pra ficar por dentro do time!:  /jogos   /ultimo_jogo   /jogador_mvp   /loja   /clipes ")

async def jogos(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎮 Próximo jogo: FURIA vs NAVI, amanhã às 16h!")

async def ultimo_jogo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✅ Última partida: vitória 2x1 contra a Liquid!")

async def jogador_mvp(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("⭐ Destaque: KSCERATO - 1.34 de rating no último campeonato.")

async def loja(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👕 Acesse a loja oficial da FURIA: https://loja.furia.gg")

async def clipes(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📹 Veja os highlights: https://clips.twitch.tv/FURIA")

# Roda o bot
app = ApplicationBuilder().token("7851266072:AAEAfNl0aKO8Ez8jxbHr6smu7-_Rcv7o9ZU").build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("jogos", jogos))
app.add_handler(CommandHandler("ultimo_jogo", ultimo_jogo))
app.add_handler(CommandHandler("jogador_mvp", jogador_mvp))
app.add_handler(CommandHandler("loja", loja))
app.add_handler(CommandHandler("clipes", clipes))

print("Bot rodando...")
app.run_polling()

# chrysfuriabot o nome do bot pra pesquisa