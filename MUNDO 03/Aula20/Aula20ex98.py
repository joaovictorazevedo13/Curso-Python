from time import sleep


def lin():
    print('-=' * 15)


def contador(i, f, r):
    print(f'Contagem de {i} até {f} de {r} em {r}:')

    if r < 0:
        r = r * -1
    if i < f:
        cont = i
        while cont <= f:
            print(f"{cont}", end=' ')
            cont = cont + r #i + r
        print('Fim')
    else:
        cont = i
        while cont >= f:
            print(f"{cont}", end=' ')
            cont = cont - r  # i + r
        print('Fim')



lin()
contador(1, 10, 1)
lin()
contador(10, 0, 2)
lin()
print('Agora é a sua vez!')
i = int(input('Inicio: '))
f = int(input('Final: '))
r = int(input('Razão: '))
lin()
contador(i, f, r)
lin()




