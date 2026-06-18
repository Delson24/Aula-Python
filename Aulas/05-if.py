vendas = 1500
meta = 600

if vendas >= meta:
    print("Batemos a meta de vendas")
    if vendas >= (2 * meta):
        print("Foi muito facil, batemos mais que o dobro da meta")
    else:
        print("passamos por pouco da meta")
else:
    vendas_faltantes = meta - vendas
    print(f"Faltam {vendas_faltantes} vendas para bater a meta")


# faixa de bonus
# 50 se ele bateu a meta
# 100 se ele bateu mais doque o dobro da meta
# 0 se ele nao bateu a meta

meta_funcionario = 500
vendas_funcionario = 1000

if vendas_funcionario >= (2 * meta_funcionario):
    bonus = 100
elif vendas_funcionario >= meta_funcionario:
    bonus = 50
else:
    bonus = 0

print(bonus)

# cadastro de produtos

lista_produtos = ["iphone", "mac", "apple watch", "airpod"]

produto_a_cadastrar = input("Degite o produto que deseja cadastrar: ")
produto_a_cadastrar = produto_a_cadastrar.lower

if produto_a_cadastrar in lista_produtos:
    print("O produto ja foi cadastrado")
else:
    lista_produtos.append(produto_a_cadastrar)

print(lista_produtos)

# mais de uma condicao
meta_empresa = 500
meta_funcionario = 50
vendas_empresa = 590
vendas_funcionario = 45

if vendas_funcionario >= meta_funcionario and vendas_empresa >= meta_empresa:
    print("vai ganhar bonus")
else:
    print("sem bonus")