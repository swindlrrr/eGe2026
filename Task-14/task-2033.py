num = 6*144**26 + 11*12**75 - 48
cnt = 0
B = 11
while num:
    if num % 12 == B:
        cnt += 1
    num //= 12
print(cnt)
