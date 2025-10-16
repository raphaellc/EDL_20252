class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None
    
    def setValor(self, valor):
        self.valor = valor
    
    def getValor(self):
        return self.valor
    
    def setProximo(self, proximo):
        self.proximo = proximo
    
    def getProximo(self):
        return self.proximo
    
    def setAnterior(self, anterior):
        self.anterior = anterior
    
    def getAnterior(self):
        return self.anterior