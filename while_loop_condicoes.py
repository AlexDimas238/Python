# == While Loops == 
# Publicar um produto com comissão de 10? se for acima de R$20

valor = int(input('Digite o valor do produto: '))

while valor > 20:
    valor = (valor * 0.1) + valor
    print(f'O Valor final com a comissão é R$ {valor} ')
    break