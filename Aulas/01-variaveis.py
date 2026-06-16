# faturamento primeiro mes
faturamento = 1000
custo = 300
imposto = 0.2 # imposto de 20% = 0.2

lucro_1 = faturamento - custo - imposto * faturamento

# faturamento do segundo mes
faturamento = 790
custo = 300
imposto = 0.15 # impost de 15% = 0.15

lucro_2 = faturamento - custo - imposto * faturamento

print ("O lucro da loja foi de", lucro_1, "mzn")
print ("O lucro da loja foi de", lucro_2, "mzn")

margem_lucro = lucro_2 / faturamento

print(margem_lucro)

meta = 0.2

bateu_meta = margem_lucro >= meta
print(bateu_meta)

# mod % (resto da divisao)
# // (parte inteira)

duracao_contrato = 140 #meses
anos = duracao_contrato // 12
meses_sobra = duracao_contrato % 12
print("O contrato tem", anos, "anos e", meses_sobra, "meses")

