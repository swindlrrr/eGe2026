from string import printable
from itertools import product

ans = []
alph = sorted('СЕНТЯБРЬ')
for pos, val in enumerate(product(alph, repeat = 5), start = 1):
    val = ''.join(val)
    if pos % 2 ==0 and val[0] == 'Р' and 'Ь' not in val:
        ans.append(pos)
print(max(ans))