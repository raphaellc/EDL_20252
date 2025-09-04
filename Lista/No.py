class No:
    __valor: int
    __proximo: 'No'

    def __init__(self, valor: int):
        self.__valor = valor
        self.__proximo = None
    
    def defineValor(self, valor: int):
        self.__valor = valor

    def defineProximo(self, proximo: 'No'):
        self.__proximo = proximo

    def obtemValor(self) -> int:
        return self.__valor

    def obtemProximo(self) -> 'No':
        return self.__proximo
    
    def __str__(self):
        return str(self.valor) 
    