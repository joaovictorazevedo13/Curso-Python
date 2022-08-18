print('\nALUGUEL DE CARROS\n')
d = int(input('Quantidade de dias alugado: '))
km = float(input('Quantidade de km rodados: '))
dia = d*60
kmr = km*0.15
total = dia+kmr

print(('O total a pagar é igual é de R${:.2f}').format(total))
