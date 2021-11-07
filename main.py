import turtle as t
import random as r

name = input("거북이 이름을 입력하시오.(이름은 쉼표(,)로 구분함)")
name = name.split(",")
turtlenum = len(name)
set = list()
for i in range(turtlenum):
    set.append({"module": t.Turtle(), "number": i+1})

turtles = list()
for i in range(turtlenum):
    turtles.append(set[i]["module"])

def go(t, y):
    t.penup()
    t.goto(-200, y)
    t.pendown()

trial = int(input("시도 횟수를 입력하시오"))
for i in range(turtlenum):
    turtles[i].shape("turtle")
    go(turtles[i], 100-200/turtlenum*i)
    turtles[i].write(name[i])
    s = 0
    for j in range(1, trial + 1):
        a = r.randint(0, 9)
        if a >= 4:
            turtles[i].forward(30)
            s = s+1
    set[i]["time"] = s

win = [set[0]["time"]]
for i in range(1, turtlenum):
    if win[0] < set[i]["time"]:
        win = [set[i]["time"]]
    if win[0] == set[i]["time"]:
        win.append(set[i]["time"])

for i in range(turtlenum):
    if win[0] == set[i]["time"]:
        turtles[i].write("Winner~", font=("", 15, "bold"))

t.mainloop()
