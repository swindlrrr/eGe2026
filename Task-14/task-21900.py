def convert(num, sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1, 2301):
    num = 7**350 + 7**150 - x
    N = convert(num, 7)
    if N.count('0') == 200:
        ans.append(x)
print(max(ans))