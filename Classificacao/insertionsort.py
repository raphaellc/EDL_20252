def exchange(arr, i, j):
    """
    Troca os elementos nos índices i e j de uma lista.
    """
    arr[i], arr[j] = arr[j], arr[i]

def insertion_sort(a):
    """
    Ordena uma lista de inteiros usando o algoritmo Insertion Sort,
    baseado na lógica Java fornecida na imagem.

    Args:
        a: A lista a ser ordenada.
    """
    # Loop externo: Começa do segundo elemento (índice 1)
    for i in range(1, len(a)):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            exchange(a, j - 1, j)
            j -= 1

# Exemplo de uso:
if __name__ == "__main__":
    lista_exemplo = [12, 11, 13, 5, 6]
    print(f"Lista original: {lista_exemplo}")
    insertion_sort(lista_exemplo)
    print(f"Lista ordenada: {lista_exemplo}")

    outra_lista = [7, 2, 9, 1, 4, 3, 8, 6, 5]
    print(f"Outra lista original: {outra_lista}")
    insertion_sort(outra_lista)
    print(f"Outra lista ordenada: {outra_lista}")

    lista_vazia = []
    print(f"Lista vazia original: {lista_vazia}")
    insertion_sort(lista_vazia)
    print(f"Lista vazia ordenada: {lista_vazia}")

    lista_um_elemento = [42]
    print(f"Lista de um elemento original: {lista_um_elemento}")
    insertion_sort(lista_um_elemento)
    print(f"Lista de um elemento ordenada: {lista_um_elemento}")