from itertools import product
ans = []

alph = sorted('МАНГУСТ')
for pos, val in enumerate(product(alph, repeat = 6), start = 1):
    val = ''.join(val)
    if val[0] != 'У' and val.count('М') == 2 and val.count('Г') <= 1:
        ans.append(pos)
print(max(ans))