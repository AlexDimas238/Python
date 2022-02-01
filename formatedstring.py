#Utilizando Formated String

name = "Alex"
sobrenome = 'santos'
profissao = 'Programador'

texto = 'O ' + name + ' ' + sobrenome + ' é um ' + '['+ profissao + ']'

# Com Formated String
texto2 = f'O {name} {sobrenome} é um excelente [{profissao}]'

print(texto)
print(texto2)