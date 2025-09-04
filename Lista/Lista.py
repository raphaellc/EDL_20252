from No import No

class Lista:
    __inicio_lista: 'No'
    __tamanho: int

    def __init__(self):
        self.__inicio_lista = None
        self.__tamanho = 0

    def inserir(self, valor: int):
        self.__inserir(valor)
        self.__tamanho += 1

    def __inserir(self, valor: int):
        if self.__inicio_lista is None:
            self.__inicio_lista = No(valor)
        else:
            no_atual = self.__inicio_lista
            while no_atual.obtemProximo() is not None:
                no_atual = no_atual.obtemProximo()

            no_atual.defineProximo(No(valor))

    def listarValores(self):
        if self.__inicio_lista is None:
            print("A lista está vazia.")
            return

        no_atual = self.__inicio_lista
        while no_atual is not None:
            print(no_atual.obtemValor())
            no_atual = no_atual.obtemProximo()

    def existe(self, valor) -> bool:
        no_atual = self.__inicio_lista
        while no_atual is not None:
            if no_atual.obtemValor() == valor:
                return True
        return False
    
    def remover(self, valor):


if __name__ == "__main__":
    lista = Lista()
    lista.inserir(1)
    lista.inserir(2)
    lista.inserir(3)
    lista.listarValores()

