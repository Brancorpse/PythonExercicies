import matplotlib.pyplot as plt

x = [1,2,4,5]
y = [2,3,7,1]

plt.title("Gráfico de Barras em Python")
titulo = "Exercício Gráfico de Barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.bar(x,y)
plt.show()

