from datetime import date
dados = dict()
lista = list()
anoatual = (date.today().year)
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de Nascimento: '))
idade = anoatual - nasc
dados['idade'.upper()] = idade
dados['ctps'.upper()] = int(input('Digite o nº da CTPS: '))
if dados['ctps'.upper()] == 0:
    print(f"{dados['nome']} não possui CTPS")
else:
    dados['ano de contratacao'.upper()] = int(input('Ano de Contratação: '))
    dados['salario'.upper()] = float(input('Salário em R$: '))
    anoapos = dados['ano de contratacao'.upper()] + 35
    idadeapos = anoapos - nasc
    dados['idade da aposentadoria'.upper()] = idadeapos
    lista.append(dados.copy())
    for k, v in dados.items():
        print(f'{k}: {v}')
    print()
