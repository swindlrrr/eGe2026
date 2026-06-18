# ans = []
#
# for N in range(1,1000):
#     R = bin(N)[2:]
#     R = R + str((R.count('1')%2))
#     R = R + str((R.count('1')%2))
#     R = int(R,2)
#     if R > 123:
#         ans.append(R)
# print(min(ans))

from itertools import *
from string import printable

cnt = 0
alph = printable[:14]
for pos, val in enumerate(product(alph, repeat=5), start=1):
    val = ''.join(val)
    if val[0] != '0' and val.count('9') == 1 and (val.count(i) <= 3 for i in printable[11:14]):
        cnt += 1
print(cnt)
