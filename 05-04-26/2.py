from itertools import *
def f(x,y,z,w):
    return ((z == x) <= w) and (w <= (y and x))

for x1, x2, x3 in product([0,1], repeat = 3):
    t = (
        (1,1,x1,0,1),
        (1,x2,x3,0,1),
        (1,0,1,1,1)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p, sep='')
