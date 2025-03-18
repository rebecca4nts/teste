# batalha.py
from registro import Registro

def batalha(heroi, vilao, registro):
    while heroi.esta_vivo() and vilao.esta_vivo():
        # Aviso de vida baixa
        if heroi.vida <= heroi.vida * 0.3:
            registro.registrar(f"ATENÇÃO: A vida de {heroi.nome} está muito baixa! ({heroi.vida} HP)")

        # Turno do herói
        registro.registrar(f"\nTurno de {heroi.nome}:")
        acao = input("Escolha sua ação (atacar, ataque especial, usar poção): ").lower()
        if acao == "atacar":
            dano = heroi.atacar(vilao)
            registro.registrar(f"{heroi.nome} atacou {vilao.nome} causando {dano} de dano!")
        elif acao == "ataque especial":
            dano = heroi.atacar_especial(vilao)
            if dano is not None:
                registro.registrar(f"{heroi.nome} usou um ataque especial em {vilao.nome} causando {dano} de dano!")
            else:
                registro.registrar(f"Ataque especial ainda não está carregado! ({3 - heroi.carga_ataque_especial} rodadas restantes)")
        elif acao == "usar poção" and heroi.pocoes:
            tipo = input("Escolha o tipo de poção (cura, melhoria): ")
            registro.registrar(heroi.usar_pocao(tipo))
        else:
            registro.registrar("Ação inválida ou sem poções disponíveis.")

        # Incrementa a carga do ataque especial
        heroi.carga_ataque_especial += 1

        if not vilao.esta_vivo():
            registro.registrar(f"{vilao.nome} foi derrotado!")
            break

        # Turno do vilão
        registro.registrar(f"\nTurno de {vilao.nome}:")
        dano = vilao.atacar(heroi)
        registro.registrar(f"{vilao.nome} atacou {heroi.nome} causando {dano} de dano!")

        if not heroi.esta_vivo():
            registro.registrar(f"{heroi.nome} foi derrotado!")
            break

    return heroi.esta_vivo()