def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //=sys
    return res[::-1]
x = 0
num = 3*7**(x+1) + 13*7**(x+2) + 31 * 7**(3*x) + 1*7**(2*x)
N = convert(num,7)
if sum(map(int, N)) == 18:
    x += 1
print(min(x))
