a = int(input('valor 1: '))
b = int(input('valor 2: '))
c = int(input('Valor 3: '))
if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c
#maiores teste
if a>b and a>c:
    maior = a
if b>c and b>a:
    maior = b
if c>a and c>b:
    maior = c
print('o menor valor é o: {}'.format(menor))
print('o maior valor é o: {}'.format(maior))