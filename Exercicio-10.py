print("Insira um número de sua escolha, por favor.")
Número1 = input()
print("Muito bem. Agora, um outro número, também de sua escolha.")
Número2 = input()
if Número1 > Número2:
    for Número in range(int(Número2) + 1, int(Número1)):
        print("Os valores entre os números " + str(Número2) + " e " + str(Número1) + " são: " + str(Número) + ".")
elif int(Número2) > int(Número1):
    for Número in range(int(Número1) + 1, int(Número2)):
        print("Os valores entre os números " + str(Número2) + " e " + str(Número1) + " são: " + str(Número) + ".")