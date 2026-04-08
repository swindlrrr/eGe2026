from sys import setrecursionlimit
def G(n):
    if n < 8: return 3 * n
    if n >= 8: return G(n - 3) + 2

def F(n):
    return 3 * (G(n - 2) + 5)
setrecursionlimit(15000000)
print(F(12345))