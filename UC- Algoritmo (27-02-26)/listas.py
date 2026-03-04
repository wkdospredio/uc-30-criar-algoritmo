Nome1 = "Weverton"
nome2 = "Mateus"
Nome3 = "Kawan"

nomes = [ "Weverton, Mateus, Kawan."]
print(nomes)

dados = ["elis" , 0, 1.70,True]
print(dados)
print(type(dados))
print(type(dados[0]))
print(type(dados[1]))
print(type(dados[2]))
print(type(dados[3]))

lista = ["Cachorro" , "Gato"]
lista.append("Coelho") #add no fim de lista
print("Atualizado" , lista)

lista.insert(1, "Grilo") #add na posição determinada
print("Atualizado:" , lista)

lista.extend(["macaco" , "Ovelha"]) #add mais de um dado de uma vez
print("Lista Final", lista)