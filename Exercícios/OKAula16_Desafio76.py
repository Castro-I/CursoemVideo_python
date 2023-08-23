# Lista de preços #

produtos = (
    'Monitor', 1399.99, 'Processador', 1129.99, 'Mémoria', 259.99,
    'Placa-mãe', 949.99, 'Fonte', 339.99, 'Placa Gráfica',
    2399.99, 'Gabinete', 229.99, 'Mouse', 99.99, 'Teclado', 179.99)


def print_produtos(produto, valor):
    print('{:.<48} R$  {:>4.2f}'.format(produto, valor))


print('_' * 60)
print('TABELA DE PREÇOS'.center(60))
print('_' * 60)
print_produtos(produtos[0], produtos[1])
print_produtos(produtos[2], produtos[3])
print_produtos(produtos[4], produtos[5])
print_produtos(produtos[6], produtos[7])
print_produtos(produtos[8], produtos[9])
print_produtos(produtos[10], produtos[11])
print_produtos(produtos[12], produtos[13])
print_produtos(produtos[14], produtos[15])
print_produtos(produtos[16], produtos[17])
print('_' * 60)
