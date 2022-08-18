from moeda import aumentar, diminuir, metade, dobro, moeda
n = float(input('Digite um preço: R$'))
print(f'{moeda(n)} + 10% = {aumentar(n, 10, True)}')
print(f'{moeda(n)} - 10% = {diminuir(n, 10, True)}')
print(f'A metade de {moeda(n)} é igual a {(metade(n, True))}')
print(f'O dobro de {moeda(n)} é igual a {(dobro(n, True))}')
