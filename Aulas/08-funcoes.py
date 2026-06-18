# forma mais basica
def se_inscreva_canal():
    print("se inscreva no canal")
    print("da um like")

se_inscreva_canal()

dic_produtos = {"iphone": 10000, "mac": 15000, 
                "apple watch": 15000, "airpod": 2000}  

def calcular_novo_preco(preco):
    inflacao = 0.1
    iss = 0.07
    novo_preco = preco * (1 + (inflacao + iss))
    return novo_preco

for item in dic_produtos:
    preco_original = dic_produtos[item]
    novo_preco = calcular_novo_preco(preco_original)
    dic_produtos[item] = novo_preco

print(dic_produtos)