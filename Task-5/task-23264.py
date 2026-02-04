def convert(num, sys):
    res = ""
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


ans = []
for N in range(1, 100_000):
    R = convert(N,3)
    if N % 3 == 0:
        R = R + R[-2:]
    else:
        v = (N % 3) * 5
        v = convert(v, 3)
        R = R + v
    R = int(R, 3)
    if R > 150:
        ans.append(R)
print(min(ans))
