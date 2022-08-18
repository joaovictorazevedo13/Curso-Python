tempc = float(input('Temperatura em ºC: '))
tempf = ((tempc*9/5)+32)
tempk = (tempc+273.15)

print(('Temperatura em Fahrenheit: {:.2f}ºF\nTemperatura em Kelvin: {:.2f}ºK').format(tempf, tempk))
