"""
Estruturas lógicas:
And (e)
or (ou)
not (não)
is (é)

Operadores unários
    - not, is
Operadores binários
    - and, or
Regra de funcionamento
Para o 'and', ambas as condições precisam ser verdadeiras para ser verdadeira(True)
"""
ativo = True
logado = True

if ativo and logado:
    print('Bem-vindo ao sistema!')
else:
    print('Você precisa ativar sua conta. Por favor, verifique seu e-mail')

"""
para o 'or', uma das condições precisam ser verdadeiras para ser verdadeira(True)
"""

if ativo and logado:
    print('Bem-vindo ao sistema!')
else:
    print('Você precisa ativar sua conta. Por favor, verifique seu e-mail')

"""
para o 'not', o valor do booleano é invertido, ou seja, True vira False, se False vira True
"""
if not ativo:
    print('Você deve ativar sua conta, instrução no seu e-mail')
else:
    print('Bem-vindo!')

"""
Para o 'is' é necessario fazer uma comparação entre valores
"""
print(ativo is True)