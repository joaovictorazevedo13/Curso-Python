soma = 0
n = int(input('Digite um numero para saber a tabuada: '))
for c in range(1, 11):
    print(('{} x {:2} = {}').format(n, c, n*c))
