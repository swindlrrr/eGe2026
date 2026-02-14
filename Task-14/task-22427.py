from string import printable

for x in printable[:14]:
    num1 = int(f'4b3{x}1c7', 14)
    num2 = int(f'5{x}g83f7', 17)
    num = num1 + num2
    if num % 15 == 0:
        print(num // 15)
