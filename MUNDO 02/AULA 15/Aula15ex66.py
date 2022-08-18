soma = quant = 0
while True:
    n = int(input('Digite 999 para parar: '))
    if n == 999:
        break
    quant = quant + 1
    soma = soma + n
print(f'A soma dos {quant} numeros é igual a {soma}')
