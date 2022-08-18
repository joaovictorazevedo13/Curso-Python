n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))
media = (n1 + n2) / 2
if media < 5:
    print('Aluno reprovado!')
elif 5 < media < 6.9:
    print('Aluno em recuperação.')
else:
    print('Aluno aprovado!')