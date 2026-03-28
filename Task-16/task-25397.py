from functools import lru_cache
@lru_cache(None)
def G(n):
    if n < 301208: return G(n+7)-21
    if n >=301208: return 10 * n + 50
def F(n):
    if n > 40 : return F(n-4) + 3020
    if n <= 40: return 3 * (G(n-2) -15 )
for n in range(301208, 38, -1): G(n)
for n in range(41, 2027): F(n)
print(F(2026))