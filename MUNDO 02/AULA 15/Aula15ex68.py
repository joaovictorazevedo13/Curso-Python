from random import randint
while True:
    n = int(input('Diga um valor: '))
    computador = randint(0, 10)
    total = n + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    print(f'voce jogou {n} e o computador jogou {computador}. Total de {total}')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    if tipo == 'P':
        if total % 2 == 0:
            v = 0
            print('Você venceu')
            v = v + 1
        else:
            print('Voce perdeu')
            break
    if tipo == 'I':
        if total % 2 == 1:
            v = 0
            print('Você venceu!')
            v = v + 1
        else:
            print('Você perdeu!')
            break
        print('Vamos jogar novamente...')
print(f'Você venceu {v} vezes')
