from No import No
from Pessoa import Pessoa
class Fila:
    def __init__(self):
        self._inicio = None
        self._fim = None
        self._tamanho = 0
        self._inicio_prioridade = None
        self._fim_prioridade = None
        self._tamanho_prioridade = 0
        self._qtd_prioridades = 0
    
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
    
    def enfileirar(self, valor:Pessoa):
        novo_no = No(valor)
        if novo_no.valor._prioridade > 0:
            if self._inicio_prioridade is None:
                self._inicio_prioridade = novo_no
                self._fim_prioridade = novo_no
            else:
                self._fim_prioridade.setProximo(novo_no)
                novo_no.setAnterior(self._fim_prioridade)
                self._fim_prioridade = novo_no
            self._tamanho_prioridade += 1
        else:    
            if self._inicio is None:
                self._inicio = novo_no
                self._fim = novo_no
            else:
                self._fim.setProximo(novo_no)
                novo_no.setAnterior(self._fim)
                self._fim = novo_no
            self._tamanho += 1
    
    def mostrarFila(self):
        print("--- Fila Normal ---")
        if self._inicio is None:
            print("Fila normal vazia")
        else:
            self._mostrarFilaRecursivo(self._inicio)
        
        print("\n--- Fila Prioridade ---")
        if self._inicio_prioridade is None:
             print("Fila de prioridades vazia")
        else:
             self._mostrarFilaRecursivo(self._inicio_prioridade)
        print("-------------------------")

    def _mostrarFilaRecursivo(self, no_atual):
        print (no_atual.getValor().getNome())
        if no_atual.getProximo() is not None:
            self._mostrarFilaRecursivo(no_atual.getProximo())
    
    def desenfileirar(self):
        no_retorno : No = None     
        if self._qtd_prioridades < 3 and self._tamanho_prioridade > 0:
            if self._inicio_prioridade is None:
                print("Fila de prioridades vazia")
                return None
            self._qtd_prioridades += 1
            no_retorno = self._inicio_prioridade 
            self._inicio_prioridade = self._inicio_prioridade.getProximo()
            self._tamanho_prioridade -= 1
            if self._inicio_prioridade is None:
                self._fim_prioridade = None
            else:
                self._inicio_prioridade.setAnterior(None)
            return no_retorno.valor.getNome()
        else:
            self._qtd_prioridades = 0
            if self._inicio is None:
                print("Fila Normal Vazia")
                return None
            else:
                no_retorno = self._inicio
                self._inicio = self._inicio.getProximo()
                self._tamanho -= 1
                if self._inicio is None:
                    self._fim = None
                else:
                    self._inicio.setAnterior(None)
                return no_retorno.valor.getNome()
    
            