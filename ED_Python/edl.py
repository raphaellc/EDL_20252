# Criação de uma lista de números
numeros = [10, 20, 30, 40]
print(f"Lista original: {numeros}")

# Listas são mutáveis: o elemento no índice 1 é alterado
numeros[1] = 25
print(f"Lista após modificar o segundo elemento: {numeros}")

# Adicionando um novo elemento ao final da lista
numeros.append(50)
print(f"Lista após adicionar o número 50: {numeros}")

# Criação de uma tupla para coordenadas
coordenadas = (12.5, 60.0, 9.8)
print(f"Tupla de coordenadas: {coordenadas}")

# Acessando um elemento pelo índice
print(f"O primeiro elemento é: {coordenadas[0]}")

# Tuplas são imutáveis, então a linha abaixo causaria um erro:
# TypeError: 'tuple' object does not support item assignment
# coordenadas[0] = 10.0

# Criação de um conjunto a partir de uma lista com valores duplicados
numeros_com_duplicatas = [1, 2, 2, 3, 4, 4, 4]
conjunto_numeros = set(numeros_com_duplicatas)
print(f"Lista original: {numeros_com_duplicatas}")
print(f"Conjunto (duplicatas são removidas): {conjunto_numeros}")

# Verificando a existência de um item no conjunto
print(f"O número 3 está no conjunto? {3 in conjunto_numeros}")

# Criação de um dicionário de contatos
contatos = {'Ana': 1234, 'Bia': 5678}
print(f"Dicionário de contatos: {contatos}")

# Acessando o valor associado à chave 'Bia'
print(f"Telefone da Bia: {contatos['Bia']}")

# Adicionando um novo par chave-valor
contatos['Carlos'] = 9101
print(f"Dicionário atualizado: {contatos}")

