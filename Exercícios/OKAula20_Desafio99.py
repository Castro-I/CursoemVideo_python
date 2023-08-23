from time import sleep


# função
def maior(* numeros):
    lista_num = list()
    for valor in numeros:
        lista_num.append(valor)

    print('Analisando os valores:...')
    sleep(2)
    for x in lista_num:
        print(x, end=' ')
        sleep(0.3)
    if len(lista_num) > 0:
        print(f'\n{len(lista_num)} valores foram digitados.')
        print(f'o maior entre eles é: {max(lista_num)}')
        print('~' * 40)
    else:
        print('Nenhum valor foi digitado.')
        print('portanto a análise não é possível.')
        print('~' * 40)


# Programa principal
maior(1, 3, 4, 9, 12)
maior(3, 45, 78, 9)
maior(4, 7, 9, 10)
maior(3, 7)
maior()
