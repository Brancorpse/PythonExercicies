# adicionando funções

# funções são pequenos códigos usados para funções específicas
# é necessário quebrar nosso código em códigos menores e reutilizáveis, que chamamos de função
# usamos o comando def para criar a função, onde poderá ser usada em outros códigos.
# Parâmetros: São informações passadas de antemão para as funções

def saudacoes(first_name, last_name):
    print(f'Olá {first_name} {last_name}!!!')
    print('Bem vindo!!!')

# Em alguns casos, nós especificamos a variável nos parâmetros, conforme abaixo:
# def saudacoes(first_name="John, last_name="Zorn"):

'''Importante: a execução não interpreta o código acima, por ser uma função. Só o executa pois está sendo
exercitado embaixo'''

print("Comecar")

# Aqui, especificamente

saudacoes("John", "Zorn")
saudacoes("Sofia", "Rei")

# Obs: a função deve ser criada antes de ser chamada para a execução

print("Finalizar")




