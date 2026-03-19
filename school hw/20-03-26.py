from itertools import product, permutations
def f(x, y, z, w):
    return ((w <= y) <= x) or not z
for x1, x2, x3, x4, x5, x6, x7, x8 in product([0,1], repeat = 8):
    t = (
        (x1,x2,1,x3,0),
        (x4,0,x5,x6,0),
        (x7,1,0,0,0)
    )
    if len(t) == len(set(t)):
        for p in permutations('xyzw', r =4):
            if all(f(**dict(zip(p,l))) == l[-1] for l in t):
                print(*p, sep = '')


from itertools import permutations
graph = 'EH HG GC CF FA AE ED DF DB BH BG'.split()
matrix = '23 168 158 578 347 27 456 234'.split()

print(*range(1,9))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)


from itertools import product
cnt = 0
for pos, val in enumerate(product('ЕЛОПРСТ', repeat=5), start = 1):
    val = ''.join(val)
    if pos % 2 == 1 and val[-1] in 'ЕО' and sum(val.count(c) for c in 'ЛПРСТ') <= 3:
        cnt += 1
print(cnt)



from itertools import permutations
graph ='CE EG GF FA AC CD DH HE BF BA'.split()
matrix ='68 47 45 237 368 15 248 257'.split()

print(*range(1,9))

for i in permutations('ABCDEFGH'):
    if all(str(i.index(x)+1) in matrix[i.index(y)] for x, y in graph):
        print(*i)


from itertools import product, permutations


def f(x, y, z, w):
    return not (y <= x) or (z <= w) or not z


for x1, x2, x3, x4, x5, x6, x7 in product([0, 1], repeat=7):
    t = (
        (x1, 0, x2, x3, 0),
        (0, 1, x4, x5, 0),
        (1, x6, x7, 0, 0)
    )

    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if all(f(**dict(zip(p, l))) == l[-1] for l in t):
                print(*p, sep='')
