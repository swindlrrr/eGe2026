from math import ceil,log2
ans=[]
for N in range(1,100_000):
    L = 377
    i = ceil(log2(N))
    I = ceil(L*i/8)
    if I * 23155>5536*2**10:
        ans.append(N)
print(min(ans))
