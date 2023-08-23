#Boletim com listas compostas
dados = list()
while True:
    nome = str(input('Nome:'))
    n1 = float(input('Nota 1:'))
    n2 = float(input('Nota 2:'))
    media = ((n1 + n2) / 2)
    dados.append([nome, [n1, n2], media])
    r = str(input('Deseja continuar? [S/N]')).strip().upper()
    if r[0] in 'S':
        continue
    elif r[0] in 'N':
        break
    else:
        print('Resposta inválida.')
        r = str(input('Deseja continuar? [S/N]'))

print('-=' * 10, 'BOLETIM', '=-' * 10)
print(f'{"No.":<4}{"NOME":^10}{"MÉDIA":>8}')
print('-' * 26)
for pos, a in enumerate(dados):
    print(f'{pos:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    r = int(input('Deseja mostrar as notas de qual aluno? (999 interrompe)'))
    if r == 999:
        print('FIM.')
        break
    if r <= len(dados) - 1:
        print(f'Notas de {dados[r][0]}: {dados[r][1]}')
        print('-' * 20)
print('Volte sempre.')
