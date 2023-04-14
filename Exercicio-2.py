Usuário = []
Senha = []
print("Favor inserir seu nome de usuário: ")
Usuário = input()
print("Agora, a sua senha: ")
Senha = input()
while Senha == Usuário:
    print("A senha não pode ser igual ao usuário, favor tentar novamente:")
    print("Insira seu nome de usuário: ")
    Usuário = input()
    print("Agora, a sua senha: ")
    Senha = input()
else:
    print("Obrigado. (Usuário inserido: " + Usuário + ") - " + "(Senha inserida: " + Senha + ")")