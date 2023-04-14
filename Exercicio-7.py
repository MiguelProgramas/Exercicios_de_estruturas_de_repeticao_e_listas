ListaNúmeros = []
print("Insira 5 números diferentes, por favor:")
for i in range (5):
    Valor_Inserido = input()
    ListaNúmeros.append(Valor_Inserido)

MaiorDaLista = max(ListaNúmeros)

print("O maior número da lista é: " + MaiorDaLista + ".")