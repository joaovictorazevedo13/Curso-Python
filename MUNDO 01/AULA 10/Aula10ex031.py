km = float(input('Digite a distância da viagem em km: '))
if km < 200:
    print('O valor da passagem é de R$:{:.2f}'.format(km*0.50))
else:
    print('O valor da passagem é de R$:{:.2f}'.format(km*0.45))