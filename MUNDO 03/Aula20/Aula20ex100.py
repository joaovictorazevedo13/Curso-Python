from random import randint
numeros = [[], []]


def lin():
    print('=' * 40)

def somaPar():
    print(f'Numeros pares: {numeros[1]}\n'
          f'A soma dos numeros pares: {sum(numeros[1])}')


def sorteia():
    lin()
    print('Numeros sorteados:')
    for c in range(0, 5):
        n = randint(0, 10)
        numeros[0].append(n)
        if n % 2 == 0:
            numeros[1].append(n)
    print(numeros[0])
    somaPar()
    numeros[0].clear()
    numeros[1].clear()


quantidade = int(input('Deseja fazer quantos sorteios:'))
for c in range(0, quantidade):
    sorteia()
print('FIM')