# Exercício 3: Divisão de Cargas (Logística/Transporte) || Cenário: Uma transportadora precisa levar 1.250 caixas em caminhões pequenos. Cada caminhão suporta exatamente 12 caixas. Objetivo: 1. Quantos caminhões sairão totalmente cheios? (Use //) 2. Quantas caixas sobrarão para serem enviadas em uma última viagem menor? (Use %)

total_caixas = 1250
caixas_suportadas = 12

caminhoes_cheios = total_caixas // caixas_suportadas
print(caminhoes_cheios, "caminhoes sairao totalmente cheios de caixas")

caixas_sobra = total_caixas % caixas_suportadas
print(caixas_sobra, "caixas sobraram pra serem enviadas em uma ultima viagem menor")