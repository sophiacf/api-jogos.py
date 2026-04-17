from flask import Flask, jsonify
import os

app = Flask(__name__)

jogos = [
    {"id": 1, "jogo": "Ori and the blind florest"},
    {"id": 2, "jogo": "Avakin life"},
    {"id": 3, "jogo": "Roblox"},
    {"id": 4, "jogo": "Animal Jam"},
    
]

@app.route("/filmes", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de jogos - Acesse /jogos"})

@app.route("/", methods=["GET"])
def listar_jogos():
    return jsonify(jogos)

if __name__ == "__main__":
    port = int(os.environ.get("PORT" , 5000))
    app.run(host="0.0.0.0", port=port)