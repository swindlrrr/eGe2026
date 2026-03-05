# # 5
#
# ans = []
#
# for N in range(1, 100_000):
#     R = bin(N)[2:]
#     if N % 2 == 0:
#         R = '10' + R
#     else:
#         R = '1' + R + '01'
#     R = int(R, 2)
#     if R > 516:
#         ans.append(N)
# print(min(ans))
#
#
# #8
#
# from itertools import product
#
# ans = []
# alph ='АКЛМНЯ'
# for pos, val in enumerate(product(alph, repeat = 5), start = 1):
#     val = ''.join(val)
#     if val[:2] == 'КМ':
#         ans.append(pos)
# print(min(ans))
#
#
# 14
#
# def convert(num, sys):
#     res = ''
#     while num:
#         res += str(num % sys)
#         num //= sys
#     return res[::-1]
#
# ans = []
# for x in range(1, 10001):
#     num = 7**270+7**170+7**70 - x
#     N = convert(num, 7)
#     R = N.count('0')
#     ans.append([R, x])
# print(max(ans))
