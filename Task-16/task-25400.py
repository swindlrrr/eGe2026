from sys import setrecursionlimit
def G(n):
    if n < 28: return 3 * n - 4
    if n >= 28: return G(n - 5) - 15
def F(n):
    if n < 31054: return F(n + 4) + 3020
    if n >= 31054: return 3 * (G(n - 2) - 15)
setrecursionlimit(31055)
print(F(15))