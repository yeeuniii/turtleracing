import turtle
import time

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()
t4 = turtle.Turtle()

def point(t,x,y):
    t.penup()
    t.goto(x, y)
    t.pendown()

t1.speed(0)
point(t1,0,-250)
t1.pensize(5)
t1.circle(250)
t1.shape("circle")

for i in range(0,360,6):
    point(t1, 0, 0)
    t1.setheading(60-i)
    t1.penup()
    if i%30==0:
        t1.fd(230)
        t1.write(int(i / 30 + 1),font=("Arial", 15, "normal"))
        t1.pendown()
        t1.pensize(2)
        t1.fd(20)
    else:
        t1.penup()
        t1.fd(240)
        t1.pendown()
        t1.fd(10)

point(t1, 0, 0)

def turnright2():
    t2.clear()
    t2.speed(0)
    point(t2,0, 0)
    t2.color("red")
    t2.rt(6)
    t2.fd(200)

def turnright3():
    if t2.heading()==90:
        t3.clear()
        t3.speed(0)
        point(t3,0,0)
        t3.rt(6)
        t3.fd(180)

def turnright4():
    if (t2.heading()==90) & (t3.heading()==90):
        t4.clear()
        t4.color("blue")
        t4.speed(0)
        point(t4,0,0)
        t4.rt(30)
        t4.fd(100)


tm=time.localtime(time.time())
t2.setheading(-tm.tm_sec*6+90)
t3.setheading(-tm.tm_min*6+90)
t4.setheading(-tm.tm_hour*30+90)
t4.pensize(2)

t2.color('red')
t2.fd(200)
t3.fd(180)
t4.color("blue")
t4.fd(100)

while True:
    turnright2()
    turnright3()
    turnright4()
    time.sleep(1)