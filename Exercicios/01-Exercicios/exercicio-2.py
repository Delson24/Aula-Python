#Exercício 2: Controle de Estoque de E-commerce (Logística)|| Cenário: Um e-commerce começou o dia com 250 unidades de um smartphone no estoque. Durante o dia, foram vendidos 78 unidades e chegaram mais 100 unidades de um fornecedor. Objetivo: Atualize a variável de estoque e exiba o saldo final. 

quant_inicial = 250
quant_vendidos = 78
quant_adicional = 100
quant_inicial = quant_inicial - quant_vendidos
print(quant_inicial)

quant_final = quant_inicial + quant_adicional
print(quant_final)
