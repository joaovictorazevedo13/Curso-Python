dic = dict()
gollista = list()
dic['nome'] = str(input('Nome: '))
partidas = int(input('Numero de partidas jogadas: '))
for c in range(0, partidas):
    gol = int(input(f'Numero de gols partida {c+1}: '))
    gollista.append(gol)
dic['gols'] = gollista
dic['total'] = sum(gollista)
gollista = [dic.copy()]
print('-=' * 30) #---------------------------------------------------------------------
print(f"O jogador {dic['nome']} jogou {partidas} partidas")
total = 0
for v in dic['gols']:
    total += 1
    print(f"=>> Na partida {total}, marcou {v} gols.")
print(f"==> No total foram {dic['total']} gols")