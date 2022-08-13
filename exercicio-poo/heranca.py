# Herança é quando uma classe herda métodos e funções de outra classe. reusa o código
# Exercício exemplo herança

# Classe mãe criada inicialmente, onde as filhas herdarão funções

# Importando módulo para converter peso

from exercicios_modulos.converter_peso_bixo import calcula_peso

class Mammal:

    def __init__(self, name):
        self.name = name

    def walk(self):
        print("walk")

# Agora, as classes Dog e Cat herdará a função da classe mãe

class Dog(Mammal):
    def bark(self):
        print(f"Eu sou {self.name}")
        print("Au Au Au")
        print(calcula_peso(500))

# Sempre reuse seu código. Não se repita. Deixará o código melhor
# Instanciando objetos

class Cat(Mammal):
    def meow(self):
        print(f"Eu sou {self.name}")
        print("Miau miau")
        print(calcula_peso(1200))

sabbath = Dog("Eu sou Sabbath")
sabbath.walk()
sabbath.bark()

batou = Cat("Eu sou Batou")
batou.walk()
batou.meow()










