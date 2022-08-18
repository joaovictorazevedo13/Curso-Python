matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = sterc = maior =  0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
        if matriz[l][c] % 2 == 0:
            spar += matriz[l][c]
print('\nMATRIZ')
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print(f'A soma dos valores pares é igual a: {spar}')
for l in range(0, 3):
    sterc += matriz[l][2]
print(f'A soma dos valores na terceira coluna é igual a: {sterc}')
for c in range(0, 3):
    if c == 0:
        maior = matriz[1][c] #maior recebe matriz
    else:
        if matriz[1][c] > maior:
            maior = matriz[1][c]
print(f'O maior valor da segunda linha: {maior}')