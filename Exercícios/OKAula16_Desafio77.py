# Contador de vogais #

palavras = ('escola', 'lingua', 'boca', 'casa', 'livros', 'computador', 'escova', 'mesa', 'mouse', 'monitor')


def teste_vogais(palavra):
    vogais = []
    a = f'{palavra}'.find('a')
    if a >= 0:
        vogais.append('a')
    e = f'{palavra}'.find('e')
    if e >= 0:
        vogais.append('e')
    i = f'{palavra}'.find('i')
    if i >= 0:
        vogais.append('i')
    o = f'{palavra}'.find('o')
    if o >= 0:
        vogais.append('o')
    u = f'{palavra}'. find('u')
    if u >= 0:
        vogais.append('u')
    print(f'{palavra.upper()} tem as vogais {vogais}')


teste_vogais(palavras[0])
teste_vogais(palavras[1])
teste_vogais(palavras[2])
teste_vogais(palavras[3])
teste_vogais(palavras[4])
teste_vogais(palavras[5])
teste_vogais(palavras[6])
teste_vogais(palavras[7])
teste_vogais(palavras[8])
teste_vogais(palavras[9])
