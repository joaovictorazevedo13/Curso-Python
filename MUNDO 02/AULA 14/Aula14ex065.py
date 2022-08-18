resp = 'S'
quant = media = soma = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um numero: '))
    quant = quant + 1
    soma = soma + n
    media = soma / quant
    if quant == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Deseja continuar? [S/N] ')).upper().strip()[0]
print('\nNumero digitados: {}\nSoma: {}\nMedia: {}\nMaior numero: {}\nMenor Numero: {}'.format(quant, soma, media, maior, menor))
