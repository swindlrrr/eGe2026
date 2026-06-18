# 8
from itertools import *
from string import printable

cnt = 0
alph = printable[:9]
for val in product(alph, repeat=5):
    val = ''.join(val)
    if val[0] != '0' and val.count('3') == 2:
        for i in printable[1:9:2]:
            val = val.replace(i, '*')
        if '*2' not in val and '2*' not in val:
            cnt += 1
print(cnt)

# 17
with open() as file:
    data = [int(i) for i in file]
min_9 = min(i for i in data if i > 0 and i % 9 == 0)

ans = []
for num1, num2 in zip(data, data[1:]):
    if num1 != num2:
        if abs(num1 - num2) % min_9 == 0:
            ans.append(num1 + num2)
print(len(ans), max(ans))


# 23
def f(cur, end):
    if cur == end: return 1
    if cur > end: return 0
    cur_str = str(cur)
    if int(cur_str[-2]) < int(cur_str[-1]):
        return f(cur + 1, end) + f(int(cur_str[:-2] + cur_str[-1] + cur_str[-2]), end)
    else:
        return f(cur + 1, end)


print(f(100, 150))

# 24
from re import finditer

with open() as file:
    data = file.readline()

number = r'([1-9][0-9]*|0)'
pattern = rf'{number}([+*]{number})+'

matches = [match.group() for match in finditer(pattern, data)]
print(len(max(matches, key=len)))


# 15
def DEL(n, m):
    return n % m == 0


def f(x):
    B = 15 <= x <= 30
    return DEL(x, A) or (DEL(x, 23) <= (not B))


for A in range(1, 1_000)[::-1]:
    if all(f(x) for x in range(1, 1_000)):
        print(A)
        break


#14
ans = []
for x in range(1, 2030):
    num = 5 ** 150 + 5 ** 100 - x
    cnt_0 = 0
    while num:
        if num % 5 == 0: cnt_0 += 1
        num //= 5
    ans.append([cnt_0, x])

print(max(ans, key=lambda x:(x[0], -x[1])))



num = 228

summ = 0
while num:
    if num % 36 > 9: summ += num % 36
    num //= 36

print(summ)



num = 4*16**25 + 2*8**30 - 64**10

cnt = 0
while num:
    if num % 2 == 0: cnt += 1
    num //= 2

print(cnt)


from string import printable

for x in printable[:22]:
    num1 = int(f'63{x}89875', 22)
    num2 = int(f'17{x}51', 22)
    num3 = int(f'75{x}3', 22)
    num = num1 + num2 + num3
    if num % 21 == 0:
        print(num // 21)


#13

from ipaddress import ip_network
net = ip_network(f'146.180.173.153/255.192.0.0', 0)
print(net[-2])

from ipaddress import ip_network
net = ip_network(f'210.185.140.126/255.255.255.252', 0)
print(net.network_address)
