# CRUD API EM PYTHON


**Resumo**:
Esse projeto é uma api simples em python para gerenciamento de clientes conectada com banco de dados mysql. 
<br/>Nessa api é posssível cadastrar, consultar, excluir e atualizar dados dos clientes.

## Configuração de ambiente:

Programas utilizados:
* Visual Studio Code
* Git Bash
* Python 3.6+
* Docker
* Postman

Frameworks utilizados:
* Flask
* SQLAlchemy 
* Mysql.connector
* Json

Comandos para instalar bibliotecas necessárias para execução da aplicação em python:
* python get-pip.py
* pip install flask
* pip install flask_sqlalchemy
* pip mysql-connector-python
* pip install mysqlclient
* pip install mysql-connector-python

Imagens Docker:
* mysql:5.7 - Servidor de banco de dados MySQL
* adminer - Ferramenta para administração do BD MySQL

Como Executar a aplicação:
* Navegar até a pasta do projeto
* Subir o servidor de banco de dados: 
```console
docker-compose up -d
```
* Na primeira execução será necessário executar o script SQL localizado no arquivo Desafio Docker\Scripts SQL\CreateDataBase.sql
* Executar a aplicação:
```console
python app.py
```
* Realizar chamadas na API pelo Postman utilizando a collection do projeto (CRUD API Python.postman_collection.json)