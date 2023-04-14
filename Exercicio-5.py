População_A = []
Crescimento_A = []

População_B = []
Crescimento_B = []

Anos_Necessários = 0

while True:
    print("Favor inserir a população total do país 'A' (o valor inserido deve ser maior que 0).")
    População_A = input()
    while int(População_A) < 1:
        print("O valor inserido é menor que 1. Favor tentar novamente:")
        População_A = input()
    print("Agora, a taxa de crescimento do país 'A' (o valor inserido pode ser um número decimal, e deve ser igual ou maior que 1.")
    Crescimento_A = input()
    Crescimento_A = float(Crescimento_A)
    while float(Crescimento_A) < 1.0:
        print("O valor inserido é menor que 1. Favor tentar novamente:")
        Crescimento_A = input()
    print("Partindo para a população total do pais 'B', agora. (Lembrando que o valor deve ser maior que 0).")
    População_B = input()
    while int(População_B) < 1:
        print("O valor inserido é menor que 1. Favor tentar novamente:")
        População_B = input()
    print("Finalizando com a taxa de crescimento do país 'B'. (Lembrando que o valor inserido pode ser um decimal, porém é obrigatório que seja maior que 0).")
    Crescimento_B = input()
    Crescimento_B = float(Crescimento_B)
    while float(Crescimento_B) < 1.0:
        print("O valor inserido é menor que 1. Favor tentar novamente:")
        Crescimento_B = input()

    while int(População_A) < int(População_B):
        População_A = float(População_A) + (float(População_A)*float(Crescimento_A))
        População_B = float(População_B) + (float(População_B)*float(Crescimento_B))
        Anos_Necessários += 1

    print("Será necesário um total de " + str(Anos_Necessários) + " anos para que a população do país A se iguale ou ultrapasse a população do país B.")

    print("Gostaria de tentar novamente? (S para sim, N para não).")
    Resposta_Final = input()
    Resposta_Final = Resposta_Final.lower()
    if Resposta_Final == "n":
        print("Entendido. Obrigado.")
        break
