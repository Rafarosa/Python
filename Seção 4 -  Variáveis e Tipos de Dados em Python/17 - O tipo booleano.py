"""
Tipo Booleano

Algebra booleana

2 constante, verdadeiro ou falso
True - verdadeiro
False - Falso

Obs: sempre com a inicial maiúscula

errado
true, false

correto
True, False
"""

ativo = False
logado = True

print(ativo)

"""
Operação basica
"""

# Negação (Not):
"""
Fazendo a negação, se o valor booleano for verdadeiro o resultado será falso
se o valor booleano for falso o resultado será verdadeiro
"""
print(f'Tabela verdade: Operação NOT\n Negação de Verdadeiro: {not True}\n Negação de Falso {not False}\n')

# Ou (or)
"""
É uma operação binária, ou seja, depende dos dois valores. Ou um ou outro deve ser verdadeiro para a aperação ser 
verdadeira 
se ambas as condições formem falsa, o resultado será falso
"""
print(f'Tabela verdade: Operação OR\n Verdade ou Verdade: {True or True} \n Verdadeiro ou Falso: {True or False}\n '
      f'Falso ou Verdadeiro: {False or True}\n Falso ou Falso: {False or False}')

# E (and)
"""
É uma operação, também binária, ou seja, depende dos dois valores. Ambos deve ser verdadeiros para a aperação ser 
verdadeira 
se condição for falsa, o resultado será falso

"""
print(f'\nTabela verdade: Operação AND\n Verdade e Verdade: {True and True} \n Verdadeiro e Falso: {True and False}\n '
      f'Falso e Verdadeiro: {False and True}\n Falso e Falso: {False and False}')
