def f(x, y, z):
    return (x | 50 == x) or (y & 34 != 0) or (z | 24 != 24) or (x * y * z > (A // 8))

ans = []
for A in range(1, 500)[::-1]:
    if all(f(x,y,z) for x in range(1,500) for y in range(1,500) for z in range(1,500)):
        print(A)
        break



def f(x, y):
    return (x + 2 * y > A) or (y < x) or (x < 30)

for A in range(0,1000)[::-1]:
    if all(f(x,y) for x in range(0,1000) for y in range(0,1000)):
        print(A)
        break



def f(x, y):
    return (x<A) and (y<3*A) or (2*x+y>128)
for A in range(0,1000):
    if all(f(x,y) for x in range(1,1000) for y in range(1,1000)):
        print(A)
        break


from itertools import combinations


def f(x):
    P = 12 <= x <= 26
    Q = 30 <= x <= 53
    A = A1 <= x <= A2
    return (A<=P) or Q

ans = []
line_A = [12, 26, 30, 53]
line_X = [20, 27, 32]
for A1, A2 in combinations(line_A, 2):
    if all(f(x) for x in line_X):
        ans.append(A2-A1)
print(max(ans))


def f(x, y):
    return (x + y <= 22) or (y <= x - 6) or (y >= A)
for A in range(0,1000)[::-1]:
    if all(f(x,y) for x in range(0,1000) for y in range(0,1000)):
        print(A)
        break



def f(x, y):
    return (x < A) or (y < A) or (x + 2 * y > 50)
for A in range(0,1000):
    if all(f(x,y) for x in range(0,1000) for y in range(0,1000)):
        print(A)
        break