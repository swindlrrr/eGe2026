def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]


num = 15625**16 - 3125**3 * 25**19 + 625**4 - 2005
N = convert(num, 5)
N = N.count('0')
print(N)