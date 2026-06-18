def convert(num, sys):
    res = ""
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


ans = []
for N in range(1, 10000):
    R = convert(N, 3)
    if N % 3 == 0:
        R = '1' + R + R[3:]
    else:
        R = R + convert((N % 3) * 8, 3)
        R = int(R, 3)
        ans.append(R)
print(max(ans))
