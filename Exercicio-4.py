from decimal import Decimal

população_A =  Decimal(80000.0)
crescimento_A =  Decimal(1.03)

população_B =  Decimal(200000.0)
crescimento_B = Decimal( 1.015)

anos_Necessários = 0

while população_A <= população_B:
    população_A = população_A*crescimento_A
    população_B = população_B*crescimento_B
    anos_Necessários += 1

print(anos_Necessários)