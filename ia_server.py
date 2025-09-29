from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/ia-sinal")
def ia_sinal():
    # Simulação de sinal de compra/venda
    sinal = {
        "ativo": "EURUSD",
        "acao": "COMPRA",
        "confianca": 0.87
    }
    return jsonify(sinal)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
