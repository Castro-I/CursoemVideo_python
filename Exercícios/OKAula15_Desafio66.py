#Ler valores, somar e, no fim, apresentar o resultado:
s = cont = 0
while True:
    n = int(input('Digite um número:'))
    if n == 999:
        break
    s += n
    cont += 1
    print('(Digite 999 se quiser parar.)')
print(f'Você digitou {cont} números e a soma entre eles é igual a {s}.')
