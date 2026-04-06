numeros = []

for i in range(8):
    numeros.append(int(input("Digite um número: ")))

repetidos = False
mostrados = []

for num in numeros:
    if numeros.count(num) > 1 and num not in mostrados:
        print(f"O número {num} apareceu {numeros.count(num)} vezes")
        repetidos = True
        mostrados.append(num)

if not repetidos:
    print("Nenhum número foi repetido")