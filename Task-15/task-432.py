def DEL(x,A):
    return x % A == 0

def f(x):
    return ((not DEL(x,84)) or (not DEL(x,90))) <= (not DEL(x,A))

for A in range(1,30000):
    if all(f(x) for x in range(1,30000)):
        print(A)
        break