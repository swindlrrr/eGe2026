def convert(num, sys):
    res = ""
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


ans = []
for N in range(1, 100_000):
    R = convert(N, 4)
    if R[0] == "3":
        R = R.replace('1', '*')
        R = R.replace('3', '1')
        R = R.replace('*', '1')
        R = "21" + R
    else:
        R = R + '12'
        R = '1' + R[0:]
    R = int(R, 4)
    if R < 598:
        ans.append(N)
print(max(ans))
