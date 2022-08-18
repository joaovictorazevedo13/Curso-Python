def dobra(lst):
    pos = 0
    while pos < len(valores):
        lst[pos] = lst[pos] * 2
        pos += 1


valores = []
while True:
    n = int(input('Digite um valor: '))
    valores.append(n)
    while True:
        cont = str(input('Deseja continuar?[S/N] ')).upper()[0]
        if cont in 'SN':
            break
        print('ERRO. Digite apenas S ou N.')
    if cont == 'N':
        break
print(f"Valores: {valores}")
dobra(valores)
print(f"Valores dobrados: {valores}")