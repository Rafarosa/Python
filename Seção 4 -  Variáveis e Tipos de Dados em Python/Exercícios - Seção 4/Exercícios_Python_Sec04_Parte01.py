"""
01 - Faça um programa que leia um número inteiro e o imprima.
"""
"""
print('01 - Faça um programa que leia um número inteiro e o imprima.')
num1 = int(input('Por gentileza informe um número interio:'))
print(f'O número informado foi: {num1}\n ')

"""

"""
02 - Faça um programa que leia um número real e o imprima.
"""
"""
print('02 - Faça um programa que leia um número real e o imprima.')
num2 = float(input("Por gentileza, informe um número real(ex: 2,44 ou -34,6): "))
print(f'O número informado foi: {num2}\n ')
"""

"""
03 - Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
"""
"""
print('03 - Peça ao usuário para digitar três valores inteiros e imprima a soma deles.')
num3a = int(input('Por gentilez, informe o primeiro número inteiro: '))
num3b = int(input('Agora, informe o segundo número inteiro: '))
num3c = int(input('Por fim, informe o terceiro número: '))
snum3 = num3a + num3b + num3c

print(f'A soma dos números {num3a},{num3b} e {num3c} é: {snum3}')
"""


"""
04 - Leia um número real e imprima o resultado do quadrado desse número.
"""
"""
print('04 - Leia um número real e imprima o resultado do quadrado desse número.')
num4 = float(input('Por gentileza, informe um número para verificar o seu quadado:'))
num4quad = num4**2

print(f'O valor do número {num4} elevado ao quadrado é {num4quad:.2f}')
"""


"""
05 - Leia um número real e imprima a quinta parte deste número.
"""
"""
print('05 - Leia um número real e imprima a quinta parte deste número.')
num5 = float(input('Informe um número para saber qual é a sua quinta parte: '))
num5div5 = num5/5
print(f'A quinta parte do número {num5} é: {num5div5:.2f}')
"""


"""
06 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.
Afórmula de conversão é: F = C*(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit
e C a temperatura em Celsius.
"""
"""
print('06 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit.')
cel = float(input('Informe a tempreratua em graus Celsius para saber sua equivalência em Fahrenheit: '))

fah = cel*(9.0/5.0) + 32.0

print(f'A temperatura {cel}ºC ficará {fah:.2f} ºF')
"""

"""
07 - Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.
A fórmula de conversão é: C = 5.0*(F — 32.0)/9.0, sendo C a temperatura em Celsius
e F a temperatura em Fahrenheit.
"""
"""
print('07 - Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius.')

fah = float(input('Informe a tempreratua em graus Fahrenheit para saber sua equivalência em Celsius: '))

cel = 5.0 * (fah - 32.0) / 9.0

print(f'A temperatura {fah}ºF ficará {cel:.2f} ºC')
"""
"""
08 - Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. A
fórmula de conversão é: C = K — 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.
"""
"""
print('08 - Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius.')
kel = float(input('Informe a tempreratua em graus Kelvin para saber sua equivalência em Celsius: '))

cel = kel - 273.15

print(f'A temperatura {cel}ºC ficará {kel:.2f}ºK')
"""
"""
09 - Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. A
fórmula de conversão é: K = C + 273.15, sendo C a temperatura em Celsius e K a
temperatura em Kelvin.
"""

"""
10 - Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s
(metros por segundo). A fórmula de conversão é: M — K/3.6, sendo K a velocidade em
km/h e M em m/s
"""