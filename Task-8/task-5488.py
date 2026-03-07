from string import printable
from itertools import product

cnt = 0
alph = 'ПОЛИНА'
for pos, val in enumerate(product(alph, repeat = 8), start = 1):
    val = ''.join(val)
    if sum(val.count(i) for i in 'ПЛН') > sum(val.count(g) for g in 'ОИА'):
        cnt += 1
print(cnt)