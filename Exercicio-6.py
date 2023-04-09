ListaAlunoNotas = [['Caio', [10, 10, 10, 10]], ['Henrique', [9, 8, 7, 6]], ['Ian', [8, 7, 8, 9]], ['Davi', [10, 8, 8, 9]], ['Samuel', [2, 3, 4, 8]], ['Cauã', [4, 6, 8, 6]], ['Maykon', [6, 8, 10, 8]], ['João', [8, 10, 6, 9]], ['Arthur', [1, 1, 1, 1]], ['Kiryu Kazuma', [10, 10, 10, 10]]]

def calcularMédia(aluno):
    notas = aluno[1]
    media = sum(notas) / len(notas)
    return media

for aluno in ListaAlunoNotas:
    nome = aluno[0]
    media = calcularMédia(aluno)
    if media >= 7:
        print(f'O aluno {nome} teve média de {media:.2f}.')

