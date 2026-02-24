from string import printable

def convert(num,sys):
    res = ''
    while num:
        res += str(num%sys)
        num //= sys
    return res[::-1]

cnt = 0
for x in printable[:16]:
    num1 = int(f'8569{x}', 16)
    num2 = int(f'12{x}48', 16)
    num = num1+num2
    N = convert(num, 8)
    while N:
        if N % 2 ==0:
        cnt += 1


