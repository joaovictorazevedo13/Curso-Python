n = int(input('Digite 999 para parar: '))
soma = 0
soma2 = 0
while n != 999:
    soma = soma + 1
    soma2 = soma2 + n
    n = int(input('Digite 999 para parar: '))
print('Foram digitados {} números e a soma entre eles é igual a {}'.format(soma, soma2))
