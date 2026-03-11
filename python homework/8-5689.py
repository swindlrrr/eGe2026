from itertools import product
cnt = 0
for val in product('01', repeat=16):  # перебираем все 16-значные последовательности из 0 и 1
    val = ''.join(val)
    if val[0] != '0' and val.count('1') % 3 == 0:
        cnt += 1
print(cnt)