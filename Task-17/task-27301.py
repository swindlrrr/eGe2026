with open(r'./Files/17_27301.txt') as file:
    data = [int(i) for i in file]
    maxx = max(i for i in data if str(i)[:2] == '45')
ans = []

for nums in zip(data, data[1:], data[2:]):
    u1 = nums[0] < 0
    u2 = nums[1] < 0
    u3 = nums[2] < 0
    u = sum(nums)
    if u1 + u2 + u3 == 1:
        if u>= maxx and str(u)[-2:] == '45':
            ans.append(sum(nums))
print(len(ans), min(ans))
