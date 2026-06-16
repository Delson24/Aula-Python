faturamento = 1000
custo = 300

lucro = faturamento - custo

# apresentar o resultado nas tres formas possiveis
print("O faturamento foi de", faturamento, "e o lucro foi de", lucro)

mensagem = "O faturamento foi de " + str(faturamento) + " e o lucro foi de " + str(lucro) 
print(mensagem)    

#f-string
texto = f"O faturamento foi de {faturamento}mzn e o lucro foi de {lucro}mzn"
print(texto)

texto = "O faturamento foi de {}mzn e o lucro foi de {}mzn".format(faturamento, lucro)
print(texto)


# formulas/funcoes de texto
email= "EMAIL_FALSO@gmail.com"

email= email.lower() # coloca em letra minuscula
email= email.upper() # coloca em letra maiscula

print(email)

# tamanho de um texto
tamanho_texto = len(email)
print(f"O texto tem {tamanho_texto} caracteres")

# posiçao de um caracter no texto
posicao = email.find("@")
print(posicao)

# pedaços de um texto
nome_usuario = email[:posicao]
print(nome_usuario)

# trocar pedaço de texto
email = email.lower()
email = email.replace("@gmail.com", "@yahoo.com")
print(email)