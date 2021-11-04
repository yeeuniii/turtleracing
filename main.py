import turtle as t
import random as r


set={}
while True:
    name = input("거북이 이름을 입력하시오.")
    if name == "":
        break
    else:
        set[name] = t.Turtle()

turtlename=list(set.keys())
turtles=list(set.values())
turtlenum=len(set)

def go(t,y):
    t.penup()
    t.goto(-200,y)
    t.pendown()

trial=int(input("시도 횟수를 입력하시오"))
for i in range(turtlenum):
    turtles[i].shape("turtle")
    go(turtles[i],100-200/(turtlenum-1)*i)
    turtles[i].write(turtlename[i])
    for j in range(1, trial + 1):
        turtles[i].forward(10)

t.mainloop()



