import turtle

t = turtle.Turtle()
def turtle_draw():


    count = 0 
    t.speed(200000)

    while count< 843:
        t.forward(70)
        t.left(150 + count/18)
        t.forward(70)
        t.forward(70)
        t.right(120 + count/18)
    
        count= count + 2
turtle_draw()
    

input()