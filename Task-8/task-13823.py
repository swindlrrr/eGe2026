from itertools import product
ans =[]
alph = sorted('МИЗАНТРОП')
for pos, val in enumerate(product(alph, repeat = 5), start = 1):
    val = ''.join(val)
    if val[0] == 'Н' and val.count('Р') == 2 and pos % 2 ==0:
        ans.append(pos)
print(max(ans))