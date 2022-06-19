"""
Escopo de variável

Dois caso de escopo

1 -  Variáveis Globais
    - Variáveis globais são reconhecidas em qualquer lugar do programa

2 - Variáveis Locais
    - Variaveis Locais são reconhecidas apenas no bloco ande forma declaradas, ou seja, seu escopo está limitado ao
    bloco onde foi declarada

Para declarar variaveis em Python fazemos

nome_da_variavel = valor_da_variavel

Python é uma linguagem de tipagem dinâmica. isso significa que ao declar uma variável, nos não colocamos o tipo de dado
dela.
Este tipo é inferido ao atribuirmos valor a mesma

Exemplo em C
int numero = 42

Exemplo em Java
int numero = 42
"""
numero = 42 # variavel global
print(numero)
print(type(numero))

numero = 'Palavra'
print(numero)
print(type(numero))


numero = 42
#novo = 0

if numero < 10:
    novo = numero + 10 # A variável 'novo' está declarado locamente dentro do bloco if.
    print(novo)

print(novo)