valores = list()
for cont in range(0, 5):
    n = int(input(f'Digite um valor {cont}: '))
    if cont == 0 or n > valores[-1]:
        valores.append(n)
        print(f'Valor adicionado ao fim da lista')
    else:
        pos = 0
        while pos < len(valores):#cont - 5
            if n <= valores[pos]:#n <= 1 ate 5[0]
                valores.insert(pos, n)
                break
            pos = pos + 1
            print('Valor adicionado ao começo da lista')
print('=-=' * 30)
for posicao, num in enumerate(valores):
    print(f'Valor {num} digitado na posição {posicao}')
print(f'valores digitados: {valores}')