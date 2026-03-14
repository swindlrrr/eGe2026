from string import printable
from itertools import product

cnt = 0
for val in product(printable[:7], repeat = 6):
    val = ''.join(val)
    if val[0] != '0' and val[-1] >= '4' and sum(val.count(i) for i in printable[:7:2]) == sum(val.count(i) for i in printable[1:7:2]):
            cnt += 1
print(cnt)
