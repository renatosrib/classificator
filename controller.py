from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return 'Sistema IMDB!'

@app.route('/cadastrar', methods=['POST'])
def cadastro():
    return 'registrado com sucesso'

@app.route('/listar')
def listar():
    return '-Filme 1\n- Filme2'