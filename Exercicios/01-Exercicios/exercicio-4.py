#Exercício 4: Análise de Margem de Lucro (Financeiro) || Cenário: Uma consultoria faturou R$ 15.000,00 em um projeto. Os custos fixos foram de R$ 5.000,00 e o imposto sobre o faturamento é de 15%. Objetivo: Calcule o imposto, o lucro líquido e a margem de lucro (Lucro / Faturamento). No final, crie uma variável booleana chamada meta_atingida que verifica se a margem de lucro é superior a 0.30 (30%).

faturamento = 15000
custos = 5000
imposto_faturamento = 0.15

imposto = faturamento * imposto_faturamento 
print("O imposto sobre o farturamento eh", imposto)

lucro_liquido = faturamento - custos - imposto
print("O lucro liquido eh", lucro_liquido)

margem_lucro = lucro_liquido / faturamento
print("A margem de lucro eh", margem_lucro)

meta = 0.30

meta_atingida = margem_lucro >= meta
print(meta_atingida)


