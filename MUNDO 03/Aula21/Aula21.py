def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f = f * c
    return f

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False


num = int(input('Digite um numero: '))
if par(num):
    print(f'{num} é par e o seu fatorial é igual a: {fatorial(num)}')
else:
    print(f'{num} é impar e o seu fatorial é igual a: {fatorial(num)}')

