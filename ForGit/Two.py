import turtle
turtle.speed(500)

def sq(a,b):
    if b!=0:    
        for i in range(4):
            turtle.forward(a)
            turtle.right(90)
    else: 
        return 0
    return(sq(a//2,b-1))

sq(100,4)