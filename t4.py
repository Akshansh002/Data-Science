from turtle import *

speed('fastest')
pensize(2)
bgcolor('black')
pencolor('white')
side=6
for i in range(side):
    fd(100)
    for i in range(side):
        fd(50)
        lt(360/side)
    lt(360/side)
hideturtle()
mainloop()        
