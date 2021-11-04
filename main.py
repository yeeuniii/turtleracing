import turtle as t
import random as r


set = {}
while True:
    name = input("거북이 이름을 입력하시오.")
    if name == "":
        break
    else:
        set[name] = t.Turtle()

turtlename = list(set.keys())
turtles = list(set.values())
turtlenum = len(set)

def go(t, y) :
    t.penup()
    t.goto(-200, y)
    t.pendown()

trial = int(input("시도 횟수를 입력하시오"))
for i in range(turtlenum):
    turtles[i].shape("turtle")
    go(turtles[i], 100-200/(turtlenum-1)*i)
    turtles[i].write(turtlename[i])
    s=0
    for j in range(1, trial + 1):
        a = r.randint(0, 9)
        if a >= 4:
            turtles[i].forward(10)
            s = s+1
    set[turtlename[i]+"time"] = s
print(set)

win=[set[turtlename[0]+"time"]]
for i in range(1,turtlenum):
    if win[0]<set[turtlename[i]+"time"]:
        win=[set[turtlename[i]+"time"]]
    if win[0]==set[turtlename[i]+"time"]:
        win.append(set[turtlename[i]+"time"])

for i in range(turtlenum):
    if win[0]==set[turtlename[i]+"time"]:
        turtles[i].write("Winner~")

t.mainloop()
