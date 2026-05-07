from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/pizzaria/<sabor>')
def pizzaria(sabor):

    pizzas = {

        "calabresa": {
            "nome": "Pizza de Calabresa",
            "imagem": "https://cdn-icons-png.flaticon.com/512/3595/3595455.png",
            "descricao": "Uma pizza tradicional feita com calabresa, cebola e bastante queijo."
        },

        "frango": {
            "nome": "Pizza de Frango",
            "imagem": "https://cdn-icons-png.flaticon.com/512/6978/6978255.png",
            "descricao": "Pizza recheada com frango desfiado e queijo derretido."
        },

        "mussarela": {
            "nome": "Pizza de Mussarela",
            "imagem": "https://cdn-icons-png.flaticon.com/512/3132/3132693.png",
            "descricao": "Uma das pizzas mais populares, preparada com muito queijo mussarela."
        }
    }
    if sabor in pizzas:

        dados = pizzas[sabor]

        pagina = f"""
        <html>
            <head>
                <title>{dados['nome']}</title>
            </head>

            <body style="font-family: Arial; text-align:center;">

                <h1>{dados['nome']}</h1>

                <img src="{dados['imagem']}" width="250">

                <p>{dados['descricao']}</p>

            </body>
        </html>
        """

        return render_template_string(pagina)

    else:

        return """
        <h1>Sabor não disponível</h1>

        <p>
            Os sabores disponíveis são:
            calabresa, frango e mussarela.
        </p>
        """


if __name__ == '__main__':
    app.run(debug=True)