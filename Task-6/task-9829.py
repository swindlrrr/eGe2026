from turtle import *

screensize(5000, 5000)
tracer(False)
m = 20
lt(90)
rt(90)
for i in range(3):
    rt(45)
    fd(10 * m)
    rt(45)
rt(315)
fd(10 * m)
for i in range(2):
    rt(90)
    fd(10 * m)
up()
for x in range(-20, 8):
    for y in range(-15, 15):
        goto(x * m, y * m)
        dot(3,"red")
update()
done()
