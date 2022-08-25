# Listas
    #Armazenar mais de uma informação em variaveis
    # Manter a sequencia dos dados em uma variavel

cor_cliente = input("Digite a cor desejada: ")
cores = ['amarelo', 'verde', 'azul']

#utuliza o lower() para colocar tudo que for digitado em letras minusculas.

if cor_cliente.lower() in cores:
    print("Em estoque")
else:
    print('Não temos esta cor no estoque')