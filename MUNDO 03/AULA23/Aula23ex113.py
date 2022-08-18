def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO. Por favor, digite um numero valido.')
            continue
        except (KeyboardInterrupt):
            print('Entrada de dados interrompida pelo usuário.')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            r = float(input(msg))
        except (ValueError, TypeError):
            print(f'ERRO. Digite um numero real válido.')
            continue
        else:
            return r


n = leiaInt('Digite um numero inteiro: ')
r = leiaFloat('Digite um numero real: ')
print(f'Voce digitou o numero {n}')
print(f'Voce digitou o numero {r}')
