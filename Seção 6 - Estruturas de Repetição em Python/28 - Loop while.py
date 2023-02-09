"""
loop while

Forma geral

while expressão_boleana:
    //execução do loop

O bloco do while será repedido enaquendo a expressão booleana for verdadeira.

expressão booleana é toda a expressão onde o resultado é verdadeiro ou falso
"""
numero01 = 1

while numero01 < 10:
    print(numero01)
    numero01 += 1
# OBS: em um loop while, é importante que cuidemos do critério de parada para não causar um loop infinito.

"""
Exemplo 02
"""
resposta = ''
while resposta != 'Sim':
    resposta = input('Já terminou Jessica??? ')

