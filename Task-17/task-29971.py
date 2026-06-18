with open(r'./Files/17_29971.txt') as file:
    data = [int(i) for i in file]
ans = []
max_33 = max(i for i in data if str(i)[-2:] == '33')
for nums in zip(data,data[1:], data[2:]):
    if sum(len(str(abs(num))) == 2 for num in nums) == 2:
        if sum(nums) ** 2 < max_33:
            ans.append(sum(nums))
print(len(ans), max(ans))
