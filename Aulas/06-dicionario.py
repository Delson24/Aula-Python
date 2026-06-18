lista_produtos = ["iphone", "mac", "apple watch", "airpod"]
lista_precos = [10000, 15000, 5000, 2000]

# dicionario = {chave: valor, chave: valor, chave: valor}
dic_produtos = {"iphone": 10000, "mac": 15000, 
                "apple watch": 15000, "airpod": 2000}

# pegar as chaves do dicionario
print(dic_produtos.keys())

# pegar os valores do dicionario
print(dic_produtos.values())

# pegar um item
preco_iphone = dic_produtos["iphone"]
print(preco_iphone)

# editar um item -> dicionario[chave] = novo_valor
dic_produtos["mac"] = dic_produtos["mac"] * 1.1
print(dic_produtos)
 
# adicionar um item
dic_produtos["apple tv"] = 14000
print(dic_produtos)

# remover um item
dic_produtos.pop("mac")
print(dic_produtos)

# verificar se o item existe no dicionario
if "iphone" in dic_produtos:
    print("produto encontrado")
else:
    print("produto nao encontrado")


# tornar duas listas em um dicionario
lista_produtos = ["iphone", "mac", "apple watch", "airpod"]
lista_precos = [10000, 15000, 5000, 2000]

novo_dicionario = dict(zip(lista_produtos, lista_precos))
print(novo_dicionario)