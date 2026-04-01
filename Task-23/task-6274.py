def f(s):
    a = s[-1]
    if len(s) > 1 and a == 42: return 1
    if a < 40 or a > 49 or a in s[:-1]: return 0
    return sum(f(s + [a - h]) for h in [-3, -1, 1, 3])


print(f([42]))
