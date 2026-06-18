with open(r'./Files/17_23757.txt') as file:
    data = [int(i) for i in file]
    minn = min(i for i in data if len(str(i)) == 2)

ans = []
for nums in zip(data, data[1:]):
    if sum(len(str(abs(num))) == 2 for num in nums) == 1:
        if sum(nums) % minn == 0:
            ans.append(sum(nums))

print(len(ans), max(ans))