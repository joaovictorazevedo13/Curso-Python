num = list([[], []])
valor = 0
for c in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        num[0].append(valor)
    else:
        num[1].append(valor)
print(f'Numeros pares: {num[0]}\n'
      f'Numeros impares: {num[1]}')
