co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
hip = (co ** 2 + ca **2) ** (1/2)

print(('Hipotenusa: {:.2f}').format(hip))