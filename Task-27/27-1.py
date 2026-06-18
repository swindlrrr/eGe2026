from math import dist

def center(clus):
    ans = []
    for dot in clus:
        sum_dist = sum(dist(dot, d) for d in clus)
        ans.append([sum_dist, dot])
    return min(ans)[1]


with open(r'./Files/27_B_23284.txt') as file:
    dots = [list(map(float, i.replace(',', '.').split())) for i in file]

clus1 = [d for d in dots if d[0] > 5 and d[0] < 10]
clus2 = [d for d in dots if d[0] > 13 and d[0] < 19]
clus3 = [d for d in dots if d[0] > 20 and d[0] < 24]

centr1 = center(clus1)
centr2 = center(clus2)
centr3 = center(clus3)

P = dist(centr1, centr2)
Q = dist(centr1, centr3)
V = dist(centr2, centr3)
Q1 = min([P, Q, V])
Q2 = max([P, Q, V])
print(abs(Q1 * 10_000), abs(Q2 * 10_000))
