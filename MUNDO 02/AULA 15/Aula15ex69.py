from datetime import date
cont = 0
pessoas = homens = mulheres = 0
while cont != 2:
    print('\nCADASTRE UMA PESSOA\n')
    nome = str(input('Digite o nome da pessoa: '))
    ano = int(input('Ano de nascimento: '))
    sexo = str(input('Sexo? [M/F]')).strip().upper()[0]
    while sexo not in 'MF':
        sexo = str(input('Sexo? [M/F]')).strip().upper()[0]
    anoatual = date.today().year
    idade = anoatual - ano
    cont = int(input('Deseja continuar? [1]SIM/[2]NAO: '))
    if cont == 2:
        break
    if idade > 18:
        pessoas = pessoas + 1
    if sexo in 'M':
        homens = homens + 1
    if sexo in 'F':
        if idade < 20:
            mulheres = mulheres + 1
print(f'{pessoas} pessoas tem mais de 18 anos\n'
      f'{homens} homens foram cadastrados\n'
      f'{mulheres} mulheres cadastradas tem menos de 20 anos')