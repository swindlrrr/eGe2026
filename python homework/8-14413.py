from itertools import permutations
cnt = 0
for val in set(permutations('СОРТИРОВКА', r=10)):
    val = ''.join(val)
    t = val
    for c in 'ОИА':
        t = t.replace(c, '0')
    for c in 'СРТВК':
        t = t.replace(c, '1')
    if '000' not in t and '111' not in t:
        cnt += 1
print(cnt)