# Novo módulo para organizar código que contém função de comparação de lista

def find (numbers):

    max = numbers[0]
    for number in numbers:
        if number > max:
            max = number
    return max




