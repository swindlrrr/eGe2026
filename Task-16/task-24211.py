from sys import setrecursionlimit
def F(n):
    return 3 * (G(n-2) + 5)

def G(n):
    if n < 8: return 3 * n
    return G(n-3)+2
setrecursionlimit(12346)
print(F(12345))