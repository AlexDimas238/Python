# usando o While Loop
# Criar uma promoção para um produto de R$100
# Mudando o valor do produto a cada dia não ficando abaixo de R$ 20

valor = 100
dia = 0

while valor > 20:
    dia += 1
    print(f' No dia {dia} o produto vai ser vendido por R$ {valor}')
    valor -= 15