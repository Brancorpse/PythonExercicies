notas = list(map(float, input('Digite as notas das provas: ').split()))
ac = list(map(float, input('Digite as notas das atividades: ').split()))
simulado = float(input('Digite a nota do simulado: '))

media_provas = (sum(notas) / len(notas))
media_ac = (sum(ac) / len(ac))
media_final = ((media_provas + media_ac + simulado) / 3)

print(f'\033[32mA Média Final é: {media_final:.1f}')

if media_final >= 6:
    print('Na média!')
else:
    print('Abaixo da média')



    



        


             
