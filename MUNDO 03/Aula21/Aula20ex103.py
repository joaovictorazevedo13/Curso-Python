def ficha(jogador='<<Desconhecido>>', gol=0):
    print(f'{jogador} fez {gol} gols.')


nome = str(input('Nome do jogador: '))
gols = str(input('Gols marcados: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gol = 0
if nome.strip() == '':
    ficha(gol=gols)
else:
    ficha(nome, gols)
