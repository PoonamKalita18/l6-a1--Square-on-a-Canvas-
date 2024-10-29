import turtle
turtle.Screen().bgcolor("Pink")
p= turtle.Screen()
p.setup(400,500)
turtle.title("Hi! Welcome")
board= turtle.Turtle()

for x in range(4):
    board.forward(100)
    board.left(90)
    x=x+1
turtle.done()