animais = ["gato", "cachorro", "papagaio", "boi"]

print(animais)

print('# add um item na posição 2 da lista')
animais.insert(2, "boi")
print(animais)

print('# remove o item da lista')
animais.remove("boi")
print(animais)

print('# remove último item da lista')
animais.pop()
print(animais)

print('# remove o item na posição 1 da lista')
animais.pop(1)
print(animais)

print('# mostra a posição em que o item aparece na lista')
print(animais.count("gato"))
