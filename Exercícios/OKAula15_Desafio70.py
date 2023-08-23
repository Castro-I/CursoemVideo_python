#  LEITOR DE COMPRAS
compra = []
Mbarato = Mmil = total = cont = 0
barato = ''
while True:
    prod = str(input('Nome do produto:'))
    valor = float(input('Preço: R$'))
    cont += 1
    if 1000 <= valor:
        Mmil += 1
    if cont == 1 or valor < Mbarato:
        Mbarato = valor
        barato = prod
    total += valor
    res = str(input('Deseja continuar?')).upper().strip()
    compra.append(prod)
    while res not in 'SIMNAONÃO':
        print('Respota inválida. Digite novamente.')
        res = str(input('Deseja continuar?')).upper().strip()
    if res not in 'SIM':
        break
print(f'A lista de compra ficou assim:\n{compra}')
print(f'O total da compra é de R$ {total:.2f}.')
if Mmil >= 1:
    print(f'{Mmil} produtos valem mais que R$ 1000,00.')
print(f'O produto mais barato é {barato}, que custa R$ {Mbarato:.2f}.')
