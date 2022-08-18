dic = dict()
lista = list()
dic['Aluno:'] = str(input('Nome do aluno: '))
dic['Media:'] = float(input('Media do aluno: '))
if dic['Media:'] >= 6:
    dic['Situação:'] = 'Aprovado'
else:
    dic['Situação:'] = 'Reprovado'
lista.append(dic.copy())
for k, v in dic.items():
    print(f'{k} {v}')
print()