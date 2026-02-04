ans = []
for N in range(1, 100_000):
    R = bin(N)[2:]
    if N % 3 == 0:
        R = R + R[-3:]
    else:
        v = (N % 3) * 3
        v = bin(v)[2:]
        R = R + v
    R = int(R, 2)
    if R < 130:
        ans.append(N)
print(max(ans))
