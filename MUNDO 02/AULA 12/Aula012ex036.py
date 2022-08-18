print('EMRESTIMO BANCARIO')
print('-=-' * 7)
casa = float(input('Valor da casa: '))
sal = float(input('Salário: '))
anos = float(input('Deseja pagar em quantos anos? '))
parc = ((casa / anos) / 12)
sal30 = sal * 0.30

if parc > sal30:
    print('Emprestimo negado!')
else:
    print('Emprestimo Aprovado')

