# Exercício 3: Migração de Servidor de E-mail (Setor de TI) Sua empresa mudou de nome e todos os funcionários que usavam o domínio @empresa.com.br agora devem usar o domínio @grupocorp.com. O e-mail do funcionário é andre_silva@empresa.com.br. Crie um código que substitua automaticamente o domínio antigo pelo novo e exiba o novo endereço de e-mail.

email = "andre_silva@empresa.com.br"
pedaco_email = "@grupocorp.com"
posicao = email.find("@")
print(posicao)

nome = email[:posicao]
print(nome)

novo_email = nome + pedaco_email
print(novo_email)






