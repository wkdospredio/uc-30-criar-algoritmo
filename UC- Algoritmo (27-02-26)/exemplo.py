numero1 = float(input("Digite o 1º numero:"))
numero2 = float(input("Digite o 2º numero:"))
 
soma = numero1 + numero2

produto = numero1 * numero2

soma = numero1 + numero2
produto = numero1 * numero2

print("soma" , soma)
print("produto", produto)



numero = int(input("Digite um Numero : "))

if (numero % 2 == 0):
    resultado = numero ** 2
else:
    resultado = numero ** 3

    print("resultado", resultado)

usuario = input("Digite o user ")
senha   = input("Digite sua senha ")

if (usuario == "procopio" and senha == "12345") or (usuario == "paiva" and senha == "54321"):
    print("Seja Bem Vindo")

else:

 print("Usuário e senha não conferem.")

nome = input("Digite seu nome: ")
senhaCorreta = "123456"
 
tentativa = 3

while  tentativa > 3:
    senha = input("Digite sua senha:")

    if senha == senhaCorreta:
       print(f"Óla, {nome}! Seja Bem-vindo!")
       break
    else:
       tentativa -= 1

    if tentativa == 2:
       print("Senha errada! Você tem 2 tentativa.")
    elif tentativa == 1:
       print("Senha errada! Você em  1 tentativa.")
    else:
       print("Senha bloqueada!")