def f(current, end, x,y,z):
    if current > end or x>4 or z > 5: return 0
    if current == end and x <= 4 and y >= 2 and z == 5: return 1
    return f(current * 5, end, x + 1, y, z) + f(current * 3, end, x, y + 1, z) + f(current + 45, end, x, y, z + 1)
print(f(1, 2970, 0, 0, 0))