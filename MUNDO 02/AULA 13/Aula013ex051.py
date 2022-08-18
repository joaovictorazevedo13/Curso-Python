n1 = int(input('Primeiro termo: '))
raz = int(input('Razão: '))
dec = n1 + 10 * raz
for c in range(n1, dec, raz):
    print(c)
