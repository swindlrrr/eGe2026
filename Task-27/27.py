from math import dist


def center(clus):
    ans = []
    for dot in clus:
        sum_dist = sum(dist(dot, d) for d in clus)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'./Files/27_A_23284.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

clus1 = [d for d in dots if d[1] < 15]
clus2 = [d for d in dots if d[1] > 15]

centr1 = center(clus1)
centr2 = center(clus2)

Px = (centr1[0] + centr2[0])
Py = (centr1[1] + centr2[1])

print(abs(Px * 10_000), abs(Py * 10_000))

