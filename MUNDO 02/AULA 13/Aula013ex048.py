soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont + 1
        soma = soma + c
        print(format(c), end=', ')
print('\n\nA soma dos {} valores solicitados é igual a: {}'.format(cont, soma))
