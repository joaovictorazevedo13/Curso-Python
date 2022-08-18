def moeda(x=0, moedas='R$'):
    return f"{moedas}{x:.2f}".replace('.', ',')



def aumentar(x=0, taxa=0, formato=False):
    mais10 = x + (x * taxa / 100)
    return mais10 if formato == False else moeda(mais10)


def diminuir(x=0, taxa=0, formato=False):
    menos10 = x - (x * taxa / 100)
    return menos10 if formato == False else moeda(menos10)


def dobro(x=0):
    dobro2 = x * 2
    return dobro2


def metade(x=0, formato=False):
    metade2 = x / 2
    return metade if formato == False else moeda(metade2)


def lin():
    print('=' * 30)


def resumo(x=0, taxaa=10, taxar=5):
    dados = dict()
    lin()
    print('RESUMO DO VALOR'.center(30))
    lin()
    dados['Preço analisado: \t'] = moeda(x)
    dados['Dobro do preço: \t'] = moeda(dobro(x))
    dados['Metade do preço: \t'] = metade(x, True)
    dados[f'{taxaa}% de aumento: \t'] = aumentar(x, taxaa, True)
    dados[f'{taxar}% de redução: \t'] = diminuir(x, taxar, True)
    for k, v in dados.items():
        print(f"{k} {v.rjust(6)}")
    lin()


