from flask import Flask, render_template

app = Flask(__name__)

@app.route('/autenticar')
def autenticar():
    return render_template('formulario.html')

if __name__ ==  '__main__':
    app.run(debug=True)