from itertools import product, permutations
def f(w, x, y, z):
    return (x<=y) and z and (not w)
for x1, x2, x3, x4, x5, x6 in product([0,1], repeat = 6):
    t = (
        (0,1,x1,x2,1),
        (1,1,x3,x4,1),
        (1,x5,1,x6,1)
    )
    if len(t)==len(set(t)):
        for p in permutations('wxyz', r = 4):
            if all(f(**dict(zip(p,l))) == l[-1] for l in t):
                print(*p, sep ='')
                exit()