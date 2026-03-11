from itertools import product
cnt = 0
a = set(product('КОНЕЦ', repeat=5))
b = set(product('ДРАКОН', repeat=5))
cnt = len(a ^ b)
print(cnt)