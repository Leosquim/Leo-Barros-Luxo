import requests

# URL do seu servidor IA (que fala com o news_server)
url = "http://127.0.0.1:5001/ask"

# Mensagem pedindo notícias
data = {"message": "Quais são as últimas notícias?"}

headers = {"Content-Type": "application/json"}

response = requests.post(url, json=data, headers=headers)

print("Status Code:", response.status_code)
print("Resposta JSON:", response.json())
