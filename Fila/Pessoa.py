class Pessoa: 
    def __init__(self, nome : str, idade, prioridade: int = 0):
        self._nome = nome
        self._idade = idade
        self._prioridade = prioridade

    def getNome(self):
        return self._nome

    def getIdade(self):
        return self._idade          
    
    def getIdade(self):
        return self._idade
    def getPrioridade(self):
        return self._prioridade
    
    def setNome(self, nome):
        self._nome = nome

    def setIdade(self, idade):
        self._idade = idade

    def setPrioridade(self, prioridade):
        self._prioridade = prioridade   

