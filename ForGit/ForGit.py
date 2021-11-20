import turtle
a=[0]*10
turtle.speed(5000)
for i in range(10):
    a[i]=int(input())
for i in range(10):
    turtle.circle(a[0])