valores = list()
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
        print('Adicionado com sucesso')
    else:
        print('Numero duplicado.')
    continuar = str(input('Deseja continuar?[S/N] ')).upper().strip()
    if continuar == 'N':
        break
print(f'\nNumeros digitados: {sorted(valores)}')