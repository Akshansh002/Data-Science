from turtle import *

speed('fastest')
colors=['red','yellow','blue','green']
pensize(2)
for i in range (100):
    pencolor(colors[i%4])
    fd(i*2)
    lt(60)
    circle(i*2,60)

mainloop()