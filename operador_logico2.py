# Operadores Lógicos

from ast import Or


renda_acima_5mil = False
nome_limpo = True

if renda_acima_5mil or nome_limpo:
    print('Financiamento Aprovado')
else:
    print('Financiamento Negado')    