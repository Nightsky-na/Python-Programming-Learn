# Turtle lib don't need to install 
import turtle
import random 
window = turtle.Screen()
tao = turtle.Turtle()
# tao.shape('turtle')
# tao.forward(100)
# tao.left(90)
# tao.forward(100)
# tao.left(90)
# tao.forward(100)
# tao.left(90)
# tao.forward(100)
# tao.left(90)
# tao.reset() # reset all 
# tao.goto(200,200)
# tao.pensize(2)
# tao.fd(50)
# tao.home()
color = ['red','blue','yellow','green']
tao.pensize(5)

for i in range(4):
    print(color[i])
    tao.color(color[i])
    tao.forward(100)
    tao.left(90)
    print(f"เต่าเดินครั้งที่{i+1}")

for i in range(10):
    c = random.choice(color);
    r = random.randint(50,100);
    print(r)
    tao.pencolor(c)
    # tao.circle(random.random()*10)
    tao.circle(r)
    tao.left(36)


window.exitonclick()
"""
for i in range(5):
    print('Hello{}'.format(i))

list(range(5))
for i in list(range(5)):
    print(i)

for i in ['Kon', 'Tita', 'Mam']:
    print(i)

for student in ['Kon', 'Tita', 'Mam']:
    print(student)
"""