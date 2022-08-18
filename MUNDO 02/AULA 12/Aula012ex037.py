n = int(input('Digite um numero para converter: '))
print('Escolha uma opção para conversão:\n'
      '[ 1 ] para binario\n'
      '[ 2 ] para octal\n'
      '[ 3 ] para hexadecimal\n')
opc = int(input('Digite a opção desejada: '))
if opc == 1:
    print('\nO numero {} convertido para binario: {}'.format(n, bin(n)[2:]))
elif opc == 2:
    print('\nO numero {} convertido para octal: {}'.format(n, oct(n)[2:]))
elif opc == 3:
    print('\nO numero {} convertido para octal: {}'.format(n, hex(n)[2:]))
