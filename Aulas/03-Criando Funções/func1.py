"""
  Um função com um parâmetro
  opcional, seria o cálculo de
  uma compra com o uso de 
  um cupom de desconto


  Modificado em 09 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 27 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""

carrinho = []

produto1 = {"nome": "tênis", "valor": 21.32}
produto2 = {"nome": "meia", "valor": 31.32}
produto3 = {"nome": "camiseta", "valor": 31.32}
produto4 = {"nome": "shorts", "valor": 41.32}

carrinho.append(produto1)
carrinho.append(produto2)
carrinho.append(produto3)
carrinho.append(produto4)


def total_carrinho(carrinho):
    return sum(produto["valor"] for produto in carrinho)


def cupom_desconto(cupom=""):
    if cupom == "gratis":
        return 0.70  # Desconto de 30% é calculado
    else:
        return 1


print("O total de sua compra é de: {:2f}".format(total_carrinho(carrinho) * cupom_desconto()))
print("Usando o cupom gratis seu valor será de: {:.2f} 30% menos!".format(
    total_carrinho(carrinho) * cupom_desconto("gratis"))
)
