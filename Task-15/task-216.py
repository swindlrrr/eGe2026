def f(x):
    return ((x&26!=0) or (x&13!=0)) <= ((x&29==0) <= (x&A!=0))

for A in range(1,100000):
    if all(f(x) for x in range(1,100000)):
        print(A)
        break