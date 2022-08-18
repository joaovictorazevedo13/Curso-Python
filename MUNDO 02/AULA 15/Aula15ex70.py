total = menor = quantidade = cont = 0
barato = ' '
while True:
    produto = str(input('Nome do Produto: '))
    preco = float(input('Preço do produto em R$:'))
    cont = cont + 1
    resp = ' '
    total = total + preco
    if preco > 1000:
        quantidade += 1
    if cont == 1: #tambem pode usar OR
        menor = preco
        barato = produto
    else:
        if preco < menor:
            menor = preco
            barato = produto
    while resp not in 'SN':
        resp = str(input('Deseja continuar? [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break

print(f'O gasto total de produto é igual R${total}\n'
      f'Foram comprados {quantidade} produtos acima de R$1000\n'
      f'O produto {barato} é o mais barato e custa R${menor:.2f}')