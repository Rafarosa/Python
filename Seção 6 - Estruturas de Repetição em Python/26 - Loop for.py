"""
Loop for

Loop - Estrutura de repetição
For -  Uma dessas estrutura

Estrutura do for em Python

for item in interavel:
    // execução do loop

Utilizamos loops para interar sobre sequëncias ou sebre valores interãveis

Exemplo de interãveis
- String
    nome = 'Rafael AR da Rosa'
- Lista
    lista = [1,2,3,4 5]
- Range
    numeros =  range(1,10)

"""

# Exemplo de for 1 (Iterando com uma String)
nome = 'Rafael AR da Rosa'
lista = [1, 3, 5, 7, 8]
numeros = range(1,10)


for letras in nome:
    print(letras)

# Exemplo for 2 (Iterando sobre uma lista)

for numeros in lista:
    print(numeros)

# Exemplo for 3 (Iterando com um range)
#OBS: o valor final não é inclusivo
for numeros_range in range(1,10):
    print(numeros_range)

# Enumerate

for indice, letra in enumerate(nome):
    print(indice,nome[indice])

for valor in enumerate(nome):
    print(valor)

# Exemplo em uma necessidade de imprimir x vezes algo

qtd = int(input('Informe quantas vezes você quer que imprima a frase Oi: '))
for i in range(1, qtd + 1):
    print (f'Oi {i}')