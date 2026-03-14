from itertools import permutations
cnt = 0
for val in set(permutations('АМФИБРАХИЙ', r=10)):
    val = ''.join(val)
    if 'ИИФАА' in val or 'ААФИИ' in val:
        cnt += 1
print(cnt)