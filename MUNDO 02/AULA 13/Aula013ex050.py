soma = 0
cont = 0
for c in range(1, 7):
    n = int(input('Digite o {} valor: '.format(c)))
    if c % 2 == 0:
        soma = soma + n
        cont = cont + 1
print('\nA soma dos {} valores solicitados é igual a: {}'.format(cont, soma))
