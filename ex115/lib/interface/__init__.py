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


def lin(tam=42):
    print('=' * tam)


def cabecalho(txt):
    lin()
    print(txt.center(42))
    lin()


def menu(lista):
    cabecalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    lin()
    opc = leiaInt('Sua opção: ')
    return opc


