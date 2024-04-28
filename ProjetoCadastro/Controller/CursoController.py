
from ProjetoCadastro.Model.Curso import Curso
from ProjetoCadastro.Model.BaseDados import BaseDados

class CursoController:
    
    @staticmethod
    def cadastrarCurso():
        curso = Curso(str(input("Digite o nome do curso: \n")),
                    str(input("Digite o período do curso: \n")))
        return BaseDados.cadastrarCurso(curso)
    
    @staticmethod
    def passarCurso(pessoa):
        curso = Curso(str(input("Digite o nome do curso: \n")), str(input("Digite o período do curso: \n")))
        return BaseDados.passarCurso(BaseDados.buscarCurso(curso), pessoa)
    
    @staticmethod
    def buscarCurso():
        curso = str(input("Digite o nome do curso: \n"))
        return BaseDados.buscarCurso(Curso(curso, None))
    
    @staticmethod
    def atualizarCurso():
        curso = Curso(str(input("Digite o nome do curso: \n")), str(input("Digite o período do curso: \n")))
        novos_dados = Curso(str(input("Digite o novo nome do curso: \n")), str(input("Digite o novo período do curso: \n")))
        return BaseDados.atualizarCurso(BaseDados.buscarCurso(curso), novos_dados) 
        
    @staticmethod
    def removerCurso():
        return BaseDados.deletarCurso(CursoController.buscarCurso())
    
    @staticmethod
    def listarCursos():
        return BaseDados.listarCursos()