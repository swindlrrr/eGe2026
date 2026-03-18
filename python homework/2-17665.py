from itertools import product, permutations
def f(x, y, w, z):
    return(z<=(not(y<=x))) or w

for x1, x2,x3,x4,x5,x6,x7,x8 in product([0,1], repeat = 8):
    t = (
        (x1,1,x2,x3,0),
        (x4,x5,0,0,0),
        (x6,0,1,x7,0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xywz', r = 4):
            if all(f(**dict(zip(p,l))) == l[-1] for l in t):
                print(*p, sep = '')
                exit()
