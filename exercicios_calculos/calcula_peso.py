peso_grama = input('Digite o seu peso em gramas: ')
# função type mostra o tipo da variável em questão
print(type(peso_grama))
quilo = int(peso_grama)/100
# converter para libras

peso_libra = quilo / 0.45359237
print('Valor em quilo')
print(quilo)
print('Valor em libra')
print(f"Seu peso em libra é: {peso_libra}")