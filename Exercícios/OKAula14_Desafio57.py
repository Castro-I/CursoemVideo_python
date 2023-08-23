# Validação de dados
print('Olá, usuário!')
sexo = str(input('Por favor, digite seu sexo:')).strip().upper()[0]
while sexo not in 'MmFf':
    print('Opção inválida.')
    sexo = str(input('Por favor, digite novamente:')).strip().upper()[0]
print('Sexo cadastrado.')
