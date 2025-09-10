from Pessoa import Pessoa
class No:
    __valor: Pessoa
    __proximo: 'No'

    def __init__(self, valor: Pessoa):
        self.__valor = valor
        self.__proximo = None
    
    def defineValor(self, valor: Pessoa):
        self.__valor = valor

    def defineProximo(self, proximo: 'No'):
        self.__proximo = proximo

    def obtemValor(self) -> Pessoa:
        return self.__valor

    def obtemProximo(self) -> 'No':
        return self.__proximo
    
    def __str__(self):
        return str(self.valor) 
    