print(('-' * 39))
print(f'{"LISTA DE PRODUTOS":^39}')
print(('-' * 39))
produtos = ('Arroz', 8.00, 'Feijao', 10.00, 'Batata', 5.00, 'Macarrao', 3.00, 'Molho de Tomate', 2.00, 'Farinha', 5.99, 'Manteiga', 4.99)
for pos in range(0, len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}', end='')
    if pos % 2 == 1:
        print(f'R${produtos[pos]:>6.2f}')