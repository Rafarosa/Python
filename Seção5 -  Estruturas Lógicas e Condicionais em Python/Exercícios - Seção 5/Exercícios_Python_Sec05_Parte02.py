import math

print('11- Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a'
      'soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor'
      '8 (2 + 5 + 1). Se o número lido não for maior do que zero, o programa terminará com a '
      'mensagem --Número inválido --.')

numex11 = int(input('Informe um número para ser mostrado a soma do seu algarismos: '))

if numex11 >= 0:
    num = str(numex11)
    lista = list(map(int, num.strip()))
    print(sum(lista))

else:
    print('--Número inválido --')

"""
12- Ler um número inteiro. Se o número lido for negativo, escreva a mensagem --Número
inválido--. Se o número for positivo, calcular o logaritmo deste numero.
"""
"""
13- Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e
a segunda prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno
e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou
superior a 60 pontos.
"""
"""
14- A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo
de O até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral
e a um exame final. A média das três notas mencionadas anteriormente obedece aos
pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo
com o resultado, mostre na tela se o aluno está reprovado (média entre O e 2,9), de
recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias.
"""
"""
15- Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
da semana correspondente a este numero. Isto é, domingo se 1, segunda-feira se 2, e
assim por diante.
"""
"""
16- Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês
correspondente a este numero. Isto é, janeiro se 1, fevereiro se 2, e assim por diante.
"""
"""
17- Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
A = ((basemaior + basemenor) + altura) / 2

Lembre-se a base maior e a base menor devem ser números maiores que zero.
"""
