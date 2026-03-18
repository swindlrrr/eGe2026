print('x w y z')
for x in 0,1:
    for y in 0,1:
        for z in 0,1:
            for w in 0,1:
                f = not(y <= (x == w)) and (z <= x)
                if f:
                    print(x, w, y, z)

from itertools import product, permutations
def f(x, y, z, w):
    return not(y <= (x == w)) and (z <= x)
for x1, x2, x3, x4, x5 in product([0,1], repeat = 5):
    t = (
        (x1, 1, 1, x2, 1),
        (0, x3, x4, 0, 1),
        (x5, 0, 1, 0, 1)
    )
    if len(t)==len(set(t)):
        for p in permutations('xwyz'):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p, sep='')