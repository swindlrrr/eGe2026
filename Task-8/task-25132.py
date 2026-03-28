from itertools import product
cnt = 0
summ = 0
for val in sorted(product('СДАЙЕГЭ', repeat=6)):
    val = ''.join(val)
    cnt += 1
    if 'ЕГЭ' in val:
        summ += cnt
print(summ)
