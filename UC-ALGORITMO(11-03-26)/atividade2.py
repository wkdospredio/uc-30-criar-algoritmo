# QUESTAO1
salario_base = 3500.00
bonus = 800.00
desconto = 250.00

# Cálculos
salario_bruto = salario_base + bonus
salario_liquido = salario_bruto - desconto

# --- Resultados ---

print(f"Salário Bruto: R$ {salario_bruto}")
print(f"Salário Líquido: R$ {salario_liquido}")

print("-" * 30)

# Verificando os tipos de dados
print(f"Tipo da variável salario_base: {type(salario_base)}")
print(f"Tipo da variável bonus: {type(bonus)}")
print(f"Tipo da variável desconto: {type(desconto)}")
print(f"Tipo da variável salario_bruto: {type(salario_bruto)}")
print(f"Tipo da variável salario_liquido: {type(salario_liquido)}")


