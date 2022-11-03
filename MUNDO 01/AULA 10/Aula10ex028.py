from random import randint
from time import sleep
print('JOGO DE ADVINHAR\n')
n1 = int(input('Digite um número entre 0 e 5: '))
lista = randint(0, 5)
sorteio = lista
print('Processando...\n')
sleep(2)
if sorteio == n1:
    print('PARABENS VOCÊ ACERTOU!')
else:
    print('EROOOU! GAME OVER!')


