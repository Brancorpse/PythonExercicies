# tuples são listas que não podem ser alteradas. Não podemos inserir mais itens nem remover

# Para definir uma tuple, apenas crie uma lista usando parênteses em vez de colchetes

numbers = (1, 2, 3)

# só podemos contar e puxar o index de cada posição
print(numbers[0])

# Unpacking - desempacotar uma tuple em várias variáveis

x, y, z = numbers

print(x, y, z)

