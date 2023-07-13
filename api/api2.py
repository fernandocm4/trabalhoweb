from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

livros = [
    {
        'id': 1,
        'título': 'As Armas da Persuasão',
        'autor': 'Robert B. Cialdini'
    },
    {
        'id': 2,
        'título': 'Sherlock Holmes O Cão dos Baskerville',
        'autor': 'Arthur Conan Doyle'
    },
    {
        'id': 3,
        'título': 'Mitologia Nórdica',
        'autor': 'Neil Gaiman'
    },
    {
        'id': 4,
        'título': 'A Biblioteca da Meia Noite',
        'autor': 'Matt Haig'
    },
]


CREATE_LIVROS_TABLE = ("CREATE TABLE IF NOT EXISTS livros (id SERIAL PREMARY KEY, titulo TEXT, autor TEXT);")
INSERT_LIVROS_RETURN_ID = ("INSERTO INTO livros (titulo) VALUES (%s) RETURNING id;")


@app.route('/livros',methods=['GET'])
def obter_livros():
    return jsonify(livros)

@app.route('/livros/<int:id>',methods=['GET'])
def obter_livro_por_id(id):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
        
@app.route('/livros/<int:id>',methods=['PUT'])
def editar_livro_por_id(id):
    livro_alterado = request.get_json()
    for indice,livro in enumerate(livros):
        if livro.get('id') == id:
            livros[indice].update(livro_alterado)
            return jsonify(livros[indice])

@app.route('/livros',methods=['POST'])
def incluir_novo_livro():
    novo_livro = request.get_json()

    '''titulo = novo_livro['id': 5,'título': 'taqp','autor': 'sla']
    with connection:
        with connection.cursor() as cursor:
            cursor.execute(CREATE_LIVROS_TABLE)
            cursor.execute(INSERT_LIVROS_RETURN_ID, (titulo,))
            room_id = cursor.fetchone()[0]'''

    livros.append(novo_livro)  
    return jsonify(livros)

@app.route('/livros/<int:id>',methods=['DELETE'])
def excluir_livro(id):
    for indice, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[indice]

    return jsonify(livros)

app.run(port=5000,host='localhost',debug=True)