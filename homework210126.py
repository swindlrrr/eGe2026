# 1
a, b, c = 1, 2, 3
a, b, c = 4, 5, 6
print(a, b, c)

# 2
a, b, c = input().split()
a, b, c = c, b, a
print(a, b, c)

#3
x, y = 15, 4
result = x - y
print(result)

#4
p, q = 20, 8
print("Обычное деление:", p / q)
print("Целочисленное деление:", p // q)

#5
a, b = 10, 4
a += b
print(a)

#6
x, y = 50, 8
x /= 3
print("После деления:", x)
print("Остаток:", x % y)
