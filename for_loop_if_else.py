# Enviar um e-mail com os detalhes da compra online (maximo 3 tentativas para compras confirmadas)

# Utilizando o BREAK para o loop em caso de confirmação do loop

compra_confirmada = False
dados_compra = 'Compra no Valor de $ realizada e entrega confirmada '

for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print('Detalhes enviados para o seu e-mail')
        break
else:
    print('Compra não comfirmada')