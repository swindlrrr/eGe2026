from functools import lru_cache
@lru_cache(None)
def G(n):
    if n <= 9: return 3 * n
    if n > 9: return G(n-2) + 1
def F(n):
    return G(n-1)
for i in range(1, 47996):
    F(i)
print(F(47995))