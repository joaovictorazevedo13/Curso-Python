galera = list()
dado = list()
maior = menor = 0
while True:
    dado.append(str(input('Nome: ')))
    dado.append(float(input('Peso: ')))
    if len(galera) == 0:
        maior = menor = dado[1]
    else:
        if dado[1] > maior:
            maior = dado[1]
        if dado[1] < menor:
            menor = dado[1]
    galera.append(dado[:])
    dado.clear()
    cont = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if cont == 'N':
        break
print(f'Total de pessoas cadastradas: {len(galera)}')
print(f'Maior peso foi de {maior}Kg e foi de +', end='')
for p in galera:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print()
print(f'Menor peso foi de {menor}Kg e foi de ', end='')
for p in galera:
    if p[1] == menor:
        print(f'{p[0]}')
print()
