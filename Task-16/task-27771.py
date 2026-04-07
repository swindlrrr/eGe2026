from sys import setrecursionlimit
def F(n):
    if n == 1: return 1
    if n > 1: return n * F(n-1)
setrecursionlimit(1000000)
print((F(2024) - 2 * F(2023))/F(2022))