frase = str(input('Digite um frase: ')).strip(" ")

print('A letra "A" aparece {} vezes na frase.'.format(frase.upper().count('A')))
print('A letra "A" aparece primeiro na posição: {}'.format(frase.upper().find('A')+1))
print('A letra "A" aparece pela ultima vez na posição: {}'.format(frase.upper().rfind('A')+1))