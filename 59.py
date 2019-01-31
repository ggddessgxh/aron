import turtle

turtle.pensize()

turtle.pencolor("red")
a=45
primespeed= 1
for i in range(4):
   turtle.setheading(a)
   a+=90
   for k in range(2):                
        for j in range(60):
            if j < 30:
               primespeed += 0.5     
            else:
               primespeed -= 0.5     
            turtle.forward(primespeed)
            turtle.left(3)            
    
 
