n = int(input('Digite a quantidade de termos a serem mostrados fibonacci: '))
t1 = 0
t2 = 1
cont = 0
print('{} - {} - '.format(t1, t2),end='')
while cont <= n:
    t3 = t1 + t2
    print('{} - '.format(t3), end='')
    cont += 1
    t1 = t2
    t2 = t3
print('fim')

