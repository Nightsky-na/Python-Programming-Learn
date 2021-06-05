import turtle as t
import random as rd
# print(t.screensize()) # width = 300, height = 400

# Set up
def create():
    for i in range(4):
        tao.forward(100)
        tao.left(90)

tao = t.Turtle()
window = t.Screen()
color = [ 'red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
tao.pensize(4)
i = 0
for time in range(10):
    tao.color(color[i])
    i = i+1 if i<6 else 0
    tao.penup()
    tao.goto(rd.randint(-200,200),rd.randint(-150,150))
    tao.pendown()
    create()

window.exitonclick()
