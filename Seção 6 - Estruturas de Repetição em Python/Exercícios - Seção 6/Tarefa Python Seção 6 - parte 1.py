"""
1. Faça um programa que determine o mostre os cinco primeiros múltiplos de 3, conside-
rando números maiores que 0.
"""
# for multplo3 in range(1, 6):
#    print(f'o {multplo3}º multiplo de 3 é {multplo3 * 3}')
"""
2. Escreva um programa que escreva na tela, de 1 até 100, de 1 em 1, 2 vezes. A primeira
Vez deve usar a estrutura de repetição for, a segunda while.
"""
# for numeros in range(1, 101):
#    print(f'Número do for {numeros}')
#
#numeroswhile = 1
# while numeroswhile <= 100:
#    print(f'Números do While {numeroswhile}')
#    numeroswhile += 1

"""
3. Faça um algoritmo utilizando o comando while que mostra uma contagem regressiva
na tela, iniciando em 10 e terminando em 0O. Mostrar uma mensagem “FIM!" após a
contagem.
"""
#contagem = 10
#
# while contagem >= 0:
#    print(f'Contando... {contagem}')
#    contagem -= 1
# print('Fim')
"""
4. Escreva um programa que declare um inteiro, inicialize-o com 0, e incremente-o de 1000
em 1000, imprimindo seu valor na tela, até que seu valor seja 100000 (cem mil).
"""
#num4 = 0
#
# while True:
#    num4 += 1000
#    if num4 > 100000:
#        break
#    else:
#        print(num4)
"""
5. Faça um programa que peça ao usuário para digitar 10 valores e some-os.
"""
#num51 = 0
# for i in range(10):
#    num5 = int(input('informe um numero para ser somado:'))
#    num51 = num51 + num5
# print(num51)
"""
6. Faça um programa que leia 10 inteiros e imprima sua média.
"""
#num61 = 0
#quantidade = 10
# for i in range(quantidade):
#    num6 = int(input(f'Informe {i+1}º número intero para saber a média deles: '))
#    num61 = num61 + num6
#media = num61/quantidade
#print(f"A média dos números informado é {media}")
"""
7. Faça um programa que leia 10 inteiros positivos, ignorando não positivos, e imprima sua
média.
"""
num71 = 0
quantidade7 = 10
for i in range(quantidade7):
    num7 = int(input(f'Informe o {i+1}º número para saber a média: '))
    if num7 >= 0:
        num71 = num71 + num7
    else:
        print(f'O número {num7} não será somado para a sua média')
media7 = num71/10
print(f"Sua média é {media7}")
"""
8. Escreva um programa que leia 10 números e escreva o menor valor lido e o maior valor
lido.
"""
nummenor
"""
9. Faça um programa que leia um número inteiro N e depois imprima os N primeiros
números naturais ímpares.
"""
"""
10. Faça um programa que calcule e mostre a soma dos 50 primeiros números pares.
"""
