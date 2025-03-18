# registro.py
import os 
import time  # Adicionado para usar time.sleep()
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

class Registro:
    def __init__(self):
        self.historico = []

    def registrar(self, mensagem, cor=Fore.WHITE):  # Adicionado 'cor' como parâmetro opcional
        self.historico.append(mensagem)
        print(cor + mensagem + Style.RESET_ALL)

    def mostrar_historico(self):
        print(Fore.CYAN + "\n=== Histórico de Eventos ===" + Style.RESET_ALL)
        for evento in self.historico:
            print(Fore.YELLOW + evento + Style.RESET_ALL)

    def limpar_terminal(self): #limpa o terminal periodicamente para manter a organização e visualização mais limpa
        input("\nPressione Enter para continuar..." + Style.RESET_ALL)  # Pausa antes de limpar
        os.system('cls' if os.name == 'nt' else 'clear')

    def cabecalho(self, titulo):
        print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)
        print(Fore.CYAN + titulo.center(50) + Style.RESET_ALL)
        print(Fore.CYAN + "=" * 50 + Style.RESET_ALL)

    def mensagem_destacada(self, mensagem):
        print(Fore.MAGENTA + "\n" + ">" * 3 + " " + mensagem + " " + "<" * 3 + Style.RESET_ALL)  