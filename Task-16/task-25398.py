from sys import setrecursionlimit
def G(n):
    if n < 221337: return G(n+11) - 48
    if n >= 221337: return 2 * n + 50
def F(n):
    if n > 30: return F(n-6) + 2048
    if n <= 30: return 3 * (G(n-5)+13)
setrecursionlimit(1000_000)
print(F(5078))