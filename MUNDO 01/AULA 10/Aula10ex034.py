salario = float(input('Digite o salario do funcionario para receber o aumento: '))
if salario >= 1250:
    print('Novo salário: R${:.2f}'.format(salario+(salario*0.10)))
else:
    print('Novo salário: R${:.2f}'.format(salario+(salario*0.15)))
