Lista20Números = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
Pares = []
Ímpares = []
for i in Lista20Números:
    if i%2 == 0:
        Pares.append(i)
    else:
        Ímpares.append(i)
print(str(Pares))
print(str(Ímpares))