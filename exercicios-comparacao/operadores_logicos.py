# Exercício para treinar operadores lógicos

tem_bom_rendimento = True
tem_bom_credito = False
historico_criminal = False

if tem_bom_rendimento and tem_bom_credito:
    print ("Elegível para empréstimo")

if tem_bom_rendimento or tem_bom_credito:
        print("Elegível para empréstimo")

if tem_bom_rendimento and not tem_bom_credito:
        print("Elegível para empréstimo")
else:
    print("Não elegível para empréstimo")
