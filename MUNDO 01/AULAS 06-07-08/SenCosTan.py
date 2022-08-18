from math import sin, cos, tan, radians
ang = float(input('Digite o angulo: '))
sen = sin(radians(ang))
co = cos(radians(ang))
tg = tan(radians(ang))

print('Seno: {:.2f}'.format(sen))
print('Cosseno: {:.2f}'.format(co))
print('Tangente: {:.2f}'.format(tg))