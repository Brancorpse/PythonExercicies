entrada = open("human.fasta").read()
saida = open("out.html", "w")

# vetor

cont2 = {}
for i in ['A', 'T', 'C', 'G']:
    for j in ['A', 'T', 'C', 'G']:
        cont2[i+j] = 0

entrada = entrada.replace("\n","")

for k in range(len(entrada)-1):
    cont2[entrada[k]+entrada[k+1]] += 1
print(cont2)

#gerar página html

'''for k in cont2:
    saida.write("<div style='width:65px; border:1px solid #111; height:65px; float:left;background-color:rgba(0,0,255,"+str(cont2[k]/max(cont2.values()))+")'></div>\n")
    if i%4 == 0:
        saida.write("<div style='clear:both'></div")
        i += 1'''

