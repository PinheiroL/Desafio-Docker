from flask import Flask, Response, request         #response -> retorno da api     ||     request -> para trabalhar com um body
from flask_sqlalchemy import SQLAlchemy            # irá tratar diretamente com o banco de dado (para não precisar fazer tudo na mão)
import mysql.connector
import json

app = Flask(__name__)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:MySql2019!@localhost/crud_python_bd'  #passar caminho para o banco de dados

db = SQLAlchemy(app)

class Cliente (db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nome = db.Column(db.String(100))
    cpf = db.Column(db.String(12))
    telefone = db.Column(db.String(11))

    def to_json(self):
        return {"id": self.id, "cpf": self.cpf, "nome": self.nome, "telefone": self.telefone}

#Caso precisarmos criar a tabela do DB pelo codigo. Esecutar somente a primeira vez
#db.create_all()

# Consulta todos os clientes
@app.route("/clientes", methods=["GET"])
def seleciona_clientes():
    clientes_objetos = Cliente.query.all() #selecionar usuario
    clientes_json = [cliente.to_json() for cliente in clientes_objetos] # varrer a lista de clientes

    return gera_response(200, "clientes", clientes_json)

# Consulta cliente por id
@app.route("/cliente/<id>", methods=["GET"])
def seleciona_cliente(id):
    cliente_objeto = Cliente.query.filter_by(id=id).first() #filtar cliente
    cliente_json = cliente_objeto.to_json()

    return gera_response(200, "cliente", cliente_json)

# Cadastro do cliente
@app.route("/cliente", methods=["POST"])
def cria_cliente():
    body = request.get_json()

#try / execept -> gerar exceção caso não tenha os parametros
    try:
        cliente = Cliente(nome=body["nome"], cpf= body["cpf"], telefone= body["telefone"]) #classe cliente
        db.session.add(cliente) #adiciona cliente na seção // faz altomatico pela biblioteca SQLAlchemy 
        db.session.commit()
        return gera_response(201, "cliente", cliente.to_json(), "Criado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "cliente", {}, "Erro ao cadastrar")


# Atualização do cliente
@app.route("/cliente/<id>", methods=["PUT"])
def atualiza_cliente(id):
    cliente_objeto = Cliente.query.filter_by(id=id).first() #selecionar cliente
    body = request.get_json() #obter modificações em body

    try:
        if('nome' in body):
            cliente_objeto.nome = body['nome']
        if('telefone' in body):
            cliente_objeto.telefone = body['telefone']
        
        db.session.add(cliente_objeto)
        db.session.commit()
        return gera_response(200, "cliente", cliente_objeto.to_json(), "Atualizado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "cliente", {}, "Erro ao atualizar")

# Remoção do cliente
@app.route("/cliente/<id>", methods=["DELETE"])
def deleta_cliente(id):
    cliente_objeto = Cliente.query.filter_by(id=id).first()

    try:
        db.session.delete(cliente_objeto)
        db.session.commit()
        return gera_response(200, "cliente", cliente_objeto.to_json(), "Deletado com sucesso")
    except Exception as e:
        print('Erro', e)
        return gera_response(400, "cliente", {}, "Erro ao deletar")


#Metodo responsavel por gerar o modelo de response padrão da API
def gera_response(status, nome_do_conteudo, conteudo, mensagem=False):
    body = {}
    body[nome_do_conteudo] = conteudo

    if(mensagem): #testando se mesangem é falsa
        body["mensagem"] = mensagem

    return Response(json.dumps(body), status=status, mimetype="application/json")


app.run()