from itertools import  product
cnt = 0
for val in product([val for val in range(20)],repeat = 5):
    if val[0] != 0 and all(val[o] % 2 != val[o+1] % 2 for o in range(4)) and (val[0]+val[-1]) == 26:
        cnt += 1
print(cnt)