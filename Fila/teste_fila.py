from Fila import Fila
from Pessoa import Pessoa

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