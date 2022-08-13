# exercício com listas usando números
import random

numeros = [random.randrange(10)]
max = numeros[0]
print(max)
for numero in numeros:
    if numero > max:
        max = numeros
print(max)

