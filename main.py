import turtle as t
import random as r

name = input("거북이 이름을 입력하시오.(이름은 쉼표(,)로 구분함)\n")
name = name.split(",")
turtlenum = len(name)
set = list()
for i in range(turtlenum):
    set.append({"name": name[i],"module": t.Turtle(), "number": i+1, "time": 0})

def go(t, y):
    t.penup()
    t.goto(-200, y)
    t.pendown()

trial = int(input("시도 횟수를 입력하시오\n"))
for i in set:
    i["module"].shape("turtle")
    go(i["module"], 150-300/turtlenum*(i["number"]-1))
    i["module"].write(i["name"])


for j in range(1, trial + 1):
    for i in set:
        a = r.randint(0, 9)
        if a >= 4:
            i["module"].forward(30)
            i["time"] = i["time"]+1

print(set)
win = [set[0]["time"]]
print(win)
for i in set:
    if win[0] < i["time"]:
        win[0] = i["time"]

for i in set:
    if win[0] == i["time"]:
        i["module"].write("Winner~", font=("", 15, "bold"))

t.mainloop()
