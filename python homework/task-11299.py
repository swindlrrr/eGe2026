from itertools import product
from string import printable
ans = []

alph = sorted('БМЮРН')
for pos, val in enumerate(product(alph, repeat = 6), start = 1):
    val = ''.join(val)
    if pos % 2 != 0 and val[0] != 'М' and 'Ю' not in val and val.count('Р') >= 2:
        ans.append(pos)
print(max(ans))