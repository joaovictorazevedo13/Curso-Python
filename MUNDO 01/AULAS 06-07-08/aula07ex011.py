print('\nQUANTIDADE DE TINTA NECESSÁRIA PARA PINTAR UMA PAREDE\n')
alt = float(input('Altura da parede em metros: '))
larg = float(input('Largura da parede em metros: '))
area = (alt*larg)
tinta = (area/2)

print(('Área da Parede: {}m²\nQuantidade de tinta: {}L').format(area, tinta))