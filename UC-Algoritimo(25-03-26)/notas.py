def estatistica(*notas):
    soma = sum(notas)
    media = sum(notas) / len(notas)
    maior = max(notas)
    menor = min(notas)
    return soma, media, maior, menor

print(estatistica(5, 8, 6, 9))
