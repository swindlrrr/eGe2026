from sys import setrecursionlimit
def F(n):
    if n <= 10: return n
    return n-7 + F(n - 21)
setrecursionlimit(190000)
print((F(185734) - F(185650))/F(40))


from itertools import product
ans = []

alph = sorted('МАНГУСТ')
for pos, val in enumerate(product(alph, repeat = 6), start = 1):
    val = ''.join(val)
    if val[0] != 'У' and val.count('М') == 2 and val.count('Г') <= 1:
        ans.append(pos)
print(max(ans))


from itertools import product
cnt = 0
summ = 0
for val in sorted(product('СДАЙЕГЭ', repeat=6)):
    val = ''.join(val)
    cnt += 1
    if 'ЕГЭ' in val:
        summ += cnt
print(summ)



def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for x in range(0, 100_000):
    num = 3 * 7 ** (x + 1) + 13 * 7 ** (x + 2) + 31 * 7 ** (3 * x) + 1 * 7 ** (2 * x)
    N = convert(num, 7)
    summ = sum(map(int, N))
    if summ == 18:
        print(x)
        break


from string import printable
for x in printable[:29]:
    num1 = int(f'463{x}7921', 29)
    num2 = int(f'8241{x}153', 29)
    num = num1 + num2
    if num % 28 ==0:
        print(num//28)


def f(current, end, x,y,z):
    if current > end or x>4 or z > 5: return 0
    if current == end and x <= 4 and y >= 2 and z == 5: return 1
    return f(current * 5, end, x + 1, y, z) + f(current * 3, end, x, y + 1, z) + f(current + 45, end, x, y, z + 1)
print(f(1, 2970, 0, 0, 0))


from math import ceil, log2
for L in range(100000):
    N = 562
    i = ceil(log2(N))
    I = ceil(L * i / 8)
    if I * 45877>49*2**20:
        print(L)
        break
