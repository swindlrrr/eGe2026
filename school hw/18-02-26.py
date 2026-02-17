def convert_2(num, sys):
    res = 0
    for i in range(len(num)):
        res += int(num[i],36) * sys ** (len(num) - i -1)
    return res

for x in range(42):
    num1 = convert_2(list('j569') + [x], 42)
    num2 = convert_2(list('1') + [x] + list('ia'),42)
    num = num1 + num2
    if num % 155 ==0:
        print(num//155)


from string import printable
for x in printable[:25]:
    num1 = int(f'11353{x}12', 25)
    num2 = int(f'135{x}21', 25)
    num = num1+num2
    if num % 24 ==0:
        print(num//24)


from string import printable
for x in printable[:23]:
    num1 = int(f'7{x}38596', 23)
    num2 = int(f'14{x}36', 23)
    num3 = int(f'61{x}7', 23)
    num = num1 + num2 + num3
    if num % 22 ==0:
        print(num//22)

from turtle import *

screensize(5000, 5000)
tracer(False)
m = 20
lt(90)


for i in range(9):
    fd(22*m)
    rt(90)
    fd(6*m)
    rt(90)
up()
fd(1*m)
rt(90)
fd(5*m)
lt(90)
down()
for i in range(9):
    fd(53*m)
    rt(90)
    fd(75*m)
    rt(90)
up()
for x in range(0,2):
    for y in range(0,22):
        goto(x*m,y*m)
        dot(3, 'red')
update()
done()



def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]


ans = []
for N in range(1, 100_000):
    R = convert(N, 9)
    if R[0] == "7":
        R = R.replace('6', '*')
        R = R.replace('3', '6')
        R = R.replace('*', '3')
        R = '34' + R
    else:
        R = R + '45'
        R = '3' + R[1:]
    R = int(R, 9)
    if R < 2876:
        ans.append([R, N])
print(max(ans))




ans = []
for N in range(1, 100_000):
    R = bin(N)[2:]
    if N % 2 == 0:
        R = '1' + R + '00'
    else:
        R += bin(R.count('1'))[2:]
    R = int(R, 2)
    if R > 88 and N>8:
        ans.append([R, N])
print(min(ans))


for x in range(37):
    num1 = int('c',36)*37**8 + 5*37**7 + 9*37**6 + x*37**5 + int('b',36)*37**4 + int('a',36)*37**3 + 9*37**2 + 8*37**1 + int('f',36)*37**0
    num2 = int('e',36)*37**8 + 3*37**7 + x*37**6 + 5*37**5 + int('d',36)*37**4 + int('a',36)*37**3 + 9*37**2 + int('c',36)*37**1 + 6*37**0
    num = num1*num2
    if num % 36 == 0:
        print(2*37**2 + x*37**1 + 1*37**0)



from string import printable

for x in printable[:14]:
    num1 = int(f'4b3{x}1c7', 14)
    num2 = int(f'5{x}g83f7', 17)
    num = num1 + num2
    if num % 15 == 0:
        print(num // 15)


num = 6*144**26 + 11*12**75 - 48
cnt = 0
B = 11
while num:
    if num % 12 == B:
        cnt += 1
    num //= 12
print(cnt)
