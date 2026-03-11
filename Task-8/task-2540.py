from itertools import product
cnt = 0
for val in sorted(product('АВТОР', repeat=4)):
    val = ''.join(val)
    cnt += 1
    if val == 'ВАТА':
        print(cnt)