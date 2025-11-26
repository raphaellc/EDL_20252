# ----------------------------------------------------------------------
# Estrutura do QuickSort em Python com visualização didática (Debug)
#
# O pivô é escolhido como o último elemento do subarray (a[high]).
# Inclui prints para acompanhar comparações, trocas e o estado dos índices.
# ----------------------------------------------------------------------

def exchange(a, i, j):
    """
    Função auxiliar para trocar dois elementos na lista.
    Exibe a informação da troca.
    """
    # [TROCA] Informa qual elemento está sendo trocado e em quais índices.
    print(f"    [TROCA]: Trocando {a[i]} (índice {i}) por {a[j]} (índice {j}).")
    a[i], a[j] = a[j], a[i]

def partition(a, low, high):
    """
    Função de Particionamento (Lomuto modificado).
    Exibe o estado inicial e o processo de iteração.
    """
    print("\n" + "="*80)
    # [CONTEXTO] Informa o intervalo e o pivô da chamada atual
    print(f"| FUNÇÃO PARTITION: low={low}, high={high}")
    pivot = a[high]
    print(f"|   Pivô escolhido (a[{high}]): {pivot}")
    print(f"|   Array no escopo do Partition: {a[low:high+1]} (índices de {low} a {high})")
    print(f"|   Array Completo Atual: {a}")
    print("="*80)

    # Índice do menor elemento (elemento de troca)
    # No início, 'i' está fora do array (low - 1)
    i = low - 1  

    # Percorre todos os elementos do subarray, exceto o pivô (high)
    for j in range(low, high):
        
        # === Visualização do Teste de Mesa (Ponteiros) ===
        pointers = ["   "] * len(a)
        if i >= low:
            pointers[i] = "i <="
        pointers[j] = "j"
        pointers[high] = "Pivô"
        
        # Imprime o estado atual da lista e dos ponteiros
        print(f"\n| Estado Array:   [{'|'.join([f'{val:^3}' for val in a])}]")
        print(f"| Índices (k):    [{'|'.join([f'{k:^3}' for k in range(len(a))])}]")
        print(f"| Ponteiros (k):  [{'|'.join([f'{p:^3}' for p in pointers])}]")
        
        # [COMPARAÇÃO] Informa a comparação atual
        print(f"| [COMPARAÇÃO]: a[{j}] ({a[j]}) <= Pivô ({pivot})? ", end="")
        
        # Se o elemento atual for menor ou igual ao pivô
        if a[j] <= pivot:
            print("SIM.")
            # Move o índice 'i' para a próxima posição de troca
            i += 1
            # Realiza a troca (exchange)
            exchange(a, i, j)
        else:
            print("NÃO. (a[j] é maior que o Pivô)")

    # Troca final: Coloca o pivô em sua posição correta (i + 1)
    print("-"*80)
    # [FIM LOOP] Troca final do Pivô
    print(f"| [POSICIONAMENTO PIVÔ]: Trocando Pivô ({pivot}) em {high} com a[{i+1}] ({a[i+1]})")
    exchange(a, i + 1, high)
    
    # [CONTEXTO] Resultado do particionamento
    pivot_final_index = i + 1
    print(f"|   Array após Particionamento: {a}")
    print(f"|   Novo índice final do Pivô (p): {pivot_final_index}")
    print("="*80)
    
    return pivot_final_index

def sort(a, low, high):
    """
    Função principal recursiva do QuickSort.
    Exibe o contexto das chamadas recursivas.
    """
    print("\n" + "~"*50)
    # [CONTEXTO] Chamada da função SORT
    print(f"~ FUNÇÃO SORT: Chamada com low={low}, high={high}")
    print(f"~ Subarray atual: {a[low:high+1]}")
    print("~"*50)
    
    # Condição de parada: se o subarray tiver 1 ou 0 elementos
    if low < high:
        # Particiona o array e obtém o índice do pivô
        p = partition(a, low, high)
        print(f"\n~ Posição final do Pivô (p): {p}. O array está particionado em {a[low:p]} | {a[p]} | {a[p+1:high+1]}")
        
        # Chama recursivamente para o lado esquerdo do pivô
        print(f"\n~ [CHAMADA 1 - ESQUERDA]: sort(low={low}, high={p - 1})")
        sort(a, low, p - 1)
        
        # Chama recursivamente para o lado direito do pivô
        print(f"\n~ [CHAMADA 2 - DIREITA]: sort(low={p + 1}, high={high})")
        sort(a, p + 1, high)
    else:
        # [CONTEXTO] Condição de parada
        print(f"~ Condição de Parada Atingida: low ({low}) >= high ({high}). Retorna.")

def quicksort(a):
    """
    Função de inicialização do QuickSort.
    """
    print("="*100)
    print("### INICIANDO QUICK SORT COM DEBUG DIDÁTICO ###")
    print(f"### Array Inicial: {a} (Tamanho: {len(a)}) ###")
    print("="*100)
    
    # Chama a função recursiva com os índices da lista inteira
    sort(a, 0, len(a) - 1)
    
    print("\n" + "="*100)
    print("### QUICK SORT FINALIZADO ###")
    print(f"### Array Final Ordenado: {a} ###")
    print("="*100)


# ----------------------------------------------------------------------
# Exemplo de Uso
# ----------------------------------------------------------------------
if __name__ == '__main__':
    # Exemplo dos slides (adaptado para ter um tamanho 7)
    data = [8, 1, 6, 4, 0, 3, 9, 5]
    
    # Executa o QuickSort e imprime o passo a passo
    quicksort(data)