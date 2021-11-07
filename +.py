import turtle as t
import random as r

t.shape("turtle")
num=int(input("몇마리의 거북이?"))
for i in range(1,num+1):
    i = {}
    set[i]=t.Turtle()
turtles=list(set.values())

def go(t,y):
    t.penup()
    t.goto(-200,y)
    t.pendown()

trial=int(input("시도 횟수"))
for i in range(1,trial+1):
    a=r.randint(0, 9)
    print(a)
    if a>=4:
        t.forward(50)
for i in range(num):
    turtles[i].shape("turtle")
    go(turtles[i],100-200/(num-1)*i)
    for j in range(1, trial + 1):
        turtles[i].forward(10)

t.mainloop()