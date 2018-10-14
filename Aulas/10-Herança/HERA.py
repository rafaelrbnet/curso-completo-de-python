"""
  Usando o conceito de
  herança com uso de 
  classes

  Modificado em 07 de abril de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 04 Outubro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""


# Classe "Pai"
class Servidor:

    def __init__(self):
        self.memoria = None
        self.cpu = None
        self.disco = None

    def contratar_memoria(self, memoria):
        self.memoria += memoria

    def contratar_cpu(self, cpu):
        self.cpu += cpu

    def contratar_disco(self, disco):
        self.disco += disco


# Classe "Filha"
class Cloud(Servidor):
    def __init__(self):
        self.memoria = 512
        self.cpu = 1
        self.disco = 50


dns = Cloud()

print("Memória Inicial", dns.memoria)
print("Disco Inicial", dns.disco)
print("CPU Inicial", dns.cpu)

dns.contratar_disco(50)


# Classe "Filha"
class Fisico(Servidor):
    def __init__(self):
        self.memoria = 4096
        self.cpu = 4
        self.disco = 1024


dns = Fisico()
print("Fisico")
print("Memória Inicial", dns.memoria)
print("Disco Inicial", dns.disco)
print("CPU Inicial", dns.cpu)

dns.contratar_disco(1024)

print("Disco total ", dns.disco)
