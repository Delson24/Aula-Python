# Exercício 2: Gestão de Estoque (Edição e Verificação) Uma loja de eletrônicos possui os seguintes produtos: estoque = ["monitor", "teclado", "mouse", "headset"]. O gerente pediu para:
# 1.	Adicionar o item "webcam" ao final da lista.
# 2.	O "teclado" teve seu nome atualizado para "teclado mecanico". Faça essa alteração na lista.
# 3.	Verificar se "impressora" está no estoque. O programa deve exibir True ou False.
# 4.	Remover o "mouse" da lista, pois saiu de linha.

produtos =  ["monitor", "teclado", "mouse", "headset"]

produtos.append("webcam")
print(produtos)

# editar uma veriavel do tipo string
produtos[1] = "teclado mecanico"
print(produtos)

procurar_impressora = "impressora" in produtos
print(procurar_impressora)

# remover mouse da lista
produtos.remove("mouse")
print(produtos) 

