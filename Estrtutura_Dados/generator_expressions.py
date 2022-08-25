# Generator Expressions
    # Uma forma mais rapida para Listas, dicionários e etc
    # Menos memória alocada
    # Valores em bytes

#importar a função para verificar consumo de memória

from sys import getsizeof

numeros = [x * 10 for x in range(10)]
print(type(numeros))
print(numeros)
print(getsizeof(numeros))

print('====================================')

numeros = (x * 10 for x in range(10))
print(type(numeros))
print(list(numeros))
print(getsizeof(numeros))