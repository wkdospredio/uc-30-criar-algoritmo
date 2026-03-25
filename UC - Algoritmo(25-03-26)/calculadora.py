a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "erro (divisão por zero)"
    return a / b

print("Soma:", soma(a, b))
print("Subtração:", subtracao(a, b))
print("Multiplicação:", multiplicacao(a, b))
print("Divisão:", divisao(a, b))