# Erros
    # Excelente para testes
    # Não realiza o 'Stop' no programa
    # Mensagens customizadas quando encontra um erro

# Criei uma lista com index de 0 a 2 porém solicitei o index 3 que não existe

try:
    letras = ['a', 'b', 'c']
    print(letras[3])
except IndexError:
    print('Index não existe')