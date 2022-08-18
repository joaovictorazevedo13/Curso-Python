estado = dict() #or{}
brasil = list() #or[]
for c in range(0 , 2):
    estado['uf'] = str(input('Unidade Federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print('---' * 30)
for e in brasil:
    for k, v in e.items(): #para keys e values na lista brasil:
        print(f'O campo {k} tem valor {v}')
print('---' * 30)
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()