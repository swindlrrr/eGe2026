from math import dist

def center(clus):
    res = []
    for dot in clus:
        sum_dist = sum(dist(dot,d) for d in clus)
        res.append([sum_dist,dot])
    return min(res)[1]



with open(r'./Files/27_A_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x,y,data = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if data == 'VII':
            stars.append([float(x), float(y)])

clus1 = [d for d in dots if d[1] > 8]
clus2 = [d for d in dots if d[1] < 8]

center1 = center(clus1)
center2 = center(clus2)

stars1 = [s for s in stars if s in clus1]
stars2 = [s for s in stars if s in clus2]

A = []
for s in stars1:
    A.append(dist(s,center1))
for s in stars2:
    A.append(dist(s,center2))
print(min(A) * 10_000,max(A) * 10_000)







