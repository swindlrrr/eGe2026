from itertools import product
cnt = 0
for a, b, c in product(range(16), repeat=3):
    if b > a > c and a + b + c <= 15:
        cnt += 1
print(cnt)