from datetime import datetime

# Python Object-Oriented Programming
    # Classes
    # Utilizadas para criar Objetos (Instances)
    # Objetos são partes dentro de uma class (instancias)
    # Classes são utilizadas para agrupar dados e funções, podendo reutilizar
    #=======
    # Class: Frutas
    # Objects: Abacate, Banana...

    # Construtores


# Criar a classe
class Funcionarios:
    def __init__(self, nome, sobrenome, ano_nascimento):
        self.nome = nome
        self.sobrenome = sobrenome
        self.ano_nascimento = ano_nascimento

    def nome_completo(self):
        return self.nome + ' ' + self.sobrenome

    def idade_funcionario(self):
        ano_atual = datetime.now().year
        self.ano_nascimento = int(ano_atual - self.ano_nascimento)
        return self.ano_nascimento

   
# Criar o Objeto(usuário) e passar os parâmetros
usuario1 = Funcionarios('Elena', 'Cabral', 2009)
usuario2 = Funcionarios('Karol', 'Silva', 2000)
usuario3 = Funcionarios('Dimas', 'Reis', 1988)

# 3 formas de imprimir os dados
print(usuario1.nome)
print(usuario3.nome_completo())
print(Funcionarios.nome_completo(usuario2))

print(Funcionarios.idade_funcionario(usuario2))
