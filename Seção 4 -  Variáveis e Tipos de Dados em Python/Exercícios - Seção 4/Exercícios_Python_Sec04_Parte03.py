

print('21 - Leia um valor de massa em libras e apresente-o convertido em quilogramas. A fórmula de conversão é: K = L * 0 45, sendo K a massa em quilogramas e L a massa em libras.')

l1 = float(input('Por gentileza, informe o valor em libras para saber o valor e quilos: '))

k1 = l1 * 0.45

print(f'{l1} Libras é igual a {k1:.2f} quilos')


print(
    '22 - Leia um valor de comprimento em jardas e apresente-o convertido em metros. A fórmula de conversão é: M = 0,91 * J, sendo J o comprimento em jardas e M o comprimento em metros.')

j1 = float(input('informe o valor em jardas para verificar seu valor em metros: '))

m1 = 0.91 * j1

print(f'{j1} Jardas é igual a {m1:.2f} metros')


print('23 - Leia um valor de comprimento em metros e apresente-o convertido em jardas. A fórmula de conversão é: J = M / 0,91, sendo J o comprimento em jardas e M o comprimento em metros.')

m2 = float(input('informe o valor em metros para verificar seu valor em jardas: '))

j2 = m2 / 0.91

print(f'{m2} Metros é igual a {j2:.2f} Jardas')

print('24 - Leia um valor de área em metros quadrados m² e apresente-o convertido em acres. A fórmula de conversão é: A = M * 0,000247, sendo M a área em metros quadrados e A a área em acres.')

mq1 = float(input('Informe o valor em m² para apresentar a sua conversão em Acres: '))

ac1 = mq1 * 0.000247

print(f'{mq1}m² é igual a {ac1:.4f}Acres')

print('25 - Leia um valor de área em acres e apresente-o convertido em metros quadrados m². A fórmula de conversão é: M = A * 4018,58 , sendo M a área em metros quadrados e A a área em acres.')

ac2 = float(input('Informe o valor em acres para apresentar a sua conversão em m²: '))

mq2 = ac2 * 4018.58

print(f"{ac2} Acres é igual a {mq2:.2f}M²")

print('26 - Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares. A fórmula de conversão é: H = M * 0,0001, sendo M a área em metros quadrados e H a área em hectares.')

mq3 = float(input('Informe o valor em M² para ser convertido em hectares: '))

h1 = mq3 * 0.0001

print(f'{mq3}m² é igual a {h1:.2f} hectares')

print('27 - Leia um valor de área em hectares e apresente-o convertido em metros quadrados m². A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H a área em hectares.')

mq3 = float(input('Informe o valor em Hectares para ser convertido em M²: '))

h2 = mq3 * 0.0001

print(f'{mq3}m² é igual a {h2:.2f} hectares')

print('28 - Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.')

valor01 = float(input('Informe o primeiro valor: '))
valor02 = float(input('Informe o segundo valor: '))
valor03 = float(input('Informe o terceiro valor: '))

valorTotal = valor01**2 + valor02**2 + valor03**2

print(f'{valor01}² + {valor02}² + {valor03}² é igual a {valorTotal}')


print('29 - Leia quatro notas, calcule a média aritmética e imprima o resultado.')

nota01 = float(input('Informe a primeira nota:'))
nota02 = float(input('Informe a segunda nota:'))
nota03 = float(input('Informe a terceira nota:'))
nota04 = float(input('Informe a quarta nota:'))

mediaFinal = (nota01+nota02+nota03+nota04)/4

print(f'Sua média final é {mediaFinal} pontos')

print('30 - Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.')

real1 = float(input('Informe o valor em Reais(BRL):'))
dolar1 = float(input('Informe o valor da cotação do dolar hoje:'))

reEmDolar = real1/dolar1

print(f'Você tem ${reEmDolar:.2f} com a cotação do dolar a ${dolar1}')
