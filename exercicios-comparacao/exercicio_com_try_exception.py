# Exercicio contendo as funções try e exception
# No terminal, exit code 1 sempre significa crash no app

try:
    idade = int(input('Idade: '))
    renda = 20000
    risco = renda / idade
    print(idade)
# except informa condições de erro caso os valores inseridos sejam incorretos
except ZeroDivisionError:
    print("Idade não pode ser zero")

except ValueError:
    print('Valor Inválido')


