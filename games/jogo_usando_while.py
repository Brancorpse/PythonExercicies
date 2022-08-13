# Criando jogo de palpite com while. Primeiro, inserimos um número secreto
# Criado abaixo variáveis que serão usadas de parâmetro do inicio e fim do loop
import random

numero_secreto = random.randrange(1,10)
contagem_palpite = 0
limite_palpite = 3

# Criando loop de opções

while contagem_palpite < limite_palpite:
    palpite = int(input('Insira um número de 1 a 10: '))
    contagem_palpite += 1
    if palpite == numero_secreto:
        print('Acertou! Você venceu!!!')
        break

    else:
        print('Errou! Tende de novo!!!')

print(f'O número secreto é: {numero_secreto}')
print('Game Over!')

