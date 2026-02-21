def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]

for x in range(0, 2025):
    num = 9**2024 + 9**1987 - x
    N = convert(num, 9)
    if N.count('8') == 1984:
        print(x)