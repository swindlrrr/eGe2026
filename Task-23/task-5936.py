# def f(current,end,c):
#     if current % 2 != 0: c +=1
#     if current == end: return 1
#     if current > end or c > 4 : return 0
#     return f(current + 2, end, c) + f(current + 3, end, c) + f(current * 2 + 1, end, c)
# print(f(1,625, 0))
from sys import setrecursionlimit
def f(curr, end, c):
    if curr % 2:
        c += 1
    if curr >= end:
        return curr == end and c <= 4
    return f(curr + 2, end, c) + f(curr + 3, end, c) + f(curr * 2 + 1, end, c)
setrecursionlimit(150_000)

print(f(1, 625, 0))
