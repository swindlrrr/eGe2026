ans = 0

for x in range(1, 4000):
    num = 9 * 13 ** 9 + 5 * 13 ** 5 + 2 * 13**2 - x
    cnt_0 = 0
    while num:
        if num % 13 == 0: cnt_0 += 1
        num //= 13
    if cnt_0 % 2 == 0:
        ans += x
print(ans)
