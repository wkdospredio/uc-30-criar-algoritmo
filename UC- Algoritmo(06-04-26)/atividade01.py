import random

numero = random.randint(1, 100)
tentativas = 0

while True:
    palpite = int(input("Digite um número: "))
    tentativas += 1

    if palpite < numero:
        print("maior")
    elif palpite > numero:
        print("menor")
    else:
        print("acertou!")
        print("tentativas:", tentativas)
        break