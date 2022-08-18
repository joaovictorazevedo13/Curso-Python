from random import randint
from time import sleep
lista = []
jogos = []
cont = 0
print('MEGASENA\n')
quantidade = int(input('Quantidade de jogos que deseja fazer? '))
total = 1
while total <= quantidade:
    cont = 0
    while True:
        n = randint(1, 60)
        if n not in lista:
            lista.append(n)
            cont = cont + 1 #contador quant de vezes que ja apareceu
        if cont >= 6:
            break
    lista.sort()
    total = total + 1
    jogos.append(lista[:])
    lista.clear()
for i, l in enumerate(jogos):
    print(f'Jogo {i+1}: {l}')
    sleep(1)
print('----- BOA SORTE -----')