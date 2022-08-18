frase = str(input('Digite uma frase: ')).strip().upper()
separar = frase.split()
juntar = ''.join(separar)
inverso = ''
for letra in range(len(juntar) - 1, - 1, - 1):
    inverso = inverso + juntar[letra]
if juntar == inverso:
    print('A frase {} é um palindromo'.format(frase))
else:
    print('A frase {} não é um palindromo'.format(frase))
