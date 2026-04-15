from itertools import *
def f(x,y,z,w):
    return not(x<=y) or (z==w) or z

for x1,x2,x3,x4,x5,x6,x7 in product([0,1], repeat = 7):
    t = (
        (0,0,x1,x2,0),
        (x3,x4,1,x5,0),
        (x6,1,0,x7,0)
    )
    if len(t)==len(set(t)):
        for p in permutations('xyzw'):
            if all(f(**dict(zip(p,l))) == l[-1] for l in t):
                print(*p, sep = '')