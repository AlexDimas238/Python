# Desafio com Funções
    # Criar um programa que calcula a quantidade de latas necessárias para pintar uma parede

rendimento = int(input('Qual é o rendimento da lata?  '))
altura = int(input('Qual é a Altura da parede?   '))
largura = int(input('Qual é a Largura da parede?   '))

def calculo_latas():
    latas = (altura * largura) / rendimento
    print(f'Você precisa de {latas} latas de tinta')

calculo_latas()