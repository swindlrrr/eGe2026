from functools import lru_cache
@lru_cache()
def f(current, end, x, y):
    if x == 23: return 0
    if current>= end: return current == end and y == 1
    if current == 11: y = 1
    if x == 1: return f(x+2, end, 0,0) + f(current * 2, end, 0,0)
    return f(x+1, end, 1,0) + f(x+2, end, 0) + f(x*2, end,0,0)
print(f(11,79,0,0))