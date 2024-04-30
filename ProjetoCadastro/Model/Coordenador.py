import sys
sys.path.append('.')
from ProjetoCadastro.Model.Professor import Professor

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
        return super()._getNome()
    
    def _setNome(self, nome):
        super()._setNome(nome)
        
    def _getCpf(self):
        return super()._getCpf()
    
    def _setCpf(self, cpf):
        super()._setCpf(cpf)
    
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
        
    def __eq__(self, other):
        if isinstance(other, Coordenador):
            return super().__eq__(other) and self._getNome() == other._getNome() and self._getCpf() == other._getCpf()
        return False
        
    def __repr__(self) -> str:
        return f"Nome: {self.__nome}, Cpf: {self.__cpf}, Endereço: {self.__endereco}, Curso: {self.__curso}, Disciplinas: {self.__disciplinas}, Coordena o curso: {self.__coordena}"