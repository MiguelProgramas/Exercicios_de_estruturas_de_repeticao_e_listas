IdadesDosUsuários = []
AlturasDosUsuários = []

for item in range(5):
    print("Qual é a sua idade? (Em anos, naturalmente).")
    IdadeDoUsuário = input()
    print("Agora, a sua altura, por favor. (Não se incomode com unidades de medida, insira apenas o número).")
    AlturaDoUsuário = input()
    IdadesDosUsuários.append(IdadeDoUsuário)
    AlturasDosUsuários.append(AlturaDoUsuário)
IdadesDosUsuários.reverse()
AlturasDosUsuários.reverse()

print("As idades dos participantes, quando invertidas, seguem como: " + str(IdadesDosUsuários))
print("As alturas dos participantes, quando invertidas, seguem como: " + str(AlturasDosUsuários))

