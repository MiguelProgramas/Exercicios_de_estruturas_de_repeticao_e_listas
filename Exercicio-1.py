ValoresCorretos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Insira uma nota entre 1 e 10, por favor.")
Nota = input()
while int(Nota) not in ValoresCorretos:
    print("Valor inválido, favor tentar novamente:")
    Nota = input()
else:
    print("Obrigado. (Valor inserido: " + Nota + ").")

