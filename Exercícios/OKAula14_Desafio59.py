# Recebendo os valores
from time import sleep
num1 = int(input('Digite um número:'))
num2 = int(input('Digite outro número:'))
# Criar o menu
menu = '''MENU
[1] - SOMA
[2] - MULTIPLICAÇÃO
[3] - MAIOR
[4] - NOVOS NÚMEROS
[5] - SAIR'''
print(menu)
op = int(input('Qual operação deseja realizar:'))
# Operações
while op != 5:
    if op not in range(1, 5):
        op = int(input('Opção invávlida. Digite a opção desejada:'))
        print(menu)
    else:
        if op == 1:
            print('O resultado de {} + {} é {}'.format(num1, num2, (num1 + num2)))
        elif op == 2:
            print('O resultado de {} x {} é {}'.format(num1, num2, (num1 * num2)))
        elif op == 3:
            if num1 > num2:
                print('O maior número é {}.'.format(num1))
            elif num1 == num2:
                print('Os dois números são iguais.')
            else:
                print('O maior número é {}.'.format(num2))
        elif op == 4:
            num1 = int(input('Digite o novo número:'))
            num2 = int(input('Digite um novo número:'))
        print('=-=' * 10)
        sleep(1)
        print(menu)
        op = int(input('Deseja realizar outra operação?'))
print('FIM')
