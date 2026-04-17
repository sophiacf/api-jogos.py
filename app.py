from flask import Flask, jsonify
import os

app = Flask(__name__)

jogos = [
    {"id": 1, "titulo": "Ori and the blind florest", "plataforma": "steam"},
    {"id": 2, "titulo": "Avakin life", "plataforma": "mobile"},
    {"id": 3, "titulo": "Roblox", "plataforma": "pc e mobile"},
    {"id": 4, "titulo": "Animal Jam", "plataforma": "pc e mobile"},
    
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
