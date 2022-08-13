import matplotlib.pyplot as plt

x = [1,2,4,5]
y = [2,3,7,1]

titulo = "Scatterplot: Gráfico de Dispersão"
eixox = "Eixo X"
eixoy = "Eixo Y"

# Legendas
plt.xlabel("Eixo X")
plt.ylabel("Eixo Y")

plt.title(titulo)
plt.xlabel(eixox)
plt.ylabel(eixoy)

plt.scatter(x,y, label = "meus pontos", color = "red", marker="8")
plt.plot(x,y)
plt.legend()
# plt.show()
#Salvar figura

plt.savefig("gráfico.pdf")

 
