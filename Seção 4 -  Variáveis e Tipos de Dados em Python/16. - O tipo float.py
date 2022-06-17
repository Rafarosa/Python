"""
Tipo Float

Tipo real, decimal

Casas decimais

OBS: separador de casas decimais na programação é ponto e não virgula
"""
# Errado do ponto de vista do Float, mas gera uma tupla
valor = 1, 44
print(valor)
print(type(valor))

# certo do ponto de vista Float

valor = 1.44
print(valor)
print(type(valor))

# É possivel fazer dupla atribuição

valor1, valor2 = 1, 44
print(valor1)
print((type(valor1)))

print(valor2)
print((type(valor2)))

# Podemos converter um floart para um int
"""
OBS: ao converter valores para inteiro, nos pedemos precisão.
"""
res = int(valor) # Remove o ponto flutuante
print(res)
print(type(res))

# Podemos trabalhar com números complexos
vv = 5j
print(type(vv))