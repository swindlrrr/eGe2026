def DEL(n,m):
    return n % m == 0

def f(x):
    return (DEL(x,A) and DEL(x,24) and (not DEL(x,16))) <= (not DEL(x,A))

for A in range(1,1000):
    if all(f(x) for x in range(1,1000)):
        print(A)
        break