def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]
num = 16**820 - 2**761 + 14
N = convert(num,4)
N = N.count('0')
print(N)