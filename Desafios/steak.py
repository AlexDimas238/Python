# Desafio com if, elif, else

# criar um programa que ao solicitar a temperatura, informe o ponto da carne

'''
  # minha resposta

temperatura = int(input('Informe a temperatura da carne: '))

if temperatura < 48:
    print('Cozinhe por mais alguns minutos')
elif temperatura >= 48 and temperatura < 54:
    print('Selada')
elif temperatura >= 54 and temperatura < 60:
    print('Ao Ponto para Mal')
elif temperatura >= 60 and temperatura < 65:
    print('Ao Ponto')
elif temperatura >= 65 and temperatura < 71:
    print('Ao Ponto para o bem')
else:
    print('A carne está bem passada')

'''

temperatura = int(input('Informe a temperatura da carne: '))

if temperatura < 48:
    print('Cozinhe por mais alguns minutos')
elif temperatura in range(48, 53):
    print('Selada')
elif temperatura in range(54, 59):
    print('Ao Ponto para Mal')
elif temperatura in range(60, 64):
    print('Ao Ponto')
elif temperatura in range(65, 71):
    print('Ao Ponto para o bem')
else:
    print('A carne está bem passada')