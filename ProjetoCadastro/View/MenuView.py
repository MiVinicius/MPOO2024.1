import sys
sys.path.append('.') # obrigatório para o import funcionar
from ProjetoCadastro.Controller.AlunoController import AlunoController
from ProjetoCadastro.Controller.ServidorController import ServidorController
from ProjetoCadastro.Controller.ProfessorController import ProfessorController
from ProjetoCadastro.Controller.CoordenadorController import CoordenadorController
from ProjetoCadastro.Controller.DiretorController import DiretorController
from ProjetoCadastro.Controller.BaseDadosController import BaseDadosController

class MenuView:
    
    def Menu():
        while True:
            print("""
 ####      ##     ####       ##      ####    ######   #####     ####   
##  ##    ####    ## ##     ####    ##  ##     ##     ##  ##   ##  ##  
##       ##  ##   ##  ##   ##  ##   ##         ##     ##  ##   ##  ##  
##       ######   ##  ##   ######    ####      ##     #####    ##  ##  
##       ##  ##   ##  ##   ##  ##       ##     ##     ####     ##  ##  
##  ##   ##  ##   ## ##    ##  ##   ##  ##     ##     ## ##    ##  ##  
 ####    ##  ##   ####     ##  ##    ####      ##     ##  ##    ####   
                """)
            print("===========================" * 6)
            print("1 -  Cadastrar Aluno")
            print("2 -  Cadastrar Servidor")
            print("3 -  Cadastrar Professor")
            print("4 -  Cadastrar Coordenador")
            print("5 -  Cadastrar Diretor")
            print("6 -  Listar Alunos")
            print("7 -  Cadastrar Endereço para Aluno")
            print("8 -  Cadastrar Endereço para Servidor")
            print("9 -  Cadastrar Endereço para Professor")
            print("10 - Cadastrar Endereço para Coordenador")
            print("11 - Cadastrar Endereço para Diretor")
            
            opcao = int(input("Escolha uma opção: "))
            match opcao:
                case 1:
                    AlunoController.cadastrarAluno()
                case 2:
                    ServidorController.cadastrarServidor()
                case 3:
                    ProfessorController.cadastrarProfessor()
                case 4:
                    CoordenadorController.cadastrarCoordenador()
                case 5:
                    DiretorController.cadastrarDiretor()
                case 6:
                    BaseDadosController.listarAlunos()
                case 7:
                    AlunoController.passarEndereco(AlunoController.buscarAluno())
                case 8:
                    ServidorController.passarEndereco(ServidorController.buscarServidor())
                case 9:
                    ProfessorController.passarEndereco(ProfessorController.buscarProfessor())
                case 10:
                    CoordenadorController.passarEndereco(CoordenadorController.buscarCoordenador())
                case 11:
                    DiretorController.passarEndereco(DiretorController.buscarDiretor())
                case _:
                    print("Opção invalida")
                    

MenuView.Menu()
