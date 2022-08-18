soma = 0
n = 0
soma2 = 0
while n != 999:
    soma += 1
    soma2 += n
    n = int(input('Digite um numero[999 para parar]: '))
print('Foram digitados {} numeros.'.format(soma))
print('E a soma entre eles é igual a {}'.format(soma2))
