from math import ceil, log2

for N in range(1,100_0000):
    L = 35
    i = ceil(log2(N))
    I = ceil(L * i/8) + 48
    if I * 1536 <= 120 * 2**10:
        print(N)
