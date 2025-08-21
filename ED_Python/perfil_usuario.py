# 1. Inicialização do Dicionário
print("--- 1. Inicializando o dicionário ---")
# Um dicionário é uma coleção de pares chave-valor. [cite: 1599]
# As chaves devem ser de um tipo imutável (como strings, números ou tuplas).
perfil_usuario = {
    'id': 101,
    'nome': 'Ana',
    'idade': 28,
    'cidade': 'São Paulo'
}
print(f"Dicionário inicial: {perfil_usuario}")
print("-" * 50)


# 2. Manipulação dos dados na variável original
print("--- 2. Manipulando os dados via variável original ---")

# Atualizando um valor existente
print("\nAtualizando a idade de 28 para 29...")
perfil_usuario['idade'] = 29
print(f"Dicionário atualizado: {perfil_usuario}")

# Adicionando um novo par chave-valor [cite: 1605]
print("\nAdicionando a profissão...")
perfil_usuario['profissao'] = 'Engenheira'
print(f"Dicionário atualizado: {perfil_usuario}")

# Removendo um item usando a palavra-chave 'del'
print("\nRemovendo a cidade...")
del perfil_usuario['cidade']
print(f"Dicionário final: {perfil_usuario}")
print("-" * 50)


# 3. Atribuição a outra variável (Aliasing)
print("--- 3. Atribuindo o dicionário a uma nova variável (alias) ---")
# Quando atribuímos um objeto mutável, como um dicionário, a uma nova variável,
# não criamos uma cópia. Ambas as variáveis passam a apontar para o mesmo objeto.
# Isso é chamado de aliasing. [cite: 1509]
perfil_alias = perfil_usuario
print("Variável 'perfil_alias' agora aponta para o mesmo objeto que 'perfil_usuario'.")
print(f"Conteúdo de perfil_alias: {perfil_alias}")
print("-" * 50)


# 4. Manipulação por meio da nova variável (alias)
print("--- 4. Manipulando os dados via nova variável ---")
print("\nAdicionando o status 'Ativo' usando a variável 'perfil_alias'...")
perfil_alias['status'] = 'Ativo'
print(f"Conteúdo de perfil_alias após a mudança: {perfil_alias}")


# Verificando a variável original para ver o efeito
# Como o objeto é "aliased", mudanças feitas através de um nome afetam o outro. [cite: 1510]
print("\n>>> Verificando o dicionário original ('perfil_usuario') novamente...")
print(f"O dicionário original também reflete a mudança: {perfil_usuario}")
print("\nConclusão: Ambas as variáveis modificam o mesmo e único objeto na memória.")
print("-" * 50)

# Para criar uma cópia independente (shallow copy), use o método .copy()
print("--- Bônus: Criando uma cópia real e independente ---")
perfil_copia = perfil_usuario.copy()
perfil_copia['id'] = 202 # Modificando a cópia
print(f"Objeto original não foi alterado: {perfil_usuario}")
print(f"A cópia foi alterada: {perfil_copia}")