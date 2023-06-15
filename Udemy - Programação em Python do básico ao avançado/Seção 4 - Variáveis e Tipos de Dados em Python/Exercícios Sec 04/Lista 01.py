""" 
1. Faça um programa que leia um número inteiro e o imprima.
"""
ler_numero = int(input('Informe um número: '))

print(f'O número informado é {ler_numero}')

"""
2. Faça um programa que leia um número real e o imprima.
"""
ler_numero_real = float(input('Informe um número real: '))

print(f'O número real informado é {ler_numero_real}')

"""
3. Peça ao usuário para digitar três valores inteiros e imprima a soma deles.
"""
ler_numero_1 = int(input('Informe o primeiro número: '))
ler_numero_2 = int(input('Informe o segundo número: '))
ler_numero_3 = int(input('Informe o terceiro número: '))

soma_numeros = ler_numero_1 + ler_numero_2 + ler_numero_3

print(f'A soma dos números {ler_numero_1},{ler_numero_2} e {ler_numero_3} é igual a {soma_numeros}')

"""
4. Leia um número real e imprima o resultado do quadrado desse número.
"""

ler_num_real = float(input('Informe um número real: '))

numero_quadrado = ler_num_real**2

print(f'O quadrado do número {ler_num_real} é {numero_quadrado}')

"""
5. Leia um número real e imprima a quinta parte deste número.
"""
num = float(input("Digite um número real: "))

quinta = num / 5

print(f'A quinta parte do numero{num} é {quinta}')
"""
6. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Fahrenheit. 
A fórmula de conversão é: F= C*(9.0/5.0)+32.0, sendo F a temperatura em Fahrenheit e C a temperatura em Celsius.
"""
graus_celsius = float(input('Informe a temperatura em graus Celsius: '))

conversor_fahrenheit = graus_celsius*(9.0/5.0)+32.0

print(f'{graus_celsius}º graus Celsius em Fahrenheit, é equivalente a {conversor_fahrenheit}ºF')

"""
7. Leia uma temperatura em graus Fahrenheit e apresente-a convertida em graus Celsius. 
A fórmula de conversão é: C= 5.0(F-32.0)/9.0, sendo C a temperatura em Celsius e F a temperatura em Fahrenheit.
"""
graus_fahrenheit = float(input('Informe a temperatura em graus Fahrenheit:'))

conversor_celsius = 5.0*(graus_fahrenheit-32.0)/9.0

print(f'{graus_fahrenheit}º graus Fahrenheit em Celsius, é equivalente a {conversor_celsius}')

"""
8. Leia uma temperatura em graus Kelvin e apresente-a convertida em graus Celsius. 
A fórmula de conversão é: C= K - 273.15, sendo C a temperatura em Celsius e Ka temperatura em Kelvin.
"""
graus_kelvin = float(input('Informe a temperatura em graus Kelvin: '))

conversor_kelvin_celsius = graus_kelvin - 273.15

print(f'{graus_kelvin}º graus Kelvin em Celsius, é equivalente a {conversor_kelvin_celsius}ºC')

"""
9. Leia uma temperatura em graus Celsius e apresente-a convertida em graus Kelvin. 
A fórmula de conversão é: K = C + 273.15, sendo C a temperatura em Celsius e K a temperatura em Kelvin.
"""
graus_celsius_2 = float(input('Informe a temperatura em graus Celscios: '))

conversor_celsius_kelvin = graus_celsius_2 + 273.15

print(f'{graus_celsius_2}º graus Celsius em kelvin, é equivalente a {conversor_celsius_kelvin}ºK')

"""
10. Leia uma velocidade em km/h (quilômetros por hora) e apresente-a convertida em m/s.
(metros por segundo). A fórmula de conversão é: M = K/3.6, sendo K a velocidade em km/h e M em m/s.
"""
velocidade_kmh = float(input('Informe a sua velocidade em Km/h:'))

converte_ms =  velocidade_kmh/3.6

print(f'A velocidade de {velocidade_kmh}Km/h é igual a {converte_ms:.2f}m/s')