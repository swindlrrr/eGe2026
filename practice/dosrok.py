# #1
# from itertools import *
#
# graph = 'АВ ВЕ ЕК КД ДБ БА БВ ГД ГЕ ГК'.split()
# matrix = '457 346 24 123 167 257 156'.split()
#
# print(*range(1,8))
#
# for i in permutations('АБВГДЕК'):
#     if all(str(i.index(x) + 1 ) in matrix[i.index(y)] for x, y in graph):
#         print(*i)

# 2
# from itertools import *
#
#
# def f(x, y, z, w):
#     return (w == z) or (not (y <= w)) or (not x)
#
#
# for x1, x2, x3, x4, x5 in product([0, 1], repeat=5):
#     t = (
#         (0,0,1,x1,0),
#         (x2,1,1,x3,0),
#         (0,x4,x5,0,0)
#     )
#     if len(t) == len(set(t)):
#         for p in permutations('xyzw'):
#             if all(f(**dict(zip(p,l))) == l[-1] for l in t):
#                 print(*p, sep = '')

#5

# ans = []
# for N in range(1,1000):
#     R = bin(N)[2:]
#     G = (R.count('0') + R.count('1')) % 2
#     R1 = R + str(G)
#     R2 = R1 + str(G)
#     R3 = int(R2,2)
#     if R3 > 253:
#         ans.append(N)
# print(min(ans))

#6

# from turtle import *
# screensize(5000,5000)
# tracer(False)
# m = 50
# lt(90)
#
# rt(315)
# for i in range(7):
#     fd(12*m)
#     rt(45)
#     fd(6*m)
#     rt(135)
# up()
# for x in range(-8,0):
#     for y in range(-10,15):
#         goto(x*m,y*m)
#         dot(5,'red')
# update()
# done()

# #8
# from itertools import *
#
# ans = []
# alph = sorted('АПРЕЛЬ')
#
# for pos,val in enumerate(product(alph, repeat = 5), start = 1):
#     val = ''.join(val)
#     if pos%2 == 0  and val[0] != 'Ь' and val[0] != 'Р' and val.count('Л') >= 2:
#         ans.append(pos)
# print(max(ans))
#

# #11
# from math import ceil,log2
#
# L = 289
# N = 1025
# i = ceil(log2(N))
# I = ceil(i*L/8)
# G = I * 524288/2**20
# print(G)

#14
#
# cnt = 0
# numm = 2*2187**567+729**566-2*243**565+81**564-2*27**563-6561
# while numm:
#     if numm%27>9:
#         cnt +=1
#     numm//=27
# print(cnt)

# #15
# from itertools import combinations
# def f(x):
#     P = 25<= x <= 64
#     Q = 40 <= x <= 115
#     A = A1 <= x <= A2
#     return P <= ((Q and (not A)) <= (not P))
# ans = []
# line_A = [25,40,64,115]
# line_x = [26,41,65]
# for A1, A2 in combinations(line_A, 2):
#     if all(f(x) for x in line_x):
#         ans.append(A2-A1)
# print(min(ans))

#19
def f(x,s):
    if x >= 65: return s % 2 == 0
    if s == 0: return False
    h = [
        f(x+1,s-1),
        f(x*3,s-1)
        ]
    return any(h) if (s-1)%2==0 else any(h)
print('19)', min([x for x in range(1,59) if f(x,2)]))
print('20)', [x for x in range(1,59) if f(x,3) and not f(x,1)])
print('21)', [x for x in range(1,59) if f(x,4) and not f(x,2)])

