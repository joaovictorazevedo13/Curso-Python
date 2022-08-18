def notas(* notas, sit=False):
    """
    função para analisar notas e situações de varios alunos.
    :param notas: notas dos aluno
    :param sit: valor opcional para verificar a situação da turma conforme a media
    :return: dicionario com varias informações sobre a turma
    """
    dados = dict()
    dados['qtd de notas'] = len(notas)
    dados['maior nota'] = max(notas)
    dados['menor nota'] = min(notas)
    dados['media'] = sum(notas) / len(notas)
    if sit:
        if dados['media'] >= 6:
            dados['situação'] = 'BOA'
        else:
            dados['situação'] = 'RUIM'
    for k, v in dados.items():
        print(f"{k.upper()}: {v}")
    return dados


notas(2, 5, 6, 7, sit=True)

