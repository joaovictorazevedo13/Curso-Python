from datetime import date
atual = date.today().year
soma = 0
maior = 0
nomevelho = ''
menos20 = 0
for analise in range(1, 5):
    nome = str(input('Nome da {}ª pessoa: '.format(analise)))
    ano = int(input("Ano de nascimento: "))
    idade = atual - ano
    soma = soma + idade
    media = soma / analise
    sexo = int(input('Sexo:\n'
                     '  [ 1 ] Masculino\n'
                     '  [ 2 ] Feminino\n'
                     '  Opção: '))
    lista = ('', 'Masculino', 'Feminino')
    if analise == 1 and sexo == 1:
        maior = idade
        nomevelho = nome
    elif idade > maior and sexo == 1:
        maior = idade
        nomevelho = nome
    if idade < 20 and sexo == 2:
        menos20 = menos20 + 1
#print("{} tem {} anos e é do sexo {}".format(nome, idade, lista[sexo]))
print('A media de idade é igual a {:.0f}'.format(media))
print("O homem mais velho tem {} anos e se chama {}".format(maior, nomevelho))
print('Ao todo são {} mulheres com menos de 20'.format(menos20))
