# tupla eh como uma lista imutavel

cordenadas = (10.08234708, 1.02432685)
print(cordenadas)

# unpaking
latitude, longitude = cordenadas
print(latitude)
print(longitude)

# bonus 1: 2mzn por venda
# bonos 2: 1% do valor das vendas

vendas_funcionarios = [10, 20, 30, 50, 50, 600, 250, 40]

# tuplas para funcoes

def calcular_bonus(lista_vendas):
    bonus1 = 2 * len(lista_vendas)
    bonus2 = 0.01 * sum(lista_vendas)
    return bonus1, bonus2

resultado_bonus = calcular_bonus(vendas_funcionarios)
bonus1, bonus2 = resultado_bonus
print(bonus1)
print(bonus2)

# tuplas com for

lista_vendas = [("Delson", 1000), ("Carolina", 200), ("Valter", 500)]
for vendedor, vendas in lista_vendas:
    print(f"O {vendedor} vendeu {vendas}")
