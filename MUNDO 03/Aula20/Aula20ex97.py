def lin():
    print('-=' * 20)


itens = []
while True:
    e = str(input('Escreva algo: '))
    itens.append(e)
    while True:
        cont = str(input('Deseja continuar?[S/N] ')).upper()[0]
        if cont in 'SN':
            break
        print('ERRO. Utilize apenas S ou N.')
    if cont == 'N':
        break

for k, v in enumerate(itens):
    lin()
    print(f'{v}'.center(40))
    lin()