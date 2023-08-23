try:
    a = int(input('Numerador:'))
    b = int(input('Divisor:'))
    r = a / b
except (ValueError, TypeError):
    print('Houve um problema com os dados recebidos.')
except ZeroDivisionError:
    print('Essa divisão não é possível.')
except Exception as erro:
    print(f'Problema encontrado: {erro.__cause__}')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre!')
