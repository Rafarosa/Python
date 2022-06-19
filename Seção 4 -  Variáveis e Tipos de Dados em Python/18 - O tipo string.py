"""
Tipo string

Em Python, um dado é considerado tipo string sempre que:
- Estiver entre àspas simples -> 'uma string', '1234', 'a', 'True', '42.3'
- Estiver entre àspas duplas -> "texto longo", "y = -b +-", "1234"
- Estiver entre àspas simples triplas -> '''uma string''', '''1234''', '''a''', '''True''', '''42''.3'''
- Estiver entre àspas tripas duplas -> onde estamos escrevendo esse texto
"""
"""
nome = 'Rafael A.R da Rosa'
print(nome)
print(type(nome))

bar = "Mano's bar"
print(bar)
print(type(bar))

atriz = "Angelina \" Jolie"
print(atriz)
print(type(atriz))

nome = 'Alisa Quinteiro Machado'
print(nome.upper())
print(nome.lower())
print(nome.split()) # transforma em uma lista de strings
print(nome.split()[0]) # Retorna o valor de cada item da lista criada apartira do split do nome
print(nome.split()[1])

[:: -1] -  Começa a retornar os elemento em ordem inversa
print(nome[:: -1])

barcode = '65590000020249650024696000084002480690000001490'
print(f'{barcode[0:3]}{barcode[9:13]}')
"""
nome = 'Alisa Quinteiro Machado'
"""
[:: -1] -  Começa a retornar os elemento em ordem inversa
"""
print(nome[:: -1]) # inversão Pythônico

print(nome.upper()) # converte letras em maiúsculas
print(nome.lower()) # converte letras em minúsculas
print(nome.split()) # transforma em uma lista de strings
print(nome.split()[0]) # Retorna o valor de cada item da lista criada apartira do split do nome
print(nome.split()[1]) # Retorna o valor de cada item da lista criada apartira do split do nome
print(nome[:: -1])  # Começa a retornar os elemento em ordem inversa

s = "Olá, mundo!"
print(s.replace("mundo", "meu abacate")) # Substitui uma substring por alguma outra coisa.

