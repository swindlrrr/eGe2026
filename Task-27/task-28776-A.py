from math import dist


def center(cluster):
    res = []
    for dot in cluster:
        sum_dist = sum(dist(dot, d) for d in cluster)
        res.append([sum_dist, dot])
    return min(res)[1]


with open(r'.\files\27_A_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if data[0] == 'Y' and data[2:] == 'III':
            stars.append([float(x), float(y)])

cluster_1 = [d for d in dots if d[1] < 10]
cluster_2 = [d for d in dots if d[1] > 10]

center_1 = center(cluster_1)
center_2 = center(cluster_2)

A = []
for s in stars:
    A.append(dist(center_2, s))
print(min(A) * 10_000, max(A) * 10_000)
