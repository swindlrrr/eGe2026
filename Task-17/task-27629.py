

with open(r'.\files\17_27629.txt') as file:
    data = [int(i) for i in file]

maxx = max(i for i in data if len(str(abs(i))) == 4 and str(i)[-2:] == '43')

ans = []
for num1, num2 in zip(data, data[1:]):
    u1 = len(str(abs(num1))) == 4
    u2 = len(str(abs(num2))) == 4
    if u1 + u2 >= 1 and (num1 + num2) ** 2 < maxx ** 2:
        ans.append((num1 + num2) ** 2)

print(len(ans), max(ans))

##########################################

ans = []
for nums in zip(data, data[1:]):
    if sum(len(str(abs(num))) == 4 for num in nums) >= 1:
        if sum(nums) ** 2 < maxx ** 2:
            ans.append(sum(nums) ** 2)

print(len(ans), max(ans))