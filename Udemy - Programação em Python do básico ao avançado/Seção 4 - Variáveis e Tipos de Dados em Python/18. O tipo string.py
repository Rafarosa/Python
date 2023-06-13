"""
Tipo String

já vimos que em python, um dado é considerado um tipo string sempre que:
- Estiver entre àspas simples -> 'uma string', '123', 'a', 'true', '43.6'
- Estiver entre àspas duplas -> "uma string", "123", "a", "true, "43.6"
- Estiver entra àspas simples truplas: ''' texto, número ou booleano '''
- Estiver entre àspas duplas triplas: 
"""
nome = 'Rafael Rosa'
print(nome)
print(type(nome))

nomeComApostrofo = "Ginas's bar"
print(nomeComApostrofo)

nomeFamoso = 'Angelina\nJolie'
print(nomeFamoso)

nomeFamoso2 = 'Rubens Alamo'

print(nomeFamoso.upper()) # todas as letras maiúsculas
print(nomeFamoso2.lower())# todas as letras em minúsculas
print(nomeComApostrofo.split())# transforma a string em uma lista de strings

# toda a string é uma lista e pode ser acessado cada uma das 'letra' da palavras
print(nomeFamoso[0:9])
print(nomeFamoso.split()[0])
print(nomeFamoso.split()[1])

#invertendo a ordem da string 
print(nomeFamoso[::-1])

# Substituição de caracteres
print(nomeComApostrofo.replace('a', 'q'))