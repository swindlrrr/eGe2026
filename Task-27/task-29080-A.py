from math import dist


def center(clus):
    res = []
    for dot in clus:
        sum_dist = sum(dist(dot, d) for d in clus)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'./Files/27_A_29080.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if data[:2] == 'L3':
            stars.append([float(x), float(y)])

clus1 = [d for d in dots if d[1] > 8]
clus2 = [d for d in dots if d[1] < 8]

center1 = center(clus1)
center2 = center(clus2)

stars1 = [s for s in stars if s in clus1]
stars2 = [s for s in stars if s in clus2]

A1 = []
for s in stars:
    A1.append(dist(s, center1))
A2 = []
for s in stars:
    A2.append(dist(s, center2))
print(max(A1) * 10_000, max(A2) * 10_000)
