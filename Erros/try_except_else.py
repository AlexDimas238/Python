# Erros
    # Excelente para testes
    # Não realiza o 'Stop' no programa
    # Mensagens customizadas quando encontra um erro

try:
    valor = int(input('Digite o valor do seu produto: '))
    print(valor)
except ValueError:
    print(' Favor digitar um valor em numeros')
finally:
    print('Pode ter erro ou acerto, mesmo assim vou executar')

# else:
#    print('O usuario digitou um valor correto')

