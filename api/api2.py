from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()


app = Flask (__name__)
CORS(app)
infos = [
    {
        'id': 1,
        'nome': 'Miguel',
        'email': 'miguel@gmail.com',
        'data': '23.03.2000'

    },

    {
        'id': 2,
        'nome': 'Jean',
        'email': 'jean@gmail.com',
        'data': '14.08.2005'

    }
]

#Adicionar informações
############################################################
@app.route('/infos',methods=['POST'])
def add_info():
    nova_info = request.get_json()
    infos.append(nova_info)
    return jsonify(infos)


#Consultar informções (Geral, por id, por nome, por email, por data de nascimento)
#------------------------------------------------------------
#Consultar as informações gerais
@app.route('/infos',methods=['GET'])
def obter_info():
    return jsonify(infos)
#-----------------------------------------------------------
#Consutar info por id
@app.route('/infos/<int:id>',methods=['GET'])
def obter_id(id):
    for info in infos:
        if info.get('id') == id:
            return jsonify(info)
#-----------------------------------------------------------        
#Consutar info por nome
@app.route('/infos/<string:nome>',methods=['GET'])
def obter_nome(nome):
    for info in infos:
        if info.get('nome') == nome:
            return jsonify(info)
#-----------------------------------------------------------
#Consutar info por email
@app.route('/infos/email/<string:email>', methods=['GET'])
def obter_email(email):
    for info in infos:
        if info.get('email') == email:
            return jsonify(info)
#-----------------------------------------------------------        
#Consutar info por data de nascimento
@app.route('/infos/data/<string:data>',methods=['GET'])
def obter_data(data):
    for info in infos:
        if info.get('data') == data:
            return jsonify(info)




#Editar informações por id, por nome, por email, por data de nascimento
#############################################################
#Editar uma info por id
@app.route('/infos/<int:id>',methods=['PUT'])
def editar_id(id):
    info_alterada = request.get_json()
    for indice,info in enumerate(infos):
        if info.get('id') == id:
            infos[indice].update(info_alterada)
            return jsonify(infos[indice])
#-----------------------------------------------------------
#Editar uma info por nome
@app.route('/infos/<string:nome>',methods=['PUT'])
def editar_nome(nome):
    info_alterada = request.get_json()
    for indice,info in enumerate(infos):
        if info.get('nome') == nome:
            infos[indice].update(info_alterada)
            return jsonify(infos[indice])
#-----------------------------------------------------------
#Editar uma info por email
@app.route('/infos/email/<string:email>',methods=['PUT'])
def editar_email(email):
    info_alterada = request.get_json()
    for indice,info in enumerate(infos):
        if info.get('email') == email:
            infos[indice].update(info_alterada)
            return jsonify(infos[indice])
#-----------------------------------------------------------
#Editar uma info por data de nascimento
@app.route('/infos/data/<string:data>',methods=['PUT'])
def editar_data(data):
    info_alterada = request.get_json()
    for indice,info in enumerate(infos):
        if info.get('data') == data:
            infos[indice].update(info_alterada)
            return jsonify(infos[indice])



#Excluir informações por id, por nome, por email, por data de nascimento
#############################################################       
#Excluir info por id
@app.route('/infos/<int:id>',methods=['DELETE'])
def excluir_id(id):
    for indice, info in enumerate(infos):
        if info.get('id') == id:
            del infos[indice]
    return jsonify(infos)
#------------------------------------------------------------
#Excluir info por nome
@app.route('/infos/<string:nome>',methods=['DELETE'])
def excluir_nome(nome):
    for indice, info in enumerate(infos):
        if info.get('nome') == nome:
            del infos[indice]
    return jsonify(infos)
#------------------------------------------------------------
#Excluir info por email
@app.route('/infos/email/<string:email>',methods=['DELETE'])
def excluir_email(email):
    for indice, info in enumerate(infos):
        if info.get('email') == email:
            del infos[indice]
    return jsonify(infos)
#------------------------------------------------------------
#Excluir info por data de nascimento
@app.route('/infos/data/<string:data>',methods=['DELETE'])
def excluir_data(data):
    for indice, info in enumerate(infos):
        if info.get('data') == data:
            del infos[indice]
    return jsonify(infos)



app.run(port=5000, host='localhost', debug=True)