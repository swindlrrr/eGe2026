from itertools import *

graph = 'EA AH HB BF FG GE AC CH CF GD ED'.split()
matrix = '247 148 467 123 68 358 13 256'.split()

print(*range(1,9))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
        print(*i)