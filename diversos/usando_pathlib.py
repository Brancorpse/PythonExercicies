# Trabalhando com pacotes com função de manipular arquivos

# Importando a classe principal

from pathlib import Path

# Instanciando objeto contendo arquivo para a procura

path = Path("../exercicios_modulos")

# Resultado mostra que a pasta existe com valor booleando. 'True'.

print(path.exists())

# verificando todos os arquivos python existentes

for file in path.glob('*.py'):
    print(file)



#

