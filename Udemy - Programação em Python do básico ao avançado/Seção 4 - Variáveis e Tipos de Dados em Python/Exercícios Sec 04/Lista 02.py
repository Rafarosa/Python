"""
11. Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilômetros por hora). 
A fórmula de conversão é: K = M*3.6, sendo K a velocidade em km/h e M em m/s.
"""
metros_segundos1 = float(input('informe a velocidade em m/s: '))

converter_km1 = metros_segundos1*3.6

print(f'{metros_segundos1} m/s é igual a {converter_km1} Km/h')

"""
12. Leia uma distância em milhas e apresente-a convertida em quilômetros. 
A fórmula de conversão é: K = 1,61*M, sendo K a distância em quilômetros e M em milhas.
"""
milhas1 = float(input('Infome a distância em milhas: '))

converter_quilometros = 1.61*milhas1

print(f'{milhas1} mi é igaual a {converter_quilometros:.2f} km')

"""
13. Leia uma distância em quilômetros e apresente-a convertida em milhas. 
A fórmula de conversão é: M = K/1,61, sendo K a distância em quilômetros e M em milhas.
"""
quilometros1 = float(input('Informe a distância em quilômetros: '))

converter_milhas = quilometros1/1.61

print(f'{quilometros1}Km é igual a {converter_milhas:.2f} mi')

"""
14. Leia um ângulo em graus e apresente-o convertido em radianos. 
A fórmula de conversão é: R = G*π/180, sendo G o ângulo em graus e R em radianos e π = 3.14
"""
graus = float(input('Informe o ângulo em graus: '))

converte_radianos = graus*3.14/180

print(f'{graus} Graus é igual a {converte_radianos} radianos')

"""
15. Leia um ângulo em radianos e apresente-o convertido em graus. 
A fórmula de conversão é: G = R * 180/π, sendo G o ângulo em graus e R em radianos e π = 3.14.
"""
radianos = float(input('Infomre o ângulo em radianos: '))

converte_graus = radianos*180/3.14

print(f'{radianos} radianos é igual a {converte_graus:.2f} graus')

"""
16. Leia um valor de comprimento em polegadas e apresente-o convertido em centímetros. 
A fórmula de conversão é: C = P*2,54, sendo C o comprimento em centímetros e P o comprimento em polegadas.
"""
polegadas = float(input('Informe o valor em polegadas: '))

converte_centimetros = polegadas*2.54

print(f'{polegadas} pol é igual a {converte_centimetros}cm')

"""
17. Leia um valor de comprimento em centímetros e apresente-o convertido em polegadas. 
A fórmula de conversão é: P = C/2,64 sendo C o comprimento em centímetros e P o comprimento em polegadas.
"""
centimetros = float(input('Informe o valor em centimetros: '))

converte_polegadas = centimetros/2.64

print(f'{centimetros}cm é igual a {converte_polegadas:.2f}pol')

"""
18. Leia um valor de volume em metros cúbicos m3 e apresente-o convertido em litros. 
A fórmula de conversão é: L= 1000 * M, sendo L o volume em litros e M o volume em metros cúbicos.
"""
metros_cubicus = float(input('informe o valor em m³: '))

converte_litros = metros_cubicus*1000

print(f'{metros_cubicus}m³ é igual a {converte_litros}L')

"""
19. Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m3. 
A fórmula de conversão é: M = L/1000, sendo L o volume em litros e M o volume em metros cúbicos.
"""
litros = float(input('Informe o valor em litros: '))

converte_metros = litros/1000

print(f'{litros}L é igual a {converte_metros}m³')

"""
20. Leia um valor de massa em quilogramas e apresente-o convertido em libras. 
A fórmula de conversão é: L = K/0.45, sendo K a massa em quilogramas e L a massa em libras.
"""
quilogramas = float(input('Informe o peso em Kg: '))

converte_libras = quilogramas/0.45

print(f'{quilogramas}Kg é igual a {converte_libras:.2f}lb')
