# == Nested Loop
 # outer Loop (Loop de Fora)
    # Inner Loop (Loop de dentro)

linhas = 6
colunas = 8
simbolo = '#'

for x in range(linhas):
    for y in range(colunas):
        print(simbolo, end='')
    print()