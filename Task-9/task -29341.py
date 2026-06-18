with open(r'./Files/29341.txt') as file:
    data = [list(map(int, i.split())) for i in file]
cnt = 0
for line in data:
    amount = [line.count(i) for i in set(line)]
    if sorted(amount) == []