import requests

url = "http://127.0.0.1:5002/news"  # endpoint do servidor de notícias
response = requests.get(url)

print("Status Code:", response.status_code)
print("Resposta JSON:", response.json())
