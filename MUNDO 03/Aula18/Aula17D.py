galera = list()
dado = list()
for cont in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear() #exlcuir dados, senao ficara duplicado, ja foi feito uma copia
for pessoa in galera:
    print(f'{pessoa[0]} tem {pessoa[1]} anos')

