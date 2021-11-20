import turtle
turtle.speed(500)

def w(a,i):
    if i>0:
        w(a//2,i-1)
    else:
        turtle.forward(a)
    turtle.left(60)
    if i>0:
        w(a//2,i-1)
    else:
        turtle.forward(a)
    turtle.right(120)
    if i>0:
        w(a//2,i-1)
    else:
        turtle.forward(a)
    turtle.left(60)
    if i>0:
        w(a//2,i-1)
    else:
        turtle.forward(a)
a=int(input())
b=int(input())
w(a,b)
