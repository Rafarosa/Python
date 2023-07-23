""" 
11. Escreva um programa que leia um número inteiro maior do que zero e devolva, na tela, a soma de todos os seus algarismos. Por exemplo, ao número 251 corresponderá o valor 8 (2+5+1). Se o número lido não for maior do que zero, o programa terminará com a mensagem "Número inválido".
"""
def soma_algarismos(numero):
    soma = 0
    for algarismo in str(numero):
        soma += int(algarismo)
    return soma

numero = int(input("Digite um número inteiro maior do que zero: "))

if numero > 0:
    resultado = soma_algarismos(numero)
    print(f"A soma dos algarismos do número {numero} é {resultado}.")
else:
    print("Número inválido.")

""" 
12. Ler um número inteiro. Se o número lido for negativo, escreva a mensagem "Número inválido". Se o número for positivo, calcular o logaritmo desse número.
"""
def calculo_logaritimo(num12):
  loga = math.log(num12)
  return loga

num12 = int(input('Informe um número interio:'))
if num12 > 0:
  positivo = calculo_logaritimo(num12)
  print(f'O Logaritimo de {num12} é igual a {positivo}')
else:
  print('Número inválido')
 
""" 
13. Faça um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.
"""

nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

peso1 = 1
peso2 = 1
peso3 = 2

nota_minima = 60

media = (nota1 * peso1 + nota2 * peso2 + nota3 * peso3) / (peso1 + peso2 + peso3)

if media >= nota_minima:
    print("Aluno aprovado. Média:", media)
else:
    print("Aluno reprovado. Média:", media)

""" 
14. A nota final de um estudante é calculada a partir de três notas atribuídas entre o intervalo de 0 até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 4,9) ou se foi aprovado. Faça todas as verificações necessárias. 
"""
peso_lab = 2
peso_semestre = 3
peso_final = 5

trabalho_laboratorio = float(input('Informe a nota do trabalho: '))
avaliacao_semestral = float(input('informe a nota da avaliação semestral: '))
exame_final = float(input('Informe a nota do exame final: '))

somatoria_notas = (trabalho_laboratorio * peso_lab)+(avaliacao_semestral * peso_semestre) +(exame_final *peso_final)
print (somatoria_notas)
somatoria_peso = peso_lab + peso_semestre + peso_final
print(somatoria_peso)
nota_final = somatoria_notas/somatoria_peso
print(nota_final)

if nota_final <= 2.9:
  print(f'Sua nota é {nota_final}, infelizmente foi reprovado!')
elif nota_final >=3 and nota_final <= 4.9:
  print(f'Sua nota é {nota_final}, infelizmente você está de recuperação!')
else:
  print(f'Parabéns! sua nota é {nota_final}, você foi Aporvado ')

""" 
15. Usando switch, escreva um programa que leia um inteiro entre 1 e 7 e imprima o dia da semana correspondente a este número. Isto é, domingo se 1, segunda-feira se 2, e assim por diante.
"""
dia_da_semana = int(input('informe um número de 1 a 7 e descubra o dia da semana:'))
match dia_da_semana:
  case 1:
    print('Domingo!')
  case 2:
    print('Segunda!')
  case 3:
    print('Terça!')
  case 4:
    print('Quarta!')
  case 5:
    print('Quinta!')
  case 6:
    print('Sexta!')
  case 7:
    print('Sabado!')
  

""" 
16. Usando switch, escreva um programa que leia um inteiro entre 1 e 12 e imprima o mês correspondente a este número. Isto é, janeiro se 1, fevereiro se 2, e assim por diante. 

mes_do_ano = int(input('informe um valor de 1 a 12 e descubra o mês do Ano'))
"""
match mes_do_ano:
  case 1:
    print('Janeiro!')
  case 2:
    print('Fevereiro!')
  case 3:
    print('Março!')
  case 4:
    print('Abril!')
  case 5:
    print('Maio!')
  case 6:
    print('Junho!')
  case 7:
    print('Julho!')
  case 8:
    print('Agosto!')
  case 9:
    print('Setembro!')
  case 10:
    print('Outubro!')
  case 11:
    print('Novembro!')
  case 12:
    print('Dezembro!')
  case _ :
    print('Número inválido!')
 
""" 
17. Faça um programa que calcule e mostre a área de um trapézio. Sabe-se que:
A= (basemaior + basemenor) * Altura / 2
Lembre-se que a base maior e a base menor devem ser números maiores que zero.
"""
base_maior = float(input('Informe a base maior do trapézio: '))
base_menor = float(input('informe a base menor do trapézio: '))
altura = float(input('informe a altura do trapézio: '))

if base_menor > 0 and base_maior > 0:
      area = ((base_maior + base_menor) * altura)/2
      print(f'A área do trapézio é {area}')
else:
  print('Dados inválidos')