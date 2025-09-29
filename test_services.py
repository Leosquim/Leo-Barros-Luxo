import requests

services = {
    "IA": "http://127.0.0.1:5001/api/ia-sinal",
    "NEWS": "http://127.0.0.1:5002/api/news",
    "VOICE": "http://127.0.0.1:5003/tts",
    "EXCEL LOOP": "http://127.0.0.1:5004/api/export_excel",
    "DASHBOARD": "http://127.0.0.1:5000/"
}

print("🟢 Testando serviços do robô...")

for name, url in services.items():
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            print(f"✅ {name} respondeu em {url} → 200 OK")
        else:
            print(f"⚠️ {name} respondeu mas com erro → {response.status_code}")
    except Exception as e:
        print(f"❌ {name} falhou: {e}")
