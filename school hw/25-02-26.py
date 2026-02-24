def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num//=sys
    return res[::-1]

for x in range(1,2031):
    num = 7**170 + 7**100 - x
    N = convert(num, 7)
    if N.count('0') == 71:
        print(x)



from string import printable

for x in printable[:14]:
    num1 = int(f'4b3{x}1c7', 14)
    num2 = int(f'5{x}g83f7', 17)
    num = num1 + num2
    if num % 15 == 0:
        print(num // 15)



def convert(num, sys):
    res = ''
    while num:
        res += str(num % sys)
        num //= sys
    return res[::-1]

ans = []
for x in range(10,70001):
    num = 5**2025 + 5**400 - x
    N = convert(num, 5)
    R = N.count('4')
    ans.append([R,x])
print(max(ans))




from turtle import *

screensize(5000, 5000)
tracer(False)
m = 10
lt(90)
for i in range(2):
    fd(21 * m)
    rt(90)
    fd(27 * m)
    rt(90)
up()
fd(9 * m)
rt(90)
fd(10 * m)
lt(90)
down()
for i in range(2):
    fd(86 * m)
    rt(90)
    fd(47 * m)
    rt(90)
up()

up()
for x in range(11, 27):
    for y in range(10, 21):
        goto(x * m, y * m)
        dot(3, 'red')
update()
done()



from turtle import *
screensize(5000,5000)

tracer(False)
m = 30

for i in range(9):
    fd(22 * m)
    rt(90)
    fd(6 * m)
    rt(90)
up()
fd(1 * m)
rt(90)
fd(5 * m)
lt(90)
down()
for i in range(9):
    fd(53 * m)
    rt(90)
    fd(75 * m)
    rt(90)
up()
for x in range(-100, 100):
    for y in range(-10, 10):
        goto(x * m, y * m)
        dot(8, "white")
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
    R = convert(N, 7)
    if R[-1] == '2':
        R = R.replace('3', '*')
        R = R.replace('1', '3')
        R = R.replace('*', '1')
        R = '21' + R
    else:
        R = '1' + R[1:] + '36'
    R = int(R, 7)
    if R < 744:
        ans.append([R, N])


ans = sorted(ans, key=lambda x:(-x[0], x[1]))
print(ans[0])



cnt = 0
for n in range(1,40):
    if bin(n)[-4:] == '1011':
        cnt = n
print(cnt)