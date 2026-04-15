from itertools import *
alph = 'КАЙФ'
cnt = 0
for pos, val in enumerate(product(alph,repeat=4), start = 1):
    val = ''.join(val)
    if val.count('К') == 1 and val.count('А') == 1 and val.count('Й') == 1 and val.count('Ф') == 1 and val[-1] != 'Й' and 'КФ' not in val:
        cnt+=1
print(cnt)