# Erros
    # Excelente para testes
    # Não realiza o 'Stop' no programa
    # Mensagens customizadas quando encontra um erro


try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print(' Favor digitar um valor em numeros')