lista = ('Agua', 'Banana', 'Caneca', 'Dado', 'Elefante', 'Formiga', 'Geleia', 'Helicoptero')
for palavras in range(0, len(lista)):
    print(f'\nNa palavra {lista[palavras]} temos as vogais: ', end='')
    for letra in lista[palavras]:
        if letra.upper() in 'AEIOU':
            print(f'{letra}', end='')

