# def f(x, s):
#     if x >= 165: return s % 2 == 0
#     if s ==0: return False
#     h = [f(x+1,s-1),
#         f(x*2,s-1)]
#     return any(h) if (s-1) % 2 ==0 else all(h)
# print('19)', [x for x in range(1,165) if f(x,2)])
# print('20)', [x for x in range(1,165) if f(x,3) and not f(x,1)])
# print('21)', [x for x in range(1,165) if f(x,4) and not f(x,2)])
#
#
# def f(current, end):
#     if current == end: return 1
#     if current < end:   return 0
#     return f(current - 1,end) + f(current - 3, end) + f(current // 3, end)
# print(f(22,2))
#
#
# def f(current,end):
#     if current == end: return 1
#     if current > end or current == 17: return 0
#     return f(current + 2, end) + f(current + 3, end) + f(current * 2, end)
#
# print(f(3,10)*f(10,25))
#
#
# def f(current, end):
#     if current == end: return 1
#     if current < end or current == 8: return 0
#     return f(current - 1, end) + f(current - 4, end) + f(current//3, end)
# print(f(19,14)*f(14,
#
#
# from functools import lru_cache
#
#
# @lru_cache(None)
# def G(n):
#     if n < 10: return 2 * n
#     if n >= 10: return G(n - 2) + 1
#
#
# def F(n):
#     return 2 * (G(n - 3) + 8)
# for i in range(1, 15549):
#     F(i)
# print(F(15548))
#
#
# from functools import lru_cache
# @lru_cache(None)
# def G(n):
#     if n <= 9: return 3 * n
#     if n > 9: return G(n-2) + 1
# def F(n):
#     return G(n-1)
# for i in range(1, 47996):
#     F(i)
# print(F(47995))