#sem dicionário
matricula1 = 2026001
nome1 = "Ana silva"
telefone1 = "9998-8889"

#com dicionário
aluno = {
    "matricula": 2026001,
    "nome": "carla",
    "telefone1": "9998-8889"

}
print(aluno)

contato = {
    "@Neymarjr": "Neymar Jr.",
    "@brunamarquezine": "Bruna M.",
    "@paollaoliveira": "paolla O.",
    "@vampeta": "vampeta.10",
    "@joaocarlos21": "João C."
}

print(contato)
print(type(contato))

#Acesso direto
print(contato["@Neymarjr"])

# Acesso seguro com get()
print(contato.get("@vampeta10"))
print(contato.get("inesxistente"))
print(contato.get("inesxistente", "Não encontrado"))

#add novo elemento
contato["@Neymarjr"] = "Neymar Jr."
print("Após add ",contato)

contato.update({
    "@brunamarquezine": "Bruna Marquezine",
    "@vampeta10": "vampeta.10",
})

print("Após Atualização:", contato)



#pop: remove e retorna
removido = contato.pop("@vamepeta10")
print(f"Removido:{removido}")
print("Após o pop: ", contato)


# del remove sem retornar
del contato["@paollaoliveira"]
print("Após o del:", contato)

#clear esvazia tudo
copia = dict(contato)
contato.clear()
print("Após clear: ", contato)
print("copia", copia)

print("Número de contatos: ", len(contato)) #tamanho dicio

#verificar existência
if "@joaocarlos21" in contato:
    print(f"Encontrado: {contato['@joao']}")

if "@inexistente" in contato:
    print("Existe")
