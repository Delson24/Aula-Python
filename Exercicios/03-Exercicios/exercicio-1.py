# Exercício 1: Calculadora de Imposto sobre Vendas (Setor Fiscal) Uma empresa de serviços precisa calcular o imposto de 15% sobre o valor bruto de uma nota fiscal. Como o valor muitas vezes vem copiado de planilhas com "R$" e vírgula, seu programa deve:
#1.	Pedir para o usuário digitar o valor bruto (Ex: R$ 5.000,00).
#3.	Converter para número decimal (float).
#4.	Calcular o valor do imposto (15% do valor bruto).
#5.	Exibir uma mensagem formatada com f-string mostrando o valor do imposto com duas casas decimais.

imposto = 0.15

valor = input("degite o valor: ")
print(f"O valor eh {valor}")
