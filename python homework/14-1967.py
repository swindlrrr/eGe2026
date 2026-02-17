def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]
num = 3*4**38 + 2*4**23 + 4**20 + 3*4**5 + 2*4**4 + 1
N = convert(num,16)
N = N.count('0')
print(N)