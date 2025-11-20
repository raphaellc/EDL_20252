# ----------------------------------------------------------------------
# Implementação do Odd-Even Sort, seguindo a estrutura do código Java.
#
# NOTA: O Odd-Even Sort completo geralmente requer um loop "while is_sorted"
# externo para garantir que todo o array esteja ordenado. A estrutura
# fornecida aqui usa um loop 'for' simples para controlar o número de passes,
# que é a estrutura exata do seu código Java.
# ----------------------------------------------------------------------

def odd_even_sort(a):
    """
    Ordena uma lista (array) usando o algoritmo Odd-Even Sort.
    
    Args:
        a: A lista (mutável) a ser ordenada.
    """
    n = len(a)
    
    # Loop de controle de passes (equivalente ao "for(int i= 0; i< a.length; i++)" em Java)
    for i in range(n):
        
        # Passo ÍMPAR (compara e troca pares de índices ímpares/pares, ex: (1, 2), (3, 4), ...)
        # A condição (i % 2 != 0) controla quando este passo é executado.
        if i % 2 != 0:
            
            # Percorre a lista para comparar (j-1, j) onde j é PAR e começa em 2.
            for j in range(2, n, 2):
                # Usa o operador '<' para emular o compareTo < 0
                if a[j] < a[j - 1]:
                    # Troca usando a sintaxe Python
                    a[j], a[j - 1] = a[j - 1], a[j]
        
        # Passo PAR (compara e troca pares de índices pares/ímpares, ex: (0, 1), (2, 3), ...)
        # Executado quando a condição acima é falsa (i % 2 == 0).
        else:
            
            # Percorre a lista para comparar (j-1, j) onde j é ÍMPAR e começa em 1.
            for j in range(1, n, 2):
                if a[j] < a[j - 1]:
                    # Troca usando a sintaxe Python
                    a[j], a[j - 1] = a[j - 1], a[j]

# ----------------------------------------------------------------------
# Exemplo de Uso
# ----------------------------------------------------------------------
if __name__ == '__main__':
    # Lista de teste com inteiros
    data = [7, 4, 3, 1, 6, 8, 2, 5]
    print(f"Lista original: {data}")
    
    odd_even_sort(data)
    
    print(f"Lista ordenada: {data}")

    # Exemplo com lista já ordenada (não fará trocas)
    data_2 = [1, 2, 3, 4, 5]
    print(f"\nLista original 2: {data_2}")
    odd_even_sort(data_2)
    print(f"Lista ordenada 2: {data_2}")