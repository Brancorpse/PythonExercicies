import random

# Criando app de rola dados usando a biblioteca random


class Dice:
    def roll(self):
        first = random.randint(1,6)
        second = random.randint(1,6)
        return (first, second)

# Instanciando o objeto


dice = Dice()
print(dice.roll())