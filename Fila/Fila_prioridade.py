# --- Definição das Classes Corrigidas ---

class Pessoa: 
    def __init__(self, nome, idade, prioridade: int = 0):
        self._nome = nome
        self._idade = idade
        self._prioridade = prioridade
    
    # Método __str__ adicionado para facilitar a visualização nos testes
    def __str__(self):
        tipo = "Prioridade" if self._prioridade > 0 else "Normal"
        return f"Pessoa(Nome: {self._nome}, Idade: {self._idade}, Tipo: {tipo})"
    
    def __repr__(self):
        return self.__str__()

    def getNome(self):
        return self._nome

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
        # Usando o getter para verificar a prioridade
        if valor.getPrioridade() > 0:
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
    
    # --- MÉTODO MODIFICADO PARA TESTE ---
    # Mostra ambas as filas para depuração
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
        print (no_atual.getValor())
        if no_atual.getProximo() is not None:
            self._mostrarFilaRecursivo(no_atual.getProximo())
    
    def desenfileirar(self):
        # Lógica original fornecida pelo usuário
        no_retorno : No = None      
        if self._qtd_prioridades < 3:
            if self._inicio_prioridade is None:
                print("Fila de prioridades vazia") # Ponto de falha
                return None
            self._qtd_prioridades += 1
            no_retorno = self._inicio_prioridade 
            self._inicio_prioridade = self._inicio_prioridade.getProximo()
            self._tamanho_prioridade -= 1
            if self._inicio_prioridade is None:
                self._fim_prioridade = None
            else:
                self._inicio_prioridade.setAnterior(None)
            return no_retorno.valor
        else:
            self._qtd_prioridades = 0
            if self._inicio is None:
                print("Fila Normal Vazia") # Outro ponto de falha
                return None
            else:
                no_retorno = self._inicio
                self._inicio = self._inicio.getProximo()
                self._tamanho -= 1
                if self._inicio is None:
                    self._fim = None
                else:
                    self._inicio.setAnterior(None)
                return no_retorno.valor

# --- SCRIPT DE TESTE ---
if __name__ == "__main__":

    # 1. Criar Pessoas
    print("Criando pessoas...")
    p1 = Pessoa("Prioridade 1 (Idoso)", 65, 1)
    p2 = Pessoa("Prioridade 2 (Gestante)", 30, 1)
    p3 = Pessoa("Prioridade 3 (PCD)", 40, 1)
    p4 = Pessoa("Prioridade 4 (Idoso)", 80, 1)
    
    n1 = Pessoa("Normal 1", 25, 0)
    n2 = Pessoa("Normal 2", 33, 0)
    n3 = Pessoa("Normal 3", 19, 0)

    # 2. Criar Fila
    fila_atendimento = Fila()

    # 3. Enfileirar em ordem mista
    print("Enfileirando pessoas...")
    fila_atendimento.enfileirar(p1) # Fila P: [P1]
    fila_atendimento.enfileirar(p2) # Fila P: [P1, P2]
    fila_atendimento.enfileirar(n1) # Fila N: [N1]
    fila_atendimento.enfileirar(p3) # Fila P: [P1, P2, P3]
    fila_atendimento.enfileirar(n2) # Fila N: [N1, N2]
    fila_atendimento.enfileirar(p4) # Fila P: [P1, P2, P3, P4]
    fila_atendimento.enfileirar(n3) # Fila N: [N1, N2, N3]


    print("\n--- Estado Inicial das Filas ---")
    fila_atendimento.mostrarFila()

    # 4. Desenfileirar e testar a lógica 3:1
    print("\n--- Iniciando Atendimento (Desenfileirar) ---")
    
    # Contagem de prioridade = 0. Deve chamar P1
    print("\nChamando 1º (esperado: P1)")
    print(f"Atendido: {fila_atendimento.desenfileirar()}") # P1 (Contagem prioridade = 1)
    
    # Contagem de prioridade = 1. Deve chamar P2
    print("\nChamando 2º (esperado: P2)")
    print(f"Atendido: {fila_atendimento.desenfileirar()}") # P2 (Contagem prioridade = 2)

    # Contagem de prioridade = 2. Deve chamar P3
    print("\nChamando 3º (esperado: P3)")
    print(f"Atendido: {fila_atendimento.desenfileirar()}") # P3 (Contagem prioridade = 3)

    # Contagem de prioridade = 3. Deve chamar N1
    print("\nChamando 4º (esperado: N1)")
    print(f"Atendido: {fila_atendimento.desenfileirar()}") # N1 (Contagem prioridade = 0)

    # Contagem de prioridade = 0. Deve chamar P4
    print("\nChamando 5º (esperado: P4)")
    print(f"Atendido: {fila_atendimento.desenfileirar()}") # P4 (Contagem prioridade = 1)

    print("\n--- Estado Atual das Filas ---")
    fila_atendimento.mostrarFila() # Fila P: [Vazia], Fila N: [N2, N3]

    # --- Demonstração da FALHA ---
    # Contagem de prioridade = 1. Fila P está VAZIA.
    # O código irá falhar e não atenderá N2.
    print("\nChamando 6º (Esperado: Falha - 'Fila de prioridades vazia')")
    print(f"Atendido: {fila_atendimento.desenfileirar()}") # Imprime "Fila de prioridades vazia" e retorna None

    # Contagem de prioridade = 1 (não incrementou).
    print("\nChamando 7º (Esperado: Falha - 'Fila de prioridades vazia')")
    print(f"Atendido: {fila_atendimento.desenfileirar()}") # Imprime "Fila de prioridades vazia" e retorna None
    
    print("\n--- Estado Final das Filas (N2 e N3 nunca foram chamados) ---")
    fila_atendimento.mostrarFila()