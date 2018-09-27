servidores = ["dns", "database", "webserver", "voip", "mongodb"]

# O comando continue é usado para trabalhar com exeção de uma lista.
for s in servidores:
    if s == "webserver":
        print("O servidor {} não pode estar na lista".format(s))
        break
    else:
        print("Todos os servidores estão atualizados")
print("Finalizando o programa")
