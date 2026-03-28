from sys import setrecursionlimit
def F(n):
    if n <= 10: return n
    return n-7 + F(n - 21)
setrecursionlimit(190000)
print((F(185734) - F(185650))/F(40))