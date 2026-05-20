from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/autenticar', methods=['GET', 'POST'])
def autenticar():
    if request.method == 'POST':
        usuario = request.form['Usuário']
        senha = request.form['senha']
        return f"Usuário: {usuario}, Senha: {senha}"
    return render_template('formulario.html')

if __name__ ==  '__main__':
    app.run(debug=True)