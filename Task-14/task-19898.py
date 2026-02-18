def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


ans = []
for x in range(1,10001):
    N = convert(7**270+7**170+7**70-x, 7)
    N = N.count('0')
    ans.append([N,x])
print(max(ans))
