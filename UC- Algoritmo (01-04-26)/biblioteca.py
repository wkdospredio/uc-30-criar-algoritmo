        #dicionario para armazenar os livros
catalogo = {}

#dicionario para armazenar os emprestimos
emprestimo = {}

#lista para armazenar o historico de transição
historico = {}

def adicionarLivro(codigo, titulo, autor, quantidade):
    if codigo in catalogo:
        print(f"Erro: Livro com codigo {codigo} já existe!")
        return False
    
    catalogo[codigo] = {
        "titulo": titulo,
        "autor": autor,
        "quantidade": quantidade
    }

    print(f"Livro '{titulo}' adicionado com sucesso")
    return True


#funcao emprestar livro
def emprestarLivro(codigo, nomeAluno):
    if codigo not in catalogo:
        print(f"Erro: Livro com código {codigo} não encontrado")
        return False
    
    if catalogo[codigo]["quantidade"] <= 0:
        print(f"Erro: '{catalogo[codigo['titulo']]}' não encontrado.")
        return False
    

    livroAluno = contarLivrosAlunos(nomeAluno)
    if livroAluno >= 2:
        print (f"Erro: Aluno já pegou a quantidade máxima")
        return False
    
    if codigo in emprestimo and nomeAluno in emprestimo[codigo]:
        print(f"Erro: {nomeAluno} já pegou este livro.")
        return False
    

    if codigo not in emprestimo:
        emprestimo[codigo] = []

    emprestimo[codigo].append(nomeAluno)

    catalogo[codigo]["quantidade"] -= 1

    historico.append({
        "tipo": "emprestimo",
        "codigo": codigo,
        "titulo": catalogo[codigo]["titulo"],
        "aluno": nomeAluno
    })

    print(f"{nomeAluno} pegou '{catalogo[codigo['titulo']]}' com sucesso")
    return True



#funcao devolver livro
biblioteca = ["O Hobbit", "1984", "Dom Casmurro", "O Pequeno Príncipe"]

def devolverLivro(codigo, biblioteca):
    if codigo in biblioteca:
        return f"O livro '{codigo}' está disponível"
    else:
        return f"Desculpe, livro indisponível"


devolverLivro("0001","A Cartomante", "Machado de Assis", 2)

historico.append()