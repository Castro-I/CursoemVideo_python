# Listas

num = [2, 5, 3, 1]
print(f'A lista é {num}')
num[2] = 3
print(f'Toquei o elemento na posição 2 :{num}')
num.append(7)
num.insert(3, 2)
print(f'Adicionei o elemento 7 no fim da lista e adicioneio o elemetno 2 na posição 3:{num}')
num.sort()
print(f'Reorganizei em ordem crescente: {num}')
num.sort(reverse=True)
print(f'Ordem decresceente : {num}')
del num[0]
num.remove(3)  # elimina apenas a primeira ocorrência
num.pop()
num.pop(0)
print(f'Todos os tipos de deeleção: {num}')
print(len(num))

# AULA 18

produtos = [['Processador', 1150], ['placa mãe', 949.99], ['memórias', 500]]
print(produtos[0][0])
print(produtos[0][1])
print(produtos[1][0])
print(produtos[1][1])
print(produtos[2][0])
print(produtos[2][1])
for p in produtos:
    print(f'O produto {p[0]} custa R$ {p[1]:.2f}')

