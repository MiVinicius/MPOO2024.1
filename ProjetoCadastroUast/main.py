import Aluno, Professor, Curso, Disciplina, Sala, os


clear = lambda: os.system('cls')  # vai limpar a tela do terminal

def menu():
    while True:
        clear()
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
        print("Conta de Administrador Ativada")
        print("===========================" * 6)
        print("1 - cadastrar aluno - requer cadastro do endereço, curso e disciplina e sala")
        print("2 - cadastrar professor - requer cadastro do endereço, curso e disciplina e sala")
        print("3 - sair")
        print("===========================" * 6)

        opcoes = str(input("o que deseja fazer? "))
        
        match opcoes:
            case "1":
                clear()
                Aluno.Aluno().cadastrarAluno()
            case "2":
                clear()
                Professor.Professor().cadastrarProfessor()
            case "3":
                clear()
                break

class main():
    menu()
    
if __name__ == '__main__':
    main() 