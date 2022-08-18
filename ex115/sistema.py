from ex115.lib.interface import *
from ex115.lib.arquivo import *

arq = 'joao.txt'

if not arquivoExiste(arq):
    print('Arquivo inexistente')
    criarArquivo(arq)


while True:
    resposta = menu(['Listar Pessoass', 'Cadastrar Pessoas', 'Sair do Sistema'])
    if resposta == 1:
        print('opção 1')
        lerArquivo(arq)

    elif resposta == 2:
        print('opção 2')

    elif resposta == 3:
        cabecalho('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mErro. Opção inválida\033[m')