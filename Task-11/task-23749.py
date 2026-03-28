from math import ceil, log2

for N in range(1, 10000000):
    L = 2783
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 3845627 >= 11 * 2 ** 30:
        print(N)
        break
