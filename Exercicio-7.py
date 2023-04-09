Multiplicar = 1
ListaDe5Números = [1, 2, 3, 4, 5]
Soma = sum(ListaDe5Números)
print("O total da soma dos números nessa lista é de: " + str(Soma) + "!")
for Número in ListaDe5Números:
    Multiplicar *= Número
    Número += 1
print("O total da multiplicação dos números nessa lista é de: " + str(Multiplicar) + "!")
print(ListaDe5Números)