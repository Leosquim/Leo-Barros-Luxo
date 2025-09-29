import os
import requests
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")

mensagem = "✅ Olá Léo! Seu bot do Telegram já está funcionando 🚀"

url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

res = requests.post(url, data={"chat_id": CHAT_ID, "text": mensagem})

print(res.json())
