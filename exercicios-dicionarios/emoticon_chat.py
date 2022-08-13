# Exercicio de pequeno app que programa uso de emoticon através de dicionário
# Assim, criaremos uma função onde conterá a configuração do dicionário a ser usado no chat

def emoji_converter(message):
    words = message.split(' ')
    emojis = {
        ":)": "😊",
        ":(": "😔"
    }
    output = ""

    for word in words:
        output += emojis.get(word, word) + " "
    return output
# Adicionando input e usando sua variável como parâmetro de envio para a função

message = input(">")
print(emoji_converter(message))






