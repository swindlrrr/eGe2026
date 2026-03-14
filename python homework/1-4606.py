from itertools import permutations
graph ='CE EG GF FA AC CD DH HE BF BA'.split()
matrix ='68 47 45 237 368 15 248 257'.split()

print(*range(1,9))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)