#!/usr/src/app/venv/bin/python
from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
@app.route('/title/<title>')
def index(title=None):
	if title:
		return render_template('index.html',title=title,msg="Hello, world!")
	else:
		return render_template('index.html',msg="Hello, world!")

@app.route('/form',methods=['GET','POST'])
def process_form():
	nome=request.form['nome']
	idade=request.form['idade']
	sexo=request.form['sexo']
	return render_template('tabulado.html',nome=nome,idade=idade,sexo=sexo)

@app.errorhandler(404)
def error_pager(error):
	return render_template('404.html')

if __name__ == "__main__":
	app.run(host='0.0.0.0',port=int("80"))
