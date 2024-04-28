
class Aluno():
    
    __nMatricula = 0 
    
    def __init__(self, nome, cpf, Endereco = None) -> None:
        self.__nome = nome
        self.__cpf = cpf
        self.__matricula = self.incrementar_matricula()
        self.__endereco = Endereco
        self.__curso = None
        self.__disciplinas = []
        
    @classmethod
    def incrementar_matricula(cls): # assim a matricula terá um valor diferente para cada instancia
        cls.__nMatricula += 1
        return cls.__nMatricula
    
    def _mostrarDados(self):
        return print(self.__repr__())
    
    def _setNome(self, nome):
        self.__nome = nome
        
    def _getNome(self):
        return self.__nome
    
    def _setCpf(self, cpf):
        self.__cpf = cpf
        
    def _getCpf(self):
        return self.__cpf
    
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
    
    def __eq__(self, other):
        if isinstance(other, Aluno):
            return self.__nome == other.__nome and self.__cpf == other.__cpf
        return False
    
    def __repr__(self) -> str:
        return f"Nome: {self.__nome}, CPF: {self.__cpf}, Matricula: {self.__matricula}, Endereço: {self.__endereco}, Curso: {self.__curso}, Disciplinas: {self.__disciplinas}"
    