"""
Estruturas condicionais
if (se) - Indica início de uma condicional
else(se não) - Indica uma inversão a condicional if,
elif(Se não se) - validação de condições entre o início e o fim das validações
"""

idade = 26

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print('Mostar a carteira de identidade')
else:
    print('Maior de idade')
