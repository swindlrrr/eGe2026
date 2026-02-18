def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1,2006):
    N = convert(4**163 * 5 + 12**62-x, 5)
    if N.count('1')<N.count('4'):
        ans.append(x)
print(max(ans))