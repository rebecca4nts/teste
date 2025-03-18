# main.py
from registro import Registro
from colorama import Fore
from fases import escolher_heroi, fase_1, fase_2, fase_3

def jogar():
    registro = Registro()
    registro.limpar_terminal()
    heroi = escolher_heroi()
    registro.limpar_terminal()
    registro.cabecalho("Introdução")
    registro.registrar(f"Você escolheu o {heroi.classe}!", Fore.GREEN)
    registro.registrar("Saudações, aventureiro! Que bom que decidiu aceitar esta missão. Leve este mapa, ele o levará até o covil onde a princesa está sendo mantida. Boa sorte!", Fore.BLUE)

    if fase_1(heroi, registro):
        if fase_2(heroi, registro):
            fase_3(heroi, registro)
    else:
        registro.mostrar_historico()

if __name__ == "__main__":
    jogar()