from math import dist

def center(clus):
    res = []
    for dot in clus:
        sum_dist=sum(dist(dot,d) for d in clus)
        res.append([sum_dist,dot])
    return min(res)[1]

with open(r'./Files/27_B_29081.txt') as file:
    dots = []
    stars = []
    for i in file:
        x,y,data = i.replace(',', '.').split()
        dots.append([float(x), float(y)])
        if data != 'VII' and int(data[1]) >= 8:
            stars.append([float(x), float(y)])

clus1 = [d for d in dots if d[0]>21]
clus2 = [d for d in dots if d[0] < 21 and d[1] > 22]
clus3 = [d for d in dots if d[0]< 21 and d[1] < 22]

stars1 = [s for s in stars if s in clus1]
stars2 = [s for s in stars if s in clus2]
stars3 = [s for s in stars if s in clus3]

B1 = []
for s1 in stars1:
    for s2 in stars2:
        B1.append(dist(s1,s2))
for s2 in stars2:
    for s3 in stars3:
        B1.append(dist(s2,s3))
for s1 in stars1:
    for s3 in stars3:
        B1.append(dist(s1,s3))
print(min(B1) * 10_000)

B2 = []
for s1 in stars1:
    for s2 in stars2:
        if s1 != s2:
            B2.append(dist(s1,s2))
for s1 in stars2:
    for s2 in stars2:
        if s1 != s2:
            B2.append(dist(s1,s2))
for s1 in stars3:
    for s2 in stars3:
        if s1 != s2:
            B2.append(dist(s1,s2))
B2 = sum(B2) / len(B2)
print(B2 * 10_000)



