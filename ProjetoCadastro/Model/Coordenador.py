from Professor import Professor

class Coordenador(Professor):
    
    def __init__(self, nome, cpf, coordena=None):
        super().__init__(nome, cpf)
        self.__curso = None
        self.__coordena = coordena
        self.__endereco = None
        self.__disciplinas = []
        
    def _mostrarDados(self):
        return print(self.__repr__())
        
    def _getNome(self):
        return self.__nome
    
    def _setNome(self, nome):
        self.__nome = nome
        
    def _getCpf(self):
        return self.__cpf
    
    def _setCpf(self, cpf):
        self.__cpf = cpf
    
    def _getEndereco(self):
        return self.__endereco
    
    def _setEndereco(self, endereco):
        self.__endereco = endereco
    
    def _getCurso(self):
        return self.__curso
    
    def _setCurso(self, curso):
        self.__curso = curso
    
    def _getCoordena(self):
        return self.__coordena
    
    def _setCoordena(self, coordena):
        self.__coordena = coordena
    
    def _getDisciplinas(self):
        return self.__disciplinas
    
    def _setDisciplina(self, disciplina):
        self.__disciplinas.append(disciplina)
        
    def __repr__(self) -> str:
        return f"Nome: {self.__nome}, Cpf: {self.__cpf}, Endereço: {self.__endereco}, Curso: {self.__curso}, Disciplinas: {self.__disciplinas}, Coordena o curso: {self.__coordena}"