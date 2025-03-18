class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        dano = max(0, self.ataque - alvo.defesa)
        alvo.vida -= dano
        return dano

    def esta_vivo(self):
        return self.vida > 0


class Heroi(Personagem):
    def __init__(self, nome, vida, ataque, defesa, classe):
        super().__init__(nome, vida, ataque, defesa)
        self.classe = classe
        self.arma = None
        self.pocoes = []
        self.carga_ataque_especial = 0  # Contador para o ataque especial

    def salvar_refem(self, refem):
        return f"{self.nome} salvou {refem.nome}!"

    def usar_pocao(self, tipo):
        if tipo == "cura":
            self.vida += self.vida // 2
            return f"{self.nome} usou uma poção de cura e recuperou metade da vida!"
        elif tipo == "melhoria":
            escolha = input("Escolha o atributo para melhorar (vida, ataque, defesa): ")
            if escolha == "vida":
                self.vida += 20
            elif escolha == "ataque":
                self.ataque += 10
            elif escolha == "defesa":
                self.defesa += 10
            return f"{self.nome} melhorou o atributo {escolha}!"
        else:
            return "Poção inválida."

    def melhorar_ataque(self):
        self.ataque = int(self.ataque * 1.25)
        return f"{self.nome} melhorou seu ataque em 25% com a nova arma!"

    def atacar_especial(self, alvo):
        if self.carga_ataque_especial >= 3:
            dano = max(0, int(self.ataque * 1.5) - alvo.defesa)
            alvo.vida -= dano
            self.carga_ataque_especial = 0  # Reseta a carga
            return dano
        else:
            return None  # Ataque especial ainda não está carregado


class Vilao(Personagem):
    def __init__(self, nome, vida, ataque, defesa, tipo):
        super().__init__(nome, vida, ataque, defesa)
        self.tipo = tipo


class NPC(Personagem):
    def __init__(self, nome, vida, ataque, defesa, profissao):
        super().__init__(nome, vida, ataque, defesa)
        self.profissao = profissao