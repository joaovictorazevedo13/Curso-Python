while True:
    n = int(input('Digite o numero para saber a tabuada: '))
    if n < 0:
        break
    for c in range(1, 11):
        print(f'{n} x {c} = {n*c}')

print('FIM')