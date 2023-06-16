""" 
21. Leia um valor de massa em libras e apresente-o convertido em quilogramas. 
A fórmula de conversão é: K = L * 0.45, sendo K a massa em quilogramas e L a massa em libras. 
"""
libras = float(input('Informe o valor em Libras: '))

converter_quilogramas = libras*0.45

print(f'{libras}lb é igual a {converter_quilogramas}Kg')

"""
22. Leia um valor de comprimento em jardas e apresente-o convertido em metros. 
A fórmula de conversão é: M = 0.91 * J, sendo J o comprimento em jardas e M o comprimento em metros.
"""
jardas = float(input('Informe o comprimento em Jardas(yd): '))

converte_jardas_metros = jardas * 0.91

print(f'{jardas}yd é igual a {converte_jardas_metros}m')

"""
23. Leia um valor de comprimento em metros e apresente-o convertido em jardas. 
A fórmula de conversão é: J = M/0.91 , sendo J o comprimento em jardas e M o comprimento em metros.
"""
metros = float(input('Informe o comprimento em metros(m): '))

converto_metros_jardas = metros/0.91

print(f'{metros}m é igual a {converto_metros_jardas:.2f}yd')

"""
24. Leia um valor de área em metros quadrados m² e apresente-o convertido em acres. 
A fórmula de conversão é: A = M * 0,000247, sendo M a área em metros quadrados e A a área em acres.
"""
metros_quadados = float(input('Informe a area em m²: '))

converte_acres = metros_quadados*0.000247

print(f'{metros_quadados}m² é igual a {converte_acres:.6f} acres')

"""
25. Leia um valor de área em acres e apresente-o convertido em metros quadrados m². 
A fórmula de conversão é: M = A * 4048.58, sendo M a área em metros quadrados e A a área em acres.
"""
acres = float(input('Informe o valor em Acres: '))

converte_metros_quadrados = acres*4048.48

print(f'{acres} acres é igual a {converte_metros_quadrados}m²')

"""
26. Leia um valor de área em metros quadrados m² e apresente-o convertido em hectares. 
A fórmula de conversão é: H = M * 0.0001, sendo M a área em metros quadrados e H a área em hectares.
"""
metros_quadrados = float(input('Informe a área em m²: '))

converte_hectares = metros_quadrados*0.0001

print(f'{metros_quadrados}m² é igual a {converte_hectares}')

"""
27. Leia um valor de área em hectares e apresente-o convertido em metros quadrados m2. 
A fórmula de conversão é: M = H * 10000, sendo M a área em metros quadrados e H a área em hectares.
"""
hectarar = float(input('Informe a área em hectares(ha): '))

converte_metrosquadrados2 = hectarar*10000

print(f'{hectarar}ha é igual a {converte_metrosquadrados2}m²')

"""
28. Faça a leitura de três valores e apresente como resultado a soma dos quadrados dos três valores lidos.
"""
valor_um = float(input('informe o primeiro valor: '))
valor_dois = float(input('informe o segundo valor: '))
valor_tres = float(input('informe o Terceiro valor: '))

soma_dos_quadrados = valor_um**2 + valor_dois**2 + valor_tres**2

print(
    f' A soma dos quadados dos valores {valor_um},{valor_dois} e {valor_tres} é igual a {soma_dos_quadrados}')


"""
29. Leia quatro notas, calcule a média aritmética e imprima o resultado.
"""
nota_um = float(input('Informe a primeira nota:'))
nota_dois = float(input('Informe a segunda nota:'))
nota_tres = float(input('Informe a terceira nota:'))
nota_quatro = float(input('Informe a quarta nota:'))

media_aritimética = (nota_um+nota_dois+nota_tres+nota_quatro)/4

print(f'A média aritimética das notas {nota_um},{nota_dois},{nota_tres} e {nota_quatro} é {media_aritimética}')

"""
30. Leia um valor em real e a cotação do dólar. Em seguida, imprima o valor correspondente em dólares.
"""
brl_moeda = float(input('Informe o valor da moeda Reais(R$): '))
us_moeda = float(input('Informe a contação do dolar hoje(em reais):'))

valor_dolar = brl_moeda/us_moeda

print(f'O valor em dolar de {brl_moeda} R$, é {valor_dolar:.2f}USS$ ')
