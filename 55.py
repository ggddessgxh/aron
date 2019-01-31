import turtle
turtle.screensize()
turtle.pensize()
turtle.pencolor("red")
turtle.speed(5)
for i in range(2):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.goto(100,100)
turtle.pendown()
for j in range(4):
    turtle.forward(85)
    turtle.right(90)
    
