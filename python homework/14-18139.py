from string import printable

cnt = 0
for Y in range(1,101):
    for x in printable[1:25]:
        num1 = int(f'8af7{x}11', 25)
        num2 = int(f'{x}da87', 25)
        num = num1 + num2
        if num % Y ==0:
            cnt += 1
            break
print(cnt)


