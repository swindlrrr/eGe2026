from sys import setrecursionlimit

def F(n):
    if n < 6: return n
    if n >= 6: return (3*n - 2) * F(n - 5)

setrecursionlimit(1000000)
print((F(20568) - 51702*F(20563))/F(20553))
