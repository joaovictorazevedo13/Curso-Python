def voto(ano):
    from datetime import date
    atual = date.today().year
    idade = atual - ano
    if idade < 16:
        return f'Com {idade} anos o voto NÃO É OBRIGATÓRIO'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos o voto é OPCIONAL.'
    else:
        return f'Com {idade} anos o voto é OBRIGATÓRIO'


nasc = int(input('Digite ano de nascimento: '))
print(voto(nasc))