import sys
sys.path.append('.') # obrigatório para o import funcionar
from ProjetoCadastro.Controller.AlunoController import AlunoController
from ProjetoCadastro.Controller.ServidorController import ServidorController
from ProjetoCadastro.Controller.ProfessorController import ProfessorController
from ProjetoCadastro.Controller.CoordenadorController import CoordenadorController
from ProjetoCadastro.Controller.DiretorController import DiretorController


def Menu():
    while True:
        print("Cadastro da Universidade")
        print("1 - Cadastrar Aluno")
        print("2 - Cadastrar Servidor")
        print("3 - Cadastrar Professor")
        print("4 - Cadastrar Coordenador")
        print("5 - Cadastrar Diretor")
        
        
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
            case _:
                print("Opção invalida")
                

Menu()
