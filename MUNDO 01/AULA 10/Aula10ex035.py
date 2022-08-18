print('POSSIBILIDADE DE UM TRIANGULO A PARTIR DE 3 RETAS\n')
r1 = float(input('Reta 1: '))
r2 = float(input('Reta 2: '))
r3 = float(input('Reta 3: '))
if (r1 < (r2 + r3)) and (r2 < (r1 + r3)) and (r3 < (r1 + r2)):
    print('É POSSIVEL FORMAR UM TRIANGULO')
else:
    print("NAO E POSSIVEL FORMAR UM TRIANGULO")