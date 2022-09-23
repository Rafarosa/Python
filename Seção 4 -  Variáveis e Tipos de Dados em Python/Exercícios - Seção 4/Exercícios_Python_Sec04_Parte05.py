print('41 - Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas.'
      'trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre'
      'o valor calculado.')

valorHora = float(input('Informe o valor da Hora trabalhada em reais (R$):'))
nHorasTrabalho = int(input('Informe a quantidade de horas trabalhadas no mês: '))
valorPago = valorHora * nHorasTrabalho
vAdicional = valorPago + (valorPago * 0.10)

print(f'O valor a ser pago é de R${valorPago:.2f}, com o adicional de 10%, o valor será {vAdicional:.2f}')


print('42 - Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-'
      'se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso,'
      'ele paga 7% de imposto sobre o salário-base.')

salarioBase = float(input('Informe o salario base do funcionário (R$): '))
salarioGrati = salarioBase * 0.05
impostoSalario = salarioBase * 0.07
salarioLiquido = (salarioBase + salarioGrati) - impostoSalario

print(f' - Salário base do funcionário é de R${salarioBase:.2f}\n'
      f' - Gratificação do funcionário é de R${salarioGrati:.2f}\n'
      f' - Imposto sobre o salário Base é de R${impostoSalario:.2f}\n'
      f' - Salario Líquido é de R$ {salarioLiquido:.2f}')

print('43 - Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:'
      '• O total a pagar com desconto de 10%;'
      '• O valor de cada parcela, no parcelamento de 3x sem juros;'
      '• A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)'
      '• A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)')

valorTotal = float(input('Informe o valor total do protudo\serviço a ser vendido: R$'))
vDescont10 = valorTotal - (valorTotal * 0.10)
vParcela3 = valorTotal / 3
comissaoVista = valorTotal * 0.05
comissaoParcela = valorTotal * 0.05

print(f'O total a pagar com desconto de 10%: R${vDescont10:.2f}\n'
      f'O valor de cada parcela, no parcelamento de 3x sem juros: R${vParcela3:.2f}\n'
      f'A comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto): R${comissaoVista}\n'
      f'A comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total): R${comissaoParcela:.2f}')

print('44 - Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar'
      'subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir'
      'seu objetivo.')
alturaDegrau = float(input('Informe a altura do degrau em milimetros: '))
alturaAlcancar = float(input('Informe a altura a qual deseja alcançar em metros:'))

quantidadeDegraus = alturaAlcancar / (alturaDegrau/1000)
print('Aqui usaremos a NR-31 - definição de 200mm de espaço entre degraus ')
print(f'Para atingir a altura de {alturaAlcancar:.2f}m, é necessario subir {quantidadeDegraus:.2f}')

print('45 - Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela'
      'ASCII para resolver o problema.')

letra = str(input('Informe uma letra maiúscula para ser convertida em minuscula: '))
print(f'Convertendo a letra {letra} fica {letra.lower()}')

print('46 -Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).'
      'Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:'
      'limeroLido = 123'
      'NúmeroGerado = 321')

numeral3Digitos = int(input('Informe um número para ser invertido: '))
numeral3Digitos = str(numeral3Digitos)
print(f'O valor invertido é: {numeral3Digitos[::-1]}')

print('47 - Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.')
numeral4Digitos = int(input('Informe um número interio de 4 digitos: '))
numeral4Digitos = str(numeral4Digitos)

print(f'{numeral4Digitos[0]}\n{numeral4Digitos[1]}\n{numeral4Digitos[2]}\n{numeral4Digitos[3]}\n')


print('48 - Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.')
segundos = float(input('Informe o valor interio em segundos para saber horas,minutos e segundos: '))
minutos = segundos / 60
horas = minutos / 60

print(f'{segundos} segundos, equivalem a {minutos:.2f} minutos, e a {horas:.2f} horas')


print('50 - Implemente um programa que calcule o ano de nascimento de uma pessoa apartir de sua idade e do ano atual')
ano =  2022
idade = int(input('Informe sua idade: '))

print(f'Você nasceu em {ano - idade}')