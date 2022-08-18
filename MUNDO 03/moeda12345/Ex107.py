from moeda import aumentar, diminuir, metade, dobro
n = float(input('Digite um preço: R$'))
print(f"{n} + 10% = R${aumentar(n, 10):.2f}")
print(f"{n} - 10% = R${diminuir(n, 10):.2f}")
print(f'A metade de R${n} é igual a {metade(n):.2f}')
print(f'O dobro de R${n} é igual a {dobro(n):.2f}')


