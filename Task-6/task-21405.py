from turtle import *
screensize(5000,5000)
tracer(False)
m = 30
lt(90)

rt(30)
for i in range(30):
    rt(150)
    fd(6 * m)
    rt(30)
    fd(12 * m)
up()
for x in range(-10,10):
    for y in range(-20,10):
        goto(x * m, y * m)
        dot(3, "red")
update()
done()