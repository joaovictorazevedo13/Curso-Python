lista = list()
par = list()
impar = list()
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    continuar = str(input('Deseja continuar?[S/N] ')).upper().strip()[0]
    if continuar == 'N':
        break
for pos, num in enumerate(lista):
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)
print('=-=-=-' * 5)
print(f'Lista: {lista}')
print(f'Lista par: {par}')
print(f'Lista impar: {impar}')