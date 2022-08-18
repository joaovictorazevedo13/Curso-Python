teste = list()
teste.append('Joao')
teste.append(24)
galera = list()
galera.append(teste[:])  # [:] - copia
teste[0] = 'Rafa' #substituindo 'Joao'
teste[1] = 22 #substituindo '24'
galera.append(teste[:]) # [:] - copia
print(galera)