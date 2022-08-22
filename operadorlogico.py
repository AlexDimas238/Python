velocidade = input('Qual a sua velocidade ? ')
velocidade = int(velocidade)

if velocidade >50 and velocidade < 80:
    print('Você esta no limite de velocidade ')  
elif velocidade < 50:
    print('Aumente a velocidade')
else:
    print('Você esta acima da velocidade permitida.')