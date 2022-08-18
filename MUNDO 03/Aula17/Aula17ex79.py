valores = list()

while True:
    valores.append(int(input('Digite um numero: ')))
    continuar = str(input('Deseja continuar?[S/N] ')).upper().strip()
    apagar = set(valores)
    ordem = sorted(apagar)
    if continuar == 'N':
        break
print(f'Numeros digitados: {valores}')
print(f'Numeros digitados em ordem: {ordem}')
