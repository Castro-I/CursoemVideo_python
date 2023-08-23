#Analisando e gerando dicinonários
def notas(*n, sit=False):
    """
    Função para analisar uma quantidade variada de notas e retornar resultados,apresentando ainda a situação geral da amostra.
    :param n:nota(Aceita várias)
    :param sit:(Opcional) Apresenta a situação geral da amostra.
    :return:Retorna um dicionário com os resultados da análise.
    """
    geral_notas = dict()
    geral_notas['Total'] = len(n)
    geral_notas['Maior nota'] = max(n)
    geral_notas['Menor nota'] = min(n)
    geral_notas['Média'] = sum(n) / len(n)
    if sit:
        if geral_notas['Média'] > 7:
            geral_notas['Situação'] = 'BOA'
        elif geral_notas['Média'] > 5:
            geral_notas['Situação'] = 'RAZOÁVEL'
        else:
            geral_notas['Situação'] = 'RUIM'
    return geral_notas


# Programa principal
resp = notas(5.5, 6, 8.5, 9,  sit=True)
print(resp)
help(notas)
