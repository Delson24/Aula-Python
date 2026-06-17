# Exercício 1: Dashboard de Vendas (Análise de Dados) Você recebeu uma lista com as vendas diárias de uma equipe: vendas = [1500, 2000, 800, 3500, 1200]. Crie um programa que exiba um pequeno relatório contendo:
# 1.	O total de vendas na semana.
# 2.	A média de vendas diária.
# 3.	O valor da melhor venda e da pior venda do período.

# total vendas na semana
lista_vendas =  [1500, 2000, 800, 3500, 1200]
total_vendas = sum(lista_vendas)
print("total de vendas na semana foi de", total_vendas)

# quantidade de vendas
quant_vendas = len(lista_vendas)
print("A quantidade de vendas e:", quant_vendas)

# media de vendas diaria
media_vendas_diaria = total_vendas / quant_vendas
print("A quantidade de vendas diarias e de:", media_vendas_diaria)

# O valor da melhor venda e da pior venda do período
melhor_venda = max(lista_vendas)
print("A melhor foi:", melhor_venda)

pior_venda = min(lista_vendas)
print("A pior venda foi:", pior_venda)