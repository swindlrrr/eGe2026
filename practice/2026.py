#8
from itertools import *
from string import printable
cnt = 0
alph = printable[:9]
for val in product(alph, repeat = 5):
    val = ''.join(val)
    if val[0] != '0' and val.count('3') == 2:
        for i in printable[1:9:2]:
            val = val.replace(i, '*')
        if '*2' not in val and '2*' not in val:
            cnt += 1
print(cnt)

