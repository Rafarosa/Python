# Desafio operadores Lógicos

# Os trabalhos
trabalho_terca = True
trabalho_quinta = True

if trabalho_terca and trabalho_quinta == True:
    print('Confirmado a compra de uma TV 50" e ir tomar sorvete')
elif trabalho_terca != trabalho_quinta:
    print('Confirmado a compra de uma TV 32" e ir tomar sorvete')
else:
    print('ficar em casa')


# Resposta do desafio conforme o curso

tv_50 = trabalho_terca and trabalho_quinta
sorvete = trabalho_terca or trabalho_quinta
tv_32 = trabalho_terca != trabalho_quinta
mais_saudavel = not sorvete

print('TV50={} TV32={} Sorvete={} Saudável={}'.format(
    tv_50, tv_32, sorvete, mais_saudavel))

