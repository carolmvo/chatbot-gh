from flask import Flask, render_template, request, jsonify
from nltk.chat.util import Chat, reflections

app = Flask(__name__)

pares = [
    [
        r"(?i)\b(oi|olá|e aí|ei|bom dia|boa tarde|boa noite)\b", 
        ["Oi! Seja bem-vindo ao CozinhIA 🍳 Me conta o que você quer cozinhar hoje!"]
    ],

    [
        r"(?i)^.*(ajuda|me ajudar|como funciona|o que você faz).*$", 
        ["Eu te ajudo com receitas! Me diga um ingrediente ou tipo de prato que você tem em mente"]
    ],

    [
        r"(?i).*(bolo de chocolate).*", 
        ["Pra fazer bolo de chocolate: 2 ovos, 2 xícaras de açúcar, 1 xícara de leite, 2 de farinha, 1 colher de fermento e 1/2 xícara de chocolate em pó. Asse a 180ºC por 30 minutos. Quer tentar outro sabor de bolo ou mudar o recheio?"]
    ],
    [
        r"(?i).*(bolo de cenoura).*", 
        ["Bolo de cenoura: Bata 3 cenouras, 3 ovos, 1 xícara de óleo. Junte com 2 de açúcar, 2 de farinha, 1 colher de fermento. Asse por 40 minutos a 180ºC. Quer alguma sugestão de cobertura ou outra receita?"]
    ],
    [
        r"(?i).*(bolo de morango).*", 
        ["Bolo de morango: 2 xícaras de farinha, 1 de açúcar, 2 ovos, 1/2 xícara de óleo, 1 xícara de leite, 1 colher de fermento. Asse por 30 minutos. Quer mais alguma ideia doce?"]
    ],

    [
        r"(?i).*\b(quero|sim|quero|claro|por favor)\b.*", 
        ["Perfeito! Me diga um ingrediente ou tipo de receita que você quer que eu te mostre"]
    ],
    [
        r"(?i).*\b(nao obrigada|nao obrigado|nao|não|não obrigado|não obrigada|agora não|tô de boa|to de boa|agora nao)\b.*", 
        ["Sem problemas. Estarei por aqui quando quiser cozinhar algo gostoso. Até a próxima!"]
    ],

    [
        r"(?i).*(biscoitos de chocolate).*", 
        ["Biscoitos de chocolate: 2 xícaras de farinha, 1 de açúcar, 1/2 de manteiga, 1 ovo, baunilha, 1 xícara de chocolate picado. Asse por 15 min a 180ºC. Quer uma sobremesa diferente agora?"]
    ],
    [
        r"(?i).*(torta de limão).*", 
        ["Torta de limão: Base de biscoito e manteiga. Recheio com leite condensado, creme de leite e suco de limão. Geladeira por 2h. Quer experimentar outra torta ou sobremesa gelada?"]
    ],
    [
        r"(?i).*(brigadeiro).*", 
        ["Brigadeiro de micro-ondas: Misture 1 lata de leite condensado, 2 colheres de chocolate em pó, 1 de manteiga. Micro por 2 min, mexe, depois mais 1 min. Quer aprender outro doce rápido?"]
    ],
    [
        r"(?i).*(salada de frutas).*", 
        ["Salada de frutas: Corte frutas frescas e adicione suco de laranja. Dá pra incrementar com iogurte ou granola. Quer sugestões com frutas diferentes?"]
    ],
    [
        r"(?i).*(bolo de caneca).*", 
        ["Bolo de caneca: 1 ovo, 2 colheres de açúcar, 2 de chocolate, 2 de farinha, 1 de óleo e 1 de leite. Micro-ondas por 1:30 min. Quer outra receita de micro-ondas?"]
    ],

    [
        r"(?i).*(pizza caseira).*", 
        ["Pizza caseira: Massa com farinha, fermento, água morna, sal e azeite. Cresça 1h, abra e cubra. Quer sugestões de recheio pra sua pizza?"]
    ],
    [
        r"(?i).*(omelete).*", 
        ["Omelete simples: 2 ovos batidos com sal. Frite com óleo e adicione o que quiser: queijo, legumes, etc. Quer ideias de recheio leve ou proteico?"]
    ],
    [
        r"(?i).*(pão de queijo).*", 
        ["Pão de queijo: 1 xícara de polvilho, 1/2 de queijo, 1 ovo, sal e azeite. Modele e asse por 20 min. Quer uma variação com mais queijo ou temperos?"]
    ],

    [
        r"(?i).*(doce|sobremesa).*", 
        ["Adoro doces! Posso sugerir brigadeiro, bolo de caneca ou torta de limão. Algum desses te interessa?"]
    ],
    [
        r"(?i).*(salgado|lanche).*", 
        ["Pra um lanche salgado, temos pão de queijo, pizza ou omelete. Qual desses você quer tentar?"]
    ],
    [
        r"(?i).*(jantar|almoço).*", 
        ["Pra um jantar leve ou rápido, recomendo pizza caseira ou omelete. Quer outra opção?"]
    ],

    [
        r"(?i).*(tchau|obrigado|obrigada|valeu|até logo|até mais).*", 
        ["Foi um prazer cozinhar com você! Volte sempre que quiser mais receitas. Até logo"]
    ],

    [
        r"(.*)", 
        ["Hmm... não entendi muito bem... Tenta me dizer um ingrediente ou tipo de prato que você gostaria de preparar!"]
    ]
]

chatbot = Chat(pares, reflections)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def get_bot_response():
    user_msg = request.json["msg"]
    response = chatbot.respond(user_msg)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)