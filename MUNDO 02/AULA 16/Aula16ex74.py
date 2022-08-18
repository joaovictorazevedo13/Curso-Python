from random import randint
num = (randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), randint(1, 5), )
print(f'Numeros sorteados: {num}')
ordem = sorted(num)
print('A ordem dos numeros: {}'.format(ordem))
print(f'Maior numero é o {max(num)} e o menor numero é o {min(num)}')