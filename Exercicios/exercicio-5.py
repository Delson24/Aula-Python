#Exercício 5: Conversão de Tempo de Contrato (Gestão de Projetos) || Cenário: Um contrato de manutenção de software tem a duração de 40 meses. O cliente quer ver esse tempo no formato: "X anos e Y meses". Objetivo: Utilize os operadores de divisão inteira e resto da divisão para converter os 40 meses.

duracao_contrato = 40               # 40 meses
ano = 12                            # 1 ano = 12 meses
ano_contrato = duracao_contrato // ano
meses_contrato = duracao_contrato % ano
print("O contrato tem", ano_contrato, "anos e", meses_contrato, "meses")


