from Testes import testesAluno, testesProfessor
import os

clear = lambda: os.system('cls')  # vai limpar a tela do terminal

def menu():
    while True:
        clear()
        print("===========================" * 6)
        print("1 - Rodar testes")
        print("2 - sair")
        print("===========================" * 6)

        opcoes = str(input("o que deseja fazer? "))
        
        match opcoes:
            case "1":
                clear()
                testesAluno()
                testesProfessor()
                input("pressione enter para continuar...")
            case "2":
                clear()
                break

class main():
    menu()
