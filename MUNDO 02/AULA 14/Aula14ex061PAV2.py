n = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
termo = n
c = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while c <= total: #while 1 <= 0
        print('{} - '.format(termo), end='')
        termo = termo + razao #2 + 2 = 4 + 2 = 6 + 2 = 8
        c += 1 #1/ 1 + 1 = (2) / 2 + 1 = (3) / 3 + 1 = (4)
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais? '))
print('PA finalizada com {} termos motrados'.format(total))
print('FIM')