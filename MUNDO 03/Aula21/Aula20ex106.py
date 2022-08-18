c = ('\033[m',  # 0 sem cor
     '\033[0;30;44m',  # 1 azul
     '\033[7;40m')  # 2 branco)


def ajuda(com):
    titulo(f"Acessando o manual do comando \ '{com} \'", 1)
    print(c[2])
    help(com)


def titulo(msg, cor=0):
    tam = len(msg)
    print(c[cor], end='')
    print('~' * tam)
    print(msg)
    print('~' * tam)
    print(c[0], end='')


while True:
    titulo('SISTEMA DE AJUDA PyHelp', 1)
    item = str(input('Digite algo que você precisa de ajuda no Python: ')).upper()
    if item == 'FIM':
        'FIM DO SISTEMA'
        break
    else:
        ajuda(item)
titulo('Fim do Programa', 1)