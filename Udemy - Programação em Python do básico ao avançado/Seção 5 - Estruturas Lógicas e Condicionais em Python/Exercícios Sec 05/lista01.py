""" 
1. Faça um programa que receba dois números e mostre qual deles é o maior.
"""
num01 = float(input('Informe o primeiro número:'))
num02 = float(input('Informe o segundo número:'))
if num01 < num02:
   print(f'o número {num02} é maior que {num01}')
else:
   print(f'o número {num01} é maior que {num02}')

""" 
2. Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
"""
num03 = float(input('Informe um número:'))
 
if num03 > 0:
    raiz_quadrada = num03**1/2
    print(f'o número {num03} é positivo e sua Raiz quadrada é {raiz_quadrada}')
else:
    print('Número inválido')


""" 
3. Leia um numero real. Se o número for positivo imprima a raiz quadrada. Do contrário, imprima o numero ao quadrado.

"""
num04 = float(input('Informe um número: '))
 
if num04 > 0:
    raiz_quadrada = num04**1/2
    print(f'o número {num04} é positivo e sua Raiz quadrada é {raiz_quadrada}')
else:
    quadrado = num04**2
    print(f'o número {num04} é negativo e elevado ao quadrado é {quadrado}')

""" 
4. Faça um programa que leia um número e, caso ele seja positivo, calcule e mostre:
- O número digitado ao quadrado
- A raiz quadrada do número digitado
"""
num05 = float(input('Informe um número:'))

if num05 > 0:
    raiz_quadrada = num05**1/2
    quadrado = num05**2
    print(f'o número {num05} tem sua Raiz quadrada é {raiz_quadrada}')
    print(f'o número {num05} ao quadrado é {quadrado}')
else:
    print('Número inválido')

"""
5. Faça um programa que receba um número inteiro e verifique se este número é par ou impar. 
"""
num06 = float(input('Informe um número para validar se ele é par ou impar:'))

if num06 % 2 == 0:
  print('O número é para!')
else:
  print('O número é impara!')

""" 
6. Escreva um programa que, dados dois números inteiros, mostre na tela o maior deles, assim como a diferença existente entre ambos.
"""
num07 = int(input('Informe o primeiro número: '))
num08 = int(input('Informe o segundo número: '))

if num07 > num08:
    diferenca1 = num07 - num08
    print(f'O maior número é {num07} e a diferença entre eles é {diferenca1}')
else:
    diferenca2 = num08 - num07
    print(f'O maior número é {num08} e a diferença entre eles é {diferenca2}')

""" 
7. Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois números forem iguais, imprima a mensagem Números iguais.
"""
num09 = float(input('Informe o primeiro número: '))
num10 = float(input('Informe o segundo número: '))

if num09 == num10:
    print(f'Números iguais')
elif num09 > num10:
    print(f'{num09} é o maior ')
else:
    print(f'{num10} é o maior ')

""" 
8. Faça um programa que leia 2 notas de um aluno, verifique se as notas são válidas e exiba na tela a média destas notas. Uma nota válida deve ser, obrigatoriamente, um valor entre 0.0 e 10.0, onde caso a nota não possua um valor válido, este fato deve ser informado ao usuário e o programa termina.
"""
nota01 = float(input('Informe a primeira nota: '))
nota02 = float(input('Informe a segunda nota: '))

if nota01 >0 and nota02 >0 and nota01 <=10 and nota02 <=10:
    media = nota01 + nota02 / 2
    print (f'A média do aluno é: {media}')
else:
    print('Notas inválisas')


""" 
9. Leia o salário de um trabalhador e o valor da prestação de um empréstimo. Se a prestação for maior que 20% do salário imprima: Empréstimo não concedido, caso contrário imprima: Empréstimo concedido.
"""  
salario = float(input('Informe o seu salário: '))
prestacao = float(input('Informe o valor da prestação: '))

if prestacao <= salario*0.2:
    print('Emprestimo aprovado!')
else:
    print('Emprestimo negado!')

""" 
10. Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal, utilizando as seguintes fórmulas (onde h corresponde à altura):
- Homens: (72.7 h) - 58
- Mulheres: (62,1 h) - 44,7
"""
altura = float(input('Informe sua altura(m): '))
sexo = str(input('Informe o seu sexo (M|F): '))

if sexo == 'M':
    peso_ideal_M = (72.7*altura) - 58
    print(f'Seu peso ideal é {peso_ideal_M:.2f}')
elif sexo == 'F':
    peso_ideal_F = (62.1*altura) - 44.7
    print(f'Seu peso ideal é {peso_ideal_F:.2f}')
else:
    print('Valor inválido!')