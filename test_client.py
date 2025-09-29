import requests
import os
from dotenv import load_dotenv

# carregar variáveis do .env
load_dotenv()

url = "http://127.0.0.1:5001/ask"   # IA Server
headers = {"Content-Type": "application/json"}

# 🔹 Aqui você pode mudar a mensagem e perguntar qualquer coisa
data = {"message": "Quais são as últimas notícias do Brasil?"}

response = requests.post(url, json=data, headers=headers)
print(response.json())
