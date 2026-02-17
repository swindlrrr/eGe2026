ans = []
from string import printable
for x in printable[:25]:
    num1 = int(f'8af7{x}11', 25)
    num2 = int(f'{x}da87', 25)
    num = num1 + num2
    for Y in range(1,100_000):
        if Y <= 100:
            s = num%Y == 0
