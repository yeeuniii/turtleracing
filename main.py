import turtle as t
import random as r

t.shape("turtle")

trial=int(input("시도 횟수"))
for i in range(1,trial+1):
    a=r.randint(0, 9)
    print(a)
    if a>=4:
        t.forward(50)

t.mainloop()



