cnt = 0
for n in range(1,40):
    if bin(n)[-4:] == '1011':
        cnt = n
print(cnt)