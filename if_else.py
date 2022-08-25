''''
idade = input('Digite a sua Idade: ')
idade = int(idade)
permitido = ('Você pode votar')
nao_permitido = ('Você não pode Votar')


Forma Lógica padrão

if idade >= 16:
  print(permitido)
else:
  print(nao_permitido)

'''
#Mesma lógica em 1 linha

idade = input('Digite a sua Idade: ')
idade = int(idade)

resultado = 'Voto Permitido' if idade >= 16 else 'Voto não Permitido'

print(resultado)
