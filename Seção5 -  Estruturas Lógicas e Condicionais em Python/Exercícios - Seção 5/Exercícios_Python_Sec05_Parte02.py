import math
"""
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

print('12- Ler um número inteiro. Se o número lido for negativo, escreva a mensagem --Número'
      'inválido--. Se o número for positivo, calcular o logaritmo deste numero.')

numex12 = int(input('Informe um número inteiro: '))

if numex12 < 0:
    print('Número invalido')
else:
    logaritimo = math.log10(numex12)
    print(f'O logaritimo do número {numex12} é {logaritimo:.2f}')

print('Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e '
      'a segunda prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno '
      'e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou'
      'superior a 60 pontos.')
nota1_ex13 = float(input('Informe a primeira nota: '))
nota2_ex13 = float(input('Informe a segunda nota: '))
nota3_ex13 = float(input('Informe a terceira nota: '))

peso_nota01 = 1
peso_nota02 = 1
peso_nota03 = 2

media_ponderada = ((nota1_ex13*peso_nota01) + (nota2_ex13*peso_nota02) + (nota3_ex13*peso_nota03))/ (peso_nota01 + peso_nota02 + peso_nota03)

print(f'a média ponderada das notas {nota1_ex13,nota2_ex13,nota3_ex13} é igual a {media_ponderada} ')

if media_ponderada <=6:
    print('Reprovado!')
else:
    print('Aprovado!')

14- A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo
de O até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral
e a um exame final. A média das três notas mencionadas anteriormente obedece aos
pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo
com o resultado, mostre na tela se o aluno está reprovado (média entre O e 2,9), de
recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias.

nota_laboratorio = float(input('informe a nota do tirada no trabalho do laboratõrio: '))
peso_nota_laboratõrio = nota_laboratorio*2

nota_avaliacao_semestral = float(input('Informe a nota tirada na avaliação semestral: : '))
peso_nota_semestral = nota_avaliacao_semestral* 3

nota_exame_final = float(input('Informe a nota tirada no exame final: '))
peso_nota_final = nota_exame_final*5

nota_final_semestral = (peso_nota_laboratõrio + peso_nota_semestral + peso_nota_final) / 10



print(f'a nota final do aluno é {nota_final_semestral}')

if nota_final_semestral <= 2.9:
    print('Reprovado!')
elif nota_final_semestral >= 3 and nota_exame_final <=4.9:
    print('Recuperação')
else:
    print('Aprovado!')
"""

"""
15- Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia
da semana correspondente a este numero. Isto é, domingo se 1, segunda-feira se 2, e
assim por diante.
"""
dia = int(input("informe um número de 1 a 7 para descobror o dia da semana: "))

match dia:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda-Feira')
    case 3:
        print('Terça-Feira')
    case 4:
        print('Quarta-Feira')
    case 5:
        print('Quinta-Feira')
    case 6:
        print('Sexta-Feira')
    case 7:
        print('Sabado')
    case _:
        print('Não é um dia da semana!')


"""
16- Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês
correspondente a este numero. Isto é, janeiro se 1, fevereiro se 2, e assim por diante.
"""
"""
17- Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
A = ((basemaior + basemenor) + altura) / 2

Lembre-se a base maior e a base menor devem ser números maiores que zero.
"""
