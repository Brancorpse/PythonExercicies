import math

''' para cãlculos mais completos, ideal é importar a biblioteca math. Módulos são arquivos com
 funções reutilizáveis e prontos'''

print(math.ceil(2.9))
print(math.floor(2.9))
print(math.factorial(2))

# funçao de arredondamento

x = 2.9
print(round(x))

# função para retornar versão positiva de um número

print(abs(-2.9))


# soma e subtração

y = 10
y -= 3
print(y)
w = y + 8
print(w)


# expressão numérica

z = 10 + 3 *2

print(z)

# exponenciação

exp = 10 + 3 *2 ** 2

print(exp)

# parenteses sempre indicam prioridade

a = (2 + 3) * 10  - 3

print(a)