valor = int(input('Qual o valor que voce deseja sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total = total - ced #PARA SUBTRAIR A CELULA ATUAL E IR PARA A PROXIMA
        totced = totced + 1 #PARA CONTAR AS CEDULAS
    else:
        if totced > 0:
            print(f'Total de {totced} cédulas de R${ced}')
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        if total == 0:
            break
print('Volte sempre')
