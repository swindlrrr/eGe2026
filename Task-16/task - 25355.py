from sys import setrecursionlimit
def F(n):
    if n >= 19: return F(n-4) + 3580
    return 6 * (G(n-7) - 36)
def G(n):
    if n >= 248045: return n / 20 + 28
    return G(n + 9) - 4
setrecursionlimit(10000000)
print(F(673))