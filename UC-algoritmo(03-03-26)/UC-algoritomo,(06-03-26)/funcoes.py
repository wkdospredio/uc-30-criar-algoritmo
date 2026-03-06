notas = [7.5, 8.0, 9.5, 6.0, 8.5]
print("Notas: ", min(notas))

print("Menos ", min(notas))
print("Maior", min(notas))
print("Soma ", min(notas))
print("Media", min(notas))


nomes = ["Adriano", "breno", "Carla","Daniel"]

# apenas o elemento
print("Usando FOR simples: ")
for nome in nomes:
   print(f"Olá, {nome}!")

# índice e elemento
print("\n Usando enuerate: ")
for indice, nome in enumerate(nomes):
   print(f"posição {indice}: {nome}")


   original = ["A", "B", "C"]
   copia = list(original)

   print("Original: ", original)
   print("Cópia: ", copia)
   print("São iguai: ", original == copia)

   copia.append("D")
   print("Original", original)
   print("Cópia: ", copia)
   print("São iguais", original == copia)