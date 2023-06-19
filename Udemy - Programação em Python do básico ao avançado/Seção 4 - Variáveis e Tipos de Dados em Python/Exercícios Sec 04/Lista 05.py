""" 
41. Faça um programa que leia o valor da hora de trabalho (em reais) e número de horas trabalhadas no mês.
    Imprima o valor a ser pago ao funcionário, adicionando 10% sobre o valor calculado.
"""
valor_hora = float(input('Informe o valor da hora trabalhada em R$:'))
quantidade_horas = int(input('Informe a quantidade de horas trabalhadas no mês: '))

valor_bruto = valor_hora*quantidade_horas
valor_pago = valor_bruto+(valor_bruto*0.1)

print(f'O valor bruto a ser pago é de {valor_bruto}, com o adicional de 10%, será pago {valor_pago}')

"""
42. Receba o salário-base de um funcionário.
Calcule e imprima o salário a receber, sabendo-se que esse funcionário tem uma gratificação de 5% sobre o salário-base.
Além disso, ele paga 7% de imposto sobre o salário-base.
"""
salario_base = float(input('informe o salário base(R$): '))
gratificacao = salario_base * 0.05
imposto = salario_base * 0.07
salario_receber = salario_base + gratificacao - imposto

print(f'Salario base do funcionário é R${salario_base}\n'
      f'Sua gratificação é de R${gratificacao}\n'
      f'Imposta a ser pago é R${imposto}\n'
      f'Sendo assim, o salario a receber é de R${salario_receber}\n')

"""
43. Escreva um programa de ajuda para vendedores. A partir de um valor total lido, mostre:
• o total a pagar com desconto de 10%;
• o valor de cada parcela, no parcelamento de 3x sem juros;
• a comissão do vendedor, no caso da venda ser a vista (5% sobre o valor com des- conto)
• a comissão do vendedor, no caso da venda ser parcelada (5% sobre o valor total)
"""
valor_venda = float(input('Informe o valor da venda(R$): '))

valor_com_desconto =  valor_venda - (valor_venda*0.1)
parcelamento_3x = valor_venda / 3

comissao_avista_5 = valor_com_desconto * 0.05

comissao_parcela_5 =  valor_venda * 0.05

print(f'O valor a ser pago com desconto de 10% é R${valor_com_desconto}\n'
      f'O valor de cada parcela, se a venda for de 3x ficará R${parcelamento_3x:.2f}\n'
      f'A sua comissão será de R${comissao_avista_5} se a venda for a vista\n'
      f'A sua comissão será de R${comissao_parcela_5}')


"""
44. Receba a altura do degrau de uma escada e a altura que o usuário deseja alcançar subindo a escada.
    Calcule e mostre quantos degraus o usuário deverá subir para atingir seu objetivo.
"""
altura_degrau = float(input('Informe a altura do degrau da sua escada em metros: '))
altura_alvo = float(input('Informe a altura que deseja chegar em metros: '))

quantidade_degraus = altura_alvo // altura_degrau + 1

print(f'Voce deverá subir {quantidade_degraus} para atingir a altura de {altura_alvo}metros')


"""
45. Faça um programa para converter uma letra maiúscula em letra minúscula. Use a tabela ASCII para resolver o problema.
"""
# Método sem função
letra_maiuscula = str(input('Informe uma letra maiúscula para converter em minuscula: '))

valor_ascii_maiusculo = ord(letra_maiuscula)
print(f'valor em ASCII para o caracter maiúsculo é: {valor_ascii_maiusculo}')

valor_ascii_minusculo = valor_ascii_maiusculo + 32
print(f'valor em ASCII para o caracter maiúsculo é: {valor_ascii_minusculo}')

converter_para_letra = chr(valor_ascii_minusculo)
print(f'convertendo a letra: {converter_para_letra}')

# Método com função
converter_com_metodo = letra_maiuscula.lower()
print(f'Utilizando a forma mais simples, usando .lower(), fica {converter_com_metodo}')

"""
46. Faça um programa que leia um número inteiro positivo de três dígitos (de 100 a 999).
    Gere outro número formado pelos dígitos invertidos do número lido. Exemplo:
    NúmeroLido = 123 NúmeroGerado = 321.
"""
numero_interio_3 = int(input('Informe um número interio de 3 digitos: '))
numero_interio_3 = str(numero_interio_3)

inverter_ordem = numero_interio_3[::-1]
inverter_ordem= int(inverter_ordem)
print(inverter_ordem)


"""
47. Leia um número inteiro de 4 dígitos (de 1000 a 9999) e imprima 1 dígito por linha.
"""
numero_intero_4 = int(input('informe um numero inteiro de 1000 a 9999: '))
numero_intero_4_str = str(numero_intero_4)

print(numero_intero_4_str[0], '\n', numero_intero_4_str[1], '\n', numero_intero_4_str[2], '\n', numero_intero_4_str[3],
      '\n')

"""
48. Leia um valor inteiro em segundos, e imprima-o em horas, minutos e segundos.
"""
segundos = int(input('Informe o tempo em segundos:'))

converte_horas = segundos // 3600
converte_minutos = (segundos - (converte_horas * 3600)) //60
converte_segundos = (segundos % 60)

print(f'{converte_horas}:{converte_minutos}:{converte_segundos}')


"""
49. Faça um programa para leia o horário (hora, minuto e segundo) de inicio e a duração, em segundos, 
de uma experiência biológica. O programa deve resultar com o novo horário (hora, minuto e segundo) do termino da mesma.

50. Implemente um programa que calcule o ano de nascimento de uma pessoa a partir de sua idade e do ano atual.

"""
