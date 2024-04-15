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
        print("1 - cadastrar aluno")
        print("2 - cadastrar professor")
        print("3 - cadastrar endereco - Aluno")
        print("4 - cadastrar endereco - Professor")
        print("5 - cadastrar curso")
        print("6 - cadastrar diciplina")
        print("7 - cadastrar sala")
        print("8 - Menu Avançado - implementar depois")
        print("9 - sair")
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
                aluno = Aluno.Aluno().buscarAluno()
                Aluno.Aluno().setEndereco(aluno)
            case "4":
                clear()
                professor = Professor.Professor().buscarProfessor()
                Professor.Professor().setEndereco(professor)
            case "5":
                clear()
                Curso.Curso().cadastrarCurso()
            case "6":
                clear()
                Disciplina.Disciplina().cadastrarDisciplina()
            case "7":
                clear()
                Sala.Sala().cadastrarSala()
            case "8":
                clear()
                pass
            case "9":
                clear()
                break

class main():
    menu()
    
if __name__ == '__main__':
    main() 