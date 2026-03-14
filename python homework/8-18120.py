from itertools import product
cnt = 0
for pos, val in enumerate(product('ЕЛОПРСТ', repeat=5), start = 1):
    val = ''.join(val)
    if pos % 2 == 1 and val[-1] in 'ЕО' and sum(val.count(c) for c in 'ЛПРСТ') <= 3:
        cnt += 1
print(cnt)

