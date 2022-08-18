from moeda import aumentar, diminuir, metade, dobro, moeda
n = float(input('Digite um preço: R$'))
print(f"{moeda(n)} - 10% = {moeda(aumentar(n))}")
print(f"{moeda(n)} + 10% = {moeda(diminuir(n))}")
print(f'A metade de {moeda(n)} é igual a {moeda(metade(n))}')
print(f'O dobro de {moeda(n)} é igual a {moeda(dobro(n))}')
