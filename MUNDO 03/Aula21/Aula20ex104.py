def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input('Digite um numero: '))
        if n.isnumeric():
            n = int(n)
        else:
            print('Numero invalido. Digite um numero valido. ')
        if ok:
            break
    return valor


n = leiaInt('Digite um numero: ')
print(f'Voce digitou o numero {n}')