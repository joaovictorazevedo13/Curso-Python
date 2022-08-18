jogador = dict()
partidas = list()
time = list()
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f"Quantas partidas {jogador['nome']} jogou? "))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Gols partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        continuar = str(input('Deseja continuar?[S/N]')).upper()[0]
        if continuar in 'SN':
            break
        print('Erro. Responda apenas com S ou N.')
    if continuar == 'N':
        break
print('nº', end=' ')
for e in jogador.keys(): #apenas usar as chaves(nome, gols e total)
    print(f'{e:<15}', end='')
print()
print('--' * 30)
for k, v in enumerate(time):
    print(f"{k:<3}", end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('--' * 30)
while True:
    opc = int(input('Mostrar dados de qual jogador?[999 interrompe]: '))
    if opc == 999:
        break
    if opc >= len(time):
        print(f"ERRO. Nao existe jogador com o codigo {opc}!")
    else:
        print(f"Levantamento do jogador {time[opc]['nome']}:")
        for i, g in enumerate(time[opc]['gols']):
            print(f"                ==> No jogo {i} fez {g} gols.")
        print()
