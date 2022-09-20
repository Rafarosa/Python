
print('41 - Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas.'
      'trabalhadas no mês. Imprima o valor a ser pago ao funcionário, adicionando 10% sobre'
      'o valor calculado.')

valorHora = float(input('Informe o valor da Hora trabalhada em reais (R$):'))
nHorasTrabalho = int(input('Informe a quantidade de horas trabalhadas no mês: '))
valorPago = valorHora * nHorasTrabalho
vAdicional = valorPago + (valorPago * 0.10)

print(f'O valor a ser pago é de R${valorPago:.2f}, com o adicional de 10%, o valor será {vAdicional:.2f}')
"""
42 - Receba o salário-base de um funcionário. Calcule e imprima o salário a receber, sabendo-
se que esse funcionário tem uma gratificação de 5% sobre o salário-base. Além disso,
ele paga 7% de imposto sobre o salário-base.
"""
"""
43 - Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:

• ototal a pagar com desconto de 10%;
• o valor de cada parcela, no parcelamento de 3x sem juros;
• a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com desconto)
• a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""
"""
44 - Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar
subindo a escada. Calcule e mostre quantos degraus o usuário deverá subir para atingir
seu objetivo.
"""
"""
45 - Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela
ASCII para resolver o problema.
"""
"""
46 -Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:

limeroLido = 123
NúmeroGerado = 32
"""
"""
47 - Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.
"""
"""
48 - Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""
"""
49 - Faça um programa para leia o horário (hora, minuto e segundo) de início e a duração, em
segundos, de uma experiência biológica. O programa deve resultar com o novo horário
(hora, minuto e segundo) do termino da mesma.
"""
"""
50 - Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de
sua idade e do ano atual,
"""