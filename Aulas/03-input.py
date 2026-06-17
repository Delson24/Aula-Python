faturamento = input("digite o valor do faturamento desse mes: ") # input por padrao eh uma string
faturamento = faturamento.replace("mzn", " ") #susbtitui o mzn por um vazio

faturamento = float(faturamento) # converte string do input pra inteiro
print(f"O faturamento desse mes foi de {faturamento}")

custo = 300
lucro = faturamento - custo
print(F"O lucro foi de {lucro} e o faturamento foi de {faturamento}")