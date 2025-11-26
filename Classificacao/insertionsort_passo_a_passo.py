# ----------------------------------------------------------------------
# Insertion Sort com visualização ultra-minimalista.
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
        # 
        print(arr)
    else:
        # Quando i == j, o elemento já estava na posição correta ou 
        # a troca não é necessária, e nenhuma impressão é feita.
        pass


def insertion_sort(a):
    """
    Ordena uma lista de inteiros usando o algoritmo Insertion Sort.

    Args:
        a: A lista a ser ordenada.
    """
    n = len(a)
    
    if n == 0:
        print("[]")
        return

    # Imprime o estado inicial
    print(a)

    # Loop externo: Começa do segundo elemento (índice 1), pois o primeiro é trivialmente ordenado
    for i in range(1, n):
        # j é o índice do elemento a ser inserido na sublista ordenada
        j = i
        
        # Loop interno: Move o elemento a[j] para a esquerda até que ele esteja
        # em sua posição correta na sublista ordenada (a[0..j-1])
        while j > 0 and a[j - 1] > a[j]:
            # Troca a[j-1] e a[j], movendo a[j] (o elemento atual) uma posição para trás
            exchange(a, j - 1, j)
            j -= 1


# Exemplo de uso:
if __name__ == "__main__":
    
    # Exemplo 1: Lista simples
    lista_exemplo = [2, 7, 4, 9, 3]
    print("\n--- Teste com [2, 7, 4, 9, 3] ---")
    insertion_sort(lista_exemplo)
    # print(f"Lista ordenada final: {lista_exemplo}") # Removido para manter a saída limpa

    # Exemplo 2: Lista maior e mais complexa
    outra_lista = [7, 2, 9, 1, 4, 3, 8, 6, 5]
    print("\n--- Teste com [7, 2, 9, 1, 4, 3, 8, 6, 5] ---")
    insertion_sort(outra_lista)
    # print(f"Lista ordenada final: {outra_lista}") # Removido para manter a saída limpa

    # Exemplo 3: Lista vazia
    lista_vazia = []
    print("\n--- Teste com [] ---")
    insertion_sort(lista_vazia)

    # Exemplo 4: Lista de um elemento
    lista_um_elemento = [42]
    print("\n--- Teste com [42] ---")
    insertion_sort(lista_um_elemento)