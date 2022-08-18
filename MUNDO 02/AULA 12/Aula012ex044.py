valor = float(input('valor do produto:R$'))
print('\nPagamento:')
pagamento = int(input('Digite 1 - À vista com 10% no dinheiro.\n'
                      'Digite 2 - Á vista no cartão.\n'
                      'Digite 3 - Em ate 2x no cartão\n'
                      'Digite 4 - Para a partir de 3x\n'
                      '\033[4mDigite a opção aqui:\033[m'))
car2x = valor / 2
car3x = ((valor + (valor * 0.20)) / 3)
if pagamento == 1:
    print('O valor à vista no dinheiro: R${:.2f}'.format(valor - (valor * 0.10)))
elif pagamento == 2:
    print('O valor à vista no cartão: R${:.2f}'.format(valor - (valor * 0.05)))
elif pagamento == 3:
    print('Em 2x de R${:.2f}: R${:.2f}'.format(car2x, valor ))
else:
    numparc = float(input('Numero de parcelas: '))
    parcela = ((valor + (valor * 0.20)) / numparc)
    print('Em {:.0f}x de R${:.2f}: R${:.2f}'.format(numparc, parcela, parcela * numparc))
