idade = int(input('Digite a idade do atleta para saber a categoria de acordo com a idade: '))
if idade <= 9:
    print('A categoria do atleta com {} anos é: Mirim'.format(idade))
elif idade <= 14:
    print('A categoria do atleta com {} anos é: Infantil'.format(idade))
elif idade <= 19:
    print('A categoria do atleta com {} anos é: Junior'.format(idade))
elif idade <= 12:
    print('A categoria do atleta com {} anos é: Sênior'.format(idade))
else:
    print('A categoria do atleta com {} anos é: Master'.format(idade))
