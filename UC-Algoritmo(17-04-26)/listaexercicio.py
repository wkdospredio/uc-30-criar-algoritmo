#1
print("Hello, World")

#2
idade = int(input("Digite sua idade:"))
if idade >= 16:  
    print("pode votar")

else: print("Não pode votar")

#3
total = 0
valor = 1

while valor != 0:
    valor = float(input("Valor: "))
    total += valor

print("Total:", total)

#4
def calcular_imc(peso, altura):
    imc = peso / (altura * altura)
    
    if imc < 24.9:
        print("Magro")
    else:
        if imc <= 28.5:
            print("Normal")
        else:
            print("Acima do peso")

try:
    peso = float(input("Digite o peso: "))
    altura = float(input("Digite a altura: "))
    
    calcular_imc(peso, altura)

except:
    print("Digite apenas números!")

#5
amigos = ["kauã","neymar","vampeta","ronaldo"]

quantidade = (amigos)

print("Quantidades de amigos:",quantidade)
if quantidade % 2 == 0:
     print("voçê tem um numero par de amigos")
else:print("voçê tem um numero impar de amigos")

6#
temperaturas = [22.5, 24.0, 21.8, 25.2, 23.0, 26.5, 20.0]

soma_temperaturas = 0.0

quantidade_dias = len(temperaturas)
for temp in temperaturas:
    soma_temperaturas += temp

media = soma_temperaturas / quantidade_dias

print(f"Temperaturas registradas: {temperaturas}")
print(f"Média de temperatura da semana: {media:.2f}°C")

#7
vendas = [100, 55, 230, 40, 105, 80, 15]

soma_pares = 0

for valor in vendas:
    
    if valor % 2 == 0:
        soma_pares += valor

print(f"Lista de vendas: {vendas}")
print(f"Soma dos valores pares: {soma_pares}")

#11
idades = [22, 18, 30, 15, 20]

idades.sort()

print(idades)





