from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/api/news")
def news():
    noticias = [
        {"titulo": "Mercado sobe após dados positivos", "impacto": "positivo"},
        {"titulo": "Inflação preocupa investidores", "impacto": "negativo"}
    ]
    return jsonify(noticias)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
