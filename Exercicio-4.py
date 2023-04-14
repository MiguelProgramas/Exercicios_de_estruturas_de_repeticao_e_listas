População_A = 80000
Crescimento_A = 1.03

População_B = 200000
Crescimento_B = 1.015

Anos_Necessários = 0

while População_A < População_B:
    População_A = População_A + (População_A*Crescimento_A)
    População_B = População_B + (População_B*Crescimento_B)
    Anos_Necessários += 1

print(Anos_Necessários)

