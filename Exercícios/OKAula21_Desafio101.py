#Votação
# Função
def voto(nasc):
    import datetime
    data_atual = datetime.datetime.now()
    idade = data_atual.year - nasc
    if 16 <= idade < 18 or 65 <= idade:
        return print(f'Com {idade} anos: VOTO OPCIONAL')
    elif 18 <= idade < 65:
        return print(f'Com {idade} anos: VOTO OBRIGATÓRIO')
    else:
        return print(f'Com {idade} anos: VOTO NEGADO')


# Programa principal
voto(int(input(f'Ano de nascimento:')))
