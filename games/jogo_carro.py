# pequeno app que simula uma corrida

command = ""
iniciado = False


while True:
    command = input(">").lower()

    if command == "iniciar":
        if iniciado:
            print("Carro já está em andamento!!!")
        else:
            iniciado = True
            print("Carro saindo!!!")
    elif command == "parar":
        if not iniciado:
            print("Carro já está parado!!!")
        else:
            iniciado = False
            print("Carro parado!!!")
    elif command =="ajuda":
        print("""
iniciar - mover o carro
parar - parar  o carro
sair - fechar o jogo
        """
              )
    elif command == "sair":
        break
    else:
        print("Desculpe, eu não entendi")





