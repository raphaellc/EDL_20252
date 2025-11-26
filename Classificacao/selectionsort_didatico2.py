# ----------------------------------------------------------------------
# Selection Sort com visualização ultra-minimalista.
# Exibe APENAS o array (como uma lista de valores) após cada troca efetiva.
# ----------------------------------------------------------------------

def exchange(arr, i, j):
    """
    Troca os elementos nos índices i e j de uma lista.
    Imprime o array após a troca, apenas se i e j forem diferentes.
    """
    # Verifica se a troca é entre índices diferentes
    if i != j:
        # Troca os elementos
        arr[i], arr[j] = arr[j], arr[i]
        
        # [LOG ESSENCIAL] Imprime o estado completo do array após a troca
        print(arr)
    else:
        # Quando i == j, o elemento já estava na posição correta,
        # e nenhuma impressão é feita.
        pass


def selection_sort(a):
    """
    Ordena uma lista usando o algoritmo Selection Sort.

    Args:
        a: A lista a ser ordenada.
    """
    n = len(a)
    
    if n == 0:
        print("[]")
        return

    # Imprime o estado inicial
    print(a)

    # Loop externo: percorre o array (i é o índice da posição a ser preenchida)
    for i in range(n):
        # Assume que o elemento na posição 'i' é o menor
        min_idx = i

        # Loop interno: procura o menor elemento na parte não ordenada (a[i+1] até o final)
        for j in range(i + 1, n):
            # Se encontrar um elemento menor, atualiza o índice do mínimo
            if a[j] < a[min_idx]:
                min_idx = j
        
        # Troca o menor elemento encontrado (min_idx) com o elemento da posição i
        exchange(a, i, min_idx)


# Exemplo de uso:
if __name__ == "__main__":
    # Exemplo solicitado
    data_exemplo = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    selection_sort(data_exemplo)

    # Outro exemplo
    # print("\n--- Teste com [64, 25, 12, 22, 11] ---")
    # my_list = [64, 25, 12, 22, 11]
    # selection_sort(my_list)