with open(r'.\files\27_B_28766.txt') as file:
    dots = []
    stars = []
    for i in file:
        x, y, data = i.split()
        dots.append([float(x), float(y)])
        if data[0] == 'Z' and data[2:] == 'I':
            stars.append([float(x), float(y)])
