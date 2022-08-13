nota = []
for i in range (0,5):
    valor = int (input ("Digite o valor da nota: "))
    nota.append(valor)
print(nota)
print(sum(nota)/len(nota))
media = sum(nota)/len(nota)
if media >= 6:
    print ("Aluno Aprovado")
else:
    print ("Aluno Reprovado")
