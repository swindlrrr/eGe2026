from sys import setrecursionlimit
def F(n):
    if n >= 2025: return n
    else: return F(n+1) - F(n+2) + 7
setrecursionlimit(10**4)
print(F(15)-F(24))