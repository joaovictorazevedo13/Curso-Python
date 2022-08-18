print('Condição do seu carro\n')
tempo = int(input('Quantos anos tem seu carro: '))

if tempo<=3:
    print('Seu carro é novo!')
else:
    print('Já está na hora de trocar...\n')
print('Até mais! :)')
#OUTRA FORMA
tempo = int(input('Quantos anos tem seu carro: '))

print('carro novo' if tempo<=3 else 'carro velho')
print('---FIM---')