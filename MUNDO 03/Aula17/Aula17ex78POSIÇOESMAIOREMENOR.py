valores = list()
for cont in range(0, 5):
    valores.append(int(input(f'Digite o valor na posição {cont}: ')))
print(f'\nVocê digitou os valores: {valores}')
print(f'O maior valor digitado foi o {max(valores)} nas posições: ', end='')
for c, v in enumerate(valores):
    if v == (max(valores)):
        print(f'{c}...', end='')
print('\n')
print(f'O menor valor digitado foi o {min(valores)} nas posições: ', end='')
for c, v in enumerate(valores):
    if v == (min(valores)):
        print(f'{c}...')


#print(f'Menor numero: {min(valores)} Posição: {posmenor}\n'
      #f'Maior numero: {max(valores)} Posição: {posmaior}')
