from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    nome = "Helô"
    return render_template('index.html', title='Página Inicial', usuario=None, 
    nome=None, title= 'Home')

@app.route('/usuario')
def usuario():
    usuario = {'nome': 'Helô', 'email': 'robinhohexa6@gmail.com'}
    return render_template('index.html', title='Página do Usuário', usuario=usuario, nome=None)

@app.route('/dados', defaults = {"nome": "usuário comum"})
@app.route('/dados/<nome>')
def dados(nome):
    return f'Olá, {nome}!'

@app.route('/semestre/<int:x>')
def semestre(x):
    return f'Você está no semestre' + str(x)

@app.route('/pagamento/<float:valor>')
def pagamento(valor):
    return f'Você pagou: '+ str(valor)

if __name__ == '__main__':
    app.run(debug=True)