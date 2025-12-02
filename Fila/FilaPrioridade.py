class Pessoa: 
    def __init__(self, nome, idade, prioridade: int = 0):
        self._nome = nome
        self._idade = idade
        self._prioridade = prioridade
    
    def __str__(self):
        tipo = "Prioridade" if self._prioridade > 0 else "Normal"
        return f"[{tipo}] {self._nome}"

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
        # Ponteiros para a Fila Normal
        self._inicio = None
        self._fim = None
        self._tamanho = 0
        
        # Ponteiros para a Fila de Prioridade
        self._inicio_prioridade = None
        self._fim_prioridade = None
        self._tamanho_prioridade = 0
        
        # Contador para controlar a regra 3:1
        self._qtd_prioridades = 0
    
    def getTamanho(self):
        return self._tamanho + self._tamanho_prioridade
    
    def enfileirar(self, valor: Pessoa):
        """
        Adiciona uma pessoa na fila correta (Normal ou Prioridade)
        baseado no atributo 'prioridade' da pessoa.
        """
        # TODO: Implementar lógica de inserção encadeada
        pass
    
    def desenfileirar(self):
        """
        Retorna a próxima pessoa a ser atendida baseada na regra 3:1.
        Se prioridade < 3 e houver prioridade -> remove da prioridade.
        Senão -> remove da normal e zera contador.
        Tratar casos de filas vazias!
        """
        # TODO: Implementar lógica de remoção encadeada e regra de negócio
        pass

    def mostrarFila(self):
        """
        Imprime o conteúdo das duas filas percorrendo os nós.
        """
        # TODO: Implementar percurso e impressão
        pass

if __name__ == "__main__":
    # 1. Instancia a Fila
    fila = Fila()

    # 2. Criação de Pessoas (Cenário misto)
    p1 = Pessoa("Sr. João (Idoso)", 70, 1)
    p2 = Pessoa("Sra. Maria (Gestante)", 30, 1)
    p3 = Pessoa("Pedro (PCD)", 25, 1)
    p4 = Pessoa("Dona Ana (Idosa)", 80, 1)
    
    n1 = Pessoa("Carlos (Normal)", 25, 0)
    n2 = Pessoa("Beatriz (Normal)", 33, 0)
    n3 = Pessoa("Fernanda (Normal)", 19, 0)

    print("--- 1. Enfileirando ---")
    fila.enfileirar(p1)
    fila.enfileirar(p2)
    fila.enfileirar(n1)
    fila.enfileirar(p3)
    fila.enfileirar(n2)
    fila.enfileirar(p4)
    fila.enfileirar(n3)
    
    # Visualização esperada: 
    # Prioridade: João, Maria, Pedro, Ana
    # Normal: Carlos, Beatriz, Fernanda
    fila.mostrarFila() 

    print("\n--- 2. Atendimento (Regra 3 Pri : 1 Normal) ---")
    
    # 1º Atendimento: Prioridade 1 (João)
    print(f"Atendido: {fila.desenfileirar()}") 
    
    # 2º Atendimento: Prioridade 2 (Maria)
    print(f"Atendido: {fila.desenfileirar()}") 
    
    # 3º Atendimento: Prioridade 3 (Pedro)
    print(f"Atendido: {fila.desenfileirar()}") 
    
    # 4º Atendimento: Já foram 3 prioridades. Agora deve ser Normal (Carlos)
    print(f"Atendido: {fila.desenfileirar()}") 
    
    # 5º Atendimento: Resetou o contador. Volta para Prioridade (Ana)
    print(f"Atendido: {fila.desenfileirar()}") 

    print("\n--- 3. Verificando fim da fila de prioridade ---")
    # A fila de prioridade acabou. O sistema deve ser inteligente e chamar os normais restantes.
    
    # 6º Atendimento: Não tem prioridade, deve chamar Normal (Beatriz)
    print(f"Atendido: {fila.desenfileirar()}")
    
    # 7º Atendimento: Normal (Fernanda)
    print(f"Atendido: {fila.desenfileirar()}")

    print("\n--- 4. Estado Final (Deve estar vazio) ---")
    fila.mostrarFila()