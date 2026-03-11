from itertools import product
from string import printable

cnt = 0
for val in product(printable[:12].upper(), repeat=7):
    if val[0] != '0':
        val = ''.join(val)
        if val.count('B') == 2:
            t = val
            for c in '02468A':
                t = t.replace(c, '2')
            for c in '13579B':
                t = t.replace(c, '1')
            if '11' not in t and '22' not in t:
                cnt += 1
print(cnt)