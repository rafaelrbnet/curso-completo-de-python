"""
  Abaixo segue um exemplo do uso de 
  funções. A primeira dela possui 
  uma parâmetro obrigatório e outra 
  não. O parâmetro é o valor esperado 
  entre parênteses nas funções.


  Modificado em 09 de março de 2017
  por Vitor Mazuco (vitor.mazuco@gmail.com)

  Editado em 27 Setembro 2018
  por Rafael Baena Neto (rafael.baena@gmail.com)
  Alteração para PEP 8 e Python 3
"""

produtos = []  # Uma lista vazia a ser preenchida com todos os itens que serão salvos aqui!


# Função que faz o cadastramento de produtos e armazena na lista 'produtos'
def cadastrar_produto(oproduto):
    global produtos
    produtos.append(oproduto)


# Função que mostra os produtos na lista 'produtos'
def listar_produtos():
    global produtos
    for p in produtos:  # Usa a interação for...in para percorrer toda a lista e mostrar quais itens estão presentes
        if p != 'sair':
            print(p)  # printa os itens


produto = ""  # variavel do 'raw_input' ** não confunda com a lista acima! **
while produto != 'sair':  # Ao escrever sair, ele para o script
    produto = input("Digite o produto que queira cadastrar: ")
    cadastrar_produto(produto)  # Chama a função 'cadastrarProduto'
    print("produtos cadastrados com sucesso")  # Printa na tela se foi cadastrado ou não
    listar_produtos()  # mostra os produtos cadastrados na lista
