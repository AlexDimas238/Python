# Functions 
    # DRY - Don't Repeat yourself
    # Realizam uma tarefa
    # Calcula e retorna um valor 

def cliente1(nome):
    print(f' Olá {nome}')

def cliente2(nome):
    return f'Olá {nome}'

x = cliente1('maria')
y = cliente2('José')    

print(y)