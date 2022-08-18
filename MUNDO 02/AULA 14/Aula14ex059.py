print('DIGITE 2 NUMEROS E SELECIONE UMA DAS OPÇÕES')
n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
opc = 0
while opc != 5:
    opc = int(input('[ 1 ] Somar\n'
                '[ 2 ] Multiplicar\n'
                '[ 3 ] Maior\n'
                '[ 4 ] Novos numeros\n'
                '[ 5 ] Sair do programa\n'
                'Selecione uma das opções acima: '))

    if opc == 1:
        print('A soma entre {} e {} é igual a {}'.format(n1, n2, (n1+n2)))
    elif opc == 2:
        print('A multiplicação entre {} e {} é igua a {}'.format(n1, n2, (n1*n2)))
    elif opc == 3:
        if n1 > n2:
            print('O maior numero é o {}'.format(n1))
        else:
            print('O maior numero é o {}'.format(n2))
    elif opc == 4:
        print('------------------------------\n'
              'DIGITE 2 NUMEROS E SELECIONE UMA DAS OPÇÕES')
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
    elif opc == 5:
        print('Finalizando...')
    else:
        print('Opção invalida. Tente novamente')
print('FIM')
