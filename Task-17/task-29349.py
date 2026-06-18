with open(r'./Files/17_29349.txt') as file:
    data = [int(i) for i in file]
ans = []

minn = min(i for i in data if i > 0 and i % 123 == 0)
for num1, num2 in zip(data, data[1:]):
        if num1+num2 < minn:
            ans.append(num1+num2)
print(len(ans), abs(max(ans)))

