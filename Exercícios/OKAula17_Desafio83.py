# Validação de expressões

ex = list(str(input('Digite a espressão:')))
if ex.count('(') == ex.count(')'):
    print('A expressão está correta.')
else:
    print('A expressão está incorreta.')
