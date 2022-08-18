pessoa = dict()
galera = list()
soma = media = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo?[M/F] ')).upper()[0]
        if pessoa['sexo'] in 'MF': #Validação
            break
        print('Erro. Utilize apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma = soma + pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        cont = str(input('Deseja continuar?[S/N]')).upper()[0]
        if cont in 'SN': #validação
            break
        print('Erro. Utilize apenas S ou N')
    if cont == 'N':
        break
print('-=' * 30) #------------------------------------------------
print(f"Ao todo temos {len(galera)} pessoas cadastradas.")
media = (soma / len(galera))
print(f'A media de idade das pessoas é igual a {media}')
print(f'Lista de mulheres cadastradas:')
for p in galera:
    if p['sexo'] == 'F':
        print(f"- {p['nome']}")
print('Pessoas com idade acima da média:')
for i in galera:
    if i['idade'] > media:
        for k, v in i.items():
            print(f"{k} = {v}", end='; ')
        print()
