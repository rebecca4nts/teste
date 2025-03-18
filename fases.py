# fases.py
from personagem import Heroi, Vilao, NPC
from batalha import batalha
from registro import Registro

def escolher_heroi():
    print("Bem-vindo a Aespia, jogador! Selecione seu papel para continuar:")
    herois = {
        "cavaleiro": {"vida": 120, "ataque": 20, "defesa": 15, "descricao": "Um guerreiro resistente e equilibrado, ideal para combates corpo a corpo."},
        "mago": {"vida": 80, "ataque": 30, "defesa": 10, "descricao": "Um poderoso conjurador de magias, com alto dano mas pouca defesa."},
        "barbaro": {"vida": 100, "ataque": 25, "defesa": 12, "descricao": "Um selvagem combatente, com alta resistência e dano moderado."},
        "arqueiro": {"vida": 90, "ataque": 22, "defesa": 13, "descricao": "Um especialista em ataques à distância, ágil e preciso."}
    }

    while True:
        print("\nEscolha seu herói:")
        for i, (classe, atributos) in enumerate(herois.items(), start=1):
            print(f"{i}. {classe.capitalize()}")

        print("\nDigite o número do herói para ver seus atributos ou 'escolher' para selecionar:")
        escolha = input("Sua escolha: ").lower()

        if escolha == "escolher":
            break
        elif escolha.isdigit() and 1 <= int(escolha) <= len(herois):
            classe = list(herois.keys())[int(escolha) - 1]
            atributos = herois[classe]
            print(f"\nAtributos do {classe.capitalize()}:")
            print(f"- Vida: {atributos['vida']}")
            print(f"- Ataque: {atributos['ataque']}")
            print(f"- Defesa: {atributos['defesa']}")
            print(f"- Descrição: {atributos['descricao']}")
        else:
            print("Escolha inválida. Tente novamente.")

    print("\nEscolha seu herói:")
    for i, (classe, atributos) in enumerate(herois.items(), start=1):
        print(f"{i}. {classe.capitalize()}")

    while True:
        escolha = input("Digite o número do herói que deseja jogar: ")
        if escolha.isdigit() and 1 <= int(escolha) <= len(herois):
            classe = list(herois.keys())[int(escolha) - 1]
            atributos = herois[classe]
            return Heroi(classe.capitalize(), atributos["vida"], atributos["ataque"], atributos["defesa"], classe)
        else:
            print("Escolha inválida. Tente novamente.")


def fase_1(heroi, registro):
    registro.limpar_terminal()
    registro.registrar("No meio de sua jornada para resgatar a princesa,")
    registro.registrar("você se depara com um aldeão sendo atacado por um goblin!")
    registro.registrar("Rápido, Ajude-o!!")
    registro.registrar("\nFase 1: Enfrentando um monstro!")
    monstro1 = Vilao("Goblin", 50, 15, 5, "Monstro")
    if batalha(heroi, monstro1, registro):
        ferreiro = NPC("Ferreiro", 100, 5, 10, "Ferreiro")
        registro.registrar(heroi.salvar_refem(ferreiro))
        registro.registrar(f"{ferreiro.nome}: 'Obrigado por me salvar, aventureiro! Tome esta arma como agradecimento.'")
        heroi.arma = "Espada" if heroi.classe == "cavaleiro" else "Cajado" if heroi.classe == "mago" else "Machado" if heroi.classe == "barbaro" else "Arco"
        registro.registrar(f"Você recebeu uma {heroi.arma} como recompensa!")
        registro.registrar(heroi.melhorar_ataque())
        registro.registrar(f"Vida restante de {heroi.nome}: {heroi.vida}")
        registro.registrar(f"Novo poder de ataque: {heroi.ataque}")
        registro.limpar_terminal()  # Limpa a tela apenas após o jogador confirmar
        return True
    else:
        return False


def fase_2(heroi, registro):
    registro.limpar_terminal()
    registro.registrar("Você se sente mais forte após receber o generoso presente do ferreiro, no entanto")
    registro.registrar("ainda no caminho para o covil do dragão, você escuta gritos e rugidos que parecem estar vindo")
    registro.registrar("da caverna mais a frente. Ao chegar lá, você vê um jovem encapuzado sendo atacado por um Orc!")
    registro.registrar("Rápido, Ajude-o!!")
    registro.registrar("\nFase 2: Enfrentando um monstro mais forte!")
    monstro2 = Vilao("Orc", 80, 20, 10, "Monstro")
    if batalha(heroi, monstro2, registro):
        curandeiro = NPC("Curandeiro", 100, 5, 10, "Curandeiro")
        registro.registrar(heroi.salvar_refem(curandeiro))
        registro.registrar(f"{curandeiro.nome}: 'Obrigado por me salvar! Pegue uma de minhas poções como agradecimento.'")
        escolha = input("Escolha uma poção (cura, melhoria): ")
        heroi.pocoes.append(escolha)
        registro.registrar(f"Você escolheu uma poção de {escolha}!")
        registro.registrar(f"Vida restante de {heroi.nome}: {heroi.vida}")
        registro.limpar_terminal()  # Limpa a tela apenas após o jogador confirmar
        return True
    else:
        return False


def fase_3(heroi, registro):
    registro.limpar_terminal()
    registro.registrar("Após alguns desvios, você finalmente chega ao covil do dragão")
    registro.registrar("para resgatar a princesa sequestrada. Com toda a sua maestria e sagacidade,")
    registro.registrar("você consegue adentrar a fortaleza sem problemas, mas sua tranquilidade dura pouco")
    registro.registrar("pois você quase é atingido por uma lufada de fogo ardente!!")
    registro.registrar("É o dragão! derrote-o para salvar a princesa e fugir da fortaleza!")
    registro.registrar("\nFase 3: Enfrentando o chefão!")
    chefe = Vilao("Dragão", 120, 25, 15, "Chefão")  # Dificuldade reduzida
    if batalha(heroi, chefe, registro):
        registro.registrar(f"{heroi.nome} resgatou a princesa e venceu o jogo!")
        registro.registrar(f"Vida restante de {heroi.nome}: {heroi.vida}")
        registro.limpar_terminal()  # Limpa a tela apenas após o jogador confirmar
        return True
    else:
        registro.registrar(f"{heroi.nome} foi derrotado pelo chefão. Fim de jogo.")
        registro.limpar_terminal()  # Limpa a tela apenas após o jogador confirmar
        return False