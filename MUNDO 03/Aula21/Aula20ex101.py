from datetime import date
atual = date.today().year


def voto(ano=0):
    while True:
        ano = int(input('Ano de nascimento: '))
        idade = atual - ano
        if 65 > idade >= 18:
            print(f'Com {idade} anos o voto é OBRIGATÓRIO.')
        else:
            if 16 <= idade < 18 or n >= 65:
                print(f'Com {idade} anos o voto é OPCIONAL.')
            if 65 > idade < 16:
                print(f'Com {idade} anos o voto NÃO É OBRIGATÓRIO.')
        resp = str(input('Deseja continuar? [S/N] '))
        if resp == 'N':
            break


voto()
