import requests

url = "http://127.0.0.1:5002/news/ie"  # Irlanda
resp = requests.get(url, timeout=20)
print("Status Code:", resp.status_code)

data = resp.json()
arts = data.get("articles", [])
print(f"Total de artigos: {len(arts)}")

for i, a in enumerate(arts[:5], 1):
    print(f"{i}. {a.get('title')}\n   {a.get('url')}")
