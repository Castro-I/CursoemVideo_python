# Cadastro de pessoas
# Criando variavéis
mulher = homem = maiores = total = 0
print('CADASTRO DE PESSOAS')
print('-' * 30)
while True:
    idade = int(input('Idade:'))
    if 18 <= idade:
        maiores += 1
    sexo = str(input('Sexo[M/F]:')).upper().strip()
    while sexo not in 'MF':
        print('Resposta inválida. Digite novamente.')
        sexo = str(input('Sexo[M/F]:')).upper().strip()
    if sexo == 'M':
        homem += 1
    elif sexo == 'F' and idade < 20:
        mulher += 1
    total += 1
    print('-' * 30)
    res = str(input('Deseja continuar?')).upper().strip()
    while res not in 'SIMNAONÃO':
        print('Resposta inválida. Digite novamente.')
        res = str(input('Deseja continuar?')).upper().strip()
    if res in 'SIM':
        print('-' * 30)
    else:
        break
print(f'Ao todo foram cadastradas {total} pessoas.\n{maiores} maiores de 18 anos.')
print(f'{homem} homens foram cadastrados.\n{mulher} mulheres menores que 20 anos.')
