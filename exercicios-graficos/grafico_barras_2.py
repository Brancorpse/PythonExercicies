import matplotlib.pyplot as plt

x1 = [1,2,4,5]
y1 = [2,3,7,1]

x2 = [5,3,9,0]
y2 = [1,7,8,5]

plt.title("Gráfico de Barras em Python")
titulo = "Gráfico de Barras"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)


plt.bar(x1,y1, label = "Grupo 1")
plt.bar(x2,y2, label = "Grupo 2")
plt.show()
