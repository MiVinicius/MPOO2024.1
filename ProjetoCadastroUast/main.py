from Aluno import Aluno
from Professor import Professor
import os

clear = lambda: os.system('cls')  # vai limpar a tela do terminal

def menu():
    while True:
        print('''   
   ####     ##     #####      ##      #####   ######   ######    #####            #####    #######             ##     ####     ##   ##  ##   ##   #####    #####
  ##  ##   ####     ## ##    ####    ##   ##  # ## #    ##  ##  ##   ##            ## ##    ##   #            ####     ##      ##   ##  ###  ##  ##   ##  ##   ##
 ##       ##  ##    ##  ##  ##  ##   #          ##      ##  ##  ##   ##            ##  ##   ## #             ##  ##    ##      ##   ##  #### ##  ##   ##  #
 ##       ##  ##    ##  ##  ##  ##    #####     ##      #####   ##   ##            ##  ##   ####             ##  ##    ##      ##   ##  ## ####  ##   ##   #####
 ##       ######    ##  ##  ######        ##    ##      ## ##   ##   ##            ##  ##   ## #             ######    ##   #  ##   ##  ##  ###  ##   ##       ##
  ##  ##  ##  ##    ## ##   ##  ##   ##   ##    ##      ##  ##  ##   ##            ## ##    ##   #           ##  ##    ##  ##  ##   ##  ##   ##  ##   ##  ##   ##
   ####   ##  ##   #####    ##  ##    #####    ####    #### ##   #####            #####    #######           ##  ##   #######   #####   ##   ##   #####    #####

             ''')
        print("===========================" * 6)
        print("Só cadastro mesmo!")
        print("Se bem que poderia mostrar todos os dados depois do cadastro...")
        print("Muitas funções criadas não implementadas no menu!")
        print("===========================" * 6)
        print("1 - cadastrar aluno - requer cadastro do endereço, curso e disciplina e sala")
        print("2 - cadastrar professor - requer cadastro do endereço, curso e disciplina e sala")
        print("3 - sair")
        print("===========================" * 6)

        opcoes = str(input("o que deseja fazer? "))
        
        match opcoes:
            case "1":
                clear()
                Aluno().cadastrarAluno()
                input("pressione enter para continuar...")
            case "2":
                clear()
                Professor().cadastrarProfessor()
                input("pressione enter para continuar...")
            case "3":
                clear()
                break

class main():
    menu()
    
if __name__ == '__main__':
    main() 