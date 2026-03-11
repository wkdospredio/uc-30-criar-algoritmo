# QUESTAO2
distancia_percorrida = 450  # km
consumo_carro = 8           # km/litro
preco_litro = 5.50          # R$ por litro

# --- Processamento (Cálculos) ---
# Calculamos primeiro quantos litros foram necessários para a viagem
litros_consumidos = distancia_percorrida / consumo_carro

# Multiplicamos os litros pelo valor de cada litro
custo_total = litros_consumidos * preco_litro

# Saída de Resultados
print("### Relatório de Gastos - Maria ###")
print(f"Distância percorrida: {distancia_percorrida} km")
print(f"Consumo médio do veículo: {consumo_carro} km/l")
print(f"Preço do combustível: R$ {preco_litro:.2f}")
print("-" * 35)
print(f"Total de combustível usado: {litros_consumidos:.2f} litros")
print(f"Custo total com combustível: R$ {custo_total:.2f}")