# Dados coletados do DataSus

# ler o arquivo csv
import matplotlib.pyplot
import pip
pip.main(["install","matplotlib"])

dados = open("populacao_brasileira.csv").readlines()
# tive que colocar o arquivo dentro da pasta python
x = []
y = []

for i in range(len(dados)):
    if i != 0:
        linha = dados[i].split(";")

        x.append(int(linha[0]))
        y.append(int(linha[1]))

# Apresentação

matplotlib.pyplot.bar (x,y, color = "#e4e4e4")
matplotlib.pyplot.scatter(x, y, color='k')
matplotlib.pyplot.title("Crescimento da População Brasileira")
matplotlib.pyplot.xlabel("Ano")
matplotlib.pyplot.ylabel("população x100.000.000")
matplotlib.pyplot.savefig("populacao_brasileira")
matplotlib.pyplot.show()
