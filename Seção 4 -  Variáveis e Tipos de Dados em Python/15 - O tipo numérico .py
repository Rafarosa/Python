"""
Tipo Numérico
"""

"""
Python 3 possui três tipos de números embutidos: int, float e
complex.

Int - Inteiros são virtualmente ilimitados [3] e podem crescer até o limite da
memória. Números inteiros são escritos normalmente como em sua forma literal
(por exemplo, 100) e também podem ser gerados usando a função int()
como em int(‘1’), no qual geramos o número inteiro 1 a partir de uma
string.

float - Outro tipo muito conhecido de números é o ponto flutuante, chamado
de float. Em Python, no interpretador padrão CPython, os floats
são implementados usando o tipo double. Números de ponto flutuante têm o caractere . – como em 2.5
–, para separar as casas decimais. Também podem ser gerados pela função
float() – como em float(1) ou float(‘2.5’) –, e são aceitas na função
float() as strings nan e inf com prefixos opcionais + e - – por exemplo,
float(‘+nan’).

complex - Os números complexos também estão embutidos na linguagem, mas sua
aplicação não é tão comum no dia a dia. Eles têm a parte imaginária e a real,
sendo que cada uma delas é um float. Os números complexos, por exemplo,
dão resposta como a raiz quadrada de um número negativo e são usados
em domínios como engenharia elétrica, estatística etc. Os números complexos têm o sufixo j ou J, como
em 1+2J. Para acessar a parte real e a parte imaginária, use 1+2j.real
ou 1+2j.imag.

"""
print('Exemplos\n')

inteiro = int(1)
print(f'Esse é um número inteiro{inteiro}')

flutuante = float(-33.566)
print(f'Esses são números de pnto flutuante{flutuante}')

complexo = complex (1+2j)
print(f'Esses é um número complexo{complexo}\n')

"""
Operadores Aritiméticos 

Adição = x + y
Subtração = x - y 
Divisão em ponto flutuante = x / y 
Divisão descartando parte fracionária = x// y 
Multiplicação = x * y
Resto = x % y 
Negação = -x
Potência = x**y
"""
x = int(3)
y = int(6)

adicao = x+y
subtracao = x-y
divisao_float = x/y
divisao_s_float = x//y
multiplicacao = x*y
resto = x % y
negacao = -x

print(f'Operadores Aritiméticos\nAdiçào -> {x} + {y} = {adicao},\nSubtração -> {x} - {y} = {subtracao}\n'
      f'Divisão em ponto flutuante = {x} / {y} = {divisao_float}\n'
      f'Divisão descartando parte fracionária = {x} // {y} = {divisao_s_float}\n'
      f'Multiplicação = {x} * {y} = {multiplicacao}\n'
      f'Resto = {x} % {y} = {resto}\n'
      f'Negação = -{x}')
