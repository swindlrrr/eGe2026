def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


num = 3 * 5 ** 1984 - 7 * 25 ** 777 - 11 * 125 ** 666 - 404
N = convert(num, 5)
N = N.count('2')
print(N)


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



from string import printable
for x in printable[:19]:
    num1 = int(f'98897{x}21', 19)
    num2 = int(f'2{x}923', 19)
    num = num1 + num2
    if num % 18 ==0:
        print(num//18)



def convert (num,sys):
    res = ''
    while num:
        res +=str(num%sys)
        num //= sys
    return res[::-1]
num = 3*3125**8 + 2*625**7 - 4*625**6 + 3*125**5 - 2*25**4 - 2024
N = convert(num,25)
z = N.count('0')
print(z)



from string import printable


def convert(num, sys):
    res = ''
    while num:
        res += printable[num % sys]
        num //= sys
    return res[::-1]


for N in range(2, 37):
    if convert(41, N)[-1] == '2' and convert(131, N)[-1] == '1':
        print(N)



def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


for x in range(0, 100_000):
    num = 3 * 7 ** (x + 1) + 13 * 7 ** (x + 2) + 31 * 7 ** (3 * x) + 1 * 7 ** (2 * x)
    N = convert(num, 7)
    summ = sum(map(int, N))
    if summ == 18:
        print(x)
        break