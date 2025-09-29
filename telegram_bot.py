import requests
import telebot

# 👉 Cole o TOKEN do seu bot aqui
TELEGRAM_TOKEN = "8441569201:AAH0fLBycEyhdn1frw83utA0SbtEHSx1Jss"

bot = telebot.TeleBot(TELEGRAM_TOKEN)

# ============================
# URLs dos serviços
# ============================
IA_URL = "http://127.0.0.1:5001/api/ia-sinal"
NEWS_URL = "http://127.0.0.1:5002/api/news"
VOICE_URL = "http://127.0.0.1:5003/api/voice"   # corrigido
EXCEL_URL = "http://127.0.0.1:5004/api/export_excel"
DASHBOARD_URL = "http://127.0.0.1:5000/"

# ============================
# Comando /start
# ============================
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(
        message,
        "🤖 Olá! Eu sou o seu Robô.\n"
        "Pode me pedir IA, NEWS, VOICE, EXCEL ou DASHBOARD."
    )

# ============================
# Comando /ia
# ============================
@bot.message_handler(commands=['ia'])
def ia(message):
    try:
        r = requests.post(IA_URL, json={"texto": "Teste de IA"})
        bot.reply_to(message, f"IA respondeu: {r.json()}")
    except Exception as e:
        bot.reply_to(message, f"Erro ao chamar IA: {e}")

# ============================
# Comando /news
# ============================
@bot.message_handler(commands=['news'])
def news(message):
    try:
        r = requests.get(NEWS_URL)
        bot.reply_to(message, f"NEWS respondeu: {r.json()}")
    except Exception as e:
        bot.reply_to(message, f"Erro ao chamar NEWS: {e}")

# ============================
# Comando /voice
# ============================
@bot.message_handler(commands=['voice'])
def voice(message):
    try:
        r = requests.post(VOICE_URL, json={"texto": "Olá, testando voz"})
        bot.reply_to(message, f"VOICE respondeu: {r.json()}")
    except Exception as e:
        bot.reply_to(message, f"Erro ao chamar VOICE: {e}")

# ============================
# Comando /excel
# ============================
@bot.message_handler(commands=['excel'])
def excel(message):
    try:
        r = requests.post(EXCEL_URL, json={"dados": "Teste de exportação"})
        bot.reply_to(message, f"EXCEL respondeu: {r.json()}")
    except Exception as e:
        bot.reply_to(message, f"Erro ao chamar EXCEL: {e}")

# ============================
# Comando /dashboard
# ============================
@bot.message_handler(commands=['dashboard'])
def dashboard(message):
    bot.reply_to(message, f"📊 Acesse o Dashboard aqui: {DASHBOARD_URL}")

# ============================
# Mensagem padrão (quando não reconhece)
# ============================
@bot.message_handler(func=lambda m: True)
def echo(message):
    bot.reply_to(
        message,
        "Digite um comando válido: /ia, /news, /voice, /excel, /dashboard"
    )

print("🤖 Bot Telegram rodando...")
bot.polling()
