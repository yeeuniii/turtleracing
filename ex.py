import turtle as t
import random as r

t1 = t.Turtle()
t2 = t.Turtle()

t1.shape("turtle")
t2.shape("turtle")

def go(t,x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

go(t1,-100,0)
go(t2,-100,50)

n=int(input("몇 번의 경주?"))
for i in range(n+1):
    a = r.randint(0, 9)
    b = r.randint(0, 9)
    if a > b:
        t1.fd(10)
    else:
        t2.fd(10)

t.mainloop()



