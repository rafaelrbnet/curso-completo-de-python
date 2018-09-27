"""
  O uso do lambda é excelente para
  calcular operações matemáticas. 
  Um típico exemplo é o uso na 
  black friday, onde os preços 
  são diminuidos. 


  Modificado em 09 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 27 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""

carrinho = []

produto1 = {"nome": "Tênis", "valor": 21.32}

black_friday = lambda x: x * 2

print("Valor do produto: {}".format(black_friday(produto1["valor"])))
print("Com desconto de 50% {}".format(produto1["valor"]))
