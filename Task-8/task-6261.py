from string import printable
from itertools import product
cnt = 0
for val in product(printable[:8], repeat = 10):
    val = ''.join(val)
    if val[0] != '0' and val.count('7') == 5:
        for i in val:
            if int(i, 8) % 2 !=0 and i != '7':
                val = val.replace(i, '*')
        if '*7' not in val and '7*' not in val and '77' not in val:
            cnt += 1
print(cnt)