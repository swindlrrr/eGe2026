from math import ceil, log2
for L in range(100000):
    N = 562
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 45877>49*2**20:
        print(L)
        break