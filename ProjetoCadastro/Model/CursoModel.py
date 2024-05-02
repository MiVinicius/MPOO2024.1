
class Curso():

    def __init__(self, nome, periodo, Coordenador = None) -> None:
        self.__nome = nome
        self.__periodo = periodo
        self.__Coordenador = Coordenador
        self.__disciplinas = [] 
        
    def _mostrarDados(self):
        return print(self.__repr__())
        
    def _setNome(self, nome):
        self.__nome = nome

    def _getNome(self):
        return self.__nome
    
    def _setDisciplinas(self, disciplina):
        self.__disciplinas.append(disciplina)

    def _getDisciplinas(self):
        return self.__disciplinas
    
    def _setPeriodo(self, periodo):
        self.__periodo = periodo
        
    def _getPeriodo(self):
        return self.__periodo
    
    def _setCoordenador(self, coordenador):
        self.__Coordenador = coordenador
    
    def _getCoordenador(self):
        return self.__Coordenador
    
    def __repr__(self) -> str:
        return f"curso(s): {self.__nome}, Período: {self.__periodo}"