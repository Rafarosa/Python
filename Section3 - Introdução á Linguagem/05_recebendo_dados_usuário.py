"""
Recebendo dados do Usuário:

input()  todos dado recebido via input é do tipo string

Em Python, string é tudo que estiver entre:
- Aspas simples
- Aspas Duplas
- Aspas simples triplas
- Aspas duaplas simples

Exemplo:
- Aspas simples -> 'Nome'
- Aspas duplas -> "Nome"
- Aspas simples triplas -> ''' Nome '''
"""
# -  Aspas duplas triplas -> """ Nome"""

# Entrada de dados
# print('Qual o seu nome?: ')
# nome = input()  # input = entrada
nome = input('Qual o seu nome?: ')

# Exemplo Print antigo
# print('Seja bem vindo(a) %s' % nome)

# Exemplo de print moderno 'v.3.x'
# print('Seja bem vindo(a) {0}'.format(nome))

# Exemplo de print mais Atual *****
print(f'seja bem vindo {nome}')

# print("Qual é a sua idade?:")
# idade = input()
# Processamento de dados
idade = int(input("Qual é a sua idade?:"))

# Saída de dados
# Exemplo de dados antigo
# print("A %s tem %s anos" % (nome, idade))

# Exemplo print moderno 'v.3.x'
# print('A {0} tem {1} anos'.format(nome, idade))

# Exemplo de print mais Atual *****
print(f'O {nome} tem {idade} anos')

# cast é a conversão de um tipo de dados para outro
print(f'O {nome} nasceu em {2022 - idade}')
