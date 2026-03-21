from functools import lru_cache


@lru_cache(None)
def G(n):
    if n <= 9: return 3 * n
    if n > 9: return G(n - 4) + 2
def F(n):
    return G(n-1) + G(n-3)
for i in range(1, 43000):
    F(i)
print(F(42999))