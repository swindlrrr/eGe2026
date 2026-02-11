def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //=sys
    return res[::-1]

num = 4*625**9 - 25**15 + 2*5**11 - 7
N = convert(num, 5)
N = N.count('4')
print(N)