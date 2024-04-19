
class Aluno():
    
    __nMatricula = 0 
    
    def __init__(self, nome) -> None:
        self.__nome = nome
        self.__nMatricula += 1
        self.__matricula = self.__nMatricula
        self.__endereco = None
        self.__curso = None
        self.__disciplinas = []
        
    def _mostrarDados(self):
        print(repr)
    
    def _setNome(self, nome):
        self.__nome = nome
        
    def _getNome(self):
        return self.__nome
    
    def _setMatricula(self, matricula):
        self.__matricula = matricula 
        
    def _getMatricula (self):
        return self.__matricula
    
    def _setEndereco(self, endereco):
        self.__endereco = endereco
        
    def _getEndereco(self):
        return self.__endereco 
    
    def _setCurso(self, curso):
        self.__curso = curso
        
    def _getCurso(self):
        return self.__curso
    
    def _setDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)
        
    def _getDisciplina(self):
        return self.__disciplinas
    
    def __repr__(self) -> str:
        f"Nome: {self.__nome}, Matricula: {self.__matricula}, Endereço: {self.__endereco}, Curso: {self.__curso}, Disciplinas: {self.__disciplinas}"
    