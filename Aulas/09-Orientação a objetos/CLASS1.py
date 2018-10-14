"""
  O primeiro parâmeto self
  é obrigatório, pois é 
  com ele que o Python  
  consegue diferenciar
  os métodos das funções.

  Modificado em 06 de abril de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 04 Outubro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""


class Servidor:
    memoria = 1024
    disco = 50
    cpu = 1

    def contratar_memoria(self, memoria):
        self.memoria += memoria

    def contratar_cpu(self, cpu):
        self.cpu += cpu

    def contratar_disco(self, disco):
        self.disco += disco


dns = Servidor()

dns.contratar_memoria(1024)
dns.contratar_cpu(3)
dns.contratar_disco(50)

print(
    "O servidor tem as seguintes configurações: CPU {}, Memória: {}, Disco {} GB "
        .format(dns.cpu, dns.memoria, dns.disco)
)
