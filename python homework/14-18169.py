def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]

for x in range(1,100000):
    num = 3**2000+3**10-x
    N = convert(num,3)
    if N.count('2') == 2000:
        print(x)