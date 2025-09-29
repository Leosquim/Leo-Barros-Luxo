from flask import Flask, jsonify
import pandas as pd
from datetime import datetime

app = Flask(__name__)

@app.route("/api/export_excel")
def export_excel():
    dados = [
        {"ativo": "EURUSD", "lucro": 120},
        {"ativo": "GBPUSD", "lucro": -50}
    ]

    df = pd.DataFrame(dados)
    nome_arquivo = f"resultados_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    df.to_excel(nome_arquivo, index=False)

    return jsonify({"mensagem": "Relatório gerado", "arquivo": nome_arquivo})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5004, debug=True)
