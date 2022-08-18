ano = int(input('Digite o ano para saber se é bissexto: '))
div4 = ano % 4
div100 = ano % 100
div400 = ano % 400

if div4 == 0 and div100 != 0 or div400 == 0:
    print('O ano de {} é bissexto'.format(ano))
else:
    print('O ano de {} NÃO é bissexto'.format(ano))