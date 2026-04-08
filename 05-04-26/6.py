from turtle import *
screensize(5000,5000)
tracer(False)
m = 20
lt(90)

for i in range(4):
    fd(10*m)
    rt(270)
up()
fd(3*m)
rt(270)
fd(5*m)
rt(90)
down()
for i in range(2):
    fd(10*m)
    rt(270)
    fd(12*m)
    rt(270)
up()
for x in range(-10,-4):
    for y in range(3,11):
        goto(x*m,y*m)
        dot(3, 'red')
update()
done()
