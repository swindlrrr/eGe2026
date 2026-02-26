from itertools import product
ans = []

alph = sorted('МАНГУСТ')
for pos, val in enumerate(product(alph, repeat = 6), start = 1):
    val = ''.join(val)
    if val[0] != 'У' and val.count('М') == 2 and val.count('Г') <= 1:
        ans.append(pos)
print(max(ans))



def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(1,10001):
    N = convert(6**900+6**10-x, 6)
    if N.count('3')==N.count('5'):
        ans.append(x)
print(max(ans))



for N in range(1, 10 ** 6):
    L = 172
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if 356984 * I >= 54 * 2**20:
        print(N)
        break

def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]

for x in range(1,100_000):
    num = 7**666 + 7**333 + 49**x - 343
    N = convert(num,7)
    if N.count('6') == 49:
        print(x)


def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


ans = []
for N in range(1, 100_000):
    R = convert(N, 6)
    if R[-1] == '0':
        R = R.replace('3', '*')
        R = R.replace('5', '3')
        R = R.replace('*', '5')
        R = '33' + R
    else:
        R = R + '42'
        R = '3' + R[1:]
    R = int(R, 6)
    if R < 200:
        ans.append([R, N])
ans = sorted(ans, key=lambda x:(-x[0], x[1]))
print(ans[0])

