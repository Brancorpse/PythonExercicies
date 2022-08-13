# Exercício sobre métodos em lista. São operações que podemos fazer numa lista
# podemos adicionar, remover, checar, entre outras coisas nesta lista

numbers = [5, 2, 1, 7, 4]

# método para adicionar um número no fim da lista
numbers.append(20)
print(numbers)

# método para adicionar número num lugar específico da lista
# você informa primeiro a posição e em seguida, o número

numbers.insert(0, 10)
print(numbers)

# remover número da lista

numbers.remove(20)
print(numbers)

# remover todos os elementos da lista

numbers.clear()
print(numbers)

# adicionando novos elementos

numbers = [9, 23, 31, 87, 64, 72, 99, 87, 36]

print(numbers)

# removendo o último item da lista

numbers.pop()
print(numbers)

# mostrar onde o elemento está indexado na lista, sua posição

print(numbers.index(87))

# Verificar se há u número específico na lista. se não houver, o sistema retorna falso

print(50 in numbers)

# Contar números repetidos da lista

print(numbers.count(87))

# metodo para ordem crescente

numbers.sort()
print(numbers)


# método para ordem decrescente

numbers.reverse()
print(numbers)

# copiar lista

numbers2 = numbers.copy()

# ordenando novamente

numbers.sort()

# mesclando das duas listas

zip(numbers, numbers2)

# Calculando a soma das duas listas

total = []
for elemA, elemB in zip(numbers,numbers2):
    total.append(elemA + elemB)
print(total)

