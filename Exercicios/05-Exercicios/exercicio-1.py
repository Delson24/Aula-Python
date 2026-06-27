# Exercício 1: Validação de Investimento (Setor Financeiro) Uma corretora de valores quer automatizar a recomendação básica de perfil. Crie um programa que peça ao usuário o valor que ele deseja investir.
# 1.	Se o valor for menor que R$ 1.000,00, exiba: "Perfil iniciante: Sugerimos Tesouro Direto".
# 2.	Se o valor for entre R$ 1.000,00 e mzn 5.000,00 (inclusive), exiba: "Perfil moderado: Sugerimos Fundos Imobiliários".
# Se o valor for acima de R$ 5.000,00, exiba: "Perfil arrojado: Sugerimos Ações". *Lembre-se de tratar o input caso o usuário digite "mzn" ou use vírgula.*

margem_baixa = 1000
margem_media = 5000

entrada = input("Digite o valor que deseja investir: ")

# Tratamento do input: remove "mzn", espaços e troca vírgula por ponto
entrada = entrada.replace("mzn", "").replace(" ", "").replace(",", ".")

valor = float(entrada)  # converte para número

if valor < margem_baixa:
    print("Perfil iniciante: Sugerimos Tesouro Direto")
elif valor <= margem_media:          
    print("Perfil moderado: Sugerimos Fundos Imobiliários")
else:
    print("Perfil arrojado: Sugerimos Ações")