def bubble_sort(a):
    """
    Ordena uma lista usando o algoritmo Bubble Sort.

    Args:
        a: A lista a ser ordenada.
    """
    exchange = True
    while exchange:
        exchange = False
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                # Troca os elementos
                a[i], a[i + 1] = a[i + 1], a[i]
                exchange = True

# Exemplo de uso:
if __name__ == "__main__":
    my_list = [64, 34, 25, 12, 22, 11, 90]
    print(f"Lista original: {my_list}")
    bubble_sort(my_list)
    print(f"Lista ordenada: {my_list}")

    my_strings = ["banana", "maçã", "laranja", "abacaxi"]
    print(f"Lista de strings original: {my_strings}")
    bubble_sort(my_strings)
    print(f"Lista de strings ordenada: {my_strings}")