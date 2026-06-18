
from itertools import *

ans = []
alph = sorted('АРГУМЕНТ')

for pos, val in enumerate(product(alph, repeat=4), start=1):
    val = ''.join(val)
    val1 = ''.join(sorted(val))
    if len(val) == len(set(val)) and val == val1:
        ans.append(pos)
print(max(ans))

