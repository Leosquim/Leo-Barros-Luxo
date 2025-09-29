from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/tts", methods=["GET", "POST"])
def tts():
    if request.method == "POST":
        data = request.json or {}
        texto = data.get("texto", "Nada enviado")
        return jsonify({"mensagem": f"Texto recebido para conversão em voz: {texto}"})
    else:
        return jsonify({"mensagem": "Rota TTS está online e aguardando POST!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003, debug=True)
