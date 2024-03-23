import turtle 


#  Screen 
ws=turtle.Screen()

# Defining Turtle instance
t=turtle.Turtle()
t.color("Green")
t.width("2")
t.speed(2)

# Loop for making outside square 

for i in range(4):
	t.forward(300)
	t.left(90)


# square
t.penup()
t.goto(0,100)
t.pendown()

t.forward(300)

t.penup()
t.goto(0,200)
t.pendown()

t.forward(300)

t.penup()
t.goto(100,0)
t.pendown()

t.left(90)
t.forward(300)

t.penup()
t.goto(200,0)
t.pendown()


t.forward(300)
