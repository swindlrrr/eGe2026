# from itertools import *
#
# graph = 'FA AB BG GE EF FD AD DC EC CB'.split()
# matrix = '457 567 45 136 123 247 126'.split()
#
# print(*range(1,8))
#
# for i in permutations('ABCDEFG'):
#     if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
#         print(*i)


# from itertools import *
#
#
# def f(x, y, z, w):
#     return not (x == (w and (not z))) and (y == (x and (not w)))
#
#
# for x1, x2, x3, x4, x5, x6 in product([0, 1], repeat=6):
#     t = (
#         (x1, x2, 0, x3, 1),
#         (x4, 0, x5, 0, 1),
#         (0, x6, 1, 0, 1)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw'):
#             if all(f(**dict(zip(p, l))) == l[-1] for l in t):
#                 print(*p, sep='')


# def convert(num,sys):
#     res = ''
#     while num:
#         res += str(num%sys)
#         num //= sys
#     return res[::-1]
#
# ans = []
# for N in range(1,1000):
#     R = convert(N, 3)
#     if N % 3 == 0:
#         R = R + R[-2:]
#     else:
#         R = R + convert((N % 3) * 5, 3)
#     R = int(R, 3)
#     if R > 150:
#         ans.append(R)
# print(min(ans))
#


# from turtle import *
# screensize(5000,5000)
# tracer(False)
# m = 20
# lt(90)
#
# for i in range(9):
#     fd(22*m)
#     rt(90)
#     fd(6*m)
#     rt(90)
# up()
# fd(1*m)
# rt(90)
# fd(5*m)
# lt(90)
# down()
# for i in range(9):
#     fd(53*m)
#     rt(90)
#     fd(75*m)
#     rt(90)
# up()
# for x in range(0,2):
#     for y in range(0,22):
#         goto(x*m, y * m)
#         dot(5, 'white')
# update()
# done()


# from itertools import *
# alph = sorted('АРГУМЕНТ')
# ans = []
# for pos, val in enumerate(product(alph, repeat = 4), start = 1):
#     val = ''.join(val)
#     val1 = ''.join(sorted(val))
#     if len(val) == len(set(val)) and val == val1 and all(val.count(i) <= 1 for i in ('АРГУМЕНТ')):
#         ans.append(pos)
# print(max(ans))

# ans = 0
#
# for x in range(5556):
#     num = 5**150 + 5 ** 135 - x
#     cnt_0 = 0
#     while num:
#         if num % 5 == 0: cnt_0 += 1
#         num //= 5
#     if cnt_0 % 2 == 0:
#         ans += x
# print(ans)

# def DEL(n,m): return n % m == 0
#
# def f(x):
#     C = 30 <= x <= 45
#     return (DEL(x,A) and C) <= (not DEL(x,12))
# ans = []
# for A in range(1,10000):
#     if all(f(x) for x in range(1,1000)):
#         ans.append(A)
# print(min(ans))
#

# from sys import setrecursionlimit
# def F(n):
#     if n == 1: return 1
#     if n > 1: return (n - 1) * F(n - 1)
# setrecursionlimit(500000)
# print((F(2024)//7 - F(2023))//F(2022))


# def f(current, end):
#     if current == end: return 1
#     if current > end or current == 16: return 0
#
#     return f(current + 1, end) + f(current + 2, end) + f(current * 3, end)
#
# print(f(2,9) * f(9,18))


# def f(x,s):
#     if x >= 39: return s % 2 == 0
#     if s == 0: return False
#     h = [
#         f(x+1, s-1),
#         f(x+3, s-1),
#         f(x*2, s-1)
#     ]
#     return any(h) if (s-1) % 2 == 0 else all(h)
#
# print(min([x for x in range(1,39) if f(x,2)]))
# print([x for x in range(1,39) if f(x,3) and not f(x,1)])
# print([x for x in range(1,39) if f(x,4) and not f(x,2)])