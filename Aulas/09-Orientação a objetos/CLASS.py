"""
  Nesse script vamos
  trabalhar com 
  classes

  Modificado em 06 de abril de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 03 Outubro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""


class Servidor:
    memoria = None
    disco = None
    cpu = None


dns = Servidor()

# Essas linhas abaixo estamos dando valores aos seus atributos. De tal modo que podemoss resgatar o valor deles
# futuramente.

dns.memoria = 2048
dns.disco = 50
dns.cpu = 2

print(
    "O servidor tem as seguintes configurações: CPU {}, Memória: {}, Disco {} GB "
    .format(dns.cpu, dns.memoria, dns.disco)
)
