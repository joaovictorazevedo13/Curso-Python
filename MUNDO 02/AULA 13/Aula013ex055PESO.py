maior = 0
menor = 0
for p in range(1, 8):
    peso = int(input('Digite o peso da {}ª pessoa? '.format(p)))
    if p == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {}Kg'.format(maior))
print('O maior peso lido foi de {}Kg'.format(menor))


