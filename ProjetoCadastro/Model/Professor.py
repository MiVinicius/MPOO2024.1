import Servidor


class Professor(Servidor):
    
    def __init__(self, nome, cpf) -> None:
        super().__init__(self, nome, cpf)
        self.__endereco = None
        self.__curso  = None
        self.__disciplinas = []
    
    def _mostrarDados(self):
        print(repr)

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
    
    def _getDisciplinas(self):
        return self.__disciplinas
    
    def _setDisciplina(self, disciplina):
        self.__disciplinas.extend(disciplina)
        
    def __repr__(self) -> str:
        f"Nome: {self.__nome}, Cpf: {self.__cpf}, Endereço: {self.__endereco}, Curso: {self.__curso}, Disciplinas: {self.__disciplinas}"
    