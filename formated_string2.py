#Utilizando Formated String

name = str(input('Digite Seu Primeiro Nome: '))
sobrenome = str(input('Digite seu Sobrenome: '))
profissao = str(input('Digite a Sua Profissão: '))

# Sem Formated String
texto = 'O ' + name + ' ' + sobrenome + ' é um ' + '['+ profissao + ']'

# Com Formated String
texto2 = f'O {name} {sobrenome} é um excelente {profissao}'

print(texto)
print(texto2)