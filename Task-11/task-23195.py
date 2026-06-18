from math import ceil, log2
ans = []
for N in range(1, 1000):
    L = 172
    i = ceil(log2(N))
    I = ceil(i * L / 8)
    if I * 356984>=54*2**20:
        ans.append(N)
print(min(ans))
