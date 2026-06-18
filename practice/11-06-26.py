# from itertools import *
# graph = 'AF FE ED DC CB BG GA GF GE GD GC'.split()
# matrix = '345 467 14 123567 147 24 245'.split()
#
# print(*range(1,8))
#
# for i in permutations('ABCDEFG'):
#     if all(str(i.index(x)+1) in matrix[i.index(y)] for x,y in graph):
#         print(*i)

# from itertools import *
#
# def f(x,y,z,w):
#     return w <= (( x <= z) <= y)
#
# for x1,x2,x3,x4,x5,x6,x7 in product([0,1], repeat = 7):
#     t = (
#         (x1,x2,0,1,0),
#         (x3,0,1,x4,0),
#         (x5,x6,x7,0,0)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw'):
#             if all(f(**dict(zip(p,l))) == l[-1] for l in t):
#                 print(*p, sep = '')


# def convert(num,sys):
#     res = ''
#     while num:
#         res += str(num%sys)
#         num //= sys
#     return res[::-1]
# ans = []
# for N in range(1,1000):
#     R = convert(N,3)
#     if N % 3 == 0:
#         R = '1' + R + '02'
#     else:
#         R = R + convert((N % 3) * 4, 3)
#     R = int(R, 3)
#     if R < 100:
#         ans.append(N)
# print(max(ans))


# from turtle import *
# screensize(5000,5000)
# tracer(False)
# m = 20
# lt(90)
#
# for i in range(2):
#     fd(20*m)
#     lt(270)
#     fd(12*m)
#     rt(90)
# up()
# fd(9*m)
# rt(90)
# fd(7*m)
# lt(90)
# down()
# for i in range(2):
#     fd(13*m)
#     rt(90)
#     fd(6*m)
#     rt(90)
# up()
# for x in range(7,13):
#     for y in range(9,21):
#         goto(x*m,y*m)
#         dot(3,'red')
# update()
# done()
# print((21*13 + 14*7) - 6*12)

# from itertools import *
# from string import printable
#
# cnt = 0
# alph = printable[:7]
#
# for val, pos in enumerate(product(alph,repeat = 5), start = 1):
#     val = ''.join(val)
#     if val.count('6') == 1 and


# from math import ceil, log2
# ans = []
# for N in range(1,1000):
#     L = 562
#     i = ceil(log2(N))
#     I = ceil(i * L / 8)
#     if I * 45877 > 49 * 2**20:
#         ans.append(N)
# print(min(ans))

# from ipaddress import *
# net = ip_network('102.162.200.51/255.255.255.0', 0)
# print(net[-2])
# print(102+162+200+254)

# def convert(num,sys):
#     res = ''
#     while num:
#         res += str(num%sys)
#         num//=sys
#     return res[::-1]
#
# ans = []
# for x in range(1,2401):
#     num = 7 * 9**210 + 6 * 9 **110 - x
#     N  = convert(num, 9)
#     if N.count('0') == 100:
#         ans.append(x)
# print(max(ans))
# ans = []
# def f(x,y):
#     return (2*x+y != 110) or (x < y) or (A<x)
#
# for A in range(1,1000):
#     if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
#         ans.append(A)
# print(max(ans))

# from sys import setrecursionlimit
#
#
# def F(n):
#     if n < 10: return n
#     return 3 * n + F(n - 3)
# setrecursionlimit(10000)
# print((F(6250)+2*F(6244))//F(6238))