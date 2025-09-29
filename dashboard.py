from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "status": "ok",
        "message": "Dashboard rodando 🚀",
        "services": {
            "ia": "http://127.0.0.1:5002",
            "news": "http://127.0.0.1:5001",
            "voice": "http://127.0.0.1:5003"
        }
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
