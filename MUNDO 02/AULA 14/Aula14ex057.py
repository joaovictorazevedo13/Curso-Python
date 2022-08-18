sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados invalidados. Digite novamente o seu sexo [M/F]: ')).strip().upper()[0]
print('Dados registrados com sucesso')
