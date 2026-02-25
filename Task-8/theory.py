from itertools import product

# product - создает все комбинации определенной длины
# enumerate - нумерует все элементы последовательности

# 17549
ans = []
alph = sorted('ФОКУС')

for pos, val in enumerate(product(alph, repeat = 5), start = 1):
    val = ''.join(val)
    if val.count('Ф') == 0 and 'Ф' not in val and val.count('У') == 2:
        ans.append(pos)
print(max(ans))
