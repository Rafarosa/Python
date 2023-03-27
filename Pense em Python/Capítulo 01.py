"""  
A jornada do programador

Capítulo inicial de do livro pense em python.
Neste capítulo é mostrdo o que é um programa identifcado como uma sequência de instruções que especifca como executar uma operação de computador.
tendo a oprincipal característica entrada de dados, saída de dados, execução de operações matemáticas, condicionais e repetição.

Verificado o primeiro programa em linguagem python (print('Hello World')).

Mostra também os conceitos de operação aritimética (+ - * / ** )

valores e tipos basicos (int, float, string,)

Aspectos das lingagens formais e naturais 

Depuração, como essa função está relacionada as atividade de desenvolvimento de software



# Exercise 01

1 - Em uma instrução print, o que ocorre se você omitir um dos parenteses ou ambos

#print 'olá')
#
#Resposta para exclusão dos dois parenteses da insturção print.
#
#[Running] python -u "c:\Users\rafae\Dev\Python\Pense em Python\Capítulo 01.py"
#  File "c:\Users\rafae\Dev\Python\Pense em Python\Cap�tulo 01.py", line 23
#    print 'ol�'
#    ^^^^^^^^^^^^
#SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
#
#removendo um dos parentese
#
#[Running] python -u "c:\Users\rafae\Dev\Python\Pense em Python\Capítulo 01.py"
#  File "c:\Users\rafae\Dev\Python\Pense em Python\Cap�tulo 01.py", line 23
#    print 'ol�')
#               ^
#SyntaxError: unmatched ')'

2- Em uma instrução print, o que acontece se omitir uma das aspas ou ambas?

print('Olá')

Será apresentado uma mensagem de erro Syntax
Semelhante a esta

[Running] python -u "c:\Users\rafae\Dev\Python\Pense em Python\Capítulo 01.py"
  File "c:\Users\rafae\Dev\Python\Pense em Python\Cap�tulo 01.py", line 22
    print('Ol�)
          ^
SyntaxError: unterminated string literal (detected at line 22)

remoendo as duas aspas 

[Done] exited with code=1 in 0.048 seconds

[Running] python -u "c:\Users\rafae\Dev\Python\Pense em Python\Capítulo 01.py"
  File "c:\Users\rafae\Dev\Python\Pense em Python\Cap�tulo 01.py", line 34
       ^
SyntaxError: (unicode error) 'unicodeescape' codec can't decode bytes in position 97-98: truncated \UXXXXXXXX escape

3 -  Você pode usar um sinal de menos para fazer uma número negativo como -2.
     o que acontece se puser um sinal de mais antes de uma núemro?
     E se escrever assim: 2++2?

Resposta
Será mostrado o algarismo no valor 2 positivo 

>>>
 +2
2

2++2 será mostrado a soma dos dois algarismos 
2++2
4

4 - Na notação matemática, zero à esquerda são aceitáveis , com em 02.
    O que acontece se você entar usar isso no python

Resposta:
Será informado que essa notação não é permiotida para valores decimais e deveraá ser usado como octal

File "<stdin>", line 1
    02
    ^
SyntaxError: leading zeros in decimal integer literals are not permitted; use an 0o prefix for octal integers
    

5 - o que acontece se você tiver dois valores sem nenhum operador entre eles?

Resposta:

Será exibido os dois valores
"""