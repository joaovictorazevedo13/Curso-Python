from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoas in range(1, 8):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(pessoas)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Temos {} pessoas maior de idade\nE também temos {} pessoas menor de idade'.format(totmaior, totmenor))
