pilha = list()
expresssao = str(input('Digite expressao: ')).upper().strip()
for simb in expresssao:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            break
if len(pilha) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')
