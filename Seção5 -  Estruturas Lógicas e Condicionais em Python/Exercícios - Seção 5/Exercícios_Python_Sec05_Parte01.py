import math
"""
print("1- Faça um programa que receba dois números e mostre qual deles é o maior.")

numero01 = float(input('Informe um número: '))
numero02 = float(input('Informe outro número: '))

if numero01 > numero02:
    print(f'{numero01} é mairo que {numero02}')
else:
    print(f'{numero02} é mairo que {numero02}')
"""
"""
print("2- Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz"
      "quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o"
      "número é inválido.")

numex02 = float(input('Informe um número: '))

if numex02 > 0:
    print(f'O númro informado é {numex02} e sua raiz quadrada é {math.sqrt(numex02):.2f}')
else:
    print('Número inválido')
"""
"""
print('3- Leia um numero real. Se o número for positivo imprima a raiz quadrada. Do contrário,'
      'imprima o numero ao quadrado.')

numex03 = float(input('Informe um número real: '))

if numex03 > 0:
    print(f'O númro informado é {numex03} e sua raiz quadrada é {math.sqrt(numex03):.2f}')
else:
    print(f'O quadrado {numex03} é {math.pow(numex03,2)}')
"""
"""
print('4- Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:'
      '- O número digitado ao quadrado'
      '- A raiz quadrada do número digitado ')

numex04 = float(input('Informe um número: '))

if numex04 > 0:
    print(f'o número {numex04} elevado ao quadrado é igual a {math.pow(numex04,2)}')
    print(f'A raiz quadrada do número {numex04} é {math.sqrt(numex04):.2f}')
else:
    print('Número fora do escopo')
"""
"""
print('5- Faça um programa que receba um número inteiro e verifique se este número é par ou impar.')

numex05 = int(input('Informe um número: '))

if (numex05 % 2) >= 1:
    print(f'número {numex05} é impar')
else:
    print(f'número {numex05} é par ')
"""
"""
print('6- Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles,'
      'assim como a diferença existente entre ambos.')

num_a_ex06 = int(input('Informe o primeiro número interio: '))
num_b_ex06 = int(input('Informe o segundo número interio: '))

if num_a_ex06 > num_b_ex06:
    print(f'{num_a_ex06} é mairo que {num_b_ex06}, a diferença entre eles é de {num_a_ex06 - num_b_ex06} ')
else:
    print(f'{num_b_ex06} é mairo que {num_a_ex06}, a diferença entre eles é de {num_b_ex06 - num_a_ex06} ')
"""
"""
print('7- Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois'
      'números forem iguais, imprima a mensagem Números iguais.')

num_c_ex07 = int(input('Informe o primeiro número: '))
num_d_ex07 = int(input('Informe o primeiro número: '))

if num_c_ex07 > num_d_ex07:
    print(f'{num_c_ex07} é mairo que {num_d_ex07}')
elif num_c_ex07 < num_d_ex07:
    print(f'{num_d_ex07} é mairo que {num_c_ex07}')
else:
      print('Os números são iguais!!')
"""
"""
print('8- Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e'
      'exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um'
      'valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser'
      'informado ao usuário e o programa termina.')

nota1Ex08 = float(input('Informe a primeira nota do aluno:'))
nota2Ex08 = float(input('Informe a segunda nota do aluno:'))

if (nota1Ex08 > 0 and nota1Ex08 <=10) and (nota2Ex08 >0 and nota2Ex08 <=10):
      print(f'a média das notas é {(nota1Ex08 + nota2Ex08) / 2}')
else:
      print('Uma das notas não é válida')
"""

print('9- Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a'
      'prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso'
      'contrário imprima: Empréstimo concedido.')


salario = float(input('Informe o salário do trabalhador: '))
prestacao = float(input('informe o valor da prestação:'))

percentual = salario * 0.20

if prestacao <= percentual:
      print('Empréstimo concedido!!')
else:
      print('Empréstimo não concedido!!')

"""
10- Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu
peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):

 Homens: (72.7 * h) - 58
 Mulheres: (62.1 * h) -  44.7
"""