# Multiplos Operadores de Comparação

'''
Opção padrão

valor = int(input('Digite o Valor:'))

if valor >= 20 and valor < 40:
  print('Produto foi aceito')
else:
  print('Produto não aceito')


outra forma

if 20 <= valor < 40:
  print('Produto foi aceito')
else:
  print('Produto não aceito')


'''

#Forma Simplificada
valor = int(input('Digite o Valor:'))   

resultado = 'Produto foi Aceito' if 20 <= valor < 40 else 'Produto não Aceito'
print(resultado)