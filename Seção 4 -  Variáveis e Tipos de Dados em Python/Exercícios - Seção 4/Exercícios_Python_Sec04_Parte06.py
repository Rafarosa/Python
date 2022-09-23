import math

print('51 - Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância da origem (0,0).')
eixoX = int(input('Informe a coordenada do eixo X: '))
eixoY = int(input('Informe as coodenadas do eixo Y: '))

distancia = math.sqrt((math.pow(eixoX,2)+(math.pow(eixoY,2))))

print(f'A distância entre a origem e as coordenadas é igual a {distancia:.2f}')

"""
52 - Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido pro-
porcionalmente ao valor que cada deu para a realização da aposta. Faça um programa
que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um
ganharia do prêmio com base no valor investido.
"""
"""
53 - Faça um programa para ler as dimensões de um terreno (comprimento c e largura l),
bem como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno
com tela.
"""