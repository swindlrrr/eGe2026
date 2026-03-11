from itertools import product
cnt = 0
for val in sorted(product('АПРУС', repeat=5)):
    val = ''.join(val)
    cnt += 1
    if val[0] == 'У' and val.count('А') == 2 and 'АА' not in val:
        print(cnt)
        break