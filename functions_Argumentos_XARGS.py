# Functions
    # DRY - Don't Repeat Yourself
    # Vários Argumentos (Xargs)
# Criar uma função que soma vários números

def soma(*numeros):
    resultado = 0
    for num in numeros:
        resultado += num
    return resultado

x = soma(2,3,4,7,9)

print(x)
