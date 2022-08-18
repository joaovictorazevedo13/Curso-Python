nome = str(input('Digite seu nome: ')).strip()

print("Upper: {}".format(nome.upper()))
print('Lower: {}'.format(nome.lower()))
print('Letras ao todo: {}'.format((len(nome) - nome.count(' '))))
#print('Primeiro nome tem: {}'.format(nome.find(' ')))
separa = nome.split()
print('Primeiro nome é {} e a quantidade de letras é {}'.format(separa[0], len(separa[0])))