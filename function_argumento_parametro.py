# Functions - Criando Funções
# DRY - Don't repeat yourself
# DEF - Definition - defina a criação de uma function

def boas_vindas(nome, quantidade):
    print(f'Olá {nome}. ')
    print(f'Temos {str(quantidade)} de laptops em estoqque')


boas_vindas(input('Digite seu nome: '), 7)
    