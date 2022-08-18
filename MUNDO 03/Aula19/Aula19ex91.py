from random import randint
from operator import itemgetter
dic = dict()
lista = list()
print('-=' * 15)
print(f"{'VALORES SORTEADOS':^30}")
print('-=' * 15)
for c in range(0, 5):
    dic[f'Jogador {c+1}'] = randint(0, 6)
for k, v in dic.items():
    print(f"{k} tirou: {v}".center(30))
print('-=' * 15)
print(f"{'RANKING':^30}")
print('-=' * 15)
ranking = sorted(dic.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f"{i+1}º lugar - {v[0]} tirou: {v[1]}".center(30))

