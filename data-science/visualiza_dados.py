# Visualização em Pyyhon



import matplotlib.pyplot as plt

x = [1,2, 4, 5]
y = [2,3, 7, 1]
eixox = "Eixo x"
eixoy = "Eixo Y"
titulo = "Meu primeiro Gráfico em Python"

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.plot(x,y)
plt.show()

