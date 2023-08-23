# Validando entrada de dados em python
def leia_int(comando):
    num = str(input(comando))
    while True:
        if num.isnumeric():
            break
        else:
            print(f'\033[91mERRO!Você digitou um valor inválido.\033[m')
            num = str(input(comando))
    return num


# Programa principal
n = leia_int('Digite um valor inteiro:')
print(f'Você digitou o número {n}.')
