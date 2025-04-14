from flask import Flask, render_template, request, jsonify
import random
import nltk
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

# Definindo os pares de perguntas e respostas
pares = [
    [r"(?i)oi|olá|e aí|ei", ["Olá! Bem-vindo ao Chatbot de Perguntas Aleatórias! Vamos começar!"]],
    [r"(?i).*", ["Estou aqui para responder suas perguntas. Tente me perguntar algo!"]],
]

reflexoes_personalizadas = {
    "eu": "você",
    "meu": "seu",
    "minha": "sua",
    "sou": "é",
    "estou": "está",
    "você": "eu",
    "seu": "meu",
    "sua": "minha",
    "é": "sou"
}

chatbot = Chat(pares, reflections=reflexoes_personalizadas)

# Página principal
@app.route("/")
def home():
    return render_template("index.html")

# Rota de interação do chatbot
@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.form["message"]
    response = chatbot.respond(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
