import math

print('51 - Escreva um programa que leia as coordenadas x e y de pontos no R² e calcule sua distância da origem (0,0).')
eixoX = int(input('Informe a coordenada do eixo X: '))
eixoY = int(input('Informe as coodenadas do eixo Y: '))

distancia = math.sqrt((math.pow(eixoX,2)+(math.pow(eixoY,2))))

print(f'A distância entre a origem e as coordenadas é igual a {distancia:.2f}')


print('52 - Três amigos jogaram na loteria. Caso eles ganhem, o prêmio deve ser repartido pro-'
      'porcionalmente ao valor que cada deu para a realização da aposta. Faça um programa'
      'que leia quanto cada apostador investiu, o valor do prêmio, e imprima quanto cada um'
      'ganharia do prêmio com base no valor investido.')

valorPremio = float(input('Informe o valor do prêmio:R$ '))
invest01 = float(input('Informe a porcentagem que o apostador 01 investiu: '))
invest02 = float(input('Informe a porcentagem que o apostador 02 investiu: '))
invest03 = 100 - (invest01 + invest02)
print(f'Consequentemente, o apostador 03 investiu {invest03}%')

premio01 = valorPremio * (invest01/100)
premio02 = valorPremio * (invest02/100)
premio03 = valorPremio * (invest03/100)

print(f'Cada um recenerá {premio01:.2f}, {premio02:.2f} e {premio03:.2f} respectivamente ')


print('53 - Faça um programa para ler as dimensões de um terreno (comprimento c e largura l),'
      'bem como o preço do metro de tela p. Imprima o custo para cercar este mesmo terreno'
      'com tela.')
cTerreno = float(input('informe o comprimento do terreno em metros: '))
lTerreno = float(input('informe o largura do terreno em metros: '))
pTela = float(input('Informe o valor do metro da tela:R$ '))
perimeter = (2 * cTerreno) + (2 * lTerreno)
vTotal = perimeter * pTela

print(f'O custo para cobrir o perimetro de {perimeter:.2f}m é R${vTotal:.2f}')
