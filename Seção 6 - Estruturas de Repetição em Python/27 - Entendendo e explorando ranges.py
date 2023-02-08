"""
Ranges
- Precisamos conhecer o loop for para usar o ranges.
- precisamos conhecer range para trabalahar melhor com loop for

Ranges são utilizados para gerar sequências numéricas, não aleatórias, mas de maneira especificada

Formas gerais:

Forma 01

range(valor_de_parada)
OBS: valor_de_parada não inclusiva (início padrão 0, e passo de 1 em 1)
"""
# Exemplo 1
for num in range(11):
    print(num)
print('________________')
"""
Forma 02

range (valor_de_inicio, valor_de_parada)
OBS: valor_de_parada não inclusiva (início especificado pelo usuário, e passo de 1 em 1)
"""
# Exemplo 02
for num1 in range(1,11):
    print(num1)
print('________________')
"""
Forma 03

range (valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusiva (início especificado pelo usuário, e passo especificado pelo usuário)
"""
# Exemplo 03
for num2 in range(1,15,2):
    print(num2)
print('________________')
"""
Forma 04 (Inversa)

range (valor_de_inicio, valor_de_parada, passo)
OBS: valor_de_parada não inclusiva (início especificado pelo usuário, e passo especificado pelo usuário)
"""
## Exemplo 04

for num3 in range(10, 0, -1):
    print(num3)
print('________________')