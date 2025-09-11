from No import No
from Pessoa import Pessoa

class ListaPessoas:
    __inicio_lista: No
    __tamanho: int

    def __init__(self):
        self.__inicio_lista = None
        self.__tamanho = 0

    def inserir(self, valor: Pessoa):
        self.__inserir(valor)
        self.__tamanho += 1

    def __inserir(self, valor: Pessoa):
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
    
    def pesquisarPessoaNome(self, nome: str) -> bool:
        if self.__inicio_lista is None:
            print("A lista está vazia.")
            return False
        no_atual = self.__inicio_lista
        while no_atual is not None:
            if no_atual.obtemValor().getNome() == nome:
                return True
            no_atual = no_atual.obtemProximo()
        return False

    def removerPessoa(self, nome:str) -> bool:
        if self.__inicio_lista == None:
            print("A lista está vazia.")
            return False
        no_atual = self.__inicio_lista
        no_anterior = None

        while no_atual is not None:
            if no_atual.obtemValor().getNome() == nome:
                if no_anterior == None:
                    self.__inicio_lista = no_atual.obtemProximo()
                    return True
                else:
                    no_anterior.defineProximo(no_atual.obtemProximo())
                    return True
            no_anterior = no_atual
            if no_atual != None:
                no_atual = no_atual.obtemProximo()
        return False
        
   
        


if __name__ == "__main__":
    lista = ListaPessoas()
    lista.inserir(Pessoa("João", 25, 1.75))
    lista.inserir(Pessoa("Maria", 30, 1.65))
    lista.inserir(Pessoa("Pedro", 22, 1.80))
    if lista.pesquisarPessoaNome("Mario"):
        print("A pessoa existe na lista.")
    else:
        print("A pessoa não existe na lista.")
    
    lista.listarValores()
    lista.removerPessoa("João")
    lista.listarValores()
    lista.removerPessoa("Maria")
    lista.listarValores()

    if lista.removerPessoa("João")

    lista.removerPessoa("Pedro")
    lista.listarValores()
    
