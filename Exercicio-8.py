ListaNúmeros = []
print("Insira 5 números diferentes, por favor:")
for i in range (5):
    Valor_Inserido = input()
    Valor_Inserido = int(Valor_Inserido)
    ListaNúmeros.append(Valor_Inserido)

Soma = sum(ListaNúmeros)

print("O total da soma da lista é: " + str(Soma) + ".")

TamanhoDaLista = len(ListaNúmeros)

Média = Soma / TamanhoDaLista

print("O total da média da lista é: " + str(Média) + ".")