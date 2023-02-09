"""
Saindo do loop com break

Funciona da mesma maneira que nas linguagens C ou Java

Utilizamos o break para sair de look de forma planejada

"""
# Exemplo 01

for numero01 in range(1,10):
    if numero01 == 6:
        break
    else:
        print(numero01)
print('Sair do loop')

# Exemplo 02

while True:
    comando = input("Informe 'Sair' para sair do loop: ")
    if comando == 'sair':
        break