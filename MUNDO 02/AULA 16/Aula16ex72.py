extenso = ('ZEO', 'UM', 'DOIS', 'TRES', 'QUATRO', 'CINCO')
while True:
    num = int(input('Digite um numero entre 0 e 5: '))
    if 0 <= num <= 5:
        break
    print('Tente novamente. ', end=' ')
print(f'O numero digitado foi o {extenso[num]}')