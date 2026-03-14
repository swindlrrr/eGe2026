from itertools import permutations

graph = 'AE AD DC CF FG GE HG HA HB BC BD'.split()
matrix = '346 348 12 127 678 15 458 257'.split()
for i in permutations('GAEHCFBD'):
    if all(str(i.index(x) + 1) in matrix[i.index(y)] for x, y in graph):
        print(*i)