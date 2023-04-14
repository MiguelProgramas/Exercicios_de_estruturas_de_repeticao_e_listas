Nome = []
Idade = []
Salário = []
Sexo = []
Estado_Civil = []

print("Favor inserir seu nome (valor inserido deve possuir mais de 3 caracteres).")
Nome = input()
while len(Nome) < 3:
    print("O valor inserido possui menos de 3 caracteres. Favor tentar novamente:")
    Nome = input()
else:
    print("O nome inserido é válido. (Nome inserido: " + Nome + ").")

print("Agora, a sua idade (valor inserido deve estar entre 0 e 150).")
Idade = input()
while int(Idade) < 0 or int(Idade) > 150:
    print("O valor inserido é inválido. Favor tentar novamente:")
    Idade = input()
else:
    print("A idade inserida é válida. (Idade inserida: " + Idade + ").")

print("Partindo para seu salário, agora (valor inserido deve ser maior que 0).")
Salário = input()
while int(Salário) < 1:
    print("O valor inserido não é maior que 0. Favor tentar novamente:")
    Salário = input()
else:
    print("O salário inserido é válido. (Salário inserido: " + Salário + ").")

print("Estamos quase lá. Agora, o seu sexo (valor inserido deve ser 'm' ou 'f').")
Sexo = input()
Sexo = Sexo.lower()
SexosVálidos = ["f", "m"]
while Sexo not in SexosVálidos:
    print("O valor inserido não é nem 'f' nem 'm'. Favor tentar novamente:")
    Sexo = input()
else:
    print("O sexo inserido é válido. (Sexo inserido: " + Sexo + ").")

print("Para finalizar, o seu estado civil (valor inserido deve ser 's', ou 'c', ou 'v' ou 'd').")
Estado_Civil = input()
Estado_Civil = Estado_Civil.lower()
Estados_Civis_Válidos = ["s", "c", "v", "d"]
while Estado_Civil not in Estados_Civis_Válidos:
    print("O valor inserido não é 's', 'c', 'v' e nem 'd'. Favor tentar novamente:")
    Estado_Civil = input()
else:
    print("O estado civil inserido é válido. (Estado civil inserido: " + Estado_Civil + ").")
