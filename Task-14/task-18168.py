def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(10,70001):
    num = 5**2025 + 5**400 - x
    N = convert(num, 5)
    R = N.count('4')
    ans.append([R,x])
print(max(ans))