from flask import Flask, render_template_string

app = Flask(__name__)
    
@app.route('/filme/<genero>')
def filme(genero):

    filmes = {

        "acao": {
            "titulo": "Filmes de Ação",
            "imagem": "https://cdn-icons-png.flaticon.com/512/744/744922.png",
            "descricao": "Filmes cheios de aventura, explosões, perseguições e muita adrenalina."
        },

        "comedia": {
            "titulo": "Filmes de Comédia",
            "imagem": "https://cdn-icons-png.flaticon.com/512/742/742751.png",
            "descricao": "Filmes divertidos que fazem o público rir e se divertir."
        },

        "terror": {
            "titulo": "Filmes de Terror",
            "imagem": "https://cdn-icons-png.flaticon.com/512/3132/3132693.png",
            "descricao": "Filmes assustadores com suspense, tensão e cenas de arrepiar."
        }
    }

    if genero in filmes:

        dados = filmes[genero]

        pagina = f"""
        <html>
            <head>
                <title>{dados['titulo']}</title>
            </head>

            <body style="font-family: Arial; text-align:center;">

                <h1>{dados['titulo']}</h1>

                <img src="{dados['imagem']}" width="200">

                <p>{dados['descricao']}</p>

            </body>
        </html>
        """

        return render_template_string(pagina)

    else:

        return """
        <h1>Gênero não disponível</h1>

        <p>
            Os gêneros disponíveis são:
            ação, comédia e terror.
        </p>
        """

if __name__ == '__main__':
    app.run(debug=True)