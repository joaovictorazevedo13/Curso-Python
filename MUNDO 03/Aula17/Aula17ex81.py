valores = list()
total = 0
while True:
    valores.append(int(input('Digite um valor: ')))
    continuar = str(input('Deseja continuar?[S/N] ').upper().strip())
    for cont in range(0, len(valores)):
        cont += 1
    valores.sort(reverse=True)
    if continuar == 'N':
        break
print('-=' * 16)
print(f'Total de numeros digitados: {cont}')
print(f'Valores em ordem decrescente: {valores}')
if 5 in valores:
    print(f'O numero 5 foi digitado {valores.count(5)} vezes')
else:
    print('O numero 5 não foi digitado')