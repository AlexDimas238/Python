# importar de outro arquivo
# se utilizar o import ele vai carregar todas as funções do outro arquivo, pode carrregar a memória

   # import funcoes

   # funcoes.somar()


# se utilizar o 'from arquivo import função' vai selecionar somente a funcao escolhida

from  funcoes import somar, multi

# importar o Packet (tem que criar o arquivo '__init__.py') 
from itens.cadastro import cliente


somar()
multi()

cliente()