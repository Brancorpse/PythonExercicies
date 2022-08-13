# Exercicio que ensina sobre classes em Python
# Não são tão bem especificadas em Python como em outras linguagens
# Usamos classes para definir modelos complexos do mundo real
# Você add funções e métodos próprios para esses novos tipos de modelos
# Abaixo, você definirá todos os métodos e funções para a classe

# Cada objeto é diferente da sua classe. Ou seja, tem que sempre referenciar uma variável nova para instanciar

# Para resolver esse problema, usamos construtores
# Construtor é uma função que é chamada toda vez que um objeto é instanciado na memória. Ele constrói o objeto

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print ("move")
    def draw(self):
        print("draw")

# Abaixo, usaremos uma variável pra instanciar um objeto através da classe. Ou seja, vamos instanciar um objeto na memória

point = Point(10, 20)
point.draw()
print(point.x)















