n = int(input("Números infectados no dia 8"))
r = int(input("Fator reprodutivo da infecção"))
p = int(input("Numero alvo de pessoas infectadas"))

total = n 
novos = n
dias = 0


while total < p:
    novos = novos * r
    total += novos
    dias += 1

print(dias)