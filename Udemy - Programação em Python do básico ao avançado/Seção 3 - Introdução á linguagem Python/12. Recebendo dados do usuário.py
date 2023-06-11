""" 
Recebendo dados do usuário

input() -> Todo dado Recebido via inputé do tipo String

Em python, string é todo o que estiver entre:
- Aspas simples;
- Aspas duplas;
- Aspas simples triplas
- Aspas duplas triplas

Exemplo
- Aspas simples - 'Nome próprio'

- Aspas Duplas - "Nome composto maior"

- Aspas Duplas triplas -> usado para textos grandes

"""
# Entrada de dados
nome = input("Qual o seu nome?: ")

# Exemplo antigo, versão 2x
# print('Seja bem vindo(a) %s' %nome)
# Exemplo moderno, versão 3.x
# print('Seja bem vindo(a) {0}'.format(nome))
# Exemplo Atual
print(f'Seja bem-vindo {nome}')

#print('Qual sua idade?: ')
idade = int(input('Qual sua idade?: '))

# processamento

# Saída
# Exemplo antigo, versão 2x
# print('A %s tem %s anos' % (nome,idade))
# Exemplo moderno, versão 3.x
# print('A {0} tem {1} anos'.format(nome, idade))
# Exemplo Atual
print(f'A {nome} tem idade {idade} anos')

"""
int(idade) -> Cast

Cast é a conversão de um tipo de dado para outro 
"""
print(f'A {nome} nasceu em {2023 - idade}')
