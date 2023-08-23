from time import sleep


#Função
def contador(ini, fim, pas):
    print('~' * 40)
    print(f'Contagem de {ini} ao {fim} ao passo de {pas} casas.')

    if fim < ini:
        if pas > 0:
            for x in range(ini, (fim - 1), -pas):
                print(x, end=' ')
                sleep(0.5)
            print('FIM!')
        elif pas < 0:
            for x in range(ini, (fim - 1), +pas):
                print(x, end=' ')
                sleep(0.5)
            print('FIM!')
        elif pas == 0:
            for x in range(ini, (fim - 1), -1):
                print(x, end=' ')
                sleep(0.5)
            print('FIM!')
    elif fim > ini:
        if pas > 0:
            for x in range(ini, (fim + 1), pas):
                print(x, end=' ')
                sleep(0.5)
            print('FIM!')
        elif pas == 0:
            for x in range(ini, (fim + 1), 1):
                print(x, end=' ')
                sleep(0.5)
            print('FIM!')


#Programa principal
print(f'{"CONTADOR AUTOMÁTICO":^40}')
contador(1, 10, 1)
contador(10, 0, 2)
print('~' * 40)
print('Agora é a tua vez de personalizar a contagem.')
i = int(input('Início:'))
f = int(input('Fim:'))
p = int(input('Passo:'))
contador(i, f, p)
