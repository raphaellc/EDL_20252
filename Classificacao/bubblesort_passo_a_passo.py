# ----------------------------------------------------------------------
# Bubble Sort com visualização ultra-minimalista.
# Exibe APENAS o array (como uma lista de valores) após cada troca efetiva.
# ----------------------------------------------------------------------

def bubble_sort(a):
    """
    Ordena uma lista usando o algoritmo Bubble Sort e imprime o array a cada troca.

    Args:
        a: A lista a ser ordenada.
    """
    n = len(a)
    
    if n == 0:
        print("[]")
        return

    # Imprime o estado inicial
    print(a)

    made_exchange = True
    
    # Loop principal: continua enquanto houver trocas na passagem anterior
    while made_exchange:
        made_exchange = False
        
        # Loop de passagem: percorre o array, comparando pares adjacentes
        for i in range(n - 1):
            # Se o elemento atual for maior que o próximo (desordenado)
            if a[i] > a[i + 1]:
                # Troca os elementos
                a[i], a[i + 1] = a[i + 1], a[i]
                
                # Marca que uma troca foi realizada (portanto, precisamos de outra passagem)
                made_exchange = True
                
                # [LOG ESSENCIAL] Imprime o estado completo do array após a troca
                print(a)
        
        # Opcional: Otimização para diminuir o tamanho da lista a cada passagem
        # n -= 1 # Se descomentar, o algoritmo se torna mais eficiente

# Exemplo de uso:
if __name__ == "__main__":
    
    # Exemplo 1: Lista simples de números
    my_list = [2,7,4,9,3]
    print("\n--- Teste com [64, 34, 25, 12, 22, 11, 90] ---")
    bubble_sort(my_list)

    # Exemplo 2: Lista de strings
    my_strings = ["banana", "maçã", "laranja", "abacaxi"]
    print("\n--- Teste com strings ['banana', 'maçã', 'laranja', 'abacaxi'] ---")
    bubble_sort(my_strings)

    # Exemplo 3: Lista decrescente (pior caso para Bubble Sort)
    pior_caso = [5, 4, 3, 2, 1]
    print("\n--- Teste com [5, 4, 3, 2, 1] ---")
    bubble_sort(pior_caso)