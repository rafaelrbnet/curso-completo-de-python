"""
  Esse arquivo possui
  várias funções que podem 
  ser usadas em outros 
  scripts em Python fazendo assim
  um reaproveitamento de código


  Modificado em 14 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 28 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""

# Importa o arquivo utils.py que se localiza dentro desse diretório.
import utils

# Reutiliza a função escreverArquivo do arquivo utils.py
utils.escrever_arquivo("dados", "Esses são os conteúdos dos arquivos 2")

# Reutiliza a função lerArquivo do arquivo utils.py
print(utils.ler_arquivo("dados"))

# Reutiliza a função dataAtual do arquivo utils.py
print(utils.data_atual())




