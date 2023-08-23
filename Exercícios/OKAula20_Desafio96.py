#Função
def calc(larg, comp):
    a = larg * comp
    print(f' A aréa do teu terreno é de {a:.1f}m quadrados.')


#Programa principal
l = float(input('Largura(m):'))
c = float(input('Comprimento(m):'))
calc(l, c)
