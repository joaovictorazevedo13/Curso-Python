lanche = ['lanche', 'batata', 'refri']
print(f'Pedido: {lanche}')
n = str(input('Deseja algum adicional? [S/N] ')).strip().upper()
while True:
    if n == 'N':
        print('Sem adicional')
        break
    if n == 'S':
        add1 = str(input('Deseja adicional de bacon? [S/N] ')).strip().upper()[0]
        add2 = str(input('Deseja adicional de queijo? [S/N] ')).strip().upper()[0]
    if add1 == 'S':
        lanche.append('+ bacon')
    if add2 == 'S':
        lanche.append('+ queijo')
        print(f'Pedido atualizado: {lanche}')
        break
