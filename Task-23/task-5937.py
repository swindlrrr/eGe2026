def f(current, end):
    if current == end: return 1
    if current > end or : return 0
    return f(current + 2, end) + f(current + 3, end) + f(current * 2 + 1, end)
print(f(1,55))