usuario = "vitor"
password = "123456"


login = input("Digite o seu login de usuário: ")
senha = input("Digite a sua senha: ")

if (login == usuario) and (senha == password):
    print("Usuário autenticado com sucesso!")
    print("Seja Bem Vindo {} ".format(login))
else:
    print("Acesso Negado!")
