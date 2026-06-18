from math import ceil, log2

L = 32
N = 73
i = ceil(log2(N))
I = ceil(i*L/8)
print(I*3840/2**10)