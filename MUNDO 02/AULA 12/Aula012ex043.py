print('CALCULADORA IMC\n')
peso = float(input('Digite o seu peso em Kg: '))
altura = float(input('Digite o sua altura em m(ex. 1.80m): '))
imc = (peso / (altura ** 2))
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 < imc < 25:
    print('Peso Ideal')
elif 25 < imc < 30:
    print('Sobrepeso')
elif 30 < imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
