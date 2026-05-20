from math import dist

def center(clus):
    ans = []
    for dot in clus:
        sum_dist = sum(dist(dot,d) for d in clus)
        ans.append([sum_dist, dot])
    return min(ans)[1]

with open(r'./Files/27-19257-B.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

clus1 = [d for d in dots if d[0] < 0]
clus2 = [d for d in dots if d[0] > 0 and d[1] > 8]
clus3 = [d for d in dots if d[0] > 0 and d[1] < 8]

centr1 = center(clus1)
centr2 = center(clus2)
centr3 = center(clus3)


Px = (centr1[0] + centr2[0] + centr3[0]) / 3
Py = (centr1[1] + centr2[1] + centr3[1]) / 3

print(abs(Px * 10_000), abs(Py * 10_000))
