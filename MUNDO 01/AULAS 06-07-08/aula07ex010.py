real = float(input('Quantidade de dinheiro em Real: R$'))
dolar = 4.82
cambio = real/dolar

print(('Você pode comprar em dolar: U${:.2f}').format(cambio))