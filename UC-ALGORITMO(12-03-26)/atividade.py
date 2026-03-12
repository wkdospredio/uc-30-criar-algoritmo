numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))


def soma_e_produto(numero1, numero2):
    soma = numero1 + numero2
    produto = numero1 * numero2
    return soma, produto



resultado = soma_e_produto(numero1,numero2)
print(f"A soma e o produto é igual a: {resultado}")
