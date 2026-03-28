from itertools import product
cnt = 0
for val in product('0123456', repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('6') == 1:
        chet = 0
        nechet = 0
        for c in val:
            if c in '0246':
                chet += int(c)
            else:
                nechet += int(c)
        if chet < nechet:
            cnt += 1
print(cnt)