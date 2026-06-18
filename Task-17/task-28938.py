with open(r'./Files/17_29349.txt') as file:
    data = [int(i) for i in file]
ans = []

maxx = max(i for i in data if str(i)[-2:] == '28')
for num1, num2, num3 in zip(data, data[1:], data[2:]):
    u1 = len(str(abs(num1))) == 3
    u2 = len(str(abs(num2))) == 3
    u3 = len(str(abs(num2))) == 3
    u = (num1 + num2 + num3) // 3
    if u1 + u2 + u3 >= 1:
        if u > 0 and u < maxx:
            ans.append((num1 + num2 +num3))
print(len(ans),max(ans))
