#Sem função 
print("Python é fácil")
print("Python é fácil")
print("Pythoon é fácil")

# Com função
def exibirMensagem():
    print("Óla, mundo")

exibirMensagem()

#Função com parametro
def saudar(nome):
    print(f"Òla, {nome}!")


saudar("weverton")
saudar("kauã")

def exibirMensagem(nome, mensagem):
    print(f"{mensagem},{nome}")

exibirMensagem ("Weverton", "Bom dia")    

#Parâmetros nomeados
exibirMensagem(nome = "weverton", mensagem = "Boa noite") 


#Função que retorna média
def calcularmedia(nota1, nota2):
    media = (nota1 + nota2)
    return media

resultado = calcularmedia(8.0,9.0)
print(f"Média:{resultado}")