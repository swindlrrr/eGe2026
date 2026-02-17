ans = []
for N in range(1,100_000):
    R = bin(N)[2:]
    for i in range(2):
        v = R.count('1') % 2
        R = R + str(v)
    R = int(R,2)
    if R > 253:
        ans.append(N)
print(min(ans))
