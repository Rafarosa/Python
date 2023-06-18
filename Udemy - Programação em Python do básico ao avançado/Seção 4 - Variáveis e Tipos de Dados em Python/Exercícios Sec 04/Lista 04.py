"""
31. Leia um número inteiro e imprima o seu antecessor e o seu sucessor.
32. Leia um número inteiro e imprima a soma do sucessor de seu triplo com o antecessor de seu dobro.
"""
num_int_01 = int(input('Informe um número inteiro: '))

antecessor = num_int_01 - 1
sucessor = num_int_01 + 1

print(
    f' O númerio antecessor de {num_int_01} é {antecessor}, e o sucessor {sucessor}')

soma_triplo_dobro = (num_int_01*3 + 1)+(num_int_01*2 - 1)

print(
    f'soma do sucessor de seu triplo com o antecessor de seu dobro {soma_triplo_dobro}')


"""
33. Leia o tamanho do lado de um quadrado e imprima como resultado a sua área. 
"""
lado_quadrado = float(input('Informe o tamanho do lado do quadrado: '))

area_quadrado = lado_quadrado**2

print(f'A área do quadrado é {area_quadrado} medidas quandadas')

"""
34. Leia o valor do raio de um círculo e calcule e imprima a área do círculo correspondente. A área do circulo é π * raio², considere π =  3.141592

raio = float(input('informe o raio da circulo: '))
"""
area_circulo = 3.141592 * raio**2

print(f'A a área do circulo é {area_circulo:.4f} medidas quadradas')

"""
35. Sejam a e b os catetos de um triângulo, onde a hipotenusa é obtida pela equação: hipotenusa = √a²+b². 
Faça um programa que receba os valores de a e b e calcule o valor da hipotenusa através da equação. Imprima o resultado dessa operação.
"""
cateto_oposto = float(input('Informe o cateto oposto: '))
cateto_adjacente = float(input('Informe o cateto adjacente: '))

hipotenua = (cateto_oposto**2 + cateto_adjacente**2)**(1/2)

print(f'A hipotenusa do trinangulo é {hipotenua:.2f}')

"""
36. Leia a altura e o raio de um cilindro circular e imprima o volume do cilindro. 
O volume de um cilindro circular é calculado por meio da seguinte fórmula: V = π * raio², onde = 3.141592.
"""
altura_cilindro = float(input('Informe a altura do cilindor: '))
raio_cilindro = float(input('informe o raio do cilindro: '))

volume_cilindro = 3.141592 * (raio_cilindro)**2 * altura_cilindro

print(f'O volume do cilindor é {volume_cilindro:.3f} medicas cúbicas')

"""
37. Faça um programa que leia o valor de um produto e imprima o valor com desconto, tendo em vista que o desconto foi de 12%
"""
valor_produto = float(input('Informe o valor do produto(R$): '))

preco_venda = valor_produto-(valor_produto*0.12)

print(f'O valor de venda foi de R${preco_venda}')

"""
38. Leia o salário de um funcionário. Calcule e imprima o valor do novo salário, sabendo que ele recebeu um aumento de 25%.
"""
salario_atual = float(input('Informe seu salário(R$):'))

novo_salario = salario_atual + (salario_atual*0.25)

print(f'Seu novo salário é R${novo_salario}')


"""
39. A importância de R$ 780.000,00 será dividida entre três ganhadores de um concurso. Sendo que da quantia total:
• O primeiro ganhador receberá 46%;
• O segundo receberá 32%;
• O terceiro receberá o restante;

Calcule e imprima a quantia ganha por cada um dos ganhadores.
"""
premio = 780000

ganhador_01 = premio*0.46
ganhador_02 = premio*0.32
ganhador_03 = premio - (ganhador_01 + ganhador_02)

print(f'A divisão do premio de R${premio} ficará da segunte forma: \n,'
      'Primeiro ganhador recebará R$ {ganhador_01} \n' 
      'Segundo ganhador recebará R$ {ganhador_02} \n' 
      'Terceiro ganhador recebará R$ {ganhador_03}'
      )

"""
40. Uma empresa contrata um encanador a R$ 30,00 por dia. Faça um programa que solicite
o número de dias trabalhados pelo encanador e imprima a quantia líquida que deverá ser paga, sabendo-se que são descontados 8% para imposto de renda.
"""
valor_diaria = 30

dias_trabalhados = int(
    input('Informe a quantidade de dias trabalhasdos pelo encanador: '))

valor_pago = valor_diaria * dias_trabalhados
valor_pago_liquido = valor_pago-(valor_pago*0.08)

print(f'O valor pago ao encanador é de R${valor_pago_liquido}')
