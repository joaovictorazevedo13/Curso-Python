from datetime import date
print('\033[30;42mALISTAMENTO\033[m \033[m\033[30;42mMILITAR\033[m\n')
nome = str(input('Digite seu nome: '))
data = int(input('Digite seu ano de nascimento: '))
atual = date.today().year
idade = atual - data
if idade < 18:
    print('{}, você se alistará daqui {} ano(s)'.format(nome, (18 - idade)))
elif idade > 18:
    print('{}, se ainda não se alistou, você esta atrasado em {} ano(s)'.format(nome, (idade - 18)))
else:
    print('{}, se você ainda não se alistou, aliste-se ainda este ano.'.format(nome))
