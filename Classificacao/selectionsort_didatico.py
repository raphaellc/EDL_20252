# ----------------------------------------------------------------------
# Selection Sort com visualização didática (Teste de Mesa)
# Inclui prints para acompanhar o estado do array e as trocas a cada passo.
# ----------------------------------------------------------------------

def exchange(arr, i, j):
    """
    Troca os elementos nos índices i e j de uma lista e exibe a informação.
    """
    # Verifica se a troca é necessária (Selection Sort faz a troca
    # no final da iteração, mesmo que i e j sejam iguais, mas evitamos 
    # a impressão desnecessária se não houver mudança de fato).
    if i != j:
        print(f"        [TROCA] Realizando troca: {arr[i]} (i={i}) <-> {arr[j]} (j={j})")
        arr[i], arr[j] = arr[j], arr[i]
        # Mostra o array após a troca
        print(f"        [ARRAY APÓS TROCA]: {arr}")
    else:
        # Informa que o elemento já estava na posição correta
        print(f"        [FIM ITERAÇÃO] Posição correta: a[{i}] ({arr[i]}) já é o menor elemento.")


def selection_sort(a):
    """
    Ordena uma lista usando o algoritmo Selection Sort e rastreia o processo.

    Args:
        a: A lista a ser ordenada.
    """
    n = len(a)
    print("\n" + "="*80)
    print(f"INICIANDO SELECTION SORT. Array Inicial: {a}")
    print("="*80)

    # Loop externo: percorre o array, i é o índice do elemento que será ordenado (região ordenada)
    for i in range(n):
        print(f"\n--- ITERAÇÃO {i+1} --- (Buscando o menor para a posição i={i})")
        
        # Assume que o elemento atual é o menor
        min_idx = i
        print(f"    [INÍCIO] Mínimo temporário: a[{min_idx}] = {a[min_idx]}")

        # Loop interno: procura o menor elemento na parte não ordenada (a[i+1] até o final)
        for j in range(i + 1, n):
            # [COMPARAÇÃO] Mostra qual comparação está sendo feita
            print(f"    [COMPARAÇÃO] a[{j}] ({a[j]}) < a[{min_idx}] ({a[min_idx]})? ", end="")
            
            # Se encontrar um elemento menor, atualiza o índice do mínimo
            if a[j] < a[min_idx]:
                min_idx = j
                print(f"SIM. Novo índice mínimo: {min_idx} (valor {a[min_idx]})")
            else:
                print("NÃO.")
        
        # Após o loop interno, trocamos o menor elemento encontrado (min_idx)
        # com o elemento da posição i (início da região não ordenada)
        print(f"\n    [FIM VARREDURA] Menor elemento encontrado em min_idx={min_idx} (valor: {a[min_idx]})")
        print(f"    [POSIÇÃO ATUAL] Trocando com i={i} (valor: {a[i]})")
        
        exchange(a, min_idx, i)
        
        print(f"\n    [FIM DA ITERAÇÃO {i+1}] Array após troca: {a}")
        print("-"*80)

    print("\n" + "="*80)
    print("SELECTION SORT CONCLUÍDO.")
    print(f"Array Final Ordenado: {a}")
    print("="*80)


# Exemplo de uso:
if __name__ == "__main__":
    # Exemplo 1: Lista simples
    my_list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    selection_sort(my_list)

    # Exemplo 2: Lista decrescente (pior caso)
    outra_lista = [5, 4, 3, 2, 1]
    selection_sort(outra_lista)

    # Exemplo 3: Lista quase ordenada
    lista_quase_ordenada = [1, 2, 4, 3, 5]
    selection_sort(lista_quase_ordenada)

    # Exemplo 4: Lista vazia (teste de caso de borda)
    lista_vazia = []
    print(f"\nLista vazia original: {lista_vazia}")
    selection_sort(lista_vazia)
    print(f"Lista vazia ordenada: {lista_vazia}")

    # Exemplo 5: Lista já ordenada (melhor caso)
    lista_ordenada = [1, 2, 3, 4, 5]
    print(f"\nLista já ordenada original: {lista_ordenada}")
    selection_sort(lista_ordenada)
    print(f"Lista já ordenada: {lista_ordenada}")