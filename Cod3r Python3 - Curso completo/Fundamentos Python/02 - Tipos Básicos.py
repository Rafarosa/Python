# tipos basicos 

# booleanos (bool)
# São considerados os valores True e False
print ('valor verdadeiro é', True)
print('valor Falso é', False)


verdadeiro = True
falso = False

print('o valor da variavel verdadeiro é', verdadeiro)
print('o valor da variavel falso é', falso)

print('O valor da negação da variavel verdadeiro é', not verdadeiro)
print('O valor da negação da variavel falso é', not falso)

# inteiros (int)
# São considerados todos os valores inteiros 

print (1,2,3)

"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: O separados de casas decimais na programação é o ponto e não a vírgula.
"""

# Errado do ponto de vista do Float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))


# Certo do ponto de vista Float
valor = 1.44
print(valor)
print(type(valor))

# É possível fazer dupla atribuição
valor1, valor2 = 1, 44
print(valor1)
print(type(valor1))
print(valor2)
print(type(valor2))

# Podemos converter um float para um int
"""
OBS: Ao converter valores float para inteiros, nós perdemos precisão.
"""
res = int(valor)
print(res)
print(type(res))

#  Podemos trabalhar com números complexos
variavel = 5j

"""
Tipo string

Em Python, um dado é considerado do tipo string sempre que:

- Estiver entre àspas simples -> 'uma string', '234', 'a', 'True', '42.3'
- Estiver entre àspas duplas -> "uma string", "234", "a", "True", "42.3"
- Estiver entre àspas simples triplas -> '''uma string''', '''234''', '''a''', '''True''', '''42.3'''
"""
nome = 'Rafael Rosa'
print(nome)
print(type(nome))

nome = "Gina's Bar"
print(nome)
print(type(nome))

"""
Tipo lista

Um dos tipos mais versáteis em Python são as listas (list), comparado com outras linguagens uma
lista é similar a uma array, porém ela vai muito além disso. As listas não são tipadas, ou seja cada
elemento pode ser de um tipo diferente, além disso existe o conceito de slicing que permite formas
extremamente poderosas de acesso aos seus elementos.

"""

lista = []
print(type(lista))
print(dir(lista))


"""
Diccionários (dict)

Um dicionário é algo similar a uma lista de chave e valor, mas sem ordenação, por que as chaves
são transformadas em hashs por questão de performance.
Assim como as listas, os dicionários não são tipados, nem a chave, nem o valor. Mas a chave precisa
ser de um tipo imutável (como str, int, float ou tuple) ou seja cada elemento pode ser de um tipo
diferente. Vamos a alguns exemplos
"""

pessoa = {'nome': 'Juracy Filho', 'idade': 43, 'cursos': ['docker', 'python']}
print(type(pessoa))

print(len(pessoa))
print(pessoa)
print(pessoa['nome'])
