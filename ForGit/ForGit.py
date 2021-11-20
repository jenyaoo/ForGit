import turtle
a=list(map(int,input().split()))
m=0
ind=0
turtle.speed(500)
for i in range(len(a)):
    if m<a[i]:
        ind=i
        m=a[i]
for i in range(len(a)):
    if i==ind:
        turtle.color(1,0,0)
        turtle.circle(a[i])
        turtle.color(1,1,1)
    else:
        turtle.circle(a[i])