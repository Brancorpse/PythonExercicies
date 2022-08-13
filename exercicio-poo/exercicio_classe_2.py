# Segundo exercicio usando POO

# Criando a classe e o construtor

class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"Hi, i'm {self.name}")

# Instanciando o primeito objeto

john = Person(" John Smith")
john.talk()

# Instanciando o segundo objeto
# Cada obejto é uma instância diferente da classe Person
bob = Person("Bob Silva")
bob.talk()





