from No import No
class Fila:
    def __init__(self):
        self._inicio = None
        self._fim = None
        self._tamanho = 0

    def setInicio(self, inicio):
        self._inicio = inicio
    
    def getInicio(self):
        return self._inicio
    
    def setFim(self, fim):
        self._fim = fim
    
    def getFim(self):
        return self._fim
    
    def getTamanho(self):
        return self._tamanho
    
    def enfileirar(self, valor):
        novo_no = No(valor)
        if self._inicio is None:
            self._inicio = novo_no
            self._fim = novo_no
        else:
            self._fim.setProximo(novo_no)
            novo_no.setAnterior(self._fim)
            self._fim = novo_no
        self._tamanho += 1
    
    def mostrarFila(self):
        if self._inicio is None:
            print("Fila vazia")
        else:
            self._mostrarFilaRecursivo(self._inicio)

    def _mostrarFilaRecursivo(self, no_atual):
        print (no_atual.getValor())
        if no_atual.getProximo() is not None:
            self._mostrarFilaRecursivo(no_atual.getProximo())
    
    def desenfileirar(self):
        if self._inicio is None:
            print("Fila vazia")
        else:
            