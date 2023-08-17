import turtle as t
win=t.Screen()
win.title("华强买瓜")
win.screensize(960,720)
turtle=t.Turtle()
t.tracer(0)
def juxing(x,y,chang,kuan):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(chang)
    turtle.right(90)
    turtle.forward(kuan)
    turtle.right(90)
    turtle.forward(chang)
    turtle.left(90)
def yuan (x,y,r):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.circle(r)

juxing(-410,-360,240,200)
juxing(-10,-360,240,200)
yuan(-110,)
t.update()


t.done()



#win.mainloop()

