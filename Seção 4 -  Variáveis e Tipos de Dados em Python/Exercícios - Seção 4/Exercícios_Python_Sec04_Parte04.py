import math

print('35 - Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = √a² + b². '
      'Faça um programa que receba os valores de a e b e calcule  o valor da hipotenusa através da equação. Imprima o '
      'resultado dessa operação.')

a1 = float(input('Informe o cateto A do triângulo: '))
b1 = float(input("Informe o Cateto B do Triangulo: "))

hipot = math.sqrt((math.pow(a1, 2) + math.pow(b1, 2)))

print(f'a Hipotenusa deste triangulo é {hipot:.2f}')

"""
36 - Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. O volume
de um cilindro circular é calculado por meio da seguinte fórmula: V = Pi * raio² * altura,
onde Pi = 3.141592.
"""

"""
37 - Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo
em vista que o desconto foi de 12%
"""
"""
38 - Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que
ele recebeu um aumento de 25%.
"""
"""
39 - A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso.
Sendo que da quantia total:

• O primeiro ganhador receberá 46%;

• O segundo receberá 32%;

• Oterceiro receberá o restante;

 Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""
"""
40 - Uma empresa contrata um encanador a R$30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser
paga, sabendo-se que são descontados 8% para imposto de renda.
"""
