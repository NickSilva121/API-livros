from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'titulo': 'As Crônicas de Nárnia - O Leão, a Feiticeira e o Guarda-Roupa',
        'autor': 'C.S. Lewis'
    },
    {
        'id': 2,
        'titulo': 'Harry Potter e a Pedra Filosofal',
        'autor': 'J.K Howling'
    },
    {
        'id': 3,
        'titulo': 'Os 7 Hábitos das Pessoas Altamente Eficazes',
        'autor': 'Sean Covey'
    },
]

# Consulta (todos)
@app.route('/livros', methods=['GET'])
def get_livros():
    return jsonify(livros)
# Consulta (id)
@app.route('/livros/<int:id>',  methods=['GET'])
def get_livro_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
# Edição
@app.route('/livros/<int:id>', methods=['PUT'])
def edit_livro_id(id):
    livro_alt = request.get_json()
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alt)
            return jsonify(livros[indice])
# Criar
@app.route('/livros', methods=['POST'])
def create_livro():
    new_livro = request.get_json()
    livros.append(new_livro)

    return jsonify(livros)
# Exclusão
@app.route('/livros/<int:id>', methods=['DELETE'])
def exclui_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]
    return jsonify(livros)
app.run(port=5000, host='127.0.0.1', debug=False)