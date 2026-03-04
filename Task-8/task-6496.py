from itertools import product

alph = sorted('БЕРСК')
cnt = 0
for pos, val in enumerate(product(alph, repeat=5), start=1):
    cnt += 1
for pos, val in enumerate(product(alph, repeat=6), start=1):
    cnt += 1
for pos, val in enumerate(product(alph, repeat=7), start=1):
    cnt += 1
print(cnt)
