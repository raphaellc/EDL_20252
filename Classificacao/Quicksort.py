# ----------------------------------------------------------------------
# Estrutura do QuickSort em Python, seguindo o padrão de 3 funções
# da implementação em Java (Página 5 do PDF).
#
# O pivô é escolhido como o último elemento do subarray (a[high]).
# ----------------------------------------------------------------------

def exchange(a, i, j):
    """Função auxiliar para trocar dois elementos na lista."""
    a[i], a[j] = a[j], a[i]

def partition(a, low, high):
    """
    Função de Particionamento (Hoare/Lomuto modificado).
    
    Seleciona o pivô como o elemento em a[high].
    Rearranja o subarray a[low..high] para que:
    1. Todos os elementos <= pivô fiquem à esquerda.
    2. Todos os elementos > pivô fiquem à direita.
    3. O pivô esteja em sua posição final correta.

    Retorna o índice final do pivô.
    """
    # 1. Escolhe o pivô (o último elemento)
    pivot = a[high]
    
    # 2. Índice do menor elemento (elemento de troca)
    # Segue a lógica: i = low - 1;
    i = low - 1  

    # 3. Percorre todos os elementos do subarray (exceto o pivô)
    for j in range(low, high):
        # Se o elemento atual for menor ou igual ao pivô
        if a[j] <= pivot:
            # Incrementa o índice do menor elemento
            i += 1
            # Coloca a[j] na região "<= pivô"
            exchange(a, i, j)

    # 4. Coloca o pivô em sua posição final correta, 
    # trocando-o com o primeiro elemento da região "> pivô" (i + 1)
    exchange(a, i + 1, high)
    
    # 5. Retorna o índice onde o pivô foi colocado
    return i + 1

def sort(a, low, high):
    """
    Função principal recursiva do QuickSort.
    Ordena o subarray a[low..high].
    """
    # Condição de parada: se o subarray tiver 1 ou 0 elementos
    if low < high:
        # Particiona o array e obtém o índice do pivô
        # a[p] está agora em sua posição final
        p = partition(a, low, high)

        # Chama recursivamente para o lado esquerdo do pivô
        sort(a, low, p - 1)
        
        # Chama recursivamente para o lado direito do pivô
        sort(a, p + 1, high)

def quicksort(a):
    """
    Função de inicialização do QuickSort.
    Recebe a lista/array e inicia a ordenação.
    """
    # Chama a função recursiva com os índices da lista inteira
    sort(a, 0, len(a) - 1)


# ----------------------------------------------------------------------
# Exemplo de Uso
# ----------------------------------------------------------------------
if __name__ == '__main__':
    data = [11, 5, 7, 6, 12, 17, 8]
    print(f"Lista original: {data}")
    
    # Executa o QuickSort
    quicksort(data)
    
    print(f"Lista ordenada: {data}")

    # Outro exemplo
    data_2 = [8, 1, 6, 4, 0, 3, 9, 5]
    print(f"\nLista original 2: {data_2}")
    quicksort(data_2)
    print(f"Lista ordenada 2: {data_2}")