from random import randint
print('PC: Estava pensando em numero entre 0 e 10.')
pc = randint(0, 10)
acertou = False
tentativas = 0
while not acertou:
    jogador = int(input('Digite um numero para tentar adivinhar: '))
    tentativas = tentativas + 1
    if jogador == pc:
        acertou = True
    else:
        if jogador > pc:
                        print('- Menos!')
        if jogador < pc:
            print('- Mais!')
print('Parabens voce acertou em {} tentativas!'.format(tentativas))
