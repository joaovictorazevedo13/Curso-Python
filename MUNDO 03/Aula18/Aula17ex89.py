ficha = []
while True:
    nome = str(input('Nome: '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1+n2)/2
    ficha.append([nome, [n1, n2], media])
    cont = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print('-=' * 30)
print(f'{"nº":<4}{"NOME":<10}{"MEDIA":>8}')
print('--' * 30)
for c, a in enumerate(ficha):
    print(f'{c:<4}{a[0]:<10}{a[2]:>8}')
while True:
    opc = int(input('Deseja ver a nota de qual aluno (999 interrompe): '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('fim')