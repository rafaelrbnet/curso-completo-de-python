#!/usr/bin/env python
# -*- coding: UTF-8 -*- 

# Como podemos observar o laço for é bem mais difícil que um laço de modo infinito. Não possui diferenças entre usar o while ou o for.
lista = [ # 0    # 1       # 2 
		"linux","devops","python"
]

for i in lista:
	print i


# Por padrão o laço for nao printa os números do índice da lista. Para isso é necessário chamar o comando "enumerate"

lista2 = [# 0    # 1       # 2
		"linux","devops","python"
]

for num,item in enumerate(lista):
	print "%s está na posição %s"%(item,num)


