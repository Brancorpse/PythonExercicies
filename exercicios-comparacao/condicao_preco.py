# Exercício para testar condições
import  math as mt

good_credit = False
bad_credit = True

if good_credit:
    valor_casa = 1000000 * 10 / 100
elif bad_credit:
    valor_casa = 1000000 * 20 / 100
print(f"Valor do desconto: ${valor_casa}")
