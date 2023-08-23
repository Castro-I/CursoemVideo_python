# TUPLES "()" #
# Tuples são imutavéis
lanche = ('hámburger', 'suco', 'pizza', 'pudim')
print(len(lanche))
print(lanche)
print(lanche[0])
print(lanche[0:3])
print(lanche[0:])
print(lanche[:2])
print(lanche[0::2])
print(lanche[-1])
print(lanche[-1:])
print(sorted(lanche)) # Print em oredem alfabética #

for c in lanche:
    if c == 'suco':
        print(f'eu vou beber {c}.')
    elif c == 'pizza':
        continue
    else:
        print(f'eu vou comer {c}.')
if len(lanche) > 2:
    print('comi demais!')

janta = ('arroz', 'feijão', 'salada', 'bife')

for c in janta:
    if len(lanche) > 2:
        print('comi demais no lanche, acho que não jantarei.')
        break
    else:
        print(f'jantarei {c}.')

for pos, comida in enumerate(janta):
    print(f'Comida: {comida} na posição {pos}.')

a = (2, 4, 3)
b = (1, 3, 6, 9)
c = a + b
d = b + a
print(c)
print(d)
print(c.count(3))
print(c.index(6))

pessoa = ('Ícaro', 23, 'M', 67.5)
print(pessoa)
del pessoa
print(pessoa)
