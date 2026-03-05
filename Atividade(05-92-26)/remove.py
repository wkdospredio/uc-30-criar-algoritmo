nomes = ["kauã", "kawan", "wilder", "elis"]
print("Nomes: ", nomes)

nomes.remove ("kawan")
print("Lista atualizada: ", nomes)

#removido = nomes.pop()
removido = nomes.pop()
print(f"removido:{removido}")
print("Após pop(): ", nomes)

# del - remover pelo indice
del nomes [0]
print("Após del nomes[0] ", nomes)

# clear: esvazia
nomes.clear()
print("Lista atualizada: ", nomes)
