# Módulos

# Basicamente, são arquivos com códigos. Usamos para organizar nosso código

# Com isso, é possível reusar o nosso código importando-o em outro módulo, quando necessário
# Neste caso, importaremos este módulo em outros arquivos

def calcula_peso(peso_grama):

    # Calculando
    quilo = int(peso_grama) / 100
    # converter para libras
    peso_libra = quilo / 0.45359237
    print('Valor em quilo')
    print(quilo)
    print('Valor em libra')
    print(f"O peso do bichinho é: {peso_libra}")






