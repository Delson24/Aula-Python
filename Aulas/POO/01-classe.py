# vamos criar uma classe pra site da netflix

class Cliente:
    def __init__(self, nome, email, plano_assinatura):
        self.nome = nome
        self. email = email
        self.lista_plano = ["basic", "premium"]
        if plano_assinatura in self.lista_plano:
            self.plano_assinatura = plano_assinatura
        else:
            raise Exception("Plano Invalido ")
        
    # funçao mudar plano
    def mudar_plano(self, novo_plano):
        if novo_plano in self.lista_plano:
            self.plano_assinatura = novo_plano
        else:
            print("Plano Invalido")

    # funçao ver filme 
    def ver_filme(self, filme, plano_filme):
        if self.plano_assinatura == plano_filme:
            print(f"Ver o filme{filme}")
        elif self.plano_assinatura == "premium":
            print("ver filme")
        elif self.plano_assinatura == "basic" and plano_filme == "premium":
            print("faça upgrade dp plano para o plano premiu pra poder ver o filme")
        else: 
            print("Plano invelido")

cliente = Cliente("Delson ", "delson@gmail.com", "premium")
print(cliente.plano_assinatura)
cliente.ver_filme("Harry poter", "premium")

# botao de fazer upgrade
cliente.mudar_plano("premium")
print(cliente.plano_assinatura)
