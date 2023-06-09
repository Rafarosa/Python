import this

print(this)

"""
PEP 8 -Python Enhancement Proposal
São propostas de melhorias para a linguagem Python

a idéia do PEP é que possamos escrever códigos Python de forma Pythônica.
"""
"""
[1] -  Utilize Camel Case para nomes de classes;
"""


class Calculadora:
    pass


"""
[2] -  Utilize nomes em minúsculo, separados pro underline para funções ou variáveis 
"""


def soma():
    pass


class soma_dois():
    pass


""" 
[3] - Utilize 4 espaços para identação!
"""

if 'a' in 'banana':
    print('Tem')

"""
[4] - Linhas em branco
- Separar funções e definições de classe cm duas linhas em branco;
- Métodos dentro de uma classe deve ser separados com uma unica linha em branco
"""


class Class:
    pass


class clsass:
    pass

""" 
[5] -  Imports

- Imports deve sempre ser feitos em linhas Separadas

Errado
import sys, os

Certo
import Sys
import os

- Não há problema em utilizar:
from types import StringType, ListTyps

- Caso tenha muitos imports de um mesmo pacote, recomendamos fazer:

from types import (
    Stringtype,
    ListTipe,
    SetType,
    OutroType
)

- Imports devem ser colocados no topo do topo do arquivo, logo depois de qualquer comentário ou docstring
- Antes de constantes ou variáveis globais

[6] - Espaços em expressões e instruções 
"""
# Não faça
fucao( algo[ 1 ], { outro: 2 })
dict ['chave'] = lsita [ indice]

# Faça
funcao(algo[1], {outro: 2})
dict['chave'] = lsita[indice]

""" 
[7] - termine uma instrução sempre com uma nova linha
"""

# The Zen of Python, by Tim Peters
#
# Beautiful is better than ugly.
# Explicit is better than implicit.
# Simple is better than complex.
# Complex is better than complicated.
# Flat is better than nested.
# Sparse is better than dense.
# Readability counts.
# Special cases aren't special enough to break the rules.
# Although practicality beats purity.
# Errors should never pass silently.
# Unless explicitly silenced.
# In the face of ambiguity, refuse the temptation to guess.
# There should be one-- and preferably only one --obvious way to do it.
# Although that way may not be obvious at first unless you're Dutch.
# Now is better than never.
# Although never is often better than *right* now.
# If the implementation is hard to explain, it's a bad idea.
# If the implementation is easy to explain, it may be a good idea.
# Namespaces are one honking great idea -- let's do more of those!
