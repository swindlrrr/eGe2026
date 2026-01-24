# Цикл while

num = 0
while num < 5:
    # print('Hello')
    num += 1

# Сумма цифр числа
num = 123
summ = 0
while num != 0:
    summ += num % 10
    num //= 10
# print(summ)


# Цикл for

# range(n) - диапазон от 0 до n не включительно
# range (n, m) - формирует диапазон целых чисел от n до m не включительно с шагом 1
# range(n, m, k) - формирует диапазон целых чисел от n до m не включительно с шагом k

for i in range(0, -6, -1):
    print(i)
