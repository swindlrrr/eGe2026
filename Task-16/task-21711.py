from sys import setrecursionlimit

def F(n):
    if n < 20: return n
    if n >= 20: return (n - 6) * F(n - 7)

setrecursionlimit(100000000)
print((F(47872) - 290*F(47865))/F(47858))
