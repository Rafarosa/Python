"""
11. Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h
(quilômetros por hora). A fórmula de conversão é: K = M * 3.6, sendo K a velocidade
em km/h e M em m/s

12. Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de
conversão é: K = 1,61 * M, sendo K a distância em quilômetros e M em milhas.

13. Leia uma distância em quilômetros é apresente-a convertida em milhas. A fórmula de
conversão é: M = K/1,61, sendo K a distância em quilômetros e M em milhas.

14. Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão
é: R= G * Pi/180, sendo G o ângulo em graus e R em radianos e Pi = 3.14.

15. Leia um ângulo em radianos e apresente-o convertido em graus. A fórmula de conversão
é:G = R * 180/Pi, sendo G o ângulo em graus e R em radianos e Pi = 3.14.

16. Leia um valor de comprimento em polegadas e apresente-o convertido em centimetros.
A fórmula de conversão é: C = P * 2,54, sendo C o comprimento em centímetros e P o
comprimento em polegadas.

17. Leia um valor de comprimento em centimetros e apresente-o convertido em polegadas.
A fórmula de conversão é: P = C/2,54, sendo C o comprimento em centímetros e P o
comprimento em polegadas.

18. Leia um valor de volume em metros cúbicos m³ e apresente-o convertido em litros. A fórmula de conversão é: L = 1000 * M, sendo L o volume em litros e M o volume em metros cúbicos.

19. Leia um valor de volume em litros e apresente-o convertido em metros cúbicos m³. A
fórmula de conversão é: M = L/1000, sendo L o volume em litros e M o volume em metros cúbicos.

20. Leia um valor de massa em quilogramas é apresente-o convertido em libras. A fórmula de conversão é: L = K/0,45, sendo K a massa em quilogramas e L a massa em libras.

"""

"""
print(
    "1. Leia uma velocidade em m/s (metros por segundo) e apresente-a convertida em km/h (quilômetros por hora). A fórmula de conversão é: K = M * 3.6, sendo K a velocidade em km/h e M em m/s")

m = float(input('Por favor, informe a velociada em m/s: '))

k = m * 3.6

print(f'A veliocidade {m}m/s em Km/h é {k:.2f}Km/h')
"""
"""
print('12. Leia uma distância em milhas e apresente-a convertida em quilômetros. A fórmula de conversão é: K = 1,61 * M, sendo K a distância em quilômetros e M em milhas.')

mi = float(input('Por gentileza, informe a distância em milhas: '))

km = 1.61 * mi

print(f'A distância {mi} Milhas é igua a {km:.2f} Km')
"""
"""
print('13. Leia uma distância em quilômetros é apresente-a convertida em milhas. A fórmula de conversão é: M = K/1,61, sendo K a distância em quilômetros e M em milhas.')

km2 = float(input('Por gentileza informe a distância em quilômetros: '))

mi2 = km2/1.61

print(f'A distância {km2} Km é igua a {mi2:.2f} milhas')
"""
print('14. Leia um ângulo em graus e apresente-o convertido em radianos. A fórmula de conversão é: R= G * Pi/180, sendo G o ângulo em graus e R em radianos e Pi = 3.14.')

g1 = float(input('Por favor, informe o ângulo em graus para conversão:'))

r1 = (g1 * 3.14)/180

print(f'{g1} Graus é igual a {r1} Radianos')