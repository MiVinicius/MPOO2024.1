from Testes import testesAluno, testesProfessor, testesCurso, testesDisciplina, testesSala, testesEndereco
import os

clear = lambda: os.system('cls')  # vai limpar a tela do terminal

def menu():
    while True:
        clear()
        print("===========================" * 6)
        print("1 - Rodar testes (estão no arquivo Testes.py)")
        print("2 - sair")
        print("===========================" * 6)

        opcoes = str(input("o que deseja fazer? "))
        
        match opcoes:
            case "1":
                clear()
                testesAluno()
                testesProfessor()
                testesEndereco()
                testesCurso()
                testesDisciplina()
                testesSala()
                input("pressione enter para continuar...")
            case "2":
                clear()
                break

class main():
    menu()
