n = int(input('Digite um número para saber se é primo: '))
cont = 0
for c in range(1, n + 1):
    if n % c == 0:
        cont = cont + 1
print('\nO numero {} foi divisivel {} vezes, por tanto:\n'.format(n, cont))
if cont == 2:
    print("O numero {} é primo".format(n))
else:
    print('O numero {} não é primo'.format(n))

