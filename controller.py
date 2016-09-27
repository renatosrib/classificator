from flask import Flask, request, current_app

app = Flask(__name__)

@app.route('/')
def home():
    return 'Sistema IMDB!'

@app.route('/form')
def cadastro_categoria():
    return current_app.send_static_file('form.html')

@app.route('/cadastrar', methods=['POST'])
def cadastro():
    return str(request.form['category']) + 'registrado com sucesso'

@app.route('/listar')
def listar():
    return '-Filme 1\n- Filme2'