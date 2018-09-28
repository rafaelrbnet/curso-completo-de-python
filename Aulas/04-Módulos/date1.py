"""
  Temos um script que simula a expiração 
  de um token de acesso. Criamos uma
  subtração de 2 objetos Datetime e nessa
  diminuição, ele nos retorna um outro objeto
  Datetime com a diferença nas datas.
  Agora podemos usar o método total_seconds
  que irá mudar o resultado em segundos e irá
  comparar com o valor de 3600 segundos que 
  equivale a 1h.


  Modificado em 14 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 28 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""

from datetime import datetime

acesso = datetime(2017, 1, 22, 00, 00, 00)
atual = datetime(2017, 1, 22, 1, 2, 00)

if (atual - acesso).total_seconds() > 3600:
    print("Seu token expirou")
else:
    print("Acesso liberado")
