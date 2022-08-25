# Funções dentro de Listas
    # Manipulando Listas

cidades = ['Rio de Janeiro', 'São Paulo', 'Salvador', 'Curitiba']
#               0                  1            2           3

# Selecionando somente o index desejado
print(cidades[2])

# Alterando o valor de um index especifico
cidades[1]= 'Vitória'

# Funções add no final da lista
#cidades.append('Santa Catarina')

# Função remover item da lista
#cidades.remove('Rio de Janeiro')

#Inserir item em posição especifica
#cidades.insert(0, 'Porto Alegre')

# Organizar lista em ordem alfabetica
cidades.sort()

print(cidades)