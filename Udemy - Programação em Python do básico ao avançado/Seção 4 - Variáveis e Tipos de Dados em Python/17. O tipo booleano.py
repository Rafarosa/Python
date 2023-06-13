""" 
Tipo Booleano

Algebra Booleana

2 constantes, verdadeiro ou falso

 SEMPRE com inicial em maiúscula
True -> verdadeiro
False -> falso

"""

ativo = True
logado = False
print(ativo)

""" 
Operação Negação (not)

Fazer negação, se o valor booleano for verdadeiro, o resultado será falso.
Se o valor booleano for falso, o resultado será verdadeiro

"""
print(not ativo)

""" 
Operações binárias
Tabela verdade
Or (ou)

Ou um ou outro deve ser verdadeiro para a condição ser verdadeira

"""
print(
    True or True,
    True or False,
    False or False,
    False or True
)
# Exemplo
# Usuário logado no sistema

print('Usuario logado no sistema:',ativo or logado)

""" 
Operação AND(e)

Ambas as condiçãoes devem ser verdadeiras para que o retorno seja verdadeiro

"""
print(
    True and True,
    True and False,
    False and False,
    False and True
)

