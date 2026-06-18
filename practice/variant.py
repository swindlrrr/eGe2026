#1
# from itertools import *
#
# graph = 'DC CF FG GE EA AD DB CB BH HA HG'.split()
# matrix = '346 348 12 127 678 15 458 257'.split()
#
# print(*range(1,9))
#
# for i in permutations('ABCDEFGH'):
#     if all(str(i.index(x) + 1 ) in matrix[i.index(y)] for x, y in graph):
#         print(*i)

#2
# from itertools import *
#
# def f(x,y,z,w):
#     return not(w <= (x == y)) and (z <= x)
#
# for x1,x2,x3,x4,x5 in product([0,1], repeat = 5):
#     t = (
#         (x1,0,1,0,1),
#         (0,x2,x3,0,1),
#         (x4,1,1,x5,1)
#     )
#
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw'):
#             if all(f(**dict(zip(p,l))) == l[-1] for l in t):
#                 print(*p, sep = '')


#5

# def convert(num,sys):
#     res = ''
#     while num:
#         res += str(num%sys)
#         num //= sys
#     return res[::-1]
#
# ans = []
# for N in range(1,10_000):
#     R = convert(N, 3)
#     if N % 3 == 0:
#         R = R + R[-2:]
#     else:
#         R = R + convert((N % 3) * 5, 3)
#     R = int(R,3)
#     if R > 150:
#         ans.append(R)
# print(min(ans))

#11
# from math import ceil,log2
# ans = []
#
# for L in range(1,10000):
#     N = 10 + 27
#     i = ceil(log2(N))
#     I = ceil(i * L/ 8)
#     if I * 3548 > 12 * 2**10:
#         ans.append(L)
# print(min(ans))

#6
# from turtle import *
#
# screensize(5000, 5000)
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
#         goto(x * m, y * m)
#         dot(3,"red")
# update()
# done()

#8
# from itertools import *
# ans = []
#
# alph = sorted('СТРОКА')
# for pos, val in enumerate(product(alph,repeat = 5), start = 1):
#     val = ''.join(val)
#     if (pos % 2) != 0 and val[0] != 'А' and val[0] != 'Л' and val.count('С') == 1:
#         ans.append(pos)
# print(max(ans))

#14

# from string import printable
# ans = []
#
# for x in printable[:29]:
#     num1 = int(f'463{x}7921', 29)
#     num2 = int(f'8241{x}153',29)
#     num = num1+num2
#     if num%28 == 0:
#         ans.append(num//28)
# print(min(ans))


