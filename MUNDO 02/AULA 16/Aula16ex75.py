import par as par

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
n4 = int(input('Digite o quarto numero: '))
n = (n1, n2, n3, n4)
print(f'O numero 9 apareceu {n.count(9)} vezes')
if 3 in n:
    print(f'O 3 foi digitado na posição {n.index(3)+1} pela primeira vez')
else:
    print('O numero 3 nao foi digitado')
print('Números pares: ', end='')
for c in n:
    if c % 2 == 0:
        print(f'{c}', end=' ')