linha = [[], [], []]
par = []
for c in range(0, 3):
    n = int(input(f'Digite um valor para [0, {c}]: '))
    linha[0].append(n)
    if n % 2 == 0:
        par.append(n)
for c in range(0, 3):
    n1 = int(input(f'Digite um valor para [1, {c}]: '))
    linha[1].append(n1)
    if n1 % 2 == 0:
        par.append(n1)
for c in range(0, 3):
    n2 = int(input(f'Digite um valor para [2, {c}]: '))
    linha[2].append(n2)
    if n2 % 2 == 0:
        par.append(n2)
print('\nMATRIZ')
print(f'[{linha[0][0]:^5}] [{linha[0][1]:^5}] [{linha[0][2]:^5}]\n'
      f'[{linha[1][0]:^5}] [{linha[1][1]:^5}] [{linha[1][2]:^5}]\n'
      f'[{linha[2][0]:^5}] [{linha[2][1]:^5}] [{linha[2][2]:^5}]')
print('-==' * 30)
print(f'A soma dos valores pares é igual a: {sum(par)}\n'
      f'A soma dos valores da terceira coluna é igual a: {(linha[0][2]) + (linha[1][2]) + (linha[2][2])}')
print(f'O maior da segunda linha: {max(linha[1])}')

