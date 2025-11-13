def exchange(arr, i, j):
    """
    Troca os elementos nos índices i e j de uma lista.
    """
    arr[i], arr[j] = arr[j], arr[i]

def selection_sort(a):
    """
    Ordena uma lista usando o algoritmo Selection Sort.

    Args:
        a: A lista a ser ordenada.
    """

    for i in range(len(a)):
        min_idx = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min_idx]:
                min_idx = j
        exchange(a, min_idx, i)

# Exemplo de uso:
if __name__ == "__main__":
    my_list = [64, 25, 12, 22, 11]
    print(f"Lista original: {my_list}")
    selection_sort(my_list)
    print(f"Lista ordenada: {my_list}")

    outra_lista = [5, 4, 3, 2, 1]
    print(f"Outra lista original: {outra_lista}")
    selection_sort(outra_lista)
    print(f"Outra lista ordenada: {outra_lista}")

    lista_quase_ordenada = [1, 2, 4, 3, 5]
    print(f"Lista quase ordenada original: {lista_quase_ordenada}")
    selection_sort(lista_quase_ordenada)
    print(f"Lista quase ordenada: {lista_quase_ordenada}")

    lista_vazia = []
    print(f"Lista vazia original: {lista_vazia}")
    selection_sort(lista_vazia)
    print(f"Lista vazia ordenada: {lista_vazia}")