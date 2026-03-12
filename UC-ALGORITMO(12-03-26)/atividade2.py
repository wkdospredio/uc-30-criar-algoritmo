horas = int(input("Quantas horas voçê trabalha por dia: "))
valor = int(input("Quanto voçê ganha por dia: "))

def calcularsSalario(horas, valor):
    soma = horas * valor
    produto = horas * valor
    return soma, produto

resultado = calcularsSalario(horas,valor)
print(f"Seu salário: {resultado}")