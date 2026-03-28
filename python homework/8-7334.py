from itertools import product
cnt = 0
ans = []
for val in sorted(product('МЫСЛЬ', repeat=5)):
    val = ''.join(val)
    cnt += 1
    if val.startswith('ЫЫ'):
        ans.append(cnt)
print(ans[-2])