ListaTop20 = []
ListaTop10Personas = ["Archangel", "Maria", "Arsene", "Raoul", "Isanagi", "Yoshitsune", "Jack", "Silky", "Pixie", "Okami"]
ListaTop10Números = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
ListaTop10NúumerosDNV = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
for item in range(10):
    ListaTop20.append(ListaTop10Números[item])
    ListaTop20.append(ListaTop10Personas[item])
    ListaTop20.append(ListaTop10NúumerosDNV[item])
print(ListaTop20)
