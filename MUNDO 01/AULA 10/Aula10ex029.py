vel = float(input("Velocidade do carro em km/h: "))
tar = (vel-80)
multa = (tar*7)
if vel > 80:
    print('Você foi multado! E o valor da multa é de R$:{:.2f}'.format(multa))
else:
    print('Dentro da velocidade permitida.')