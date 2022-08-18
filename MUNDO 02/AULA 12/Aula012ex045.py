import time
from random import randint
print('JOKENPÔ!')
jogador = int(input('[ 0 ] Pedra\n'
                    '[ 1 ] Papel\n'
                    '[ 2 ] Tesoura\n'
                    'Digite a opção: '))
lista = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)

print('Escolha do Jogador: {}'.format(lista[jogador]))
print('==' * 5)
time.sleep(1)
print('JO\n'
      'KEN...')
time.sleep(2)
print('PÔ!')
print('==' * 5)
print('Escolha do PC: {}'.format(lista[pc]))
print('==' * 5)
if (pc == 0 and jogador == 2) or (pc == 1 and jogador == 0) or (pc == 2 and jogador == 1):
    print('PC ganhou!')
elif (pc == 2 and jogador == 0) or (pc == 0 and jogador == 1) or (pc == 1 and jogador == 2):
    print('Jogador ganhou!')
else:
    print('EMPATE!')

