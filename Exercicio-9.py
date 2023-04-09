Quadrado = 1
Resultado = []
A = [1, 2, 3, 4, 5, 6, 7 , 8, 9, 10]
for Número in A:
    Quadrado = Número * Número
    Número += 1
    Resultado.append(Quadrado)
print("O total da soma dos quadrados dos números da lista é: " + str(sum(Resultado)))
